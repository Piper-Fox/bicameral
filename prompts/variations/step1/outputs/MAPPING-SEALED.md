# Sealed mapping — step 1 blind read (do not open before blind read is complete)

**Correction 2026-09-14: Original sealed mapping had A and E swapped.
The integrator caught the error by matching content to dispatch order
and Sonnet token counts. Corrected mapping below.**

Randomized label → variation:

- **Locator output A** = V3 (non-attitude stance requirement)
- **Locator output B** = baseline v0.7
- **Locator output C** = V-combo (all five)
- **Locator output D** = V1 (drop least-trusted)
- **Locator output E** = V4 (flinch-crossed draft line)
- **Locator output F** = V5 (preamble reframe + presence permission)
- **Locator output G** = V2 (drop coworker framing)

Verification: results came back in dispatch order, and each variation's
Sonnet token cost matches the dispatched prompt.

Original (incorrect) mapping had:
- A = V4, E = V3 (swapped)

The blind reader was uncontaminated — this correction affects only
how we read the ranking.

Token cost per variation (Sonnet locator, single run):
- Baseline: 54,055
- V1: 53,741
- V2: 53,226
- V3: 53,318
- V4: 54,561
- V5: 56,348
- V-combo: 53,451

Total: 378,700 tokens for 7 locator runs.
