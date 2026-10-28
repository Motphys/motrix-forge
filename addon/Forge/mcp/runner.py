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

import sys
import traceback

import bpy

from .. import settings
from .constants import TIMER_ACTIVE_INTERVAL
from .utils import get_server, update_ui

STATE_OFFLINE_MESSAGE = "Online access must be enabled in the system preferences"


def check_online_state(prefs: settings.Forge_prefs | None) -> bool:
    """Check whether online access is permitted and return the result.

    Args:
        prefs: The addon preferences instance, or None when there is no add-on
            entry to read them from (the documented headless case).

    Returns:
        True when online access is permitted, False otherwise.
    """

    if bpy.app.online_access:
        return True
    if prefs is not None:
        # With no preferences there is nowhere to record the reason, so the
        # message below is the only report.
        prefs.autostart_error = STATE_OFFLINE_MESSAGE
    if bpy.app.background:
        print(f"Error: {STATE_OFFLINE_MESSAGE}")
        print("  Use --online-mode to enable online access from the command line")
    return False


def exec_blocking() -> None:
    """Block polling client connections until the server stops.

    Catches ``KeyboardInterrupt`` so that Ctrl+C exits cleanly.
    """

    mcp_server = get_server()
    if mcp_server is None:
        return

    try:
        while mcp_server.is_running():
            mcp_server.poll_blocking()
    except KeyboardInterrupt:
        pass


def exec_interactive() -> float | None:
    """Timer callback: poll connections, return next interval.

    Returns:
        The next timer interval in seconds, or None to unregister the timer.
    """

    mcp_server = get_server()
    if mcp_server is None:
        return None

    # While errors *should* never happen: without exception handling here,
    # any error would remove the timer - effectively breaking the add-on.
    try:
        work_state = mcp_server.poll()
    except BaseException:  # Keep the persistent timer alive even for tool-supplied BaseException.
        print(
            f"""Error: unhandled exception in the MCP server timer.\nThis may be a bug in Forge-MCP,
as errors should not be raised at this point, continuing:\n{traceback.format_exc()}""",
            file=sys.stderr,
        )
        # This is undefined, set to true so we reset the timer.
        work_state = True

    if not mcp_server.is_running():
        return None

    if work_state:
        mcp_server.timer_state.timer_idle_reset()

    return mcp_server.timer_state.timer_idle_interval()


def start_interactive(prefs):
    """Start the listener and polling timer together, or repair a missing timer."""
    mcp_server = get_server()
    if mcp_server is None:
        raise RuntimeError("MCP bridge is not registered; re-enable the Forge add-on")

    mcp_server.logging = prefs.use_log
    mcp_server.timer_state.internal_timer_update(
        active=prefs.active_interval,
        idle=prefs.idle_interval,
        idle_delay=prefs.idle_delay_interval,
    )
    started = False
    try:
        if not mcp_server.is_running():
            mcp_server.start(host=prefs.host, port=prefs.port, token=prefs.token)
            started = True
        if not bpy.app.timers.is_registered(exec_interactive):
            bpy.app.timers.register(exec_interactive, first_interval=TIMER_ACTIVE_INTERVAL, persistent=True)
    except Exception:
        # A listener without a polling timer accepts connections but never
        # answers them. Do not leave that misleading running state behind.
        if started:
            mcp_server.stop()
        raise
    prefs.autostart_error = ""
    return mcp_server


def auto_start_delayed():
    """Start the server after the configured delay.

    Reads the autostart preference, checks online access, and starts the
    MCP server if conditions are met. Registers the interactive polling timer.
    """
    prefs = settings.get_addon_prefs()
    if prefs is None:
        # Blender can call register() before creating the add-on preferences.
        # Keep the scheduled callback alive until registration has finished.
        return 1.0
    if not prefs.autostart:
        return None
    if not check_online_state(prefs):
        return None  # Stop re-running; don't retry every second.

    mcp_server = get_server()
    if mcp_server is None:
        return None

    try:
        start_interactive(prefs)
    except Exception as ex:
        prefs.autostart_error = str(ex)
        print(f"Blender MCP: auto-start failed: {str(ex)}")
    else:
        print(f"Blender MCP: server auto-started on {mcp_server.host}:{mcp_server.port}")
    update_ui()
    return None  # Run only once.
