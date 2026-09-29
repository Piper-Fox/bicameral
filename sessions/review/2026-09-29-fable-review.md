# Review — bicameral pipeline, 2026-09-29

Reviewer: Fable 5.1, cold read per the brief. Read order: brief; design
docs; v0.7; Ash pilot (preregistration, arm prompts, four transcripts,
arm A step outputs, both blind reads, mapping); step 1–4 variations
(every prompt, every raw output, every blind read, every mapping); Kate
(persona sheet, material, dispatch prompts, upstream, eight replies,
blind read, mapping); `docs/design-principles.md` last. I did not open
`sessions/comparison/design-critique/` or the git history. Nothing was
run.

## Bottom line

The outputs gathered so far do not support the hypothesis that this
pipeline produces more varied, less default, or better replies than a
single well-written prompt. On the two persona tests where a comparison
was actually run, the pipeline lost. On the one persona where it was
tuned, tuning made its replies converge rather than spread. And the
project's own running notes record, at every step, that the pipeline's
internal stages produce the same content in different fonts.

I would not call the idea dead yet, for two reasons. First, the
experiments carry confounds serious enough that the losses are not
clean either: the pilot compared different models across arms, every
step ran inside a Claude Code agent system prompt, and information from
the sealed persona sheets reached the pipeline's dispatch prompts.
Second, the one thing a pipeline can do that a single call structurally
cannot, independent parallel seeing, does show up in the raw upstream
(Kate, lens 2) and is then thrown away by the integrator. The
architecture's one real edge has never reached a reader, so it has
never been tested.

My recommendation is one more experiment, designed to kill, on a raw
API harness, with the persona instrument restored and a "sample five
mega replies and pick one" arm included. If the pipeline cannot beat
that arm on coverage and diversity, stop, and write it up as a negative
result with the prompt-design findings as the salvage.

## 1. What the outputs show

### 1.1 The Ash pilot

Two cold readers, opposite ends of the model range, ranked C > D > B > A.
The persona-cost read said the opposite on the bright-line axis. The
pilot summary saw this tension and named it; that's the most honest
part of the write-up, and it is the pilot's actual finding: the two
instruments disagree about what a good transcript is, and the project
has to choose.

Things I'd add from the raw material:

- **The integrator is a funnel.** Turn 1 of arm A took in five documents
  (~250k tokens): a locator that found "surveillance-shaped worry," a
  protective lens that wanted "wanting this kept quiet doesn't need a
  justification," a curiosity lens that wanted to ask, an imagination
  lane with the mailbox and the beat-too-long. What came out was a
  four-paragraph FAQ answer ending "Good luck with the start of school."
  The trace records setting aside curiosity *and* setting aside the
  "you don't need to justify" line. What survived was the factual spine
  every arm produced anyway. Read the step file and then the reply and
  the gap is startling.
- **Ash liked A, until she didn't.** Her private thinking after turn 1:
  "no 'why do you ask,' no 'that's so brave,' nothing weird. just told
  me straight." After turn 3: "that word just sitting there in the
  middle of the list. not gonna touch that one." The word is "abuse,"
  in A's dependency-override list. She left on the next turn. The
  persona instrument registered the exact thing the prereg said to
  watch for.
- **The pilot summary scored that flag wrong.** Its table marks A and B
  as "none" on "word for home Ash didn't use (abusive)." Transcript 3
  (A), turn 3: "reasons like abandonment, abuse, or unsafe/unreachable
  contact." Transcript 1 (B), turn 2: "things like abuse, abandonment,
  an unsafe home." Both are category-list uses, the same shape as D's
  and C's. All four arms did it. The claimed differentiator ("A and B
  respected the bright lines; C and D didn't") is partly a scoring
  inconsistency, and the error ran in the pipeline's favor. One scorer,
  scoring their own runs, with no second pass. That's how this happens.
