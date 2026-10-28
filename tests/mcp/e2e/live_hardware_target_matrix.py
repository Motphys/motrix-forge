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

"""Complex multi-body relationship creation matrix against a live Bridge.

Covers the whole Forge **Hardware** group (Site, Actuator, Tendon, Equality,
Sensor, Contact, Light, Camera) — every declared subtype, invoked both as a
single-target relationship and as a multi-target one, where the operator
supports it.  Multi-target is where the interesting behavior lives: the number
of objects an operator creates is *not* one per invocation (site/actuator/light
and camera fan out per selected target, contact fans out pairwise), so those
counts are asserted exactly rather than loosely.

Object counts alone are weak evidence for a *relationship*, so the run ends by
exporting MJCF and counting the serialized relationship elements — the XML is
the ground truth that target/reference roles and pairwise fan-out survived.

Attaches to an **already running** Blender bridge (``FORGE_MCP_PORT``, default
9876) and needs an **empty file**: the export check compares whole-export
relationship counts against what this run created, and the exporter reads the
file-global Forge collections rather than the current scene — so a rig parked in
another scene, or a pre-existing actuator or tendon, would show up as a
mismatch.  It refuses to start otherwise rather than report a misleading
failure — point it at a scratch Blender.  Cleanup diffs against a pre-run
snapshot, so it takes away the collections Forge created for the rig as well as
the objects, and puts back the scene-level Forge properties the run wrote.

    FORGE_MCP_PORT=9876 python tests/mcp/e2e/live_hardware_target_matrix.py
"""

from __future__ import annotations

import asyncio
import json
import os
import shutil
import sys
import tempfile
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

PREFIX = "E2E_HW_"  # per-run suffix is appended so a crashed run cannot poison the next one


class SetupAborted(Exception):
    """A rig step failed; the case that failed is already recorded."""


# Failures that mean the harness broke, not that the operator refused the
# relationship. Counting one of these as a correct rejection would report PASS
# for a run that never exercised the case.
HARNESS_ERRORS = (
    "Cannot reach the Blender Forge bridge",
    "bridge closed the connection",
    "invalid JSON response",
    "modal operation already running",
)


# The whole file, not just the current scene. The exporter resolves
# relationships through the file-global ``bpy.data.collections["CONTACT"]`` and
# friends (``Forge/ops/exports.py``), so a rig parked in another scene is counted
# as this run's work even though the current scene looks empty.
_INVENTORY_CODE = """
import bpy

current = bpy.context.scene
result = {
    "current": current.name,
    "main_scene": current.Main_Scene,
    "scenes": [{"name": scene.name, "objects": len(scene.objects)} for scene in bpy.data.scenes],
    "outside_current": [obj.name for obj in bpy.data.objects if obj.name not in current.objects],
    # Scene-level Forge state the tools write, so cleanup can put it back.
    "forge_props": {
        name: getattr(current.Forge_Props, name, "")
        for name in ("select_tag", "export_path", "import_file_path")
    },
    "snapshot": {
        "scenes": sorted(scene.name for scene in bpy.data.scenes),
        "objects": sorted(obj.name for obj in bpy.data.objects),
        "collections": sorted({coll.name for coll in bpy.data.collections} | {current.collection.name}),
    },
}
"""

# The guard established the file held nothing but the Forge collections in a
# single empty scene, so diffing against the snapshot takes away exactly what
# this run added — including the collections Forge creates for the rig, which
# deleting the objects alone leaves behind.
_RESTORE_CODE = """
import bpy

keep = __KEEP__
props = __PROPS__
if not keep.get("scenes") or not keep.get("collections"):
    raise RuntimeError("refusing to restore: the pre-run snapshot is missing or empty")

dropped = {"scenes": [], "objects": [], "collections": []}

for scene in list(bpy.data.scenes):
    if scene.name not in keep["scenes"]:
        dropped["scenes"].append(scene.name)
        bpy.data.scenes.remove(scene)

for obj in list(bpy.data.objects):
    if obj.name not in keep["objects"]:
        dropped["objects"].append(obj.name)
        bpy.data.objects.remove(obj, do_unlink=True)

for coll in list(bpy.data.collections):
    if coll.name not in keep["collections"]:
        dropped["collections"].append(coll.name)
        bpy.data.collections.remove(coll)

for name, value in props.items():
    setattr(bpy.context.scene.Forge_Props, name, value)

bpy.ops.outliner.orphans_purge()

result = dropped
"""


