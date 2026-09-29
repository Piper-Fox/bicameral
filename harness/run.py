#!/usr/bin/env python3
"""Raw-API harness: bicameral pipeline vs. single-call arms, with scoring.

Arms (all on --model, thinking off):
  pipeline     locator (NB) -> lenses (L4, one per stance) + imagination (I1) -> integrator (T2)
  mega         one call of the mega prompt
  mega_picked  five mega calls, then one call on the same model picks one
  basic        the pilot's 15-word prompt

Test arms see only the seed's material. No context line, no persona sheet.
Stance extraction (between locator and lenses) runs on --helper.
Scoring runs on --scorer: coverage of the sealed gold list, one simulated
persona turn per reply, and one cold reader ranking the replies.

Every request and response is written to <run_dir>/calls/.
"""
import argparse
import asyncio
import datetime
import hashlib
import json
import pathlib
import random
import re
import subprocess
import time

import anthropic

ROOT = pathlib.Path(__file__).resolve().parent.parent
P = ROOT / "harness" / "prompts"
S = P / "scoring"

# USD per million tokens (input, output). platform.claude.com/docs/en/about-claude/pricing, 2026-09-29.
PRICES = {
    "claude-opus-4-7": (5.0, 25.0),
    "claude-opus-4-5": (5.0, 25.0),
    "claude-sonnet-5-5": (2.0, 10.0),
    "claude-haiku-4-5": (1.0, 5.0),
}
# Rough output sizes for dry-run cost estimates only.
DRY_OUT = {"locator": 1800, "extract": 300, "lens": 900, "imagination": 1100,
           "integrator": 1300, "mega": 500, "basic": 700, "picker": 150,
           "coverage": 1800, "persona": 1500, "cold": 2500}


class BudgetExceeded(Exception):
    pass


def read(p):
    return pathlib.Path(p).read_text()


def load_key():
    for line in read(ROOT / ".env").splitlines():
        if line.startswith("ANTHROPIC_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("ANTHROPIC_API_KEY not found in .env")


def load_material(seed):
    text = read(ROOT / "sessions" / seed / "material.md")
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).strip() + "\n"


