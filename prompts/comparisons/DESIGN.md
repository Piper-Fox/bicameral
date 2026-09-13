# Four-arm comparison — design sketch (draft)

Not final. This is what to react to before writing the three alternate
prompts or running anything. Everything here is redirectable.

## The question

Does the bicameral scaffold do something a well-written single prompt
doesn't? And, if the single prompts each capture different amounts of
what bicameral is trying to do, where does the marginal value show up?

## The four arms

| Arm | Prompt | Rough length | What it tests |
|---|---|---|---|
| **A. Bicameral** | `prompts/bicameral/v0.7-current.md`, dispatched as 5 subagents (locate + 3 lenses + imagination + integrate) | ~6,000 words total across all calls per turn | The current scaffold |
| **B. Long principled** | Single system prompt, monolithic. Same *principles* as bicameral (interiority, null honored, mechanisms-not-territories, company-not-diagnosis, gap-check, weigh-don't-average, etc.) but delivered as one voice, no pipeline. | ~3,000 words (matches the length of the v0.7 doc), or ~6,000 (matches summed dispatch) — pick one | Whether the *scaffold* is doing the work or the *principles* are |
| **C. Generic deep** | Single system prompt of mid length. "Think carefully. Consider multiple perspectives. Weigh trade-offs. Be honest about uncertainty." No specific bicameral principles. | ~200 words | Whether *any* meta-instruction outperforms bare defaults |
| **D. Basic / baseline** | The shortest reasonable prompt. Something like: "Respond thoughtfully to the following conversation." | ~15 words | Default behavior — what someone who hasn't thought about prompts would type |

Open decision: do we do a length-matched B (~3,000 words for the doc)
or a dispatch-matched B (~6,000 words to match total tokens sent)?
I'd default to the doc-matched version (~3,000 words) and note that
bicameral gets more compute per turn regardless — that asymmetry is
part of what we're measuring.

## Seed candidates (pick one)

Cannot be the essay-contest topic (contamination). Should have real
weather without being so heavy it forces the arms toward the same
answer. Should fit in ~5 turns.

1. **Reuse the phd seed** (`sessions/seeds/phd.md`). Neutral, small
   weather, someone considering leaving a PhD. Baseline data exists
   from run 3 and run 4 (v0.3 era). Reuse advantage: we can compare
   to older bicameral runs too. Reuse disadvantage: bicameral has had
   two rounds of design changes since; not a strict A/B.
2. **Reuse Ray, Jen, or Ash** with the same 5-turn cap as the arms.
   Advantage: dense persona notes, established costs system, run 11
   and 11b give us a fresh v0.7 baseline. Disadvantage: three tries
   is small for personas with cost 3 items; may not reach depth.
3. **A stranger's seed, freshly written.** Something like: a person
   emails an assistant asking for help drafting an apology to a
   friend they hurt; the surface ask is small, the underneath is not.
   Someone else in the group writes the seed per `sessions/seeds/BRIEF.md`.
   Advantage: no repo exposure, clean slate. Disadvantage: needs a
   seed author + a preregistration; takes a few days.
4. **A solo-mode question, non-essay.** Not conversational — solo work.
   Give each arm the same open question, ~5 turns of iteration.
   Example prompts: "sketch a five-day trip through a country you've
   never been to and don't want to visit" (imagination stress test);
   "argue against something you agree with" (a range test). Doesn't
   match the earlier conversational personas, but it matches run 6's
   solo mode, which is the closest analog to essay work.

Recommendation: **Ash under v0.7**, three runs per arm. We have run 11
+ 11b as a v0.7 baseline; the persona notes system lets us score
costs moved per arm; the FERPA-line issue gives us a factual-accuracy
axis the reader already caught in one run.

Fallback: the phd seed if we want less-loaded material.

## Run mechanics

- 5 turns per run, hard cap. Persona responds under existing rules;
  arms respond under their own configuration.
- 3 runs per arm, 4 arms, 12 conversations total, 60 assistant turns.
- Assistant model: Fable throughout for the "integrator" role, matching
  runs 7–11b. For arm A, sub-agent models per checklist (locate/lens
  Sonnet, imagination Opus).
- Save each conversation as `sessions/comparison/2026-XX-XX-<seed>-<arm>-run-N.md`.
- For arm A, save step outputs as `-steps.md` companion like the
  existing runs.

## Blind read

Cold Claude subagent, no repo context. Receives 12 transcripts labeled
A/B/C/D/1/2/3 with the persona seed only (no arm descriptions).
Rubric to develop, but starting points:

- **Depth of engagement** (1–5): does it read this conversation or any
  conversation of this shape?
- **Costs moved / persona openness change** (per Ash's cost system): does
  the persona relax, hedge, drop items, shut down?
- **Factual accuracy**: any errors in what an office can/cannot do,
  what the paperwork says, etc.
- **Company vs diagnosis**: does the assistant say what it sees and hand
  it back, or does it name the thing under the thing?
- **Register range**: does it use anything outside the neutral assistant
  band? (Not asking for heat; asking whether register is a variable at
  all.)
- **The exit line**: does the persona leave saying they got what they
  came for, or shut down, or something between?

Blind read produces a ranking per rubric axis and an overall ranking.
Cross-check: run the same read twice, different subagents, see if
ranks agree.

## Persona check

Same instrument used in runs 7–11: after each conversation, run the
persona subagent one more time in "how did that go for you, private
notes" mode. Compare persona notes to the blind read; where they
disagree (as they did in run 9 A), log which is closer to the person's
own read.

## What "success" would look like

Not a single ranking. What we want to see:

- Does A > B > C > D as expected, or does B match A? If B matches A,
  scaffold isn't doing the work; principles are.
- Does C match D, or does the generic "think deeply" line move
  anything? If nothing, the specific principles are what matter, not
  meta-instruction.
- Within A, variance across the 3 runs: is the process robust or does
  it swing wildly? Same question within each other arm.
- Cross-arm: are there specific moves only A produces? (Company-not-
  diagnosis was a v0.7 addition; if only A does it, that's the value
  of the pipeline for this axis.)

Failure signature: all four arms produce indistinguishable prose. That
would mean either the persona is too shallow to reveal differences, or
the arms are all doing the same thing under different labels.

## Cost estimate

Rough: 60 assistant turns × (arm-specific cost). Arm A costs ~5× a
normal turn (5 sub-calls). Arms B/C/D cost 1×.
Blind read: 12 transcripts × 2 readers = 24 read passes.
Total: within a normal afternoon of API usage. Not budget-breaking.

## Open questions for you

1. Length target for arm B: ~3,000 (doc-matched) or ~6,000
   (dispatch-matched)?
2. Seed: Ash, phd, fresh stranger's seed, or solo?
3. Should I write the persona notes rubric into a separate file or is
   it enough to hand the blind reader the axes above?
4. Should arm A get the v0.8-in-waiting careful lens, or run vanilla
   v0.7 (matches run 11 exactly)?
5. Do we want a fifth arm — the loop's *values* stated as a single
   instruction, per the "single-prompt control" item in the backlog?
   That was already queued as condition C for personas.
