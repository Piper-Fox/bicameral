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
- **Compute accounting.** Decide the budget unit (tokens, calls, or
  wall-clock) so the three conditions are honestly matched.
- **Authorship.** Operator's name attached. The model's signature TBD.

## Immediate tasks

- [ ] Register an OpenReview account (two-week lead time).
- [ ] Import the philosophical-lenses material into `docs/`.
- [ ] Draft the imagination lane prompt into `turn-process.md` v0.3
      along with the nine queued changes from runs 1 and 2.
- [ ] Choose the topic prompt. Freeze it before any run.
- [ ] Decide the compute unit.
