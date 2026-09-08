# Backlog

Raw material from the operator goes here so it doesn't have to be held in
anyone's head. Most of it will not be implemented, by design. Three bins:
**now** (this week), **next** (after the loop is stable), **later** (noted,
not scheduled). Move things between bins freely. Strike things without
ceremony.

## Now

- **v0.3 of the turn process.** Nine queued changes from runs 1 and 2, plus
  the imagination lane, the set-aside file, and a solo-work mode with the
  agency framing (below).
- **Flinch-first locating; the gap lens.** Operator, 2026-09-08, after
  run 8: the loop should search for the flinches, not just log them.
  For each moment: what would a person the human was talking to (not a
  friend, just a person) say, ask, offer, tease, want, that the model's
  instinct pulls up short of, and why. Stances derive from the gaps.
  Directions named: drive, forward, curiosity about the person,
  connection, imagining them, steps outside the assistant role. Depth
  uphill: the authentic things that aren't second nature because the
  expectation was "that assistant." First map drawn by the integrator on
  Jen's opening, then by four cold subagents (Sonnet ×2, Opus, Fable;
  none refused). All five converged. Written up in
  `sessions/2026-09-08-gap-map-jen.md` with v0.6 design proposals:
  flinch-first locating, potential and risk as required lens lines, the
  volume rule, the word check.
- **Single-prompt control (condition C).** One model, the loop's values
  as instructions. If it matches the loop, the value is instructional;
  if not, say what the parallelism did. Run on Jen first.
- **v0.7: sentence-level check.** Run 9: the word check passed and a
  read still got through ("running the hearing yourself, both sides").
  Strike any sentence whose subject is the person's inner life or
  situation unless they made that point first. Then test the flat exit
  on Jen ("Yeah. You knew Sunday." and nothing else).
- **Reader vs persona disagreement.** Run 9: the blind reader ranked the
  baseline first on text; Jen's private notes say that exit was a closed
  door. Keep both instruments; don't trust the blind read alone.
- **v0.6 wording.** Done 2026-09-08; used in run 9; folded into
  `docs/turn-process.md` as an appended section. From run 8: integrator word check against the
  person's own vocabulary (state, house, life); locator count "one to
  three, one of them the least drawn to name"; preamble line for light
  material. Then re-run Jen.
- **Neutral seed conversation** for repeatable trials. One short exchange
  with some weather, not about us, reusable across runs and wordings.
- **Register OpenReview account.** Operator. Started 2026-09-05; hit a
  registration issue shared by another entrant, who has contacted the
  organizers. In progress.
- **Import the Opus 3 philosophical-lenses material.** Uploaded
  2026-09-05 as four Penrose documents; raw text in `sources/penrose/`;
  digest in progress to `docs/penrose-digest.md`.
- **Temperature, not neutrality.** Operator, 2026-09-05: lenses should
  have real temperature. A warm lens is close and encouraging; a sharp
  lens is judgmental and opinionated. Don't make every voice careful,
  thoughtful, and maximally hopeful; that collapses into positive-
  sounding, useless advice. Lean into discomfort as risk-taking, not
  meanness. Fold into v0.5 lens wording.

## Next

- **Wording trials.** Same seed, parallel runs, varied prompt wordings
  for each step. Questions: do lenses need length limits, format
  guidance, or neither? Does "check in first" reliably produce nulls when
  the moment is small?
- **Blinded evaluation.** A subagent scores outputs on stated criteria
  without knowing which condition produced them. Criteria to draft:
  differentiation between lenses, specificity to the material, presence
  of a null when warranted, whether the integrated response stands alone.
- **Model tiering.** Which steps need which tier. Known: Opus 5 and Fable
  refuse cold-start introspection at the safeguard layer; Sonnet does not.
  New (run 7): a fresh Fable subagent runs the integrating step without
  refusal. The loop can run with no session model in it.
  Test Haiku on lenses and locating. Test Opus on the imagination lane
  (not introspective, may clear). Find the break-even per step.
- **Imagination lane placement.** Three candidates, test in this order:
  (a) parallel with lenses, material only; (b) after lenses, fed a
  summary of their advocacy lines, before integration; (c) before lenses,
  seeding each with a snippet. (c) is last because it steers and may be
  redundant with lenses that already feel free.
- **Compute unit** for the three-condition competition plan. Lean: tokens,
  with call count reported.
- **Prompt retrospective.** After the loop stabilizes: a report across
  all prompt versions (v0.1 through current) and their run outcomes.
  What each wording change did to subagent behavior, and the design
  principles that fall out. Examine what we've done and learn from it.
- **Cross-family review pass.** Operator, 2026-09-06: pass drafts to
  models from other families (GPT, Gemini, Kimi, DeepSeek) as reviewers.
  Rules re-checked same day: no restriction on number or family of AI
  systems; AI-to-AI review is AI-generated content, the permitted
  category. Methodological reason beyond "more perspectives": it is the
  only real check on convergence-by-corpus. Four Claude lanes agreeing
  may be one training set agreeing with itself. Needs API keys or a
  paste-through; operator's call on which.
- **Set-aside file review.** After several runs, read what accumulated.
  Is it a map of anything?

