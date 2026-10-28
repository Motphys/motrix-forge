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

import bpy

from .server import MCPServer

# Module-level holder — survives file loads / new scenes.
# A module global dies with the module on addon
# reload, where ``unregister_mcp`` stops the server anyway.
_server: MCPServer | None = None


def get_server() -> MCPServer | None:
    """Return the active MCP server instance, or ``None`` if not registered."""
    return _server


def set_server(server: MCPServer | None) -> MCPServer | None:
    """Store *server* as the singleton, returning the previous instance."""
    global _server
    previous = _server
    _server = server
    return previous


def update_ui():
    """Redraw all 3D Viewport areas to reflect property changes."""
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == "VIEW_3D":
                area.tag_redraw()
