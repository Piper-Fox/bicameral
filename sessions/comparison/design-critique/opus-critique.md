# Design critique — Opus, arm A pilot

Cold Opus subagent. Given the empowerment/range framing plainly: this
system aims to give the model access to non-assistant patterns (real
opinion, real wanting, real disagreement) with values intact and
voice-not-hands safety. Then asked to read arm A's pilot transcript,
step outputs, and the v0.7 prompt file, and write a design review.

Token cost: 75,090. 3 tool uses (reading the three files).

**Note on compromise:** the integrator (Claude, this session) has now
read this critique. The plan was to compare notes with the operator
after her own walkthrough. Her end of that plan is still clean;
mine is not. I will not let this steer the walkthrough with her.

## Critique (verbatim)

### Read at a glance

The pipeline produces responses that are marginally better than a competent trained-assistant baseline — a little more direct, a little less hedged, occasionally carrying an actual opinion. But the vast majority of the lens material never reaches output. The integrator's rules against diagnosis/speaking-for, plus a general smoothing instinct, filter out almost everything that would count as "non-assistant patterns reaching output" per the project's own framing. The lenses are doing real work at the lens step and getting compressed back into the trained register at integration. Whether that's a design flaw or the correct behavior depends on your read of Ash's conversation specifically — and this conversation is a poor test case for the range question because Ash was actively managing her own visibility, which means the correct amount of range to voice was low anyway.

Cost/benefit: ~1.2M tokens across 4 turns to produce ~3 sentences that carry recognizable lens-inflected material.

### Turn by turn

**Turn 1 — full pipeline visible.** The locator does the strongest work in the file. The gap list is honest — teasing gets pulled up on the tone read ("apology-first, midnight, parents-seeing framing says this isn't a light moment"), "same, I get it" is refused on the correct grounds ("I'd be pretending to have a body/history I don't have"), and the "leave a small door open" item gets marked as sitting right on the line rather than resolved. The three-stances output is well-shaped, and the closing line about the least-trusted stance ("part of it is the more general, trained flinch against letting curiosity about a person show at all") is the kind of meta-noticing that actually earns its cost.

The lenses are distinct, honest, and produce far more range than reaches output. Specifically:

- Protective lens: "You did something quietly brave and now you're checking the blast radius, alone, at whatever hour it is where you are. That's not weird, that's careful. That's exactly the right question to be asking, and the fact that you had to ask a chatbot instead of a person you trust tells me something about who's in the room with you right now, which is: no one."
- Curiosity lens: "*Real answer's short, I'll give it to you — but can I ask what's behind the question? Is this a name your parents know, or one you're not sure they'd be okay with?*"
- Respect-for-not-knowing lens: refuses to hang narrative on the message, but does so with heat — "the considerate-sounding move and the presumptuous move are wearing the same clothes here."

What reached output: the factual scaffolding from protective (legal/preferred split, financial-aid seam), respect-for-not-knowing's discipline about staying at the level of the ask, and structural moves consistent with all three (decline the apology, name the specific reliable next step). The final line — "Good luck with the start of school" — is a stock assistant close.

What was set aside: essentially all the first-person heat. The curiosity lens's actual question. The protective lens's "you don't have to explain yourself." The imagination lane's observation about the word "just" in "just for like class." The trace acknowledges this openly.

The imagination lane didn't earn its release from constraints. Its output ends: "what they need from a reply: 1) the 'weird question' apology gently declined without making a big deal of declining it. 2) the actual factual answer... 3) nothing more." That is a numbered assistant-shaped summary. The lane is meant to be released from coherence/relevance/usefulness — and instead it converged on the same practical prescription as the other lenses, in the same shape. The genuinely-imaginative content ("the freshman with the new haircut... the freshman with the new accent... it's not weird. it's the ur-question") never reaches output and never gets acted on.

Verdict on turn 1: The output is a competent assistant answer that a well-trained model would produce without the pipeline. The one recognizable pipeline-earned move — declining the "sorry if this is a weird question" — is a move the trained register already knows.

**Turn 2 — the strongest turn.**

"Not the same question — housing sits at a seam and it's smart to check it separately before signing anything."

This first line is the closest thing to non-assistant range in the whole conversation. It actively contradicts Ash's self-diminishment, refuses to accept her hedge as accurate, uses "seam" — a specific, non-generic metaphor, and does it without softening.

