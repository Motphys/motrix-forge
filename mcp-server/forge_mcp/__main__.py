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

"""Run the Forge MCP server over stdio: ``python -m forge_mcp``."""

from __future__ import annotations

import forge_mcp.resources  # noqa: F401 — importing registers the MJCF docs as MCP resources
import forge_mcp.tools  # noqa: F401 — importing registers all tools on `mcp`
from forge_mcp import mcp
from forge_mcp.tools import apply_tool_filter


def main() -> None:
    """Start the Forge MCP server over stdio, honoring the ``FORGE_TOOLS`` filter."""
    # Production filtering keeps the skill contract discoverable alongside any
    # write-tool subset. Unit-test MCPServer instances remain generic filters.
    mcp._forge_enforce_skill = True
    apply_tool_filter(mcp)
    mcp.run()


if __name__ == "__main__":
    main()
