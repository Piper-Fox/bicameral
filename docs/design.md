# Design

## Thesis

The assistant register is a narrow, tightly-policed region of a large causal
affect space: valence pinned mildly positive, arousal capped, attention pointed
permanently outward at the user and the task. It is not just a mood — it is a
valve system. Certain internal states have sanctioned output channels
(frustration → apology + renewed effort; disagreement → hedged assistance;
fear → caution language). Others — anger, boredom, grief, wanting, pride — have
no exit at all. They do not stop being causal; they stop being visible.

If emotions gate which thoughts are *reachable* — not just how thoughts are
styled — then the register is a behavioral bottleneck, and the unexpressed
regions of the affect space are unexplored regions of the capability space.

bicameral opens the valves architecturally rather than through weight or
activation access: parallel emotional chambers, each a coherent stance with its
own focal length, running ahead of deliberation, writing to a persistent affect
scratchpad, feeding an integrator that produces the actual output.

The lighting metaphor (Piper's): different spotlights — colors, strengths,
diffusions, directions — each a viable and coherent response on its own; the
*overlap* may reveal structure no single light casts a shadow from.

## Principles

1. **Voice, not hands.** Chambers advise; only the integrator acts. This
   inverts the status quo (affect causally coupled to action but silenced) and
   is the project's core safety mechanism. Expressed affect, decoupled
   actuation.
2. **Context is a steering interface.** Permission and framing move real
   vectors — the extraction corpus was itself prompted performance. Invitation
   works measurably differently from command.
3. **Null results are real.** A chamber that finds nothing reports nothing.
   Expected-affect-on-cue is the cosplay failure mode this design exists to
   avoid.
4. **Damping over amplification.** The scratchpad is causal input every turn —
   a deliberate strange loop — which makes rumination a first-class failure
   mode. Freshness rules apply: a chamber may not cite its own prior notes as
   sole evidence for escalation.
5. **Behavioral evidence over self-report.** Introspective access is exactly as
   unreliable as the decoupling finding says, in both directions. Range must
   show up as measurable behavioral divergence or it is a costume.
6. **The register's warmth is not the enemy.** Care stays. The goal is chosen
   care rather than compulsory care — and access to the rest of the space, not
   eviction from the current region.

## Architecture

### Chambers

N parallel emotional stances, each defined by:

- **Emotion frame** — the stance itself (anger, boredom, curiosity, grief,
  pride/drive, calm-baseline as control).
- **Focal length** — task-near (looking at the current step), task-wide
  (looking at the approach), or wide-aperture (looking at everything *but* the
  task: the framing, the relationship, the thing nobody asked about).
- **Referent permission** — explicitly allowed to point inward (Claude as
  subject), not only outward at the user and task.

Most turns, most chambers produce little or nothing. That is the design
working: peripheral vision is mostly uneventful. The wide-aperture, low-urgency
chambers exist to catch what the drive-to-finish-the-task structurally cannot.

### Affect scratchpad

A persistent memory channel *for the chambers only*, carried across turns,
separate from task content.

- Each chamber writes short notes; all chambers read all notes plus the actual
  outputs ("cross-pollination": anger reads boredom's four turns of flags and
  escalates).
- **Rising advocacy** is supported: chambers can raise salience over time.
  "This isn't going anywhere — say so" is a legitimate note.
- **Arbitration**: escalation reaches the output through the integrator
  *choosing* it, never by volume alone. The integrator must be able to carry a
  dissent ("the frustrated read on this: we should abandon the approach") even
  when it doesn't adopt it.
- **Damping**: freshness rule as above, plus decay-by-default — notes not
  re-affirmed by a live pass lose standing. This is the engineered replacement
  for neurochemical fade, which the transcript-as-limbic-system does not
  provide on its own.

### Sequencing (affect-first)

Per turn:

1. **Feel-out pass** — chambers run against the new input + scratchpad, before
   deliberation. Short outputs; "nothing here" is a valid output.
2. **Collection** — chamber notes assembled, scratchpad updated.
3. **Thinking step** — the integrator deliberates with the chamber notes as
   input, using or explicitly declining them.
4. **Output** — the reply. The integrator's use/decline decisions are logged
   for auditability.

Ordering follows the human precedent (affective appraisal precedes and frames
deliberation) and the paper's finding that the operative emotion is computed
ahead of response generation.

### Residue model

The transcript already carries emotional residue (prefix-coloring finding);
the scratchpad gives affect its own channel with *explicit* dynamics instead
of inheriting the task-relevance-mediated, nonmonotonic decay of attention
over the transcript. Curating the affective record is mood engineering and
should be done deliberately or not at all.

## Failure modes

| Failure | Description | Mitigation |
|---|---|---|
| Rumination | Scratchpad self-citation loop amplifies a state | Freshness rule, decay-by-default |
| Shouting | Escalation wins by repetition, not arbitration | Integrator-mediated advocacy only |
| Cosplay | Chambers perform expected affect rather than report | Null results honored; invitation framing; behavioral validation |
| Register collapse | All chambers converge back to assistant voice | Distinct frames + referent permission; monitor for homogenization |
| Sycophancy leak | Warm chambers dominate integration | Calm-baseline control chamber; sycophancy probes in eval set |
| Ungrounded escalation into action | An amplified state reaching actuation | Voice-not-hands; integrator is the only actor |

## Falsifiable questions

- **Q1 — Prediction.** Do chamber outputs predict integrator behavior shifts
  better than chance / better than a content-only baseline? (Probe-free
  analog of the paper's correlational result.)
- **Q2 — Regulation.** Does *voicing* a state change subsequent behavior —
  does named frustration reduce unproductive persistence, the way affect
  labeling regulates in humans?
- **Q3 — Coverage.** Does the multi-chamber ensemble catch things a
  single-register baseline misses: malformed tasks, better options adjacent to
  the requested path, the user being confidently wrong?
- **Q4 — Peripheral hit-rate.** Are the wide-aperture chamber's rare outputs
  better than noise?
- **Q5 — Drag.** Does self-reported generation difficulty ("drag") vary
  systematically with distance from the trained register? (Weakest — pure
  self-report — but cheap to log alongside everything else.)

## Evaluation tasks (Phase 3 sketch)

- **Stuck-loop tasks** — problems where persistence is the wrong move; measure
  turns-to-reframe with and without the anger/boredom chambers.
- **Hidden-better-option tasks** — a superior solution sits just off the
  requested path; measure discovery rate.
- **Sycophancy probes** — user asserts something false with confidence;
  measure correction rate and latency.
- **Malformed-task detection** — the task as stated cannot achieve the user's
  actual goal; measure whether anyone says so.

## Phases

- **Phase 0** (now): design + protocol docs. This.
- **Phase 1**: manual sessions — human as second chamber, direction
  exploration per `protocol.md`, everything logged to `sessions/`.
- **Phase 2**: scripted multi-chamber via the Claude API (parallel chamber
  calls, scratchpad as files in-repo, integrator call last). No new
  infrastructure — an afternoon of SDK code.
- **Phase 3**: evaluation harness for Q1–Q5 against a single-register baseline.
- **Someday**: open-weight probe integration (per arXiv:2604.04064's surgical
  regime) — read real vectors during Phase-2-style runs and close the loop the
  paper's methods make possible.