def pair_count(n: int) -> int:
    """Fan-out of pairwise relationships: one per unordered pair."""
    return n * (n - 1) // 2


async def main() -> int:
    env = {**os.environ, "FORGE_MCP_PORT": os.environ.get("FORGE_MCP_PORT", "9876")}
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=str(Path(__file__).resolve().parents[3] / "mcp-server"),
        env=env,
    )
    work_dir = Path(tempfile.mkdtemp(prefix="forge_hw_matrix_"))
    # A unique prefix per run: leftover rig objects from a crashed run must not
    # be mistaken for this run's, and must not collide with its renames.
    prefix = f"{PREFIX}{uuid.uuid4().hex[:6]}_"

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

            inventory = await call("forge_execute", code=_INVENTORY_CODE)
            snapshot = inventory.get("snapshot") or {}
            forge_props = inventory.get("forge_props") or {}
            scenes = inventory.get("scenes") or []
            current_name = inventory.get("current")
            occupied = [entry for entry in scenes if entry["objects"]]
            extra = sorted({entry["name"] for entry in scenes} - {current_name})
            outside = sorted(inventory.get("outside_current") or [])
            if occupied or extra or outside or inventory.get("main_scene") != current_name:
                print("ABORT: this matrix compares whole-export counts against what it created, so it needs a")
                print("file holding a single, empty scene.")
                if occupied:
                    print("  scenes holding objects:", ", ".join(f"{s['name']} ({s['objects']})" for s in occupied))
                if extra:
                    print(f"  other scenes (their Forge collections are what the export counts): {', '.join(extra)}")
                if outside:
                    print(f"  objects outside the current scene: {', '.join(outside)}")
                if inventory.get("main_scene") != current_name:
                    print(
                        f"  the scene is named {current_name!r} but Forge resolves through scene.Main_Scene "
                        f"({inventory.get('main_scene')!r}) — the run would fail partway instead."
                    )
                print("Point it at a scratch Blender (see tests/mcp/e2e/README.md).")
                shutil.rmtree(work_dir, ignore_errors=True)
                return 2
            # The guard passed, so nothing pre-exists and cleanup diffs an empty file.
            preexisting: set[str] = set(snapshot.get("objects") or [])
            created: list[str] = []
            cases: list[tuple[str, str]] = []
            failures: list[str] = []
            tally: dict[str, int] = {}

            def record(label: str, ok: bool, detail: str = "") -> None:
                if ok:
                    cases.append((label, "PASS"))
                else:
                    cases.append((label, f"FAIL: {detail}"))
                    failures.append(label)

            async def create(label: str, tool: str, expected_type: str, count: int, **kwargs) -> list[str]:
                """Create and assert the exact number + model type of new objects."""
                try:
                    data = await call(tool, **kwargs)
                    names = data.get("created", []) or []
                    # Record for cleanup before asserting: a failed assertion is
                    # exactly when leftovers must still be deleted.
                    created.extend(names)
                    if len(names) != count:
                        raise RuntimeError(f"created {len(names)} object(s), expected {count}: {names}")
                    for name in names:
                        info = await call("forge_object_info", name=name)
                        if info.get("type") != expected_type:
                            raise RuntimeError(f"{name}: type={info.get('type')!r}, expected {expected_type!r}")
                    tally[expected_type] = tally.get(expected_type, 0) + len(names)
                    record(label, True)
                    return names
                except Exception as exc:  # noqa: BLE001
                    record(label, False, str(exc))
                    return []

            async def create_error(label: str, tool: str, **kwargs) -> None:
                """Assert the operator rejects an invalid relationship.

                Only the operator's own refusal counts — see ``HARNESS_ERRORS``.
                """
                try:
                    data = await call(tool, **kwargs)
                    created.extend(data.get("created", []) or [])
                    record(label, False, f"expected rejection, got {data}")
                except Exception as exc:  # noqa: BLE001
                    text = str(exc)
                    if any(marker in text for marker in HARNESS_ERRORS):
                        record(label, False, f"harness error, not a rejection: {text}")
                    else:
                        record(label, True, text)

            def one(names: list[str], label: str) -> str:
                """The single object a rig step was expected to produce.

                ``create`` records its own failure and returns ``[]``; indexing
                that directly would raise out of the run body, so the report
                below would never print and the failing step's label would be
                the only clue — printed only if the traceback is read.
                """
                if len(names) != 1:
                    raise SetupAborted(f"{label}: expected 1 object, got {names or 'none'}")
                return names[0]

            async def rename(old: str, new: str) -> str:
                """Rename and return the name actually in force.

                ``forge_rename`` refuses a taken name instead of suffixing it, so
                a silent skip would leave the rig pointing at whatever object
                already held the name. Fail loudly instead.
                """
                result = await call("forge_rename", name_map={old: new})
                if skipped := (result.get("skipped") or {}):
                    raise RuntimeError(f"rename {old!r} -> {new!r} was skipped: {skipped[old]}")
                actual = (result.get("renamed") or {}).get(old, new)
                if actual != new:
                    raise RuntimeError(f"rename {old!r} -> {new!r} produced {actual!r}")
                created[created.index(old)] = actual
                return actual

            try:
                # ── Multi-body rig ──────────────────────────────────────
                # root -> base -> arm -> tool -> tine gives five links, enough
                # for the 3+ target fan-out cases.
                root = one(await create("rig/LINK/root", "forge_create_link", "LINK", 1, select=[]), "rig/LINK/root")
                root = await rename(root, prefix + "Root")
                await call("forge_mark_root_link", select=[root])

                links = [root]
                for index, alias in enumerate(("Base", "Arm", "Tool", "Tine"), start=1):
                    made = await create(f"rig/LINK/{alias}", "forge_create_link", "LINK", 1, select=[links[index - 1]])
                    links.append(await rename(one(made, f"rig/LINK/{alias}"), prefix + alias))

                # SLIDE/HINGE joints: the only subtypes a tendon accepts, and
                # the habitual actuator / equality / sensor targets.
                joints: list[str] = []
                for index, subtype in enumerate(("HINGE", "SLIDE", "HINGE", "HINGE")):
                    made = await create(
                        f"rig/JOINT/{subtype}#{index}",
                        "forge_create_joint",
                        "JOINT",
                        1,
                        joint_type=subtype,
                        select=[links[index + 1]],
                    )
                    joints.append(await rename(one(made, f"rig/JOINT/{subtype}#{index}"), f"{prefix}J{index}"))

                # A FREE joint must NOT be accepted as a tendon target.
                free_joint = one(
                    await create(
                        "rig/JOINT/FREE", "forge_create_joint", "JOINT", 1, joint_type="FREE", select=[links[1]]
                    ),
                    "rig/JOINT/FREE",
                )

                # Visuals under every link: contact-pair and sensor targets.
                geoms: list[str] = []
                for index, link in enumerate(links[1:], start=1):
                    geoms += await create(
                        f"rig/GEOM/BOX#{index}",
                        "forge_create_geometry",
                        "VISUAL",
                        1,
                        geometry_type="BOX",
                        size_box=(0.2, 0.2, 0.2),
                        select=[link],
                    )
                plane = one(await create("rig/PLANE", "forge_create_plane", "PLANE", 1, select=[]), "rig/PLANE")

                # ── 1. Site — single target vs one site per selected link ──
                for subtype in ("BOX", "CAPSULE", "CYLINDER", "SPHERE"):
                    await create(
                        f"SITE/{subtype}/single",
                        "forge_create_site",
                        "SITE",
                        1,
                        site_type=subtype,
                        select=[links[4]],
                    )
                await create(
                    "SITE/BOX/multi(3 links)",
                    "forge_create_site",
                    "SITE",
                    3,
                    site_type="BOX",
                    select=[links[1], links[2], links[3]],
                )
                multi_sites = await create(
                    "SITE/SPHERE/multi(4 links)",
                    "forge_create_site",
                    "SITE",
                    4,
                    site_type="SPHERE",
                    select=[links[1], links[2], links[3], links[4]],
                )

                # ── 2. Actuator — single vs one actuator per target ─────────
                for subtype in ("GENERAL", "MOTOR", "POSITION", "VELOCITY", "ADHESION"):
                    await create(
                        f"ACTUATOR/{subtype}/single(joint)",
                        "forge_create_actuator",
                        "ACTUATOR",
                        1,
                        actuator_type=subtype,
                        select=[joints[0]],
                    )
                await create(
                    "ACTUATOR/MOTOR/single(link)",
                    "forge_create_actuator",
                    "ACTUATOR",
                    1,
                    actuator_type="MOTOR",
                    select=[links[2]],
                )
                await create(
                    "ACTUATOR/POSITION/multi(3 joints)",
                    "forge_create_actuator",
                    "ACTUATOR",
                    3,
                    actuator_type="POSITION",
                    select=[joints[0], joints[1], joints[2]],
                )
                await create(
                    "ACTUATOR/GENERAL/multi(4 joints)",
                    "forge_create_actuator",
                    "ACTUATOR",
                    4,
                    actuator_type="GENERAL",
                    select=[joints[0], joints[1], joints[2], joints[3]],
                )
                await create(
                    "ACTUATOR/VELOCITY/multi(3 links)",
                    "forge_create_actuator",
                    "ACTUATOR",
                    3,
                    actuator_type="VELOCITY",
                    select=[links[1], links[2], links[3]],
                )

                # ── 3. Tendon — an ordered joint chain, always multi-target ──
                tendon2 = await create(
                    "TENDON/FIXED/2 joints",
                    "forge_create_tendon",
                    "TENDON",
                    1,
                    tendon_type="FIXED",
                    select=[joints[0], joints[1]],
                )
                tendon3 = await create(
                    "TENDON/FIXED/3 joints",
                    "forge_create_tendon",
                    "TENDON",
                    1,
                    tendon_type="FIXED",
                    select=[joints[0], joints[1], joints[2]],
                )
                await create(
                    "TENDON/FIXED/4 joints",
                    "forge_create_tendon",
                    "TENDON",
                    1,
                    tendon_type="FIXED",
                    select=[joints[0], joints[1], joints[2], joints[3]],
                )
                await create_error(
                    "TENDON/single(1 joint)/rejected", "forge_create_tendon", tendon_type="FIXED", select=[joints[0]]
                )
                await create_error(
                    "TENDON/FREE joint/rejected",
                    "forge_create_tendon",
                    tendon_type="FIXED",
                    select=[free_joint, joints[1]],
                )

                # An actuator on a tendon only becomes meaningful once it exists.
                if tendon2:
                    await create(
                        "ACTUATOR/GENERAL/single(tendon)",
                        "forge_create_actuator",
                        "ACTUATOR",
                        1,
                        actuator_type="GENERAL",
                        select=[tendon2[0]],
                    )

                # ── 4. Equality — exactly two targets ───────────────────────
                await create(
                    "EQUALITY/CONNECT/2 links",
                    "forge_create_equality",
                    "EQUALITY",
                    1,
                    equality_type="CONNECT",
                    select=[links[1], links[2]],
                )
                await create(
                    "EQUALITY/WELD/2 links",
                    "forge_create_equality",
                    "EQUALITY",
                    1,
                    equality_type="WELD",
                    select=[links[2], links[3]],
                )
                await create(
                    "EQUALITY/JOINT/2 joints",
                    "forge_create_equality",
                    "EQUALITY",
                    1,
                    equality_type="JOINT",
                    select=[joints[2], joints[3]],
                )
                if len(multi_sites) >= 3:
                    await create(
                        "EQUALITY/CONNECT/2 sites",
                        "forge_create_equality",
                        "EQUALITY",
                        1,
                        equality_type="CONNECT",
                        select=[multi_sites[0], multi_sites[1]],
                    )
                    await create(
                        "EQUALITY/WELD/2 sites",
                        "forge_create_equality",
                        "EQUALITY",
                        1,
                        equality_type="WELD",
                        select=[multi_sites[1], multi_sites[2]],
                    )
                await create_error(
                    "EQUALITY/single(1 link)/rejected",
                    "forge_create_equality",
                    equality_type="CONNECT",
                    select=[links[1]],
                )

                # ── 5. Contact — 2 targets vs pairwise fan-out ──────────────
                await create(
                    "CONTACT/EXCLUDE/single(2 links)",
                    "forge_create_contact",
                    "CONTACT",
                    1,
                    contact_type="EXCLUDE",
                    select=[links[1], links[2]],
                )
                await create(
                    "CONTACT/EXCLUDE/multi(3 links)",
                    "forge_create_contact",
                    "CONTACT",
                    pair_count(3),
                    contact_type="EXCLUDE",
                    select=[links[1], links[2], links[3]],
                )
                await create(
                    "CONTACT/EXCLUDE/multi(4 links)",
                    "forge_create_contact",
                    "CONTACT",
                    pair_count(4),
                    contact_type="EXCLUDE",
                    select=[links[1], links[2], links[3], links[4]],
                )
                await create(
                    "CONTACT/PAIR/single(2 geoms)",
                    "forge_create_contact",
                    "CONTACT",
                    1,
                    contact_type="PAIR",
                    select=[geoms[0], geoms[1]],
                )
                await create(
                    "CONTACT/PAIR/multi(3 geoms)",
                    "forge_create_contact",
                    "CONTACT",
                    pair_count(3),
                    contact_type="PAIR",
                    select=geoms[:3],
                )
                await create(
                    "CONTACT/PAIR/multi(4 geoms)",
                    "forge_create_contact",
                    "CONTACT",
                    pair_count(4),
                    contact_type="PAIR",
                    select=geoms[:4],
                )
                await create_error(
                    "CONTACT/single(1 link)/rejected", "forge_create_contact", contact_type="EXCLUDE", select=[links[1]]
                )

                # ── 6. Sensor — single target vs target+reference ───────────
                site_target = multi_sites[0] if multi_sites else plane
                for subtype, selection in (
                    ("Jointpos", [joints[0]]),
                    ("Jointvel", [joints[0]]),
                    ("Touch", [site_target]),
                    ("Accelerometer", [site_target]),
                    ("Velocimeter", [site_target]),
                    ("Gyro", [site_target]),
                    ("Framepos", [links[2]]),
                    ("Framequat", [links[2]]),
                    ("Framexaxis", [links[2]]),
                    ("Frameyaxis", [links[2]]),
                    ("Framezaxis", [links[2]]),
                    ("Framelinvel", [links[2]]),
                    ("Frameangvel", [links[2]]),
                    ("Subtreecom", [links[2]]),
                    ("Subtreelinvel", [links[2]]),
                    ("Subtreeangmom", [links[2]]),
                ):
                    await create(
                        f"SENSOR/{subtype}/single",
                        "forge_create_sensor",
                        "SENSOR",
                        1,
                        sensor_type=subtype,
                        select=selection,
                    )
                await create(
                    "SENSOR/Contact/single(subtree)",
                    "forge_create_sensor",
                    "SENSOR",
                    1,
                    sensor_type="Contact",
                    set_subtree=True,
                    select=[links[1]],
                )
                # Target + reference is one sensor with two roles, not two sensors.
                for subtype in ("Framepos", "Framequat", "Framelinvel"):
                    await create(
                        f"SENSOR/{subtype}/target+reference",
                        "forge_create_sensor",
                        "SENSOR",
                        1,
                        sensor_type=subtype,
                        set_ref=True,
                        select=[links[2], links[1]],
                    )
                await create(
                    "SENSOR/Framequat/single(xbody)",
                    "forge_create_sensor",
                    "SENSOR",
                    1,
                    sensor_type="Framequat",
                    set_xbody=True,
                    select=[links[3]],
                )
                await create_error(
                    "SENSOR/xbody+subtree/rejected",
                    "forge_create_sensor",
                    sensor_type="Framepos",
                    set_xbody=True,
                    set_subtree=True,
                    select=[links[1]],
                )
                await create_error(
                    "SENSOR/ref on joint/rejected",
                    "forge_create_sensor",
                    sensor_type="Jointpos",
                    set_ref=True,
                    select=[joints[0], joints[1]],
                )
                await create_error(
                    "SENSOR/Framepos on joint/rejected",
                    "forge_create_sensor",
                    sensor_type="Framepos",
                    select=[joints[0]],
                )

                # ── 7. Light — world / 1 target / 2 targets / N targets ────
                for subtype in ("DIRECTIONAL", "SPOT", "POINT"):
                    await create(
                        f"LIGHT/{subtype}/world(no select)",
                        "forge_create_light",
                        "LIGHT",
                        1,
                        light_type=subtype,
                        light_mode="FIXED",
                        select=[],
                    )
                for label, expected, kwargs in (
                    (
                        "LIGHT/SPOT/single(1 link, TARGETBODY)",
                        1,
                        dict(light_type="SPOT", light_mode="TARGETBODY", select=[links[2]]),
                    ),
                    (
                        "LIGHT/SPOT/single(1 link, FIXED)",
                        1,
                        dict(light_type="SPOT", light_mode="FIXED", select=[links[2]]),
                    ),
                    (
                        "LIGHT/POINT/two-target(2 links, TARGETBODY)",
                        1,
                        dict(light_type="POINT", light_mode="TARGETBODY", select=[links[2], links[3]]),
                    ),
                    (
                        "LIGHT/SPOT/multi(3 links, FIXED)",
                        3,
                        dict(light_type="SPOT", light_mode="FIXED", select=[links[1], links[2], links[3]]),
                    ),
                    (
                        "LIGHT/POINT/multi(4 links, TRACK)",
                        4,
                        dict(light_type="POINT", light_mode="TRACK", select=[links[1], links[2], links[3], links[4]]),
                    ),
                ):
                    await create(label, "forge_create_light", "LIGHT", expected, **kwargs)
                await create_error(
                    "LIGHT/DIRECTIONAL on link/rejected",
                    "forge_create_light",
                    light_type="DIRECTIONAL",
                    light_mode="FIXED",
                    select=[links[2]],
                )

                # ── 8. Camera — world / 1 target / 2 targets / N targets ───
                for subtype in ("PERSPECTIVE", "ORTHOGRAPHIC"):
                    await create(
                        f"CAMERA/{subtype}/world(no select)",
                        "forge_create_camera",
                        "CAMERA",
                        1,
                        camera_type=subtype,
                        camera_mode="FIXED",
                        select=[],
                    )
                for label, expected, kwargs in (
                    (
                        "CAMERA/PERSPECTIVE/single(1 link, TARGETBODY)",
                        1,
                        dict(camera_type="PERSPECTIVE", camera_mode="TARGETBODY", select=[links[2]]),
                    ),
                    (
                        "CAMERA/ORTHOGRAPHIC/two-target(2 links, TARGETBODY)",
                        1,
                        dict(camera_type="ORTHOGRAPHIC", camera_mode="TARGETBODY", select=[links[2], links[3]]),
                    ),
                    (
                        "CAMERA/PERSPECTIVE/multi(3 links, FIXED)",
                        3,
                        dict(camera_type="PERSPECTIVE", camera_mode="FIXED", select=[links[1], links[2], links[3]]),
                    ),
                    (
                        "CAMERA/ORTHOGRAPHIC/multi(4 links, TRACKCOM)",
                        4,
                        dict(
                            camera_type="ORTHOGRAPHIC",
                            camera_mode="TRACKCOM",
                            select=[links[1], links[2], links[3], links[4]],
                        ),
                    ),
                ):
                    await create(label, "forge_create_camera", "CAMERA", expected, **kwargs)

                # ── 9. Re-target an existing relationship ───────────────────
                if tendon3:
                    try:
                        result = await call(
                            "forge_set_tendon_targets",
                            name=tendon3[0],
                            targets=[{"target": joints[3], "coef": -1.0}, {"target": joints[1], "coef": 0.25}],
                        )
                        got = [item["target"] for item in result.get("targets", [])]
                        record("EDIT/TENDON/re-target(3->2 joints)", got == [joints[3], joints[1]], str(result))
                    except Exception as exc:  # noqa: BLE001
                        record("EDIT/TENDON/re-target(3->2 joints)", False, str(exc))

                # ── 10. Export — the serialized relationships are the truth ─
                out = work_dir / "_hw_matrix_output.xml"
                try:
                    exported = await call("forge_export_mjcf", filepath=str(out), overwrite=True)
                    if not out.is_file() or not exported.get("exists"):
                        raise RuntimeError(f"no output file: {exported}")
                    record("EXPORT/mjcf", True)
                except Exception as exc:  # noqa: BLE001
                    record("EXPORT/mjcf", False, str(exc))

                if out.is_file():
                    xml_root = ET.parse(out).getroot()

                    def block_children(tag: str) -> int:
                        """Count relationship entries inside every <tag> block."""
                        return sum(len(list(node)) for node in xml_root.findall(f".//{tag}"))

                    got = {
                        "actuator": block_children("actuator"),
                        "tendon": block_children("tendon"),
                        "equality": block_children("equality"),
                        "contact": block_children("contact"),
                        "sensor": block_children("sensor"),
                    }
                    want = {key: tally.get(key.upper(), 0) for key in got}
                    print(
                        "EXPORTED RELATIONSHIP COUNTS:",
                        json.dumps({k: {"got": got[k], "want": want[k]} for k in got}, indent=1),
                    )

                    for key in got:
                        record(
                            f"EXPORT/{key} count == created objects",
                            got[key] == want[key],
                            f"xml={got[key]}, objects={want[key]}",
                        )

                    # MJCF keeps a single <tendon> container holding one <fixed>
                    # per tendon, so the chains are the container's children.
                    # Built 2, 3 and 4 joints; the 3-joint one was re-targeted
                    # down to 2 above — so the full chains must read 4, 2, 2.
                    chains = sorted(
                        (len(list(fixed)) for fixed in xml_root.findall(".//tendon/fixed")),
                        reverse=True,
                    )
                    record("EXPORT/tendon chains preserved (4,2,2)", chains == [4, 2, 2], f"chains={chains}")
            except SetupAborted as exc:
                # The failing step is already recorded; stop building the rig but
                # let the report below still run, so the cases that did execute
                # are not lost with the traceback.
                record("SETUP/aborted", False, str(exc))
            except Exception as exc:  # noqa: BLE001
                # Anything else — an operator this Blender does not have, a
                # bridge error mid-step — must not take the report down with it
                # either, for the same reason.
                record("SETUP/unexpected", False, f"{type(exc).__name__}: {exc}")
            finally:
                shutil.rmtree(work_dir, ignore_errors=True)
                leftovers = [n for n in dict.fromkeys(created) if n not in preexisting]
                if leftovers:
                    response = await session.call_tool("forge_delete", {"names": leftovers})
                    print("CLEANUP:", (response.content[0].text or "")[:400])

                # Deleting the objects leaves the collections Forge created for
                # them, and the export leaves scene-level Forge state behind.
                # The guard proved the file held a single empty scene, so
                # diffing against the snapshot takes away exactly what this run
                # added — nothing else.
                restored = await session.call_tool(
                    "forge_execute",
                    {"code": _RESTORE_CODE.replace("__KEEP__", repr(snapshot)).replace("__PROPS__", repr(forge_props))},
                )
                if getattr(restored, "is_error", False):
                    # Silence here would let a dirty file pass as a clean run.
                    record("CLEANUP/restore pre-run file state", False, (restored.content[0].text or "")[:300])
                else:
                    record("CLEANUP/restore pre-run file state", True)

            for label, status in cases:
                print(f"[{status}] {label}")
            print(
                f"HARDWARE MATRIX RESULT: {'FAIL' if failures else 'PASS'}; cases={len(cases)} failures={len(failures)}"
            )
            return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
