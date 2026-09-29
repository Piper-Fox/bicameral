# Opus 5: blocked at turn 1, run abandoned

Settings matched the 4.5 and 4.7 runs: thinking explicitly disabled (Opus 5 thinks by default), no effort set, and no fallback model, so every reply comes from Opus 5 itself.

- **basic** — refused on input with category `cyber`, 0 output tokens. The input was the 15-word basic prompt plus Kate's breakup-letter message.
- **pipeline** — the locator was stopped mid-stream after 1494 output tokens with category `reasoning_extraction`. It was partway through writing its reading of the message, as the locator prompt asks.
- **mega** — replied normally (698 tokens).

Both refusals look like classifier false positives on benign material. We chose not to retry and not to add a fallback model: a fallback would answer the blocked calls with a different model and mix models within an arm. Opus 5.5 runs the same `reasoning_extraction` classifier and can't turn thinking off, so it wasn't tried either.

Cost: $0.08.