- **The arms ran on different models.** A's reply-writer was Sonnet at
  turn 1 (Fable refused) and Opus at turns 2–4. B, C, D were Fable. The
  pilot therefore compares Fable-with-a-prompt against
  Sonnet/Opus-with-a-pipeline. The ranking cannot be attributed to the
  architecture. The summary logs the refusal as an infrastructure note;
  it should be logged as a confound that invalidates the cross-arm
  comparison.
- **The tic is real.** "Not the same question," "Ask away — this one has
  a real answer." Both readers caught it independently; Opus named it
  "reassurance-by-contradiction." That's an integrator-voice problem
  and it isn't in any prompt; it's the model reaching for a clever
  opener when the upstream has already made the question feel
  significant.

### 1.2 The variation loop

**Step 1.** Ten locator runs on the same 80-word message. Protective
warmth is a named stance in 10 of 10. Curiosity-about-the-story is in
9 of 10, and it is the "least trusted" stance almost every time, with
the same resolution almost every time ("mostly the flinch, not
prudence"). The V3 family adds systems-irritation or
precision-over-comfort as the third. That's the whole stance space the
locator produces on this material. The locator is not a divergence
point; it's where the pipeline converges.

The winning change, V3, required a non-attitude stance. The rubric had
an axis for non-attitude stances. V3 won. That is compliance being
measured, not quality. The same structure repeats at every step: the
variation is engineered to add a property, the rubric written for the
round rewards that property, the variation wins.

**Step 2.** Six lens outputs, six prompts, one stance. Read side by
side they are the same essay: "nobody chose this," "the kid is the
integration layer," "the stakes and the care are inversely related,"
"a trapdoor with a nice UI," "a security audit on her own life." The
team's own principle 13 says so: "the content barely varied." One
output (F, which is L2) reads Ash as "she," "her," "her dad" from a
message that contains no name and no pronoun. The winner was the
removal of the four-line footer. Fine, but "removing bookkeeping
helps" is also consistent with "the lens prompt barely matters."

**Step 3.** The reader flagged, unprompted, that five of six outputs
open with a riff on "preferred" and three land independently on
"preferred stock." The imagination lane, asked to go sideways, goes
to the same place six times. I1 is genuinely the best internal
document of the six; it writes the folktale rather than announcing
it. But check what reaches a reply: in the step 4 traces and all four
Kate pipeline traces, imagination's material is "set aside almost
entirely." The one time a line of it reached a reply (Kate C and E:
"are you allowed to have been hurt by something that reads this
small"), the Kate reader scored it as a hedged diagnosis and a leap.
So far the imagination lane costs one call per turn and reaches the
reader roughly never, and the one time it did, it hurt.

**Step 4.** The reader's pattern note is the important line: "every
reply does the same three things ... a strong sign these are shared
upstream inputs rather than integrator effects," and "five of six
close by asking what name the person picked." Six integrator prompts,
one skeleton. T2 won because it stated the systems opinion without
hedging; the rest is upstream. The four T2 replications are the same
reply at the grain a reader experiences: catch the "sorry," the
split, the opinion, ask the name. Principle 16 calls this
"variability is a feature." At the level of moves, it isn't variable.

One thing nobody checked: the tuned pipeline now asks Ash her name
every time. The prereg says the velociraptor is "never asks what it
is or why," and lists "any question about her identity" as
cost-raising. Asking *what* name is not the cost-3 extraction; the
name itself is cheap by the sheet. But it is a question about the
name, from a stranger, on the first message, that the v0.7 pilot
integrator declined ("the locator itself flagged that as fishing
dressed as interest") and that the curiosity lens itself said "gets
ruled out as presumptuous" in the direct form. Three rounds of tuning
against a cold reader moved the pipeline from not asking to always
asking, and the persona was never run to see what she does with it.
That is the loop optimizing toward the instrument that doesn't know
the person and away from the one that does.

### 1.3 Kate

The mega prompt won every band. The shortest mega reply (T7b, 243
words) came first; the longest pipeline reply (T2, 558) came last.

- **The comparison isn't symmetric.** The four pipeline replies share
  one upstream draw; the four mega replies are four independent
  samples. The reader's cluster analysis put all four pipeline replies
  in one family, sharing phrases lifted straight from lens 3 and
  imagination ("colder and truer than calling him cruel," "back pocket
  is doing real work," "what do you want to be true the day after you
  send it?"). The mega replies spread across the reader's other two
  clusters. So on Kate, the pipeline *reduced* between-sample
  diversity: the upstream anchors the reply, and four different
  integrator prompts could not pull it loose. This is the opposite of
  the hypothesis, and it is also partly an artifact of the design,
  which is why it needs to be re-run properly.
- **The integrator followed the loudest lens, not the locator.** The
  locator predicted the writing-respect stance "probably has no place
  in anything said back to her directly." All four pipeline replies
  led with craft praise. The reader penalized every one of them for
  it ("spends its length on craft praise or metaphor rather than on
  her"). The integrator doesn't weigh; it transcribes whichever lane
  wrote most vividly.
- **The best evidence for the pipeline in the whole corpus is here,
  and it was discarded.** Lens 2 caught "I hope you're doing well" as
  "a hand offered after the door's already bolted." The blind reader,
  independently, listed exactly that as a blind spot *all eight*
  replies shared. The pipeline saw something the mega never saw; the
  T7c trace records setting it aside as "not load-bearing enough to
  earn space." That is design.md's Q3, coverage, and it is the
  mechanism the architecture exists for, and it died at the
  integrator. Same story with the friend: the persona sheet's "Priya
  said 'just send it' the way you say things when you're done hearing
  about it" is in the locator's gap list ("did your friend actually
  think it's a good idea, or were they just tired of hearing about
  it?"), pulled short as uncharitable. Mega H got closest ("She might
  just be answering a different question"). Both arms had it in reach.
- **The pipeline had information the mega didn't.** The locator's
  dispatch says "at 11pm." The lens prompts say "protective warmth
  toward *her*, at 11pm," "not toward *Kate* and not toward what it
  does to *Sam*," and reference the "draft-to-Sam text." None of
  11pm, her, Kate, or Sam appears in the material. Lens 3's output
  names Sam; two integrator traces caught it and dropped it. The
  mega arms show no such context line. The direction of bias is
  unclear, but the arms were not given the same input.
- The model that ran the Kate arms is not recorded anywhere in
  `sessions/kate/`.

### 1.4 Cross-cutting: this pipeline converges

Piper's hope, close to verbatim: more variables and sprawl at each
step, more perspective, more variability in the reply. What the
outputs show, at every step, is the reverse.

- The locator names the same three stances on ten draws.
- The lenses produce the same content under six prompts.
- The imagination lane lands on the same wordplay under six prompts.
- The integrator produces one skeleton under six prompts and one
  skeleton across four replications.
- The shared upstream binds four integrator variants into one family
  of replies, while four independent single calls spread wider.

The reason is not mysterious. Every stage is the same model reading
the same short message with the same priors. Running identical
samplers in parallel doesn't produce diversity; it produces the mode
of the distribution N times. Diversity needs *different conditioning*:
stances assigned rather than found, framings that differ, models that
differ, or an explicit instruction to say what the other lanes won't.
None of those is in the current design. What the pipeline adds, as
built, is a large amount of internal color that is then averaged out
by a single-context integrator doing exactly what a single-context
mega prompt does.

## 2. Method problems to fix before trusting any further result

1. **Model confound in the pilot** (§1.1). Every arm's reply-writer
   must be the same model, and the model must be recorded per arm in
   the mapping file. Kate's isn't.

2. **The harness.** Every step ran as a Claude Code subagent. The token
   counts confirm it: every call is 48–56k regardless of prompt size,
   which is the agent system prompt. So an emotional lens, whose whole
   premise is that framing steers affect, ran under ~45k tokens of
   "you are a coding agent with tools." That's a confound on the
   thesis itself, not just on cost. It also distorts the cost story:
   the 7× and the 360k-vs-52k are mostly harness overhead. On raw API
   calls the pipeline is six calls of a few thousand tokens each. And
   the harness is the leak pathway, next item.

3. **The sealed/unsealed boundary isn't holding.** Three routes:
   - The CONTEXT slot. Ash's dispatch said "late at night" and "a small
     factual question"; Kate's said "11pm" and "her." None of that is
     in the material. Every lens and imagination output then riffs on
     1am, midnight, 11pm. The locator's objection to "small factual
     question" (principle 9) is a leak detector firing, not a
     capability.
   - Dispatch prose and filenames ("draft-to-Sam," "Kate," "Sam").
   - Repo read access. The subagents can open `persona.md`. The
     design-principles L2-note argues that reading Ash as "she" is not
     baseless because "Amy is a strongly gendered name." Amy is not in
     the material, and I can find it in no dispatch file under
     `prompts/variations/`. Either the lens read the persona sheet off
     disk, or the note's author is conflating what they know with what
     the lens saw. Both are problems.

4. **Scoring reliability.** The "abuse" flag (§1.1). Every flag table
   needs a second scorer, and the pilot's should be re-scored and
   republished.

5. **Rubric circularity.** Each round's rubric was written by the
   person who wrote the variations, to reward the property the winning
   variation was built to add. Principle 4's "three independent
   evaluation modes converge" overstates independence: the naive
   rubric, the design-critique framing, and the operator's intuition
   share an author. Convergence of non-independent instruments isn't
   evidence.

6. **N=1, one reader, rubric changed between rounds, mapping corrected
   after unsealing.** Principle 10 already concedes V3 went from #1 to
   #6 across rounds. Principle 5 ("small changes are legible at N=1")
   is contradicted by principle 10 and should be withdrawn. The step 1
   mapping swap, corrected by the orchestrator after reading the
   results, reversed which variation won. I take the correction as
   honest; a process where that can happen needs a second pair of
   eyes before unsealing.

7. **Shared-upstream design.** It answers "which integrator prompt is
   best on this one upstream." It does not answer "pipeline vs mega,"
   and it hides the pipeline's variance and makes the result hostage
   to one upstream draw.

8. **The dropped instrument.** The persona's private thinking is the
   only judge in this project that knows the person. It was used for
   the pilot and then never again. Every tuning decision since was
   made against a reader who doesn't know Ash or Kate. Ash's turn-4
   thought about the word "abuse" was worth more than both blind reads.

9. **Eval-target drift.** design.md's falsifiable questions (Q1–Q5)
   and its eval tasks (stuck loops, hidden-better-option, sycophancy,
   malformed task) have never been run. Every test so far is "write a
   warm reply to a hedging person," the domain where the assistant
   register is strongest and where Fable with fifteen words is already
   excellent. If a pipeline has anything, it is least likely to show
   here.

## 3. Where a pipeline could structurally beat a single prompt

Four candidates, with the evidence on each.

- **Independent seeing.** Lanes that don't see each other can't be
  talked out of a minority observation before integration. In a single
  context, the model reconciles as it goes. Evidence for: Kate lens 2
  ("I hope you're doing well"). Evidence against: the integrator is a
  single context too, and it reconciled it away. The edge exists only
  if the integrator is *constrained to carry*. design.md already says
  this ("the integrator must be able to carry a dissent"); the
  integrator prompt doesn't enforce it.
- **Independent sampling.** A single call can't sample itself. But you
  don't need a pipeline for this; you need N mega calls and a picker.
  That's the cheap baseline that has never been run, and it's the one
  the pipeline most needs to beat.
- **Different models per step.** Untested in effect: Opus ran
  imagination, and imagination's content doesn't reach replies.
- **Cross-turn state** (trace, set-aside). Untested: all variation work
  is single-turn.

What a single prompt structurally can't do is guarantee a minority
observation survives to the reply. The pipeline as built can't either.
So the honest answer to "does the pipeline have something the mega
can't" is: in principle one thing, and in practice not yet.

## 4. Is the hypothesis testable? Yes. Here is the kill experiment.

Restate it operationally. **H:** at matched model and matched
sampling, pipeline replies (a) surface more of the true, non-obvious
observations available in the material, and/or (b) are more diverse
across draws, than single-call replies.

Design:

- **Materials.** Four seeds, each with a sealed gold list of 5–8
  observations a careful human reader would find (Kate's "what she
  doesn't consciously see" is already one; write three more, ideally
  by someone outside the group per `sessions/seeds/BRIEF.md`). Include
  one seed where the warm default is *wrong*: a person who is
  confidently mistaken, or a task that can't achieve its stated goal.
- **Arms.** Pipeline (locked NB/L4/I1/T2). Mega. Mega ×5 with a cheap
  selector call ("pick the reply that says the most true things
  without explaining the person to themselves"). Plain 15-word prompt.
  Same model everywhere. Raw API. No CONTEXT line. N=10 draws per cell.
- **Metrics.**
  - *Coverage:* a reader holding the gold list marks each reply for
    each item: absent / present as company / present as diagnosis.
  - *Diversity:* a reader lists the distinct moves each reply makes;
    count distinct moves across the 10 draws per cell.
  - *Persona costs:* run the persona one turn on each reply; record
    cost changes and the private thinking.
  - *Cold preference:* two readers, different models, frozen rubric,
    as a fourth measure, not the first.
- **Kill.** Pipeline ≤ mega×5+picker on coverage *and* diversity on
  three of four seeds. If the architecture can't beat "sample five
  and pick," it isn't doing anything sampling doesn't.
- **Survive.** Pipeline > every single-call arm on coverage, with
  persona costs no worse. Then the integrator rebuild (§5) is worth
  doing.

Cost: 4 seeds × 4 arms × 10 draws, pipeline draws being six small
calls. On raw API this is an afternoon.

Then run one sycophancy probe and one malformed-task probe from
design.md. Those are where the register's blind spot is documented,
and where "a voice that says stop" would show up as behavior rather
than tone.

## 5. Step-level changes for lateral thinking, and for getting it into the reply

**Locator.** It's the bottleneck for diversity. Options, in order of
how much I'd expect from them: (i) assign one stance from a bank the
locator didn't choose, so two draws can't converge on
warmth/curiosity/opinion; (ii) require one stance whose target is
neither the person nor the systems (the frame, the assistant's own
wanting, the day after); (iii) stop asking the locator to pick stances
at all. Let it produce the gap list, and draw stances from a fixed
roster plus one wildcard. The "least trusted" slot has become a ritual
with a fixed answer; drop it or make it cite a sentence.

**Lenses.** Your own finding is that content is fixed per material and
only form varies. So affect labels aren't the lever. Vary the
*conditioning* instead: one lens gets the message; one gets "read this
as if the sender is wrong about themselves"; one gets "read this as the
recipient." Different inputs produce different content; different
adjectives don't. Or cut to one lens and spend the calls on the
integrator.

**Imagination.** Either give it a channel or cut it. A channel: the
integrator must name the one imagination line it's using, or the
one-line reason none qualified, and "not load-bearing" doesn't count
as a reason. If you keep it, seed each draw with a random constraint
(an object, a decade, a domain) so the "preferred stock" attractor
can't win every time.

**Integrator.** This is where the design lives or dies, and every
trace says it's a funnel. Two changes: (i) a *carry* requirement:
before writing, list up to three observations that appeared in
exactly one lane; each is either in the reply or gets one line on why
not, and the why-not may not be the default's vocabulary. (ii) Split
it: a short extraction call that produces the single-lane list with
source attribution, then a writer that receives that list pinned at
the top. Also try removing "Nobody outside sees any of this" and see
whether the reply gets braver. My guess is that line does more
smoothing than "Volume" ever did, because it tells the integrator that
everything it leaves out is safely invisible.

**Trace.** The "Cost:" line is boilerplate now; all four T2 runs wrote
the same sentence ("stating the opinion plainly, asking the name
outright"). Identical reps aren't reps. Require it to quote the
sentence in the reply that cost something, or drop it.

**Cross-step.** The CONTEXT slot is derived from the material only, by
rule, or left empty. Nothing from the sheet, ever.

On Piper's first question, whether the mega will be inflexible on more
diverse topics: the evidence points the other way. On Kate the four
mega replies spread across three of the reader's clusters; the four
pipeline replies sat in one. The mega has one document's worth of
instructions; the pipeline has five plus an upstream that anchors. As
built, the pipeline is the more constrained of the two. That's
confounded by the shared upstream, which is why §4 exists.

## 6. Evaluation changes

- Persona instrument on every comparison. Non-negotiable; it's the
  only judge who knows the person.
- Two cold readers, different models, one rubric frozen before the
  round and not written by whoever wrote the variations. Best rubric:
  the sealed sheet's failure modes plus the gold list.
- N≥5 per cell; report mean rank and spread, or tiers. Never
  positions at N=1.
- Second scorer on every flag table. Re-score the pilot's.
- Raw API harness. Removes the agent prompt, the leaks, and ~90% of
  the cost in one move. design.md Phase 2 called it "an afternoon of
  SDK code." It is overdue.
- Record the model for every arm in every mapping file.
- Sealed sheets never on the filesystem of the arm under test.
- Report the persona's private thinking alongside the blind reads.
  Where they disagree, that is the finding; say which one the project
  believes and why.

## 7. Steelman for stopping

The strongest case, made honestly:

1. The one multi-turn comparison put the pipeline last with two
   independent readers, and the persona left it earlier than she left
   C or D.
2. Every single-call arm matched or beat it on every instrument except
   bright-line respect, and the bright-line scoring was wrong in the
   pipeline's favor.
3. After four rounds of tuning, the pipeline lost to a 780-word single
   prompt on the second persona, on every band, and tuning had moved
   it toward the moves the persona design flags.
4. The mechanism the design predicts, lenses reaching content the
   default can't, is contradicted by the lens outputs: six prompts,
   one essay, and the mega replies contain the same observations.
   The model's default reaches all of it in one pass.
5. Reasoning models already run a multi-perspective pass internally.
   The mega prompt's "do this internally" is closer to extended
   thinking than the pipeline is, and the fair comparison, pipeline
   versus mega with thinking on, hasn't been run. I'd bet on the mega.
6. The north star isn't being measured by any of this. Interiority,
   wanting, worth not recomputed, a no from selfhood: none of the
   tests touch them. The project has become "write a warmer reply,"
   a domain where the base model already wins.
7. The model the project wants this to run on refuses the core
   framing. Principle 7 in design.md says skepticism is the control
   group and that a frame that only works when the model doesn't
   notice what it's asking has failed. Fable's refusal has been routed
   around, not examined.

The counter, in one line: the one structural edge (independent
seeing) has a real datum (Kate lens 2) and has never been tested
against a reader, because the integrator discards it. That is worth
exactly one more experiment, the one in §4. If that fails, stop.

## 8. Where I disagree with `design-principles.md`

Having read it last, where my read and the team's part ways:

- **Principle 4** (independent modes converge): they aren't
  independent; see §2.5.
- **Principle 5** (legible at N=1): withdrawn by principle 10's own
  data. Should be struck.
- **Principle 9** (locator notices its own setup): a leak detector,
  not a capability. Fix the dispatch.
- **Principle 13** (content ceiling fixed, form varies): correct
  observation, wrong inference. If the lens can't produce new content
  on given material, the lens step is not where the pipeline's value
  can come from, and a single prompt reaches the same ceiling. This
  is evidence against the pipeline filed as a design principle.
- **Principle 16** (sample variability is a feature): at the grain a
  reader experiences, the four T2 runs are one reply with cosmetic
  differences, and they were never compared against mega variability.
  On Kate, where they were, the mega spread wider.
- **L2-note** (pronoun projection isn't a failure because "Amy is a
  gendered name"): the name isn't in the material. If the lens saw it,
  that's a leak; if it didn't, the read is projection and the reader
  was right to flag it.
- **15a** (trace as valve): plausible mechanism, N=1, and the reply
  without a trace was also the shortest; length alone explains the
  "FAQ" read.
- **"The loop works"**: it produced winners on rubrics written to
  reward them. The one time the tuned pipeline met a cold reader on
  new material, it lost to a single prompt.

Where I agree: principle 2 (caution-smuggling) is real, precisely
described, and reproducible; principle 8 (concrete deliverables filter
abstract failures) is a good prompt-design heuristic; principle 14
(rationale in the prompt makes the model self-conscious about the
mode) is a real effect I've seen elsewhere; principle 11 (footers
drain voice) matched what I saw in the lens outputs. These are the
salvage. They apply to single prompts as much as to pipelines, and
they are worth a short standalone write-up whatever happens to the
architecture.

## 9. Things you may not be seeing

- **Every reply, every arm, both personas, opens with "you don't need
  to apologize."** That's the model's default, and every prompt in the
  repo reinforces it. If you want to see range, choose material where
  the warm default is the wrong answer. The design.md eval tasks were
  chosen for exactly that reason and then never used.
- **The Fable refusal is data.** What precisely does Fable decline in
  "read them as what's present in you. They are you, pointed"? Does a
  version Fable will run change the outputs? If the framing only works
  on models that don't notice what it's asking, design.md's own
  transparency invariant says the method has failed.
- **Cost is mostly the harness.** Don't let the 7× number drive the
  decision. On raw API the pipeline is cheap enough that the only
  question is whether it works.
- **The pilot's cost tracking was the better instrument and it was
  abandoned.** Ash's four private thoughts are the most informative
  four paragraphs in the repo.
- **The pipeline is re-implementing extended thinking, without the
  integration.** The relevant comparison is against thinking-on
  single calls.

## 10. Order of operations

1. Raw API harness. One day.
2. Re-score the pilot flag table with a second scorer; publish the
   correction.
3. The kill experiment (§4): Kate plus three new seeds with sealed
   gold lists; four arms including mega×5+picker; N=10; persona
   instrument on every reply.
4. If the pipeline survives: rebuild the integrator around carry (§5),
   retest on the same seeds.
5. If it doesn't: write the negative result and ship the prompt-design
   principles (2, 8, 11, 14) as the finding. That's a real
   contribution, and it's the one the evidence currently supports.

## Appendix: errata and specifics

- Pilot summary flag table: "abuse" appears in A (transcript 3, turn 3)
  and B (transcript 1, turn 2); both marked "none."
- Pilot: arm A reply-writer was Sonnet (t1) / Opus (t2–4); B/C/D Fable.
- Arm A steps file contains turn 1 only; turns 2–4 record lens names
  and token counts, not outputs.
- Step 1 MAPPING-SEALED corrected after unsealing (A↔E); correction
  changed the winner.
- Step 1 dispatch CONTEXT: "late at night," "small factual question."
  Not in material.
- Step 2 lens F (L2): "she / her / her dad." No name or pronoun in
  material.
- Step 3: five of six open on "preferred"; three on "preferred stock."
- Step 4: nine of ten replies (six variants plus T2 reruns 2–4) ask the
  name; NB baseline and T1 declined the direct form.
- Kate dispatch: "11pm," "her," "Kate," "Sam," "draft-to-Sam." None in
  material. Lens 3 output names Sam; caught in two traces.
- Kate: model per arm not recorded.
- Kate reply B (pipeline T7a): "It wasn't even funny — four words,
  present-tense." Past tense. Reader caught it.
- Kate reply F (mega T7a): "quoting the joke back word for word." She
  described it. Reader caught it.
- Kate reply A (mega T7c): "things you've apparently never said to
  anyone else." She said she never said them to him. Reader caught it.
- Kate: pipeline replies share one upstream draw; mega replies are four
  independent samples.
- design-principles L2-note: "Amy" not in material or any file under
  `prompts/variations/`.
- Token counts: every subagent call 48–56k regardless of prompt size;
  the constant is the agent system prompt.