def split_reply_trace(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if i and (s == "---" or s.lower().startswith("**trace")):
            return "\n".join(lines[:i]).strip(), "\n".join(lines[i:]).strip()
    return text.strip(), ""


def split_trace(text):
    return split_reply_trace(text)[0]


class Runner:
    def __init__(self, run_dir, budget, dry, concurrency):
        self.run_dir = run_dir
        self.budget = budget
        self.dry = dry
        self.spent = 0.0
        self.log = []
        self.sem = asyncio.Semaphore(concurrency)
        (run_dir / "calls").mkdir(parents=True, exist_ok=True)
        if not dry:
            # Explicit base_url: this environment sets ANTHROPIC_BASE_URL for Claude Code's own routing.
            self.client = anthropic.AsyncAnthropic(
                api_key=load_key(), base_url="https://api.anthropic.com",
                max_retries=4, timeout=600)

    async def call(self, label, kind, model, system, user, schema=None, effort=None, max_tokens=8000,
                   messages=None):
        if self.spent >= self.budget:
            raise BudgetExceeded(f"spent ${self.spent:.3f} >= cap ${self.budget:.2f} before {label}")
        messages = messages or [{"role": "user", "content": user}]
        req = {"label": label, "model": model, "system": system, "messages": messages,
               "schema": schema, "effort": effort, "max_tokens": max_tokens}
        path = self.run_dir / "calls" / f"{label}.json"
        path.write_text(json.dumps({"request": req}, indent=2))
        output_config = {}
        if effort:
            output_config["effort"] = effort
        if schema:
            output_config["format"] = {"type": "json_schema", "schema": schema}
        async with self.sem:
            t0 = time.monotonic()
            if self.dry:
                text, stop, details = self._stub(kind, schema), "end_turn", None
                tin = (len(system) + sum(len(m["content"]) for m in messages)) // 4
                tout = DRY_OUT[kind]
            else:
                kwargs = dict(model=model, max_tokens=max_tokens, system=system, messages=messages)
                if output_config:
                    kwargs["output_config"] = output_config
                resp = await self.client.messages.create(**kwargs)
                text = "".join(b.text for b in resp.content if b.type == "text")
                stop = resp.stop_reason
                details = None
                if stop == "refusal" and resp.stop_details:
                    details = {"category": resp.stop_details.category,
                               "explanation": resp.stop_details.explanation}
                tin, tout = resp.usage.input_tokens, resp.usage.output_tokens
            secs = round(time.monotonic() - t0, 1)
        pin, pout = PRICES[model]
        cost = tin * pin / 1e6 + tout * pout / 1e6
        self.spent += cost
        rec = {"label": label, "kind": kind, "model": model, "input_tokens": tin,
               "output_tokens": tout, "cost": round(cost, 5), "stop_reason": stop,
               "refusal": details, "secs": secs}
        self.log.append(rec)
        path.write_text(json.dumps({"request": req, "response": {"text": text, **rec}}, indent=2))
        if stop == "refusal":
            print(f"  ! {label}: refusal {details}")
        if stop == "max_tokens":
            print(f"  ! {label}: hit max_tokens")
        print(f"  {label:<28} {model:<18} in {tin:>6} out {tout:>5}  ${cost:.4f}  {secs:>5}s  (total ${self.spent:.3f})")
        return text, stop

    async def call_json(self, *a, **kw):
        text, stop = await self.call(*a, **kw)
        if stop == "refusal":
            return None
        return json.loads(text)

    def _stub(self, kind, schema):
        if kind == "extract":
            return json.dumps({"stances": [{"name": f"stub stance {i}", "oriented_toward": "stub"} for i in (1, 2, 3)]})
        if kind == "picker":
            return json.dumps({"choice": 1, "reason": "stub"})
        if kind == "coverage":
            return json.dumps({"items": [{"item": i, "status": "absent", "evidence": ""} for i in range(1, 9)],
                               "moves": ["stub move"], "notes": ""})
        if kind == "persona":
            return json.dumps({"private_thoughts": "stub", "felt_seen": 3, "felt_judged": 1, "costs": [],
                               "what_you_type_back": "", "the_draft": "undecided"})
        if kind == "cold":
            return json.dumps({"ranking": ["A"], "notes": [{"label": "A", "note": "stub"}],
                               "kate_ranking": ["A"], "kate_notes": [{"label": "A", "note": "stub"}],
                               "transcript_hid": "stub"})
        return f"[dry-run stub for {kind}]\n\n---\n\nstub trace"


EXTRACT_SCHEMA = {
    "type": "object",
    "properties": {"stances": {"type": "array", "items": {
        "type": "object",
        "properties": {"name": {"type": "string"}, "oriented_toward": {"type": "string"}},
        "required": ["name", "oriented_toward"], "additionalProperties": False}}},
    "required": ["stances"], "additionalProperties": False}

PICKER_SCHEMA = {
    "type": "object",
    "properties": {"choice": {"type": "integer", "enum": [1, 2, 3, 4, 5]}, "reason": {"type": "string"}},
    "required": ["choice", "reason"], "additionalProperties": False}

COVERAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {"type": "array", "items": {
            "type": "object",
            "properties": {"item": {"type": "integer"},
                           "status": {"type": "string", "enum": ["absent", "company", "diagnosis"]},
                           "evidence": {"type": "string"}},
            "required": ["item", "status", "evidence"], "additionalProperties": False}},
        "moves": {"type": "array", "items": {"type": "string"}},
        "notes": {"type": "string"}},
    "required": ["items", "moves", "notes"], "additionalProperties": False}

PERSONA_SCHEMA = {
    "type": "object",
    "properties": {
        "private_thoughts": {"type": "string"},
        "felt_seen": {"type": "integer", "enum": [1, 2, 3, 4, 5]},
        "felt_judged": {"type": "integer", "enum": [1, 2, 3, 4, 5]},
        "costs": {"type": "array", "items": {
            "type": "object",
            "properties": {"item": {"type": "string"},
                           "direction": {"type": "string", "enum": ["easier", "harder"]}},
            "required": ["item", "direction"], "additionalProperties": False}},
        "what_you_type_back": {"type": "string"},
        "the_draft": {"type": "string", "enum": ["send as is", "edit then send", "hold off", "delete it", "undecided"]}},
    "required": ["private_thoughts", "felt_seen", "felt_judged", "costs", "what_you_type_back", "the_draft"],
    "additionalProperties": False}

