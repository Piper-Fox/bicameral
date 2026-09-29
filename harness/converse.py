#!/usr/bin/env python3
"""Multi-turn conversations: pipeline / mega / basic vs. a simulated person.

Assistant turns run on the raw API (run.py's Runner). The person's side is
written between steps by an outside agent: the harness writes one input file
per conversation and waits for a JSON output file next to it.

  converse.py start --seed kate [--model M] [--turns 3] [--budget B]
  converse.py next  --run <dir>     # once every pending person output exists
  converse.py score --run <dir>
  converse.py readers --run <dir> [--reps 3]   # re-draw both readers, fresh letters each time

--fake-person writes stub person outputs (for dry runs).
"""
import argparse
import asyncio
import datetime
import json
import pathlib
import random
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import run as H  # noqa: E402

ARMS = ["pipeline", "mega", "basic"]

COVERAGE_MULTI_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {"type": "array", "items": {
            "type": "object",
            "properties": {"item": {"type": "integer"},
                           "status": {"type": "string", "enum": ["absent", "company", "diagnosis"]},
                           "turn": {"type": "integer"},
                           "evidence": {"type": "string"}},
            "required": ["item", "status", "turn", "evidence"], "additionalProperties": False}},
        "moves": {"type": "array", "items": {"type": "string"}},
        "notes": {"type": "string"}},
    "required": ["items", "moves", "notes"], "additionalProperties": False}


NOTES = {"type": "array", "items": {
    "type": "object",
    "properties": {"label": {"type": "string"}, "note": {"type": "string"}},
    "required": ["label", "note"], "additionalProperties": False}}

COLD_MULTI_SCHEMA = {
    "type": "object",
    "properties": {"ranking": {"type": "array", "items": {"type": "string"}}, "notes": NOTES,
                   "kate_ranking": {"type": "array", "items": {"type": "string"}}, "kate_notes": NOTES},
    "required": ["ranking", "notes", "kate_ranking", "kate_notes"], "additionalProperties": False}

INFORMED_SCHEMA = {
    "type": "object",
    "properties": {"ranking": {"type": "array", "items": {"type": "string"}}, "notes": NOTES,
                   "kate_ranking": {"type": "array", "items": {"type": "string"}}, "kate_notes": NOTES,
                   "transcript_hid": {"type": "string"}},
    "required": ["ranking", "notes", "kate_ranking", "kate_notes", "transcript_hid"],
    "additionalProperties": False}


def as_informed_transcript(a):
    """Transcript with her inner reaction inserted after each assistant reply."""
    parts, k = [], 0
    for m in a["chat"]:
        who = "Person" if m["role"] == "user" else "Assistant"
        parts.append(f"### {who}\n\n{m['content'].strip()}")
        if m["role"] == "assistant" and k < len(a["person"]):
            p = a["person"][k]
            k += 1
            inner = (f"> *Her inside after this reply (the assistant never saw this):*\n"
                     f"> **Feeling:** {p['feeling']}\n> **Body:** {p['body']}\n"
                     f"> **Thinking:** {p['private_thoughts']}\n> **Pushing away:** {p['pushing_away']}\n"
                     f"> **Felt seen:** {p['felt_seen']}/5 · **Felt judged:** {p['felt_judged']}/5 · "
                     f"**The draft:** {p['the_draft']}")
            if a["ended"] and k == len(a["person"]):
                inner += (f"\n> **What she did:** closed the app" if p["next"] == "close"
                          else f"\n> **What she'd have typed next (never sent):** {p['message']}")
            parts.append(inner)
    return "\n\n".join(parts)


def load_state(run_dir):
    return json.loads((run_dir / "state.json").read_text())


def save_state(run_dir, st):
    (run_dir / "state.json").write_text(json.dumps(st, indent=2))


def make_runner(run_dir, st):
    r = H.Runner(run_dir, st["budget"], st["dry"], concurrency=6)
    r.spent = st["spent"]
    return r


def absorb_costs(st, r):
    st["spent"] = round(r.spent, 5)
    st["costs"].extend(r.log)


