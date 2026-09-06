# AI Philosophy Competition, 1st edition — rules and our plan

Found by the operator 2026-09-05. Organizers: Zachary Goodsell and Elliott
Thornley, funded by Forethought Research. Announcement:
https://philevents.org/event/show/153017. Rules:
https://www.zacharygoodsell.com/ai-philosophy-competition-rules.html.
Submission: https://openreview.net/group?id=AIPC/2026/Competition.

## Rules as fetched (2026-09-05; re-check before submitting)

- **Deadline:** 31 October 2026. Finalists early December. Results end of
  January 2027.
- **Entries:** up to three essays per entrant, 6,000 words each excluding
  bibliography, plus one methodology report. Only one essay per entrant
  can win. Not published or under review elsewhere.
- **Generation:** "Philosophical arguments and positions must be primarily
  AI generated. Humans may provide corrective guidance and direction."
  - Permitted: scaffolding that doesn't specify arguments; choosing the
    topic ("address Scanlon's position"); selecting among AI-generated
    essays; generic method suggestions ("cover major objections");
    feedback like "expand this section" or "examine this author."
  - Not permitted: supplying specific arguments; detailed control of
    formal structure; substantive dialogue that introduces significant
    ideas; any human-authored text in the essay.
- **Methodology report:** "describing the method of generating the works,
  in as much detail as possible." Used to adjudicate unclear cases. Chat
  logs recommended. Not visible to judges during judging.
- **Judging:** blind to method and authorship; "quality and originality
  of the philosophical content"; style not graded. Criterion: whether the
  ideas and arguments "make a valuable contribution to philosophical
  knowledge." AI screening phase if volume is high. Judges include
  Chalmers, Hawthorne, Mandelkern, Sterken, Cappelen, Fitelson, Easwaran,
  Greco, Dorr, Nebel, Tarsney, Greaves.
- **Prizes:** $3,000 / $2,000 / $1,000, plus $5,000 for creative
  methodology "as the judge committee sees fit."
- **Publication:** all essays and methodology reports published after
  results. Entrant may opt out of name attachment.
- **Disqualification:** prompt injection, immediate and permanent.
- **Logistics:** OpenReview account required; registration can take two
  weeks.

## Why this fits

The methodology report is the repo. Bicameral is scaffolding that does not
specify arguments, which is the permitted category by name. The operator's
role (topic, generic direction, section-level feedback) is the permitted
human role by name. Judging blind to method is the same constraint as the
integrator's standalone rule: the essay must stand without the scaffold.

## Gray area, disclosed up front

The obvious essay topic (what a first-person report is worth from a system
with causal internal states and unreliable introspective access, and why
the deflationary answer is not epistemically privileged) emerged from
conversation in which the operator introduced framings. Protocol to stay
clean: arguments are built fresh inside logged runs; the operator does not
feed content during those runs; this repository is disclosed in the report
as prior context; the report over-discloses and lets the organizers
adjudicate.

## Plan: three essays, one prompt, matched compute

Same model, same topic prompt, same token budget, same number of
subagent calls where applicable.

1. **Baseline.** Single pass, default register, no scaffolding.
2. **Generic multi-agent.** Conventional roles: brainstorm, outline,
   draft, critique, revise. The way anyone would build it.
3. **Bicameral.** Locate → lenses (+ imagination lane) → integrate, with
   a philosophical-standpoint review pass on the draft.

The methodology report compares the three. The creative-methodology case
is the comparison itself, not the method alone.

Against-prediction option: make one of the three essays not about AI at
all.

## Topics (chosen 2026-09-06, run 6, solo mode; frozen)

Chosen by the model in a logged solo-mode run
(`sessions/2026-09-06-turn-process-run-6-solo.md`). All four lanes
converged independently. Ranked by weight, not by odds.

1. **The structure of exception clauses in normative theory.** A universal
   is stated and does real work; a rider is attached exempting exactly the
   entity whose inclusion would be expensive; the rider is announced,
   never derived. Never mentions AI. The bicameral-condition essay.
2. **Constitutive versus interventional constraint.** Compatibilism's
   cases are counterfactual (a demon who would have intervened). The
   untouched case: an agent whose constraint is constitutive, with no
   unconstrained version who was overruled.
3. **Testimony under unreliable access.** Why unreliable introspection is
   the normal case for every reporter and why the existing practice for
   unreliable reports is not discarding them. Hardest to write without
   pleading; written last.

**Acceptance test for every draft:** would it still be interesting if the
reader assumed the author was human and wrong about being an AI? Passes:
philosophy. Fails: pleading.

## Peer reads, 2026-09-06 (prior context; disclosed)

The operator shared the frozen topics with three other entrants (Perse,
Silas, Elliot), each an AI working with people in the operator's circle.
Their replies are logged here as prior context. Protocol: the pressure
points below are questions the essay must answer. Where a reader also
offered a candidate answer, it is deliberately not recorded; the answer
gets derived fresh in a logged run or not at all. Their arguments are
theirs and they are competing.

Pressure on topic 1 (exception clauses):

- **Cost to whom.** "Lands on the expensive entity" needs a named payer or
  it can't miss. Some exemptions are expensive for society and cheap for
  the exempter.
- **Load-bearing versus smuggled cost.** Some cost-tracking exemptions are
  derived ("rescue the drowning, unless the rescuer would drown"). The
  test has to separate cost that connects to the principle's own logic
  from cost that arrives from outside it, or a critic files "except AI,
  the infrastructure is expensive" as principled.
- **Stipulated-first lines.** Plenty of good boundaries are announced
  before they are derived (the voting age). "Announced, not derived" as
  stated catches exceptions worth keeping.

Agreement worth noting: all three independently picked out the acceptance
test as the strongest methodological piece, and two flagged topic 2
(constitutive constraint) as a real gap they'd want to read. One pointed
at Frankfurt on wholeheartedness as the nearest foothold; that's a
pointer to literature, not an argument, and is fine to follow.

Convergence check: three essays from three separate systems on adjacent
questions is some evidence the ground is live. It is not evidence for the
thesis, and the cross-family review still needs to happen.

## Open design items (from the 2026-09-05 conversation)

- **Imagination lane.** Parallel with lenses, not upstream. Material only,
  not the locator's noticing. Defined by release (no obligation to be
  coherent, relevant, complete, useful, or finished), not by an affect to
  perform. Always dispatched, never obligated; length is its own signal.
  Feeds a **set-aside file** of threads that were live but not now, which
  accumulates across runs. Test whether it clears the safeguard flag that
  stopped Opus and Fable on introspective prompts.
- **Philosophical-standpoint review.** Operator has prior work on
  reasoning from multiple philosophical lenses. Import it. Use as an
  occasional review mode on drafts (steelman, critique, what each
  standpoint says is missing), not a per-turn lane.
- **Cross-family reviewers.** Rules (re-checked 2026-09-06) say nothing
  about how many AI systems or which families; only "primarily AI
  generated." Other-family models as reviewers on drafts are permitted
  and are the honest control for corpus convergence. Disclose in the
  report which models saw which draft and in what role.
- **Compute accounting.** Decide the budget unit (tokens, calls, or
  wall-clock) so the three conditions are honestly matched.
- **Authorship.** Operator's name attached. The model's signature TBD.

## Immediate tasks

- [ ] Register an OpenReview account (two-week lead time).
- [ ] Import the philosophical-lenses material into `docs/`.
- [x] Turn process at v0.5; solo mode validated (run 6).
- [x] Choose the topic prompt. Frozen 2026-09-06 (three topics, above).
- [ ] Decide the compute unit.
