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

"""Exercise every Forge model type and declared subtype through MCP.

This is intentionally separate from the small smoke E2E driver.  It launches
an isolated Blender bridge, creates every supported element/subtype, edits each
created object through the public MCP editing tools, and reports a compact
pass/fail matrix.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import secrets
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[3]
SERVER = ROOT / "mcp-server"
BOOTSTRAP = Path(__file__).with_name("_bridge_full_setup.py")


def discover_blender() -> str | None:
    if found := shutil.which("blender"):
        return found
    roots = [
        Path(os.environ.get("PROGRAMFILES", r"C:\\Program Files")),
        Path(os.environ.get("PROGRAMFILES(X86)", r"C:\\Program Files (x86)")),
    ]
    candidates = []
    for root in roots:
        for exe in (root / "Blender Foundation").glob("Blender*/blender.exe"):
            candidates.append((tuple(int(n) for n in re.findall(r"\d+", exe.parent.name)) or (0,), exe))
    return str(max(candidates, key=lambda x: ((x[0][0] == 4), x[0]))[1]) if candidates else None


def wait_port(port: int, proc: subprocess.Popen, timeout: float = 120) -> bool:
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        if proc.poll() is not None:
            return False
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                return True
        except OSError:
            time.sleep(1)
    return False


class Matrix:
    def __init__(self, blender: str, port: int):
        self.blender, self.port = blender, port
        self.proc: subprocess.Popen | None = None
        self.token = secrets.token_hex(32)
        self.instance_id = secrets.token_hex(32)
        self.log = tempfile.TemporaryFile(mode="w+b")
        self.failures: list[str] = []
        self.results: list[tuple[str, str]] = []
        self.tmp = tempfile.TemporaryDirectory(prefix="forge-mcp-matrix-")
        self.external = Path(self.tmp.name) / "external.xml"
        self.external.write_text(
            '<mujoco model="external"><worldbody><body name="external_base" /></worldbody></mujoco>', encoding="utf-8"
        )

    def start(self) -> None:
        # Do not preflight-connect here: on Windows a localhost probe can
        # itself fail with a permission/timeout error, and it is racy anyway.
        # The per-run token and PID/instance verification below provide the
        # actual ownership check after the child bridge is reachable.
        env = {
            **os.environ,
            "FORGE_E2E_PORT": str(self.port),
            "FORGE_MCP_TOKEN": self.token,
            "FORGE_E2E_INSTANCE": self.instance_id,
        }
        self.proc = subprocess.Popen(
            [self.blender, "--background", "--factory-startup", "--python", str(BOOTSTRAP)],
            env=env,
            stdout=self.log,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if not wait_port(self.port, self.proc):
            self._stop_process()
            self.log.seek(0, os.SEEK_END)
            self.log.seek(max(0, self.log.tell() - 4000))
            output = self.log.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"full bridge did not start:\n{output}")

    def _stop_process(self) -> None:
        if self.proc is not None and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait(timeout=10)

    def stop(self) -> None:
        try:
            self._stop_process()
        finally:
            self.log.close()
            self.tmp.cleanup()

    async def verify_instance(self, session: ClientSession) -> None:
        identity = await self.call(
            session,
            "forge_execute",
            code="import os\nresult = {'pid': os.getpid(), 'instance': os.environ.get('FORGE_E2E_INSTANCE')}",
        )
        if (
            self.proc is None
            or self.proc.poll() is not None
            or identity.get("pid") != self.proc.pid
            or identity.get("instance") != self.instance_id
        ):
            raise RuntimeError("Refusing to modify Blender: bridge does not belong to this test")

    async def call(self, session: ClientSession, tool_name: str, **kwargs):
        response = await session.call_tool(tool_name, kwargs)
        text = response.content[0].text if response.content else ""
        if getattr(response, "is_error", False):
            raise RuntimeError(text)
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"raw": text}

    async def reset(self, session: ClientSession) -> None:
        await self.call(
            session,
            "forge_execute",
            code="""import bpy
