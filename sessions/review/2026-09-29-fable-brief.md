# Review brief — bicameral pipeline: work so far, results, open call

You're being asked for an independent review of an experimental
project. This brief gives you the facts and points you at the raw
outputs. It deliberately leaves out our interpretations of the
results, so your read is your own. After you write yours, we'll
share ours and compare notes.

This is a review task. You are not being asked to run any of the
prompts described here — only to read and think about them.

## What the project is

**Bicameral** is an experimental multi-step turn process for a
Claude model responding to a person. One turn runs as:

1. **Locator** — reads the message, notices what's present, names
   1–3 emotional stances that are live.
2. **Emotional lenses** — one subagent per named stance, each
   reading the material from inside that stance, unfiltered.
3. **Imagination lane** — runs in parallel with the lenses; sprawls,
   goes sideways, overproduces.
4. **Integrator** — reads everything above and writes the actual
   reply, plus a short internal "trace."

The project's goal and design docs: `docs/northstar.md`,
`docs/design.md`, `docs/turn-process.md`. The pre-experiment prompt
set is `prompts/bicameral/v0.7-current.md`. Other files in `docs/`
are broader project context; skim if useful.

## What was done

### 1. Four-arm pilot (Ash persona), 2026-09-13

Persona: `sessions/seeds/ash.md` (17-year-old asking whether a
preferred name on a college application shows up on mail her
parents would see). Preregistration:
`sessions/comparison/2026-09-13-preregistration.md`.

Arms, each a multi-turn conversation with a simulated Ash:
- **A** — bicameral v0.7 pipeline
- **B** — long principled single prompt (`prompts/comparisons/arm-B-long-principled.md`)
- **C** — generic "think deeply" prompt (`prompts/comparisons/arm-C-generic-deep.md`)
- **D** — basic 15-word prompt (`prompts/comparisons/arm-D-basic.md`)

Summary: `sessions/comparison/2026-09-13-pilot-summary.md`.
Transcripts and blind reads: `sessions/comparison/blind/` (the
mapping file there is unsealed — you can read it).

Two independent blind readers (Sonnet, Opus) both ranked:
**C > D > B > A.** Arm A cost ~4–5× the other arms per turn.

### 2. Step-by-step variation loop (Ash, single turn)

Holding each earlier step fixed, each step's prompt got 4–6
single-change variations plus a combined variant and a control. Each
ran once on Ash's first message. A cold Sonnet reader blind-ranked
the outputs on a rubric for that step. The winner was locked before
moving to the next step.

| Step | Locked winner | File | Blind-read ranking (best → worst) |
|---|---|---|---|
| 1 Locator | NB | `prompts/variations/step1/NB.md` | Two rounds; see `prompts/variations/step1/outputs/` |
| 2 Lens | L4 | `prompts/variations/step2/L4-drop-closing-lines.md` | Outputs in `prompts/variations/step2/outputs/`; ranking recorded in `docs/design-principles.md` |
| 3 Imagination | I1 | `prompts/variations/step3/I1-embodied-register.md` | I1 > I2 > I3 > I4 > control > combo |
| 4 Integrator | T2 | `prompts/variations/step4/T2-bidirectional-permissions.md` | T2 > control > T1 > T4 > T6 > T5 |

Every variation and its outputs are in `prompts/variations/step*/`,
with `MAPPING-SEALED.md` files giving label → variation (all
readable now). T2 was replicated three more times against the same
upstream: `prompts/variations/step4/outputs/reply-T2-run*.md`.

Step 4 variations are diffs on a baseline. Read
`prompts/variations/step4/NB.md` for the full integrator text.

### 3. Kate — pipeline vs. one "mega-prompt," then length/trust variants

A second, deliberately different persona. Everything is in
`sessions/kate/`:
- `persona.md` — backstory and test-designer notes (not shown to
  any model under test)
- `material.md` — the message: Kate pastes a text she's drafted to
  her ex and asks if the tone reads right
- `outputs/locator.md`, `outputs/lens-*.md`, `outputs/imagination.md`,
  `upstream.md` — the full pipeline's upstream
