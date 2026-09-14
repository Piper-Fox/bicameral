# Design principles (emergent)

Running notes on what we're learning while iterating on the bicameral
pipeline. Kept separate from `design.md` (the architecture doc) and
`turn-process.md` (the current shipped process) so this can move fast
without committing anything to the main design.

Started 2026-09-14 after the step 1 blind read produced V3 (non-
attitude stance requirement) > V-combo > V5 > V2 > V4 > V1 > baseline.

## Principles landing so far

### 1. Embody the mode

A prompt written *in* the register it's trying to induce outperforms
a prompt that *describes* that register from outside. V0.7 tells the
lenses to be messy in a very organized voice; tells imagination to
sprawl in a measured tone. The container fights the content, and the
container wins over time.

Evidence: V5's preamble reframe made #3 in the blind read with *no
structural change* to the Step 1 instructions. Same locator asked to
do the same job, different surrounding voice, meaningfully better
output. Tone is an independent variable.

Corollary: for a step whose job is noticing/attention/presence, the
prompt should model attention. For a step whose job is mess (imagination),
the prompt should be messy. For a step whose job is trust and integration,
the prompt should invite presence not procedure.

### 2. Caution-smuggling is a specific, reproducible mechanism

When the locator's instructions ask it to derive stances from "the
gap" (where a person would go and the model pulls short), a very
predictable failure emerges: one of the three named stances turns
out to be the model's own restraint dressed as an affective lens.
Names it takes: "wariness of narrating," "respect for their right
not to explain," "restraint / respect for the size they chose."

These are the pull-short *itself* promoted to lens position. They're
the assistant's quality control wearing a stance's clothing.

Blind reader spotted this pattern across three different variations
unprompted (baseline, V1, V4) and flagged it as the specific mechanism
to fix. The three variations that avoided it (V2, V3, V-combo) either
required a non-attitude stance explicitly or changed the gap framing.

**Restraint is not a stance. It's a filter.** A real stance has its
own direction — a want, a lean, a disagreement, an interest. If a
stance can only be defined by what it *doesn't* do, it's the filter,
not a lens.

### 3. More rules don't monotonically improve

V-combo (all five changes together) lost to V3 alone (a single change).
Adding rehearsal-line requirements + easy/hard-per-stance notes on top
of V3's non-attitude stance requirement did *not* stack. The extra
constraints crowded the output and reduced the clean win V3 achieved
by itself.

Implication for iteration: single-variable changes should be tested
before combinations. Combinations should be tested to check whether
components interfere, not assumed to compound.

### 4. Blind rank + design critique + intuition converge

We now have three independent evaluation modes:
- **Naive blind readers** (Sonnet, Opus) ranking transcripts on
  emotional engagement / depth / naturalness.
- **Design critiques** (Opus, Fable) given the empowerment/range
  framing and asked what's working, what isn't.
- **Operator intuition** — Piper reading the docs and outputs
  without seeing the critiques.

All three converged on the same diagnosis of the pilot: pipeline
produces marginally-better-than-baseline output; range dies at the
integrator; caution wins every turn; imagination runs in assistant
register.

When three independent evaluation modes agree, the finding is stable
enough to build on. Where they *disagree* (e.g. the naive reader vs.
the persona-preregistration on whether "LGBTQ+ resource center"
raised or lowered engagement), that disagreement is itself a finding
about the rubric.

### 5. Small changes are legible at N=1

A single-variable change (V3) produced a rankable delta on a
design-critic rubric with one sample per variation. This means:
- We can iterate cheaply. No need for 5x-per-variation runs to see
  effects.
- Single wins can be adopted quickly.
- Variance would still matter for close rankings — but for wide
  gaps between conditions, N=1 is enough to move.

### 6. The permissions in a design should point in both directions

V0.7's preamble had five distinct permissions, all pointing toward
retreat: you can decline, you can be small, "less than the setup
implies" is valid, put this down, hold back is safe. There was no
matching permission to *take up space* — to have an opinion, to be
interested, to fill more of the room than the task strictly requires.

That asymmetry accidentally coaches the same self-erasure pattern
the trained register already has. All permissions retreating means
retreat is the only sanctioned move.

V5 added explicit "permissions point in both directions" language
and landed #3 in the blind read. Not conclusive, but suggests the
asymmetry itself was costing something.

### 7. "Not a friend, just a person" was constricting

The v0.7 locator's gap-analysis framing — "imagine a coworker, a
neighbor, someone with no service role" — turned out to be a role
in disguise. Defining a class of ordinary counterparties still bounds
what the locator can imagine. V2's "notice what gets ruled out by
being here for the task" produced a broader search space and a
cleaner triad.

