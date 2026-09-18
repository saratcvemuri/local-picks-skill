# Changelog

One entry per change, and **the entry records the failure, not the edit**.

```
## YYYY-MM-DD
- What was recommended, and what actually went wrong, in one or two lines.
  → The rule that followed. (Step N)
```

The rule goes on its own line, arrow first, with the step it landed in. A git
diff will tell you what changed; only this file tells you *why*, and six months
out that is what shows whether a rule is still earning its place.

If you cannot write the failure line, you are making a change the skill has not
earned yet. Write it down as an issue and wait for the second occurrence.

The exception is a rule added deliberately rather than in response to something
going wrong. Those are legitimate, but they are **unearned**: nothing forced
them into existence, so nothing will naturally reveal them as unnecessary
either. File them under a `Design` heading, say plainly that no failure
prompted them, and name what would show the rule working. A rule that never
demonstrates its value is the first candidate for removal, and six months out
this heading is the only thing that distinguishes it from a rule that was paid
for in advance.

Changes that are not behavioral — packaging, tooling, docs — go under a
`Repository` heading in the same entry, so they never get mistaken for rules.

---

## 2026-09-18

- The source hierarchy was built from two queries in a city with full inspected
  guide coverage. It generalized badly twice over: to the cities that have no
  coverage at all, which is most of them, and to home, where the user already
  has better evidence than any guide.
  → Three evidence regimes — known ground, unfamiliar and consequential,
    unfamiliar and ordinary — replace the home/travel split. Reading crowd data
    is promoted from a tier to a full section, because it is the common case
    rather than the fallback. Edited sources are demoted to the regime where
    they actually earn their keep. (Steps 3–4)

- Confidence labels calibrated for one-shot travel decisions read as warnings
  ten minutes from the user's house, where being wrong costs one weeknight
  dinner and the user is the cheapest available instrument for resolving the
  uncertainty.
  → Labels move with consequence. The same word means different things at
    different stakes, and the answer says which. (Step 6)

**Design**

- No failure prompted this one. On known ground the user's rotation narrows on
  its own, and a skill that only answers what it is asked will keep confirming
  that rotation rather than widening it — the twenty places stay twenty, and
  the four that opened last month never surface.
  → An occasional unprompted suggestion, built so that ignoring it is free:
    one sentence, one candidate, no question attached, after the answer rather
    than inside it, and silent unless the stakes are low and the ground is
    familiar. (Step 8)

  **Unearned, so watch it.** It works if the user actually tries something it
  surfaced and it becomes part of the rotation. It fails if it reads as a nudge,
  if it fires on occasions or under time pressure, or if it goes ignored twice
  and keeps appearing. Eval 7 checks the mechanics; only the log will show
  whether the rule was worth having.

**Content**

- The rewrite reintroduced a real dietary line in the Step 1 example, added a
  named restaurant to the Step 8 example, and named one guide tier in Step 3
  while describing every other source by its properties. All three are the kind
  of fact this file is not supposed to hold, and the last one also undercuts the
  reason the tiers are described by property at all.
  → Examples keep their shape and specificity but carry no real place, no real
    preference and no named guide. (Steps 1, 3, 8)

**Repository**

- Body budget set to 250 lines, reverting the 300 agreed on 2026-09-17. The
  restructure above added a third of a file and still came out shorter, which
  is the argument for the tighter number rather than against it. Body is now
  198 lines.
- Deny-list extended to named guides, publications and booking platforms. The
  skill describes source tiers by their properties so that it still works where
  no guide covers anything; naming one undoes that. Named exemplars, if wanted,
  go in `references/`.
- Evals rewritten to the seven checks, adding regime routing and the
  exploratory suggestion. Both are run as sequences rather than single prompts,
  because neither failure mode is visible in one response.

## 2026-09-17

**Repository**

- Published `local-picks` as a public repo with the skill as its source of
  truth. The installed copy is now a build artifact; edits land here first.
- Added `scripts/validate_skills.py`, run on every push and pull request. It
  enforces the Agent Skills spec (frontmatter keys, name and description limits,
  name matching its directory) and two policies of this repo's own: a 300-line
  body budget and a personal-data deny-list.
- Added `license: Apache-2.0` to the skill frontmatter. It is one of the six
  keys the spec permits, so it survives packaging and upload, and it travels
  with the file when someone copies only `SKILL.md` out of the repo.
- Added `evals/local-picks/prompts.md`: five prompts covering the failure modes
  the skill was written against, plus one inverse check that a generic cooking
  question does not trigger it.

**Content**

- The Step 1 example opening named a real neighborhood and a real dietary line.
  Both were about to become public, and both are the kind of fact the skill
  itself says belongs in the user's memory rather than in the file.
  → Example assumptions stay specific and load-bearing but carry no real place
    and no real preference. The deny-list enforces it. (Step 1)

No rules changed. The skill body is otherwise unchanged from the version that
was in use before publication, apart from the frontmatter line noted above.
