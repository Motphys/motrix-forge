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

"""Run every test suite in the repository.

Usage from the repository root::

    python run_all_tests.py

The suites are run sequentially because the Forge and MCP E2E suites each
launch Blender and use shared local resources.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent


def _run_suite(name: str, command: list[str], env: dict[str, str] | None = None) -> bool:
    print(f"\n{'=' * 72}\n{name}\n{'=' * 72}", flush=True)
    result = subprocess.run(command, cwd=REPO_ROOT, env=env, check=False)
    if result.returncode == 0:
        print(f"[{name}] PASS", flush=True)
        return True
    print(f"[{name}] FAIL (exit code {result.returncode})", flush=True)
    return False


def main() -> int:
    python = sys.executable
    mcp_env = os.environ.copy()
    mcp_source = str(REPO_ROOT / "mcp-server")
    mcp_env["PYTHONPATH"] = os.pathsep.join(part for part in (mcp_source, mcp_env.get("PYTHONPATH", "")) if part)
    suites = [
        (
            "MCP unit + protocol tests",
            [python, "-m", "pytest", "tests/mcp/unit", "tests/mcp/integration"],
            mcp_env,
        ),
        ("Forge Blender tests", [python, "run_tests.py"], None),
        ("MCP Blender E2E tests", [python, "tests/mcp/e2e/driver.py"], None),
        (
            "MCP full model matrix E2E tests",
            [python, "tests/mcp/e2e/full_model_matrix.py"],
            None,
        ),
    ]

    failed = [name for name, command, env in suites if not _run_suite(name, command, env)]
    print(f"\n{'=' * 72}", flush=True)
    if failed:
        print("Failed suites:", ", ".join(failed), flush=True)
        return 1
    print("All test suites passed.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
