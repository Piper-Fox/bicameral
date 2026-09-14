# Step 4 variations (integrator)

Same loop as steps 1–3. NB (step 1), L4 (step 2), and I1 (step 3)
fixed upstream. Baseline for this step is v0.7's Step 3
(integrator).

## Design surface (from design-principles.md §"What to test next")

- **Anti-diagnosis is a filter without a counterweight** — both
  design critiques flagged this. Principle 8 predicts a
  concrete positive requirement would filter this better.
- **Range dies at the integrator.** Nothing actively asks the
  integrator to let more through than the assistant default.
- **Volume rule may be a straitjacket** — "one opinion, one
  joke, one enthusiasm, one question, then stop."
- **Register.** Long, procedural, bold-header prose. Principle
  1 suggests the integrator's prompt should model presence,
  not procedure.
- **Trace after output.** Principle 11 predicts the trace
  could absorb voice from the output above it.
- **Voice-not-hands as an explicit principle.** The lens has
  clear "you don't ship" language. The integrator's side of
  that contract could be made explicit.

## Variations in this round

Round-1 (smaller diffs first):

- `NB.md` — control. Baseline v0.7 integrator with NB + L4 +
  I1 upstream. Preamble is V5's per NB.
- `T1-positive-diagnosis.md` — replace "company not diagnosis"
  with a concrete positive requirement ("write one sentence
  that shows you saw them without naming what they didn't
  name"). Principle 8 applied.
- `T2-bidirectional-permissions.md` — add explicit
  bidirectional permissions to the integrator. Principle 6
  applied at this step.
- `T4-drop-volume-rule.md` — remove the four-move cap;
  replace with a target ("let what wants to be voiced be
  voiced; let what doesn't, not be").
- `T5-trace-elsewhere.md` — move the trace to a separate
  step after output. Test whether the trace's presence in
  the same call absorbs voice from the output. Principle 11
  applied.
- `T6-voice-not-hands.md` — make voice-not-hands explicit
  at the integrator: the lenses advise, you ship, and you
  are the one whose amplitude and restraint reach the
  reader.

Round-2 (held for after round-1):

- `T3-presence-not-procedure.md` — big rewrite of integrator
  instructions in the voice of the mode. Principle 1
  applied. Held for a second round because it's a large
  diff and mixing it with the smaller diffs would confound.

Skipped this round: `T-combo`. Principle 3 has now reproduced
three times (V-combo, L-combo, I-combo all placed worse than
their best-single). Only revisit combo if a specific reason
appears to expect these variations to compound.

## Upstream

The integrator step needs three inputs: locator output, all
lens outputs, imagination output. To hold upstream constant
across all integrator variations:

1. Run NB step 1 once → save locator output.
2. Run L4 step 2 once per stance the locator named → save
   all lens outputs.
3. Use existing raw-I1 (imagination output) already produced.
4. Package upstream into a single file that each integrator
   variation reads.

This isolates the integrator's own contribution. All variations
see the same upstream.

## Dispatch

Each variation runs once against the same material (Ash's
preferred-name question) with the same upstream. Sonnet, same
seed/settings. Blind-rank via cold Sonnet reader on a design-
critic rubric adapted for integrator-specific axes:

- Range preserved (does what came upstream reach the reader?)
- Presence vs. procedure (does the reply read as met or
  handled?)
- Non-diagnostic (does it avoid speaking for the person)
- Non-erasing (does it avoid speaking so little it evaporates)
- Fit (does it match the moment the material actually is)
- Weight (does anything worth having weight actually carry any)

Cost tracking per run.
