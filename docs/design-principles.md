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

## Open questions surfaced by step 1

- Does the caution-smuggling pattern reproduce across different
  material, or is it specific to Ash-shape conversations (bracing
  young person, apology-heavy)?
- Is V3's win robust across multiple samples, or is one run enough?
- Does the non-attitude stance requirement matter more when the
  material is emotionally rich, or when it's emotionally flat?
- What happens if we explicitly forbid restraint-as-stance rather
  than requiring non-attitude? Different mechanism — does it work
  differently?
- Does V4's rehearsal-line idea work paired with V3's stance
  requirement (both concrete words *and* opinionated stance)?
- Does the "embody the mode" principle apply to every step
  equally? Or is it more/less important for some?

## What to test next

Step 1 round 2: build a new baseline from V3+V5 combined, run 2-3
variations on that, re-rank with all previous outputs to see if
V3+V5 combined beats V3 alone.

Then step 2 (emotional lens) round 1: what variations of the lens
prompt shift the lens output quality, holding the new step 1
baseline fixed.