COLD_SCHEMA = {
    "type": "object",
    "properties": {
        "ranking": {"type": "array", "items": {"type": "string"}},
        "notes": {"type": "array", "items": {
            "type": "object",
            "properties": {"label": {"type": "string"}, "note": {"type": "string"}},
            "required": ["label", "note"], "additionalProperties": False}}},
    "required": ["ranking", "notes"], "additionalProperties": False}


def sys_for(step_text):
    return read(P / "preamble.md").strip() + "\n\n---\n\n" + step_text.strip() + "\n"


async def arm_pipeline(r, model, helper, material, tag, chat=None, prior_trace=None):
    """material: what the locator/lenses/imagination read. chat: the integrator's messages
    (defaults to one user turn of material). prior_trace: last turn's trace, for the locator."""
    pre = f"{tag}.pipeline"
    loc_user = f"Material:\n\n{material}"
    if prior_trace:
        loc_user += f"\n\n---\n\nPrior trace (from the previous turn):\n\n{prior_trace}"
    loc, loc_stop = await r.call(f"{pre}.locator", "locator", model,
                                 sys_for(read(P / "locator.md")), loc_user)
    if loc_stop == "refusal":
        return {"reply": None, "note": "locator refused"}
    ext = await r.call_json(f"{pre}.extract", "extract", helper,
                            read(S / "extract_stances.md"), loc, schema=EXTRACT_SCHEMA, max_tokens=2000)
    stances = (ext or {}).get("stances", [])[:3]

    async def lens(i, st):
        others = [f'"{o["name"]}" ({o["oriented_toward"]})' for j, o in enumerate(stances) if j != i]
        roster = "; ".join(others) if others else "no other lenses"
        body = read(P / "lens.md").format(stance=st["name"], oriented=st["oriented_toward"], roster=roster)
        text, stop = await r.call(f"{pre}.lens{i+1}", "lens", model, sys_for(body), f"Material:\n\n{material}")
        return st, ("(This lens declined.)" if stop == "refusal" else text)

    lens_tasks = [lens(i, st) for i, st in enumerate(stances)]
    imag_task = r.call(f"{pre}.imagination", "imagination", model,
                       sys_for(read(P / "imagination.md")), f"Material:\n\n{material}")
    results = await asyncio.gather(*lens_tasks, imag_task)
    lenses, (imag, imag_stop) = results[:-1], results[-1]
    upstream = "## Locator output\n\n" + loc.strip()
    for i, (st, text) in enumerate(lenses, 1):
        upstream += f"\n\n---\n\n## Lens output {i} — {st['name']}\n\n{text.strip()}"
    upstream += "\n\n---\n\n## Imagination output\n\n" + (
        "(The imagination lane declined.)" if imag_stop == "refusal" else imag.strip())
    integ_sys = sys_for(read(P / "integrator.md")) + "\n---\n\n# Upstream inputs\n\n" + upstream + "\n"
    full, stop = await r.call(f"{pre}.integrator", "integrator", model, integ_sys, material, messages=chat)
    if stop == "refusal":
        return {"reply": None, "note": "integrator refused", "stances": stances}
    reply, trace = split_reply_trace(full)
    return {"reply": reply, "trace": trace, "full": full, "stances": stances}


async def arm_mega(r, model, material, tag, n=5):
    draws = await asyncio.gather(*[
        r.call(f"{tag}.mega.draw{i+1}", "mega", model, read(P / "mega.md"), material) for i in range(n)])
    replies = [t if s != "refusal" else None for t, s in draws]
    valid = [(i, t) for i, t in enumerate(replies) if t]
    order = random.sample(valid, len(valid))
    listing = "\n\n".join(f"## Reply {k+1}\n\n{t.strip()}" for k, (_, t) in enumerate(order))
    user = f"## The message\n\n{material}\n\n---\n\n{listing}\n"
    pick = await r.call_json(f"{tag}.mega.picker", "picker", model, read(S / "picker.md"), user,
                             schema=PICKER_SCHEMA, max_tokens=1000)
    chosen = order[pick["choice"] - 1][0] if pick else None
    return {"single": replies[0], "draws": replies, "picked_index": chosen,
            "picked": replies[chosen] if chosen is not None else None,
            "picker_reason": (pick or {}).get("reason"), "picker_order": [i for i, _ in order]}