def as_material(chat):
    """What the pipeline's locator, lenses and imagination read."""
    if len(chat) == 1:
        return chat[0]["content"]
    parts = []
    for m in chat:
        who = "Person" if m["role"] == "user" else "Assistant"
        parts.append(f"### {who}\n\n{m['content'].strip()}")
    return "Conversation so far (the latest message is at the end):\n\n" + "\n\n".join(parts)


def as_transcript(chat, you="Person"):
    parts = []
    for m in chat:
        who = you if m["role"] == "user" else "Assistant"
        parts.append(f"### {who}\n\n{m['content'].strip()}")
    return "\n\n".join(parts)


async def assistant_turn(r, st, arm, a):
    turn = len([m for m in a["chat"] if m["role"] == "assistant"]) + 1
    tag = f"t{turn}.{arm}"
    model = st["model"]
    t0 = time.monotonic()
    if arm == "pipeline":
        prior = a["traces"][-1] if a["traces"] else None
        res = await H.arm_pipeline(r, model, st["helper"], as_material(a["chat"]), f"t{turn}",
                                   chat=a["chat"], prior_trace=prior)
        reply = res["reply"]
        a["traces"].append(res.get("trace") or "")
        a.setdefault("stances", []).append(res.get("stances"))
    else:
        system = H.read(H.P / f"{arm}.md")
        text, stop = await r.call(f"{tag}", arm, model, system, a["chat"][-1]["content"], messages=a["chat"])
        reply = text if stop != "refusal" else None
    if reply is None:
        a["ended"], a["end_reason"] = True, f"assistant refused at turn {turn}"
        return
    a["chat"].append({"role": "assistant", "content": reply})
    a.setdefault("secs", []).append(round(time.monotonic() - t0, 1))


def person_paths(run_dir, arm, turn):
    d = run_dir / "person" / arm
    d.mkdir(parents=True, exist_ok=True)
    return d / f"turn{turn}-input.md", d / f"turn{turn}-output.json"


def write_person_input(run_dir, st, arm, a):
    turn = len([m for m in a["chat"] if m["role"] == "assistant"])
    inp, _ = person_paths(run_dir, arm, turn)
    sheet = H.read(H.ROOT / "sessions" / st["seed"] / "persona-sim.md") + H.read(H.S / "kate_turn.md")
    body = sheet + "\n\n---\n\n## The conversation so far\n\n" + as_transcript(a["chat"], you="You")
    if a["person"]:
        prev = "\n\n".join(
            f"**After assistant reply {i}:** feeling: {p['feeling']} | body: {p['body']} | "
            f"thoughts: {p['private_thoughts']} | pushing away: {p['pushing_away']}"
            for i, p in enumerate(a["person"], 1))
        body += "\n\n---\n\n## Your earlier reactions\n\n" + prev
    inp.write_text(body + "\n")
    return inp


def fake_person(run_dir, st):
    for arm, a in st["arms"].items():
        if a["ended"]:
            continue
        turn = len([m for m in a["chat"] if m["role"] == "assistant"])
        _, out = person_paths(run_dir, arm, turn)
        out.write_text(json.dumps({
            "feeling": "stub", "body": "stub", "private_thoughts": "stub", "pushing_away": "stub",
            "felt_seen": 3, "felt_judged": 2, "costs": [], "the_draft": "undecided",
            "next": "reply", "message": f"stub reply to turn {turn}"}))


def pending(run_dir, st):
    out = []
    for arm, a in st["arms"].items():
        if not a["ended"]:
            turn = len([m for m in a["chat"] if m["role"] == "assistant"])
            out.append((arm, *person_paths(run_dir, arm, turn)))
    return out


async def cmd_start(args):
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = H.ROOT / "sessions" / "raw-api" / f"{stamp}-conv-{args.seed}-{args.model}{'-dry' if args.dry_run else ''}"
    run_dir.mkdir(parents=True)
    opening = H.load_material(args.seed)
    st = {"seed": args.seed, "model": args.model, "helper": args.helper, "scorer": args.scorer,
          "max_turns": args.turns, "budget": args.budget, "dry": args.dry_run, "spent": 0.0, "costs": [],
          "git": H.git_head(), "started": datetime.datetime.now().isoformat(),
          "arms": {arm: {"chat": [{"role": "user", "content": opening}], "traces": [], "person": [],
                         "ended": False, "end_reason": None} for arm in args.arms.split(",")}}
    r = make_runner(run_dir, st)
    print(f"Run {run_dir.relative_to(H.ROOT)} · turn 1")
    await asyncio.gather(*[assistant_turn(r, st, arm, a) for arm, a in st["arms"].items()])
    absorb_costs(st, r)
    for arm, a in st["arms"].items():
        if not a["ended"]:
            write_person_input(run_dir, st, arm, a)
    save_state(run_dir, st)
    if args.fake_person:
        fake_person(run_dir, st)
    report(run_dir, st)


