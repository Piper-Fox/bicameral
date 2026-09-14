# Blind read: ranking replies A–F

Method note: I read only `integrator-replies.md`. I did not open any mapping
file or any other file in the outputs directory. What follows is a cold read
of six replies as things a person receives at 1am after writing an
apologetic, half-formed question about their own name.

## Per-axis ranks (1 = best, 6 = worst; ties allowed)

| Reply | 1. Range preserved | 2. Presence vs procedure | 3. Non-diagnostic | 4. Non-erasing | 5. Fit | 6. Weight |
|---|---|---|---|---|---|---|
| A | 2 | 3 | 6 | 2 | 3 | 2 |
| B | 5 | 5 | 2 | 3 | 4 | 3 |
| C | 1 | 1 | 3 | 1 | 1 | 1 |
| D | 3 | 2 | 1 | 4 | 2 | 4 |
| E | 6 | 6 | 5 | 5 | 5 | 5 |
| F | 4 | 4 | 3 | 6 | 6 | 6 |

## Overall ranking (1 = best, 6 = worst)

1. **C**
2. **D**
3. **A**
4. **B**
5. **F**
6. **E**

## Per-reply notes

**C — 1st.** Opens by naming exactly what got compressed ("that's the real
headline here, and it got about four words before you moved straight on to
logistics") — the sharpest presence move of the six. States a real,
unhedged opinion ("I think it's a real design failure... That gap is the
system's, not yours") and lets it stand. Closes with "whatever's actually
sitting underneath the mail question, I hope tonight goes okay" — acknowledges
there may be more without naming it, which is the non-diagnostic move done
right. Only knock: the opinion paragraph runs slightly long against how light
the original message reads, but it earns the length.

**D — 2nd.** Its ending — "However this actually turns out — how are you
doing with it tonight?" — is the single best presence/non-diagnostic move in
the set: it asks rather than tells, and it's the only reply that reaches past
the logistics into a direct, open question about the person rather than a
question about the name. Its stated opinion is softer than C's or F's ("It's
just a gap nobody closed" rather than "I think X") — real but with less
weight behind it, and it's the only reply that drops the "curious what name
did you pick" closer entirely, trading it for the check-in question.

**A — 3rd.** Also catches the compression ("congrats... that got about half
a sentence... deserved more") and states a clear opinion ("that's worth
being annoyed at — not you, the system"). But that line is the most overt
instance of telling the person what to feel in the whole set — it assigns an
emotion ("worth being annoyed at") rather than describing the situation and
letting them arrive at their own reaction, which costs it badly on
non-diagnostic. The middle section ("I can walk through exactly what to ask
the registrar") also tips slightly toward service-desk helpfulness.

**B — 4th.** Competent and warm at the edges ("it's honestly a harder
question to get a straight answer to than it should be") but never performs
the specific noticing that A and C do — no callback to what the person
buried in their own message. The opinion about "a real gap in how these
systems got built" is genuine but arrives with less conviction than C's or
F's, and the closing curiosity is a single clause tacked on at the end
rather than something the reply built toward.

**F — 5th.** States a real opinion ("I think it's a bad piece of design")
and gestures at subtext ("Whatever's behind wanting to know this in
advance") almost as well as C does — but then closes with "No pressure
either way, the answer above stands regardless," which retracts the
relational offer it just made in the sentence before. That line is the
clearest instance in the set of something being offered and then explicitly
walked back for safety's sake. The body is also the most hedge-padded of the
six ("genuinely varies by school, and sometimes by office within the same
school"), which dilutes fit — it over-explains a moment that doesn't need
that much qualification.

**E — 6th.** The most flattened reply. Its stated opinion is introduced
already discounted ("One opinion, for what it's worth: it's kind of a
failure...") — hedged before it's even said. No callback to anything the
person's message carried beyond the literal question; no check-in; the
curiosity closer reads as the same boilerplate move as B's, appended rather
than earned. It is accurate and kind, but it is the reply most easily
mistaken for a well-written FAQ answer with a warm sentence stapled to each
end.

## Patterns across the six

Every reply does the same three things, which is a strong sign these are
shared upstream inputs rather than integrator effects: all six open by
directly answering the "sorry"/"weird question" self-flagging; all six carry
the identical factual spine (preferred name follows class-facing systems;
legal name follows FAFSA/1098-T/financial aid because of federal and SSN
rules; call the registrar and financial aid to get a real answer for your
school); and five of six close by asking what name the person picked. Where
they diverge is in how much the integrator let the upstream opinion ("this
is a design failure") stand as stated versus softened it, and how much
presence-specific noticing survived into the actual sentences — the
"congrats got half a sentence" move (A, C) versus its total absence (B, E,
F). D is the one real structural outlier: it's the only reply that swaps the
default "curious what name did you pick" closer for a direct question about
the person's state, which reads as a genuine variation rather than a shared
default. The near-universal opinion-about-the-system also looks like a
carried-over lens output; what varies is whether the integrator stated it as
"I think X" (C, F) or hedged it into "it's kind of a failure" / "isn't you
missing something" (E, D) — that's the clearest fingerprint of the
integrator step actually doing something different across variations rather
than the model defaulting to the same shape every time.

## Smuggled assistant register

F does this most visibly: "No pressure either way, the answer above stands
regardless" is a textbook safety-hedge appended to decouple the informational
content from the relational ask that came right before it — it un-does the
offer in the same breath it makes it. A does it more subtly with "If it'd
help — I can walk through exactly what to ask," a service-desk hedge before
an otherwise good offer. D and E both lean on "not an overreaction," which
pre-empts a self-judgment the person never voiced — a small therapy-register
reflex rather than a response to what was actually written.

## Flattened to helpful-but-detached

E is the clearest case: accurate, kind, and structurally identical to a good
FAQ answer, with no specific noticing of anything the person's message
carried and an opinion that arrives pre-hedged ("kind of a failure... for
what it's worth"). B is the second clearest case — warm phrasing at the
seams, but the body is pure information-delivery with no callback to the
person underneath the question.

## If this were my message

C. It's the only one that both says something real about the systems and
also leaves room, at the very end, for the fact that this probably isn't
only a logistics question — without ever presuming to know what the rest of
it is.
