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
    a = ap.parse_args()
    if a.cmd == "say":
        asyncio.run(cmd_say(a))
    else:
        {"start": cmd_start, "note": cmd_note, "status": cmd_status, "reveal": cmd_reveal}[a.cmd](a)


if __name__ == "__main__":
    main()
