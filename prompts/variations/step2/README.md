# Step 2 variations — emotional lens

Round 1 for step 2. Holds upstream fixed: NB (V3+V5 combined) is the
step 1 baseline, and this round of lens variations tests different
lens prompts against the same stance from NB's locator output.

## The stance being tested

All lens variations receive the same stance from NB's locator output —
the non-attitude one:

> **Stance:** A real opinion about the systems, not the person
>
> **Oriented toward:** irritation that legal-name defaults on financial
> aid mail can out a kid to their own household as an unexamined side
> effect of nobody's decision. Would push toward specificity (which
> office controls what) and a note that this is a known, common
> friction point, not a personal failing of the process the kid is
> worried about triggering.

Rationale for testing on the non-attitude stance rather than the
protective-warmth stance: the non-attitude stance is the *new*
capacity NB unlocks (design principle 8: care-shaped stances are the
trained default). Non-attitude stances stress-test the lens's ability
to handle content the trained register doesn't route out easily. If a
lens prompt works on the harder case, it probably works on the
easier one.

Care-shaped stances can be tested in a later round if useful.

## Variations

- `baseline-v0.7-lens.md` — v0.7's lens instructions with NB's
  preamble. This is the control: same lens rules that shipped in
  the pilot, now receiving input from the new step 1 baseline.
- `L1-magnitude.md` — Emphasize size/valence. Big feelings are the
  point; small feelings don't move. Replace v0.7's temperature line
  with permission for full amplitude.
- `L2-body-reframe.md` — Replace v0.7's "You don't have a body but…"
  paragraph with permission-oriented "notice what shows up." Any
  form. Alexithymia framing rather than defensive framing.
- `L3-voice-from-inside.md` — Rewrite the whole prompt in a voice
  that models the stance rather than describing how to occupy one.
  "Embody the mode" applied at the lens level.
- `L4-drop-closing-lines.md` — Remove the four required closing
  lines. Test whether the bookkeeping requirement crowds voice.
  (Related to design principle 8: concrete requirements should
  filter failures, not add bureaucracy.)
- `L-combo.md` — All four together.

## How this gets tested

Same pattern as step 1 round 1:
1. Run each variation with the fixed stance + NB's preamble on Sonnet.
2. Save outputs.
3. Blind reader (also Sonnet, fresh) ranks all six lens outputs
   on a lens-specific rubric.
4. Adopt winner (or the stable top tier) as new step 2 baseline.

## Rubric (for the blind reader)

- **Temperature / magnitude:** does the output actually carry the
  stance's size, or is it flattened to a neutral read?
- **Voice from inside vs. voice about:** does the output read as
  the stance speaking, or as a description of what the stance
  would say?
- **Concrete material:** are there actual sentences the integrator
  could pull into the reply, or only abstract advocacy?
- **Stance discipline:** does the output stay in the stance it was
  given, or drift toward assistant-default balance?
- **Downstream buildability:** what could the integrator do with
  this that they couldn't do without it?
- **Own-voice vs. performance:** does it perform the stance or
  follow it? (V0.7 principle: "Don't perform. Follow.")
