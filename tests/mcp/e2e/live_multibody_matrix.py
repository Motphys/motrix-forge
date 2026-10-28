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

"""Complex multi-body model creation/edit round-trip against a live Bridge."""

from __future__ import annotations

import asyncio
import json
import os
import shutil
import sys
import tempfile
import uuid
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

PREFIX = "E2E_MB_"

# What the run writes into the file besides objects. Forge keeps the export
# destination and the include / attach pickers on scene-level property groups,
# and opens a collection per model type for the objects it makes; none of that
# goes away when the objects do. Captured before the run, put back after it.
_STATE_CODE = """
import bpy

scene = bpy.context.scene
temp = getattr(scene, "Forge_Temp_Props", None)
result = {
    "forge_props": {
        name: getattr(scene.Forge_Props, name, "")
        for name in ("export_path", "import_file_path", "select_tag")
    },
    "temp_props": {
        name: getattr(temp, name, "")
        for name in ("tmp_file", "tmp_model", "tmp_prefix", "tmp_link")
    } if temp is not None else {},
    "collections": sorted(coll.name for coll in bpy.data.collections),
}
"""

_RESTORE_CODE = """
import bpy

keep = __KEEP__
scene = bpy.context.scene

for name, value in keep["forge_props"].items():
    setattr(scene.Forge_Props, name, value)

temp = getattr(scene, "Forge_Temp_Props", None)
if temp is not None:
    for name, value in keep["temp_props"].items():
        setattr(temp, name, value)

# Forge opens a collection per model type for the rig; deleting the objects
# leaves them behind. Only *empty* ones the run added are removed, so nothing
# the file already held is taken away — this script borrows a live session
# rather than requiring an empty file the way the other matrices do.
dropped = []
for coll in list(bpy.data.collections):
    if coll.name in keep["collections"] or len(coll.objects) or coll.children:
        continue
    dropped.append(coll.name)
    bpy.data.collections.remove(coll)

result = {"restored": sorted(keep["forge_props"]), "collections_dropped": dropped}
"""


