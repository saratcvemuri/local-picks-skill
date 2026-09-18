# local-picks

An [Agent Skill](https://agentskills.io) for recommending and evaluating places
and experiences — restaurants, hotels, sights, museums, tours, neighborhoods and
day plans — in any city.

It exists because bad recommendations are rarely a matter of taste. They come
from failure modes a star rating cannot see:

- **Category error.** A cocktail bar that serves food is not a dinner
  destination. A "half-day tour" is a shopping stop with a bus ride.
- **Variance, not average.** A 4.4 built from 60% fives and 20% ones is a coin
  flip. Averages hide kitchens that depend on who is working and hotels where
  half the rooms were renovated.
- **Thin or gamed samples.** Thirty motivated reviews move a small market's mean
  by two tenths. Tour marketplaces are the worst offenders.
- **Logistics.** Dark days, last seating, timed entry sold out, last funicular.

So the skill ranks sources by how hard they are to game, screens each candidate
against the traps specific to its category, and puts an explicit confidence
label — Verified, Probable, Thin — on every pick. Thin data never gets presented
as certainty.

It is instructions only. No scripts, no network calls, nothing to execute. You
can audit the whole thing in one sitting, which is the point.

## Install

**As a plugin** (Claude Code):

```bash
/plugin marketplace add saratcvemuri/local-picks-skill
```

```bash
/plugin install local-picks@local-picks-skill
```

**By hand** — copy the skill directory into your personal or project skills
folder. There is no supported way to install a skill straight from a repo path
without a marketplace, so this is the alternative:

```bash
git clone https://github.com/saratcvemuri/local-picks-skill.git && cp -R local-picks-skill/skills/local-picks ~/.claude/skills/
```

**On claude.ai** — Settings › Capabilities, uploading a zip whose *top-level
folder* is the skill directory. Files at the zip root will not install:

```bash
cd skills && zip -r ../local-picks.zip local-picks && cd ..
```

## Repository layout

```
skills/local-picks/SKILL.md      the skill
evals/local-picks/prompts.md     six prompts, read by a human
scripts/validate_skills.py       spec and policy checks, run in CI
scripts/denylist.txt             personal-data patterns
CHANGELOG.md                     one entry per change, failure first
.claude-plugin/                  marketplace and plugin manifests
```

The repo root doubles as the plugin, which is why `marketplace.json` and
`plugin.json` sit side by side and the plugin `source` is `"./"`. The skill
cannot live at the repo root: the spec requires `name` to match its parent
directory, and plugins load skills from `skills/`.

## Validation

```bash
pip install pyyaml && python scripts/validate_skills.py
```

Two kinds of check, and the difference matters:

**Spec checks** mirror the [Agent Skills
specification](https://agentskills.io/specification) and the stricter validation
that claude.ai upload and `package_skill.py` apply. Failing one means the skill
will not install somewhere. Only six frontmatter keys are permitted — `name`,
`description`, `license`, `compatibility`, `metadata`, `allowed-tools` — and
anything else is a hard error on those paths. Note that `version` is **not** one
of them; it belongs under `metadata`.

**Policy checks** are this repo's own, and nothing outside it enforces them:

- **Body budget: 300 lines.** Anthropic's guidance allows 500. This is tighter
  on purpose. The skill gains a rule every time a recommendation fails, and an
  unchecked file grows past the point where it is read carefully. Failing the
  build is the enforcement mechanism. Raising the number is a decision, not a
  fix — and the reason to raise it is never "the file got long."
- **No personal data.** The skill is public and the pressure to embed one useful
  local fact is constant: the dietary line that keeps coming up, the
  neighborhood you always stay in, the restaurant that worked last time. Each is
  individually harmless and collectively turns a general method into one
  person's notebook. Facts about places belong in the user's memory. The skill
  holds only the method for finding them.

  `scripts/denylist.txt` is a tripwire, not a guarantee. It cannot recognise an
  arbitrary restaurant or hotel name, and no pattern list can — reviewing a diff
  for names is still a human job. Terms that would themselves be personal data
  if published here go in `scripts/denylist.local.txt`, which is git-ignored and
  read by the validator when present.

### A documentation conflict worth knowing about

Anthropic's platform docs and the Agent Skills spec both give **1024
characters** as the maximum for `description`. The claude.ai Help Center article
on creating custom skills says **200**. The validator enforces 1024, on the
grounds that it is the normative spec and two other sources agree. This skill's
description is 920 characters, so if the 200 figure turns out to govern the
claude.ai upload path specifically, that route will need a shortened
description. Nothing else is affected.

## Changing the skill

The repo is the only place edits land. A session can propose a diff; nothing is
authoritative until it is committed here.

Content changes come from **observed failures only** — not from tone, not from
"this could be clearer," not from a rule that seems likely to help. Every rule
in the skill is there because a recommendation failed without it, and the
[CHANGELOG](CHANGELOG.md) records the failure rather than the edit precisely so
that a rule which has stopped earning its place can be found and removed.

Before opening a pull request:

1. `python scripts/validate_skills.py` passes.
2. The [evals](evals/local-picks/prompts.md) still behave, including the inverse
   check that a generic cooking question does not trigger the skill.
3. The CHANGELOG entry names the failure and the step the rule landed in.

Not in scope, deliberately: scripts or executable code in the skill directory,
and city- or user-specific content anywhere in the repo.

## Reporting a failure

Open an issue with the [failure report
template](.github/ISSUE_TEMPLATE/failure-report.yml). It asks what you asked,
what was recommended, what actually happened, and **which step of the skill
should have caught it**. A report that cannot name a step is a feature request
and gets triaged differently — that is not a brush-off, it is the difference
between a rule the skill has earned and one it has not.

## License

[Apache 2.0](LICENSE).
