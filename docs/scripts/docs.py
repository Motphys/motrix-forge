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

"""Run MkDocs in the repository's shared environment from any directory."""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV = ROOT.parent / ".venv"


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in {"serve", "build"}:
        print("Usage: python <docs-directory>/scripts/docs.py {serve|build} [MkDocs options]")
        return 2
    python = ENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not python.is_file():
        print("Run `uv sync` from the repository root to install documentation dependencies.", file=sys.stderr)
        return 1
    try:
        return subprocess.call([str(python), "-m", "mkdocs", *sys.argv[1:]], cwd=ROOT)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
