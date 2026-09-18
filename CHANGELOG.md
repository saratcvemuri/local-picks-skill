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

Changes that are not behavioral — packaging, tooling, docs — go under a
`Repository` heading in the same entry, so they never get mistaken for rules.

---

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