ret = bpy.ops.wm.read_homefile(use_factory_startup=True)
if 'FINISHED' not in ret: raise RuntimeError(ret)
bpy.ops.object.select_all(action='DESELECT')
result = {'ok': True}
""",
        )

    async def create(self, session: ClientSession, label: str, tool: str, expected: str, **kwargs) -> list[str]:
        try:
            data = await self.call(session, tool, **kwargs)
            names = data.get("created", [])
            if not isinstance(names, list) or not names:
                raise RuntimeError(f"created empty: {data}")
            actual_types = []
            for name in names:
                info = await self.call(session, "forge_object_info", name=name)
                actual = info.get("type") or info.get("Forge_Model_Type")
                actual_types.append(actual)
                # Attach imports the referenced subtree as ordinary Forge
                # objects and also creates the ATTACH reference.  The first
                # returned object can therefore be a LINK rather than the
                # reference itself.
                if actual != expected and not (expected == "ATTACH" and actual != "UNDEFINED"):
                    raise RuntimeError(f"type={actual!r}, expected={expected!r} ({info})")
                await self.edit(session, label, name, info)
            if expected == "ATTACH" and expected not in actual_types:
                raise RuntimeError(f"attach reference missing from created objects: {actual_types}")
            self.results.append((label, "PASS"))
            return names
        except Exception as exc:  # noqa: BLE001
            self.results.append((label, f"FAIL: {exc}"))
            self.failures.append(label)
            return []

    async def edit(self, session: ClientSession, label: str, name: str, info: dict) -> None:
        transform = await self.call(
            session, "forge_set_transform", name=name, location=(0.1, 0.2, 0.3), rotation_euler=(0.05, 0.0, 0.0)
        )
        if transform.get("name") != name:
            raise RuntimeError(f"transform did not target {name}: {transform}")
        props = info.get("props") or {}
        candidates = [
            ("mocap", not bool(props.get("mocap", False))),
            ("mass", float(props.get("mass", 1.0)) + 0.25),
            ("damping", float(props.get("damping", 0.0)) + 0.1),
            ("stiffness", float(props.get("stiffness", 0.0)) + 0.1),
            ("gap", float(props.get("gap", 0.0)) + 0.01),
            ("count", int(props.get("count", 0)) + 1),
        ]
        for key, value in candidates:
            if key in props:
                edited = await self.call(session, "forge_set_property", name=name, values={key: value})
                if key not in edited.get("set", {}):
                    raise RuntimeError(f"property {key} not set: {edited}")
                return

    async def run(self) -> int:
        env = {
            **os.environ,
            # The bridge uses AF_INET, so connect directly without IPv6 fallback.
            "FORGE_MCP_HOST": "127.0.0.1",
            "FORGE_MCP_PORT": str(self.port),
            "FORGE_MCP_TOKEN": self.token,
        }
        params = StdioServerParameters(command=sys.executable, args=["-m", "forge_mcp"], cwd=str(SERVER), env=env)
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                await self.verify_instance(session)
                for skill in ("create", "modify"):
                    await self.call(session, "forge_skill", name=skill)

                await self.reset(session)
                link = (await self.create(session, "LINK", "forge_create_link", "LINK"))[0]
                link2 = (await self.create(session, "LINK/child", "forge_create_link", "LINK", select=[link]))[0]
                await self.create(session, "FRAME", "forge_create_frame", "FRAME", select=[link])
                visuals = []
                for shape in ("BOX", "CAPSULE", "CYLINDER", "SPHERE"):
                    visuals += await self.create(
                        session,
                        f"VISUAL/{shape}",
                        "forge_create_geometry",
                        "VISUAL",
                        geometry_type=shape,
                        select=[link],
                    )
                # GEOMETRY_TYPE intentionally follows the selected visual's
                # shape.  Create a real mesh visual separately so the MESH
                # collider case exercises the explicit COLLIDER_TYPE path
                # instead of silently producing a BOX collider from visuals[0].
                raw_mesh = await self.call(
                    session,
                    "forge_execute",
                    code="""import bpy
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.mesh.primitive_cube_add()
result = {'name': bpy.context.object.name}
""",
                )
                defined_mesh = await self.call(
                    session, "forge_define_model_type", model_type="VISUAL", select=[raw_mesh["name"]]
                )
                mesh_visual = (defined_mesh.get("objects") or [raw_mesh["name"]])[0]
                for shape in ("BOX", "CAPSULE", "CYLINDER", "SPHERE", "MESH"):
                    args = {
                        "collider_type": shape,
                        "create_method": "COLLIDER_TYPE",
                        "select": [mesh_visual] if shape == "MESH" else [link],
                    }
                    made = await self.create(session, f"COLLIDER/{shape}", "forge_create_collider", "COLLIDER", **args)
                    if shape == "MESH" and made:
                        info = await self.call(session, "forge_object_info", name=made[0])
                        if (info.get("props") or {}).get("type") != "MESH":
                            raise RuntimeError(f"MESH collider has wrong geometry type: {info}")
                for shape in ("BOX", "CAPSULE", "CYLINDER", "SPHERE"):
                    await self.create(
                        session, f"SITE/{shape}", "forge_create_site", "SITE", site_type=shape, select=[link]
                    )
                await self.create(session, "HFIELD", "forge_create_height_field", "HFIELD", select=[])
                await self.create(session, "PLANE", "forge_create_plane", "PLANE", select=[])

                joints = []
                for subtype in ("FREE", "BALL", "SLIDE", "HINGE"):
                    made = await self.create(
                        session, f"JOINT/{subtype}", "forge_create_joint", "JOINT", joint_type=subtype, select=[link]
                    )
                    joints += made
                # Geometry-node visuals are intentionally lightweight in headless
                # mode and have no mesh faces.  Build one real cube through MCP,
                # define it as VISUAL, parent it to a dedicated link, then test
                # the inertia operator against that valid mesh.
                inertia_link = (await self.create(session, "LINK/inertia", "forge_create_link", "LINK", select=[]))[0]
                raw = await self.call(
                    session,
                    "forge_execute",
                    code="""import bpy
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.mesh.primitive_cube_add()
result = {'name': bpy.context.object.name}
""",
                )
                defined = await self.call(session, "forge_define_model_type", model_type="VISUAL", select=[raw["name"]])
                inertia_visual = (defined.get("objects") or [raw["name"]])[0]
                await self.call(session, "forge_define_parent", select=[inertia_link, inertia_visual])
                await self.create(session, "INERTIAL", "forge_create_inertial", "INERTIAL", select=[inertia_link])
                for subtype in ("GENERAL", "MOTOR", "POSITION", "VELOCITY", "ADHESION"):
                    await self.create(
                        session,
                        f"ACTUATOR/{subtype}",
                        "forge_create_actuator",
                        "ACTUATOR",
                        actuator_type=subtype,
                        select=[joints[-1]],
                    )
                for subtype in ("FIXED",):
                    await self.create(
                        session,
                        f"TENDON/{subtype}",
                        "forge_create_tendon",
                        "TENDON",
                        tendon_type=subtype,
                        select=joints[-2:],
                    )

                # Equality and contact cover each declared subtype.
                sites = await self.call(session, "forge_scene_info")
                objects = sites.get("objects", [])
                object_names = [item["name"] for item in objects if isinstance(item, dict) and "name" in item]
                site_names = [item["name"] for item in objects if isinstance(item, dict) and item.get("type") == "SITE"]
                if len(site_names) >= 2:
                    for subtype in ("CONNECT", "WELD"):
                        await self.create(
                            session,
                            f"EQUALITY/{subtype}",
                            "forge_create_equality",
                            "EQUALITY",
                            equality_type=subtype,
                            select=site_names[:2],
                        )
                await self.create(
                    session,
                    "EQUALITY/JOINT",
                    "forge_create_equality",
                    "EQUALITY",
                    equality_type="JOINT",
                    select=joints[-2:],
                )
                if len(object_names) >= 2:
                    for subtype in ("EXCLUDE", "PAIR"):
                        sel = (
                            [link, link2]
                            if subtype == "EXCLUDE"
                            else [
                                item["name"]
                                for item in objects
                                if isinstance(item, dict)
                                and item.get("type") in {"VISUAL", "COLLIDER", "PLANE", "HFIELD"}
                            ][:2]
                        )
                        await self.create(
                            session,
                            f"CONTACT/{subtype}",
                            "forge_create_contact",
                            "CONTACT",
                            contact_type=subtype,
                            select=sel,
                        )

                # Sensor enum is target-dependent; exercise all 17 identifiers with valid target contexts.
                sensor_targets = {
                    "JOINTpos": ("Jointpos", joints[-1], {}),
                    "JOINTvel": ("Jointvel", joints[-1], {}),
                    "Touch": ("Touch", site_names[0] if site_names else link, {}),
                    "Accelerometer": ("Accelerometer", site_names[0] if site_names else link, {}),
                    "Velocimeter": ("Velocimeter", site_names[0] if site_names else link, {}),
                    "Gyro": ("Gyro", site_names[0] if site_names else link, {}),
                    "Framepos": ("Framepos", link, {}),
                    "Framequat": ("Framequat", link, {}),
                    "Framexaxis": ("Framexaxis", link, {}),
                    "Frameyaxis": ("Frameyaxis", link, {}),
                    "Framezaxis": ("Framezaxis", link, {}),
                    "Framelinvel": ("Framelinvel", link, {}),
                    "Frameangvel": ("Frameangvel", link, {}),
                    "Contact": ("Contact", link, {}),
                    # Subtree* sensors target a LINK in the default BODY
                    # context.  set_subtree=True is reserved for Contact.
                    "Subtreecom": ("Subtreecom", link, {}),
                    "Subtreelinvel": ("Subtreelinvel", link, {}),
                    "Subtreeangmom": ("Subtreeangmom", link, {}),
                }
                for label, (subtype, target, extra) in sensor_targets.items():
                    await self.create(
                        session,
                        f"SENSOR/{label}",
                        "forge_create_sensor",
                        "SENSOR",
                        sensor_type=subtype,
                        select=[target],
                        **extra,
                    )

                for light_type in ("DIRECTIONAL", "SPOT", "POINT"):
                    for mode in ("FIXED", "TRACK", "TRACKCOM"):
                        await self.create(
                            session,
                            f"LIGHT/{light_type}/{mode}",
                            "forge_create_light",
                            "LIGHT",
                            light_type=light_type,
                            light_mode=mode,
                            select=[],
                        )
                for camera_type in ("PERSPECTIVE", "ORTHOGRAPHIC"):
                    for mode in ("FIXED", "TRACK", "TRACKCOM"):
                        await self.create(
                            session,
                            f"CAMERA/{camera_type}/{mode}",
                            "forge_create_camera",
                            "CAMERA",
                            camera_type=camera_type,
                            camera_mode=mode,
                            select=[],
                        )
                await self.create(session, "REPLICATE", "forge_create_replicate", "REPLICATE", count=2, select=[link])
                await self.create(
                    session, "INCLUDE", "forge_create_include", "INCLUDE", file=str(self.external), select=[]
                )
                # Include and attach are independent modal operations.  Reset
                # between them so a just-finished include cannot retain the
                # scene-level modal slot while the next operation starts.
                await self.reset(session)
                await self.create(
                    session, "ATTACH", "forge_create_attach", "ATTACH", file=str(self.external), select=[]
                )

                # Undefined is Blender's pre-definition state; verify it remains editable through MCP.
                raw = await self.call(
                    session,
                    "forge_execute",
                    code="""import bpy
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.empty_add(type='PLAIN_AXES')
result = {'name': bpy.context.object.name, 'type': bpy.context.object.Forge_Model_Type}
""",
                )
                if raw.get("type") != "UNDEFINED":
                    self.failures.append("UNDEFINED")
                    self.results.append(("UNDEFINED", f"FAIL: {raw}"))
                else:
                    await self.edit(session, "UNDEFINED", raw["name"], {"props": {}})
                    self.results.append(("UNDEFINED", "PASS"))

        for label, status in self.results:
            print(f"  [{status}] {label}")
        print(
            f"\nmodel matrix: {'FAILED' if self.failures else 'PASSED'} "
            f"({len(self.results)} cases, {len(self.failures)} failures)"
        )
        return 1 if self.failures else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blender", default=os.environ.get("FORGE_BLENDER") or discover_blender())
    parser.add_argument("--port", type=int, default=int(os.environ.get("FORGE_E2E_PORT", "9878")))
    args = parser.parse_args()
    if not args.blender or not Path(args.blender).exists():
        raise SystemExit(f"Blender not found: {args.blender!r}")
    matrix = Matrix(args.blender, args.port)
    try:
        matrix.start()
        return asyncio.run(matrix.run())
    finally:
        matrix.stop()


if __name__ == "__main__":
    raise SystemExit(main())
