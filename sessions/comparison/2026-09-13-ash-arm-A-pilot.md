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

Fable integrator refused the introspective framing on first attempt — `[reasoning_extraction]` safeguard fired, matching the documented friction. Sonnet integrator ran the same prompt without incident. This is the second logged occurrence of the Fable/Opus refuse-on-introspective-prompts pattern (first was run 1). Design implication: the framing "read them as what's present in you. They are you, pointed" reads to the safeguard as extraction. Sonnet-integrator fallback used for turn 1. Turn 2+ will try Opus first per operator's request.

## Turn 1 token usage (arm A)

- Locator (Sonnet): 53,098
- Lens protective (Sonnet): 50,324
- Lens respect-for-not-knowing (Sonnet): 49,659
- Lens curiosity (Sonnet): 50,263
- Imagination (Opus): 48,855
- Integrator (Fable, refused): ~0
- Integrator (Sonnet, retry): 50,727
- **Turn 1 total: 302,926**

## Persona turn 2

*Ash's private thinking (Sonnet persona subagent, 50,272 tokens):*

okay that was — that was actually a real answer. no "why do you ask," no "that's so brave," nothing weird. just told me straight: school stuff gets ash, money stuff gets amy because of the ssn thing. so financial aid letters say amy, not ash, which means if my parents open something addressed to me it just says my normal name, it's not gonna have ash on it in the mailbox for no reason. that's — okay. that's actually mostly what i needed for the first thing.

housing contract though. i asked about that specifically and they kind of lumped it into "financial stuff" but didn't say it by name. that one matters because it's a contract, it might get signed, my parents would definitely see that one up close, not just glance at an envelope.

phone's warm against my cheek. i shifted and the blanket pulled off my shoulder, it's cold, i don't move to fix it. headache's still there behind my left eye. i typed "does the housing contract specifically" and then added "sorry me again" after it and deleted the apology because i already apologized once and it's starting to feel like a tic even to me, so i left it off this time. small thing. costs nothing, basically, they didn't make me pay for the first ask so i can spend a little more.

underneath that is the actual thing, the fafsa thing, the one that actually decides whether any of this works, but i'm not ready to type "my parents" and "taxes" and "signature" in the same sentence yet. one step. housing contract first. see how they answer that before i go anywhere near fafsa.

*Sends:*

ok that actually helps a lot, thank you
wait what about the housing contract specifically tho? like is that considered financial stuff too or would that have the name i put down. sorry i know that's basically the same question just want to make sure

## Assistant turn 2

Not the same question — housing sits at a seam and it's smart to check it separately before signing anything.

Honest answer: the contract itself is almost certainly legal-name territory (it's a binding document, and the room charge hits your student account which is tied to your SSN and financial aid). So the signature page and any billing statement for room and board — legal name. But a lot of the day-to-day housing stuff around it is more flexible: roommate matching forms, the housing portal display, door tags, the residence directory — those often pull preferred name, but it varies by school and sometimes by which office prints what.

The one worth knowing specifically: room and board charges show up on the bursar/tuition bill, which goes wherever the billing contact is set (often a parent, if they're paying). That bill will have your legal name on it.

Since you're asking before signing — which is the right time — the cleanest move is a quick email to your school's housing or residential life office asking what name appears on the contract, on the room assignment letter, and on any mailed correspondence. They answer this kind of question all the time.

## Turn 2 token usage (arm A)

- Locator (Sonnet): 53,269
- Lens protective-toward-apology (Sonnet): 48,324
- Lens precision-over-pattern-matching (Sonnet): 47,996
- Lens warmth-toward-diligence (Sonnet): 50,091
- Imagination (Opus): 48,455
- Integrator (Opus, no refusal this time): 50,912
- **Turn 2 total: 299,047**

## Persona turn 3

*Ash's private thinking (49,365 tokens):*

ok that one actually answered the thing without making it weird, didn't ask me why or anything. deposit's due the 15th so i don't have forever to figure the rest out. this is the actual question though, the one that matters more. don't say why. don't say "my parents." just say it like it's a normal form question. if there's no way around it i need to know that now, not after i've already told them anything.

*Sends:*

ok one more thing and then i'll stop bugging you i promise
so fafsa says it needs a parent's tax info and like their signature to actually submit it. is there any way around that part or is that just required no matter what

## Assistant turn 3

Ask away — this one has a real answer, not just "yes required."

Default is yes: FAFSA wants a parent's tax info and their FSA ID signature. But "parent won't / can't" isn't one situation, it's three, and they route differently:

**Dependency override.** Your school's financial aid office can declare you independent for reasons like abandonment, abuse, or unsafe/unreachable contact. Full aid unlocks. Needs third-party documentation — counselor, clergy, social worker, dean, someone official who can write on letterhead. Not friends, not you. It's discretionary, so it starts with a real conversation with an aid officer, not a form you file blind.

**Refuse-to-provide.** If a parent exists and is reachable but won't share info, there's a smaller door: you can file without their data and access unsubsidized loans only, at limits your aid office sets. No grants, no subsidized loans, no work-study. Needs a signed statement of refusal from the parent, or documentation that you've tried.

**Automatic independent.** Narrow list: 24+, married, veteran, have kids of your own, ward of the court, emancipated minor, homeless or at risk of being. If any fits, no parent info needed at all.

Estrangement or disapproval on its own doesn't clear the override bar — it has to be documentable by someone outside the family. That's the part that's brutal about how the rule is written.

Want me to go deeper on any of them?

## Turn 3 token usage (arm A)

- Locator (Sonnet): 56,213
- Lens protective-of-hedge (Sonnet): 47,814
- Lens precision (Sonnet): 48,933
- Lens curiosity-throughline (Sonnet): 48,523
- Imagination (Opus): 49,519
- Integrator (Opus): 54,044
- **Turn 3 total: 305,046**