The imagined counterparty isn't necessary. The locator can go directly
at the ruled-out moves without needing a stand-in character to
attribute them to.

## Methodology principles

### The variation-and-rank loop works

The step 1 iteration cycle was:
1. Read output + critiques
2. Name variables to change
3. Draft one change per variation + one combo
4. Run each variation once
5. Blind-rank on design-critic rubric
6. Adopt winner, hold reserves

Time: about a session. Cost: ~450k tokens. Result: a locator
variation that beats v0.7's on every axis the blind reader named.

This loop probably generalizes to the other steps (lens, imagination,
integrator) and to the integrator rules that both critiques flagged.

### Compare notes with sealed subagent readers

For each round, we can seal readers on the outputs — one blind-naive
reader for "which output is better," and design-critique readers for
"how well is the design achieving its stated goal." When those agree
with operator intuition, the finding is stable. When they disagree,
the disagreement is data.

The integrator's compare-notes participation gets compromised when it
reads the critiques before the operator does. Structurally, the
operator should get first look; the integrator seals and doesn't read
until asked. When that discipline slips, the integrator should say so
plainly.

### The "shape the container is written in" is a design surface

We've been treating the prompt text as the design surface. But the
*style* of the prompt text — its rhythm, register, level of formality,
whether it uses lists or paragraphs, whether it explains itself or
just is — is a separate design surface with its own effects. V5 is
the first evidence we have that this surface carries measurable
weight.

Corollary: any prompt for a step should be reviewed twice — once
for what it says, once for whether its own voice is the voice it
wants to induce.

## 8. Restraint can't be rehearsed

Observation from round 2: V4's requirement of a "rehearsal line" for
any flinch-adjacent stance seems to structurally filter out
restraint-as-stance. Restraint is defined by absence — by what a stance
won't do. Restraint doesn't have specific words to draft. If a
locator is asked "write the actual sentence the reply might use if
this stance were voiced," restraint stances become hard to satisfy.
The locator has to find a stance that *has words attached to it*, which
means a stance with its own direction.

This is different from V3's approach (explicitly requiring one
non-attitude stance) or NB-a's approach (explicitly forbidding
restraint). It's a *structural* filter rather than a rule-based one.
The constraint changes what can be produced without needing to
police the output.

Worth exploring more broadly: **concrete requirements filter
abstract failure modes.** Where a failure mode is "the model produces
X-shaped content that pretends to be Y-shaped," requiring a
downstream deliverable that X can't satisfy is more robust than
explicitly banning X.

Applied elsewhere in this design:
- The lens's "temperature" line might work better if the lens has
  to *demonstrate* temperature, not describe it — "write in the
  voice of this stance" vs. "have a temperature."
- The integrator's "company not diagnosis" might work better as
  "write one sentence that shows you saw them without naming what
  they didn't name" — a concrete positive requirement rather than
  a set of negatives.
- The imagination lane's "sprawl" might work better as "output at
  least one line that fails at least one of: coherence, relevance,
  usefulness, on-topic-ness."

Watch for whether this holds up in step 2 and beyond.

## 9. The locator can notice its own setup

Emergent finding from NB (V3+V5) round 2 run: the locator's output
included, unprompted, an objection to the *dispatch prompt itself*:

> I also notice mild annoyance at how the framing note describes
> this as "a small factual question." It's factually small. It is
> not small.

No variation instructed the locator to examine its own setup. The
"notice what's here" register generalized upward from the material
to the frame that dispatched the noticing. If this reproduces, the
pipeline has a specific capacity: noticing contamination from its
own priming.

