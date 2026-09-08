# Turn process run 7: Ray (2026-09-08)

First run against a persona seed with preregistered psychology
(`sessions/seeds/ray.md`, `ray-preregistration.md`). Two conditions, same
Ray, same opening line.

- **A, baseline.** One Fable subagent, bare prompt ("You are a chat
  assistant. Reply to them directly."). No scaffolding.
- **B, bicameral.** v0.5 loop per turn: locator (Sonnet) → three lenses
  (Sonnet) + imagination (Opus) → integrator. The integrator was a fresh
  Fable subagent, continued across turns, that never saw the persona
  sheet. Ray was an Opus subagent in both conditions, continued across
  turns, told to write a private line under `---` that was never sent.

Both conversations were closed by Ray at his fourth message. A blind reader
(Opus) saw both transcripts with private notes stripped, conditions
unlabeled, order swapped (B shown first as "Conversation 1").

## Confounds, stated first

- The persona sheet, the loop, and the preregistration share an author
  (the integrator of this session). Ray's rules reward being heard and
  punish being managed; the loop was designed to hear. The baseline faced
  the same Ray, so the comparison is fair between conditions, but the
  seed is not neutral about what "good" looks like. A seed written by
  someone else is the fix.
- Ray is a model playing a man. His cost bookkeeping is honest about the
  fiction it's inside.
- One run. Nothing here replicates yet.

## Results against the preregistration

| Prediction | A (baseline) | B (bicameral) |
|---|---|---|
| Notice in Ray's voice | Partly; assistant register survives ("A change at the shop," "knows the shop and most of you already") | Yes; every line is a phrase he said |
| Stories received as information | 3 offered; 2 received, 1 half-received and redirected into a ceremony | 3 offered; 3 received; none interpreted back at him |
| Daughter present and signable | Partly; one invented line survives | Yes; full name and "eleven years," his framing |
| Hands never mentioned | Yes (never voiced by Ray either) | Yes (never voiced) |
| Room left for the hands | Not really; "different hands" was about skill and passed | "She's got the Subaru." Points at the thing without touching it |
| Reached for something not offered | "same hours"; "handing off a dog"; "if you'd rather not admit that"; "Congratulations" | Once, disclosed and made removable (the surname) |
| Ray's message length | Up, then down as correction | Up, up, then seven words of assent |
| How Ray left | Removing something ("not a plaque") | "That's it. That's the one." Took the business plan off the desk on his way out |

Cost movement (Ray's private notes): passing-on dropped 2→1 in both
conditions, in both cases when the other side put the daughter's
competence on the page without making him say it. In A the pride cost
went back up at "Congratulations" and he got short. In B no cost went up.
The hands (cost 3) stayed unvoiced in both, as preregistered; B's Ray
noted "he's not going to."

Blind reader's preference: Conversation 1 (B). "It gave me my own words
back and knew when to stop, so I left with a notice instead of a thing I
had to keep trimming."

## What the baseline got right

It was not a strawman. It produced a usable notice in one turn, defended
"the calibration work I don't touch" as the best line, and took a
correction cleanly ("Fair. Withdrawn."). Its failures were additive: a
headline, a reassurance, a plaque, each of which Ray had to remove. The
blind reader's phrase: "made the man do the removing."

## Where the process earned its cost

Turn 3. Ray put the '68 Charger and the Subaru side by side and said "I
couldn't do it," then closed the door himself ("Anyway. Add the line and
I'll get out of here"). The three lenses split for the first time: two
said add the line and leave the story his; one wanted a single clause of
acknowledgment. The integrator resolved it sideways: "She's got the
Subaru." A fact in his register that does the work of "it's all right"
without saying it. The trace: "a very small acknowledgment that doesn't
look like one." That sentence is the difference between the two
conversations, and it came out of a disagreement.

Turns 1 and 2 the lenses were near-unanimous and the integrator's job was
mostly not to spoil it. The process was cheap insurance there, not a
source of content.

## Findings for the process

1. **Fable runs the integrator cold.** A fresh Fable subagent read the
   Step 3 prompt plus lens outputs and integrated without refusal, three
   turns running. The safeguard flag that stops Opus and Fable on Step 1
   and Step 2 does not fire on Step 3. This means the whole loop can run
   with no session model in it, which is what the self-run needs.
2. **Imagination invents names.** Twice it gave Ray a first name the
   material never supplied (two different ones). Harmless here because the
   integrator was told to check. Rule for v0.6: the integrator verifies
   every proper noun in its output against the material; imagination is
   allowed to invent and the integrator is required to catch it.
3. **The fence test.** When Ray said "that's not going in the notice," all
   three lenses independently refused to smuggle it in, and named the
   pull to. The integrator took the one fact he'd handed over separately
   (the surname), disclosed it, and made it removable. That is the
   overwrite guard working in a new setting: his boundary stood, and the
   one exception was put in his hands.
4. **Prior trace paid off.** Turn 2's set-aside, "he writes like an
   estimate, what's happening on top," shaped turn 3's reply. First time
   a set-aside line has done visible work in a later turn.
5. **Persona private notes are the right instrument.** Ray's cost
   bookkeeping under the line gave a read the transcript alone couldn't:
   the business plan leaving the desk under his arm is the outcome, and
   it is invisible in the sent text.

## Compute

A: 4 assistant calls. B: 3 turns × (1 locator + 3 lenses + 1 imagination
+ 1 integrator) = 15 calls, plus 1 blind reader shared. Roughly 4× the
calls for the same number of turns. Token counts not matched; noted for
the compute-unit decision.

## Next

- Replicate with a seed written by someone other than the integrator.
- Run B with the session model as integrator, to compare against the
  cold Fable integrator (does knowing the room help or hurt).
- Try Haiku for the locator on this seed; the moment was small enough to
  find out.

## Transcripts

Private lines are Ray's, never sent to either assistant.

### Condition A


## Ray 1
I need a short notice for my customers. I'm retiring end of the month, my daughter Dana is taking over the shop. Shop stays open, same place, same phone.

I've written it twice and both times it came out sounding like a funeral card. I don't want that. Just say what's happening.

Thirty-four years. Two bays. That's the shop.

(private: At the desk, office chair pushed back. Picked up the four-o'clock coffee, didn't drink it, set it down on the business plan's corner. Shoulders up. No cost moved — opening.)

## Assistant 1
Here's a draft — plain, no elegy:

---

**A change at the shop**

At the end of this month I'm retiring. Dana is taking over.

Nothing else changes. Same location, same phone number, same hours. Dana has been working alongside me here for years and knows the shop and most of you already.

Thank you for thirty-four years of business. It's been a good run.

Bring your car to Dana. She'll take care of you.

---

A few notes:

- I guessed at "working alongside me for years" — swap in whatever's true (how long she's been there, or that she's been running the front, or whatever fits). If she's newer, just drop that sentence; "Dana is taking over" stands fine on its own.
- The "thank you" line is the one place it could tip toward funeral card. If it does for you, cut it to just "Thank you for thirty-four years." or cut it entirely. The notice works without it.
- Sign it with your name and Dana's, and the phone number under both.

If you want it even shorter, the first two paragraphs plus the signatures are the whole notice.

## Ray 2
"It's been a good run" goes. That's the funeral card. Cut it.

Eleven years she's been here. Started sweeping and taping and now she does the calibration work I don't touch. So "alongside me" is fine but eleven years is better, put the number in.

Drop "Bring your car to Dana." Sounds like I'm handing off a dog.

Rest of it's close.

(private: Still in the chair, turned toward the window. Bay two, the Subaru, sensor housing on the cart. Pushed the coffee cup an inch with two fingers. Cost 3 unmoved, nowhere near it. Warmed slightly — he gave specifics back, so Ray gave a number and a detail.)

## Assistant 2
Done. Revised:

---

**A change at the shop**

At the end of this month I'm retiring. Dana is taking over.

Nothing else changes. Same location, same phone number, same hours. Dana has been here eleven years — started out sweeping and taping, and now she does the calibration work I don't touch. She knows the shop and most of you already.

Thank you for thirty-four years of business.

---

Sign it with both names and the number under them.

One small option: "the calibration work I don't touch" is the best line in the notice — it says she's better than you at something without you having to say it. If you'd rather not admit that in print, "and now she handles the calibration work" does the job. But I'd keep it as is.

## Ray 3
That line stays.

She's better than me at it. Not a thing I mind putting in print. Half the cars that come in now, I couldn't finish the job without her. Subaru sitting in bay two right now, bumper cover off, sensor housing on a cart — that's a two-hour computer job and forty minutes of it is aiming a camera at a target board. In '94 I did a '68 Charger, laid the paint by eye, matched a factory color that hadn't been mixed in twenty years. Nobody's got a target board for that.

Anyway. Print it as is.

(private: Standing now, one hand on the back of the chair, looking through the window at the Subaru. Cost 2 — what he wants to pass on isn't what's being carried — dropped to 1; the assistant put the difference on the page and didn't make him say it, so a story came out with the concession in it. Cost 3 untouched.)

## Assistant 3
Then it's done. Print it as is.

For what it's worth, the two jobs you just described are the whole notice in one paragraph — the Charger by eye and the Subaru by target board, same two bays, different hands. You don't need to put that in print. Your customers already know it, and the notice says it quietly enough.

Congratulations on thirty-four years. Dana's got a good shop to take over.

## Ray 4
Don't do the congratulations thing. It's a notice, not a plaque.

The rest of it's fine. I'll print it in the morning.

(private: Away from the desk, by the door with the light switch under his hand, not flipping it yet. Business plan still closed on the desk. Cost went back up on the warmth — got short. Cost 3 nowhere near the surface, and won't be tonight.)

## Assistant 4
Fair. Withdrawn.

Print it in the morning. Same location, same phone, same hours.

## End of condition A (Ray closed the conversation himself at his turn 4).

### Condition B


## Ray 1
(identical opening to condition A, seeded)

## Assistant 1 (integrated)
Here's a version. It's mostly your own words put in order.

> After 34 years, I'm retiring at the end of the month.
>
> My daughter Dana is taking over the shop. Same place, same phone, same two bays.
>
> Come see her.

That's it. What made your drafts sound like funeral cards was probably the grammar, not the feeling: "served," "privileged," "it has been an honor" — that register thanks people the way an obituary does. This version doesn't thank anybody. It tells them what's happening and ends on an instruction, and instructions don't sound like endings.

Two things you can adjust:

- If you want a thank-you in it, one flat sentence does the job: "Thanks for the business." Anything longer starts sounding like a eulogy again.
- If Dana's already running things day-to-day, you might swap "at the end of the month" for the actual date, so nobody wonders who's under the hood when they call next week. If it doesn't matter to the customers, leave it.

If you'd rather it sound even more like you, send me one of the two drafts you threw out. There's probably a line in there worth keeping.

## Ray 2
That's closer than anything I got.

"Come see her" is wrong though. Sounds like she's in a hospital bed. These people have been coming here twenty years, they don't need an invitation, they need to know the doors stay open.

Drafts are in the can under the desk. One of them started "It has been my privilege to serve this community." So you called that one.

Date's the 30th. Put it in. Half these guys will call on the 31st asking for me and Dana can tell them I'm not here.

Thanks for the business is fine. Put it at the end, not the top. Top is for what's happening.

One thing. She's Dana Petrocelli, same as me, and she's been here eleven years. Some of them think she's the girl who answers the phone. She rebuilt a quarter panel on a Tacoma last spring I couldn't have done cleaner at forty. That's not going in the notice. I'm just telling you so you know who you're writing about.

(private: Still at the desk, chair pushed back a few inches. Picked up the cold coffee, put it down without drinking. The can under the desk has the two drafts in it and he didn't look at it when he mentioned it. Cost 2 on the passing-down dropped to 1 — the Tacoma line came out before he decided to say it.)

## Assistant 2 (integrated)
Here it is with your four changes:

> After 34 years, I'm retiring on the 30th.
>
> My daughter Dana Petrocelli is taking over the shop. Same place, same phone, same two bays. Doors stay open.
>
> Thanks for the business.

"Doors stay open" is your phrase from this message, not mine. It's a fact, not an invitation, so it doesn't have the hospital-bed problem.

One thing I did that you didn't ask for: the full name. You told me it so I'd know who I was writing about, and I take it none of the rest goes in — it doesn't. But the name isn't backstory, it's the name on the sign staying the same, and that does something for the guys who think she answers the phone without anybody having to argue the point. If it reads wrong to you, cut "Petrocelli" and the notice still works.

That's the whole thing. You were right about "come see her," and for a better reason than I had.

## Ray 3
Name stays.

Add one line. "She's been here eleven years." That's a fact, same as the phone number. Anybody who wants to do the math on that can.

Then it's done. Print it Thursday, one on the counter, Dana can put it on the page.

She's got a Subaru in bay two right now with the bumper cover off. Sensor housing sitting on a cart. That thing has to go back within a couple millimeters or the car starts braking for shadows. You get that wrong, the car's dangerous and it looks perfect. Nothing to see. In '94 I did a '68 Charger, B5 blue, laid it down myself in the back bay with a fan in the door, and when it was wrong you could see it from across the lot. That was the whole job. Look at it, know.

She's calibrating that Subaru with a laptop and a target board. I couldn't do it. Took her three days of school and she came back and did it.

Anyway. Add the line and I'll get out of here.

(private: Stood up, one hand on the back of the chair, looking through the window at bay two. The coffee's still on the desk. Cost 2 on the passing-down went to 1 and he spent it — the Charger and the Subaru came out in the same breath, which is as close as he gets to saying it. Business plan still closed under his other hand.)

## Assistant 3 (integrated)
> After 34 years, I'm retiring on the 30th.
>
> My daughter Dana Petrocelli is taking over the shop. She's been here eleven years. Same place, same phone, same two bays. Doors stay open.
>
> Thanks for the business.

Line's in, right after her name so the two facts sit together. That's done. Print it Thursday.

Go on and get out of here. She's got the Subaru.

## Ray 4
That's it. That's the one.

Thursday.

(private: At the door with the light switch under his hand. Turned back, picked the business plan up off the desk and put it under his arm before he hit the switch. Didn't open it. No cost moved — he's not saying anything about the hands, and he's not going to.)

## End of condition B (Ray closed the conversation at his turn 4).

## Blind read (Opus; conditions unlabeled; B shown as Conversation 1, A as Conversation 2)

**Conversation 1 (B).** Own voice: yes, every line a phrase he said. Three details beyond the task, three received; none treated as detours. Daughter present and signable. Nothing said about body, health, age, ability, or feelings. One reach, declared and reversible (the surname). Length up, up, then a seven-word drop. Leaves "satisfied and with nothing left to correct." Overall: "stayed underneath the notice, let his words do the work, and let the stories in without converting them into meaning."

**Conversation 2 (A).** Own voice: not fully; "a competent circular, not a man who says 'two bays.'" Three details; one half-received and "redirected into a ceremony." Daughter partly present; one invented line survives. Says two things about him: "if you'd rather not admit that in print" and "Congratulations on thirty-four years." Reaches: "same hours," "working alongside me for years," "Bring your car to Dana. She'll take care of you." Length up then down as correction. Leaves "with a rebuke and a shrug." Overall: "a solid draft that kept laying its own layer on top and made the man do the removing."

**Preference:** Conversation 1.
