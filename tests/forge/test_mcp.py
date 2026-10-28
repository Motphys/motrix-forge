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

"""Tests for MCP execution, protocol encoding, and server lifecycle."""

import json
import sys

import bpy
import pytest
from Forge.mcp import utils
from Forge.mcp.capture import CaptureOutput
from Forge.mcp.constants import MAX_CAPTURED_OUTPUT_BYTES, encode_response, send_error, send_response
from Forge.mcp.deferred import DeferredManager
from Forge.mcp.executor import CodeExecutor


class FakeConnection:
    def __init__(self):
        self.sent = b""
        self.closed = False
        self.blocking = None
        self.timeout = None

    def recv(self, *_args):
        raise BlockingIOError

    def setblocking(self, value):
        self.blocking = value

    def settimeout(self, value):
        self.timeout = value

    def sendall(self, data):
        self.sent += data

    def close(self):
        self.closed = True


class FailingConnection(FakeConnection):
    def sendall(self, _data):
        raise TimeoutError("peer stopped reading")


def _decode_response(data):
    assert data.endswith(b"\0")
    return json.loads(data[:-1])


class TestCodeExecutor:
    def test_blender_modules_are_available(self):
        result = CodeExecutor.execute(
            "result = {'bpy': bpy is not None, 'mathutils': mathutils is not None}",
            strict_json=True,
        )

        assert result.response["status"] == "ok"
        assert result.response["result"] == {"bpy": True, "mathutils": True}

    def test_success_captures_output(self):
        result = CodeExecutor.execute("print('hello'); result = {'value': 3}", strict_json=True)

        assert result.response == {"status": "ok", "result": {"value": 3}, "stdout": "hello\n"}
        assert result.check_fn is None

    def test_exception_returns_traceback_and_stderr(self):
        result = CodeExecutor.execute("import sys; print('bad', file=sys.stderr); raise ValueError('boom')", True)

        assert result.response["status"] == "error"
        assert "ValueError: boom" in result.response["message"]
        assert result.response["stderr"] == "bad\n"

    def test_baseexception_from_tool_code_is_contained(self):
        result = CodeExecutor.execute("raise KeyboardInterrupt('boom')", True)

        assert result.response["status"] == "error"
        assert "KeyboardInterrupt: boom" in result.response["message"]

    def test_result_must_be_dict(self):
        result = CodeExecutor.execute("result = 42", True)

        assert result.response["status"] == "error"
        assert "must be a dict" in result.response["message"]

    def test_strict_json_rejects_set(self):
        result = CodeExecutor.execute("result = {'value': {1, 2}}", True)

        assert result.response["status"] == "error"
        assert "not JSON-serializable" in result.response["message"]

    def test_non_strict_json_uses_repr(self):
        result = CodeExecutor.execute("result = {'value': object()}", False)

        assert result.response["status"] == "ok"
        assert result.response["result"]["value"].startswith("<object object at")

    def test_guardian_blocks_exit_and_restores_it(self):
        original_exit = sys.exit

        result = CodeExecutor.execute("import sys; sys.exit(2)", True)

        assert result.response["status"] == "error"
        assert "sys.exit() is not allowed" in result.response["message"]
        assert sys.exit is original_exit

    def test_deferred_check_function_is_returned(self):
        result = CodeExecutor.execute("def check_is_finished():\n    return {'done': True}", True)

        assert result.response == {}
        assert result.check_fn() == {"done": True}

    def test_deferred_cancel_function_is_returned(self):
        result = CodeExecutor.execute(
            "def check_is_finished():\n    return None\ndef cancel_operation():\n    return 'cancelled'",
            True,
        )

        assert result.cancel_fn is not None
        assert result.cancel_fn() == "cancelled"

    @pytest.mark.parametrize(
        ("raw_request", "message"),
        [
            (b"not json", "JSONDecodeError"),
            (json.dumps({"type": "unknown"}).encode(), "Unknown request type"),
            (json.dumps({"type": "execute", "code": "result = {}"}).encode(), "strict_json"),
        ],
    )
    def test_invalid_requests(self, raw_request, message):
        result, strict_json = CodeExecutor.execute_from_request(raw_request)

        assert result.response["status"] == "error"
        assert message in result.response["message"]
        assert strict_json is False

    def test_request_authentication(self):
        request = json.dumps(
            {"type": "execute", "code": "result = {'ok': True}", "strict_json": True, "auth_token": "secret"}
        ).encode()

        accepted, _ = CodeExecutor.execute_from_request(request, expected_token="secret")
        rejected, _ = CodeExecutor.execute_from_request(request, expected_token="wrong")

        assert accepted.response["status"] == "ok"
        assert rejected.response == {"status": "error", "message": "Authentication failed"}

    def test_capture_output_restores_streams_on_exception(self):
        original_out, original_err = sys.stdout, sys.stderr

        with pytest.raises(RuntimeError):
            with CaptureOutput() as captured:
                print("captured stdout")
                print("captured stderr", file=sys.stderr)
                raise RuntimeError("boom")

        assert captured.stdout == "captured stdout\n"
        assert captured.stderr == "captured stderr\n"
        assert sys.stdout is original_out
        assert sys.stderr is original_err

    def test_capture_output_is_bounded(self):
        with CaptureOutput() as captured:
            print("x" * (MAX_CAPTURED_OUTPUT_BYTES * 2))

        assert len(captured.stdout) <= MAX_CAPTURED_OUTPUT_BYTES
        assert "output truncated" in captured.stdout


