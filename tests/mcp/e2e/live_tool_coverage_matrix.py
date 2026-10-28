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

"""Exercise **every** registered MCP tool once against a live Bridge.

Where the other live scripts cover a subsystem (`live_hardware_target_matrix.py`
for relationships, `live_multibody_matrix.py` for a build/edit/export round
trip), this one exists to leave no tool unexercised: it ends by diffing the set
of tools it called against the server's own tool registry, so a newly added tool
fails the run until it is covered here.

Needs a file with a **single, empty scene named ``Scene``** and refuses to start
otherwise. Every clause of that is load-bearing: the run creates then deletes
everything it makes, so cleanup would otherwise remove work it does not own; the
import it ends with clears every scene except the one named ``Scene``, which
would destroy scenes the guard never inspected; Forge resolves the model through
``scene.Main_Scene``, so any other name fails partway; and the import's orphan
purge deletes datablocks with no users, which nothing can restore afterwards.

Hence the check reads the whole file, not just the current scene. Cleanup diffs
against a pre-run snapshot of scenes, objects and collections, so the file is
left exactly as it was found.

    FORGE_MCP_PORT=9876 python tests/mcp/e2e/live_tool_coverage_matrix.py
"""

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

PREFIX = "E2E_ALL_"


class SetupAborted(Exception):
    """A setup step failed and the run body cannot continue."""


# Failures that mean the harness broke, not that the tool refused. Counting one
# of these as a correct rejection would report PASS for a case never exercised.
HARNESS_ERRORS = (
    "Cannot reach the Blender Forge bridge",
    "bridge closed the connection",
    "invalid JSON response",
    "modal operation already running",
)

# The whole file, not just the current scene: the guard cannot use
# ``forge_scene_info`` (current scene only), and the ``snapshot`` is what cleanup
# diffs against afterwards.
_INVENTORY_CODE = """
import bpy

current = bpy.context.scene

# The import ends with an orphan purge, so anything holding no users is gone by
# the time cleanup runs — it cannot be restored, only reported up front.
orphans = {}
for name in dir(bpy.data):
    if name.startswith("_"):
        continue
    prop = getattr(bpy.data, name, None)
    if not isinstance(prop, bpy.types.bpy_prop_collection):
        continue
    try:
        unused = [item.name for item in prop if getattr(item, "users", 1) == 0]
    except Exception:
        continue
    if unused:
        orphans[name] = unused

result = {
    "current": current.name,
    "main_scene": current.Main_Scene,
    "orphans": orphans,
    "scenes": [{"name": scene.name, "objects": len(scene.objects)} for scene in bpy.data.scenes],
    "outside_current": [obj.name for obj in bpy.data.objects if obj.name not in current.objects],
    # Scene-level Forge state the tools write. None of it is part of the
    # scenes/objects/collections diff the restore does, so it is put back
    # explicitly — otherwise a "clean" run leaves select_tag set to this run's
    # tag and export_path pointing into the work directory it just deleted.
    # Values are captured as they are, not stringified: ``gizmo_scale`` is a
    # float and restoring it as text would fail the property's type.
    "forge_props": {
        name: getattr(current.Forge_Props, name, "")
        for name in ("select_tag", "gizmo_scale", "export_path", "import_file_path")
    },
    "snapshot": {
        "scenes": sorted(scene.name for scene in bpy.data.scenes),
        "objects": sorted(obj.name for obj in bpy.data.objects),
        "collections": sorted(
            {coll.name for coll in bpy.data.collections} | {current.collection.name}
        ),
    },
}
"""

# Removes everything the run added, by diffing against the pre-run snapshot
# rather than by asking where each datablock lives. include and import park their
# scenes, objects and collections outside the current scene, while replicate
# opens collections inside it — so a location test would miss some of the run's
# own leftovers and delete pre-existing datablocks that merely sit elsewhere.
_RESTORE_CODE = """
import bpy

keep = __KEEP__
props = __PROPS__
if not keep.get("scenes") or not keep.get("collections"):
    # An empty snapshot means the inventory never reached us intact; deleting
    # to that would take the file apart, so stop instead.
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

# The run's tools also write scene-level Forge state, which the diff above does
# not touch: select_tag and the import / export paths. Put back what the
# inventory found, so the file is left as it was rather than pointing at this
# run's work directory.
for name, value in props.items():
    setattr(bpy.context.scene.Forge_Props, name, value)

# Removing the run's objects orphaned their data — meshes, node groups, images,
# cameras. The guard established the file had no orphans to begin with, so this
# takes away exactly what the run orphaned and nothing else.
# The MJCF import resets Forge's global, visual, and temporary configuration;
# reset those groups explicitly as part of the harness cleanup as well.
bpy.ops.outliner.orphans_purge()

main_scene = bpy.data.scenes[bpy.context.scene.Main_Scene]
main_scene.Forge_GlobalConfig.reset()
main_scene.Forge_VisualConfig.reset()
main_scene.Forge_Temp_Props.reset()

result = dropped
"""


