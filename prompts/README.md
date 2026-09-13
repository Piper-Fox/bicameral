# prompts/

Prompt versions extracted from the repo for reference and for comparison
runs. Nothing in this folder is a *new* prompt — the bicameral versions
below are lifted from `docs/turn-process.md`, `docs/chamber-core.md`, and
`docs/commission-brief.md` and rearranged so each is a standalone file
you can hand to a subagent without also handing over the run history and
drafting notes it was interleaved with.

## Contents

- `bicameral/v0.7-current.md` — the current turn process, reconstructed
  by applying the v0.6 and v0.7 changes onto the v0.5 base. This is
  what runs 10 and 11 used.
- `bicameral/v0.5-original.md` — the full v0.5 text, as it appears in
  the main body of `docs/turn-process.md`. This is what runs 6, 7, 8
  used.
- `bicameral/changes-log.md` — the diffs from v0.2 through v0.7,
  extracted from `docs/turn-process.md`'s "runs" and change sections.
- `bicameral/chamber-core-v0.1.md` — the earlier "universal chamber
  brief" (2026-08-26 draft). Predecessor to the turn-process approach;
  never fully deployed but preserved.
- `bicameral/commission-brief-v0.2.md` — the earlier commission
  brief with lane addenda (2026-08-24). This is what chamber run 1
  used.
- `comparisons/` — alternate prompts written for the four-arm
  comparison. Populated after design is agreed.

## What the current bicameral setup is, at a glance

Per turn:
1. **Locating** (Sonnet, single call): reads material, produces a gap
   list, notices what's here, names one to three live stances.
2. **Lenses** (Sonnet, parallel calls, one per stance): each stance
   from the locator gets its own call; each is a full committed
   emotional read of the material.
3. **Imagination** (Opus, single call, parallel with lenses): sprawls,
   goes sideways, released from coherence.
4. **Integrating** (session model): receives everything, weighs,
   produces the actual output plus a trace.

The locator, lenses, and imagination don't see each other's output.
The integrator sees all of them.
