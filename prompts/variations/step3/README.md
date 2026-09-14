# Step 3 variations (imagination lane)

Same loop as step 1 and step 2. NB (step 1) and L4 (step 2) fixed
upstream. Baseline for this step is v0.7's Step 2b (imagination).

## Design surface (from design-principles.md §"What to test next")

- **Register.** Baseline is measured prose describing sprawl. If
  principle 1 (embody the mode) holds, imagination's prompt should
  itself be strange or messy.
- **Concrete failure requirement.** Force a line that fails
  coherence/relevance/usefulness/on-topic-ness. Principle 8
  applied.
- **Downstream release framing.** Emphasize the imagination lane
  has no sort-and-select job. Filtering is the integrator's
  problem.
- **Drop or fold the "threads to set aside" line.** Same question
  as the lens's four-line footer (principle 11).

## Variations in this round

- `NB.md` — control. Baseline step 2b (v0.7 imagination) with NB
  + L4 upstream. Preamble is V5's per NB.
- `I1-embodied-register.md` — rewrite prompt in a messy,
  sprawling voice.
- `I2-concrete-failure.md` — require at least one line that fails
  coherence / relevance / usefulness / on-topic-ness.
- `I3-drop-threads-line.md` — remove the "threads to set aside"
  closing requirement.
- `I4-mess-is-contribution.md` — reframe filtering as
  integrator's problem; mess is the contribution, not a phase.
- `I-combo.md` — all four combined.

## Dispatch

Each variation runs once against the same material (Ash's
preferred-name question). Sonnet, same seed/settings as prior
rounds. Blind-rank via cold Sonnet reader on a design-critic
rubric for imagination-specific axes: sprawl, off-topicness,
concrete novelty, register match, downstream buildability.

Cost tracking per run.
