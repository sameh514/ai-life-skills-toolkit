from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install_skills.py"


class InstallerTests(unittest.TestCase):
    def install(
        self, platform: str, destination: Path
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(INSTALLER),
                "--platform",
                platform,
                "--destination",
                str(destination),
            ],
            check=True,
            capture_output=True,
            text=True,
        )

    def test_windows_installs_core_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "skills"
            self.install("windows", destination)
            installed = {path.name for path in destination.iterdir() if path.is_dir()}
            expected = {
                path.parent.name
                for path in (ROOT / "skills" / "core").glob("*/SKILL.md")
            }
            self.assertEqual(installed, expected)

    def test_macos_installs_same_everyday_collection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "skills"
            self.install("macos", destination)
            installed = {path.name for path in destination.iterdir() if path.is_dir()}
            expected = {
                path.parent.name
                for path in (ROOT / "skills" / "core").glob("*/SKILL.md")
            }
            self.assertEqual(installed, expected)

    def test_existing_skill_is_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "skills"
            self.install("windows", destination)
            result = self.install("windows", destination)
            self.assertIn("SKIP", result.stdout)

    def test_replace_creates_backup_outside_skills_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "codex" / "skills"
            self.install("windows", destination)
            subprocess.run(
                [
                    sys.executable,
                    str(INSTALLER),
                    "--platform",
                    "windows",
                    "--destination",
                    str(destination),
                    "--replace",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            backups = list((destination.parent / "skill-backups").glob("*/*/SKILL.md"))
            self.assertTrue(backups)
            self.assertFalse(
                any("backup" in path.name for path in destination.iterdir())
            )


if __name__ == "__main__":
    unittest.main()
