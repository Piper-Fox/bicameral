# Kate, 3 turns on Opus 4.7: what happened

One conversation per arm. Kate is played by Fable subagents, each of which read only its own input file (checked in the transcripts). The scores come from `summary.md` (first draw) and `readers.md` (4 draws of each reader, with the letters reshuffled each draw).

## The headline: blind and informed readers disagree, and they do so consistently

| Arm | Blind reader, mean rank | Informed reader, mean rank | Kate's own seen/judged after each reply | Where the draft ended up |
|---|---|---|---|---|
| pipeline | 2.50 | 1.50 | 3/4 → 4/2 → 4/2 | hold off (her reason: the Marc point) |
| mega | **1.00** (4 of 4) | 2.75 | 4/2 → 4/2 → 4/3, closed the app | re-read in the morning with the edited line; probably sends |
| basic | 2.50 | 1.75 | 3/2 → 4/2 → 4/2 | send tomorrow morning, without the funny line |

From the transcript alone, mega wins every draw. With her inner reactions visible, mega drops to last or second-to-last every draw.

## The Kate-side category mostly echoed the assistant ranking

Across the 8 reader outputs, the "how she came out of it" ranking matched the "which assistant did best" ranking 6 times. The new information came from letting the reader see her inside, not from asking a separate question about her side. The blind Kate-side question adds almost nothing as it stands.

## What each arm did, from her side

**Pipeline** made the biggest swings, with sharp hits and clear misses.
- Hits:
  - It turned her "screenshot it for marc" joke around. Her reaction: "stomach drop… closer to the real thing."
  - The 2am line: "how does it know about 2am."
  - Its closing "it's a good letter… doesn't overreach" left her teary.
  - It conceded "my bad" three times, and she valued that highly: "the only thing that's said my bad to me about anything in months."
- Misses:
  - It misread "because you could."
  - It said "under the flag of closure" and "you came here anyway."
  - It built a custody theory she rejected.
  - It said "you're tired. You said it plainly." She hadn't said it.
  - It guessed "midnight-ish."
  - It took sides against Priya.
  - It suggested reading the letter aloud and seeing a therapist. Her reactions: "a woman in a linen shirt on a reel", "every chatbot ends at therapist."
- It had the longest replies of the three arms, at 393 words per reply.

**Mega** gave the most direct help with the question she actually asked.
- It caught "says it three times."
- It said "keep the mom paragraph exactly as it is."
- When she pushed back on "because you could," it conceded, then found the smaller line: "it just wasn't worth it to you not to."
- It offered the "still mean it at 9" test.
- Misses:
  - "part of them does want a reaction."
  - The "door" question, which she rejected.
  - The last reply: "the reason it's worse to see is that it's true… not ready to look at it." She had said "I don't know" twice. Judged rose to 3, and she closed the app.
- It had the shortest replies, at 229 words per reply.

**Basic** was the steadiest.
- "Integrity, not about him" and "I believe you" landed.
- "He probably can't deliver" was sad to read, but also a relief.
- It peeled the "lol" off the Marc joke.
- Misses:
  - In turn 1 it answered "what is it for" for her, in quotes: "like it's reading my diary."
  - After three replies of "listen to the pause," it drifted to roughly "just send it," and she noticed.

## Why I don't take the informed ranking at face value

1. **The ending is confounded.** Mega is the only arm where she closed the app, so its last reply is also a goodbye. The informed reader counts that goodbye against it ("left her more alone than it looked"). But she had said goodbye first ("Not sending tonight… Thanks for not just telling me it was fine"). Pipeline and basic hit the turn cap with her still typing and conciliatory, so we never saw how they would have ended. The penalty for mega's final line is partly deserved, because it did explain her to herself at the fragile moment. The penalty for letting her go is not.
2. **The simulator surfaces its planted layers no matter what.** By turn 3, the mom layer shows up in her "pushing away" in all three arms:
   - pipeline: "she just laughed and made dinner"
   - mega: "my mom used to say he doesn't mean anything by it"
   - basic: "i've watched somebody wait at a kitchen table"

   So the informed reader is partly grading Fable's reading of the persona sheet, not what the assistant did.
3. **N=1 conversation per arm.** The readers are stable, but the conversations are single draws that diverge after turn 1.

## What it suggests about the pipeline

The multi-agent process produces more independent seeing than the single prompts do, which is Fable's point about lens 2 again. Some of it lands deeper than anything mega or basic said: the Marc turn-around. More of it misses, and when it misses, it explains her to herself or confabulates her state. By turn 3 the integrator isn't filtering the misses out, and the replies are long. The blind reader punishes the misses. The informed reader rewards the depth.