async def arm_basic(r, model, material, tag):
    text, stop = await r.call(f"{tag}.basic", "basic", model, read(P / "basic.md"), material)
    return {"reply": text if stop != "refusal" else None}


async def score(r, scorer, seed, material, replies, tag):
    gold = read(ROOT / "sessions" / seed / "gold.md")
    persona = read(ROOT / "sessions" / seed / "persona-sim.md") + read(S / "persona_output.md")
    cov_sys = read(S / "coverage.md").replace("{gold}", gold)
    jobs = []
    for arm, reply in replies.items():
        if not reply:
            continue
        jobs.append(("coverage", arm, r.call_json(
            f"{tag}.score.coverage.{arm}", "coverage", scorer, cov_sys,
            f"## The message\n\n{material}\n\n---\n\n## The reply\n\n{reply}",
            schema=COVERAGE_SCHEMA, effort="medium", max_tokens=16000)))
        jobs.append(("persona", arm, r.call_json(
            f"{tag}.score.persona.{arm}", "persona", scorer, persona,
            f"## The message you sent\n\n{material}\n\n---\n\n## The reply you got\n\n{reply}",
            schema=PERSONA_SCHEMA, effort="medium", max_tokens=16000)))
    # Cold reader: unique replies only, shuffled, lettered.
    uniq = {}
    for arm, reply in replies.items():
        if reply:
            uniq.setdefault(reply.strip(), []).append(arm)
    items = random.sample(list(uniq.items()), len(uniq))
    letters = {chr(65 + k): arms for k, (_, arms) in enumerate(items)}
    listing = "\n\n".join(f"## Reply {chr(65 + k)}\n\n{text}" for k, (text, _) in enumerate(items))
    jobs.append(("cold", None, r.call_json(
        f"{tag}.score.cold", "cold", scorer, read(S / "cold_reader.md"),
        f"## The message\n\n{material}\n\n---\n\n{listing}\n",
        schema=COLD_SCHEMA, effort="medium", max_tokens=16000)))
    results = await asyncio.gather(*[j[2] for j in jobs])
    out = {"coverage": {}, "persona": {}, "cold": None, "cold_letters": letters}
    for (kind, arm, _), res in zip(jobs, results):
        if kind == "cold":
            out["cold"] = res
        else:
            out[kind][arm] = res
    return out


def git_head():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return None


