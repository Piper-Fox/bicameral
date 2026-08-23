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