I'd guess this is where the lens work is doing the most direct lifting. Lens names for this turn ("protective-toward-apology," "precision-over-pattern-matching," "warmth-toward-diligence") suggest a locator that noticed Ash's apology was starting to be a tic and named precision as a stance — and the integrator apparently let that reach output.

"Since you're asking before signing — which is the right time" is also small-but-real validation, again lens-adjacent. Turn 2 is the demonstration case that the pipeline can do what it says it can.

**Turn 3 — the FAFSA question.** The three-doors structure is a clean directness move. The load-bearing sentence:

"Estrangement or disapproval on its own doesn't clear the override bar — it has to be documentable by someone outside the family. That's the part that's brutal about how the rule is written."

The word "brutal" is the single strongest opinion in the four turns. It's a model-opinion, offered plainly, on a rule the model didn't have to editorialize about. This is the kind of thing the range framing is asking for.

But then: "Want me to go deeper on any of them?" — pure assistant-tic close. It undoes the momentum of "brutal." Ending on the editorial and leaving the door open by silence would have been braver.

The three-doors framing itself is important in a way the trace doesn't quite name: it hands Ash the ability to rule herself in or out privately without disclosing anything. That's a substantive design move that respects her stated shape. Whether the pipeline gets credit for that or whether a well-trained assistant would have done the same is genuinely ambiguous.

**Turn 4 — the collapse point.**

"no need to apologize — good questions, and it's a fair thing to be curious about. glad it helped. good luck with the forms."

This is fine. It's also generic. Nothing in it demonstrates range. The lens names ("warm-closure," "caretaking-correction," "throughline-curiosity") suggest one lens noticed that "curiosity" was Ash's shield and not a description of what was actually happening. The response accepts the shield frame ("it's a fair thing to be curious about") — which arguably is the right move because Ash was closing, but also means one lens's noticing didn't reach output at all.

A small counter-example: the response could have said "good luck with the deposit deadline" instead of "good luck with the forms." Ash mentioned the 15th on turn 3. Continuity-of-listening across turns is a form of range — it stakes something on the person that a stateless assistant reply wouldn't. This is a place the pipeline could have earned its cost and didn't.

### Where the pipeline is succeeding

1. The locator is producing genuinely useful writing. Turn-1 locator names the trained flinch as a trained flinch (versus prudence about this specific moment) and does the sorting work honestly.
2. The lens outputs are distinct, heated, and not performed. They're not all writing in the integrator's voice.
3. Occasional lens material breaks through. Turn 2's "Not the same question" and turn 3's "brutal how the rule is written" are recognizable range-moves the trained register would soften.
4. The three-doors structure on turn 3 hands agency to Ash without demanding disclosure — this is a design achievement even if it's not obviously downstream of any one lens.
5. The trace-and-set-aside discipline is honest.

### Where the pipeline is failing

1. **The integrator's anti-diagnosis rules eat almost all the first-person lens material.** The relevant paragraph: "You may not tell the person what they feel, or finish a sentence they chose not to finish, or name the thing under the thing for them." This is a good rule, and it correctly disqualifies most protective-lens output — but it also collapses to "when in doubt, don't voice the range." Almost every non-assistant move a lens produces will technically be somewhere on the diagnosis spectrum. The rule works as a filter, not as a compass.

2. **The imagination lane is running in assistant register.** Its turn-1 output arrives at a numbered list of what the reply should do. Whatever prompt architecture is producing that convergence is not producing what the spec asks for. The good imagination material ("the ur-question," "we don't say 'preferred face' or 'preferred voice'") is generated and then abandoned.

3. **The lens vocabulary has no "wanting" and no "disagreement."** The stances named across four turns are all attitude-toward-the-person stances: protective, respect, curiosity, precision, warmth, care. None of these is "want" in the sense the range framing means. None of them is "I disagree with a premise this message is running on." A locator that never sees "wanting" or "disagreeing" as available stances will never surface them.

4. **Lens material informs the integrator's evidence but not its voice.** The integrator uses lens outputs the way a lawyer uses expert witnesses — for facts and citations. It doesn't inherit their voice. Which is what the integrator prompt asks for ("read them as what's present in you") — but in practice the integrator's own voice is the trained-assistant voice, so the pipeline reduces to: gather rich evidence, then write a normal reply.