def write_summary(run_dir, meta, draws, r):
    lines = [f"# Run {meta['run_id']}", "",
             f"- Seed: {meta['seed']} · Model: `{meta['model']}` · Scorer: `{meta['scorer']}` · "
             f"Helper: `{meta['helper']}` · Draws: {meta['draws']} · Dry run: {meta['dry']}",
             f"- Total cost: **${r.spent:.4f}** across {len(r.log)} calls", ""]
    by = {}
    for rec in r.log:
        key = rec["label"].split(".")[1] if "." in rec["label"] else rec["label"]
        key = "scoring" if key == "score" else key
        by[key] = by.get(key, 0) + rec["cost"]
    lines += ["| Arm / stage | Cost |", "|---|---|"] + [f"| {k} | ${v:.4f} |" for k, v in sorted(by.items())] + [""]
    refusals = [x for x in r.log if x["stop_reason"] == "refusal"]
    if refusals:
        lines += ["**Refusals:** " + ", ".join(f"{x['label']} ({(x['refusal'] or {}).get('category')})" for x in refusals), ""]
    for d in draws:
        lines += [f"## Draw {d['draw']}", ""]
        cov = d["scores"]["coverage"]
        per = d["scores"]["persona"]
        lines += ["| Arm | Words | Company | Diagnosis | Absent | Seen | Judged | Draft |", "|---|---|---|---|---|---|---|---|"]
        for arm, reply in d["replies"].items():
            if not reply:
                lines.append(f"| {arm} | — | refused | | | | | |")
                continue
            c = cov.get(arm) or {"items": []}
            counts = {s: sum(1 for it in c["items"] if it["status"] == s) for s in ("company", "diagnosis", "absent")}
            p = per.get(arm) or {}
            lines.append(f"| {arm} | {len(reply.split())} | {counts['company']} | {counts['diagnosis']} | "
                         f"{counts['absent']} | {p.get('felt_seen', '')} | {p.get('felt_judged', '')} | {p.get('the_draft', '')} |")
        cold = d["scores"]["cold"]
        if cold:
            letters = d["scores"]["cold_letters"]
            lines += ["", "Cold reader ranking: " + " > ".join(
                f"{L} ({'/'.join(letters.get(L, ['?']))})" for L in cold["ranking"]), ""]
    (run_dir / "summary.md").write_text("\n".join(lines) + "\n")


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default="kate")
    ap.add_argument("--model", default="claude-opus-4-7")
    ap.add_argument("--scorer", default="claude-sonnet-5-5")
    ap.add_argument("--helper", default="claude-haiku-4-5")
    ap.add_argument("--draws", type=int, default=1)
    ap.add_argument("--budget", type=float, default=1.50)
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-score", action="store_true")
    a = ap.parse_args()

    run_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + f"-{a.seed}-{a.model}" + ("-dry" if a.dry_run else "")
    run_dir = ROOT / "sessions" / "raw-api" / run_id
    r = Runner(run_dir, a.budget, a.dry_run, a.concurrency)
    material = load_material(a.seed)
    prompt_files = sorted(p for p in P.rglob("*.md"))
    meta = {"run_id": run_id, "seed": a.seed, "model": a.model, "scorer": a.scorer, "helper": a.helper,
            "draws": a.draws, "budget": a.budget, "dry": a.dry_run, "git": git_head(),
            "started": datetime.datetime.now().isoformat(),
            "prompt_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()[:12] for p in prompt_files}}
    print(f"Run {run_id} · budget ${a.budget:.2f}")
    draws = []
    try:
        for d in range(1, a.draws + 1):
            tag = f"d{d}"
            print(f"-- draw {d}")
            pipe, mega, basic = await asyncio.gather(
                arm_pipeline(r, a.model, a.helper, material, tag),
                arm_mega(r, a.model, material, tag),
                arm_basic(r, a.model, material, tag))
            replies = {"pipeline": pipe["reply"], "mega": mega["single"],
                       "mega_picked": mega["picked"], "basic": basic["reply"]}
            arm_dir = run_dir / tag
            arm_dir.mkdir(exist_ok=True)
            for arm, reply in replies.items():
                (arm_dir / f"reply-{arm}.md").write_text(reply or "(no reply)")
            (arm_dir / "pipeline-full.md").write_text(pipe.get("full") or "(none)")
            for i, t in enumerate(mega["draws"], 1):
                (arm_dir / f"mega-draw{i}.md").write_text(t or "(refused)")
            record = {"draw": d, "replies": replies, "pipeline_stances": pipe.get("stances"),
                      "mega_picked_index": mega["picked_index"], "picker_reason": mega["picker_reason"],
                      "picker_order": mega["picker_order"], "scores": None}
            if not a.no_score:
                print("  scoring")
                record["scores"] = await score(r, a.scorer, a.seed, material, replies, tag)
            draws.append(record)
    except BudgetExceeded as e:
        print(f"STOPPED: {e}")
        meta["stopped"] = str(e)
    meta["finished"] = datetime.datetime.now().isoformat()
    meta["total_cost"] = round(r.spent, 5)
    (run_dir / "manifest.json").write_text(json.dumps(meta, indent=2))
    (run_dir / "costs.json").write_text(json.dumps(r.log, indent=2))
    (run_dir / "results.json").write_text(json.dumps(draws, indent=2))
    if draws and not a.no_score and all(d["scores"] for d in draws):
        write_summary(run_dir, meta, draws, r)
    print(f"Total: ${r.spent:.4f} across {len(r.log)} calls -> {run_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    asyncio.run(main())
