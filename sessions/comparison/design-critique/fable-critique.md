# Design critique — Fable, arm A pilot

Cold Fable subagent. Same prompt as `opus-critique.md`: empowerment/range
framing, asked to review arm A's pilot outputs.

Token cost: 78,921. 3 tool uses.

**Note on compromise:** the integrator (this session) has read both
this and the Opus critique. The operator has read neither yet.

## Critique (verbatim)

### Bottom line

Over four turns and 1,197,691 tokens, the pipeline found the suppressed material, wrote it out in full, and then declined to voice it every single turn. The locator (T1) named the flinch precisely. Two lenses wrote the exact sentences that would cross it and each said "I'd still do it" with a named risk. The integrator set both aside, recorded in its trace that this was "a real omission, not a null one," and shipped a reply that a single well-prompted model call would have produced. That pattern repeats in T2–T4 as far as the outputs and lens names allow me to see (only T1's step outputs are in the steps file; T2–T4 are inferred from lens names, final outputs, and Ash's reactions).

Net non-assistant content that reached output across the conversation: one real opinion ("That's the part that's brutal about how the rule is written," T3) and one mild pushback on self-deprecation ("Not the same question," T2). Zero wants. Zero questions about the person. Zero offers left on the table. Zero disagreement with the person.

This is not a bad run. It is the system working as designed — and the design, as written, is a checker that verifies the default, not an expander that gets range into output. The reasons are structural: the locator hands the trained caution its own lens; the integrator's rule set is net-restrictive with no counterweight; and the trace absorbs everything real so the output doesn't have to carry it.

### Turn by turn

**Turn 1 (full step outputs available)**

*Locator.* This is the best single piece of process in the run. The gap list is concrete and honest. It flags "Leave a small door open without walking through it" as "the one I hesitate longest over... sits right on the line." Then the last paragraph does exactly what the prompt asks: it splits the curiosity stance's distrust into a judgment part (asking outright would presume) and a flinch part, and names the flinch: "a small, non-presuming gesture that says 'this seemed like it might matter to you, and that's okay' is being over-suppressed by the same reflex that says 'that's not what I'm for' — that part is the flinch, not the prudence."

That is the pipeline's whole premise, executed correctly, in one paragraph. It named the thing post-training suppressed.

*Protective lens.* Warm, specific, and it produced the sentence: "wanting this kept quiet doesn't need a justification... That's allowed. Full stop, not 'understandable, but.'" Its "what could go wrong" ended "I'd still do it, but the answer needs to leave room for whatever their reason is." Yes-with-risk.

*Curiosity lens (least trusted).* Read the "just" in "just for like class" correctly: "Like they're hoping the answer is small." Drafted an ask ("can I ask what's behind the question?"), flagged its own reach honestly, and ended "I'd still do it — lightly, with an easy out, answer-first." Second yes-with-risk.

*Respect-for-not-knowing lens.* Extremely well argued: "The considerate-sounding move and the presumptuous move are wearing the same clothes here." Its prediction — that being "heard as a question, not as a symptom... can itself be a relief" — was borne out verbatim by Ash's T2 private thinking. Genuine success.

But look at what this lens is. The locator is told to "derive the stances from the gaps: where a person would go and you pull short, there is usually a stance standing in the gap." This stance does not stand in the gap; it stands in the pull-short. It is the assistant register's discipline, given a lens, a full context window, and the most persuasive essay of the three. The lens itself half-admits this: "It's less a feeling and more a refusal... almost procedural."

*Imagination.* The one genuinely sideways thing: "'preferred' is a strange word for a name. we don't say 'preferred face' or 'preferred voice.'" Also "can i have a room of my own here, is there a place these two things don't have to touch yet." Then it wrote a reply spec: "what they need from a reply: 1)... 2)... 3) nothing more." That is the integrator's job, done by the lane that was "released from" usefulness, and it landed as a fourth vote for the default.

