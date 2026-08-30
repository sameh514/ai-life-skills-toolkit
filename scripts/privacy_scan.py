#!/usr/bin/env python3
"""Scan the repository for anything that looks personal or secret.

Flags personal home paths, email and phone patterns, private keys, common
token formats, symbolic links, and missing Git ignore rules, then exits with
an error so they can be removed before publishing. A pass is a safety layer,
not a guarantee.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TEXT_SUFFIXES = {
    "",
    ".css",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".sh",
    ".svg",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}

RULES = {
    "macOS absolute home path": re.compile(r"/Users/[^/\s]+/"),
    "Linux absolute home path": re.compile(r"/home/[^/\s]+/"),
    "Windows absolute home path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
    "iCloud container path": re.compile(r"Mobile Documents/com~apple~CloudDocs"),
    "private key block": re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
    ),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[oprsu]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "bearer token": re.compile(
        r"(?i)\bAuthorization\s*:\s*Bearer\s+[A-Za-z0-9._~+/=-]{16,}"
    ),
    "email address": re.compile(
        r"\b[A-Z0-9._%+-]+@(?!example\.(?:com|org|net|test)\b)[A-Z0-9.-]+\.[A-Z]{2,}\b",
        re.IGNORECASE,
    ),
    "US phone number": re.compile(
        r"(?<!\d)(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}(?!\d)"
    ),
}

REQUIRED_IGNORE_LINES = {
    "private/",
    "config/preferences.local.json",
    "*.vault.json",
    ".env",
    "*.pem",
    "*.key",
}


def iter_text_files(root: Path):
    scanner_path = Path(__file__).resolve()
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.resolve() == scanner_path:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        yield path


def scan(root: Path) -> list[str]:
    failures: list[str] = []
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(root)
        for line_number, line in enumerate(text.splitlines(), 1):
            for label, pattern in RULES.items():
                if pattern.search(line):
                    failures.append(f"{relative}:{line_number}: {label}")
    for path in root.rglob("*"):
        if path.is_symlink():
            failures.append(f"{path.relative_to(root)}: symbolic link")

    ignore_path = root / ".gitignore"
    if not ignore_path.is_file():
        failures.append(".gitignore: missing")
    else:
        lines = {
            line.strip()
            for line in ignore_path.read_text(encoding="utf-8").splitlines()
        }
        for required in sorted(REQUIRED_IGNORE_LINES - lines):
            failures.append(f".gitignore: missing required rule {required}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    failures = scan(args.root.resolve())
    if failures:
        print("Privacy scan failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(
        "Privacy scan passed: no configured personal-path, identifier, or secret patterns found."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
