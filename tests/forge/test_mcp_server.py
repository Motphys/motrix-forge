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

"""MCPServer socket bridge tests — request/response framing over real TCP sockets.

Covers the interactive ``poll()`` path and the background ``poll_blocking()``
path of ``Forge.mcp.server.MCPServer`` with loopback connections.
"""

import json
import select
import socket
import threading
import time

import pytest
from Forge.mcp.constants import MAX_REQUEST_BYTES, encode_response
from Forge.mcp.server import MCPServer


@pytest.fixture
def server():
    """A running MCPServer on an OS-assigned loopback port."""
    instance = MCPServer(host="127.0.0.1", port=0)
    instance.start()
    yield instance
    instance.stop()


def _port(server: MCPServer) -> int:
    return server.state.socket.getsockname()[1]


def _request(code: str, strict_json: bool = False, auth_token: str = "") -> bytes:
    return (
        json.dumps({"type": "execute", "code": code, "strict_json": strict_json, "auth_token": auth_token}) + "\0"
    ).encode("utf-8")


def _recv_response(sock: socket.socket, timeout: float = 5.0) -> dict:
    """Read one null-delimited JSON response from the socket."""
    sock.settimeout(timeout)
    buf = bytearray()
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            raise AssertionError("server closed the connection before responding")
        buf.extend(chunk)
        if b"\0" in buf:
            break
    return json.loads(buf.split(b"\0", 1)[0])


class TestMCPServerBlocking:
    def test_roundtrip(self, server):
        """poll_blocking serves one request and returns the executed result."""
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(_request("result = {'ok': True, 'value': 42}"))

        assert server.poll_blocking(timeout=2.0) is True
        response = _recv_response(client)

        assert response["status"] == "ok"
        assert response["result"] == {"ok": True, "value": 42}
        client.close()

    def test_stdout_is_captured(self, server):
        """Printed output is included in the response."""
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(_request("print('hello from the bridge')\nresult = {}"))

        assert server.poll_blocking(timeout=2.0) is True
        response = _recv_response(client)

        assert response["status"] == "ok"
        assert "hello from the bridge" in response["stdout"]
        client.close()

    def test_completed_deferred_request_is_returned(self, server):
        """Background mode accepts a deferred callback that is already complete."""
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(_request("def check_is_finished():\n    return {'done': True}", strict_json=True))

        assert server.poll_blocking(timeout=2.0) is True
        response = _recv_response(client)

        assert response == {"status": "ok", "result": {"done": True}}
        client.close()

    def test_pending_deferred_request_is_rejected(self, server):
        """Background mode still rejects work that needs event-loop polling."""
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(_request("def check_is_finished():\n    return None"))

        assert server.poll_blocking(timeout=2.0) is True
        response = _recv_response(client)

        assert response["status"] == "error"
        assert "did not complete synchronously" in response["message"]
        client.close()

    def test_bad_json_returns_error_response(self, server):
        """Malformed request bytes produce an error response, not a crash."""
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(b"not json at all\0")

        server.poll_blocking(timeout=2.0)
        response = _recv_response(client)

        assert response["status"] == "error"
        client.close()

    def test_no_connection_times_out(self, server):
        """poll_blocking returns False when nothing connects within the timeout."""
        start = time.monotonic()
        assert server.poll_blocking(timeout=0.1) is False
        assert time.monotonic() - start < 1.0

    def test_multiple_requests_on_one_connection_are_rejected(self, server):
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(_request("result = {'first': True}") + _request("result = {'second': True}"))

        assert server.poll_blocking(timeout=2.0) is False
        response = _recv_response(client)

        assert response == {"status": "error", "message": "Only one request is allowed per connection"}
        client.close()