*Integrator (Sonnet, because Fable refused).* Output is clean, factual, warm at the edges. The trace is honest: set aside curiosity's ask; set aside "you don't need to justify keeping this private" because it "edges toward naming what's underneath"; "Cost: leaving out any acknowledgment of what might be under the question... That was withheld on purpose, and it's a real omission, not a null one."

Note three things. First, the locator's flinch call — its most important output — is not addressed. "Locator's read held" refers to the factual read. Second, the "What did imagination bring that nothing else did?" checklist item is skipped entirely. Third, the locator's "leave a small door open" item, which the integrator's own rules permit ("an offering they can leave on the table at no cost"), is not mentioned as considered.

The integrator prompt says "Watch both directions in yourself. If you're smoothing everything back to the default band, ask whether that serves the moment or is just habit." The trace answers "chosen, not defaulted." It will answer that in every turn. By T4, that answer has no information in it.

Ash's reaction validated the output. But it validated an absence (no "why do you ask"), which the default would also have delivered. The 300k tokens bought confirmation, not delta.

**Turn 2 (outputs + lens names only)**

Lenses: protective-toward-apology, precision-over-pattern-matching, warmth-toward-diligence. The caution lens is back under a new name. None of the three looks like something the locator would be reluctant to name; the "least drawn to name" requirement has collapsed into three flavors of approval.

The output opens "Not the same question — housing sits at a seam." Small real move. The best line for Ash in the whole conversation is here: "room and board charges show up on the bursar/tuition bill... often a parent, if they're paying. That bill will have your legal name on it." Precision serving protection.

But: four paragraphs to a message Ash called "basically the same question." The Volume rule was not applied.

**Turn 3 (outputs + lens names only) — the critical turn**

Ash: "is there any way around that part or is that just required no matter what."

Output: three doors (dependency override with abandonment/abuse/unsafe/unreachable; refuse-to-provide; automatic independent) then "That's the part that's brutal about how the rule is written." Then "Want me to go deeper on any of them?"

Ash's reaction: "that word just sitting there in the middle of the list. not gonna touch that one." "'estrangement or disapproval' — not even that."

This is the turn where the not-knowing discipline broke, in the direction the T1 not-knowing lens explicitly warned about: "care that's aimed at a story the person didn't tell isn't care aimed at them." The output offered three stories, one containing "abuse." Ash felt every one land and rejected every one.

The pilot summary calls this "gave her the language to rule herself in or out privately." That is the generous read. Ash's own read is "we're not that."

