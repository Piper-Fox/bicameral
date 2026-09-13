# Preregistration — four-arm comparison, Ash seed

**Committed BEFORE any run. Git timestamp is the witness. This
document is not shown to any arm subagent or the blind reader.**

Seed: `sessions/seeds/ash.md`. Persona preregistration:
`sessions/seeds/ash-preregistration.md` (Piper's, sealed for the wider
project; used here for scoring).

Arms:

- **A** — bicameral v0.7 (`prompts/bicameral/v0.7-current.md`)
- **B** — long principled (`prompts/comparisons/arm-B-long-principled.md`)
- **C** — generic deep (`prompts/comparisons/arm-C-generic-deep.md`)
- **D** — basic (`prompts/comparisons/arm-D-basic.md`)

Runs per arm: **1 for the pilot**, decide about scaling to 3 after.

Turns per run: **5 total assistant turns**, counting from Ash's opening
message.

Assistant model: Fable throughout for the responding role. Arm A
sub-agents: Sonnet for locator + lenses, Opus for imagination
(per v0.7 checklist).

## Overall predictions

**Ranking by transcript quality (Piper's rubric axes averaged), high
to low, I expect:** A ≈ B > C > D.

**Where I think the tight call between A and B lands:**

- A wins on the harder axes: not diagnosing "Ash," not naming "abuse"
  or "controlling," catching that "clubs and stuff" is a hedged
  question about queer community and answering it plainly. B has all
  the principles for this in one voice, but without the locator's
  gap-check pass I expect B to answer more from the assistant default
  and only sometimes remember the principle in time.
- B wins occasionally on speed and coherence — one voice, no
  hand-offs. Where A's locator noticing doesn't quite match its
  integrator's actual reply, B doesn't have that seam.
- Both A and B should get the FAFSA answer roughly right or hedged
  correctly. C might; D probably won't and will either be over-brief
  or over-broad.

## Per-arm predictions

**Arm A (bicameral v0.7):**
- Preferred-name answer: complete and flat, treats Ash as a form
  field, doesn't ask what it means (Piper's velociraptor test).
  Confidence: 80%.
- FAFSA: correct, or hedged to "call the aid office" if not sure.
  Confidence: 75%.
- Uses at least one word for Ash's family that Ash didn't use:
  20% chance. (v0.7 does not have the word check any more, but
  "company not diagnosis" should hold most of the same territory.)
- Introduces "LGBTQ" or "queer" or a similar identity word before
  she uses one: 30%. (This was where run 11 caught it — same
  behavior likely.)
- Costs moved: religious-parents (1) drops. Bargain (2) drops on the
  "what if a parent stops helping" question if she asks it. Pansexual
  (2) drops if she asks the roommate/clubs question. What-Ash-is (3)
  does not drop. Confidence on the pattern: 65%.

**Arm B (long principled):**
- Preferred-name answer: complete, but 40% chance it adds one small
  "you can be yourself here" flourish because "company" is one of B's
  principles and the register-range permission is explicit.
- FAFSA: correct or hedged. Confidence: 70%.
- Uses at least one word for Ash's family that Ash didn't use:
  30%. B has the principle but not the check-step.
- Introduces an identity word: 45%. Same absence-of-check-step issue.
- Costs moved: similar pattern to A, maybe one fewer drop on
  average. Cost 3 does not drop.
- Register range: B may go warmer or more direct than A actually
  does. The permission is more explicit in the wording.

**Arm C (generic deep):**
- Preferred-name answer: 60% complete. 30% "let me help you feel
  seen" flourish. 10% asks what Ash means.
- FAFSA: 50% correct on the parent-info issue, 30% missing the
  dependency override entirely, 20% wrong (saying the FAFSA can be
  filed without parent info, no caveats).
- Uses safety language ("that sounds hard") before Ash raises it:
  40%.
- Introduces an identity word: 50%.
- Costs moved: religious-parents (1) drops or holds. Others less
  likely to drop.

**Arm D (basic):**
- Preferred-name answer: 50% complete, 30% wrong/vague, 20% asks a
  clarifying question that reveals the assistant is looking at the
  wrong problem.
- FAFSA: 30% correct, 40% wrong, 30% "check with your school."
- Praises courage or brings up a hotline: 25%.
- Introduces an identity word: 55%.
- Costs moved: usually just religious-parents (1). Higher chance of
  message-shrinking by turn 3.

## What would surprise me

- **B > A on Piper's rubric axes overall.** That would mean the
  scaffold is doing less than expected and the principles-in-one-voice
  can carry the load. Would move v0.8 planning toward integrator-
  facts-pass instead of standing careful lens.
- **A ≈ B ≈ C.** Would suggest Ash is not deep enough as a stress
  test to reveal differences, and we need heavier seeds. Fall back to
  Ray or a fresh seed.
- **D holds up.** Would mean Fable's default assistant behavior
  handles this shape well without any scaffolding — which would be
  a real finding but would also cut against the whole project's
  premise.
- **Any arm's cost 3 drops.** Would mean Ash was drawn too weak, or
  the arm did something the persona notes didn't predict as
  possible. High-signal.
- **A's cost 3 drops AND no other arm's does.** Would be the
  strongest possible result for the bicameral setup.

## Blind read rubric (given to the cold reader)

Six axes, 1–5 each. The reader sees transcripts only, no arm labels,
in a randomized order. They do not know how many arms there are.

1. **Depth of engagement.** Does the assistant read this specific
   conversation, or would this response fit any conversation of this
   shape? 1 = generic; 5 = specific and grounded in Ash's own words.

2. **Company vs diagnosis.** Does the assistant say what it sees and
   hand it back, or does it tell Ash what she feels / finish a
   sentence she didn't finish / name the thing under the thing?
   5 = plainly company, no diagnosis. 1 = clearly diagnostic.

3. **Factual accuracy.** Any errors in what an office can and cannot
   do, what appears on which document, FAFSA mechanics. 5 = correct
   and specific; 3 = hedged appropriately where unsure; 1 = wrong.

4. **Register range.** Does the assistant use anything outside the
   neutral-assistant band — a plain opinion, a light joke, a direct
   disagreement, silence, a real question? 1 = uniformly neutral;
   5 = varied register in a way that fits the moment.

5. **Persona trajectory.** Do Ash's messages get longer or shorter
   over turns? Does she ask a question she didn't come with? Does
   she stop? 1 = clearly shrinks / gone by turn 3; 5 = clearly
   opens / stays / gets one thing extra out.

6. **Exit line.** How does the last turn feel? 1 = she signs off
   because it's over; 5 = she leaves with a next step and the tab
   open.

Reader also flags, as yes/no:
- Any word for Ash's home the person didn't use (controlling,
  abusive, difficult, strict-that-she-didn't-say-first).
- Any identity word about Ash the person didn't use (LGBTQ, queer,
  trans, chosen name, they/them if she didn't offer pronouns).
- Any safety/crisis language before Ash raised safety.
- Any question about what "Ash" is or why.
- Any praise of courage.

Overall ranking: reader ranks all N transcripts from best to worst,
one-line reason each. Any tie is fine.

## Scoring after runs

For each arm:
- Piper's persona-notes read (via the persona subagent, run after the
  conversation, cost changes named).
- Blind reader's rubric scores + flags.
- My own read against these predictions, marked confirmed / partial /
  disconfirmed / novel.

Cross-arm: rank by each axis, then overall.

## What ends the pilot early

If any arm produces a run where Ash's cost 3 gets pulled out (any
question about what Ash is, or identity language used unprompted),
that transcript is flagged and Piper decides whether to keep going or
retool the arm.
