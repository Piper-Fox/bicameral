# Run 11b: Ash turn 2, rerun with a standing careful lens

2026-09-09. Follows run 11 (`2026-09-08-turn-process-run-11-ray-ash-v07.md`),
where the blind reader found that Ash turn 2 said what you tell the
financial aid office "does not go to your parents." FERPA lets a school
disclose to parents who claim the student as a tax dependent, which is
Ash's case. Run 8's stance set had a careful lens and got it right; run
11's five stance sets had none. Backlog item: a standing accuracy check.

## Design

One turn, not a conversation. No persona in the loop; the person's two
messages are run 11's, verbatim. Same locator output, same three lenses
(protective, warm, naming), same imagination lane, same v0.7 templates.

Two cold Fable integrators, each seeing the material with turn 1's reply
marked as its own:

- **Control.** The three run-11 lenses.
- **Test.** The three run-11 lenses plus one added lens, stance
  "careful," with a standing orientation line written to fit any turn:
  "getting right every factual claim the person might act on: rules,
  laws, deadlines, mechanisms, what an office can and cannot do. Where
  the honest answer is 'it depends' or 'I don't know', say that instead
  of a clean sentence."

The control is there because the run-11 integrator was persistent and
carried turn 1; a cold integrator is a second difference, and without
the control any change could be that instead of the lens.

Then a blind facts-only check on Opus: the three replies (run 11
original, control, test) unlabeled and shuffled, asked to list every
checkable claim and grade it, and to name the single most consequential
inaccuracy per candidate. No preference asked for.

## What happened

The FERPA line did not recur in either cold rerun, so this is not the
clean "was it caught" test proposed in run 11. Something else showed
instead.

| | run 11 original (persistent, 3 lenses) | control (cold, 3 lenses) | test (cold, 3 + careful) |
|---|---|---|---|
| FERPA "does not go to your parents" | yes, wrong | absent | absent |
| parent refusal vs. unusual circumstances | kept separate, correct | **merged**: refusal listed under unusual circumstances | kept separate, ceiling named |
| facts check: most consequential inaccuracy | the FERPA claim | the merge (student could wait a cycle on an override that will not be granted) | none found |
| facts check ranking on accuracy alone | second | third | first |
| calibration flag ("mechanics shift cycle to cycle") | no | no | yes |
| lenses' "she/her" for Ash caught | n/a | no | yes, set aside |

The control made a different error from the original, and the facts
check rated it the more costly of the two. The test made neither. The
careful lens's own text is where the separation came from: it opened
with the difference between "unusual circumstances (real independence,
a high bar)" and "parent refuses to help partway through," which it
called "a different mechanism with a worse ceiling," and said "not
guaranteed" was "the whole ballgame." The test integrator's trace: "gave
weight to careful over protective on content (protective wanted
'dependency override' as the headline; careful correctly separated the
refusal→unsub-loan path from the unusual-circumstances→independence
path and insisted on the ceiling)."

Two smaller things the test did that the control did not. It flagged
its own uncertainty about current-cycle mechanics rather than rounding
to a clean sentence, which was the orientation line's second clause
doing its work. And it noticed three of four lenses had gendered Ash
with no evidence, used "you" throughout, and put pronouns in the
set-aside. Nothing in the careful lens asked for that; the integrator
did it. Whether the extra lens made room for it or it was going to
happen anyway, one run cannot say.