class TestMCPServerInteractive:
    def test_poll_roundtrip(self, server):
        """The non-blocking poll() loop services a connected client."""
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(_request("result = {'mode': 'interactive'}"))

        response = None
        deadline = time.monotonic() + 5.0
        while time.monotonic() < deadline:
            server.poll()
            try:
                response = _recv_response(client, timeout=0.05)
                break
            except (TimeoutError, socket.timeout):
                continue
        assert response is not None
        assert response["status"] == "ok"
        assert response["result"] == {"mode": "interactive"}
        client.close()

    def test_oversized_request_is_rejected(self, server):
        """A request larger than MAX_REQUEST_BYTES is rejected with an error."""
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=10)
        # Send from a thread — each poll() only drains 8 KiB, so the server
        # must keep polling while the sender is still pushing bytes.
        send_errors = []

        def _send():
            try:
                client.sendall(b"x" * (MAX_REQUEST_BYTES + 1))
            except OSError as ex:  # the server closes the socket on rejection
                send_errors.append(ex)

        sender = threading.Thread(target=_send)
        sender.start()

        buf = bytearray()
        deadline = time.monotonic() + 10.0
        while time.monotonic() < deadline and b"\0" not in buf:
            server.poll()
            readable, _, _ = select.select([client], [], [], 0)
            if readable:
                try:
                    chunk = client.recv(65536)
                except OSError:
                    chunk = b""
                buf.extend(chunk)
        sender.join(timeout=5)
        client.close()

        assert b"\0" in buf, f"no response received, buffer={len(buf)} bytes, send_errors={send_errors}"
        response = json.loads(buf.split(b"\0", 1)[0])
        assert response["status"] == "error"
        assert "exceeds" in response["message"]

    def test_deferred_request_roundtrip(self, server):
        """A deferred executor result is gathered and sent on a later poll."""
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(_request("def check_is_finished():\n    return {'done': True}"))

        response = None
        deadline = time.monotonic() + 5.0
        while time.monotonic() < deadline:
            server.poll()
            try:
                response = _recv_response(client, timeout=0.05)
                break
            except (TimeoutError, socket.timeout):
                continue

        client.close()
        assert response["status"] == "ok"
        assert response["result"] == {"done": True}

    def test_pending_deferred_operation_is_not_counted_as_work(self, server):
        """A deferred operation that is still running must not hold the active timer interval."""
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(_request("def check_is_finished():\n    return None"))
        server.poll()
        assert len(server.deferred.clients) == 1

        # The operation is registered but has produced no result yet, so there is
        # nothing to do: the timer is free to back off to its idle interval.
        assert server.poll() is False
        assert server.deferred.pending() is True
        client.close()

    def test_receiving_chunks_does_not_refresh_client_deadline(self, server):
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        client.sendall(b'{"type": "execute",')
        server.poll()
        assert len(server.state.clients) == 1
        server.state.clients[0].deadline -= 1.0
        first_deadline = server.state.clients[0].deadline

        client.sendall(b' "code": "result = {}",')
        initial_buffer_size = len(server.state.clients[0].buffer)
        deadline = time.monotonic() + 1.0
        while len(server.state.clients[0].buffer) == initial_buffer_size and time.monotonic() < deadline:
            server.poll()

        assert len(server.state.clients[0].buffer) > initial_buffer_size
        # Receiving progress must not extend the absolute request deadline;
        # otherwise a slowloris client can keep a connection alive forever.
        assert server.state.clients[0].deadline == first_deadline
        client.close()

    def test_response_send_advances_without_blocking_across_polls(self):
        class PartialSendConnection:
            def __init__(self):
                self.blocking = None
                self.closed = False
                self.sent = bytearray()
                self.outcomes = [3, BlockingIOError(), None]

            def setblocking(self, value):
                self.blocking = value

            def send(self, data):
                outcome = self.outcomes.pop(0)
                if isinstance(outcome, BaseException):
                    raise outcome
                size = len(data) if outcome is None else outcome
                self.sent.extend(data[:size])
                return size

            def close(self):
                self.closed = True

        instance = MCPServer()
        connection = PartialSendConnection()
        expected = encode_response({"status": "ok", "value": "response"})

        instance._queue_response(connection, {"status": "ok", "value": "response"})
        assert connection.blocking is False

        assert instance._flush_responses() is True
        assert bytes(connection.sent) == expected[:3]
        assert connection.closed is False
        assert instance._flush_responses() is False
        assert connection.closed is False
        assert instance._flush_responses() is True
        assert bytes(connection.sent) == expected
        assert connection.closed is True
        assert instance.state.responses == []

    def test_stalled_response_is_closed_after_deadline(self, capsys):
        class StalledConnection:
            def __init__(self):
                self.closed = False

            def setblocking(self, _value):
                pass

            def send(self, _data):
                raise BlockingIOError

            def close(self):
                self.closed = True

        instance = MCPServer()
        connection = StalledConnection()
        instance._queue_response(connection, {"status": "ok"})
        instance.state.responses[0].deadline = 0.0

        assert instance._flush_responses() is True
        assert connection.closed is True
        assert instance.state.responses == []
        assert "response send timed out" in capsys.readouterr().err