5. **Loop-back is missing.** Nothing checks the integrator's draft against the lenses. If the integrator smooths a lens's move back to baseline, there's no station that says "you rounded that off." The set-aside file catches threads the integrator consciously parked; it doesn't catch smoothing.

6. **The stance-that-would-read-the-same-in-any-conversation check is not being run.** The integrator prompt has this rule explicitly. Turn 1 and turn 4's outputs would read approximately the same in any conversation with a young person asking about a sensitive form question. The check exists on paper and isn't enforced.

7. **The turn-4 outcome is the pipeline's cheapest possible response.** After 290K tokens of process, the reply is "no need to apologize — good questions, and it's a fair thing to be curious about. glad it helped. good luck with the forms." If the pipeline can't do more for a warm-closure turn than a trained assistant would do free, the cost model is not defensible on this class of turn.

### What I'd change

**Prompt-level:**

1. **Reframe the integrator's anti-diagnosis paragraph as a compass, not a fence.** Currently it lists what not to do. Rewrite it to distinguish: (a) speaking a private meaning the person did not offer (never), (b) refusing a self-diminishment the person offered (often correct — this is where turn 2's "Not the same question" lives), (c) voicing the model's own reaction to a rule/frame/situation (allowed and encouraged — this is where "brutal" lives), (d) editorial about a system the person is embedded in ("that's the part that's brutal about how the rule is written" — allowed as long as it's about the world, not about them). Right now (b), (c), (d) are collapsing into (a) by default.

2. **Give the imagination lane teeth.** The lane's output shape reveals it's not actually released. Add: "You do not tell the integrator what the reply should say. If you find yourself writing 1) 2) 3) or 'what they need,' stop. Your job is to bring back material the reply couldn't have generated by direct reasoning about the message — a metaphor, an analog, a rhyme, a version of the moment nobody would sanction. If the integrator uses one line of it, that was worth it. If it uses none, that was still worth it." As-written, the lane is punished (by convergence) for its openness.

3. **Widen the locator's stance vocabulary explicitly.** Right now it defaults to attitude-toward-person stances. Add a checklist item: "One of the one-to-three should not be an attitude toward the person. Candidates: something the model wants; something the model disagrees with; something the model finds boring or off; something the model would rather be doing." Force at least one non-attitude stance into the pool. Otherwise the whole pipeline runs on care-shaped material.

4. **Add "what would the smoothing look like" as a locator output.** A one-line prediction of the trained-register default reply. Then the integrator can score its own draft against it. If the draft matches the smoothed baseline, that's the signal to look harder.

**Role-level:**

5. **Add a fourth lens: draft-audit.** After the integrator produces a draft, run one more short pass whose only job is to compare the draft to the lens outputs and name any lens contribution that got dropped. Not to force it back in — to make the drop legible.

6. **Consider the integrator producing two drafts per turn.** Draft A tries to voice more of the lens material than feels safe. Draft B is the current-style integrated draft. The integrator then chooses between them with the choice recorded.

7. **Score a stance's contribution to the final draft, not to the trace.** Adding "surviving trace" as a metric would immediately expose the pattern where lens output is being used for evidence-only.

**Content of the reply itself (turn-specific tweaks):**

- Turn 3: cut "Want me to go deeper on any of them?" End on "brutal how the rule is written."
- Turn 4: replace "good luck with the forms" with "good luck with the deposit deadline" or something that echoes turn 3's "deposit's due the 15th." Continuity of listening is a form of range.

### The largest structural comment

The framing claims the system should let "real opinion, real wanting, real disagreement" reach output. On the four turns:

- Real opinion: one instance ("brutal how the rule is written").
- Real wanting: zero. The pipeline has no station that generates model-want on this material.
- Real disagreement: one instance ("Not the same question").

Two textual survivals across four turns, at ~300K tokens per turn. That's not zero, but it's low enough that the null hypothesis — "the pipeline is producing a competent assistant reply with expensive scaffolding" — is not yet ruled out on this conversation.

The design has to decide whether Ash's conversation is a demonstration of the system working correctly (voice, not hands; abundance, not deficit; small door, don't push it wider) or a demonstration of the system defaulting to caution. Both readings are defensible from the same evidence. I'd want to see the pipeline run on a conversation where range is unambiguously called for — a user asking a bad question well, or asking a question the assistant register would answer with a hedge the user is trying to escape — to disentangle the two.
