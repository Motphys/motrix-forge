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

"""CLI command error-path coverage for the background MCP server."""

from types import SimpleNamespace

from Forge.mcp import command


def test_cli_exec_reports_missing_server(monkeypatch, capsys):
    monkeypatch.setattr(command, "get_server", lambda: None)

    assert command.cli_exec([]) == 1
    assert "not registered" in capsys.readouterr().out


def test_cli_exec_reports_start_failure(monkeypatch, capsys):
    class Server:
        def start(self, **_kwargs):
            raise RuntimeError("bind failed")

    monkeypatch.setattr(command, "get_server", lambda: Server())

    assert command.cli_exec(["--host", "127.0.0.1", "--port", "9999"]) == 1
    assert "bind failed" in capsys.readouterr().out


def test_cli_exec_handler_blocks_when_online_access_is_disabled(monkeypatch):
    prefs = SimpleNamespace()
    monkeypatch.setattr(command, "get_addon_prefs", lambda: prefs)
    monkeypatch.setattr(command, "check_online_state", lambda _prefs: False)
    monkeypatch.setattr(command, "cli_exec", lambda _argv: (_ for _ in ()).throw(AssertionError("must not run")))

    assert command.cli_exec_handler([]) == 1


def test_cli_exec_loads_blend_file_and_passes_token(monkeypatch, tmp_path):
    blend_file = tmp_path / "scene.blend"
    blend_file.touch()
    loaded = []
    starts = []

    class Server:
        def start(self, **kwargs):
            starts.append(kwargs)

        def stop(self):
            pass

    fake_bpy = SimpleNamespace(
        ops=SimpleNamespace(wm=SimpleNamespace(open_mainfile=lambda **kwargs: loaded.append(kwargs["filepath"])))
    )
    monkeypatch.setattr(command, "bpy", fake_bpy)
    monkeypatch.setattr(command, "get_server", lambda: Server())
    monkeypatch.setattr(command, "exec_blocking", lambda: None)

    assert command.cli_exec(["--blend-file", str(blend_file), "--token", "secret"]) == 0
    assert loaded == [str(blend_file.resolve())]
    assert starts == [{"host": "localhost", "port": 9876, "token": "secret"}]