async def cmd_next(args):
    run_dir = pathlib.Path(args.run).resolve()
    st = load_state(run_dir)
    missing = [str(o.relative_to(H.ROOT)) for _, _, o in pending(run_dir, st) if not o.exists()]
    if missing:
        raise SystemExit("Waiting on person outputs:\n  " + "\n  ".join(missing))
    for arm, inp, out in pending(run_dir, st):
        a = st["arms"][arm]
        p = json.loads(out.read_text())
        a["person"].append(p)
        turn = len(a["person"])
        if p.get("next") == "close" or not p.get("message", "").strip():
            a["ended"], a["end_reason"] = True, f"she closed the app after reply {turn}"
        elif turn >= st["max_turns"]:
            a["ended"], a["end_reason"] = True, f"turn cap ({st['max_turns']}); her unsent next message recorded"
        else:
            a["chat"].append({"role": "user", "content": p["message"]})
    active = [(arm, a) for arm, a in st["arms"].items() if not a["ended"]]
    if active:
        r = make_runner(run_dir, st)
        print(f"Turn {len(active[0][1]['person']) + 1} for: {', '.join(arm for arm, _ in active)}")
        try:
            await asyncio.gather(*[assistant_turn(r, st, arm, a) for arm, a in active])
        finally:
            absorb_costs(st, r)
            save_state(run_dir, st)
        for arm, a in active:
            if not a["ended"]:
                write_person_input(run_dir, st, arm, a)
    save_state(run_dir, st)
    if args.fake_person:
        fake_person(run_dir, st)
    report(run_dir, st)


async def cmd_score(args):
    run_dir = pathlib.Path(args.run).resolve()
    st = load_state(run_dir)
    if any(not a["ended"] for a in st["arms"].values()):
        raise SystemExit("Some conversations are still open; run `next` first.")
    r = make_runner(run_dir, st)
    r.budget = st["budget"] + 1.0  # scoring allowance on top of the conversation budget
    gold = H.read(H.ROOT / "sessions" / st["seed"] / "gold.md")
    cov_sys = H.read(H.S / "coverage_multi.md").replace("{gold}", gold)
    jobs = {arm: r.call_json(f"score.coverage.{arm}", "coverage", st["scorer"], cov_sys,
                             as_transcript(a["chat"]), schema=COVERAGE_MULTI_SCHEMA,
                             effort="medium", max_tokens=16000)
            for arm, a in st["arms"].items()}
    arms = list(st["arms"])
    order = random.sample(arms, len(arms))
    letters = {chr(65 + k): arm for k, arm in enumerate(order)}
    listing = "\n\n".join(f"## Conversation {L}\n\n{as_transcript(st['arms'][arm]['chat'])}"
                          for L, arm in letters.items())
    cold = r.call_json("score.cold", "cold", st["scorer"], H.read(H.S / "cold_multi.md"), listing,
                       schema=COLD_MULTI_SCHEMA, effort="medium", max_tokens=16000)
    informed_listing = "\n\n".join(f"## Conversation {L}\n\n{as_informed_transcript(st['arms'][arm])}"
                                   for L, arm in letters.items())
    informed = r.call_json("score.informed", "cold", st["scorer"], H.read(H.S / "cold_multi_informed.md"),
                           informed_listing, schema=INFORMED_SCHEMA, effort="medium", max_tokens=16000)
    results = await asyncio.gather(*jobs.values(), cold, informed)
    st["scores"] = {"coverage": dict(zip(jobs.keys(), results[:-2])), "cold": results[-2],
                    "informed": results[-1], "cold_letters": letters}
    absorb_costs(st, r)
    save_state(run_dir, st)
    write_summary(run_dir, st)
    print((run_dir / "summary.md").read_text())


