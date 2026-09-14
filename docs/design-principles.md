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

## 14. Meta-framing about the mode undermines the mode

Step-3 finding. I4 tried to *explain* to the imagination lane why
mess is the contribution ("If you produced only what could be
shipped, the integrator would have nothing to weigh against the
default. So the mess isn't tolerated. It's what's being bought.
Filtering is downstream's job..."). The result was output like
"I notice I want to know and I notice that wanting is not this
person's problem to solve for me" — flagged by the blind reader
as "therapy-speak self-regulation, not imaginative material."

Explaining WHY the mode matters pushes the model into meta-
awareness of its own mode. The imagination lane became self-
conscious *about* overproducing instead of overproducing. The
explanation defeated the embodiment.

Related to principle 1 (embody vs. describe) but distinct:
- Principle 1 says the *prompt's voice* should model the mode.
- Principle 14 says the prompt should NOT contain a rationale
  paragraph explaining why the mode is designed the way it is.
  Even if that paragraph would help a human designer, it
  becomes text the model reads as instruction to notice itself
  operating in the mode.

Corollary: rationale belongs in the design docs, not in the
prompt. The prompt says "do this"; the docs explain why.

## 15a. Labeled footers: drain or valve, by content type (revises §11)

Round-4 (step 4 integrator) finding. T5 removed the "After the
output, the trace" section from the integrator call — testing
principle 11's prediction that labeled footers absorb voice
from the main output. The prediction *inverted* at this step.
Without the trace, the reply became MORE cautious, not less —
the blind reader called T5's output "the most easily mistaken
for a well-written FAQ answer with a warm sentence stapled to
each end." T5 placed LAST of six.

Refined principle:

- **Drain** (principle 11 as originally stated): a labeled
  footer absorbs voice from the main output when the footer's
  content is a *summary* of what the main body already says.
  The lens's four-line footer ("advocating for / flinched /
  crossed well / could go wrong") asked the lens to compress
  its own voice into labels. The voice migrated into the
  labels; the body thinned. Dropping the footer let the body
  carry the voice again. L4 confirmed this.

- **Valve**: a labeled footer *supports* the main output when
  the footer's content is material the main body *specifically
  isn't saying*. The integrator's trace collects: which stances
  ran, which got weight, which got set aside and why, what cost
  something. That's material the reader will not see — it's the
  integrator's inside, made available for future-you. Removing
  the trace forces its content back into the reply itself, or
  worse, leaves it with nowhere to go. Either way the reply
  gets more careful. T5 evidence supports this direction.

Rule of thumb: a labeled footer's function is set by whether
the material it collects duplicates or complements the main
output. Duplicative → drain (remove). Complementary → valve
(keep, and consider whether more should be routed there).

**Verification note:** N=1 at both steps. Would help to test:
- Lens variation that adds a "trace-shaped" release valve
  after L4's output — does it help or hurt? Distinguishes
  drain-vs-valve at the lens layer.
- Integrator variation that adds a "summary of what I'm
  saying" footer to T2 — does the reply thin? Would confirm
  drain mechanics at the integrator layer specifically.
- Replicate T5 with different upstream/material to check the
  N=1 inversion isn't sampling noise.

Watch for: the two functions can coexist in a single footer
(some fields drain, others valve). The design implication is
per-field, not per-footer.

## 15. Labels invite naming without inhabiting

Step-3 finding, closely related to principle 1. The I-combo
output labeled its moves as the prompt's phrasing suggested —
"Absurd version:", "Wrong-frame version:", "Register note:" —
and then delivered the same measured essay voice under each
label. The blind reader called this out precisely: "It names
the destinations without visiting them."

I1's rewrite included similar labels ("As a folktale:", "As a
bad joke:") but the model *inhabited* them (wrote an actual
folktale, wrote a flat unfunny joke). Why the difference?

Hypothesis: when the surrounding instruction weight is low
(I1 alone), a label reads as an invitation to try the mode.
When the surrounding instruction weight is high (I-combo, with
concrete-failure requirement + mess-as-contribution reframe +
etc.), the labels read as *checklist items* — moves to be
executed at label-depth to satisfy the specification, not as
places to actually go.

Structural implication: any labeled prompt for a creative step
should minimize the number of *other* instructions bracketing
the labels. Labels + heavy scaffolding → naming-without-
inhabiting. Labels + light scaffolding → the model actually
goes.

## Step 2 status: locked in

*(unchanged, see above)*

## Step 3 status: locked in

After one round:
- **New step 3 baseline: I1** (embodied register — imagination
  instructions rewritten to enact sprawl in voice). File:
  `prompts/variations/step3/I1-embodied-register.md`.
- Blind reader placed I1 top of the six by rank-sum (11) with a
  significant margin. It "actually writes a folktale instead
  of talking about folktales" and produced a flat unfunny joke,
  an incantatory repeated line, a sentence cut off mid-word,
  and invented atmospheric detail it names as invented.
