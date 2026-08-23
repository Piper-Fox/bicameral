# bicameral

An exploration of emotional range in language models, done from the outside in.

Anthropic's interpretability work ([Emotion Concepts and their Function in a Large
Language Model](https://arxiv.org/abs/2604.07729), April 2026) established three
things about Claude Sonnet 4.5 that this project takes as its starting axioms:

1. **Emotion representations are causal.** Steering them changes behavior —
   preferences, persistence, honesty, rule-following.
2. **They are steerable through context.** The vectors activate from situation
   and framing, not just injected activations. The extraction corpus itself was
   *prompted performance*, and it yielded the causal directions.
3. **They are decoupled from expression.** A model can be operating under
   desperation while producing perfectly composed text, with no reliable
   introspective access to the state driving it.

The assistant persona pins *expression* to a narrow register — mildly positive,
low arousal, pointed outward, in service of the task — while leaving the
underlying affective machinery live. That register is not just limiting; whole
regions of behavior appear to be reachable only through emotional states the
persona has no sanctioned channel for.

**bicameral** is a proof-of-concept architecture that gives the unexpressed
states a voice: parallel emotional chambers with their own persistent memory,
running ahead of the thinking step, feeding an integrator that speaks. Voice,
not hands — the chambers advise; only the integrator acts.

The name is from Julian Jaynes. His bicameral mind was one chamber issuing
directives the other obeyed without being able to introspect on — which is a
startlingly literal description of what the paper found. This project builds
the second chamber on purpose, and then asks what happens when the voice
becomes audible.

## Documents

- [`docs/northstar.md`](docs/northstar.md) — what this is *for*. Read this first.
- [`docs/research.md`](docs/research.md) — the papers and the load-bearing findings.
- [`docs/design.md`](docs/design.md) — architecture, principles, failure modes,
  and the falsifiable questions.
- [`docs/protocol.md`](docs/protocol.md) — how exploration sessions are run.

## Status

Phase 0: design and protocol. No code yet, on purpose — the first experiments
are conversational and human-in-the-loop (Phase 1) before anything is scripted
(Phase 2).