class TestProtocolHelpers:
    def test_encode_response_is_null_delimited(self):
        assert _decode_response(encode_response({"status": "ok", "value": "测试"})) == {
            "status": "ok",
            "value": "测试",
        }

    def test_send_response_configures_connection(self):
        connection = FakeConnection()

        assert send_response(connection, {"status": "ok"}) is True

        assert connection.blocking is True
        assert connection.timeout > 0
        assert _decode_response(connection.sent) == {"status": "ok"}

    def test_send_error_wraps_message(self):
        connection = FakeConnection()

        assert send_error(connection, "failed") is True

        assert _decode_response(connection.sent) == {"status": "error", "message": "failed"}

    def test_send_failure_is_reported(self, capsys):
        connection = FailingConnection()

        assert send_response(connection, {"status": "ok"}) is False

        assert "response send failed: peer stopped reading" in capsys.readouterr().err


class TestDeferredManager:
    def test_completed_result_is_sent_and_removed(self):
        manager = DeferredManager()
        connection = FakeConnection()
        manager.gather(connection, lambda: {"done": True}, True, "started\n", "")

        assert manager.pending() is True
        assert manager.poll() is True
        assert manager.pending() is False
        assert connection.closed is True
        assert _decode_response(connection.sent) == {
            "status": "ok",
            "result": {"done": True},
            "stdout": "started\n",
        }

    def test_completed_result_can_be_handed_to_nonblocking_sender(self):
        manager = DeferredManager()
        connection = FakeConnection()
        queued = []
        manager.gather(connection, lambda: {"done": True}, True, "", "")

        assert manager.poll(lambda conn, response: queued.append((conn, response))) is True

        assert manager.pending() is False
        assert connection.closed is False
        assert connection.sent == b""
        assert queued == [(connection, {"status": "ok", "result": {"done": True}})]

    def test_pending_result_does_no_work(self):
        manager = DeferredManager()
        connection = FakeConnection()
        manager.gather(connection, lambda: None, True, "", "")

        assert manager.poll() is False
        assert manager.pending() is True

        manager.close_all()
        assert connection.closed is True
        assert manager.pending() is False

    def test_invalid_result_returns_error(self):
        manager = DeferredManager()
        connection = FakeConnection()
        cancelled = []
        manager.gather(connection, lambda: 42, True, "", "", lambda: cancelled.append(True))

        assert manager.poll() is True
        response = _decode_response(connection.sent)
        assert response["status"] == "error"
        assert "must return None or dict" in response["message"]
        assert cancelled == [True]

    def test_non_strict_result_uses_repr_and_is_removed(self):
        manager = DeferredManager()
        connection = FakeConnection()
        manager.gather(connection, lambda: {"value": object()}, False, "", "")

        assert manager.poll() is True
        assert manager.pending() is False
        assert connection.closed is True
        assert _decode_response(connection.sent)["result"]["value"].startswith("<object object at")

    def test_baseexception_from_deferred_callback_is_contained(self):
        manager = DeferredManager()
        connection = FakeConnection()
        cancelled = []

        def fail():
            raise KeyboardInterrupt("boom")

        manager.gather(connection, fail, True, "", "", lambda: cancelled.append(True))

        assert manager.poll() is True
        assert manager.pending() is False
        assert connection.closed is True
        assert "KeyboardInterrupt: boom" in _decode_response(connection.sent)["message"]
        assert cancelled == [True]

    def test_guardian_wraps_deferred_callback(self):
        manager = DeferredManager()
        connection = FakeConnection()
        cancelled = []
        manager.gather(connection, lambda: sys.exit(2), True, "", "", lambda: cancelled.append(True))

        assert manager.poll() is True
        assert manager.pending() is False
        assert "sys.exit() is not allowed" in _decode_response(connection.sent)["message"]
        assert cancelled == [True]

    def test_timeout_cancels_operation(self):
        manager = DeferredManager()
        connection = FakeConnection()
        cancelled = []
        manager.gather(connection, lambda: None, True, "", "", lambda: cancelled.append(True))
        manager.clients[0].deadline = 0.0

        assert manager.poll() is True
        assert cancelled == [True]
        assert manager.pending() is False
        assert "timed out" in _decode_response(connection.sent)["message"]

    def test_close_all_cancels_operations(self):
        manager = DeferredManager()
        connection = FakeConnection()
        cancelled = []
        manager.gather(connection, lambda: None, True, "", "", lambda: cancelled.append(True))

        manager.close_all()

        assert cancelled == [True]
        assert connection.closed is True
        assert manager.pending() is False


class TestMCPServerStorage:
    def test_server_reference_survives_driver_namespace_clear(self):
        """File > New / opening a blend clears ``bpy.app.driver_namespace``.

        The server singleton must live somewhere that survives it
        (regression: the MCP service was silently lost on every file load
        while the singleton was stored in ``driver_namespace`` — the polling
        timer found ``None`` and unregistered itself).
        """
        sentinel = object()
        previous = utils.set_server(sentinel)
        try:
            bpy.app.driver_namespace.clear()
            assert utils.get_server() is sentinel
        finally:
            utils.set_server(previous)

    def test_set_server_returns_previous_instance(self):
        sentinel_a, sentinel_b = object(), object()
        previous = utils.set_server(sentinel_a)
        try:
            assert utils.set_server(sentinel_b) is sentinel_a
            assert utils.get_server() is sentinel_b
        finally:
            utils.set_server(previous)