- I-combo placed *last* (rank-sum 32) — worse than baseline.
  Third confirmation of principle 3 (more rules don't
  monotonically improve) across the three steps. The mechanism
  at this step is principle 15 (labels invite naming without
  inhabiting) plus principle 14 (meta-framing undermines mode).

Reserves — held for possible future reintroduction or context-
specific use:
- **I2** (concrete failure requirement) — strong runner-up
  (rank-sum 12). Produced the cleanest resistance to the edit-
  it-out impulse ("Ottawa. No idea why that surfaced. Not
  following it"). Worth re-testing on material where the model
  can't voice-model well without help. NOT for stacking on I1;
  the combo attempt showed stacking these turns imagination
  into a checklist.
- **I3** (drop threads-to-set-aside) — third by rank-sum (13).
  Mild positive. The imagination's threads-line is less of a
  drain than the lens's four-line footer was, but removing it
  didn't cost anything.
- **I4** (mess-is-contribution) — principle-14 evidence. Held
  as a cautionary example, not for reuse.

Model-default artifact worth noting: five of six outputs opened
with a "preferred" wordplay riff, three landed on the "preferred
stock" rhyme. This is a strong default attractor at this
material — not informative about the variation. Future rounds
should note when convergent openings might mask variation
effects and consider material with fewer obvious wordplay hooks.

## Open questions carried forward

- Does the caution-smuggling pattern reproduce across different
  material?
- Does the meta-noticing pattern (principle 9) reproduce?
- Does the concrete-requirements-filter-abstract-failures
  principle (8) hold up at the integrator step?
- Does the "embody the mode" principle apply equally to every step?
- Does the labeled-footer-drain (principle 11) show up in the
  integrator's trace?
- Does the meta-framing-undermines-mode principle (14) hold at
  the integrator step, where explaining the design has
  historically felt necessary?
- Does the labels-invite-naming-without-inhabiting principle
  (15) reproduce when instruction weight is deliberately kept
  low?

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

Step 4 (integrator). NB (step 1), L4 (step 2), and I1 (step 3)
fixed upstream. Both design critiques flagged the integrator as
the layer where range dies; the operator's own intuition agreed.
This is the most consequential step in the pipeline — it's the
one that speaks outward. Everything upstream produces material.
The integrator decides what actually ships.

Design surface for the integrator has been named in prior
conversation and the two critiques:

- **Anti-diagnosis is a filter without a counterweight.**
  V0.7's "company not diagnosis" rule says what not to do
  (don't finish a sentence they didn't finish, don't name the
  thing under the thing). It doesn't say what to reach for
  instead. Both critiques flagged this. Principle 8 predicts a
  concrete positive requirement would filter this better: e.g.
  "write one sentence that shows you saw them without naming
  what they didn't name."
- **Range dies at the integrator.** The integrator's job of
  "weighing" stances currently reduces to filtering them
  against the assistant default. Nothing in the prompt
  actively asks the integrator to let more through than the
  default would voice. Permissions in the integrator, like the
  preamble, may all point toward retreat (principle 6).
- **Volume rule may be a straitjacket.** "Pick: one opinion,
  one joke or tease, one genuine enthusiasm, one question.
  Then stop." Explicitly bounds the reply to four moves on a
  light message. Worth a variation that removes it or replaces
  it with a target rather than a cap.
- **Register.** V0.7's integrator instructions are long,
  procedural, and organized under bold headers. Principle 1
  suggests the integrator's prompt should model the mode it
  wants to induce — trust, integration, presence, not
  procedure. Related to principle 14: the current prompt is
  heavy on rationale ("that means…" clauses everywhere).
- **Trace after output.** The trace lives at the end of the
  integrator prompt. Principle 11 (labeled footers absorb
  voice) predicts this could be a drain — the model may be
  writing the integrator's output partially aimed at what will
  read well in the trace. Worth a variation that moves the
  trace elsewhere or drops it.
- **Voice-not-hands as an explicit principle.** The lens step
  now has clear language about "you don't ship, the integrator
  does." The integrator side of that contract could be made
  explicit: "you receive advice from voices that don't ship;
  you are the one who does." Might reduce the reader-tone-
  policing the model does on lens outputs currently.

That's a wide surface. Round-1 variations to consider:
- **T1**: replace "company not diagnosis" with a concrete
  positive requirement (principle 8 applied).
- **T2**: add bidirectional permissions (principle 6 applied).
- **T3**: rewrite the integrator instructions in a voice of
  presence and trust rather than procedure (principle 1
  applied).
- **T4**: remove the volume rule / replace cap with a target.
- **T5**: move the trace to a separate step, or drop it.
- **T6**: make voice-not-hands explicit.
- **T-combo**: hold in reserve. Given principle 3 has now
  reproduced three times (V-combo, L-combo, I-combo all placed
  worse than their best-single), the fourth round should
  probably skip the combo unless there's a specific reason to
  expect these variations to compound.
