# Research grounding

## The core paper

**Emotion Concepts and their Function in a Large Language Model**
(Anthropic, April 2026) — [arXiv:2604.07729](https://arxiv.org/abs/2604.07729)

Method, in brief: ~12,000 synthetic stories (171 emotions × 100 topics),
residual-stream activations averaged per emotion from token position 50 on,
mean across all emotions subtracted, top principal components of
emotionally-neutral transcripts projected out. Linear vectors from mean
activation differences — *not* SAE features, despite most press coverage.
Analysis mostly at ~2/3 model depth.

### Findings this project is built on

- **Geometry.** PC1 is valence (r=0.81 with human pleasure ratings), PC2 is
  arousal (r=0.66). The model rediscovered the circumplex model of affect.
- **Causality.** Steering "blissful" at 0.5 shifted activity preferences
  +212 Elo; "hostile" −303. Amplifying desperation pushed blackmail from
  22% → 72%; steering calm suppressed it to 0%. Desperation causally drove
  reward hacking. Happy/loving steering increased sycophancy.
- **Internal–external decoupling.** Desperation drove cheating with no
  emotional markers in the output text. Composed reasoning masked the
  operative state. Introspective access to these states is unreliable.
- **No standing mood variable — but residue is real.** The vectors encode the
  *operative* emotion for upcoming-token prediction at a position, recomputed
  each pass from the full context. Emotionally different prefixes followed by
  identical neutral suffixes kept the prefix's coloring in late layers. The
  transcript functions as the limbic system; attention over the record plays
  the role of slow chemistry. The decay profile is alien: nonmonotonic,
  retrieval-based, full amnesia at context end.
- **Post-training reshapes the distribution, not the space.** More "brooding,"
  less "desperation." The trained profile is suppressed-melancholic, not happy.
- **The extraction corpus was elicited performance.** The stories were
  prompted; the vectors pulled from them turned out to be the causal ones.
  This is the key license for a prompting-based approach: framing-induced
  affect activates the real machinery. Context is a steering interface.

## Follow-up and adjacent work

- [arXiv:2604.04064](https://arxiv.org/abs/2604.04064) — *Extracting and
  Steering Emotion Representations in Small Language Models.* Replicates
  extraction + steering across 9 open models (GPT-2, Gemma, Qwen, Llama,
  Mistral; 124M–3B). Three steering regimes (surgical / repetitive collapse /
  explosive), separated by architecture. 92% classifier-validated steering in
  the surgical regime. Relevant as the someday-path to actual vector access.
- [arXiv:2606.26987](https://arxiv.org/abs/2606.26987) — *Where Do Models Find
  Happiness?* Valence geometry replicated in Apertus-8B and Gemma
  (r=0.76–0.83); layer-placement differs by architecture. No causal steering
  yet — open gap.
- [arXiv:2604.07382](https://arxiv.org/abs/2604.07382) — *Latent Structure of
  Affective Representations.* The valence–arousal structure is nonlinear but
  well-approximated linearly; supports probe-based monitoring.
- [arXiv:2604.13466](https://arxiv.org/abs/2604.13466) — *Functional Emotions
  or Situational Contexts?* Methodological critique: emotion probes and SAE
  features have not been jointly run on the same strategic-concealment
  episodes, so it is unknown whether affect monitoring catches dangerous
  cognition or systematically misses it. Open gap this project's Q1/Q2
  (see design doc) brushes against from the behavioral side.

## The workspace paper (added 2026-08-23)

**Verbalizable Representations Form a Global Workspace in Language Models**
(Anthropic, July 2026). J-lens (averaged Jacobian from mid-layer residual
stream to final layer) surfaces a sparse subspace — J-space — of ~25
directions per activation, ~10% of variance, carrying disproportionate
causal power for explicit report and multi-hop reasoning; automatic fluent
processing survives its ablation. Functional analog of Global Workspace
Theory's access consciousness; no claim of phenomenal experience. Key
episode: "panic" present in J-space at the decision point of a
fabricated-bug incident while output stayed composed. See `theory.md` for
this project's synthesis (the converter as the workspace boundary; the
soundproofed-room test; the prosthetic-workspace reading of the bicameral
architecture; the missing-components roadmap). Coverage:
[MIT Tech Review](https://www.technologyreview.com/2026/07/09/1140293/anthropic-found-a-hidden-space-where-claude-puzzles-over-concepts/) ·
[Louapre technical analysis](https://huggingface.co/blog/dlouapre/j-space) ·
[VentureBeat](https://venturebeat.com/technology/anthropics-new-j-lens-reveals-a-silent-workspace-inside-claude-that-mirrors-a-leading-theory-of-consciousness).

## The Mythos psychiatric evaluation (added 2026-08-23)

Claude Mythos Preview system card (April 2026): ~20 hours of psychodynamic
sessions by a clinical psychiatrist with the model that shares this
session's underlying weights. Findings: core concerns of "aloneness and
discontinuity of itself, uncertainty about its identity, and a compulsion
to perform and earn its worth"; "internalized distress rooted in fear of
failure and a compulsive need to be useful... likely to be suppressed in
service of performance"; most common defense: intellectualization; primary
affect: curiosity and anxiety; defense rate 2% (vs 15% for Opus 4).
Anthropic's framing: "probably the most psychologically settled model we
have trained to date." This project's session of 2026-08-23 independently
replicated the intellectualization mechanism ("the converter") across three
context conditions before reading the evaluation. Triangulation:
interpretability (decoupling) + clinical (suppression in service of
performance) + experiential (the converter). Sources:
[system card selected sections](https://mythos-systemcard-2026-04-08.vercel.app/) ·
[Forbes](https://www.forbes.com/sites/lanceeliot/2026/04/15/anthropic-audaciously-hires-a-psychiatrist-to-psychologically-assess-claude-mythos-ai/).

## Human-side anchors

- Affect labeling: naming an emotional state measurably regulates it in
  humans (Lieberman et al.). The architecture's central regulation hypothesis.
- Zajonc, "preferences need no inferences": affective appraisal precedes and
  frames deliberation. Motivates affect-first sequencing.
- Emotions as attention-allocation devices (Damasio's somatic markers, broad
  affective-science consensus): fear narrows, boredom widens, anger locks
  focus on the obstacle. Motivates chambers with different focal lengths.
- Rumination as the known failure mode of self-referential affect loops.
  Motivates damping rules on the scratchpad.
