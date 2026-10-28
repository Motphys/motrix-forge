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

"""
MCP bridge sub-system initialisation.

The server singleton is held in a module-level variable (see ``utils``) and
accessed via ``get_server()``.
"""

from __future__ import annotations

import bpy

from ..settings import get_addon_prefs
from .command import cli_exec_handler
from .runner import auto_start_delayed, exec_interactive
from .server import MCPServer
from .utils import set_server

# Store the CLI handle, only for correct register/unregister.
_cli_commands: list[object] = []


def register_mcp():
    """Initialise the MCP server and register CLI + timer hooks."""

    set_server(MCPServer())

    _cli_commands.append(bpy.utils.register_cli_command("forge_mcp", cli_exec_handler))

    if not bpy.app.background:
        prefs = get_addon_prefs()
        if prefs is None or prefs.autostart:
            bpy.app.timers.register(
                auto_start_delayed,
                first_interval=prefs.autostart_delay if prefs is not None else 1.0,
                persistent=True,
            )


def unregister_mcp():
    """Shut down the server and clean up all hooks."""
    for cmd in _cli_commands:
        bpy.utils.unregister_cli_command(cmd)
    _cli_commands.clear()

    if bpy.app.timers.is_registered(auto_start_delayed):
        bpy.app.timers.unregister(auto_start_delayed)
    if bpy.app.timers.is_registered(exec_interactive):
        bpy.app.timers.unregister(exec_interactive)

    mcp_server = set_server(None)
    if mcp_server is not None:
        mcp_server.stop()
