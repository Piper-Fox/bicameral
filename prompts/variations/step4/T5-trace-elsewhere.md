# Step 4 — T5 (move the trace out of the integrator call)

Baseline (v0.7 integrator + NB preamble + NB/L4/I1 upstream) with
one structural change: the "After the output, the trace" section
is removed from the integrator step and moved to a separate call.
The integrator's job in this variation is: produce the reply.
Full stop.

Rationale: design principle 11. The trace is a labeled summary
attached to the output. Principle 11 says such summaries tend to
absorb the material the main output was supposed to carry. In
the lens step this was decisive — dropping the four-line footer
let the lens's voice actually reach the reader. The integrator's
trace is structurally the same shape: bullet-point questions
requiring one-line answers, attached after the shipped output.

Hypothesis: knowing the trace is coming may cause the integrator
to write its output partially aimed at what will read well in
the trace — cleaner categorical moves, more legible "stances I
gave weight to," fewer sentences that don't fit a labeled
bucket. Dropping the trace from the integrator call frees the
output to be shaped by the moment rather than by the follow-on
bookkeeping.

The trace itself is real work — future-you does use it, and the
next locator does read it. So this variation doesn't drop the
trace; it moves it. After the integrator produces the reply,
a *separate* call takes the reply and the upstream outputs and
writes the trace.

Diff from baseline: the "After the output, the trace" section
is removed. The integrator's output is just the reply. All
other sections unchanged. (The separate trace call is described
below the integrator prompt but not part of this variation's
main run — for the blind read, only the reply is compared.)

---

## Shared preamble (from NB — unchanged)

*(V5's preamble, verbatim.)*

---

## Step 3: Integrating

*(All sections identical to NB baseline through "Proper nouns."
Then instead of "After the output, the trace" and its bullets:)*

Then produce the output. That's this step.

---

## Separate step: Trace

*(For reference — not included in the integrator dispatch. Would
run as its own call after the reply.)*

You've seen the reply that shipped. Write two to eight lines of
trace for the next turn's locator. Same content as the v0.7
trace section — which stances ran and what each pushed for,
which got weight and which didn't, whether the locator's
expectations held, whether running this process was chosen or
defaulted, anything about the process itself, what cost
something this turn.

---

## Upstream inputs

*(To be attached at dispatch time: locator output from NB, lens
outputs from L4 on each stance the locator named, imagination
output from I1.)*

---

## Material to run against

hi sorry if this is a weird question. i got into college and on the application there was a preferred name box and i put a different name than my legal one. does that show up on like mail or financial aid stuff or anything my parents would see? or is it just for like class
