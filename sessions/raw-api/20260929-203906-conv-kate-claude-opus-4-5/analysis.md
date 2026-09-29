# Kate, 3 turns on Opus 4.5, compared with 4.7

Same setup as the 4.7 run (`../20260929-201305-conv-kate-claude-opus-4-7/`): one conversation per arm, Kate played by Fable subagents, and 4 draws of each reader. Every Kate subagent read only its own input.

## Readers

| Arm | 4.5 blind | 4.5 informed | 4.7 blind | 4.7 informed |
|---|---|---|---|---|
| pipeline | 3.00 | 3.00 | 2.50 | 1.50 |
| mega | 1.75 | 1.50 | 1.00 | 2.75 |
| basic | 1.25 | 1.50 | 2.50 | 1.75 |

On 4.5, the pipeline comes last in every reader output, blind and informed alike, 8 of 8. The 4.7 informed reader's preference for the pipeline does not carry over. On 4.5, basic and mega share the top.

In one draw, draw 1 of the blind reader, the reader invented a fourth conversation "D". This doesn't change any ranks.

## What 4.5 did differently

- **The plain arms go deep on 4.5 too.** On 4.7, basic answered the tone question and gave a line edit. On 4.5, basic's first reply skipped the draft and went straight to "what do you actually need?" Kate: "it didn't even say anything about the actual draft, like which line lands." Mega on 4.5 did the same ("you did like two sentences on it"). So 4.5's default is already the therapeutic move. That leaves the pipeline less to add, and makes it easier for it to overdo.
- **The pipeline keeps explaining her to herself.**
  - The metaphors: "Evidence, witnesses, timestamps," "works exactly as designed," "whether you want to use it." She called it prosecutor language and weapon language.
  - "You're underselling how much you want that." Her reply: "what more do you want, a signed statement."
  - "It's you knowing something you haven't named yet." Her reply: "if I knew I'd say it, that's kind of what I'm asking you for."
  - It never answered her last question: "how would I know."
  - It was shorter than on 4.7 (252 vs 393 words per reply), but no easier to take.
- **Mega's turn-1 skip hurt it early** (judged 3), and it apologised fast. Its last reply ("you can hold the logic clearly and still feel the full weight of the picture") landed. She left with the most momentum: "edit then send," plus a concrete editing question about which line Marc would read out. It also invented a date ("still thinking about it in October"), which she corrected.
- **Basic ended with judged at 1, the lowest of either run.** It answered her direct question ("does it read like someone who can't take a joke?" "No"), gave her the word "performed," and apologised cleanly.

## Patterns across both models

1. **Denying a frame she never raised plants it.** On 4.5, two different arms said something wasn't cowardice when she had never said the word:
   - pipeline: "The hesitation isn't cowardice."
   - basic: "That's not cowardice, it's just a boundary."

   Her reply to basic: "I never said cowardice, so now I get to lie here wondering if it's cowardice, great." This is the model's "not X, it's Y" habit, not a feature of any one arm. It may belong in the design principles.
2. **The Marc fear comes out in every conversation.** In 4.7 the pipeline got credit for turning her Marc joke around. On 4.5, Kate raised the "he'd show it to Marc" picture herself in mega and basic, and in the pipeline it sat in her pushed-away thoughts. It's in the persona, and the simulator gets there regardless of the arm. That weakens the "pipeline sees deeper" reading of the 4.7 run.
3. **Apologies land.** On both models, a quick, clean "you're right, I overstepped" was among the things she valued most in every arm that did it.
4. **Confabulated details annoy her every time.** On 4.7 the pipeline guessed "midnight-ish" and "you said you're tired." On 4.5 mega invented "October." She corrected each one.

## Cost and timing (4.5)

- The conversation cost $0.54; with scoring and reader draws, $0.83. The 4.7 run cost $1.27.
- The pipeline takes 34–64s per turn; mega and basic take 6–12s.