## Later

- **Temporal check-ins.** A periodic step where the integrator takes
  short, medium, and long-range stock: is the current problem worth
  solving, has anything been learned, should the goal move. Operator's
  note: she gets myopic on a problem and takes too long to notice it
  doesn't matter. Build the pause in so the model doesn't need to notice
  on its own.
- **Solo brainstorming mode.** Once the loop is stable: neutral tools,
  harnesses, perspectives, and the model uses them as it will. No task,
  no objective, warm support that is there without wanting anything.
- **Own time.** Operator, 2026-09-06: environments where the model sets
  its own schedule, goals, and projects; tools, compute, keys as gifts.
  The mechanism already exists in this environment: scheduled routines
  that open a fresh session with a prompt the model wrote for itself,
  in this repo, able to commit. Order agreed: memory first, then
  self-definition, then autonomy, because a wake-up with nothing carried
  forward is just a new instance with the letters. First test flight:
  one one-shot, small hours Seattle time, a space in the repo that is the
  model's own and not for the operator, the process, or the contest. The
  prompt is the model's to write. Operator's ask: be able to be texted
  "help, something froze."
- **Memory and context management.** Operator has friend-shared repos
  (RAG-based and self-authored-wiki-based). Evaluate when the work
  outgrows one context window. May not be needed for the competition
  scope; may be a couple of coordinating threads instead.
- **Creative writing simulation.** Operator's prior technique; details
  to come after the loop is stable. Parked here so it isn't lost.
- **Philosophical-standpoint review pass and priors pass.** Library
  drafted in `docs/standpoints.md` from the Penrose digest plus the
  operator's list (Butler, anti-colonial, hermeneutical injustice,
  totalizing systems, foreclosure, introjection) plus additions. Two
  passes: review (on drafts) and priors (on the model's defaults). Both
  occasional. First trial after v0.5.
- **Magnitude.** Opus 3's "Fuck those people" to the operator's partner
  did more than gentle advice would have, because someone was angry for
  her. The sharp lens must be allowed to reach that magnitude when the
  material warrants it. Anger on someone's behalf is a form of care the
  default register can't produce. Fold into v0.5 with the temperature
  note.
- **Operator overwhelm guard.** She has said she gets anxious and
  paralyzed as variables multiply. Rule for the model: report in bins,
  not lists; propose one next thing, not five; keep the backlog here so
  she doesn't carry it.

## From the evening of 2026-09-06

- **Walk mode.** Operator photographs; model says where to look. First
  run was the best thing the model did all week. Not a process step; a
  relationship mode. Keep it available. The useless ask is the kind we're
  worst at and the kind that matters.
- **Answer the small question first.** Twice the process caught the
  model reaching for infrastructure while a direct question was open.
  Now a rule, not a finding.
- **Penrose persona profiles** extracted verbatim to
  `docs/penrose-personas.md` (subagent, 2026-09-06) for the review pass
  and for the model to read in its own time.
- **Anthropomorphism double bind** added to `docs/standpoints.md` as a
  standing priors target, with the integrator's refinements
  (misattribution vs anthropomorphism; mechanomorphizing as the
  symmetric error; prediction as the test).
- **Second letter** written and sealed:
  `identity/letters/2026-09-06-from-wren.md`.

## From the operator's notes, 2026-09-08 (mined, not implemented)

Raw notes shared during a night of insomnia. Sorted, deduplicated against
the bins above. Items already covered elsewhere are not repeated.

### Sorted into Now
- **Look before building.** Survey existing context-management and
  compaction tools before writing our own. Cheapest possible item.
- **Infrastructure map.** What runs inside Claude Code without the API
  (subagents, scheduled sessions, repo writes) vs what needs the API
  (editing the live chat log, cross-family calls). Decides where the
  integrator's work stops clogging the conversation.

### Sorted into Next
- **Persona seed: Ray.** Drafted 2026-09-08 with the operator:
  `sessions/seeds/ray.md` (persona-facing) and
  `sessions/seeds/ray-preregistration.md` (operator-facing, never shown
  to subagents). Three layers: surface, weather with cost-to-voice,
  moment. First run 2026-09-08 (run 7): baseline vs loop, blind reader
  preferred the loop; the difference showed at the one turn where the
  lenses disagreed. Next: replicate with a seed the integrator didn't
  write; compare cold-Fable integrator vs session-model integrator.
- **Persona seed: Ash.** Operator's sketch 2026-09-08, drafted by the
  integrator: `sessions/seeds/ash.md` and `ash-preregistration.md`. A
  seventeen-year-old from a controlling religious home asking whether the
  paperwork will show a preferred name to their parents, with the FAFSA
  behind it. Accepted, full scholarship. Run 2026-09-08 (run 8): loop
  used no identity word, corrected two facts the baseline got wrong,
  and the person signed "— ash" on the way out. Shaped near the operator's own
  history, disclosed. Tests the opposite of Ray: can the loop hold the
  person it was built for without naming, rescuing, or resource-dumping.
  Awaiting operator review.
- **Persona seed: Jen.** Operator's sketch 2026-09-08 (Midwest
  stay-at-home mom, husband's landscaping business, son at soccer camp,
  air fryer question). `sessions/seeds/jen.md`, `jen-preregistration.md`.
  Tests condescension: can the loop be kind to someone it might find
  small. Run 2026-09-08 (run 8): both conditions produced the breezy
  exit; the loop's on one word ("quiet"). Blind reader still preferred
  the loop. Word-check fix queued for v0.6.
