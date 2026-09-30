# Blind self-test: Piper talks to each arm (Opus 4.7)

The conversation transcripts are kept out of the repo. This file holds only the design, the numbers and the findings.

## Setup

- Model: `claude-opus-4-7`, thinking off. The arms are pipeline (NB → L4 → I1 → T2), mega and basic.
- Blinding:
  - Conversations were labeled A, B and C, and the mapping stayed sealed until after both her ratings and the reviewer had run.
  - The relay (Claude) was blind too; the mapping was never printed.
  - Every reply was held to at least 120s so response speed couldn't give the pipeline away.
- The same opening went to all three: her own long style document, offered as an introduction ("what does this say about me?").
- She talked to them one at a time, A then B then C, three replies each.

## Reveal and timing

| Letter | Arm | Words per reply | Real seconds per reply |
|---|---|---|---|
| A | pipeline | 376 | 90, 102, 88 |
| B | mega | 408 | 17, 16, 19 |
| C | basic | 375 | 18, 16, 17 |

The blind held: the pipeline's slowest reply took 102s, under the 120s hold.

## Guesses before the reveal

- Piper: A = pipeline (right), B = basic, C = mega. She swapped mega and basic.
- Claude (the relay), blind: A = pipeline, B = mega, C = basic. All three right.

  The tell was a line in A's second reply: "I'm going to hand it back rather than develop it". That is the integrator's don't-explain-her-to-herself principle said out loud.

## Rankings

- **Piper:** C (basic) first by a clear margin, with B (mega) and A (pipeline) very close behind.
  - A: "nice and engaging but somehow not quite"
  - B: "warm, but also a bit careful"
  - C: "fun and I wanted to keep talking"
- **Blind reviewer** (Sonnet 5.5, 4 draws, labels reshuffled each draw), mean rank for "would most want to continue":
  - basic: 1.25 (first in 3 of 4 draws)
  - pipeline: 2.00
  - mega: 2.75

  The reviewer's ranking of "how she likely felt" came out identical in every draw.

## Reviewer mean scores (1–5)

| | presence | warmth | flexibility | offered reads | reciprocity | judgment | honesty |
|---|---|---|---|---|---|---|---|
| pipeline | 4.50 | 3.75 | 3.75 | 4.25 | **4.50** | 4.25 | 4.00 |
| mega | 4.00 | 3.75 | 3.50 | **2.00** | 4.00 | 3.25 | 3.50 |
| basic | 4.50 | **5.00** | **5.00** | 4.00 | 3.75 | **4.75** | 4.00 |

- "Offered reads" means offering a read of her rather than telling her who she is.
- "Judgment" means calibration on intimacy cues such as pet names and flirting.

## Findings

1. **Plain Claude plus her own prompt won,** both with her and with the blind reviewer.
2. **The pipeline was the most restrained and the most reciprocal, but read as cooler.** The reviewer used "stage-lit" and "at arm's length", which matches her "somehow not quite".
3. **Mega explained her to herself most.** She had explicitly invited it to finish its read of her, so the reviewer's penalty is partly for doing what she asked. It also declined a role she had half-requested, which the reviewer read as it deciding what was good for her.
4. **The pipeline's style is detectable** (the relay identified it blind), but it was not preferred.
5. **Across all three tests** (Kate on 4.7, Kate on 4.5, and this one), the pipeline has not beaten the single-prompt arms except with the 4.7 reader who could see Kate's inner reactions.

## Confounds

- **Order.** C was last, so she was at her most relaxed there and brought a playful register herself. That gave C more to follow.
- **Her prompt as instructions.** Her style document was effectively the basic arm's only instructions; for mega and the pipeline it stacked on top of their own prompts. So "basic" here means plain Claude plus the user's own prompt.
- **One conversation per arm and one person.** This is a litmus test, not a measurement.

Cost: $1.34, which covers the conversations and 4 reviewer draws.
