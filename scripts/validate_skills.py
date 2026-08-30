#!/usr/bin/env python3
"""Check every skill folder before publishing.

Each skill needs a SKILL.md whose name matches its folder, a short
description, a well-formed agents/openai.yaml, working local links, and no
leftover TODO-style placeholders.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MAX_DESCRIPTION_CHARS = 350
MAX_SKILL_LINES = 120
REQUIRED_INTERFACE_FIELDS = ("display_name", "short_description", "default_prompt")


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening YAML frontmatter delimiter")
    try:
        end = next(
            index for index, line in enumerate(lines[1:], 1) if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ValueError("missing closing YAML frontmatter delimiter") from exc
    data = yaml.safe_load("\n".join(lines[1:end]))
    if not isinstance(data, dict):
        raise TypeError("frontmatter must be a mapping")
    return data


def validate_skill(skill: Path) -> list[str]:
    failures: list[str] = []
    skill_file = skill / "SKILL.md"
    if not skill_file.is_file():
        return ["missing SKILL.md"]
    try:
        frontmatter = parse_frontmatter(skill_file)
    except (OSError, UnicodeDecodeError, yaml.YAMLError, ValueError) as exc:
        return [str(exc)]

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if name != skill.name:
        failures.append(f"frontmatter name {name!r} does not match folder")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        failures.append(
            "name must be lowercase letters, numbers, or hyphens and <=64 characters"
        )
    if not isinstance(description, str) or not description.strip():
        failures.append("description is missing")
    elif len(description) > MAX_DESCRIPTION_CHARS:
        failures.append(
            f"description is longer than {MAX_DESCRIPTION_CHARS} characters"
        )

    agents = skill / "agents" / "openai.yaml"
    if agents.exists():
        try:
            data = yaml.safe_load(agents.read_text(encoding="utf-8"))
            interface = data.get("interface") if isinstance(data, dict) else None
            if not isinstance(interface, dict):
                failures.append("agents/openai.yaml must contain an interface mapping")
            else:
                for field in REQUIRED_INTERFACE_FIELDS:
                    value = interface.get(field)
                    if not isinstance(value, str) or not value.strip():
                        failures.append(
                            f"agents/openai.yaml is missing a plain-text {field}"
                        )
        except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
            failures.append(f"invalid agents/openai.yaml: {exc}")

    text = skill_file.read_text(encoding="utf-8")
    if len(text.splitlines()) > MAX_SKILL_LINES:
        failures.append(
            f"SKILL.md is longer than {MAX_SKILL_LINES} lines; move optional detail to references"
        )
    if "## Keep momentum" not in text:
        failures.append("missing Keep momentum section")
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = target.split("#", 1)[0]
        if target_path and not (skill / target_path).exists():
            failures.append(f"broken local link: {target}")
    if re.search(r"\b(?:TODO|TBD|REPLACE_ME)\b", text):
        failures.append("unfinished placeholder found")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "skills",
    )
    args = parser.parse_args()
    skill_dirs = sorted(path.parent for path in args.root.glob("*/*/SKILL.md"))
    failed = False
    for skill in skill_dirs:
        failures = validate_skill(skill)
        if failures:
            failed = True
            for failure in failures:
                print(f"FAIL {skill}: {failure}")
        else:
            print(f"PASS {skill}")
    print(f"Validated {len(skill_dirs)} skills.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
