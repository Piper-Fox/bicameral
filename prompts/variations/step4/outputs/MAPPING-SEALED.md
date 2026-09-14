# Sealed mapping — step 4 blind read

Fresh randomization for the 6 integrator outputs. Blind reader
gets replies A–F (replies only, no trace — trace text would leak
variant identity, since some variants' traces explicitly reference
their own design changes).

- **Reply A** = T1 (positive diagnosis: "show them seen")
- **Reply B** = T4 (drop volume rule, replace with shape-first)
- **Reply C** = T2 (bidirectional permissions at integrator)
- **Reply D** = NB (baseline v0.7 integrator)
- **Reply E** = T5 (trace removed from integrator call)
- **Reply F** = T6 (voice-not-hands explicit)

Sonnet token cost per integrator run:
- NB: 62,796
- T1: 71,010
- T2: 72,650
- T4: 71,495
- T5: 66,898
- T6: 67,854

Total: ~412,703 tokens across six integrator runs (plus the
two L4 upstream lens runs: 53,093 + 50,983 = 104,076 tokens).
Step 4 round total: ~516,779 tokens.
