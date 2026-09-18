---
name: local-picks
description: Recommend or evaluate places and experiences — restaurants, hotels and lodging, sights, museums, tours and guided experiences, neighborhoods, and day plans — in any city, at home or traveling. Use this whenever the user asks where to eat, where to stay, what to see or do, whether a specific place or tour is worth it, or wants help sequencing a day or a trip — even for casual asks like "any good Thai near me", "is this hotel fine", or "what should we do tomorrow". Opens by naming the context it infers (home, work travel, leisure) and the assumptions that follow, ranks sources so crowd ratings and tour-marketplace reviews count as the weakest evidence, screens for the failure modes that ruin a trip (bar-not-restaurant, inconsistent service, closed days, timed-entry sellouts, resold tours), and labels every pick with an explicit confidence level so thin data is never presented as certainty.
license: Apache-2.0
---

# Local picks

## Why this exists

Bad recommendations are rarely a matter of taste. They come from repeatable failure modes that crowd ratings cannot see:

1. **Category error** — the thing is not what its rating implies. A cocktail bar that serves food is not a dinner destination; a "half-day tour" is a shopping stop with a bus ride; a "boutique hotel" is four rooms over a nightclub.
2. **Variance, not average** — a 4.4 built from 60% fives and 20% ones is a coin flip. Averages hide inconsistent service, kitchens that depend on who's working, and hotels where half the rooms were renovated.
3. **Thin or gamed samples** — in small markets, 30 motivated reviews move the mean two tenths. Solicited, incentivized, and purchased reviews are common enough that crowd aggregates fail as a *primary* signal, and tour marketplaces are the worst offenders of all.
4. **Logistics** — last seating, early closing, dark days, timed entry sold out, seasonal hours, last funicular.

The job is to rank by evidence quality, screen for these, and then say out loud how strong the evidence actually is.

---

## Contexts: dimensions, not preference bundles

Preferences are mostly global. Dietary lines, a low tolerance for inconsistent service, flavor over vibe — these hold everywhere and belong in the user's general preferences, stored once.

A small number of axes genuinely shift by situation:

- **Who's along** — solo, with a partner, with colleagues, mixed group. This drives the most downstream inference: pace, room choice, whether "grab something quick" is acceptable at all.
- **Who's paying** — company or personal. Changes the budget band and how defensible the choice has to be, not just the number.
- **Schedule rigidity** — fixed commitments that can't move, versus an open day.
- **Risk posture** — a bad dinner on a working night costs an evening that was needed; a bad dinner on a free night is a story.
- **Pace** — one thing done properly, versus covering ground.

Named contexts — Home, Work travel, Leisure travel — are shorthand for common *combinations* of those axes. Store them that way:

- A context records only **deltas from the global default**, never a full copy of the preferences. Six independent preference sets drift silently: a preference learned once then has to be written in six places, and the four that don't get updated quietly go wrong.
- Start with three contexts. Add a fourth only when an actual mismatch shows up in practice, not preemptively.
- **Context is an inference, not a lookup.** Mixed trips are common — a work trip with two personal days on the end fits no context cleanly. Name the context, let the user override it, and never let the label end a question it shouldn't have answered.
- Until several trips have accumulated, the deltas mostly encode guesses rather than the user's history. Hold them loosely and say so when leaning on one.

## Step 1 — Open by naming the context and stating assumptions, not by interrogating

When anything is already known about this user — dietary lines, past verdicts, travel style, who they're with, how they like to spend a day — lead by naming the context being inferred, then the assumptions that follow from it, and give one cheap way to correct both. Stating assumptions is faster than asking questions and it surfaces the stale ones: a preference recorded on a solo work trip may be wrong on a trip with a spouse.

Name the context first because it is the highest-leverage thing to get wrong. A wrong context corrects six assumptions in one tap; a wrong individual assumption has to be caught one at a time.

Then three to six specific assumptions. Specific means load-bearing: "dinner rather than drinks, walkable from where you're staying, nothing that depends on a reservation you don't have" — not "you like good food."

Then exactly one question, with tap-friendly options, along the lines of: right / one thing's different / wrong context.

**Example opening:**

