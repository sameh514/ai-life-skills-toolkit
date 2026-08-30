#!/usr/bin/env python3
"""Copy this repository's eight everyday skills into the assistant's skills folder.

Works the same on Windows and macOS. Skills that are already installed are
skipped unless --replace is given, and --replace first moves the old folder to
a dated backup so nothing is lost.
"""

from __future__ import annotations

import argparse
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"


def default_destination() -> Path:
    """Return the assistant's skills folder: CODEX_HOME/skills when CODEX_HOME
    is set, otherwise .codex/skills inside the current user's home folder."""
    configured = os.environ.get("CODEX_HOME")
    base = Path(configured).expanduser() if configured else Path.home() / ".codex"
    return base / "skills"


def selected_groups(_platform: str) -> list[Path]:
    return [SKILLS_ROOT / "core"]


def available_skills(platform: str) -> list[Path]:
    skills: list[Path] = []
    for group in selected_groups(platform):
        if not group.is_dir():
            continue
        skills.extend(
            path
            for path in sorted(group.iterdir())
            if path.is_dir() and (path / "SKILL.md").is_file()
        )
    return skills


def backup_path(destination: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    backup_root = destination.parent.parent / "skill-backups" / stamp
    candidate = backup_root / destination.name
    number = 2
    while candidate.exists():
        candidate = backup_root.with_name(f"{stamp}-{number}") / destination.name
        number += 1
    return candidate


def install_one(
    source: Path, destination_root: Path, replace: bool, dry_run: bool
) -> str:
    destination = destination_root / source.name
    if destination.exists() and not replace:
        return f"SKIP    {source.name} (already exists)"
    if dry_run:
        action = "REPLACE" if destination.exists() else "INSTALL"
        return f"{action:<7} {source.name} -> {destination}"

    destination_root.mkdir(parents=True, exist_ok=True)
    backup: Path | None = None
    if destination.exists():
        backup = backup_path(destination)
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(destination), str(backup))
    try:
        shutil.copytree(source, destination)
    except Exception:
        if destination.exists():
            shutil.rmtree(destination)
        if backup is not None and backup.exists():
            shutil.move(str(backup), str(destination))
        raise
    if backup is not None:
        return f"REPLACED {source.name}; backup: {backup}"
    return f"INSTALLED {source.name}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--platform",
        choices=("auto", "windows", "macos", "all"),
        default="auto",
        help="kept for compatibility; every choice installs the same eight skills",
    )
    parser.add_argument(
        "--destination",
        type=Path,
        default=default_destination(),
        help="folder to install into (default: the assistant's skills folder)",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="back up and replace skills that are already installed",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show what would happen without copying anything",
    )
    parser.add_argument(
        "--list", action="store_true", help="list the skills without installing"
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    skills = available_skills(args.platform)
    if args.list:
        for skill in skills:
            print(skill.name)
        return 0
    for skill in skills:
        print(
            install_one(
                skill, args.destination.expanduser(), args.replace, args.dry_run
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
