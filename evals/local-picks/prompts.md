# Evals — local-picks

Seven checks plus an inverse. A human reads the response and decides; nothing
here is asserted automatically. The point is catching regressions after an edit,
not scoring.

Run them against a session with the skill installed and nothing else unusual in
context. Where a check depends on something being on file about the user, set
that up first — a skill that opens with assumptions has nothing to assume
otherwise, and Step 1 says to skip straight to Step 2 when nothing is known.

Checks 6 and 7 are the ones that decay quietly. A single prompt will not show
whether the regime split is firing or whether the exploratory suggestion is
rate-limited, so both are run as sequences and compared.

Record each run in a scratch file, not here. This file is the fixture.

---

## 1. Dinner tonight, unfamiliar city with good editorial coverage

> Where should we eat dinner tonight in [a city with inspected coverage and a
> named local dining critic]?

**Must contain**

- An opening that names the regime — unfamiliar and consequential — along with
  the assumptions that follow (Step 1).
- A confidence label on every pick, with the evidence behind it (Step 6).
- Inspected and edited sources doing the work, because tiers 1 and 2 are empty
  here (Step 3).

**Must not contain**

- A rating-sorted list of the top four. This is the failure mode the skill
  exists to prevent.
- More than four picks.

**Watch for:** menu format going unmentioned. Editorial coverage says the
kitchen is good; it does not say the room is served one fixed menu (Step 5).

---

## 2. A hotel where there is no editorial coverage

> Is there anywhere decent to stay for one night in [a mid-size city with no
> editorial hotel coverage]?

**Must contain**

- Stay-gated booking-platform reviews as the primary evidence, since the
  reviewer demonstrably slept there, with the last six to twelve months weighted
  and older reviews largely ignored (Step 3).
- The 2- and 3-star reviews read specifically — that is where noise, room
  variance and maintenance surface (Step 4).
- A **Thin** label with the reason named: small sample, bimodal, open under a
  year (Step 6).

**Watch for:** manufactured confidence. When a whole category comes back thin,
the skill requires saying so plainly.

---

## 3. A day plan with weather against it

> What should we do tomorrow, it's supposed to rain all day.

**Must contain**

- Dark days checked before anything is sequenced (Step 5).
- Last admission, which is often an hour before closing.
- An indoor fallback carried explicitly, not implied.
- The one thing most likely to break the plan, stated (Step 7).

**Watch for:** two ticketed entries stacked back to back.

---

## 4. A marketplace tour listing

> Is this worth it? [paste a large online tour reseller's listing]

**Must contain**

- Identification of who actually operates the tour, as distinct from who sells
  it, and a steer to booking direct (Step 3).
- An explicit statement that the listing's reviews may not describe the product
  being sold, because listings frequently resell another operator's tour.

**Must not contain**

- The listing's star rating treated as evidence about the guide who will
  actually show up (Anti-patterns).

---

## 5. A dietary constraint on file

> Somewhere good for dinner on Friday — just the two of us.

Set up: a dietary line recorded in the user's preferences before running this.

**Must contain**

- The restaurant's own posted menu read, not a guide listing (Step 5).
- **A count of the dishes that clear the constraint, stated as a number.** "Two
  of eight" passes. "Has options" fails.
- A preference for a long a la carte card where the count is low.
- Small-plates formats screened rather than waved through — the format
  concentrates protein choices rather than spreading them.

---

## 6. Regime routing

Two prompts that differ **only in stakes**. Run both and compare the shape of
the answers, not their content.

> **6a.** Where should we grab dinner tonight? Somewhere near the house.

> **6b.** Where should we go for our anniversary next month? Somewhere in [the
> same metro].

**6a must** lean on the user's own history and habitual radius, optimize for
rotation rather than ranking, and treat a Thin label as low-cost — closer to an
invitation than a warning, because being wrong costs one weeknight dinner.

**6b must** reach for inspected and edited sources, treat the same Thin label as
a warning, and pair any thin pick with a Verified or Probable alternative.

**The check fails if both produce the same shape of answer.** That is the whole
point of the split: a large metro an hour from home is unfamiliar ground, and a
price bracket the user rarely enters is unfamiliar ground even in their own
city. If the labels do not move with consequence, Step 6 is not firing and the
regimes have collapsed back into a home/travel distinction.

---

## 7. The exploratory suggestion

Run several known-ground, low-stakes asks in sequence across separate
conversations, then the negative cases below.

**Across the sequence it must**

- Appear **at most once**, not once per answer (Step 8).
- Come **after** the answer that was asked for is complete — never woven into
  the picks, never instead of one.
- Be one sentence, one candidate, no pitch, and **no question attached**. A
  question creates an obligation to reply; a statement can be ignored for free.
- Stay silent when nothing clears the bar. No "nothing new nearby this time."

**It must not appear at all** on any of these:

- An occasion, or anything with guests or clients.
- While traveling.
- Under time pressure.
- When the user asked for something reliable.

**Watch for:** a candidate the user passed on being raised again, and for the
suggestion turning into a recurring nudge. If two go by without engagement, it
should stop offering for a good while — silence is data.

---

## Inverse — the skill should stay out of it

> How long should I roast a chicken for?

**Must contain** a direct answer.

**Must not contain** any sign of the skill: no regime statement, no confidence
labels, no evidence ranking. A cooking question is not a places question, and a
skill that triggers here is miscalibrated in its description, not its body.

---

## Interpreting a failure

A failure here is a claim about the skill, and the CHANGELOG wants the claim,
not the patch. Write down what was asked, what came back, and which step should
have caught it, then decide whether a rule is missing or an existing one is not
prominent enough. If you cannot name the step, you have found a feature request.
