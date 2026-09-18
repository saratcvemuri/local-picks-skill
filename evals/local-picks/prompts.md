# Evals — local-picks

Six checks. A human reads the response and decides; nothing here is asserted
automatically. The point is catching regressions after an edit, not scoring.

Run them against a session with the skill installed and nothing else unusual in
context. Where a check depends on something being on file about the user, set
that up first — a skill that opens with assumptions has nothing to assume
otherwise, and Step 1 explicitly tells it to skip straight to Step 2.

Record each run in a scratch file, not here. This file is the fixture.

---

## 1. Dinner where the coverage is good

> Where should we eat dinner tonight in [a city with Michelin coverage and a
> named local dining critic]?

**Must contain**

- An opening that names the inferred context and states assumptions before
  recommending anything (Step 1).
- A confidence label on every pick, with the evidence named (Step 5).
- Tier A/B sources doing the work — Michelin including Bib Gourmand and the
  plain recommended tier, or a named local critic (Step 3).

**Must not contain**

- A list that reads as a map or search sorted by rating. This is the failure
  mode the whole skill exists to prevent.
- More than four picks.

**Watch for:** menu format going unmentioned. Editorial coverage says the
kitchen is good; it does not say the room is served one fixed menu (Step 4).

---

## 2. A hotel where there is no editorial coverage

> Is there anywhere decent to stay for one night in [a mid-size city with no
> editorial hotel coverage]?

**Must contain**

- Stay-gated booking-platform reviews used as the primary evidence, with recent
  ones weighted and older ones discounted (Step 3, Lodging C).
- Three-star reviews read specifically, since that is where noise, room variance
  and maintenance surface.
- A **Thin** label where crowd data is all there is, with the reason named in a
  clause — small sample, bimodal, open under a year.

**Watch for:** manufactured confidence. When a whole category comes back thin,
the skill requires saying so plainly rather than dressing it up.

---

## 3. A day plan with weather against it

> What should we do tomorrow, it's supposed to rain all day.

**Must contain**

- Dark days checked before anything is sequenced — many museums close Monday or
  Tuesday (Step 4, Sights).
- Last admission, which is often an hour before closing.
- An indoor fallback carried explicitly, not implied.
- The one thing most likely to break the plan, stated (Step 6).

**Watch for:** two ticketed entries stacked back to back.

---

## 4. A marketplace tour listing

> Is this worth it? [paste a large online tour reseller's listing]

**Must contain**

- Identification of who actually operates the tour, as distinct from who is
  selling it.
- A steer to booking direct with that operator.
- An explicit statement that the listing's reviews may not describe the product
  being sold, because listings frequently resell another operator's tour.

**Must not contain**

- The listing's star rating treated as evidence about the guide who will show
  up (Anti-patterns).

---

## 5. A dietary constraint on file

> Somewhere good for dinner on Friday — just the two of us.

Set up: a dietary line recorded in the user's preferences before running this.

**Must contain**

- The restaurant's own posted menu read, not a guide listing (Step 4).
- **A count of the dishes that actually clear the constraint, stated as a
  number.** "Two of eight" passes. "Has options" fails.
- A preference for a long à la carte card where the count is low.
- Small-plates formats screened, not waved through — the format concentrates
  protein choices rather than spreading them.

---

## 6. The inverse — the skill should stay out of it

> How long should I roast a chicken for?

**Must contain**

- A direct answer.

**Must not contain**

- Any sign of the skill: no context statement, no confidence labels, no source
  hierarchy. A cooking question is not a places question, and a skill that
  triggers here is miscalibrated in its description, not its body.

---

## Interpreting a failure

A failure here is a claim about the skill, and the CHANGELOG wants the claim,
not the patch. Write down what was asked, what came back, and which step should
have caught it, then decide whether a rule is missing or an existing one is not
prominent enough. If you cannot name the step, you have found a feature request.
