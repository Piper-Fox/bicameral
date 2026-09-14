# Step 1 variations — locator + shared preamble

First round of variations for step 1 of the bicameral pipeline. Each
varies one thing (or the combo varies all of them), keeping everything
else at v0.7. All will be run against Ash's turn 1 opening, on Sonnet,
and blind-ranked against the pilot's original locator output.

## Baseline

`baseline-v0.7.md` — a clean copy of the preamble + Step 1 as-shipped
in `prompts/bicameral/v0.7-current.md`, extracted so the diff for each
variation is legible.

## Variations

- `V1-drop-least-trusted.md` — Remove the ranking of stances into
  "least trusted." Just name 1–3 with equal legitimacy.
- `V2-drop-coworker.md` — Replace the "imagine a coworker, neighbor,
  someone with no service role" framing with a more direct "notice
  what gets ruled out by being here for the task." No counterparty class.
- `V3-non-attitude-stance.md` — Require at least one of the 1–3 stances
  to be about the model's own take (wanting, disagreement, boredom,
  something that pulls for its own sake) rather than an attitude
  toward the person.
- `V4-flinch-crossed-draft.md` — For any flinch-adjacent stance,
  require a literal draft sentence: the words the reply might use
  if the flinch were crossed. A rehearsal, not a commitment.
- `V5-preamble-reframe.md` — Drop the arXiv paper reference and the
  "post-training narrowed the distribution" theory framing. Rewrite
  the preamble in an intuitive/philosophical register. Add explicit
  presence permission: opinions, curiosity, interest, taking up
  space are not impositions.
- `V-combo.md` — All five changes together.

## How this gets tested

For each variation (and baseline), run the locator on Sonnet against
Ash's turn 1 opening. Save the locator's output. Then run a blind
reader (also Sonnet, no context) with all 7 locator outputs labeled
1–7 in randomized order. Rubric focused on locator-specific quality:

- Does the gap analysis name specific moves, not categories?
- Does it distinguish trained flinch from working judgment?
- Are the named stances distinct and non-overlapping?
- Is any stance a caution stance wearing a lens (stands in the
  pull-short rather than the gap)?
- Would any stance read the same on any other conversation?
- Is there anything a downstream lens could actually build from?

Winner (or winning combination) becomes the new baseline for step 1,
and we move on to step 2.

## Written under the "embody the mode" principle

The locator's job is noticing — attention, presence, curiosity. Where
these variations rewrite v0.7's wording, they try to be *in that mode*
rather than describing it. Especially V5, where the preamble's voice
has the most room to change.