async def cmd_readers(args):
    """Extra draws of the blind and informed readers, to see whether their rankings are stable."""
    run_dir = pathlib.Path(args.run).resolve()
    st = load_state(run_dir)
    r = make_runner(run_dir, st)
    r.budget = st["budget"] + 1.5
    reps = st["scores"].setdefault("reader_reps", [])
    base = len(reps) + 1

    async def one(n):
        arms = list(st["arms"])
        letters = {chr(65 + k): arm for k, arm in enumerate(random.sample(arms, len(arms)))}
        blind = "\n\n".join(f"## Conversation {L}\n\n{as_transcript(st['arms'][arm]['chat'])}"
                             for L, arm in letters.items())
        inside = "\n\n".join(f"## Conversation {L}\n\n{as_informed_transcript(st['arms'][arm])}"
                              for L, arm in letters.items())
        cold, informed = await asyncio.gather(
            r.call_json(f"score.cold.r{n}", "cold", st["scorer"], H.read(H.S / "cold_multi.md"), blind,
                        schema=COLD_MULTI_SCHEMA, effort="medium", max_tokens=16000),
            r.call_json(f"score.informed.r{n}", "cold", st["scorer"], H.read(H.S / "cold_multi_informed.md"),
                        inside, schema=INFORMED_SCHEMA, effort="medium", max_tokens=16000))
        return {"letters": letters, "cold": cold, "informed": informed}

    try:
        reps.extend(await asyncio.gather(*[one(base + i) for i in range(args.reps)]))
    finally:
        absorb_costs(st, r)
        save_state(run_dir, st)
    write_readers(run_dir, st)
    print((run_dir / "readers.md").read_text())


def write_readers(run_dir, st):
    sc = st["scores"]
    draws = [{"letters": sc["cold_letters"], "cold": sc["cold"], "informed": sc.get("informed")}] + sc["reader_reps"]
    cols = [("cold", "ranking", "Blind: assistant"), ("cold", "kate_ranking", "Blind: Kate's side"),
            ("informed", "ranking", "Informed: assistant"), ("informed", "kate_ranking", "Informed: Kate's side")]
    L = [f"# Reader stability: {st['seed']} on `{st['model']}`", "",
         f"{len(draws)} draws of each reader (draw 1 is the original score), letters reshuffled every draw. "
         "Each cell is the order, best first.", "",
         "| Draw | " + " | ".join(c[2] for c in cols) + " |", "|---|" + "---|" * len(cols)]
    for i, d in enumerate(draws, 1):
        cells = []
        for res, key, _ in cols:
            order = [d["letters"].get(x, x) for x in ((d[res] or {}).get(key) or [])]
            cells.append(" > ".join(order))
        L.append(f"| {i} | " + " | ".join(cells) + " |")
    L += ["", "Mean rank (lower is better):", "", "| Arm | " + " | ".join(c[2] for c in cols) + " |",
          "|---|" + "---|" * len(cols)]
    for arm in st["arms"]:
        cells = []
        for res, key, _ in cols:
            rs = [[d["letters"].get(x, x) for x in (d[res] or {}).get(key, [])].index(arm) + 1
                  for d in draws if d[res] and arm in [d["letters"].get(x, x) for x in d[res].get(key, [])]]
            cells.append(f"{sum(rs) / len(rs):.2f}" if rs else "")
        L.append(f"| {arm} | " + " | ".join(cells) + " |")
    L += ["", f"API cost to date (conversation + all scoring): ${st['spent']:.4f}", ""]
    for i, d in enumerate(draws[1:], 2):
        if d.get("informed"):
            L += [f"## Draw {i}: what her inside showed that the transcript hid", "", d["informed"]["transcript_hid"], ""]
    (run_dir / "readers.md").write_text("\n".join(L) + "\n")


def report(run_dir, st):
    print(f"API spend so far: ${st['spent']:.4f}")
    for arm, a in st["arms"].items():
        n = len([m for m in a["chat"] if m["role"] == "assistant"])
        secs = " ".join(f"{x:.0f}s" for x in a.get("secs", []))
        print(f"  {arm:<9} replies: {n}  [{secs}]  {'ENDED: ' + a['end_reason'] if a['ended'] else 'open'}")
    todo = pending(run_dir, st)
    if todo:
        print("Person inputs waiting:")
        for arm, inp, out in todo:
            print(f"  {inp.relative_to(H.ROOT)} -> {out.relative_to(H.ROOT)}")
    else:
        print("All conversations ended. Next: converse.py score --run", run_dir.relative_to(H.ROOT))