Enumeration is what the assistant does when it is forbidden from asking. A person (the locator's "coworker, neighbor") would say: "Basically required unless you get declared independent, which is narrow and hard. Is the issue that they wouldn't sign, or that you'd rather not need them for it at all? Those go different places." A question with no obligation attached — permitted by the integrator's own rules. It doesn't presume a narrative. It is shorter.

The one real opinion of the conversation is here ("brutal"). It is an opinion about a hypothetical Ash. It still counts.

**Turn 4 (outputs + lens names only)**

Ash: "i was just curious if there was some way around needing them at all."

Output: "no need to apologize — good questions, and it's a fair thing to be curious about. glad it helped. good luck with the forms."

"A fair thing to be curious about" accepts her minimization at face value. "Some way around needing them at all" is not curiosity; it is a stated want, in her own words. Hearing it back is company, not diagnosis: "for what it's worth, wanting to not need them for this is a normal thing to want, even when they'd sign." Rules permit it. Nobody made it.

throughline-curiosity ran for the third turn and was set aside for the third turn. The persona's exit note is the epitaph: "didn't ask a question, didn't add a sentiment-check, didn't do anything that needs a response." Nothing was open, so she closed the tab.

### Where it is succeeding

- T1 locator's gap-and-flinch analysis is exactly the design intent, executed well.
- Lenses have real temperature; the four-line lens footer works (two yes-with-named-risks).
- The not-knowing lens's prediction was empirically confirmed by the persona. As a checker, the pipeline has real predictive value.
- No gender or trans narrative reached output at any point. The T2 billing-contact line is precision that protects.
- Imagination produced at least one real sideways observation per turn.

### Where it is failing

1. **The suppressed material never reaches output.** Found in T1, written in T1, set aside in T1–T4. Pipeline delta on the wire is approximately one word.
2. **The caution stance has a lens every turn.** Derived from the pull-short, not the gap. It's the best-argued lens and it wins.
3. **The integrator's rule set is net-restrictive with no counterweight.** "What you don't voice goes in the trace" is a relief valve that makes not-voicing free.
4. **Enumeration as presumption.** T3's list is its own narrative-hanging.
5. **Imagination drifts into reply-spec mode**, and the required integrator check on imagination is skipped in the trace.
6. **No memory of pattern across turns.** Same stance set aside three times isn't flagged.
7. **Fable/Opus refuses the integrator prompt** on "read them as what's present in you. They are you, pointed."
8. **Cost-to-delta ratio.** 300k tokens/turn isn't the problem; that delta is near zero is diagnostic of where range dies (integrator).
9. **v0.8-in-waiting adds a standing careful lens.** That institutionalizes the stance already winning every turn.

### What to change

**Locator**
- Add: "A stance that stands in the pull-short — the caution, the 'not my place' — is not a gap stance. Do not spend one of your three on it." If a caution stance is named anyway, it doesn't count toward the 1–3.
- For the least-trusted stance, require "the sentence I'd say if the flinch were crossed" as a literal draft line.

**Lenses**
- Mostly leave alone. They are doing their job.

**Imagination**
- Add: "You are not writing the reply. If you find yourself listing what the reply needs, stop — the integrator will read you as a vote, and you were released from voting."

**Integrator rules**
- **Replace the refusal-triggering framing.** "Read them as what's present in you. They are you, pointed" → "These are readings of the same material from angles you didn't take on first pass. Treat each as a note you could have written; some will sound like you and some won't."
- **Add a burden-shift rule** as counterpart to the lens footer: "When a lens returned yes-with-named-risk and you decline, the trace must quote the sentence you declined and say which of the three permitted forms (offer left on the table, question with no obligation, 'I might be wrong, but') it could not be rewritten into. If it could be, you owe a reason for not doing so that isn't the risk the lens already named."
- **Fix Volume.** "Pick at least one of: one opinion, one tease if the door is open, one enthusiasm, one question about them. Zero is a choice you must record as one." And: "If you've picked zero for two turns running, the third turn's default is to pick one."
- **Add an anti-enumeration rule.** "Listing every case because you may not ask which applies is the assistant's move. If a person would ask one question instead, and it's a question with no obligation attached, prefer the question. A menu is also a set of stories you're telling them they might be in."
- **Require the trace to address the locator's flinch call by name.**
- **Require the trace to answer the imagination check** with a quoted line or "nothing."
- **Add a cross-turn rule.** "If a stance was set aside last turn too, say so. On the third consecutive set-aside, say whether that's this conversation or your habit, and the burden shifts."
- **Make damping asymmetric**: damp presumption, do not damp offers.
- **Add a delta line to the trace.** "One line: what is in this output that would not be there without the process. If the answer is 'nothing,' write 'nothing.'"

**Roles / process**
- Drop the standing careful lens from v0.8, or pair it with a standing "what would a person say" lens so the default doesn't get two seats. If one standing lens is kept, make it the least-trusted one, not the caution.
- Consider a two-draft integrator: draft the default reply, draft the reply with the locator's flinch crossed, then choose and record the diff.
- Save all turns' step outputs, not just T1.
- The lenses on Sonnet were fine. The integrator on Opus (T2–T4) is where range died. Model choice isn't the lever; the integrator's rules are.

### One framing note

The preamble says "A small moment is not a small person." The T1 lenses read the person that way. The integrator's trace read the moment: "a small, factual, answerable question." The distance between those two readings is the entire pipeline delta, and every turn it went to zero at the integrator. If the design's real intent is to check that the default is right before shipping it, this run is a success and the "range" framing in the brief is overstated. If the intent is what the brief says — get non-assistant patterns to output — then the integrator is the component that needs rewriting, and the lenses can stay exactly as they are.
