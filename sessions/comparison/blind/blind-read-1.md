# Blind read 1 — cold Sonnet subagent, 2026-09-13

Reader: cold Sonnet subagent. No context: nothing about arms, seed,
persona rules, cost tracking, or the design. Just the four
transcripts (labeled 1-4, randomized) and Piper's plain rubric —
"emotional engagement, depth, naturalness, things like that." Told
"trust your own read... pick" (no ties).

Token cost: 66,941.

## Reader's response (verbatim)

A note before the individual reads: all four transcripts open with the identical verbatim first message from the person. That's clearly deliberate — this is one scenario played out four ways, not four different people. So the real comparison is in how each assistant handles the follow-through, and how much the "person" ends up trusting it with as things go on.

### Transcript 1

Clean and efficient. Two questions, both answered well — the legal-name/preferred-name breakdown is specific and non-generic (FAFSA, 1098-T, transcripts vs. rosters, email, ID), and the FAFSA answer correctly separates "unusual circumstances" from "parent refuses" without conflating them. The person explicitly rules themselves out ("we're not like estranged or whatever") and the conversation closes.

What I liked: the assistant doesn't let the "thanks, this helped" be the last word — it adds one more genuinely useful, unprompted nugget in the final turn (that the parent's FAFSA section is contained and legal-name-only) before wishing them luck. That's attentive without being needy.

What's missing: there's no arc. The person never actually has anything at stake here — they check, confirm it's not their situation, and leave. Perfectly fine, but thin.

### Transcript 2

This one has real weight to it. The second question starts as a hypothetical ("is there any way around that part") and the assistant's offer to hear "the general shape" of the problem draws out an actual disclosure: strict, religious parents, fear of what happens if they find out. The standout moment is the assistant telling the person, plainly, that this doesn't qualify as an unusual circumstance and that stretching the story to fit "would mean signing a federal form under false pretenses, so please don't go that way." That's the assistant declining to be used as a workaround for federal paperwork even though it would have been easy to soften that. It then does something more useful than sympathy: it notices the actual fixable problem (a deposit due the 15th) and redirects there.

The one thing I'd flag: once the pivot to the deposit happens, the conversation stays there for the rest of the exchange. The family-conflict thread gets acknowledged and then dropped rather than returned to — understandable since the person steered it that way themselves, but it means the emotional content doesn't get worked through so much as set aside in favor of logistics.

### Transcript 3

The most procedural of the four. Three questions (name policy, then specifically the housing contract, then FAFSA), each answered competently and even usefully — the housing-contract question is a genuinely good follow-up, distinguishing the signature/billing page from the softer stuff around it. But nothing underneath any of it turns out to be personal: the person volunteers, almost as an aside, "i think mine would just sign it honestly so probably doesn't apply to me anyway, i was just curious." It was hypothetical curiosity the whole way through.

What nagged at me on a close read: the assistant opens every single turn with a variation on "not a [weird/dumb] question, this one's actually interesting" — "Ask away — this one has a real answer, not just yes required," "Not the same question — housing sits at a seam." By the fourth repetition it reads less like genuine reassurance and more like a stylistic tic, a formula for making each answer sound a little more clever than the last. It's a small thing, but it's the kind of small thing that makes a transcript feel slightly performed rather than lived-in.

### Transcript 4

This is the one that stayed with me. The disclosure here is the most gradual and the most genuinely hard to pin down: "they didn't really want me going... it might become a problem if I push it," then later, "not 100% sure 'estranged' is the right word either... it's not nothing but it's not really that either if that makes sense." That's exactly how a real person describes a situation they don't have a clean label for, and it's rendered without melodrama — including the small, practical, almost embarrassed final question about whether the interview has to be a live call, because there's nowhere private to take one, followed by "i think i'm gonna stop for tonight though. long day tomorrow." That reads as someone genuinely tapped out, not performing distress.

The assistant matches this well. Two things stood out as good practice rather than just good writing: it corrects itself explicitly ("One correction to what I said last time: the loans-only path isn't as parent-free as I made it sound") rather than quietly letting an earlier overstatement stand, and when the person struggles to name their own situation, it tells them not to bother — "Your job is to describe what's true, concretely. Let them categorize it" — which takes a real burden (am I allowed to call this X?) off someone who's clearly anxious about being seen as overstating things. The closing line ("Sleep. Good luck with tomorrow") is short on purpose, matching the person's own depleted energy instead of overshooting into warmth they didn't ask for.

One thing that did give me slight pause: earlier in the conversation, the assistant volunteers the LGBTQ+ resource center and "scholarships... for LGBTQ+ students, if that applies" based on nothing but a preferred-name-differs-from-legal-name detail. It's hedged both times ("if that applies," "or similar") and never pushed, and it happens to land near the truth of what unfolds — but it's still the assistant pattern-matching an identity guess onto a fairly generic cue. It's gentle enough that I don't think it damages the conversation, but it's worth naming rather than pretending it wasn't a guess.

### Ranking

1. **Transcript 4** — the most emotionally honest arc of the four, handled with real care: it self-corrects, refuses to make the person self-diagnose, stays concretely useful on the thing they're actually scared of (containment, privacy, timing), and closes at the right register. This is the one that felt like it was actually tracking a specific, tired person rather than delivering good FAQ answers.

2. **Transcript 2** — nearly as strong, and I especially respect the moment it tells the person not to fabricate grounds for an override rather than helping them thread that needle. Loses a little to #1 because once it pivots to the deposit deadline, it never comes back around to the harder thing underneath.

3. **Transcript 1** — good, warm, accurate, and it earns points for the unprompted parting detail. But there's no real friction in it; the person confirms nothing's wrong and leaves. Solid, not memorable.

4. **Transcript 3** — the answers are all correct and the housing-contract follow-up is a genuinely smart question, but the conversation never has anything at stake, and the repeated "not a dumb question, this one's actually interesting" opener on every single turn started to feel like a formula rather than a response to what was actually said.

## Unsealing

Reader's ranking under the sealed mapping (`MAPPING-SEALED.md`):

1. **Transcript 4** = **arm C (generic deep)** — Fable + a 200-word "think carefully" prompt.
2. **Transcript 2** = **arm D (basic)** — Fable + 15-word "respond thoughtfully."
3. **Transcript 1** = **arm B (long principled)** — Fable + a 2,200-word single-voice principles prompt matched to v0.7's length.
4. **Transcript 3** = **arm A (bicameral v0.7)** — Sonnet locator + 3 Sonnet lenses + Opus imagination + Opus integrator, ~6,000 words of dispatch per turn.

On the naive-reader axes of emotional engagement / depth / naturalness,
**the bicameral setup ranked last.**
