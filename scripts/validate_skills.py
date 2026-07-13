#!/usr/bin/env python3
"""Validate the repository's standalone SKILL.md packages without dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "plugins" / "agent-workflows" / "skills"
FRONTMATTER = re.compile(r"\A---\r?\n(?P<content>.*?)\r?\n---\r?\n", re.DOTALL)
NAME = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
DESCRIPTION = re.compile(r"^description:\s*(.+)\s*$", re.MULTILINE)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_skill(skill_dir: Path) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        fail(f"{skill_dir.relative_to(ROOT)} is missing SKILL.md")

    text = skill_file.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        fail(f"{skill_file.relative_to(ROOT)} has invalid YAML frontmatter")

    frontmatter = match.group("content")
    name = NAME.search(frontmatter)
    description = DESCRIPTION.search(frontmatter)
    if not name or not description:
        fail(f"{skill_file.relative_to(ROOT)} must declare name and description")
    if name.group(1) != skill_dir.name:
        fail(f"{skill_file.relative_to(ROOT)} name must match its directory")
    if "[TODO" in text:
        fail(f"{skill_file.relative_to(ROOT)} contains template placeholders")
    if not text[match.end() :].strip():
        fail(f"{skill_file.relative_to(ROOT)} needs workflow instructions")

    metadata = skill_dir / "agents" / "openai.yaml"
    if not metadata.is_file():
        fail(f"{skill_dir.relative_to(ROOT)} is missing agents/openai.yaml")
    metadata_text = metadata.read_text(encoding="utf-8")
    required = ("display_name:", "short_description:", "default_prompt:")
    if not all(field in metadata_text for field in required):
        fail(f"{metadata.relative_to(ROOT)} is missing required interface metadata")
    if f"${name.group(1)}" not in metadata_text:
        fail(f"{metadata.relative_to(ROOT)} default prompt must mention ${name.group(1)}")

    print(f"OK: {skill_dir.relative_to(ROOT)}")


def main() -> None:
    if not SKILLS_DIR.is_dir():
        fail("skills directory is missing")
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("no skills found")
    for skill_dir in skill_dirs:
        validate_skill(skill_dir)
    print(f"Validated {len(skill_dirs)} skill(s).")


if __name__ == "__main__":
    main()
