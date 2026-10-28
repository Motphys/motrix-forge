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

"""Coverage for the MCP timer/online-state integration boundary."""

from types import SimpleNamespace

import pytest
from Forge import mcp, settings
from Forge.mcp import operator as mcp_operator
from Forge.mcp import runner
from Forge.mcp import utils as mcp_utils
from Forge.mcp.server import MCPServer


class _TimerState:
    def __init__(self):
        self.reset_count = 0

    def timer_idle_reset(self):
        self.reset_count += 1

    def timer_idle_interval(self):
        return 0.25


class _Server:
    def __init__(self, running=True, poll_result=True, poll_error=False):
        self.running = running
        self.poll_result = poll_result
        self.poll_error = poll_error
        self.timer_state = _TimerState()

    def poll(self):
        if self.poll_error:
            raise RuntimeError("poll failed")
        return self.poll_result

    def is_running(self):
        return self.running


def test_check_online_state_records_offline_error(monkeypatch):
    prefs = SimpleNamespace(autostart_error="")
    monkeypatch.setattr(runner, "bpy", SimpleNamespace(app=SimpleNamespace(online_access=False, background=False)))

    assert runner.check_online_state(prefs) is False
    assert prefs.autostart_error == runner.STATE_OFFLINE_MESSAGE


def test_check_online_state_accepts_online(monkeypatch):
    prefs = SimpleNamespace(autostart_error="stale")
    monkeypatch.setattr(runner, "bpy", SimpleNamespace(app=SimpleNamespace(online_access=True, background=False)))

    assert runner.check_online_state(prefs) is True
    assert prefs.autostart_error == "stale"


def test_exec_interactive_resets_idle_timer(monkeypatch):
    server = _Server(running=True, poll_result=True)
    monkeypatch.setattr(runner, "get_server", lambda: server)

    assert runner.exec_interactive() == 0.25
    assert server.timer_state.reset_count == 1


def test_exec_interactive_survives_poll_error(monkeypatch):
    server = _Server(running=True, poll_error=True)
    monkeypatch.setattr(runner, "get_server", lambda: server)

    assert runner.exec_interactive() == 0.25
    assert server.timer_state.reset_count == 1


def test_exec_interactive_unregisters_when_server_stops(monkeypatch):
    server = _Server(running=False)
    monkeypatch.setattr(runner, "get_server", lambda: server)

    assert runner.exec_interactive() is None


class _Timers:
    def __init__(self):
        self.callbacks = {}

    def register(self, callback, **kwargs):
        assert callback not in self.callbacks
        self.callbacks[callback] = kwargs

    def is_registered(self, callback):
        return callback in self.callbacks

    def unregister(self, callback):
        del self.callbacks[callback]


@pytest.fixture
def interactive_bridge(monkeypatch):
    timers = _Timers()
    fake_bpy = SimpleNamespace(app=SimpleNamespace(timers=timers, online_access=True, background=False))
    prefs = SimpleNamespace(
        host="127.0.0.1",
        port=0,
        token="",
        autostart=True,
        autostart_delay=2.0,
        active_interval=0.05,
        idle_interval=1.0,
        idle_delay_interval=5.0,
        use_log=False,
        autostart_error="stale",
    )
    server = MCPServer()
    monkeypatch.setattr(runner, "bpy", fake_bpy)
    monkeypatch.setattr(runner, "get_server", lambda: server)
    monkeypatch.setattr(runner.settings, "get_addon_prefs", lambda: prefs)
    monkeypatch.setattr(runner, "update_ui", lambda: None)
    try:
        yield server, prefs, timers, fake_bpy
    finally:
        server.stop()


def test_autostart_waits_for_preferences(interactive_bridge, monkeypatch):
    server, prefs, timers, _ = interactive_bridge
    monkeypatch.setattr(runner.settings, "get_addon_prefs", lambda: None)
    assert runner.auto_start_delayed() == 1.0
    assert not server.is_running()
    monkeypatch.setattr(runner.settings, "get_addon_prefs", lambda: prefs)
    assert runner.auto_start_delayed() is None
    assert server.is_running()
    assert timers.is_registered(runner.exec_interactive)
    assert prefs.autostart_error == ""