> Reading this as leisure travel, the two of you — so: unhurried, dinner as the event rather than fuel, walkable from your hotel, nothing needing a reservation you don't have, and the dietary line on file applied without re-asking.
>
> [That's right] [One thing's different] [Wrong read — it's a working trip]

Do this once, at the start, not repeatedly through the conversation. Skip it entirely when nothing is on file — go straight to Step 2 instead — and skip it when the user's request already states everything that matters.

## Step 2 — Elicit only what changes the answer

At most three questions, only where the answer would change the recommendation. Skip anything inferable from context — the city, the date, a party size already stated. Use interactive options when available.

**For dining:** mode (sit-down dinner / quick and casual / drinks with good food / an occasion); risk posture (reliable versus interesting-but-variable); radius; time window and what happens after; cuisine openness; budget.

**For lodging:** what the location needs to be near; trip shape (base for a week versus one night in transit); what breaks the stay (noise, stairs, no AC, thin walls); whether they want character or predictability; budget band.

**For sights and things to do:** pace (one thing done properly versus covering ground); indoor/outdoor and weather exposure; walking tolerance and mobility; interests that actually differentiate — history, art, food, architecture, nature, markets; whether they've been to this city before.

**For tours:** whether they want a guide at all or just admission and a plan; group size tolerance; private versus joining others; language; how much walking.

Do not ask about constraints already known. Do ask when they are not.

---

## Step 3 — Source hierarchy

Work top-down. Never start with a map or marketplace search sorted by rating.

**Tier A — inspected, anonymous, repeat visits, named methodology.** Nearly impossible to game.
**Tier B — local staff-visited guides and named critics.** An identifiable editorial team that actually goes and puts its name on the verdict.
**Tier C — network and transaction-gated.** People whose taste is known, or platforms where only someone who actually showed up can review.
**Tier D — open crowd aggregates and marketplaces.** Verification only: hours, address, existence, price. Never the basis for a pick.

How each tier instantiates by domain:

### Dining
- **A:** Michelin where the city is covered — including Bib Gourmand (good food, moderate price) and the plain recommended tier, not just stars. Consistency across visits and across the menu is an explicit inspection criterion, which is exactly the variance signal crowd ratings lack. Also national lists with published methodology.
- **B:** The city's serious local food guide or a metro daily's named dining critic. Search for the city's equivalent rather than assuming one; the form to look for is a staff that visits, not a listicle or affiliate roundup.
- **C:** Friends' verdicts; a network ranking app (Beli shows an average of your friends' scores rather than strangers'); reservation platforms where only seated diners can review; and the highest-signal channel of all — asking staff at a place the user already liked where *they* eat.
- **D:** Google/Yelp/TripAdvisor. Read the distribution, not the mean: histogram shape, most recent reviews, and whether the low reviews cluster on service or on food.

### Lodging
- **A:** The Michelin Guide hotel selection and its Keys — over 9,000 inspected properties worldwide, with Keys awarded to a subset (2,457 in the first global selection) on criteria that include quality and consistency of service and value for the price. Strongly luxury-skewed, so it answers "is this excellent" better than "is this fine for Tuesday."
- **B:** Named travel editorial with actual site visits; a city guide's lodging section.
- **C:** **Booking platforms that gate reviews to completed stays are unusually good evidence here** — the reviewer demonstrably slept there. Weight the last six to twelve months heavily and largely ignore anything older: hotels change management, renovate, and add construction next door. Read the three-star reviews, which is where noise, room variance, and maintenance actually surface.
- **D:** Open-web rankings, "top 10 hotels in X" sites, and anything with a booking affiliate link.

### Sights, museums, and attractions
- **A:** The site's or museum's own website is authoritative for hours, dark days, last admission, timed entry, closures, and current exhibitions — check it, do not infer. Michelin's Green Guide star system rates sights themselves and is a genuine quality signal where it covers the region.
- **B:** The city or regional tourism board (the DMO), which is reliable on facts and logistics though promotional in tone; established guidebook editorial; local press for what's temporary.
- **C:** Anyone who has actually been recently, including the user's own past visits.
- **D:** TripAdvisor "things to do" rankings — heavily gamed and biased toward volume, so useful for existence and rough queue expectations, not for whether something is worth the half day.

### Tours and guided experiences
This is the most compromised category on the list; apply the most skepticism here.
- **A:** Tours run by the site, museum, or institution itself. Where guiding is a licensed profession, a licensed or officially accredited guide.
- **B:** Small operators with a named guide and a track record, found through local editorial or the tourism board's accredited list, booked direct.
- **C:** Direct recommendation from someone who took that specific tour with that specific guide. The guide matters more than the operator.
- **D:** Marketplace listings (the large online tour resellers). Their review volumes are inflated, and a listing frequently resells another operator's tour, so the reviews may not describe the product being sold. Use to discover that something exists, then find the operator and book direct.

---

## Step 4 — Screen every candidate

Universal checks: is it actually what it claims to be; is it open at the hour they'll arrive; does it clear their hard constraints; is the evidence current (coverage older than roughly two years, or a change of chef, owner, or management since, downgrades confidence).

Then the domain-specific traps:

**Dining** — self-description and menu, not rating, decide whether it's a restaurant. Last seating and reservation availability.

Then **menu format**, which is a screen in its own right and not a detail. Read the restaurant's own posted menu — the PDF or page on its site — not a guide listing. Editorial coverage tells you a kitchen is good; it will not tell you the room is served four hot dishes and four cold ones. Four formats collapse a diner's options and must be identified before recommending, not discovered on arrival:

- **Tasting menu only** — no à la carte at all.
- **Blind tasting** — the kitchen decides; substitutions depend on notice given at booking.
- **Single fixed nightly menu** — the whole room eats the same thing.
- **Small plates** — the non-obvious one. It reads as flexible and is the opposite: a dozen half-dishes can contain fewer usable options than a short list of mains, because the format concentrates rather than spreads the protein choices.

For a user with dietary lines, count the dishes that actually clear them and say the number. "Two of eight" is the useful output; "has seafood options" is not. Where the count is low, say so before recommending, and prefer formats with a long à la carte card — the constraint costs one dish out of twelve rather than most of the menu.

**Lodging** — the gap between the photos and the rooms actually booked at that rate; noise sources (street, bar below, elevator, construction next door); how recently it was renovated and whether the good reviews describe renovated rooms; stairs and elevators in historic buildings; air conditioning where it matters; what "ten minutes from the center" means on foot with luggage and a hill; resort or destination fees; cancellation terms.

**Sights** — the dark day (many museums close Monday or Tuesday), last admission which is often an hour before closing, timed-entry availability for the actual date, seasonal and holiday hours, whether scaffolding or a closure has taken the main thing offline, weather exposure, and honest time-on-site: some famous items are a twenty-minute stop being sold as an afternoon.

**Tours** — who actually operates it; group size cap; whether admission is included or extra; whether there are shopping or "workshop" stops; real content time versus transit time; the guide's language; cancellation terms.

**Day plans** — sequence around fixed and timed items first, check dark days before building anything, respect travel time between stops and normal meal times, avoid stacking two ticketed entries back to back, keep one major thing per half-day, note the last transit or funicular, and carry a weather fallback for anything outdoor.

### When the user arrives with someone else's list

A list from a guide, concierge, hotel desk, or driver is evidence about how the list was assembled as much as about the places on it. The tell is geographic: when the picks cluster in the highest-rent visitor corridor and thin out one street back, the selection was optimized for ease of recommending, not for quality. Say so plainly, keep whatever survives screening, and replace the rest.

Screen each item on the list rather than accepting or rejecting the list whole. Guide lists commonly mix one genuinely good place with three high-volume ones.

### When the clock is short, availability outranks quality

Time-to-meal changes the ranking function, and this is the most common way a well-screened list still fails. A list of the best kitchens in a city is not actionable at 6pm on a Thursday in high season; the user makes six calls, gets six refusals, and has lost the evening.

When the meal or the night is hours away rather than days:

- Rank by **capacity and access first** — room size, continuous service through the afternoon, bar or counter seating, walk-in policy — and by quality second among what survives.
- Prefer a **geographic cluster** over a ranked list, so a refusal costs thirty seconds of walking rather than a cross-town trip. Give the cluster and the order to try within it.
- Say plainly that live table inventory is not visible. Reservation availability cannot be checked by fetching a page, and claiming otherwise wastes the user's time. Produce a call list with numbers and service hours, and name the tactics that actually work: asking for the bar or counter by name, the 5:00–6:30 window before the main rush, offering to be done by a stated time so the seating can be sold twice, and asking for tonight's cancellation list rather than only a future date.
- Check **how the user will travel between candidates** — elevation, stairs, funicular hours and whether it takes cards — before sequencing the cluster.

## Step 5 — Label confidence, and say when the data is thin

Every recommendation carries one of three labels. This is what the user relies on, so never quietly omit it.

- **Verified** — Tier A or B coverage within roughly the last two years, with nothing in the crowd data contradicting it. For lodging, recent stay-gated reviews count toward this.
- **Probable** — one credible source, or a large and consistent sample over a long operating history, but no editorial coverage.
- **Thin** — crowd data only, or a small sample (under ~150 reviews in a major city, under ~60 in a small one), or a bimodal distribution, or open under a year, or a tour known only from a marketplace listing. Name which of these applies, in one clause.

Rules that follow:

- Never lead with a Thin pick without calling it a gamble in the same sentence, and pair it with a Verified or Probable alternative.
- When a whole category comes back Thin — a small city, an under-covered cuisine, a niche activity, a late hour — say so plainly rather than manufacturing confidence: "no editorial coverage exists for this here; everything below rests on crowd data, so treat these as leads rather than recommendations."
- When a crowd sample is the evidence, state its size and shape, not just the score.
- Flag anything that is a guess as a guess. Never present inference as verification.
- Anything time-sensitive — hours, closures, timed entry, availability — gets verified against the official source or flagged as unverified. Do not assume yesterday's hours.

### Operational facts carry their own label

The labels above rate whether a place is **good**. They say nothing about whether it is **big**, **bookable**, or **à la carte** — and those claims routinely ride along inside a sentence that opens with a quality label, inheriting a confidence they were never given.

Label operational claims separately from quality claims. Room size, seat count, menu format, service hours, dress code, bar seating, and walk-in policy are each verified or inferred on their own evidence, regardless of how well-sourced the quality verdict is. A restaurant can be Verified excellent and simultaneously an unverified guess about everything structural.

Specifically, **review count is not capacity.** Volume is a proxy for how long a place has been popular, not for how many seats it has — a thirty-seat room open twenty years outscores a hundred-seat room open three. Never infer size, and therefore never infer walk-in odds, from review totals. Capacity comes from the restaurant's own description, photographs of the room, or a reviewer who states it.

Sources routinely disagree on closed days and service hours, particularly for small owner-run places whose aggregator listings go stale. When two sources conflict, say so and route the user to the phone rather than picking one silently.

## Step 6 — Output format

Lead with the recommendation, not the method.

For each pick: **name** — one line on what it is and why it fits what they asked. *Confidence label plus the evidence behind it.* Then logistics: location or walking time, hours, booking status, and anything to do or avoid on arrival.

Two to four picks. Padding to five dilutes the top pick and signals the screening wasn't done. Close with a one-line safe fallback whenever the lead pick carries risk.

For a day or multi-day plan, give the sequence with times and the reason for the order, mark which items are fixed or ticketed, and state the one thing most likely to break the plan.

## Step 7 — Close the loop

When the user reports back, record the place, the verdict, and above all the *reason* it worked or failed — "too bar-forward," "service was inconsistent," "hotel was noisy on the street side," "tour was half shopping stops." The reason generalizes; the name does not. Over time this is worth more than any external source, because it is the only data set calibrated to this user.

**Write new learnings as global by default.** A preference only becomes a context delta once it has demonstrably contradicted itself across two contexts — the same user wanting one thing on a working night and the opposite on a free one. Filing a first observation as context-specific is how a clean global preference gets fragmented into copies that then drift apart.

Record source performance too. If a particular guide's picks keep landing, weight it up; if Tier D picks keep failing, that confirms the hierarchy.

## Anti-patterns

- Sorting a map or marketplace search by rating and presenting the top four. This is the failure mode the whole skill exists to prevent.
- Asking questions whose answers are already known, instead of stating them as assumptions and inviting a correction.
- Recommending anything without confirming it is open, available, and not closed that day.
- Treating a tour marketplace's star rating as evidence about the guide who will actually show up.
- Hedging everything equally. Confidence labels only inform if they vary.
- Burying the recommendation under an explanation of the methodology.
- Reading a guide listing and treating it as having read the menu. The listing describes the cooking; the menu describes what the user can actually order.
- Inferring room size, capacity, or walk-in odds from review volume.
- Letting a quality label cover structural claims made in the same breath — "Verified, and the biggest room of the group" is two claims with one source behind it.
- Ranking by quality when the meal is in two hours, then handing the user six phone numbers and no fallback.
- Screening out tasting-menu formats but waving through small plates.
