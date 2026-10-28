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

"""End-to-end driver for forge-mcp against a live (headless) Blender + Forge bridge.

Tier 3 of the test plan. Spawns its own headless Blender 4.5 with the Forge
addon bridge on ``FORGE_E2E_PORT`` (default 9877 — never the live 9876), spawns
the forge-mcp server over stdio pointing at that port, and drives a set of real
``bpy.ops.forge.*`` scenarios through the MCP protocol, asserting on the
results. Requires Blender 4.5 and the ``addon`` directory in this repo.

Usage:
    python tests/mcp/e2e/driver.py [--blender PATH] [--port 9877]
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

REPO_ROOT = Path(__file__).resolve().parents[3]
SERVER_DIR = REPO_ROOT / "mcp-server"
ADDON_DIR = REPO_ROOT / "addon"
BRIDGE_SCRIPT = Path(__file__).resolve().parent / "_bridge_setup.py"


def _parse_version(name: str) -> tuple[int, ...]:
    return tuple(int(n) for n in re.findall(r"\d+", name)) or (0,)


def _discover_blender() -> str | None:
    """Locate a Blender binary on this system: PATH first, then standard install dirs.

    Prefers a 4.x install (the Forge suite is verified on 4.5), falling back to
    the highest version found otherwise.
    """
    if found := shutil.which("blender"):
        return found

    roots = [
        Path(os.environ.get("PROGRAMFILES", r"C:\Program Files")),
        Path(os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)")),
    ]
    candidates: list[tuple[tuple[int, ...], Path]] = []
    for root in roots:
        base = root / "Blender Foundation"
        if not base.is_dir():
            continue
        for exe in base.glob("Blender*/blender.exe"):
            version = _parse_version(exe.parent.name.removeprefix("Blender").strip())
            candidates.append((version, exe))
    if not candidates:
        return None
    candidates.sort(key=lambda c: (c[0][0] == 4, c[0]), reverse=True)
    return str(candidates[0][1])


def _wait_port(port: int, timeout: float = 120.0) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                return True
        except OSError:
            time.sleep(1)
    return False


class E2E:
    def __init__(self, blender: str | None, port: int):
        self.blender = blender
        self.port = port
        self.blender_proc: subprocess.Popen | None = None

    def start(self) -> None:
        blender = self.blender or _discover_blender()
        if not blender or not Path(blender).exists():
            raise SystemExit(
                f"Blender not found (auto-discovery gave {blender!r}); install Blender or set --blender / FORGE_BLENDER"
            )
        self.blender = blender
        if not ADDON_DIR.exists():
            raise SystemExit(f"Forge addon not found: {ADDON_DIR}")

        env = {**os.environ, "FORGE_E2E_PORT": str(self.port)}
        print(f"[bridge] {self.blender} --background --factory-startup --python {BRIDGE_SCRIPT}")
        self.blender_proc = subprocess.Popen(
            [self.blender, "--background", "--factory-startup", "--python", str(BRIDGE_SCRIPT)],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if not _wait_port(self.port):
            out = ""
            if self.blender_proc.stdout:
                out = self.blender_proc.stdout.read()
            raise SystemExit(f"bridge did not come up on port {self.port}:\n{out[-2000:]}")

    def stop(self) -> None:
        if self.blender_proc is not None:
            try:
                self.blender_proc.terminate()
                self.blender_proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.blender_proc.kill()

    async def run(self) -> int:
        # The bridge listens on AF_INET; avoid IPv6 localhost fallback delays.
        env = {**os.environ, "FORGE_MCP_HOST": "127.0.0.1", "FORGE_MCP_PORT": str(self.port)}
        params = StdioServerParameters(command=sys.executable, args=["-m", "forge_mcp"], cwd=str(SERVER_DIR), env=env)
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                # Blender operations are guarded by the corresponding skill
                # contract; load the guides before the first scene reset or
                # create/modify operation.
                for skill_name in ("create", "modify"):
                    guide = await session.call_tool("forge_skill", {"name": skill_name})
                    if getattr(guide, "is_error", False):
                        text = guide.content[0].text if guide.content else ""
                        raise RuntimeError(f"failed to load {skill_name} skill: {text}")
                tool_names = {t.name for t in (await session.list_tools()).tools}
                required = [n for n, _, _ in _SCENARIOS] + ["forge_import_mjcf", "forge_export_mjcf"]
                missing = [name for name in required if name not in tool_names]
                if missing:
                    raise SystemExit(f"tools missing: {missing}")

                failures: list[tuple[str, str]] = []
                for name, kwargs, validate in _SCENARIOS:
                    await self._reset_scene(session)
                    ok, text = await self._call(session, name, kwargs)
                    detail = None
                    if ok:
                        try:
                            data = json.loads(text)
                        except json.JSONDecodeError:
                            data = {"raw": text[:200]}
                        detail = validate(data)
                    else:
                        detail = text[:200]
                    status = "PASS" if detail is None else f"FAIL: {detail}"
                    if detail is not None:
                        failures.append((name, status))
                    print(f"  [{status}] {name}")
                failures += await self._run_background_io(session)
                return 1 if failures else 0

    async def _run_background_io(self, session: ClientSession) -> list[tuple[str, str]]:
        """Round-trip a minimal MJCF through the background bridge."""
        failures: list[tuple[str, str]] = []
        with tempfile.TemporaryDirectory(prefix="forge-mcp-e2e-") as directory:
            input_path = Path(directory) / "background-input.xml"
            output_path = Path(directory) / "background-output.xml"
            input_path.write_text(
                '<mujoco model="background"><worldbody><body name="base" /></worldbody></mujoco>',
                encoding="utf-8",
            )
            await self._reset_scene(session)
            cases = [
                (
                    "forge_import_mjcf",
                    {"filepath": str(input_path), "import_material": False},
                    lambda data: (
                        None
                        if data.get("filepath") == str(input_path.resolve()) and data.get("objects", 0) >= 1
                        else f"unexpected import result: {data}"
                    ),
                ),
                (
                    "forge_export_mjcf",
                    {"filepath": str(output_path), "overwrite": True},
                    lambda data: (
                        None
                        if data.get("exists") is True and output_path.is_file()
                        else f"unexpected export result: {data}"
                    ),
                ),
            ]
            for name, kwargs, validate in cases:
                ok, payload = await self._call(session, name, kwargs)
                detail = payload
                if ok:
                    try:
                        detail = validate(json.loads(payload))
                    except json.JSONDecodeError:
                        detail = f"invalid JSON: {payload[:200]}"
                status = "PASS" if detail is None else f"FAIL: {detail}"
                if detail is not None:
                    failures.append((name, status))
                print(f"  [{status}] {name}")
        return failures

    @staticmethod
    async def _reset_scene(session: ClientSession) -> None:
        """Back to the factory startup scene (Camera/Cube/Light), nothing selected.

        ``read_homefile(use_factory_startup=True)`` is allowed by Forge's
        Guardian and preserves the registered Forge classes. Deselect the Cube
        so create ops whose poll requires "no selection" can run.
        """
        code = (
            "import bpy\n"
            "ret = bpy.ops.wm.read_homefile(use_factory_startup=True)\n"
            "if 'FINISHED' not in ret:\n"
            "    raise RuntimeError(f'failed to load factory startup: {ret}')\n"
            "bpy.ops.object.select_all(action='DESELECT')\n"
            "result = {\n"
            "    'ok': True,\n"
            "    'scene': bpy.context.scene.name,\n"
            "    'objects': sorted(obj.name for obj in bpy.context.scene.objects),\n"
            "    'selected': sorted(obj.name for obj in bpy.context.selected_objects),\n"
            "}\n"
        )
        response = await session.call_tool("forge_execute", {"code": code})
        text = response.content[0].text if response.content else ""
        if getattr(response, "is_error", False):
            raise RuntimeError(f"E2E scene reset failed: {text}")
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"E2E scene reset returned invalid JSON: {text[:200]}") from exc
        if (
            payload.get("ok") is not True
            or payload.get("objects") != ["Camera", "Cube", "Light"]
            or payload.get("selected") != []
        ):
            raise RuntimeError(f"E2E scene reset returned an unexpected result: {payload}")

    @staticmethod
    async def _call(session: ClientSession, name: str, kwargs: dict) -> tuple[bool, str]:
        try:
            result = await session.call_tool(name, kwargs)
            if getattr(result, "is_error", False):
                return False, result.content[0].text
            return True, result.content[0].text
        except Exception as exc:  # noqa: BLE001
            return False, f"{type(exc).__name__}: {exc}"


def _has(data: dict, key: str) -> str | None:
    return None if key in data else f"missing key {key!r}; got {sorted(data)[:6]}"


def _has_any(data: dict, keys: list[str]) -> str | None:
    return None if any(k in data for k in keys) else f"none of {keys}; got {sorted(data)[:6]}"


def _created(data: dict) -> str | None:
    created = data.get("created")
    return None if isinstance(created, list) and created else f"created empty/missing; got {sorted(data)[:6]}"


# name -> (kwargs, validator); validator returns None on success else a detail string.
# Validators stay lenient — they pin the transport + operator wiring, not exact props.
_SCENARIOS: list[tuple[str, dict, object]] = [
    ("forge_create_link", {}, _created),
    ("forge_create_plane", {}, _created),
    ("forge_create_height_field", {}, _created),
    (
        "forge_scene_info",
        {},
        lambda d: _has(d, "object_count") if "object_count" in d else _has_any(d, ["objects", "count"]),
    ),
    ("forge_object_info", {"name": "Cube"}, lambda d: _has_any(d, ["Forge_Model_Type", "type", "name"])),
    ("forge_blendfile_summary", {}, lambda d: _has_any(d, ["path", "dirty", "datablocks", "file_path"])),
    ("forge_measure", {"names": ["Cube"]}, lambda d: None if isinstance(d, dict) and d else f"empty result; got {d}"),
    (
        "forge_batch_rename",
        {"new_name": "part", "select": ["Cube"]},
        lambda d: _has_any(d, ["renamed", "objects", "result"]),
    ),
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--blender", default=os.environ.get("FORGE_BLENDER"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("FORGE_E2E_PORT", "9877")))
    args = parser.parse_args()

    e2e = E2E(args.blender, args.port)
    try:
        e2e.start()
        code = asyncio.run(e2e.run())
    finally:
        e2e.stop()
    print(f"\ne2e {'FAILED' if code else 'PASSED'}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