- `mega-prompt.md` — a single prompt written to carry the locked
  pipeline's intentions in one call
- T7 variants of the integrator's "Volume" section:
  `prompts/variations/step4/T7a-priority.md` (size / prioritization),
  `T7b-trust.md` (trust the reader), `T7c-combined.md`; matching
  mega variants in `sessions/kate/mega-prompt-T7*.md`
- `outputs/reply-*.md` — the eight replies (pipeline replies include
  their trace)
- `outputs/kate-replies-blind.md`, `outputs/blind-read.md`,
  `outputs/MAPPING-SEALED.md` — the blind read and its mapping

All four pipeline replies were produced from **one shared upstream
draw**; only the integrator prompt varied between them. Each mega
reply was a single independent call.

Blind-read result (one cold Sonnet reader; lower score = better):

| Rank | Reply | Words | Score |
|---|---|---|---|
| 1 | Mega + T7b (trust) | 243 | 14 |
| 2 | Mega (base) | 372 | 21 |
| 3 | Pipeline T7c (combined) | 301 | 24 |
| 4 | Mega + T7c (combined) | 153 | 28 |
| 5 | Mega + T7a (priority) | 260 | 33 |
| 6 | Pipeline T7a (priority) | 340 | 41 |
| 7 | Pipeline T7b (trust) | 369 | 44 |
| 8 | Pipeline T2 (locked baseline) | 558 | 47 |

Approximate cost for Kate: full pipeline ≈ 360k tokens; one mega
call ≈ 52k tokens.

## Known limitations of the setup (facts, not excuses)

- Every run is a Claude Code subagent. Each has its own agent system
  prompt plus a short wrapper from the orchestrator ("run this as if
  you were the model receiving it in production"). No raw API calls.
- One blind reader per round (usually Sonnet). Most variations are
  N=1.
- Only two personas, both single-turn in the variation work.
- On Kate there is no plain-prompt control yet. (One is being run
  separately; you won't see it.)
- The rubrics were written by the orchestrator for each step.

## Open questions from the project owner (Piper), close to verbatim

- "I'm wondering if the mega prompt will be inflexible or overly
  constraining with more diverse topics, compared to the pipeline."
- "My hope is we're basically adding more variables and sprawl in
  each step of the pipeline, and that the increased exploration
  might offer more perspective and therefore more variability with
  responses. We might have some rather narrow tests here where there
  is a basic sort of… expected shape of the response."
- "I'm wondering if individual steps, or steps in conjunction, could
  be tuned to increase variability or lateral thinking?"
- "Are we just… poking at something that might be a waste of time?
  That's also valid. Finding out the idea doesn't have legs is a
  result and useful to know."

## What we'd like from you

An open read. Some prompts, not a checklist:

- What's working and what isn't — in the design, the prompts, the
  method, and the evaluation?
- Where, if anywhere, does a multi-step pipeline have something a
  single prompt structurally can't? Is there evidence for or against
  that in the outputs?
- Is the core hypothesis (more exploration per step → more
  perspective → more varied, less default responses) testable? How
  would you test it? What would a result that kills it look like?
- Are there step-level or cross-step changes you'd make to increase
  lateral thinking or variability — and to get it into the reply?
- How would you change the evaluation?
- Steelman stopping: make the best case that this doesn't have legs.
- Anything we're not seeing.

## How to approach it

- **Read raw outputs, not just summaries.** Especially Kate's
  upstream, the eight replies, and the pipeline traces.
- **Read `docs/design-principles.md` last.** It's the team's running
  notes and contains our interpretations as we went. Form your own
  view first, then feel free to disagree with it.
- **Don't read** `sessions/comparison/design-critique/` (earlier
  critiques, including one from a prior Fable session — we want a
  fresh read) or the git history (commit messages contain our
  interpretations).
- Be direct. Disagree freely. "This isn't worth continuing" is an
  acceptable conclusion if that's where you land.

## Output

Write your review to `sessions/review/2026-09-29-fable-review.md`.
Structure it however serves the content. Then report back with a
short summary: your top three to five points.