async def main() -> int:
    env = {**os.environ, "FORGE_MCP_PORT": os.environ.get("FORGE_MCP_PORT", "9876")}
    params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "forge_mcp"],
        cwd=str(Path(__file__).resolve().parents[3] / "mcp-server"),
        env=env,
    )
    work_dir = Path(tempfile.mkdtemp(prefix="forge_all_tools_"))
    prefix = f"{PREFIX}{uuid.uuid4().hex[:6]}_"
    # Two files on purpose. Attach and include are alternative ways to pull an
    # external model into a scene, and a file may not be both included and
    # attached in the same one: the attach task list comes back empty and the
    # operator reports "Attach fail: list index out of range". Give each its own.
    external = work_dir / f"_all_tools_include_{uuid.uuid4().hex}.xml"
    external.write_text(
        '<mujoco model="all_tools_include"><worldbody><body name="include_base" /></worldbody></mujoco>',
        encoding="utf-8",
    )
    attach_file = work_dir / f"_all_tools_attach_{uuid.uuid4().hex}.xml"
    attach_file.write_text(
        '<mujoco model="all_tools_attach"><worldbody><body name="attach_base" /></worldbody></mujoco>',
        encoding="utf-8",
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            cases: list[tuple[str, str]] = []
            failures: list[str] = []
            used: set[str] = set()
            registered: set[str] = set()

            def record(label: str, ok: bool, detail: str = "") -> None:
                if ok:
                    cases.append((label, "PASS"))
                else:
                    cases.append((label, f"FAIL: {detail}"))
                    failures.append(label)

            async def raw(tool: str, **kwargs):
                """Call a tool, counting it as exercised whatever the outcome."""
                used.add(tool)
                response = await session.call_tool(tool, kwargs)
                blocks = response.content or []
                text = blocks[0].text if blocks and hasattr(blocks[0], "text") else ""
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    data = {"raw": text}
                return data, bool(getattr(response, "is_error", False)), text, blocks

            async def ok(label: str, tool: str, **kwargs):
                """Assert a tool succeeds; return its parsed payload."""
                try:
                    data, is_error, text, _ = await raw(tool, **kwargs)
                    if is_error:
                        raise RuntimeError(text or str(data))
                    record(label, True)
                    return data
                except Exception as exc:  # noqa: BLE001
                    record(label, False, str(exc))
                    return None

            async def fails(label: str, tool: str, **kwargs) -> None:
                """Assert a tool is rejected.

                Only the tool's own refusal counts — a bridge or harness failure
                would otherwise read as a correct rejection, reporting PASS for a
                case that was never exercised.
                """
                try:
                    _, is_error, text, _ = await raw(tool, **kwargs)
                    if not is_error:
                        record(label, False, f"expected rejection, got {text}")
                    elif any(marker in text for marker in HARNESS_ERRORS):
                        record(label, False, f"harness error, not a rejection: {text}")
                    else:
                        record(label, True)
                except Exception as exc:  # noqa: BLE001
                    record(label, False, f"call itself failed: {exc}")

            def scene_names(payload: dict) -> list[str]:
                return [o["name"] if isinstance(o, dict) else o for o in payload.get("objects") or []]

            async def created_by(tool: str, **kwargs) -> list[str]:
                data = await raw(tool, **kwargs)
                return data[0].get("created") or []

            def created_first(payload: dict | None) -> str | None:
                """First created name, or None when the tool created nothing.

                ``op_call`` always reports a ``created`` key, so an empty list is
                a normal outcome of an operator that returns without creating —
                indexing it would raise out of the run body.
                """
                return next(iter((payload or {}).get("created") or []), None)

            def one(names: list[str], label: str) -> str:
                """The single object a setup step was expected to produce.

                ``created_by`` returns ``[]`` when the operator created nothing,
                so indexing the result directly would raise out of the run body
                and the report at the end would never print.
                """
                if len(names) != 1:
                    raise SetupAborted(f"{label}: expected 1 object, got {names or 'none'}")
                return names[0]

            registered = {t.name for t in (await session.list_tools()).tools}

            # ``forge_scene_info`` only describes the *current* scene, but the
            # import at the end of this run clears every scene except the one
            # named "Scene" (``io_ops._clear_scenes`` removes them outright), and
            # the cleanup below re-reads only the current scene. So the guard has
            # to look at the whole file, or it would wave through a run that
            # silently destroys scenes it never saw.
            inventory = await ok("scene inventory", "forge_execute", code=_INVENTORY_CODE)
            if inventory is None:
                shutil.rmtree(work_dir, ignore_errors=True)
                return 2

            snapshot = inventory.get("snapshot") or {}
            scenes = inventory.get("scenes") or []
            current_name = inventory.get("current")
            occupied = [s for s in scenes if s["objects"]]
            extra = sorted({s["name"] for s in scenes} - {current_name})
            outside = sorted(inventory.get("outside_current") or [])
            orphans = inventory.get("orphans") or {}
            main_scene = inventory.get("main_scene")
            if occupied or extra or outside or orphans or current_name != "Scene" or main_scene != current_name:
                print("ABORT: this run needs a file with a single, empty scene named 'Scene'.")
                if main_scene != current_name:
                    print(
                        f"  scene.Main_Scene names {main_scene!r} while the current scene is {current_name!r} — "
                        "Forge resolves every model through Main_Scene, so the run would fail partway through "
                        "instead of failing this guard."
                    )
                if orphans:
                    print("  datablocks with no users — the import purges these and nothing can restore them:")
                    for kind, names in sorted(orphans.items()):
                        shown = ", ".join(sorted(names)[:5]) + (" …" if len(names) > 5 else "")
                        print(f"    {kind} ({len(names)}): {shown}")
                if current_name != "Scene":
                    print(
                        f"  the scene is named {current_name!r}, but Forge resolves everything through "
                        f"scene.Main_Scene ({inventory.get('main_scene')!r}) and the import keeps only the "
                        "scene named 'Scene' — the run would fail partway through instead."
                    )
                if occupied:
                    print("  scenes holding objects:", ", ".join(f"{s['name']} ({s['objects']})" for s in occupied))
                if extra:
                    print(f"  other scenes (removed by the import at the end): {', '.join(extra)}")
                if outside:
                    print(f"  objects outside the current scene: {', '.join(outside)}")
                print("Use a scratch Blender or a fresh file — see tests/mcp/e2e/README.md.")
                shutil.rmtree(work_dir, ignore_errors=True)
                return 2

            try:
                # ── Guides and docs ────────────────────────────────────
                for skill in ("create", "modify"):
                    await ok(f"forge_skill/{skill}", "forge_skill", name=skill)
                await ok("forge_search_docs", "forge_search_docs", query="friction", max_results=3)
                await fails("forge_search_docs/bad args", "forge_search_docs", query="x", max_results=0)

                # ── Rig: links, joints, hierarchy ──────────────────────
                root = one(await created_by("forge_create_link", select=[]), "forge_create_link/root")
                await ok("forge_rename", "forge_rename", name_map={root: prefix + "Root"})
                root = prefix + "Root"
                await ok("forge_mark_root_link", "forge_mark_root_link", select=[root])

                links = [root]
                for index, alias in enumerate(("Base", "Arm", "Tool"), start=1):
                    made = await created_by("forge_create_link", select=[links[index - 1]])
                    child = one(made, f"forge_create_link/{alias}")
                    await ok(f"forge_create_link/{alias}", "forge_rename", name_map={child: prefix + alias})
                    links.append(prefix + alias)
                record("forge_create_link/child", len(links) == 4, f"links={links}")

                joints: list[str] = []
                for index, subtype in enumerate(("HINGE", "SLIDE", "BALL", "FREE")):
                    made = await ok(
                        f"forge_create_joint/{subtype}", "forge_create_joint", joint_type=subtype, select=[links[1]]
                    )
                    if made:
                        joints += made.get("created") or []

                # ── Raw mesh -> define_model_type -> define_parent ─────
                mesh = await ok(
                    "forge_execute/raw cube",
                    "forge_execute",
                    code=(
                        "import bpy\nbpy.ops.object.select_all(action='DESELECT')\n"
                        "bpy.ops.mesh.primitive_cube_add(location=(6.0, 0.0, 0.0))\n"
                        "result = {'name': bpy.context.object.name}\n"
                    ),
                )
                mesh_name = (mesh or {}).get("name")
                if mesh_name:
                    # define_model_type renames to the type prefix (Cube -> GEO_Cube),
                    # so the name in force afterwards is the one it reports back.
                    defined = await ok(
                        "forge_define_model_type", "forge_define_model_type", model_type="VISUAL", select=[mesh_name]
                    )
                    if defined:
                        mesh_name = (defined.get("objects") or [mesh_name])[0]
                    await ok("forge_define_parent", "forge_define_parent", select=[links[3], mesh_name])

                # ── Inertial needs a link whose visuals do not intersect ──
                inertial = await ok("forge_create_inertial", "forge_create_inertial", select=[links[3]])
                if inertial is None:
                    await ok("forge_create_inertial/retry", "forge_create_inertial", select=[links[3]])
                await ok("forge_mesh_check", "forge_mesh_check", select=[mesh_name] if mesh_name else [])

                # ── Geometry / collider / site / world elements ────────
                visual = await ok(
                    "forge_create_geometry",
                    "forge_create_geometry",
                    geometry_type="BOX",
                    size_box=(0.4, 0.4, 0.4),
                    select=[links[1]],
                )
                visual_name = created_first(visual)
                collider = await ok(
                    "forge_create_collider",
                    "forge_create_collider",
                    collider_type="BOX",
                    create_method="COLLIDER_TYPE",
                    size_box=(0.3, 0.3, 0.3),
                    select=[links[2]],
                )
                collider_name = created_first(collider)
                site = await ok(
                    "forge_create_site", "forge_create_site", site_type="SPHERE", size_radius=0.1, select=[links[2]]
                )
                site_name = created_first(site)
                await ok("forge_create_frame", "forge_create_frame", select=[links[1]])
                await ok("forge_create_plane", "forge_create_plane", select=[])
                await ok("forge_create_height_field", "forge_create_height_field", select=[])
                await ok(
                    "forge_create_material",
                    "forge_create_material",
                    category="Metal",
                    material="Aluminum",
                    select=[visual_name] if visual_name else [],
                )

                # ── Hardware relationships ─────────────────────────────
                actuator = await ok(
                    "forge_create_actuator",
                    "forge_create_actuator",
                    actuator_type="POSITION",
                    select=[joints[0]] if joints else [],
                )
                actuator_name = created_first(actuator)
                tendon = await ok("forge_create_tendon", "forge_create_tendon", tendon_type="FIXED", select=joints[:2])
                tendon_name = created_first(tendon)
                if tendon_name:
                    await ok(
                        "forge_set_tendon_targets",
                        "forge_set_tendon_targets",
                        name=tendon_name,
                        targets=[{"target": joints[1], "coef": 1.0}, {"target": joints[0], "coef": -0.5}],
                    )
                await ok(
                    "forge_create_equality",
                    "forge_create_equality",
                    equality_type="CONNECT",
                    select=[links[1], links[2]],
                )
                await ok(
                    "forge_create_contact", "forge_create_contact", contact_type="EXCLUDE", select=[links[1], links[2]]
                )
                await ok("forge_create_sensor", "forge_create_sensor", sensor_type="Framepos", select=[links[1]])
                await ok(
                    "forge_create_light",
                    "forge_create_light",
                    light_type="SPOT",
                    light_mode="TARGETBODY",
                    select=[links[1]],
                )
                await ok(
                    "forge_create_camera",
                    "forge_create_camera",
                    camera_type="PERSPECTIVE",
                    camera_mode="TARGETBODY",
                    select=[links[1]],
                )

                # ── Meta elements ──────────────────────────────────────
                await ok("forge_create_include", "forge_create_include", file=str(external), select=[])
                await ok(
                    "forge_create_attach",
                    "forge_create_attach",
                    file=str(attach_file),
                    model="all_tools_attach",
                    select=[links[2]],
                )

                # Replicate deliberately takes over its source subtree: it moves
                # the objects into its own collection with ``hide_viewport=True``
                # and Blender cannot select objects there. So it gets a subtree of
                # its own, after everything that still needs to select the rig.
                scratch = one(await created_by("forge_create_link", select=[]), "forge_create_link/scratch")
                await ok(
                    "forge_create_replicate",
                    "forge_create_replicate",
                    count=2,
                    sep="_R",
                    offset=(0.5, 0.0, 0.0),
                    select=[scratch],
                )

                # ── define_* : change a type on an existing object ──────
                if visual_name:
                    await ok(
                        "forge_define_geometry_type",
                        "forge_define_geometry_type",
                        geometry_type="SPHERE",
                        select=[visual_name],
                    )
                    await ok(
                        "forge_define_geometry_type/restore",
                        "forge_define_geometry_type",
                        geometry_type="BOX",
                        select=[visual_name],
                    )
                if collider_name:
                    await ok(
                        "forge_define_collider_type",
                        "forge_define_collider_type",
                        collider_type="CAPSULE",
                        select=[collider_name],
                    )
                if site_name:
                    await ok(
                        "forge_define_site_type", "forge_define_site_type", site_type="CYLINDER", select=[site_name]
                    )
                if joints:
                    await ok(
                        "forge_define_joint_type", "forge_define_joint_type", joint_type="SLIDE", select=[joints[0]]
                    )
                if actuator_name:
                    # select=None would leave the previous selection (a joint) in
                    # place, and the operator polls for ACTUATOR targets.
                    await ok(
                        "forge_define_actuator_type",
                        "forge_define_actuator_type",
                        actuator_type="MOTOR",
                        apply_to_all=True,
                        select=[actuator_name],
                    )

                # ── Editing tools ──────────────────────────────────────
                await ok(
                    "forge_set_transform",
                    "forge_set_transform",
                    name=links[1],
                    location=(0.5, 0.0, 0.5),
                    rotation_euler=(0.0, 0.1, 0.0),
                )
                if site_name:
                    # define_site_type turned this site into a CYLINDER above, so
                    # it takes (radius, height) rather than a SPHERE's scalar.
                    await ok("forge_set_shape_size", "forge_set_shape_size", name=site_name, size=(0.12, 0.24))
                await ok("forge_set_property", "forge_set_property", name=links[1], values={"mocap": False})
                await ok(
                    "forge_set_scene_property", "forge_set_scene_property", group="g_option", values={"timestep": 0.002}
                )
                await ok(
                    "forge_set_scene_property/gizmo",
                    "forge_set_scene_property",
                    group="forge_props",
                    values={"gizmo_scale": 0.25, "select_tag": "E2E_ALL"},
                )
                await ok("forge_scale_gizmo_size", "forge_scale_gizmo_size", select=[links[1]])

                # ── Instance links ─────────────────────────────────────
                await ok("forge_mark_instance_link", "forge_mark_instance_link", select=[links[2]])
                await ok(
                    "forge_set_scene_property/instance_body",
                    "forge_set_scene_property",
                    group="forge_props",
                    values={"instance_body": links[2]},
                )
                await ok("forge_set_instance_idname", "forge_set_instance_idname", select=[links[3]])

                # ── Queries / inspection ───────────────────────────────
                await ok("forge_object_info", "forge_object_info", name=links[1])
                await ok("forge_scene_config", "forge_scene_config", group="g_option")
                await ok("forge_blendfile_summary", "forge_blendfile_summary")
                await ok("forge_measure", "forge_measure", names=[links[1], links[2]])
                await ok("forge_select_by_tag", "forge_select_by_tag")
                await ok(
                    "forge_batch_rename",
                    "forge_batch_rename",
                    new_name=prefix + "BATCH",
                    numerate="##",
                    select=[links[1], links[2]],
                )

                # Both modes: `layout=True` returns the window layout as JSON, the
                # default returns a PNG. Exercising only the first left the image
                # path untested and the case passing on any payload.
                shot, shot_error, shot_text, _ = await raw("forge_screenshot", layout=True)
                image, image_error, image_text, image_blocks = await raw("forge_screenshot")
                if shot_error or image_error:
                    # Screenshots need a GUI Blender; a background one is expected
                    # to refuse, and that refusal is itself the documented behavior.
                    record(
                        "forge_screenshot",
                        "requires Blender in GUI mode" in (shot_text + image_text),
                        (shot_text or image_text)[:200],
                    )
                else:
                    is_image = bool(image_blocks) and getattr(image_blocks[0], "type", "") == "image"
                    record("forge_screenshot", bool(shot) and is_image, f"layout={bool(shot)} image={is_image}")

                # ── CoACD decomposition, then select the hulls ─────────
                if visual_name:
                    await ok(
                        "forge_coacd",
                        "forge_coacd",
                        name=visual_name,
                        threshold=0.1,
                        resolution=500,
                        max_ch_vertex=32,
                        max_convex_hull=2,
                    )
                await ok("forge_select_hulls", "forge_select_hulls")

                # ── Export / save / import ─────────────────────────────
                out = work_dir / "_all_tools_output.xml"
                exported = await ok("forge_export_mjcf", "forge_export_mjcf", filepath=str(out), overwrite=True)
                if exported is not None and not out.is_file():
                    record("forge_export_mjcf/wrote file", False, f"no file at {out}")

                copy_path = work_dir / "_all_tools_copy.blend"
                before_copy = await ok("forge_blendfile_summary/before copy", "forge_blendfile_summary")
                await ok(
                    "forge_save_blendfile",
                    "forge_save_blendfile",
                    filepath=str(copy_path),
                    overwrite=True,
                    save_copy=True,
                )
                after_copy = await ok("forge_blendfile_summary/after copy", "forge_blendfile_summary")

                if before_copy is not None and after_copy is not None:
                    # save_copy must not adopt the destination as the current file.
                    before_fp = (before_copy.get("path_info") or {}).get("filepath")
                    after_fp = (after_copy.get("path_info") or {}).get("filepath")
                    record(
                        "forge_save_blendfile/kept the current file path",
                        before_fp == after_fp,
                        f"{before_fp!r} -> {after_fp!r}",
                    )
                record("forge_save_blendfile/wrote the copy", copy_path.is_file(), str(copy_path))

                # Import clears the Forge scene; everything present is ours, so
                # it is safe here and the cleanup below re-reads the scene.
                await ok("forge_import_mjcf", "forge_import_mjcf", filepath=str(out))

                await fails("forge_skill/unknown guide is rejected", "forge_skill", name="definitely-not-a-guide")
            except SetupAborted as exc:
                # A setup step could not produce the object the rig needs. Stop
                # the body but fall through to the report, so the cases that did
                # run are still listed instead of being lost with a traceback.
                record("SETUP/aborted", False, str(exc))
            except Exception as exc:  # noqa: BLE001
                # Anything else — an operator this Blender does not have, a
                # bridge error mid-step — must not take the report down with it
                # either, for the same reason.
                record("SETUP/unexpected", False, f"{type(exc).__name__}: {exc}")
            finally:
                shutil.rmtree(work_dir, ignore_errors=True)
                # The run started from a single empty scene, so whatever is here
                # now is this run's — including anything renamed, replicated or
                # imported.
                after = await raw("forge_scene_info")
                leftovers = scene_names(after[0])
                if leftovers:
                    response = await session.call_tool("forge_delete", {"names": leftovers})
                    print("CLEANUP:", (response.content[0].text or "")[:200])
                # Counted whatever the outcome: the coverage check asks whether
                # the tool was exercised, and reaching here means it was.
                used.add("forge_delete")

                # Whatever the run left anywhere — extra scenes from
                # include/import, orphaned objects, replicate's collections — is
                # removed by diffing against the pre-run snapshot, so the next
                # run does not trip its own guard on these leftovers.
                data, purge_error, purge_text, _ = await raw(
                    "forge_execute",
                    code=_RESTORE_CODE.replace("__KEEP__", repr(snapshot)).replace(
                        "__PROPS__", repr(inventory.get("forge_props") or {})
                    ),
                )
                if purge_error:
                    # Silence here would let a dirty file pass as a clean run.
                    record("CLEANUP/restore pre-run file state", False, purge_text[:300])
                else:
                    restored = (
                        (data.get("scenes") or []) + (data.get("objects") or []) + (data.get("collections") or [])
                    )
                    if restored:
                        print("CLEANUP restored:", ", ".join(restored))
                    record("CLEANUP/restore pre-run file state", True)

            missing = sorted(registered - used)
            record(
                f"COVERAGE/all {len(registered)} registered tools exercised", not missing, f"never called: {missing}"
            )

            for label, status in cases:
                print(f"[{status}] {label}")

            print(
                f"TOOL COVERAGE RESULT: {'FAIL' if failures else 'PASS'}; "
                f"tools={len(used)}/{len(registered)} cases={len(cases)} failures={len(failures)}"
            )
            return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