def test_register_schedules_autostart_before_preferences_exist(interactive_bridge, monkeypatch):
    server, _, timers, fake_bpy = interactive_bridge
    fake_bpy.utils = SimpleNamespace(register_cli_command=lambda *_: object())
    monkeypatch.setattr(mcp, "bpy", fake_bpy)
    monkeypatch.setattr(mcp, "MCPServer", lambda: server)
    monkeypatch.setattr(mcp, "set_server", lambda _: None)
    monkeypatch.setattr(mcp, "get_addon_prefs", lambda: None)
    monkeypatch.setattr(mcp, "_cli_commands", [])
    mcp.register_mcp()
    assert timers.is_registered(runner.auto_start_delayed)


def test_start_is_idempotent_and_repairs_polling(interactive_bridge):
    server, prefs, timers, _ = interactive_bridge
    runner.start_interactive(prefs)
    listener = server.state.socket
    runner.start_interactive(prefs)
    assert server.state.socket is listener
    assert len(timers.callbacks) == 1
    timers.unregister(runner.exec_interactive)
    runner.start_interactive(prefs)
    assert timers.is_registered(runner.exec_interactive)
    assert server.state.socket is listener


def test_logging_preference_changes_without_restarting_bridge(interactive_bridge, monkeypatch):
    server, prefs, _, _ = interactive_bridge
    monkeypatch.setattr(mcp_utils, "get_server", lambda: server)
    runner.start_interactive(prefs)
    listener = server.state.socket

    for enabled in (True, False, True):
        prefs.use_log = enabled
        settings._update_mcp_logging(prefs, None)
        assert server.logging is enabled
        assert server.state.socket is listener


def test_logging_preference_can_change_before_bridge_registration(monkeypatch):
    monkeypatch.setattr(mcp_utils, "get_server", lambda: None)
    settings._update_mcp_logging(SimpleNamespace(use_log=True), None)


def test_start_rolls_back_listener_when_timer_registration_fails(interactive_bridge, monkeypatch):
    server, prefs, timers, _ = interactive_bridge

    def fail(*_args, **_kwargs):
        raise RuntimeError("timer registration failed")

    monkeypatch.setattr(timers, "register", fail)
    assert runner.auto_start_delayed() is None
    assert not server.is_running()
    assert prefs.autostart_error == "timer registration failed"


def test_autostart_records_bind_error_and_manual_retry_recovers(interactive_bridge):
    server, prefs, timers, _ = interactive_bridge
    blocker = MCPServer(host=prefs.host, port=0)
    blocker.start()
    prefs.port = blocker.state.socket.getsockname()[1]
    try:
        assert runner.auto_start_delayed() is None
        assert not server.is_running()
        assert prefs.autostart_error
        assert not timers.is_registered(runner.exec_interactive)
    finally:
        blocker.stop()
    runner.start_interactive(prefs)
    assert server.is_running()
    assert prefs.autostart_error == ""


def test_stop_cancels_pending_autostart(interactive_bridge, monkeypatch):
    server, _, timers, fake_bpy = interactive_bridge
    monkeypatch.setattr(mcp_operator, "bpy", fake_bpy)
    monkeypatch.setattr(mcp_operator, "_server", lambda: server)
    timers.register(runner.auto_start_delayed)
    runner.start_interactive(runner.settings.get_addon_prefs())
    operator = SimpleNamespace(report=lambda *_: None)
    assert mcp_operator.MCP_OT_Server_Stop.execute(operator, None) == {"FINISHED"}
    assert not server.is_running()
    assert not timers.callbacks


def test_autostart_respects_disabled_preference(interactive_bridge):
    server, prefs, timers, _ = interactive_bridge
    prefs.autostart = False
    assert runner.auto_start_delayed() is None
    assert not server.is_running()
    assert not timers.callbacks
