#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md in this repo.

Exits non-zero on any failure. Two kinds of check live here:

  Spec checks     mirror the Agent Skills specification and the stricter
                  validation that claude.ai upload and package_skill.py apply.
                  If these fail, the skill will not install somewhere.

  Policy checks   are this repo's own discipline: a body-length budget and a
                  personal-data tripwire. Nothing outside this repo enforces
                  them, which is exactly why they are enforced here.

Usage:
    python scripts/validate_skills.py [--skills-dir skills]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

# --- Spec constants -------------------------------------------------------
# Sourced from https://agentskills.io/specification and
# https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
# Re-verify against the docs before changing any of these.

ALLOWED_KEYS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
REQUIRED_KEYS = {"name", "description"}

NAME_MAX = 64
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_RESERVED = ("anthropic", "claude")

DESCRIPTION_MAX = 1024
COMPATIBILITY_MAX = 500

XML_TAG = re.compile(r"<[^>]+>")

# --- Policy constants -----------------------------------------------------
# The body budget is deliberate, not technical. The skill gains a rule every
# time a recommendation fails; an unchecked file grows past the point where it
# is read carefully. Anthropic's own guidance allows 500 lines. This is
# tighter on purpose. Raising it is a decision, not a fix.

BODY_MAX_LINES = 300

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)


class Failure(Exception):
    pass


def load_denylist(scripts_dir: Path) -> list[tuple[str, re.Pattern[str]]]:
    """Read denylist.txt plus an optional, untracked denylist.local.txt.

    The local file exists so the owner can screen for terms that would
    themselves be personal data if published in this repo.
    """
    patterns: list[tuple[str, re.Pattern[str]]] = []
    for name in ("denylist.txt", "denylist.local.txt"):
        path = scripts_dir / name
        if not path.exists():
            continue
        for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            try:
                patterns.append((f"{name}:{lineno}", re.compile(line, re.IGNORECASE)))
            except re.error as exc:
                raise Failure(f"{name}:{lineno}: bad regex {line!r}: {exc}")
    return patterns


def split_frontmatter(text: str, path: Path) -> tuple[dict, str]:
    match = FRONTMATTER.match(text)
    if not match:
        raise Failure(f"{path}: no YAML frontmatter delimited by --- at the top of the file")
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise Failure(f"{path}: frontmatter is not valid YAML: {exc}")
    if not isinstance(data, dict):
        raise Failure(f"{path}: frontmatter must be a YAML mapping, got {type(data).__name__}")
    return data, text[match.end():]


def check_frontmatter(data: dict, path: Path, errors: list[str]) -> None:
    rel = path.parent.name

    missing = REQUIRED_KEYS - data.keys()
    if missing:
        errors.append(f"{path}: missing required key(s): {', '.join(sorted(missing))}")

    unexpected = data.keys() - ALLOWED_KEYS
    if unexpected:
        errors.append(
            f"{path}: unexpected key(s) in frontmatter: {', '.join(sorted(unexpected))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_KEYS))}. "
            f"Anything outside this set is a hard error on claude.ai upload and in "
            f"package_skill.py. Per-tool extras belong under `metadata`."
        )

    name = data.get("name")
    if isinstance(name, str):
        if len(name) > NAME_MAX:
            errors.append(f"{path}: name is {len(name)} characters, maximum is {NAME_MAX}")
        if not NAME_PATTERN.fullmatch(name):
            errors.append(
                f"{path}: name {name!r} must be lowercase letters, numbers and single "
                f"hyphens, with no leading, trailing or consecutive hyphens"
            )
        for word in NAME_RESERVED:
            if word in name.lower():
                errors.append(f"{path}: name {name!r} contains the reserved word {word!r}")
        if name != rel:
            errors.append(
                f"{path}: name {name!r} does not match its directory {rel!r}. "
                f"The spec requires these to be identical."
            )
    elif name is not None:
        errors.append(f"{path}: name must be a string, got {type(name).__name__}")

    description = data.get("description")
    if isinstance(description, str):
        if not description.strip():
            errors.append(f"{path}: description is empty")
        if len(description) > DESCRIPTION_MAX:
            errors.append(
                f"{path}: description is {len(description)} characters, maximum is {DESCRIPTION_MAX}"
            )
        if XML_TAG.search(description):
            errors.append(f"{path}: description must not contain XML tags")
    elif description is not None:
        errors.append(f"{path}: description must be a string, got {type(description).__name__}")

    compatibility = data.get("compatibility")
    if isinstance(compatibility, str) and len(compatibility) > COMPATIBILITY_MAX:
        errors.append(
            f"{path}: compatibility is {len(compatibility)} characters, "
            f"maximum is {COMPATIBILITY_MAX}"
        )

    metadata = data.get("metadata")
    if metadata is not None and not isinstance(metadata, dict):
        errors.append(f"{path}: metadata must be a mapping, got {type(metadata).__name__}")


def check_body(body: str, path: Path, errors: list[str]) -> None:
    lines = body.strip("\n").splitlines()
    if len(lines) > BODY_MAX_LINES:
        errors.append(
            f"{path}: body is {len(lines)} lines, budget is {BODY_MAX_LINES}. "
            f"This is a policy cap, not a technical limit. Either cut a rule that "
            f"has stopped earning its place, or move reference material to a "
            f"separate file in the skill directory."
        )


def check_denylist(
    text: str, path: Path, patterns: list[tuple[str, re.Pattern[str]]], errors: list[str]
) -> None:
    """Facts about places and people belong in the user's memory, not in a public skill."""
    for lineno, line in enumerate(text.splitlines(), 1):
        for origin, pattern in patterns:
            match = pattern.search(line)
            if match:
                errors.append(
                    f"{path}:{lineno}: matched deny-list pattern from {origin}: "
                    f"{match.group(0)!r}. Personal or place-specific facts belong in "
                    f"the user's memory, not in this file."
                )


def validate(skill_md: Path, patterns: list[tuple[str, re.Pattern[str]]]) -> list[str]:
    errors: list[str] = []
    text = skill_md.read_text(encoding="utf-8")
    try:
        data, body = split_frontmatter(text, skill_md)
    except Failure as exc:
        return [str(exc)]
    check_frontmatter(data, skill_md, errors)
    check_body(body, skill_md, errors)
    check_denylist(text, skill_md, patterns, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", default="skills", help="directory holding skill folders")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    skills_dir = repo / args.skills_dir

    if not skills_dir.is_dir():
        print(f"error: {skills_dir} is not a directory", file=sys.stderr)
        return 1

    try:
        patterns = load_denylist(repo / "scripts")
    except Failure as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    if not skill_files:
        print(f"error: no skills/*/SKILL.md found under {skills_dir}", file=sys.stderr)
        return 1

    # A stray SKILL.md one level too deep silently never loads. Catch it here.
    for stray in sorted(skills_dir.glob("*/*/SKILL.md")):
        print(f"error: {stray.relative_to(repo)} is nested too deeply to load", file=sys.stderr)
        return 1

    total = 0
    for skill_md in skill_files:
        errors = validate(skill_md, patterns)
        rel = skill_md.relative_to(repo)
        if errors:
            total += len(errors)
            print(f"FAIL {rel}", file=sys.stderr)
            for error in errors:
                print(f"  - {error.replace(str(skill_md), str(rel))}", file=sys.stderr)
        else:
            print(f"ok   {rel}")

    if total:
        print(f"\n{total} problem(s) in {len(skill_files)} skill(s)", file=sys.stderr)
        return 1
    print(f"\n{len(skill_files)} skill(s) validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