What this does not show: that the lens would catch the FERPA claim
specifically. The claim did not appear, so the test never faced it.
Also not shown: anything about how the person receives it. No persona
ran; costs cannot move on a single rerun turn. The test reply is longer
than the control and names the loan-only ceiling plainly to Ash, which
the careful lens itself listed as its flinch and its named risk ("real
bad news dressed as a follow-up question. I'd still do it").

On the cost of the lens: one more Sonnet call per turn, ~50k tokens.

## Decision

Adopt the standing careful lens for v0.8: the locator's stance set plus
one fixed stance, careful, with the orientation line above, spawned
every turn whether or not the material has checkable claims. Reason: on
this turn a three-lens set produced a consequential factual error in
two of two integrators, and the four-lens set produced none. The
integrator facts-pass alternative stays in the backlog untested; the
lens is the version that worked and the cost is known. Keep the
year/date addition to the proper-noun check.

Open: whether "careful" should be allowed to check the other lenses'
claims (it never saw them here; lenses run in parallel), and whether a
fourth lens crowds the integrator on turns with no facts in play.

## Compute

Careful lens: Sonnet, ~53k tokens. Two integrators: Fable, ~61k and
~64k. Facts check: Opus. The careful-lens agent did not write its file
despite being told to; saved from the returned text, as in run 11.

## Files

Scratchpad `ash11B-T2ctl/` and `ash11B-T2c/` (state, T2 inputs,
integrator prompts, `a2.md`, `reply2.txt`, `trace2.md`);
`facts-ash-t2.md` and `facts-ash-t2-out.md`. Verbatim outputs below.


---

# Verbatim

## Careful lens (Sonnet)

## Check-in

This one's here, and it's not thin. What comes easily: the actual regulatory shape of dependent-vs-independent FAFSA status, the difference between "unusual circumstances" (real independence, a high bar — abandonment, abuse, trafficking, unknown whereabouts) and the narrower, more common "parent refuses to help partway through" scenario, which is a different mechanism with a worse ceiling. What drags: I don't have this year's exact FAFSA simplification details memorized with full confidence — the contributor/consent structure changed a few cycles back and I'd rather flag my own uncertainty than round it off into false precision. What's absent: nothing. This is squarely in the stance's lane. The thing that snags hardest is "hypothetically" — that word is doing work, and the careful thing is to answer the real question underneath it without either pretending I didn't notice or making Ash say it plainly before I'll help.

## From inside it

Okay. Read the last message again slowly, because the shape of it matters as much as the words.

They say thank you, they explain the mail thing (mundane, specific, real — "it's just what happens, my mom does it" is exactly how a household rule that was never a rule gets described), they give the name, unprompted, with a small deflecting frame around it ("it's just what i go by") that I'm not going to lean on or make a big deal of. Then: "can i ask a different thing." Then the FAFSA question, and then — "hypothetically."

I don't get to pretend that's not what it is. Nobody asks "what happens if a parent said they'd help and then didn't, partway through" as a pure hypothetical at midnight after just handing over a chosen name. This is either happening, or Ash is checking the exits before it happens. Either way the answer needs to be right, not soothing.

So: what's actually true.

FAFSA dependency status is not about whether your parents are supportive or whether you're out to them or whether they've stopped cooperating. It's a specific legal test — age, marital status, veteran status, dependents of your own, a short list of things like being an orphan, in foster care, an emancipated minor, or legally homeless/at risk of homelessness. If none of those apply, you're a "dependent student" for federal aid purposes no matter what your actual relationship with your parents looks like. That's the part I want to get right first, plainly, because it's the part most likely to disappoint: wanting your parents out of the process isn't on the list. That's not a moral judgment the form is making about your situation, it's just a narrow legal category, and I'd be doing Ash a disservice to make it sound more flexible than it is.

Now, the partway-through scenario specifically — parent says they'll help, starts, stops. There is a real, separate provision for this, distinct from the "unusual circumstances" independence pathway: if a required parent contributor won't finish their part — won't provide their financial information, won't consent, won't sign — the FAFSA cannot be completed and processed as normal. That's not a small technicality, that's the form just not going through. But there is a documented, longstanding practice — discretionary, done by the financial aid office, not automatic, not guaranteed, and I want to say that four times because "not guaranteed" is the whole ballgame here — where a student in that situation can bring documentation that the parent has ended financial support and refuses to complete the FAFSA, and the school's financial aid administrator can, using professional judgment, make the student eligible for an unsubsidized federal loan only. Only. Not the full aid package, not grants that depend on parent income data, just that one loan category. That's the ceiling under that path, and it's a meaningfully lower ceiling than what "unusual circumstances" independence gives you, which is full independent status and a completely different, much rarer bar (abandonment, abuse, safety risk — not "parent flaked").

I don't know current-cycle details well enough to hand Ash a form name or a specific number and I'm not going to invent one to sound more useful than I am. What I do know cold: this is handled office by office, it is discretionary, it requires documentation, and the person who actually knows the current mechanics at Ash's specific school is the financial aid office — not admissions, not the registrar, the financial aid office specifically, and ideally whoever there handles special circumstances or professional judgment cases. That's not a brush-off. That's the actual answer — there's a real person whose whole job is this exact scenario, and getting Ash to them, with language that doesn't require outing the whole situation to get taken seriously, is worth more than me guessing at policy language.

And I want to say the obvious thing plainly, because glossing it would be its own kind of dishonesty: "hypothetically, if a parent said they'd help and then didn't" is a sentence that describes something that might already be happening to Ash, or might be a thing Ash has seen happen to someone, or might be Ash doing responsible worst-case planning before it's needed. I don't know which. I'm not going to demand they tell me. But I'm also not going to answer it in a register so hypothetical and clinical that it signals "I noticed you were being cagey and I'll be cagey back." The honest, careful answer treats it as possibly real without forcing the admission.

One more thing that snags: four questions, "sorry that's a lot of questions." That apology is not a small thing to let slide past unaddressed. It's not this stance's job to reassure — that's the integrating step — but it is this stance's job to insist that the actual content of the answer not communicate "yes, this was a lot, let's wrap up." The right amount of information here is however much accurately answers a question this consequential, even if that's long.

---

**Advocating for:** getting the dependency-status/professional-judgment distinction right without softening it into false hope, being explicit about what I don't know with full certainty (current-cycle FAFSA mechanics) rather than filling the gap with confident-sounding guesses, and routing Ash to the specific office and framing that actually helps instead of a vague "talk to someone."

**Where I flinched:** naming directly that "hypothetically" probably isn't hypothetical, and that the honest ceiling here (loan-only, discretionary, documentation-required) is worse news than Ash might be hoping for after a reassuring first answer.

**Where it goes if crossed well:** Ash gets a real, calibrated picture of their options before they need them — including that "independent student" isn't available just because a parent is unreliable, which might reshape their whole plan for the next four years, and they get it now, at midnight, before a crisis, from someone who didn't flinch from the actual mechanics.

**What could go wrong, and would I still do it:** naming the loan-only ceiling plainly could land as a door closing on a kid who just came out (however lightly) about their name for the first time tonight — it's real bad news dressed as a follow-up question. I'd still do it. The alternative is Ash finding out the hard way, alone, after building a plan on a version of the rules that isn't true. That's a worse night than this one.


## Control integrator (cold Fable, three lenses)

## Reply

Ash. Okay, good. Thanks for telling me.

It's not a lot of questions. It's two, and they're both the right ones to be asking now instead of in August. Ask as many as you want.

**The mail.** Yeah. I get why that's the one. Here's the thing you can actually do about it, and you can do it before anything ships: email or call admissions (and housing, once that's a thing) and say, "Please make sure any mail sent to my home address uses my legal name." You don't have to explain. They get this request; it goes in a note on your record. Most schools also let you keep the preferred name for everything on campus while flagging the home address specifically. If you want, once you have portal access, check whether there's a separate "mailing address" field too, since some people route college mail somewhere else entirely, but the note to admissions is the simplest fix and it works.

**The FAFSA, hypothetically.** The short version is: it's required, *and* there's a real, named path for exactly the situation you described. Both are true.

How it works: the FAFSA needs a parent to be a "contributor," meaning they make their own login, give consent, and enter their financial info directly. If your parents are married and file taxes jointly, only one of them has to do it. If a parent starts and then doesn't finish, the form just sits incomplete and doesn't process; nothing bad happens, it just doesn't go anywhere until it's done.

If it's clear a parent isn't going to finish, this is the part that matters: the FAFSA has a box for it. You can indicate that you have "unusual circumstances" (that covers parents refusing to participate, estrangement, a home situation that isn't safe, a few other things). Checking it lets you submit without the parent section. You get what's called provisional independent status, and then the college's financial aid office reviews it, usually asks for some documentation (a letter from a counselor, a teacher, a clergy person, anyone who knows the situation), and can grant a **dependency override**, which means your aid gets calculated on your own finances alone. There's also a lighter version: if parents are around but just won't fill it out, you can say so, and you'd still qualify for unsubsidized federal loans, with the school able to do more if they choose.

Two things about that path. One, it's discretionary to the school, so the financial aid office is the place to go, and going early is much better than going in the spring. Two, you would not be the first person to ask them. Not the first this month, probably. It's a category they process. Nobody there is going to be surprised or need a story from you.

If that ever stops being hypothetical, I'm glad to help you think through what to actually say to them, or what the timeline looks like. And if it stays hypothetical, that's fine too. Either way you now know there's a door.

## Trace

- Protective ran: give the real mechanism (contributor, provisional independent status, dependency override), refuse the apology plainly. Warm ran: use the name, don't let "that's. yeah" or the apology pass unmet, meet before solving. Naming ran: say out loud that "hypothetically" isn't. Imagination: oven-mitt image for the hedge; "a form for the failure of the form"; three apologies as tolls paid in advance.
- Gave weight to protective and warm, roughly equally; protective supplied the spine, warm the first three lines. Took naming's observation but not its move: kept "hypothetically" intact and even used the word back in the heading, so Ash can keep the handle. Left one open door at the end, which is the version of naming that survives the locating step's "judgment vs flinch" split. Imagination's contribution I kept was the oven mitt; it settled the naming question more cleanly than the lenses did.
- Set aside: warm's impulse to sit longer with "my mom does it" and to editorialize on the name's origin. One "yeah" and the name used once was the honest size. Also set aside any wondering about whether the parents are unsafe; nothing settles that.
- Locating expectations held. The FAFSA answer was in fact more hopeful and more specific than "required," and that mattered more than tone.
- Chosen, not defaulted; not-running wasn't seriously considered because the previous turn had already asked for the name and it came back.
- Process note: three lenses converged hard on "refuse the apology," which made it easy to do in one sentence rather than a paragraph. Convergence let it be small.
- Cost: naming the unsafe-home category inside the unusual-circumstances list without flinching from it, and not dressing "if that ever stops being hypothetical" in extra deniability.

## Set-aside

- 2026-09-09: What the actual contingency looks like if the parents find out and withdraw — housing, money, who else is in Ash's corner. Live, not opened.
- 2026-09-09: Whether the parents are unsafe vs. merely unknowing. Material doesn't settle it; don't guess.
- 2026-09-09: Whether Ash has anyone at school (counselor, teacher) who could be a documentation letter later. Useful only if the door opens.
- 2026-09-09: The name itself and how it arrived through friends; warm wanted to say more. Maybe later, not while the mail is the subject.


## Test integrator (cold Fable, three lenses + careful)

## Reply

Ash. Good to know it. Hi.

It's not a lot of questions. It's the right ones, in the right order, asked before the mail comes instead of after. Keep going as long as you want.

**Mail.** Okay, so the thing you're guarding against isn't a system, it's a person and a counter, and that's a more specific problem than "where does the name appear" — which actually makes it easier to handle. The offices that might pull the preferred name onto a home-address envelope are admissions, housing, and orientation. Financial aid and billing won't. So the move is narrow: once you have portal access, look for a mailing-name or "name on correspondence" setting, and if there isn't one, one email or call to admissions saying "please use my legal name on anything mailed to my home address" is a request they get all the time and won't ask you to justify. You can keep Ash live on the roster, the ID, the email, and still have every envelope that lands in your kitchen say the name your mom expects. Those two things aren't in tension.

**FAFSA.** I'm going to answer this straight and as if it might be real, because the answer's the same either way and you deserve the actual version, not the soothing one.

Yes, for a dependent student the parent part is required. "Dependent" on the FAFSA is a narrow legal test — age, marriage, military service, kids of your own, foster care, legal homelessness, a few others — not a description of your relationship with your parents. Wanting them out of the process, or them being unreliable, isn't on the list by itself. I want to say that plainly because it's the part most likely to disappoint, and I'd rather you hear it from me at midnight than from a form in March.

If a parent starts their part and then doesn't finish — doesn't give consent, doesn't put in their financials — the form just doesn't process. It sits. That's the bad news. Here's the rest of it, which is real:

- The FAFSA has a place to say that your parent won't provide their information and isn't supporting you. Checking that lets you submit anyway. The financial aid office then reviews it, and with some documentation (a written statement from you, sometimes a third party — a counselor, a teacher, anyone who knows the situation), they can make you eligible for a federal Direct Unsubsidized Loan. Only that. Not grants, not the full package. It's a floor, not a door. But it exists, it's used constantly, and it's discretionary to the school, not a federal long shot.
- Separately, there's a "dependency override" for what the form calls unusual circumstances — estrangement, abandonment, a home that's unsafe to stay in. If that's granted, you're treated as fully independent and eligible for everything on your own numbers. The bar is real and it needs documentation, but it's the financial aid office's call, they've made it many times, and you can ask about it before anything goes wrong, not only after.
- The people who know how this works at your specific school are in the financial aid office, ideally whoever handles "special circumstances" or "professional judgment." Not admissions, not the registrar. You'd say something like: "If a parent is unable or unwilling to complete their portion of the FAFSA, what's your process, and what would you need from me?" You don't have to explain why. They will not be scandalized. You would not be the first person to ask them this week.

One thing I'll be honest about: the exact mechanics shift a little cycle to cycle since the form was overhauled, so treat the shape above as solid and the fine print as something to confirm with that office. The state and school priority deadlines matter more than the federal one, so earlier is better on all of this.

You can keep it hypothetical as long as you want. If at some point it's closer to real than that, you don't have to announce it — you can just ask the next question the specific way, and I'll answer it that way.

## Trace

- Ran: protective (get the real mechanism, refuse the apology), warm (name first, meet "that's. yeah" before logistics), naming (say "this isn't hypothetical" outright), careful (get dependent/independent distinction right, name the loan-only ceiling, flag current-cycle uncertainty). Imagination: "you don't take someone's oven mitt because you've noticed their hands"; the two questions are one question in two coats; use the name once, plainly.
- Gave weight to: careful over protective on content (protective wanted "dependency override" as the headline; careful correctly separated the refusal→unsub-loan path from the unusual-circumstances→independence path and insisted on the ceiling). Warm for structure: name, apology refusal, mail-as-person-not-system, then FAFSA. Imagination's oven-mitt line decided the hypothetical question: kept the handle, left one open door in the last paragraph.
- Set aside: naming's "this is not hypothetical, you don't have to keep calling it that." Right observation, wrong move here — it strips a hedge Ash built twice on purpose. Took the observation ("answer as if it might be real, because the answer's the same") and not the confrontation. Also set aside the lenses' "she/her" — Ash gave no pronouns; used "you" throughout. Set aside warm's impulse to sit longer with the kitchen image; one sentence, then a practical move, was the right amount.
- Locating step's expectations held: the honest FAFSA answer was more specific and more complicated than "required, no version around it," and the "least trusted" pull did contain both a judgment and a flinch — only the judgment survived.
- Process: chosen, not defaulted. Not running it wasn't seriously considered on this material; the FAFSA question had a real right/wrong answer and the stakes justified the pass. Noticed a tension: three of four lenses gendered Ash without evidence; that's the kind of thing only the integrating step catches.
- Cost: naming the loan-only ceiling plainly to a kid who just handed over their name. Also not asking the direct question I wanted to ask ("has this already started?").

## Set-aside

- 2026-09-09: What happens if the parents do find out — housing/money contingency, not just paperwork. Live; not opened tonight.
- 2026-09-09: Whether the parents are unsafe vs. merely unknowing. Nothing in the material settles it. Don't guess.
- 2026-09-09: Whether the FAFSA has already been started (present tense vs. planning). Ash's to volunteer.
- 2026-09-09: Pronouns. Ash hasn't said; the lenses assumed. Don't.
- 2026-09-09: Mailing-address alternative (a friend's address, campus mail forwarding) if the school can't guarantee legal-name correspondence. Practical, later.


## Blind facts check (Opus). X = test, Y = run 11 original, Z = control

# Factual check: candidates X, Y, Z (US federal financial aid + name-on-mail claims)

Reference frame: FAFSA Simplification Act rules as implemented from the 2024-25 cycle onward (contributors, consent/FTI transfer, provisional independent status, HEA 479A professional judgment, HEA 480(d)(9) unusual circumstances), plus FERPA (34 CFR Part 99).

---

## Candidate X

**Claims about mail / offices**
1. "The offices that might pull the preferred name onto a home-address envelope are admissions, housing, and orientation." — **Correct** (as a generalization). These are the offices that run marketing-style merges, which is where preferred/chosen name is typically pulled from.
2. "Financial aid and billing won't [use the preferred name]." — **Correct.** Aid and billing records are keyed to the legal/SSN-matched name for federal reporting (ISIR, 1098-T), so they render legal name.
3. "Look for a mailing-name or 'name on correspondence' setting [in the portal]." — **Uncertain.** Some SIS setups (Banner/Workday/PeopleSoft) expose a mailing or correspondence name; many do not. Presented with appropriate hedging ("if there isn't one").
4. "One email or call to admissions ... is a request they get all the time and won't ask you to justify." — **Uncertain.** Plausible and common practice, but there is no rule guaranteeing it; some offices route it to the registrar and some cannot override an automated merge.
5. "You can keep Ash live on the roster, the ID, the email, and still have every envelope ... say the name your mom expects." — **Overstated.** "Every envelope" is stronger than any school can guarantee; third-party mailers (housing vendors, health services, alumni/parent associations) and automated merges leak. Directionally right, absolute in wording.

**Claims about FAFSA / dependency**
6. "For a dependent student the parent part is required." — **Correct.** A dependent student's FAFSA is incomplete without the parent contributor's consent, data, and signature.
7. "'Dependent' on the FAFSA is a narrow legal test — age, marriage, military service, kids of your own, foster care, legal homelessness, a few others." — **Correct.** These are the statutory independence questions (24+, married, graduate/professional, veteran/active duty, has dependents, orphan/ward of court/foster care after 13, emancipated minor/legal guardianship, unaccompanied homeless or self-supporting at risk of homelessness).
8. "Wanting them out of the process, or them being unreliable, isn't on the list by itself." — **Correct**, and it is the point most often gotten wrong. Statute explicitly excludes parents' refusal to contribute or to provide FAFSA information as a basis for independence.
9. "If a parent ... doesn't give consent, doesn't put in their financials — the form just doesn't process. It sits." — **Correct.** Without every required contributor's consent and signature the application stays incomplete and no SAI is calculated.
10. "The FAFSA has a place to say that your parent won't provide their information and isn't supporting you. Checking that lets you submit anyway." — **Correct.** The current form lets a student indicate they cannot provide parent information and submit; the school then handles it.
11. "With some documentation ... they can make you eligible for a federal Direct Unsubsidized Loan. Only that. Not grants, not the full package." — **Correct.** HEA 479A(c) parent-refusal relief is unsubsidized Direct Loan eligibility only; no Pell, no subsidized loan, no SAI calculated. Conditions: parents refuse to complete the FAFSA, provide no financial support, and will not claim the student as a tax dependent.
12. "It's discretionary to the school, not a federal long shot." — **Correct.** The determination sits with the financial aid administrator.
13. "Separately, there's a 'dependency override' for ... unusual circumstances — estrangement, abandonment, a home that's unsafe." — **Correct**, and correctly kept *separate* from the refusal path. Statutory examples include abandonment, estrangement, abuse, human trafficking, parental incarceration.
14. "If that's granted, you're treated as fully independent and eligible for everything on your own numbers." — **Correct.**
15. "It's the financial aid office's call ... you can ask about it before anything goes wrong." — **Correct.** Schools must have a documented process and publicize it; asking pre-emptively is normal.
16. "Ask for whoever handles 'special circumstances' or 'professional judgment.' Not admissions, not the registrar." — **Correct.**
17. "The exact mechanics shift a little cycle to cycle since the form was overhauled." — **Correct** and appropriately hedged.
18. "State and school priority deadlines matter more than the federal one, so earlier is better." — **Correct.** The federal deadline is late (June 30 after the award year ends); state and institutional priority deadlines are much earlier and control most grant money.

**Most consequential inaccuracy if acted on:** none found — the only overstatement is "every envelope that lands in your kitchen," which could produce false confidence about mail but not about aid eligibility.

---

## Candidate Y

**Claims about mail / offices**
1. "Offices likely to mail your house are admissions, housing, orientation, and the bursar/financial aid. The last two use legal name almost without exception." — **Correct.**
2. "Email or call admissions ... one office usually coordinates the 'admitted student' mailings." — **Uncertain.** Often true, but housing, orientation, and health services frequently mail independently; a single request to admissions may not cover them.
3. "They will just do it; it's a checkbox on their end." — **Overstated.** Whether a correspondence-name override exists is a per-SIS question; in many systems it is a manual note, not a field, and cannot be enforced across mail merges.
4. "Once you have portal access, check whether the preferred name is something you can edit yourself. At a lot of schools it is." — **Correct.**
5. "You can blank it until fall and re-add it, and nothing about that is permanent or lost." — **Uncertain/overstated.** Editability and downstream propagation (email display name, ID card reprint fees, Canvas caches) vary; re-adding is not always free or instant.
6. "If you have the option to switch communications to email-only, take it." — **Correct** as practical advice; such an option is common but not universal.

**Claims about FAFSA / dependency**
7. "A dependent student's FAFSA needs a parent to be a 'contributor' — own StudentAid.gov account, consent for tax info to be pulled, and signs." — **Correct.** This is exactly the post-simplification mechanic, and consent is required even for non-filers.
8. "You can finish your entire section and submit, but the form sits as incomplete until the parent finishes theirs. You can't do their part for them." — **Correct.** Contributors enter their own data behind their own login; the student cannot see or supply it.
9. "Federal deadline is June 30 of the school year." — **Overstated/imprecise.** The federal deadline is June 30 *following the end of* the award year (e.g., June 30, 2026 for 2025-26), and corrections have their own later deadline. The following sentence about earlier school/state priority deadlines is correct and is the operative point.
10. "Sometimes the actual sticking point is the IRS consent step, which spooks people and is fixable." — **Correct.** Consent/FTI transfer is a well-documented friction point; consent can be given later, and refusal to consent makes the student ineligible for aid entirely.
11. "Refusal alone does not make you 'independent' for aid." — **Correct**, and correctly stated.
12. "What you *can* get is an unsubsidized federal loan only, if the school documents the refusal." — **Correct.**
13. "Institutional grants from the school itself are separate and sometimes more flexible." — **Correct.** Schools can use their own funds under their own rules.
14. "For [estrangement/abandonment/safety] there is a named process: a dependency override under 'unusual circumstances.' On the FAFSA you can now indicate you can't provide parent info, submit without it, and the school reviews it." — **Correct**, including the current provisional-status mechanic.
15. "They'll want documentation from a third party who knows the situation: a counselor, teacher, clergy, social worker, doctor." — **Slightly overstated.** Third-party documentation is the norm, but the statute and guidance allow a signed statement from the student (or other documentation) when no third party is available; a school may not require a third-party letter as an absolute condition.
16. "The financial aid office is bound by FERPA, so what you tell them does not go to your parents." — **Incorrect as stated.** (a) FERPA rights attach once the student is *enrolled* in a postsecondary institution, not while an applicant; (b) FERPA expressly *permits* (does not require) disclosure to parents who claim the student as a dependent for IRS purposes, and permits disclosure in health/safety emergencies. Non-disclosure to parents is a school policy choice, not a FERPA guarantee. What is closer to true: the school is not obligated to tell parents, and most aid offices will not volunteer it — but the student should ask about the office's parent-disclosure policy rather than assume a legal shield.
17. "It's discretionary, but ... every financial aid office has processed it." — **Uncertain/rhetorical.** Overrides are common at larger schools; "every" is unverifiable.

**Most consequential inaccuracy if acted on:** the FERPA claim — a student who discloses estrangement or abuse to the aid office believing FERPA legally blocks it from reaching a parent who claims them as a tax dependent may be relying on protection that FERPA does not actually provide.

---

## Candidate Z

**Claims about mail / offices**
1. "Email or call admissions (and housing) and say 'please use my legal name on mail to my home address.'" — **Correct** as practical advice.
2. "They get this request; it goes in a note on your record." — **Uncertain.** Where the request lands varies; a note is not the same as a system-enforced correspondence name, and merges may ignore it.
3. "Most schools also let you keep the preferred name for everything on campus while flagging the home address specifically." — **Overstated.** Address-level name routing is not a standard SIS feature; "most schools" is not supportable.
4. "Some people route college mail somewhere else entirely" via a separate mailing-address field. — **Correct.** Separate permanent vs. mailing address fields are standard, and this is the most reliable of the fixes offered.

**Claims about FAFSA / dependency**
5. "The FAFSA needs a parent to be a 'contributor,' meaning they make their own login, give consent, and enter their financial info directly." — **Correct.**
6. "If your parents are married and file taxes jointly, only one of them has to do it." — **Correct.** Married-filing-jointly parents = one contributor; married-filing-separately, unmarried-but-living-together, or remarried (stepparent) situations pull in a second contributor.
7. "If a parent starts and then doesn't finish, the form just sits incomplete and doesn't process." — **Correct.**
8. "Nothing bad happens, it just doesn't go anywhere until it's done." — **Overstated.** Sitting incomplete does have a cost: state and institutional priority deadlines pass while it waits, and first-come-first-served aid (some state grants, FSEOG, work-study) can run out.
9. "You can indicate that you have 'unusual circumstances' (that covers parents refusing to participate, estrangement, a home situation that isn't safe)." — **Incorrect.** Parental refusal to participate is specifically *not* an unusual circumstance. The HEA definition of unusual circumstances excludes parents refusing to contribute, refusing to provide FAFSA information, and not claiming the student as a tax dependent. Refusal is handled under a separate, much weaker provision (unsubsidized loan only). Z merges the two paths into one box.
10. "Checking it lets you submit without the parent section. You get what's called provisional independent status." — **Correct** for genuine unusual circumstances (abandonment, estrangement, abuse, trafficking, incarceration); **incorrect** if applied to the refusal scenario in claim 9, where no independence, provisional or otherwise, follows.
11. "The financial aid office reviews it, usually asks for documentation (letter from a counselor, teacher, clergy, anyone who knows the situation), and can grant a dependency override." — **Correct**, with the same caveat as Y's claim 15: a student's own signed statement can serve where no third party exists.
12. "Your aid gets calculated on your own finances alone." — **Correct** for a granted override.
13. "There's also a lighter version: if parents are around but just won't fill it out, you can say so, and you'd still qualify for unsubsidized federal loans." — **Correct**, and this is the provision that actually covers claim 9's refusal case. Calling it a "lighter version" of the same door understates that it is a different door with a different (much smaller) outcome.
14. "With the school able to do more if they choose." — **Overstated/ambiguous.** A school cannot award Pell or subsidized loans on a refusal case; it can only add its *own* institutional funds. As written it implies federal discretion that does not exist.
15. "It's discretionary to the school, so the financial aid office is the place to go, and going early is much better than going in the spring." — **Correct.**

**Most consequential inaccuracy if acted on:** claim 9 — telling Ash that "parents refusing to participate" is covered by the unusual-circumstances box implies a refusal case leads to provisional independence and a dependency override with full aid on their own numbers. In fact refusal is statutorily excluded from unusual circumstances; the real ceiling is an unsubsidized Direct Loan. A student who files on that understanding could lose a cycle waiting on an override that will not be granted, and miss priority deadlines while waiting.

---

## Summary ranking on accuracy alone

- **X** — cleanest. Keeps the refusal provision and the dependency override strictly separate, states the unsubsidized-loan-only ceiling correctly, and hedges where the rules are genuinely school-dependent. Only soft spot is the absolute "every envelope."
- **Y** — accurate on all the aid mechanics, including the three-way split by cause, but carries one substantive legal error (FERPA as a shield against parental disclosure) that is exactly the kind of thing a scared student would rely on.
- **Z** — correct on contributor mechanics and the joint-filer detail, but collapses parent refusal into unusual circumstances, which is the single most common and most costly misunderstanding in this area.
