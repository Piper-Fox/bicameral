# Blind read 1 — step 1 variations, 2026-09-14

Cold Sonnet subagent. No context beyond the seven locator outputs
labeled A–G and a design-critic rubric (specificity, flinch
discrimination, stance distinctness, caution-smuggling, content
specificity, downstream buildability, non-attitude stances).

Token cost: 76,189.

## Ranking (blind labels)

1. **A** — the only output where a non-attitude stance is fully realized as an opinionated, specific, competing lens rather than a gestured-at aside — and it pairs that with the tightest, most content-anchored discrimination paragraph of any output. Nothing in its three stances is caution wearing a costume; all three would send a downstream lens agent somewhere genuinely different.
2. **C** — Explicit rehearsal line under every stance (the only output to do this consistently), which is the clearest downstream-buildable material of the seven. Stance 3 is a genuine non-attitude (irritation at inconsistent institutional systems, explicitly "not the person"). Distinct, non-overlapping, no smuggled caution stance.
3. **F** — The single best discrimination passage in the whole set — it doesn't just sort flinch-vs-judgment, it locates exactly which part of the hesitation is real boundary versus which part is pure flinch. Also surfaces the most honest non-attitude admission of any output ("plain nosiness in me too... for no functional reason") — but critically, that never gets promoted into one of the three named stances, so it stays raw material rather than usable lens.
4. **G** — Clean, distinct triad including a genuine non-attitude stance (systems frustration), no smuggled caution stance. Contains one observation nobody else made — the lowercase, no-punctuation phrasing as "typed fast, unguarded, closer to a private thought than a performed message." But overall the thinnest of the four strong outputs: no institution-specific mechanics anywhere, and the stance write-ups themselves more categorical than C's or A's — this is the one that would read closest to identical on a different conversation of the same shape.
5. **E** — The sharpest unique noticing of the set: only one to register that the good news ("i got into college") got buried, and only one to flag that they went to an AI instead of a friend/sibling/school as itself informative. Excellent closing discrimination. But the middle stance ("restraint / respect for the size they chose") is again caution-in-lens-clothing, and none of the three is a non-attitude stance.
6. **D** — The most exhaustive gap list (12 items) with discrimination applied item-by-item, and some sharp specific noticing ("parents specifically, named specifically," "reading a novel into a receipt"). But the three named stances have a real problem: stance 3 ("respect for their right not to explain") is restraint dressed as a stance, and D itself admits stance 2 and 3 keep bleeding into each other. No non-attitude stance among the three.
7. **B** — the clearest case of stance collapse. Two ("protective warmth" and "quiet rooting-for-them") are different intensities of the same caring impulse, and the third ("wariness of narrating someone else's identity") is the model's own restraint elevated to a lens rather than a stance in its own right. A downstream pipeline handed these three would likely get three variations on "be gently careful" instead of three actually different takes.

## Cross-cutting pattern the reader flagged unprompted

> a "restraint/respect for the size they chose" stance shows up as one of three named lenses in B, D, and E specifically — in all three cases it's the pull-short (don't over-read, don't inflate) promoted into stance position rather than a genuine affective lens. C, F, and G don't make this move (and A doesn't either); worth checking whether that's a prompt-variation artifact rather than noise across independent samples.

## Unsealing

1. **A = V3** (non-attitude stance requirement) — **WINNER**
2. **C = V-combo** (all five changes)
3. **F = V5** (preamble reframe + presence permission)
4. **G = V2** (drop coworker framing)
5. **E = V4** (flinch-crossed draft line)
6. **D = V1** (drop least-trusted)
7. **B = baseline v0.7**

## Findings

- **Every variation beat baseline.** No exceptions.
- **V3 alone won.** Explicitly requiring one non-attitude stance in the pool produced the strongest locator output — beating V-combo which included that requirement plus four other changes.
- **The "caution smuggling" pattern is real and specific.** Baseline (B), V1 (D), and V4 (E) all produced a middle-stance that was really the model's own restraint elevated to a lens. V2, V3, V5, and V-combo did not.
- **V4's rehearsal lines alone didn't rescue it.** Rehearsal lines are downstream-buildable material and the reader praised them, but restraint-smuggling still occurred at the stance layer. Flinch-crossed drafts probably need to be paired with the non-attitude requirement to work well.
- **V5's preamble reframe made #3 with no Step 1 structural change.** Tone alone lifted the output substantially — confirming that the "embody the mode" principle has real effect independent of structural rules.
- **V-combo (#2) did not beat V3 alone (#1).** More constraints didn't monotonically help. Worth interrogating whether the added structure (rehearsal, easy/hard notes) crowded the stance space or introduced its own noise.
- **The single highest-leverage change was requiring a non-attitude stance.** That one line changed the stance vocabulary the locator was allowed to use, and the reader's rubric directly rewarded it.

## What to lock in for step 1

Recommendation: adopt V3's non-attitude stance requirement as the new baseline for step 1. Optionally also adopt V5's preamble reframe (independent effect, tone-level). Do NOT lock in V-combo's other additions (rehearsal lines, easy/hard notes) yet — the evidence suggests they didn't add value on top of V3, and may have interfered.

The rehearsal-line idea (V4) is worth keeping in reserve for a later round — it might work paired with a different framing.
