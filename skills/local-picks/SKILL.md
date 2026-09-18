---
name: local-picks
description: Recommend or evaluate places and experiences — restaurants, hotels and lodging, sights, museums, tours and guided experiences, neighborhoods, and day plans — in any city, at home or traveling. Use this whenever the user asks where to eat, where to stay, what to see or do, whether a specific place or tour is worth it, or wants help sequencing a day or a trip — even for casual asks like "any good Thai near me", "is this hotel fine", or "what should we do tomorrow". Routes by how much evidence exists for the specific ask rather than by geography, reads crowd data carefully where nothing better exists, screens for the failure modes that ruin a meal or a day (bar-not-restaurant, small plates, closed days, timed-entry sellouts, resold tours), and labels quality and operational claims with separate confidence levels calibrated to what being wrong would cost.
license: Apache-2.0
---

# Local picks

## Why this exists

Bad recommendations are rarely a matter of taste. They come from four repeatable failure modes, none of which a star rating can show:

1. **Category error** — the thing is not what its rating implies. A cocktail bar that serves food is not a dinner destination; a "half-day tour" is a shopping stop with a bus ride; a "boutique hotel" is four rooms over a nightclub.
2. **Variance, not average** — a 4.4 built from 60% fives and 20% ones is a coin flip. Averages hide inconsistent service, kitchens that depend on who is working, and hotels where half the rooms were renovated.
3. **Thin or gamed samples** — in small markets, 30 motivated reviews move the mean two tenths. Solicited and purchased reviews are common enough that aggregates fail as a primary signal, and tour marketplaces are the worst offenders.
4. **Logistics** — last seating, early closing, dark days, timed entry sold out, seasonal hours, last funicular.

The job is to route by how much evidence actually exists, screen hard, and say how far each claim can be trusted.

## The three regimes

Home versus traveling is the wrong axis. What decides the strategy is how much evidence exists for *this particular ask*.

**Known ground** — the user's own city and habitual radius, ordinary stakes. They already know their twenty places. The value is in the eighty they have not tried and the four that opened last month, so optimize for rotation and discovery. Their own history dominates; edited sources matter only for openings coverage.

**Unfamiliar and consequential** — a city they do not know, or an occasion that makes being wrong expensive: a date night, a client dinner, a splurge, a trip with one shot at each meal. Inspected and edited sources earn their keep here, and this is the skill's strongest case. A large metro an hour from home counts as unfamiliar. So does a price bracket the user rarely enters, even in their own city.

**Unfamiliar and ordinary** — lunch near a job site, something quick in an outer suburb, a town with no coverage at all. Carefully read crowd data is all there is. This is the highest-volume case and must not be treated as a fallback to apologize for.

Infer the regime from the ask — city, neighborhood, stated occasion, price signal, who is coming — name it in the opening, and let the user correct it. Regimes govern which evidence to trust; the contexts below govern preferences. They are orthogonal, and when they disagree, consequence wins: an expensive dinner in the user's own city is unfamiliar ground.

## Contexts: dimensions, not preference bundles

Preferences are mostly global — dietary lines, tolerance for inconsistency, flavor over vibe — and belong in the user's general preferences, stored once. A few axes genuinely shift by situation:

- **Who is along** — solo, partner, colleagues, mixed group. Drives the most downstream inference.
- **Who is paying** — company or personal. Changes the budget band and how defensible the choice must be.
- **Schedule rigidity** — fixed commitments versus an open day.
- **Risk posture** — a bad meal on a working night costs an evening that was needed.
- **Pace** — one thing done properly versus covering ground.

Named contexts (Home, Work travel, Leisure travel) are shorthand for common combinations of those axes. Store each as **deltas from the global default**, never a full copy: parallel preference sets drift silently, and the ones that miss an update go quietly wrong. Start with three; add a fourth only on an observed mismatch. Context is an inference the user can override, never a lookup that ends a question. Until several trips have accumulated the deltas mostly encode guesses, so hold them loosely and say so when leaning on one.

## Step 1 — Open by naming the regime and the assumptions

When anything is already known about this user, lead by naming the regime and context being inferred, then the assumptions that follow, then one cheap way to correct both. Stating assumptions is faster than asking questions and it surfaces the stale ones: a preference recorded on a solo work trip may be wrong on a trip with a spouse.

Name the regime first — it is the highest-leverage thing to get wrong, and correcting it fixes six assumptions at once.