class TestMCPServerLifecycle:
    def test_restart_on_same_port_after_serving_requests(self, server):
        port = _port(server)
        for _ in range(3):
            with socket.create_connection(("127.0.0.1", port), timeout=5) as client:
                client.sendall(_request("result = {'ok': True}"))
                assert server.poll_blocking(timeout=2.0)
                assert _recv_response(client)["status"] == "ok"
            server.stop()
            server.start(port=port)

    def test_start_twice_raises(self, server):
        with pytest.raises(RuntimeError, match="already running"):
            server.start()

    def test_stop_closes_socket(self, server):
        assert server.is_running() is True
        server.stop()
        assert server.is_running() is False
        # poll_blocking and poll are no-ops without a listening socket.
        assert server.poll_blocking(timeout=0.05) is False
        assert server.poll() is False

    def test_stop_closes_connected_clients(self, server):
        client = socket.create_connection(("127.0.0.1", _port(server)), timeout=5)
        # Send an incomplete request so the client stays in the active list.
        client.sendall(b'{"type": "execu')
        for _ in range(10):
            server.poll()

        assert server.state.clients
        server.stop()
        assert server.state.clients == []

    def test_bind_failure_does_not_leave_server_running(self):
        blocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        blocker.bind(("127.0.0.1", 0))
        blocker.listen(1)
        instance = MCPServer(host="127.0.0.1", port=blocker.getsockname()[1])
        try:
            with pytest.raises(OSError):
                instance.start()
            assert instance.is_running() is False
        finally:
            blocker.close()

    def test_non_loopback_binding_requires_token(self):
        instance = MCPServer(host="0.0.0.0", port=0)

        with pytest.raises(ValueError, match="authentication token"):
            instance.start()

        assert instance.is_running() is False

    def test_configured_token_is_required(self):
        instance = MCPServer(host="127.0.0.1", port=0, token="secret")
        instance.start()
        try:
            for token, expected_status in [("wrong", "error"), ("secret", "ok")]:
                client = socket.create_connection(("127.0.0.1", _port(instance)), timeout=5)
                client.sendall(_request("result = {'ok': True}", auth_token=token))
                assert instance.poll_blocking(timeout=2.0) is True
                assert _recv_response(client)["status"] == expected_status
                client.close()
        finally:
            instance.stop()


@pytest.mark.parametrize("blocking", [False, True])
@pytest.mark.parametrize("enabled", [False, True])
def test_console_logging_respects_switch_and_precedes_execution(server, capsys, monkeypatch, blocking, enabled):
    server.logging = enabled
    server.token = "logging-test-secret"
    execute = server.executor.execute_from_request
    before_execution = []

    def observed_execute(*args):
        before_execution.append(capsys.readouterr().err)
        return execute(*args)

    monkeypatch.setattr(type(server.executor), "execute_from_request", staticmethod(observed_execute))
    with socket.create_connection(("127.0.0.1", _port(server)), timeout=5) as client:
        client.sendall(_request("result = {'logged': True}", auth_token=server.token))
        if blocking:
            assert server.poll_blocking(timeout=2.0)
        else:
            deadline = time.monotonic() + 5
            while not before_execution and time.monotonic() < deadline:
                server.poll()
            server.poll()
        assert _recv_response(client)["result"] == {"logged": True}

    assert len(before_execution) == 1
    response_log = capsys.readouterr().err
    if enabled:
        assert "Forge request:" in before_execution[0]
        assert '"auth_token": "***"' in before_execution[0]
        assert "Forge response:" in response_log
    else:
        assert before_execution[0] == response_log == ""
    assert server.token not in before_execution[0] + response_log


class TestRequestFraming:
    def test_request_logging_redacts_authentication_token(self):
        request = json.dumps({"type": "execute", "auth_token": "top-secret"}).encode()

        logged = MCPServer._request_for_log(request)

        assert "top-secret" not in logged
        assert '"auth_token": "***"' in logged

    def test_extract_request_data_pipelining(self):
        buf = bytearray(b'{"a": 1}\0{"b": 2}\0partial')

        assert MCPServer._extract_request_data(buf) == b'{"a": 1}'
        assert MCPServer._extract_request_data(buf) == b'{"b": 2}'
        assert MCPServer._extract_request_data(buf) is None
        assert bytes(buf) == b"partial"