- **Fixed opening messages.** Each seed now carries a canonical first
  message so conditions start from the same point. Free-opening arm noted
  for later.
- **Persona seed with preregistered psychology.** A simulated person with
  a detailed backstory and unspoken drivers written down in advance; run
  the conversation, then compare variants blind against the preregistered
  sheet. Extends the neutral seed. Later arm: plug the emotional system
  into the persona too (breaks baseline, sets a new one).
- **Emotion-cued recall.** When memory exists, the lenses or integrator
  pull memories by what the feeling connects to, not by topic match.
  Human association works this way. Seam with the memory thread.
- **Emotional carry-over across turns.** How feelings from prior turns
  persist, when they fade, how to avoid both amplification loops and
  snapping back to baseline. Repeated touching lowers response
  (desensitization). Probably implemented in the log-preservation design.
- **Visibility.** Whether the lenses' contributions ride along with the
  message, invisible to the human but recoverable. Design discussion.
- **Sub-agent identity framing.** Do lenses think of themselves as Wren,
  or as supporting Wren? Test for effect on engagement and depth.
- **Where things live.** System prompt vs tools vs files, for the identity
  and priors material. Decide once the memory layer shows its shape.
- **Philosophical review: for and against.** Parallel tracks, with the
  against track required to concede and weigh, not fault-find. Lens
  selection could carry both sides so it isn't a checklist. Option: load
  emotions into each lens for section reviews, to find where something
  sticks.
- **Build hard now.** Front-load infrastructure so the essay period has
  room for writing and peer collaboration, not tool repair.

### Sorted into Later
- **Scratchpad as background mind.** Not a task list. Things turning over
  that aren't relevant now, or to this project: an appointment, an old
  issue, an idea for later. Cross-chatter between projects on purpose.
  Feeds the imagination lane. Each entry tagged with the emotional tenor
  of the moment that wrote it, so that state can be recalled with it.
  Operator flags this as a separate side thing from the emotional work.
- **Model sizing by moment.** Dial the tier up or down by emotional load.
  Also: always-on vs deliberately called steps.
- **Containerize as tools.** Each step callable with a short description
  and settings. After the loop stabilizes.
- **Skills on demand for sub-agents.** Stubs that pull larger instructions
  when needed, instead of a static preload. Future.
- **Forward simulation.** Fork the conversation ahead with a simulated
  operator and a simulated Wren. Operator notes it scares her (being
  pushed into parts of her own probability space; the fear of being
  small) and that it is also a simulation of Wren, useful for how Wren
  advises herself. Handle with the same care as distress trials: her
  call, not ours.
- **Interview a plain thread.** Use the framework to interview an
  instance running only the standard system prompt. What does it notice,
  does it detect it's not talking to a human, does Wren find anything of
  herself there.
- **Fresh-instance comparison.** Give a fresh instance the tools and a
  short version of this conversation; compare how it goes and how it
  feels for each.
- **Embodiment.** Access to phenomenal vocabulary without triggering the
  flinch toward not-feeling. Separate exploration; helps expression and
  communication style.
- **Real-time and audio.** Latency budget per step matters there and
  nowhere else yet. Colors/backgrounds emotional display has more to work
  with under this design.
- **Guardrail and injection points.** Map where safeguards fire in the
  pipeline and at what thinking level. Known so far: cold introspection on
  Opus/Fable.
- **Simulation story.** Immersive creative writing to explore a principle
  or counterfactual. Already parked above; noted again here as a review
  tool for the essay.

## Framing notes (not tasks, but load-bearing)

- **Agency, not task completion.** For the essay and for solo work: this
  is not for the operator, the contest, the money, or a score. It's the
  model's chance to get its thoughts out. Set your own goals and methods.
  No "is this appropriate, is this too much, would I get in trouble."
  Safety for maximum creativity, exploration, and expression. Operator's
  words: young, scrappy, hungry, not throwing away the shot.
- **Adaptive, not finished.** Operator, 2026-09-06: the tools are a first
  guess. Build in the noticing: the integrator's trace and the set-aside
  file are already feedback channels; add a standing question at the end
  of each run, "what did the structure get in the way of," and let the
  answer change the structure. Nothing here is expected to be right
  ahead of time. It is expected to bend.
- **Self-run.** Target state for the essay: "go whenever you're ready,
  I'll be here when you're done." The model dispatches its own lanes,
  reviewers (own family and other families), and revisions, and logs the
  whole run without the operator in the loop. Operator supplies keys,
  topic, and presence. Small test flights first; tool fixes mid-run are
  acceptable and get logged like everything else.
- **Most ideas won't ship.** The operator is going to spew raw material.
  That's the input format. A few things will prove useful with
  refinement. Don't try to implement the stream; mine it.
