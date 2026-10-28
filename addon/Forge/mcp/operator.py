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
from bpy.types import Operator

from .. import settings
from .runner import STATE_OFFLINE_MESSAGE, auto_start_delayed, check_online_state, exec_interactive, start_interactive
from .utils import get_server


def _server():
    """Convenience: return the MCP server singleton or None."""

    return get_server()


class MCP_OT_Server_Start(Operator):  # type: ignore[misc]
    """Start the MCP bridge server and register the interactive polling timer."""

    bl_idname = "forge.mcp_server_start"
    bl_label = "Start MCP Bridge"
    bl_description = "Start the MCP socket bridge server that the MCP server can connect to"

    def execute(self, context: bpy.types.Context):
        """Start the MCP bridge server and register the interactive timer.

        Args:
            context: The active Blender context.

        Returns:
            A set of Blender operator return flags.
        """

        prefs = settings.get_addon_prefs()

        # Timers do not fire in background mode. Use the CLI command instead:
        # `blender --background --command forge_mcp`.
        if bpy.app.background:
            self.report({"ERROR"}, "Use `--command forge_mcp` to start the MCP bridge server in background mode")
            return {"CANCELLED"}
        if prefs is None:
            # Host, port and token all come from the preferences, so there is
            # nothing to start the server with.
            self.report({"ERROR"}, "Forge add-on preferences are unavailable; cannot start the MCP server")
            return {"CANCELLED"}
        if not check_online_state(prefs):
            self.report({"ERROR"}, STATE_OFFLINE_MESSAGE)
            return {"CANCELLED"}

        try:
            mcp_server = start_interactive(prefs)
        except Exception as ex:  # pylint: disable=broad-exception-caught
            prefs.autostart_error = str(ex)
            self.report({"ERROR"}, str(ex))
            return {"CANCELLED"}
        self.report({"INFO"}, f"MCP server started on {mcp_server.host}:{mcp_server.port}")
        return {"FINISHED"}


class MCP_OT_Server_Stop(Operator):  # type: ignore[misc]
    """Stop the MCP bridge server and unregister the interactive timer."""

    bl_idname = "forge.mcp_server_stop"
    bl_label = "Stop MCP Bridge"
    bl_description = "Stop the MCP Bridge Server"

    def execute(self, context: bpy.types.Context) -> set[str]:
        """Stop the MCP bridge server and unregister the interactive timer.

        Args:
            context: The active Blender context.

        Returns:
            A set of Blender operator return flags.
        """
        prefs = settings.get_addon_prefs()
        mcp_server = _server()

        # Clear any stale auto-start error so it does not persist in the UI.
        # Stopping needs nothing from the preferences, so a missing entry only
        # costs the message.
        if prefs is not None:
            prefs.autostart_error = ""
        if bpy.app.timers.is_registered(auto_start_delayed):
            bpy.app.timers.unregister(auto_start_delayed)
        if bpy.app.timers.is_registered(exec_interactive):
            bpy.app.timers.unregister(exec_interactive)
        if mcp_server is not None:
            mcp_server.stop()
        self.report({"INFO"}, "MCP bridge server stopped")
        return {"FINISHED"}


classes = (
    MCP_OT_Server_Start,
    MCP_OT_Server_Stop,
)
