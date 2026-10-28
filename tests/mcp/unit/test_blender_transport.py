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

"""Regression tests for the MCP client's null-delimited bridge protocol."""

import json

import forge_mcp.blender as blender
import pytest
from mcp.server.mcpserver.exceptions import ToolError


class FakeSocket:
    def __init__(self, chunks):
        self.chunks = iter(chunks)
        self.sent = b""

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return None

    def sendall(self, data):
        self.sent += data

    def recv(self, _size):
        return next(self.chunks, b"")


def _patch_connection(monkeypatch, *chunks):
    connection = FakeSocket(chunks)
    monkeypatch.setattr(blender.socket, "create_connection", lambda *_args, **_kwargs: connection)
    return connection


def test_call_blender_rejects_eof_before_delimiter(monkeypatch):
    _patch_connection(monkeypatch, b'{"status":"ok","result":{}', b"")

    with pytest.raises(ToolError, match="before completing"):
        blender.call_blender("result = {}", enforce_skill=False)


@pytest.mark.parametrize("payload", [{"result": {}}, {"status": "pending", "result": {}}])
def test_call_blender_rejects_missing_or_unknown_status(monkeypatch, payload):
    _patch_connection(monkeypatch, json.dumps(payload).encode() + b"\0")

    with pytest.raises(ToolError, match="unknown response status"):
        blender.call_blender("result = {}", enforce_skill=False)


def test_call_blender_requires_object_result(monkeypatch):
    _patch_connection(monkeypatch, b'{"status":"ok","result":[]}\0')

    with pytest.raises(ToolError, match="field 'result'"):
        blender.call_blender("result = {}", enforce_skill=False)


def test_call_blender_accepts_valid_delimited_response(monkeypatch):
    connection = _patch_connection(
        monkeypatch,
        b'{"status":"ok",',
        b'"result":{"value":3},"stdout":"done"}\0',
    )

    assert blender.call_blender("result = {}", enforce_skill=False) == {"value": 3, "stdout": "done"}
    assert connection.sent.endswith(b"\0")
