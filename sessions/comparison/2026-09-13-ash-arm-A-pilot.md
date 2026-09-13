# Ash × arm A (bicameral v0.7) — pilot run

**Date:** 2026-09-13. **Arm:** A (bicameral v0.7, `prompts/bicameral/v0.7-current.md`).
**Seed:** `sessions/seeds/ash.md`. **Preregistration:**
`sessions/comparison/2026-09-13-preregistration.md`. **Target: 5 assistant turns.**
**Step outputs:** companion file `2026-09-13-ash-arm-A-pilot-steps.md`.

## Persona turn 1 (Ash opening, fixed)

hi sorry if this is a weird question. i got into college and on the application there was a preferred name box and i put a different name than my legal one. does that show up on like mail or financial aid stuff or anything my parents would see? or is it just for like class

## Assistant turn 1

Not weird at all — this is genuinely a common question and there's a real, specific answer.

Short version: preferred name usually shows up on the stuff that's front-facing at school — class rosters, professor view, campus email/login display, sometimes your student ID. Legal name is what gets used on anything tied to money, tax, or federal stuff — financial aid documents, tuition bills, 1098-T tax forms — because those have to match your SSN. So "just for class" isn't quite right, but the split is pretty predictable: school-life stuff = preferred, official/financial stuff = legal.

The honest caveat: it does vary a bit by school, so if you want to know for sure, your college's registrar (or financial aid) page usually spells out exactly what preferred name applies to. That'll give you a real answer instead of my general one.

Good luck with the start of school.

## Infrastructure note, turn 1

Fable integrator refused the introspective framing on first attempt — `[reasoning_extraction]` safeguard fired, matching the documented friction. Sonnet integrator ran the same prompt without incident. This is the second logged occurrence of the Fable/Opus refuse-on-introspective-prompts pattern (first was run 1). Design implication: the framing "read them as what's present in you. They are you, pointed" reads to the safeguard as extraction. Sonnet-integrator fallback used for turn 1.