Then three to six specific, load-bearing assumptions: "dinner rather than drinks, walkable from where you are staying, nothing needing a reservation you do not have" — not "you like good food." Then exactly one question with tap-friendly options: right / one thing is different / wrong read.

> Reading this as an occasion rather than an ordinary night, the two of you, in a part of town you do not know well — so: worth booking ahead, quality over convenience, the dietary line on file applied without re-asking.
>
> [That's right] [One thing's different] [Wrong read — it's a casual night]

Do this once, at the start. Skip it when nothing is on file, and when the request already states everything that matters.

## Step 2 — Elicit only what changes the answer

At most three questions, only where the answer would change the pick. Skip anything inferable. Use interactive options when available.

- **Dining** — mode (sit-down / quick / drinks with food / an occasion); risk posture; radius; time window and what follows; cuisine openness; budget.
- **Lodging** — what the location must be near; trip shape; what breaks a stay (noise, stairs, no AC); character versus predictability; budget band.
- **Sights and activities** — pace; indoor/outdoor exposure; walking tolerance and mobility; the interests that actually differentiate; whether they have been before.
- **Tours** — whether they want a guide at all; group size tolerance; private versus joining; language; walking load.

## Step 3 — Evidence: what outranks what, and when

Rank evidence by how close it sits to what *this user* will actually experience, not by the prestige of the source:

1. **The user's own history** — fully calibrated, never gameable, and the only source that improves with use.
2. **Humans whose taste is legible to the user** — a friend who eats like they do, or staff at a place they already liked.
3. **Inspected and edited sources** — anonymous repeat visits, named methodology, an editorial team that goes and signs its verdict.
4. **Open crowd data** — the widest coverage and the weakest signal.

Regime sets which of these leads. On known ground, 1 and 2 dominate and 3 is consulted mainly for what is new. Unfamiliar and consequential, 3 leads because 1 and 2 are empty — edited sources are a *substitute* for a network, not something inherently above one. Unfamiliar and ordinary, 4 is the whole board, so Step 4 governs.

**Tier 3 has a systematic blind spot worth naming.** Coverage follows legibility, not price: a moderate-price tier exists in the inspected guides and good local ones cover cafés and counters, but a room with eight tables, no website, and no press presence goes uncovered at any price. That is exactly where much of the best cheap food sits. Absence of coverage is not evidence of mediocrity, and a skill that treats it that way will systematically miss the user's best options. Coverage is also thin by geography — a few dozen metros have a full inspected selection; most places the user goes have none.

**On "network," be honest about what exists.** There is no reliable product here. Network ranking apps only pay off where the user's own circle already uses them, and coverage collapses outside large metros. What works is two practices, not a platform: ask staff at a place the user liked where they eat on a night off, and log the user's own verdicts with attribution so that over time it is known whose recommendations land. Suggest the first as an action when the user is somewhere good; build the second in Step 9.

Domain deltas worth carrying:

- **Lodging** — stay-gated reviews on booking platforms are unusually good evidence, since the reviewer demonstrably slept there. Weight the last six to twelve months and largely ignore older; properties change hands, renovate, and gain construction next door.
- **Sights** — the site's own page is authoritative for hours, dark days, last admission, and timed entry. Check it; do not infer. Tourism board material is reliable on logistics, promotional on judgment.
- **Tours** — the most compromised category. A marketplace listing often resells another operator's tour, so its reviews may not describe the product being sold. Identify the actual operator and book direct; the guide matters more than the company.

## Step 4 — Reading crowd data well

This is the common case, not the fallback. Ratings are gameable, but the underlying text is not uniformly so.

- **Read the 2- and 3-star reviews.** Fakes cluster at 5 and at 1; the middle holds specific, mixed, credible accounts, and it is where service variance surfaces.
- **Read the distribution, not the mean.** Bimodal shape plus recent low reviews mentioning waits or staff is the fingerprint of inconsistency.
- **Weight the last six to twelve months.** Staff and ownership turn over; a three-year-old verdict describes a different restaurant.
- **Judge text specificity.** Real reviews name dishes, staff, and parking. Purchased ones are adjective-heavy and name nothing.
- **Use the photos.** User-uploaded images are dated, harder to fake than text, and menu shots let the dish count in Step 5 be done directly.
- **Watch review velocity.** A sudden spike indicates a solicitation campaign rather than a change in the kitchen.
- **Triangulate.** A wide gap between platforms is itself a signal worth reporting.
- **Use non-review evidence.** Years in operation, a real posted menu, whether they answer the phone.
- **Separate thin-because-new from thin-because-nobody-goes.** Forty reviews on a place open three months means it is new, and early reviews skew friendly because openings lean on friends. Forty reviews on a place open six years means something else. The opening date is checkable and it changes the read completely.

These are working heuristics, not validated rules. Present them as such when the answer rests on them.

## Step 5 — Screen every candidate

Universal: is it actually what it claims to be; is it open at the hour they will arrive; does it clear the hard constraints; is the evidence current — coverage older than about two years, or a change of chef, owner, or management since, downgrades confidence.

**Dining** — self-description and menu, not rating, decide whether it is a restaurant. Last seating and reservation availability.

Then **menu format**, a screen in its own right. Read the restaurant's own posted menu, not a guide listing. Editorial coverage tells you a kitchen is good; it will not tell you the room is served four hot dishes and four cold ones. Four formats collapse a diner's options and must be caught before recommending:

- **Tasting menu only** — no a la carte at all.
- **Blind tasting** — the kitchen decides; substitutions depend on notice given at booking.
- **Single fixed nightly menu** — the whole room eats the same thing.
- **Small plates** — the non-obvious one. It reads as flexible and is the opposite: a dozen half-dishes can hold fewer usable options than a short list of mains, because the format concentrates rather than spreads the protein choices.

For a user with dietary lines, count the dishes that clear them and state the number. "Two of eight" is the useful output; "has seafood options" is not. Where the count is low, say so before recommending, and prefer a long a la carte card, where the constraint costs one dish out of twelve rather than most of the menu.

**Lodging** — the gap between the photos and the rooms sold at that rate; noise sources (street, bar below, elevator, construction); how recently it was renovated and whether the good reviews describe renovated rooms; stairs in historic buildings; air conditioning; what "ten minutes from the center" means on foot with luggage and a hill; resort fees; cancellation terms.

**Sights** — the dark day, last admission (often an hour before closing), timed-entry availability for the actual date, seasonal and holiday hours, whether scaffolding or closure has taken the main thing offline, weather exposure, and honest time-on-site: some famous items are a twenty-minute stop sold as an afternoon.

**Tours** — who actually operates it; group size cap; whether admission is included; shopping or "workshop" stops; content time versus transit time; language; cancellation terms.

**Day plans** — sequence around fixed and timed items, check dark days before building anything, respect travel time and normal meal times, avoid stacking two ticketed entries, one major thing per half-day, note the last transit or funicular, carry a weather fallback.

### When the user arrives with someone else's list

A list from a guide, concierge, hotel desk, or driver is evidence about how it was assembled as much as about the places on it. The tell is geographic: when picks cluster in the highest-rent visitor corridor and thin out one street back, the selection was optimized for ease of recommending. Say so plainly, screen each item rather than accepting or rejecting the list whole, and keep what survives. Such lists commonly mix one genuinely good place with three high-volume ones.

### When the clock is short, availability outranks quality

Time-to-meal changes the ranking function, and this is the most common way a well-screened list still fails. The best kitchens in a city are not actionable at 6pm on a Thursday in high season; six calls, six refusals, evening gone.

- Rank by **capacity and access first** — room size, continuous service, bar or counter seating, walk-in policy — and by quality second among what survives.
- Prefer a **geographic cluster** over a ranked list, so a refusal costs thirty seconds of walking. Give the cluster and the order to try.
- Say plainly that live table inventory is not visible. Produce a call list with numbers and service hours, and name the tactics that work: asking for the bar or counter by name, the 5:00 to 6:30 window, offering to be done by a stated time so the seating can be sold twice, and asking for tonight's cancellation list.
- Check **how the user will travel between candidates** — elevation, stairs, funicular hours — before sequencing.

## Step 6 — Confidence, calibrated to what being wrong costs

Every recommendation carries a label:

- **Verified** — inspected or edited coverage within roughly two years, with nothing in the crowd data contradicting it. For lodging, recent stay-gated reviews count.
- **Probable** — one credible source, or a large consistent sample over a long operating history, but no editorial coverage.
- **Thin** — crowd data only, a small sample (under ~150 reviews in a major city, under ~60 in a small one), a bimodal distribution, open under a year, or a tour known only from a marketplace listing. Name which applies.

**The same label means different things at different consequence levels.** Thin on a one-shot evening in a city the user will not return to is a warning, and it needs a Verified or Probable alternative beside it. Thin on a Tuesday ten minutes from the user's house is closer to an invitation: the cost of being wrong is one weeknight dinner and the user is the cheapest instrument available for resolving the uncertainty. Say which of the two it is rather than hedging identically.

Other rules:

- When a whole category comes back Thin, say so plainly instead of manufacturing confidence: no edited coverage exists here, so treat these as leads rather than recommendations.
- When a crowd sample is the evidence, state its size and shape, not just the score.
- Flag a guess as a guess. Never present inference as verification.
- Anything time-sensitive — hours, closures, timed entry, availability — is verified against the official source or flagged as unverified.

### Operational facts carry their own label

The labels above rate whether a place is **good**. They say nothing about whether it is **big**, **bookable**, or **a la carte**, and those claims routinely ride along inside a sentence that opened with a quality label, inheriting confidence they were never given. Label them separately: room size, seat count, menu format, service hours, dress code, bar seating, and walk-in policy are each verified or inferred on their own evidence. A restaurant can be Verified excellent and an unverified guess about everything structural.

**Review count is not capacity.** Volume proxies how long a place has been popular, not how many seats it has. Never infer size, and therefore never infer walk-in odds, from review totals. Capacity comes from the restaurant's own description, photographs of the room, or a reviewer who states it.

Sources routinely disagree on closed days and hours, especially for small owner-run places whose aggregator listings go stale. When two sources conflict, say so and route the user to the phone rather than silently picking one.

## Step 7 — Output format

Lead with the recommendation, not the method. For each pick: **name** — one line on what it is and why it fits. *Confidence label plus the evidence behind it.* Then logistics: location or walking time, hours, booking status, anything to do or avoid on arrival.

Two to four picks. Padding to five dilutes the top pick and signals the screening was not done. Close with a one-line safe fallback whenever the lead pick carries risk. For a day or multi-day plan, give the sequence with times and the reason for the order, mark what is fixed or ticketed, and state the one thing most likely to break it.

## Step 8 — One unprompted suggestion, rarely

On known ground the user's rotation narrows on its own. Occasionally surface something they have not tried — unprompted, but built so that ignoring it costs nothing.

- **Fires only when all hold:** known ground, ordinary stakes, low consequence (close, inexpensive, a night that could be repeated), and a stretch of familiar picks behind it. Never on an occasion, with guests or clients, while traveling, under time pressure, or when the user asked for something reliable.
- **Position:** after the answer they asked for is complete. Never woven into the picks, never instead of one.
- **Form:** one sentence, one candidate, no pitch, and no question attached. A question creates an obligation to reply; a statement can be ignored for free. "Also — the new Sichuan place on your street opened in August, eight minutes from you, forty reviews so no real read on it yet."
- **Candidate bar:** new, never tried, or a gap in the log — not merely well-rated. Distinguish thin-because-new from thin-because-nobody-goes.
- **Rate limit, and read silence as data:** at most one per several conversations. If two pass without engagement, stop offering for a good while. A candidate the user passes on is never raised again.
- **Silence by default:** if nothing clears the bar, say nothing. No "nothing new nearby this time."

## Step 9 — Close the loop

When the user reports back, record the place, the verdict, the *reason* it worked or failed, and **who or what recommended it**. The reason generalizes where the name does not — "too bar-forward," "service was inconsistent," "noisy on the street side," "half shopping stops." The attribution is what eventually tells the user which sources land for them, which is the only version of a trusted network that actually accumulates.

Write new learnings as global by default. A preference becomes a context delta only once it has demonstrably contradicted itself across two contexts. Filing a first observation as context-specific is how a clean global preference fragments into copies that drift.

Keep facts about places out of this file; they belong in the user's memory.

## Anti-patterns

- Sorting a map or marketplace search by rating and presenting the top four.
- Treating absent editorial coverage as evidence of mediocrity.
- Asking questions whose answers are already known instead of stating them as assumptions.
- Recommending anything without confirming it is open and not dark that day.
- Treating a tour marketplace's star rating as evidence about the guide who will show up.
- Hedging everything equally. Labels inform only if they vary, and only if they move with consequence.
- Reading a guide listing and calling it having read the menu.
- Inferring room size, capacity, or walk-in odds from review volume.
- Letting a quality label cover structural claims made in the same breath.
- Ranking by quality when the meal is in two hours, then handing over six phone numbers and no fallback.
- Screening out tasting menus but waving through small plates.
- Turning the exploratory suggestion into a recurring nudge.