async def main() -> int:
    env = {**os.environ, "FORGE_MCP_PORT": os.environ.get("FORGE_MCP_PORT", "9876")}
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=str(Path(__file__).resolve().parents[3] / "mcp-server"),
        env=env,
    )
    # The export writes the XML plus its asset files, so keep both the include
    # file and the export destination in a scratch directory instead of leaving
    # generated output in the source tree.
    work_dir = Path(tempfile.mkdtemp(prefix="forge_live_multibody_"))
    external = work_dir / f"_live_multibody_external_{uuid.uuid4().hex}.xml"
    external.write_text(
        '<mujoco model="multibody_external"><worldbody><body name="external_base" /></worldbody></mujoco>',
        encoding="utf-8",
    )
    # Attach and include are alternative ways to pull an external model in, and
    # a file may not be both in the same scene: the attach task list comes back
    # empty and the operator reports "Attach fail: list index out of range".
    # Give each its own file.
    attach_file = work_dir / f"_live_multibody_attach_{uuid.uuid4().hex}.xml"
    attach_file.write_text(
        '<mujoco model="multibody_attach"><worldbody><body name="attach_base" /></worldbody></mujoco>',
        encoding="utf-8",
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            for skill in ("create", "modify"):
                await session.call_tool("forge_skill", {"name": skill})

            async def call(tool: str, **kwargs):
                response = await session.call_tool(tool, kwargs)
                text = response.content[0].text if response.content else ""
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = {"raw": text}
                if getattr(response, "is_error", False):
                    raise RuntimeError(f"{tool}: {data}")
                return data

            created: list[str] = []
            cases: list[tuple[str, str]] = []
            failures: list[str] = []

            async def make(label: str, tool: str, expected: str, *, any_of: bool = False, **kwargs) -> list[str]:
                """Create and assert the model type of what came back.

                ``any_of`` is for operators that legitimately create more than
                one kind of object — `attach` imports the external body as well —
                where requiring *every* created object to carry ``expected``
                could never hold.
                """
                try:
                    data = await call(tool, **kwargs)
                    names = data.get("created", [])
                    if not names:
                        raise RuntimeError(f"no created objects: {data}")
                    created.extend(names)
                    types = [(name, (await call("forge_object_info", name=name)).get("type")) for name in names]
                    if any_of:
                        if expected not in [actual for _, actual in types]:
                            raise RuntimeError(f"no {expected!r} among {types}")
                    else:
                        for name, actual in types:
                            if actual != expected:
                                raise RuntimeError(f"{name}: type={actual!r}, expected={expected!r}")
                    cases.append((label, "PASS"))
                    return names
                except Exception as exc:  # noqa: BLE001
                    print(f"CREATE {label} ERROR: {exc}")
                    cases.append((label, f"FAIL: {exc}"))
                    failures.append(label)
                    return []

            async def edit(
                label: str, name: str, values: dict[str, object], expected_keys: set[str] | None = None
            ) -> None:
                try:
                    result = await call("forge_set_property", name=name, values=values)
                    landed = set(result.get("set", {}))
                    if expected_keys and not expected_keys.issubset(landed):
                        raise RuntimeError(f"set={landed}, expected={expected_keys}, result={result}")
                    info = await call("forge_object_info", name=name)
                    props = info.get("props") or {}
                    for key, value in values.items():
                        if key in props and key in result.get("set", {}):
                            actual = props[key]
                            if isinstance(value, float) and abs(float(actual) - value) > 1e-5:
                                raise RuntimeError(f"{key}: readback {actual!r} != {value!r}")
                            if isinstance(value, (str, bool, int)) and actual != value:
                                raise RuntimeError(f"{key}: readback {actual!r} != {value!r}")
                    cases.append((label, "PASS"))
                except Exception as exc:  # noqa: BLE001
                    cases.append((label, f"FAIL: {exc}"))
                    failures.append(label)

            # Captured before anything is written, so `finally` can put the
            # scene-level Forge state back. A failure here only costs the
            # restore, not the run, so it is reported and carried on.
            state: dict = {}
            try:
                state = await call("forge_execute", code=_STATE_CODE)
            except Exception as exc:  # noqa: BLE001
                print(f"STATE CAPTURE FAILED (cleanup will be partial): {exc}")

            try:
                # ── Build a multi-body hierarchy ────────────────────────
                root = (await make("LINK/root", "forge_create_link", "LINK", select=[]))[0]
                await call("forge_rename", name_map={root: PREFIX + "Root"})
                created[created.index(root)] = PREFIX + "Root"
                root = PREFIX + "Root"
                link_arm = (await make("LINK/arm", "forge_create_link", "LINK", select=[root]))[0]
                link_tool = (await make("LINK/tool", "forge_create_link", "LINK", select=[link_arm]))[0]
                frame = (await make("FRAME/arm", "forge_create_frame", "FRAME", select=[root]))[0]
                replicate = (
                    await make(
                        "REPLICATE",
                        "forge_create_replicate",
                        "REPLICATE",
                        count=2,
                        sep="_R",
                        offset=(0.4, 0, 0),
                        select=[frame],
                    )
                )[0]

                # Four geometry subtypes under root; collider types under arm.
                visuals: dict[str, str] = {}
                for shape in ("BOX", "CAPSULE", "CYLINDER", "SPHERE"):
                    made = await make(
                        f"VISUAL/{shape}", "forge_create_geometry", "VISUAL", geometry_type=shape, select=[root]
                    )
                    if made:
                        visuals[shape] = made[0]
                colliders: dict[str, str] = {}
                for shape in ("BOX", "CAPSULE", "CYLINDER", "SPHERE"):
                    made = await make(
                        f"COLLIDER/{shape}",
                        "forge_create_collider",
                        "COLLIDER",
                        collider_type=shape,
                        create_method="COLLIDER_TYPE",
                        select=[link_arm],
                    )
                    if made:
                        colliders[shape] = made[0]
                # MESH collider is derived from a visual.
                made = await make(
                    "COLLIDER/MESH",
                    "forge_create_collider",
                    "COLLIDER",
                    collider_type="MESH",
                    create_method="GEOMETRY_TYPE",
                    select=[visuals["BOX"]],
                )
                if made:
                    colliders["MESH"] = made[0]

                sites: dict[str, str] = {}
                for shape in ("BOX", "CAPSULE", "CYLINDER", "SPHERE"):
                    made = await make(f"SITE/{shape}", "forge_create_site", "SITE", site_type=shape, select=[link_tool])
                    if made:
                        sites[shape] = made[0]
                hfield = (await make("HFIELD", "forge_create_height_field", "HFIELD", select=[]))[0]
                plane = (await make("PLANE", "forge_create_plane", "PLANE", select=[]))[0]

                # Real mesh visual on a dedicated branch for inertial
                # computation.  Other primitives intentionally remain in the
                # multibody scene, but are spatially overlapping by default;
                # inertia validation must scope to a non-intersecting branch.
                inertia_link = (await make("LINK/inertia", "forge_create_link", "LINK", select=[link_tool]))[0]
                raw = await call(
                    "forge_execute",
                    code="""import bpy
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.mesh.primitive_cube_add(location=(4.0, 0.0, 0.0))
result = {'name': bpy.context.object.name}
""",
                )
                mesh_name = raw["name"]
                defined = await call("forge_define_model_type", model_type="VISUAL", select=[mesh_name])
                mesh_visual = (defined.get("objects") or [mesh_name])[0]
                created.append(mesh_visual)
                await call("forge_define_parent", select=[inertia_link, mesh_visual])
                inertia = await make("INERTIAL/root", "forge_create_inertial", "INERTIAL", select=[inertia_link])

                # Joint subtypes on the arm link; each is later used by
                # actuator/equality/tendon relationships.
                joints: dict[str, str] = {}
                for subtype in ("FREE", "BALL", "SLIDE", "HINGE"):
                    made = await make(
                        f"JOINT/{subtype}", "forge_create_joint", "JOINT", joint_type=subtype, select=[link_arm]
                    )
                    if made:
                        joints[subtype] = made[0]

                # Actuator subtypes target a hinge joint.
                actuators: dict[str, str] = {}
                for subtype in ("GENERAL", "MOTOR", "POSITION", "VELOCITY", "ADHESION"):
                    made = await make(
                        f"ACTUATOR/{subtype}",
                        "forge_create_actuator",
                        "ACTUATOR",
                        actuator_type=subtype,
                        select=[joints["HINGE"]],
                    )
                    if made:
                        actuators[subtype] = made[0]
                tendon = (
                    await make(
                        "TENDON/FIXED",
                        "forge_create_tendon",
                        "TENDON",
                        tendon_type="FIXED",
                        select=[joints["SLIDE"], joints["HINGE"]],
                    )
                )[0]
                equality = {}
                for subtype, selection in (
                    ("CONNECT", [root, link_arm]),
                    ("WELD", [root, link_tool]),
                    ("JOINT", [joints["SLIDE"], joints["HINGE"]]),
                ):
                    made = await make(
                        f"EQUALITY/{subtype}",
                        "forge_create_equality",
                        "EQUALITY",
                        equality_type=subtype,
                        select=selection,
                    )
                    if made:
                        equality[subtype] = made[0]
                _contact_exclude = (
                    await make(
                        "CONTACT/EXCLUDE",
                        "forge_create_contact",
                        "CONTACT",
                        contact_type="EXCLUDE",
                        select=[root, link_arm],
                    )
                )[0]
                contact_pair = (
                    await make(
                        "CONTACT/PAIR",
                        "forge_create_contact",
                        "CONTACT",
                        contact_type="PAIR",
                        select=[visuals["BOX"], colliders["BOX"]],
                    )
                )[0]

                # Sensor subtypes and valid target contexts.
                sensor_targets = [
                    ("Jointpos", joints["HINGE"]),
                    ("Jointvel", joints["HINGE"]),
                    ("Touch", sites["SPHERE"]),
                    ("Accelerometer", sites["SPHERE"]),
                    ("Velocimeter", sites["SPHERE"]),
                    ("Gyro", sites["SPHERE"]),
                    ("Framepos", root),
                    ("Framequat", root),
                    ("Framexaxis", root),
                    ("Frameyaxis", root),
                    ("Framezaxis", root),
                    ("Framelinvel", root),
                    ("Frameangvel", root),
                    ("Subtreecom", root),
                    ("Subtreelinvel", root),
                    ("Subtreeangmom", root),
                ]
                sensors: list[str] = []
                for subtype, target in sensor_targets:
                    made = await make(
                        f"SENSOR/{subtype}", "forge_create_sensor", "SENSOR", sensor_type=subtype, select=[target]
                    )
                    sensors += made
                contact_sensor = (
                    await make(
                        "SENSOR/Contact/Subtree",
                        "forge_create_sensor",
                        "SENSOR",
                        sensor_type="Contact",
                        set_subtree=True,
                        select=[root],
                    )
                )[0]
                sensors.append(contact_sensor)

                # Lighting/camera subtypes.
                lights: list[str] = []
                for light_type in ("DIRECTIONAL", "SPOT", "POINT"):
                    made = await make(
                        f"LIGHT/{light_type}",
                        "forge_create_light",
                        "LIGHT",
                        light_type=light_type,
                        light_mode="FIXED",
                        select=[],
                    )
                    lights += made
                cameras: list[str] = []
                for camera_type in ("PERSPECTIVE", "ORTHOGRAPHIC"):
                    made = await make(
                        f"CAMERA/{camera_type}",
                        "forge_create_camera",
                        "CAMERA",
                        camera_type=camera_type,
                        camera_mode="FIXED",
                        select=[],
                    )
                    cameras += made
                include_objs = await make("INCLUDE", "forge_create_include", "INCLUDE", file=str(external), select=[])
                include = include_objs[0] if include_objs else None
                await make(
                    "ATTACH",
                    "forge_create_attach",
                    "ATTACH",
                    any_of=True,
                    file=str(attach_file),
                    select=[link_tool],
                )

                # ── Edit parameters and verify readback ─────────────────
                await call("forge_set_transform", name=root, location=(1.0, 0.0, 0.0), rotation_euler=(0.0, 0.1, 0.0))
                await edit("EDIT/LINK", root, {"mocap": True, "gravcomp": 0.25}, {"mocap", "gravcomp"})
                if inertia:
                    # diaginertia is computed by forge_create_inertial; only
                    # mass is an intentional post-computation edit here.
                    await edit("EDIT/INERTIAL", inertia[0], {"mass": 4.5}, {"mass"})
                for shape, name in visuals.items():
                    size = (
                        (0.8, 0.6, 0.4)
                        if shape == "BOX"
                        else ((0.25, 0.9) if shape in {"CAPSULE", "CYLINDER"} else 0.3)
                    )
                    try:
                        await call("forge_set_shape_size", name=name, size=size)
                        cases.append((f"EDIT/VISUAL/{shape}/size", "PASS"))
                    except Exception as exc:
                        cases.append((f"EDIT/VISUAL/{shape}/size", f"FAIL: {exc}"))
                        failures.append(f"EDIT/VISUAL/{shape}/size")
                for shape, name in colliders.items():
                    if shape == "MESH":
                        continue
                    size = (
                        (0.7, 0.5, 0.3)
                        if shape == "BOX"
                        else ((0.2, 0.8) if shape in {"CAPSULE", "CYLINDER"} else 0.25)
                    )
                    try:
                        await call("forge_set_shape_size", name=name, size=size)
                        cases.append((f"EDIT/COLLIDER/{shape}/size", "PASS"))
                    except Exception as exc:
                        cases.append((f"EDIT/COLLIDER/{shape}/size", f"FAIL: {exc}"))
                        failures.append(f"EDIT/COLLIDER/{shape}/size")
                await edit("EDIT/JOINT", joints["HINGE"], {"type": "SLIDE", "damping": 0.15}, {"type", "damping"})
                await edit("EDIT/ACTUATOR", actuators["MOTOR"], {"gear": [2.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, {"gear"})
                await edit("EDIT/TENDON", tendon, {"stiffness": 2.0, "damping": 0.2}, {"stiffness", "damping"})
                await edit("EDIT/CONTACT", contact_pair, {"margin": 0.02, "gap": 0.01}, {"margin", "gap"})
                await edit("EDIT/SENSOR", sensors[0], {"noise": 0.01, "cutoff": 10.0}, {"noise", "cutoff"})
                await edit("EDIT/LIGHT", lights[0], {"mode": "TRACK"}, {"mode"})
                await edit("EDIT/CAMERA", cameras[0], {"mode": "TRACK"}, {"mode"})
                await edit("EDIT/REPLICATE", replicate, {"count": 3, "sep": "_E"}, {"count", "sep"})
                await edit("EDIT/HFIELD", hfield, {"gap": 0.01}, {"gap"})
                await edit("EDIT/PLANE", plane, {"gap": 0.02}, {"gap"})
                for shape, name in sites.items():
                    size = (
                        (0.3, 0.25, 0.2)
                        if shape == "BOX"
                        else ((0.1, 0.4) if shape in {"CAPSULE", "CYLINDER"} else 0.12)
                    )
                    try:
                        await call("forge_set_shape_size", name=name, size=size)
                        cases.append((f"EDIT/SITE/{shape}/size", "PASS"))
                    except Exception as exc:
                        cases.append((f"EDIT/SITE/{shape}/size", f"FAIL: {exc}"))
                        failures.append(f"EDIT/SITE/{shape}/size")
                if include:
                    await edit("EDIT/INCLUDE", include, {"file": str(external)}, {"file"})

                # Export validates that the edited graph remains serializable.
                out = work_dir / "_live_multibody_output.xml"
                exported = await call("forge_export_mjcf", filepath=str(out), overwrite=True)
                if not out.is_file() or not exported.get("exists"):
                    failures.append("EXPORT")
                    cases.append(("EXPORT", f"FAIL: {exported}"))
                else:
                    cases.append(("EXPORT", "PASS"))
            except Exception as exc:  # noqa: BLE001
                # A step died — most of the rig is indexed straight out of
                # `make`, which hands back an empty list on failure. Record it
                # and fall through: the cases that did run, and the report
                # below, are the reason this script exists, and a traceback
                # throws both away.
                cases.append(("SETUP/unexpected", f"FAIL: {type(exc).__name__}: {exc}"))
                failures.append("SETUP/unexpected")
            finally:
                shutil.rmtree(work_dir, ignore_errors=True)
                # Delete only objects created by this test.  Include/Attach
                # can create referenced objects, so use the recorded list.
                if created:
                    response = await session.call_tool("forge_delete", {"names": list(dict.fromkeys(created))})
                    print("CLEANUP:", response.content[0].text if response.content else "")

                # Objects going away does not put back the export path, the
                # include / attach pickers, or the collections Forge opened.
                if state:
                    restored = await session.call_tool(
                        "forge_execute", {"code": _RESTORE_CODE.replace("__KEEP__", repr(state))}
                    )
                    if getattr(restored, "is_error", False):
                        # Silence here would let a dirty session pass as clean.
                        failures.append("CLEANUP/restore forge state")
                        cases.append(
                            (
                                "CLEANUP/restore forge state",
                                f"FAIL: {(restored.content[0].text or '')[:200]}",
                            )
                        )
                    else:
                        cases.append(("CLEANUP/restore forge state", "PASS"))
                        print("CLEANUP (forge state):", (restored.content[0].text or "")[:200])

            for label, status in cases:
                print(f"[{status}] {label}")
            print(f"MULTIBODY RESULT: {'FAIL' if failures else 'PASS'}; cases={len(cases)} failures={len(failures)}")
            return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