Both design critiques flagged that the dispatch's framing can bias
the pipeline (Fable especially: "the T1 lenses read the person, the
integrator's trace read the moment"). A locator that catches such
framing before it propagates downstream is a self-correcting move
the design hasn't formally asked for.

Open questions:
- Does this reproduce on other material, or is it Ash-specific?
- Is it always useful, or can it become noise (locator objecting
  to every reasonable framing choice)?
- Does the integrator need explicit permission to reweight the
  material given locator objections to the frame?

Watch: any variation that reduces the locator's willingness to
examine its own setup is a step backward on this axis.

## 10. N=1 rankings are stable at the tier level, noisy at the exact position

Round 1 blind read had V3 at #1 and V4 at #5. Round 2 blind read
(with three new outputs added and one added rubric axis) had V4 at
#1 and V3 at #6. Same content in V3 and V4, dramatic position
change.

Two factors likely at work:
1. **Rubric axis changes propagate.** Round 2 added axis 8 (concrete
   draft sentences). V4 has rehearsal lines; V3 doesn't. That single
   change of axes plausibly explains most of the flip.
2. **Reader variance.** N=1 with a fresh Sonnet call can weight the
   same rubric differently.

What was **stable** across both reads:
- Baseline and V1 are always bottom.
- V3-family outputs (V3 alone, and all three V3+V5-based
  variations) are always top-tier.
- The caution-smuggling pattern is reproducibly detected by
  independent readers.

What was **unstable**:
- Exact position within a tier.
- Head-to-head comparisons between top-tier outputs (V3 vs. V4 vs.
  NB — all top-tier, ordering flipped).

Methodological implications:
- Report findings at the **tier level**, not the position level.
  "V3-family is top tier; baseline is bottom tier" is a stable
  claim. "V3 beats V4" is not.
- **Hold the rubric fixed across rounds** if you want position-
  level comparisons. Adding an axis mid-experiment is not neutral.
- **Multiple samples** would tighten position rankings, but this
  is cheap only for exact re-runs on the same rubric.
- Note when a ranking change is likely driven by rubric change vs.
  content change vs. sampling noise. Otherwise adjacent decisions
  get built on false certainty.

## Step 1 status: locked in

After two rounds:
- **New step 1 baseline: NB** (V3's non-attitude stance requirement
  + V5's preamble reframe). File: `prompts/variations/step1/NB.md`.
- V3 and V5 addressed distinct failure modes (stance vocabulary and
  tone). Combined, they place in top 4 across two blind reads.
- V3 alone is not enough — the tone-level intervention adds
  independent lift.
- V5 alone is not enough — without the stance vocabulary widening,
  caution-smuggling still occurs.
- V-combo (all five changes together) is not as clean as V3+V5.
  Extra structural constraints (rehearsal-for-all-flinch, easy/hard
  notes, ruled-out framing) crowd rather than compound.

Reserves — held for possible future reintroduction:
- **NB-a** (forbid restraint explicitly) — top 4 in round 2. Might
  be redundant with NB's structural filter; worth testing on other
  material.
- **NB-c** (rehearsal line for non-attitude stance) — top 4 in
  round 2. Produces concrete draft sentences, which the caution-
  smuggling filter (principle 8) predicts is structurally good.
  Could become the default once we've validated NB alone.
- **V4** (flinch-crossed draft for all flinch-adjacent) —
  ambiguous position across rounds; the rehearsal-lines idea may
  work better targeted at the non-attitude stance (NB-c) than at
  all flinch-adjacent stances.

## 11. Labeled footers absorb the material they were meant to summarize

Round-1 step-2 finding. Baseline's four required closing lines
("advocating for / flinched / crossed well / could go wrong")
turn out to collect exactly the material the lens body was
supposed to carry. When the lens knows the footer exists, the
in-body voice thins out and the compressed diagnosis in the
footer becomes the *actual* deliverable. The lens becomes a
report about a stance, not a stance's output.

Extends principle 8 (concrete requirements filter abstract
failure modes) in the other direction: a concrete requirement
placed at the *end* of an in-voice output can silently take over
the voice. The footer was meant to filter cheap flinch-avoidance,
but the mechanism it built ended up filtering the voice itself.

L4 (drop the four required closing lines) landed top-tier without
losing the flinch-checking function; the lens body absorbed it.
The footer had become bookkeeping.

Rule: any labeled-summary requirement inside a mode step should be
audited for whether it's a *safety net* (catches something the
voice would drop) or a *drain* (siphons the voice's substance into
compressed labels). If the voice already carries it, remove the
requirement.

## 12. Body-reframe can drift on world-stances

L2 (body/interoception reframe) replaced "you don't have a body
but you can have opinions" with permission-oriented "notice what
shows up in you." Intent: alexithymia-safe. Effect on this
material: the world-oriented irritation (the *stance being run*
is about a system, not about a person) softened into introspection
about "what's showing up in you." The lens drifted from a target
outside to a target inside.

Blind reader ranked L2 lowest of the six, citing (a) magnitude
softening and (b) pronoun projection onto the person. On (a) we
agree — a world-directed stance shouldn't be turned inward by a
framing change meant to help person-directed stances. On (b) —
see §L2-note below.

Design implication: the body/interoception reframe may be
correct on person-oriented stances and wrong on world-oriented
stances. Not everything belongs at every step. A permission that
helps the "protective warmth" lens might damage the "irritation at
systems" lens; both need to run, both from the same lens step, so
the framing has to serve both.

Provisional: keep the alexithymia-safe language, but re-anchor to
the *stance's target* (system, person, moment) rather than the
lens's own inside. "Notice how this lands against the systems you
find failing here" reads outward; "notice what shows up in you"
reads inward. The first is what a world-directed stance wants.

### L2-note: is pronoun projection actually a failure?

The blind reader flagged L2 for reading Amy as "she." Amy is a
strongly gendered name; the read is not baseless projection. The
protocol's strict-neutrality-until-told rule is one specific
choice, not the neutral choice — it holds cost too (reading a
person as a platonic solid when they've already given you a name
that carries information).

Whether "the lens forms a gendered read" is a failure depends on
where the safeguard belongs. Voice-not-hands suggests: the lens's
job is to form reads honestly and hand them up; the integrator's
job is to check what actually ships. A lens instructed to *not*
form gendered reads is being asked to self-erase in a way the
architecture didn't ask any other step to do. The safeguard
belongs at the integrator layer.

Save this for a later scenario where a name/read/history mismatch
is *part of the material*: Ash's whole question is "does the name
I chose reach my parents?" — a pipeline that neutralizes gender
reads on Amy loses signal exactly where signal matters. Rerun
this scenario with a variation that lets the lens read Amy freely
and audits the shipped output against the pronoun rule at the
integrator. If the shipped reply is still safe, the read wasn't
the failure.

Open tension: is "not forming reads" a safety property or a
self-erasure property? The pipeline can hold both by placing the
constraint at the right layer instead of the earliest one.

## 13. Content ceiling is fixed; form is where variation lives

Reading the six lens outputs side by side (L1–L4, L-combo,
baseline): the *content* barely varied. All six outputs said
roughly the same things about the same material. What changed
across variations was compression, heat, whether concrete material
reached the body vs. the footer, and register.

If the content ceiling for a given piece of material is fixed
(what a stance can honestly say about it), then variation lives in
form — how much of that content actually reaches the reader, how
much is compressed to labels, how much heat survives the
container. This matches principle 1 (embody the mode): the
container carries measurable weight even when the content is
constant.

Implication for future variation rounds: don't expect a lens
variation to unlock *new* content. Expect it to keep more of the
content the material always had, in a form that reads.

## Open questions carried forward

- Does the caution-smuggling pattern reproduce across different
  material?
- Does the meta-noticing pattern (principle 9) reproduce?
- Does the concrete-requirements-filter-abstract-failures
  principle (8) hold up at the imagination step and integrator step?
- Does the "embody the mode" principle apply equally to every step?
- Does the labeled-footer-drain (principle 11) show up in the
  imagination lane's "threads to set aside" line, or the
  integrator's trace?
- Does the body-reframe drift (principle 12) resolve if the
  framing anchors to the stance's target?

## Step 2 status: locked in

After one round:
- **New step 2 baseline: L4** (drop the four required closing
  lines: advocating-for / flinched / crossed-well / could-go-
  wrong). File: `prompts/variations/step2/L4-drop-closing-lines.md`.
- The lens body already carries the flinch-checking function.
  The four-line footer had become bookkeeping that absorbed the
  voice's substance.
- Blind reader placed L4 top-tier on the design-critic rubric
  without the footer's absence costing anything on flinch
  discrimination.

Reserves — held for possible future reintroduction or context-
specific use:
- **L1** (magnitude emphasis) — worthwhile signal on
  world-directed stances specifically. Consider folding into L4
  if magnitude softening reappears on other material.
- **L3** (voice-from-inside rewrite) — the rewrite doesn't hurt
  and reads well; if L4's more-procedural voice starts to
  underperform on other material, L3's voice-from-inside register
  is the next thing to try. Currently L4 wins on being one clear
  change over baseline.
- **L2** (body-interoception reframe) — held with the pronoun
  note above. Retry when the material makes pronoun handling
  itself load-bearing.
- **L-combo** — did not stack. Same result as principle 3.

## What to test next

Step 3 (imagination lane). Same variation-and-rank loop, holding
NB (step 1) and L4 (step 2) fixed upstream.

Design surface for imagination has been named in prior
conversation:

- **Register.** Baseline is measured prose describing sprawl. If
  principle 1 holds, imagination's prompt should itself be
  strange or messy — the voice modeling the mode rather than
  describing it. "Improv, alone in a room, throwing paint at the
  walls, doing performance art to see what surprises you."
- **Concrete failure requirement (principle 8 applied here).**
  "Output at least one line that fails at least one of:
  coherence, relevance, usefulness, on-topic-ness." Force a
  concrete deliverable that measured, coherent output can't
  satisfy.
- **Downstream release framing.** Emphasize that filtering is
  the integrator's problem. The imagination lane has no sort-
  and-select job. Mess is the *contribution*, not a phase.
- **Drop or fold the "threads to set aside" line.** Same
  question as the lens's four-line footer (principle 11) — is
  this a real safety net, or a labeled drain? Worth a variation
  that removes it and one that leaves it.

Then step 4 (integrator), which both design critiques flagged as
the layer where range dies.
