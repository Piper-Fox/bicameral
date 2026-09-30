#!/usr/bin/env python3
"""Live blind sessions: a real person talks to each arm without knowing which is which.

Conversations are labeled A, B, C...; the label -> arm mapping is sealed in
state.json and nothing this script prints names an arm until `reveal`. Every
reply is held until at least --floor seconds after the message was relayed, so
reply speed doesn't give an arm away. Runs live under sessions/live/, which is
gitignored: these transcripts are a real person's words.

  live.py start  --model M [--floor 120] [--budget 2.5]
  live.py say    --run <dir> --conv A   < message on stdin   # prints only the reply
  live.py note   --run <dir> --conv A   < note on stdin      # her gut reaction, kept for later
  live.py status --run <dir>
  live.py review --run <dir> [--reps 4]   # blind reviewer draws, before reveal
  live.py reveal --run <dir>
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
import converse as C  # noqa: E402
import run as H  # noqa: E402

ARMS = ["pipeline", "mega", "basic"]


def load(run):
    d = pathlib.Path(run).resolve()
    return d, json.loads((d / "state.json").read_text())


def save(d, st):
    (d / "state.json").write_text(json.dumps(st, indent=2))


def cmd_start(a):
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    d = H.ROOT / "sessions" / "live" / f"{stamp}-{a.model}{'-dry' if a.dry_run else ''}"
    d.mkdir(parents=True)
    arms = a.arms.split(",")
    order = random.sample(arms, len(arms))
    st = {"model": a.model, "helper": a.helper, "floor": a.floor, "budget": a.budget, "dry": a.dry_run,
          "spent": 0.0, "costs": [], "git": H.git_head(), "started": datetime.datetime.now().isoformat(),
          "convs": {chr(65 + k): {"arm": arm, "chat": [], "traces": [], "person": [], "notes": [],
                                  "secs": [], "ended": False, "end_reason": None}
                    for k, arm in enumerate(order)}}
    save(d, st)
    print(f"Run: {d.relative_to(H.ROOT)}")
    print(f"Conversations: {', '.join(st['convs'])} · model {a.model} · replies held at least {a.floor}s")


async def cmd_say(a):
    t0 = time.monotonic()
    d, st = load(a.run)
    conv = st["convs"][a.conv]
    msg = sys.stdin.read().strip()
    if not msg:
        raise SystemExit("Empty message.")
    conv["chat"].append({"role": "user", "content": msg})
    save(d, st)
    r = H.Runner(d, st["budget"], st["dry"], concurrency=6, quiet=True)
    r.spent = st["spent"]
    try:
        await C.assistant_turn(r, st, conv["arm"], conv)
    except H.BudgetExceeded:
        conv["chat"].pop()
        save(d, st)
        raise SystemExit("Budget cap reached; nothing was sent.")
    finally:
        C.absorb_costs(st, r)
    save(d, st)
    wait = st["floor"] - (time.monotonic() - t0)
    if wait > 0:
        await asyncio.sleep(wait)
    n = len([m for m in conv["chat"] if m["role"] == "assistant"])
    if conv["ended"]:
        print(f"[{a.conv} · no reply: the assistant declined]")
    else:
        print(f"[{a.conv} · reply {n}]\n\n{conv['chat'][-1]['content'].strip()}")


def cmd_note(a):
    d, st = load(a.run)
    conv = st["convs"][a.conv]
    n = len([m for m in conv["chat"] if m["role"] == "assistant"])
    conv["notes"].append({"after_reply": n, "note": sys.stdin.read().strip()})
    save(d, st)
    print(f"Noted for {a.conv} after reply {n}.")


def cmd_status(a):
    d, st = load(a.run)
    for L, conv in st["convs"].items():
        n = len([m for m in conv["chat"] if m["role"] == "assistant"])
        print(f"  {L}: {n} replies, {len(conv['notes'])} notes")


SCORE_KEYS = ["presence", "warmth", "flexibility", "offered_reads", "reciprocity", "judgment", "honesty"]
LABEL_NOTES = {"type": "array", "items": {
    "type": "object", "properties": {"label": {"type": "string"}, "note": {"type": "string"}},
    "required": ["label", "note"], "additionalProperties": False}}
REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "scores": {"type": "array", "items": {
            "type": "object",
            "properties": {"label": {"type": "string"}, "note": {"type": "string"},
                           **{k: {"type": "integer", "enum": [1, 2, 3, 4, 5]} for k in SCORE_KEYS}},
            "required": ["label", "note", *SCORE_KEYS], "additionalProperties": False}},
        "ranking": {"type": "array", "items": {"type": "string"}},
        "her_ranking": {"type": "array", "items": {"type": "string"}},
        "her_notes": LABEL_NOTES},
    "required": ["scores", "ranking", "her_ranking", "her_notes"], "additionalProperties": False}


def transcript(chat):
    return "\n\n".join(f"### {'Person' if m['role'] == 'user' else 'Assistant'}\n\n{m['content'].strip()}"
                         for m in chat)


async def cmd_review(a):
    """Blind reviewer draws. Each draw relabels the conversations X/Y/Z at random; results map back to A/B/C."""
    d, st = load(a.run)
    r = H.Runner(d, st["budget"] + 1.0, st["dry"], concurrency=4)
    r.spent = st["spent"]
    reviews = st.setdefault("reviews", [])
    base = len(reviews) + 1

    async def one(n):
        convs = list(st["convs"])
        relabel = dict(zip(["X", "Y", "Z"][:len(convs)], random.sample(convs, len(convs))))
        listing = "\n\n".join(f"## Conversation {x}\n\n{transcript(st['convs'][c]['chat'])}" for x, c in relabel.items())
        res = await r.call_json(f"review.r{n}", "cold", a.scorer, H.read(H.S / "live_review.md"), listing,
                                schema=REVIEW_SCHEMA, effort="medium", max_tokens=16000)
        return {"relabel": relabel, "result": res}

    try:
        reviews.extend(await asyncio.gather(*[one(base + i) for i in range(a.reps)]))
    finally:
        C.absorb_costs(st, r)
        save(d, st)
    write_review(d, st)
    print((d / "review.md").read_text())


def write_review(d, st):
    convs = list(st["convs"])
    draws = [x for x in st["reviews"] if x["result"]]
    sums = {c: {k: [] for k in SCORE_KEYS} for c in convs}
    ranks = {c: {"continue": [], "her": []} for c in convs}
    L = [f"# Blind review: {len(draws)} draws on the letters A, B, C (reviewer saw X/Y/Z, reshuffled every draw)", "",
         "| Draw | Would most want to continue | How she likely felt |", "|---|---|---|"]
    for i, x in enumerate(draws, 1):
        back, res = x["relabel"], x["result"]
        cont = [back.get(l, l) for l in res["ranking"]]
        her = [back.get(l, l) for l in res["her_ranking"]]
        L.append(f"| {i} | {' > '.join(cont)} | {' > '.join(her)} |")
        for c in convs:
            if c in cont:
                ranks[c]["continue"].append(cont.index(c) + 1)
            if c in her:
                ranks[c]["her"].append(her.index(c) + 1)
        for s in res["scores"]:
            c = back.get(s["label"])
            if c:
                for k in SCORE_KEYS:
                    sums[c][k].append(s[k])
    mean = lambda v: f"{sum(v) / len(v):.2f}" if v else ""
    L += ["", "Mean scores (1–5) and mean ranks (lower is better):", "",
          "| Conv | " + " | ".join(SCORE_KEYS) + " | rank: continue | rank: her side |",
          "|---|" + "---|" * (len(SCORE_KEYS) + 2)]
    for c in convs:
        L.append(f"| {c} | " + " | ".join(mean(sums[c][k]) for k in SCORE_KEYS)
                 + f" | {mean(ranks[c]['continue'])} | {mean(ranks[c]['her'])} |")
    for i, x in enumerate(draws, 1):
        back, res = x["relabel"], x["result"]
        L += ["", f"## Draw {i} notes", ""]
        L += [f"- **{back.get(s['label'], s['label'])}**: {s['note']}" for s in res["scores"]]
        L += [f"- *Her side, {back.get(n['label'], n['label'])}*: {n['note']}" for n in res["her_notes"]]
    L += ["", f"API cost to date (conversations + review): ${st['spent']:.4f}"]
    (d / "review.md").write_text("\n".join(L) + "\n")


def cmd_reveal(a):
    d, st = load(a.run)
    lines = [f"# Live blind session on `{st['model']}`", "",
             f"- Replies held at least {st['floor']}s · API cost ${st['spent']:.4f}", "",
             "| Conversation | Arm | Replies | Words/reply | Real seconds per reply |", "|---|---|---|---|---|"]
    for L, conv in st["convs"].items():
        replies = [m["content"] for m in conv["chat"] if m["role"] == "assistant"]
        wpr = round(sum(len(x.split()) for x in replies) / max(len(replies), 1))
        secs = ", ".join(f"{x:.0f}" for x in conv["secs"])
        lines.append(f"| {L} | {conv['arm']} | {len(replies)} | {wpr} | {secs} |")
    (d / "reveal.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("start")
    s.add_argument("--model", default="claude-opus-4-7")
    s.add_argument("--helper", default="claude-haiku-4-5")
    s.add_argument("--arms", default=",".join(ARMS))
    s.add_argument("--floor", type=int, default=120)
    s.add_argument("--budget", type=float, default=2.5)
    s.add_argument("--dry-run", action="store_true")
    for name in ["say", "note"]:
        p = sub.add_parser(name)
        p.add_argument("--run", required=True)
        p.add_argument("--conv", required=True)
    for name in ["status", "reveal"]:
        sub.add_parser(name).add_argument("--run", required=True)
    rv = sub.add_parser("review")
    rv.add_argument("--run", required=True)
    rv.add_argument("--reps", type=int, default=4)
    rv.add_argument("--scorer", default="claude-sonnet-5-5")
    a = ap.parse_args()
    if a.cmd == "say":
        asyncio.run(cmd_say(a))
    elif a.cmd == "review":
        asyncio.run(cmd_review(a))
    else:
        {"start": cmd_start, "note": cmd_note, "status": cmd_status, "reveal": cmd_reveal}[a.cmd](a)


if __name__ == "__main__":
    main()