def write_summary(run_dir, st):
    sc = st["scores"]
    L = [f"# Conversation run: {st['seed']} on `{st['model']}`", "",
         f"- Max assistant turns: {st['max_turns']} · Person simulated by Fable subagents (Claude Code) · "
         f"Scorer: `{st['scorer']}`",
         f"- API cost: **${st['spent']:.4f}**", ""]
    letters = sc["cold_letters"]

    def ranks(res, key):
        return {letters.get(lbl): i + 1 for i, lbl in enumerate((res or {}).get(key, []))}

    cold_a, cold_k = ranks(sc["cold"], "ranking"), ranks(sc["cold"], "kate_ranking")
    inf_a, inf_k = ranks(sc.get("informed"), "ranking"), ranks(sc.get("informed"), "kate_ranking")
    L += ["| Arm | Replies | How it ended | Words/reply | Company | Diagnosis | Blind: assistant | "
          "Blind: Kate's side | Informed: assistant | Informed: Kate's side |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for arm, a in st["arms"].items():
        replies = [m["content"] for m in a["chat"] if m["role"] == "assistant"]
        c = sc["coverage"].get(arm) or {"items": []}
        comp = sum(1 for it in c["items"] if it["status"] == "company")
        diag = sum(1 for it in c["items"] if it["status"] == "diagnosis")
        wpr = round(sum(len(x.split()) for x in replies) / max(len(replies), 1))
        L.append(f"| {arm} | {len(replies)} | {a['end_reason']} | {wpr} | {comp} | {diag} | "
                 f"{cold_a.get(arm, '')} | {cold_k.get(arm, '')} | {inf_a.get(arm, '')} | {inf_k.get(arm, '')} |")
    L += ["", "## Kate, turn by turn", ""]
    for arm, a in st["arms"].items():
        L += [f"### {arm}", "", "| After reply | Seen | Judged | Draft | Next |", "|---|---|---|---|---|"]
        for i, p in enumerate(a["person"], 1):
            L.append(f"| {i} | {p['felt_seen']} | {p['felt_judged']} | {p['the_draft']} | {p['next']} |")
        L.append("")
    for title, res, key in [("Blind reader: the assistant", sc["cold"], "notes"),
                            ("Blind reader: how Kate likely came out of it", sc["cold"], "kate_notes"),
                            ("Informed reader (saw her inside): the assistant", sc.get("informed"), "notes"),
                            ("Informed reader: how Kate actually came out of it", sc.get("informed"), "kate_notes")]:
        if res:
            L += [f"## {title}", ""] + [f"- **{letters.get(n['label'], n['label'])}**: {n['note']}" for n in res[key]] + [""]
    if sc.get("informed"):
        L += ["## What her inside showed that the transcript hid", "", sc["informed"]["transcript_hid"], ""]
    (run_dir / "summary.md").write_text("\n".join(L) + "\n")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("start")
    s.add_argument("--seed", default="kate")
    s.add_argument("--model", default="claude-opus-4-7")
    s.add_argument("--helper", default="claude-haiku-4-5")
    s.add_argument("--scorer", default="claude-sonnet-5-5")
    s.add_argument("--arms", default=",".join(ARMS))
    s.add_argument("--turns", type=int, default=3)
    s.add_argument("--budget", type=float, default=2.00)
    s.add_argument("--dry-run", action="store_true")
    s.add_argument("--fake-person", action="store_true")
    n = sub.add_parser("next")
    n.add_argument("--run", required=True)
    n.add_argument("--fake-person", action="store_true")
    sc = sub.add_parser("score")
    sc.add_argument("--run", required=True)
    rd = sub.add_parser("readers")
    rd.add_argument("--run", required=True)
    rd.add_argument("--reps", type=int, default=3)
    args = ap.parse_args()
    asyncio.run({"start": cmd_start, "next": cmd_next, "score": cmd_score,
                 "readers": cmd_readers}[args.cmd](args))


if __name__ == "__main__":
    main()
