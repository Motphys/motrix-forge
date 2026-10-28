#!/usr/bin/env python
# Copyright (C) 2020-2026 Motphys Technology Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of Motrix Forge.
#
# Motrix Forge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Motrix Forge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Motrix Forge. If not, see <https://www.gnu.org/licenses/>.
# ==============================================================================

"""Discover a supported Blender, launch it in background mode, and run Forge tests.

Usage (command line, from repo root)::

    python run_tests.py

Or with custom arguments::

    python run_tests.py --tb=short -v -k "serialization"

When invoked by regular Python, this script discovers and validates Blender
4.5+ (including 5.2) from the system's Program Files directories or ``PATH``,
preferring the newest installation, then launches itself through Blender.
Set ``BLENDER_PATH`` to use a specific executable. Arguments are forwarded to
pytest. When invoked by Blender, it runs pytest directly.

``--factory-startup`` prevents user-enabled addons and asset-library settings
from shadowing the Forge sources and assets in this checkout.
"""

import os
import shutil
import site
import subprocess
import sys
from pathlib import Path

import bpy

# ── 0. Paths ───────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent  # T:/Project/blender-tools/
TEST_DIR = REPO_ROOT / "tests" / "forge"
MINIMUM_BLENDER_VERSION = (4, 5)


def _is_blender_process() -> bool:
    """Return whether this script is currently hosted by Blender."""
    executable_names = {Path(sys.executable).name.lower(), Path(sys.argv[0]).name.lower()}
    return any(name in {"blender", "blender.exe"} for name in executable_names)


def _blender_candidates():
    """Yield possible Blender executables from Windows system configuration."""
    seen_roots: set[Path] = set()
    for variable in ("ProgramW6432", "ProgramFiles", "ProgramFiles(x86)"):
        value = os.environ.get(variable)
        if not value:
            continue
        root = Path(value)
        if root in seen_roots:
            continue
        seen_roots.add(root)

        foundation = root / "Blender Foundation"
        if foundation.is_dir():
            for install_dir in sorted(foundation.glob("Blender *"), reverse=True):
                yield install_dir / ("blender.exe" if os.name == "nt" else "blender")

    path_executable = shutil.which("blender")
    if path_executable:
        yield Path(path_executable)


def _blender_version(executable: Path) -> tuple[int, int] | None:
    """Return the ``(major, minor)`` version reported by *executable*."""
    if not executable.is_file():
        return None
    try:
        result = subprocess.run(
            [str(executable), "--version"],
            check=False,
            capture_output=True,
            text=True,
            errors="replace",
        )
    except OSError:
        return None
    first_line = result.stdout.splitlines()[0] if result.stdout else ""
    if result.returncode != 0 or not first_line.startswith("Blender "):
        return None
    try:
        major, minor = (int(part) for part in first_line.split()[1].split(".")[:2])
    except (IndexError, ValueError):
        return None
    return major, minor


def _find_blender() -> Path:
    """Return the configured or newest installed executable reporting Blender 4.5+."""
    override = os.environ.get("BLENDER_PATH") or os.environ.get("BLENDER_45_PATH")
    if override:
        executable = Path(override).resolve()
        version = _blender_version(executable)
        if version is None or version < MINIMUM_BLENDER_VERSION:
            minimum = f"{MINIMUM_BLENDER_VERSION[0]}.{MINIMUM_BLENDER_VERSION[1]}"
            raise FileNotFoundError(f"BLENDER_PATH={override!r} is not a Blender {minimum}+ executable.")
        return executable

    seen: set[Path] = set()
    supported: list[tuple[tuple[int, int], Path]] = []
    for candidate in _blender_candidates():
        candidate = candidate.resolve()
        if candidate in seen:
            continue
        seen.add(candidate)
        version = _blender_version(candidate)
        if version is not None and version >= MINIMUM_BLENDER_VERSION:
            supported.append((version, candidate))
    if not supported:
        raise FileNotFoundError(
            "Blender 4.5+ was not found in Program Files or PATH. "
            "Set BLENDER_PATH to its executable if it is installed elsewhere."
        )
    return max(supported, key=lambda item: item[0])[1]


def _launch_background_tests() -> int:
    """Launch this runner through the newest supported Blender installation."""
    blender = _find_blender()
    pytest_args = sys.argv[1:]
    if pytest_args[:1] == ["--"]:
        pytest_args = pytest_args[1:]

    command = [
        str(blender),
        "--background",
        "--factory-startup",
        "--python",
        str(Path(__file__).resolve()),
    ]
    if pytest_args:
        command.extend(["--", *pytest_args])

    print(f"Using Blender: {blender}", flush=True)
    return subprocess.call(command, cwd=REPO_ROOT)


IN_BLENDER = _is_blender_process()
if not IN_BLENDER:
    sys.exit(_launch_background_tests())


# ── 1. Ensure pytest is available ──────────────────────────────────
# Blender disables the user site-packages directory (``site.ENABLE_USER_SITE``
# is False), so a pytest installed by the standalone Blender Python is not
# importable here. Add it explicitly before falling back to an install.
_user_site = site.getusersitepackages()
if _user_site and _user_site not in sys.path:
    sys.path.append(_user_site)

try:
    import pytest
except ImportError:
    # Attempt to install pytest into Blender's site-packages
    blender_dir = Path(bpy.app.binary_path).resolve().parent
    py_exe = blender_dir / bpy.app.version_string.split()[0].rsplit(".", 1)[0] / "python" / "bin" / "python.exe"
    if not py_exe.is_file():
        raise RuntimeError("pytest is not installed in Blender's Python environment")
    print(f"pytest not found. Installing via {py_exe} …")
    subprocess.check_call([str(py_exe), "-m", "pip", "install", "pytest", "-q"])
    import pytest


# ── 2. Collect pytest args ─────────────────────────────────────────
# If Blender is used, everything after the first ``--`` is pytest args.
pytest_args = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []

if not pytest_args:
    # Default: run all tests with verbose short traceback
    pytest_args = ["-v", "--tb=short", str(TEST_DIR)]
elif not any(
    not arg.startswith("-") and (Path(arg.split("::", 1)[0]).exists() or arg.split("::", 1)[0].endswith(".py"))
    for arg in pytest_args
):
    # Keep this Blender-specific runner scoped to the Forge suite when callers
    # provide only pytest options (for example ``--collect-only`` or ``-k``).
    # A warning filter such as ``error::DeprecationWarning`` is not a node ID.
    pytest_args.append(str(TEST_DIR))


# ── 3. Run tests ───────────────────────────────────────────────────
print(f"{'─' * 60}")
print("  Motrix Forge Test Runner")
print(f"  Blender:     {bpy.app.version_string if IN_BLENDER else 'N/A (standalone)'}")
print(f"  pytest:      {pytest.__version__}")
print(f"  test dir:    {TEST_DIR}")
print(f"  pytest args: {' '.join(pytest_args)}")
print(f"{'─' * 60}")

exit_code = pytest.main(pytest_args)
sys.exit(exit_code)
