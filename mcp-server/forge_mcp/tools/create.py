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

"""Create commands — mirror ``bpy.ops.forge.create_*`` (see forge_mcp/skills/forge_create.md).

Every tool takes ``select`` (object names): selection is replaced with that list
(order matters — first becomes active) before the operator runs. ``None`` leaves
the current selection untouched. Results include ``created`` — names of new
scene objects (scene diff across the call), so generated names never need
guessing.
"""

from __future__ import annotations

from typing import Literal

from .. import call_blender, mcp
from ..blender import op_call
from ._hints import WRITE

# ── Enums ─────────────────────────────────────────────────────────────

VisualGeometryType = Literal["BOX", "CAPSULE", "CYLINDER", "SPHERE"]
ColliderGeometryType = Literal["BOX", "CAPSULE", "CYLINDER", "SPHERE", "MESH", "SDF"]
JointType = Literal["FREE", "BALL", "SLIDE", "HINGE"]
ActuatorType = Literal["GENERAL", "MOTOR", "POSITION", "VELOCITY", "ADHESION"]
TendonType = Literal["FIXED"]
EqualityType = Literal["CONNECT", "WELD", "JOINT"]
ContactType = Literal["EXCLUDE", "PAIR"]
SensorType = Literal[
    "Jointpos",
    "Jointvel",
    "Touch",
    "Accelerometer",
    "Velocimeter",
    "Gyro",
    "Framepos",
    "Framequat",
    "Framexaxis",
    "Frameyaxis",
    "Framezaxis",
    "Framelinvel",
    "Frameangvel",
    "Contact",
    "Subtreecom",
    "Subtreelinvel",
    "Subtreeangmom",
]
LightType = Literal["DIRECTIONAL", "SPOT", "POINT"]
TrackMode = Literal["FIXED", "TRACK", "TRACKCOM", "TARGETBODY", "TARGETBODYCOM"]
CameraType = Literal["PERSPECTIVE", "ORTHOGRAPHIC"]
ColliderMethod = Literal["GEOMETRY_TYPE", "COLLIDER_TYPE"]


def _deferred_creation_call(op_name: str, label: str, select: list[str] | None, setup: str) -> str:
    """Build Blender code for a create operator that may continue as a modal job."""
    lines = [
        "import bpy",
        "scene = bpy.data.scenes[bpy.context.scene.Main_Scene]",
        "props = scene.Forge_Props",
        setup,
        "if props.modal_operation_active:",
        '    raise RuntimeError(f"Forge modal operation already running: {props.modal_operation_name}")',
        "before = set(scene.objects)",
    ]
    if select is not None:
        names = ", ".join(repr(name) for name in select)
        lines += [
            "bpy.ops.object.select_all(action='DESELECT')",
            "for obj in bpy.data.objects:",
            "    if 'selected_order' in obj:",
            "        del obj['selected_order']",
            f"for order, name in enumerate([{names}]):",
            "    obj = bpy.data.objects[name]",
            "    obj['selected_order'] = order",
            "    obj.select_set(True)",
        ]
        if select:
            lines.append(f"bpy.context.view_layer.objects.active = bpy.data.objects[{select[0]!r}]")
        else:
            lines.append("bpy.context.view_layer.objects.active = None")

    lines += [
        "props.modal_operation_deferred = True",
        "try:",
        f"    ret = bpy.ops.forge.{op_name}()",
        "except BaseException:",
        "    props.modal_operation_deferred = False",
        "    # The operator claimed the scene-level modal slot before failing, and",
        "    # nothing else releases it — every later operation would be refused as",
        "    # 'already running' for the rest of the session.",
        "    if props.modal_operation_active and props.modal_operation_status != 'RUNNING':",
        "        props.modal_operation_active = False",
        '        props.modal_operation_token = ""',
        "    raise",
        "if 'CANCELLED' in ret:",
        "    props.modal_operation_deferred = False",
        "    if props.modal_operation_active and props.modal_operation_status != 'RUNNING':",
        "        props.modal_operation_active = False",
        '        props.modal_operation_token = ""',
        f'    raise RuntimeError("{label} failed to start")',
        "if 'RUNNING_MODAL' in ret:",
        "    operation_token = props.modal_operation_token",
        "    if not operation_token:",
        "        props.modal_operation_deferred = False",
        f'        raise RuntimeError("{label} did not publish an operation token")',
        "",
        "    def release_operation():",
        "        if props.modal_operation_token == operation_token:",
        "            props.modal_operation_active = False",
        "            props.modal_operation_deferred = False",
        '            props.modal_operation_token = ""',
        "",
        "    def check_is_finished():",
        "        if props.modal_operation_token != operation_token:",
        f'            raise RuntimeError("{label} operation state was replaced")',
        "        if props.modal_operation_status == 'RUNNING':",
        "            return None",
        "        status = props.modal_operation_status",
        f'        message = props.modal_operation_message or f"{label} ended with {{status}}"',
        "        release_operation()",
        "        if status != 'FINISHED':",
        "            raise RuntimeError(message)",
        "        return {",
        '            "return_value": ["FINISHED"],',
        '            "objects": [obj.name for obj in scene.objects if obj.select_get()],',
        '            "created": [obj.name for obj in scene.objects if obj not in before],',
        "        }",
        "",
        "    def cancel_operation():",
        "        if props.modal_operation_token == operation_token:",
        "            if props.modal_operation_status == 'RUNNING':",
        "                if bpy.app.background:",
        "                    release_operation()",
        "                else:",
        "                    props.modal_operation_deferred = False",
        "                    props.cancel_requested = True",
        "            else:",
        "                release_operation()",
        "",
        "    result = {}",
        "else:",
        "    props.modal_operation_deferred = False",
        "    # Finished without going modal: the operator still claimed the",
        "    # scene-level modal slot in begin_modal_operation, and nothing releases",
        "    # it on this path, so every later operation would be refused as",
        "    # 'already running'.",
        "    if props.modal_operation_active and props.modal_operation_status != 'RUNNING':",
        "        props.modal_operation_active = False",
        '        props.modal_operation_token = ""',
        "    result = {",
        '        "return_value": list(ret),',
        '        "objects": [obj.name for obj in scene.objects if obj.select_get()],',
        '        "created": [obj.name for obj in scene.objects if obj not in before],',
        "    }",
    ]
    return "\n".join(lines)


# ── Link / Inertial / Joint ───────────────────────────────────────────


@mcp.tool(annotations=WRITE, name="forge_create_link")
def create_link(select: list[str] | None = None) -> dict:
    """Create a `link` (mjcf body), optionally based on selected object(s).

    - Select none: create at 3d cursor location.
    - Select `link` / `frame` / `replicate`: new link at local space [0, 0, 0].
    - Select `visual` / `collider` whose parent is `link` / `frame` / `replicate`: new link parented under that
      parent, at the selected object's local position, rotation zeroed.
    - Select `visual` / `collider` without parent in `[LINK, FRAME, REPLICATE]`: new link at the selected object's
      location, marked as `Root Link`.
    """
    return call_blender(op_call("create_link", select=select))


@mcp.tool(annotations=WRITE, name="forge_create_inertial")
def create_inertial(select: list[str] | None = None) -> dict:
    """Create an `inertial` object as child of the selected `link`.

    - Uses the operator defaults: VISUAL geometry and no optional mesh validation.
      Collects geometry recursively through Frame children, excluding child Links.
    - Primitive shapes use analytic mass and inertia; Mesh geometry requires TetGen.
    - Creates new inertials without replacing existing ones. Use the documented
      operator through forge_execute for COLLIDER input or check_mesh_valid=True.
    """
    return call_blender(op_call("create_inertial", select=select))


@mcp.tool(annotations=WRITE, name="forge_create_joint")
def create_joint(joint_type: JointType = "HINGE", select: list[str] | None = None) -> dict:
    """Create a `joint` object as child of the selected `link`.

    - The exported rotation / slide axis is the joint object's local +Z in parent space — rotate the joint object
      (e.g. euler) so its Z points along the desired world axis.
    """
    return call_blender(op_call("create_joint", select=select, joint_type=joint_type))


# ── Geometry / Collider / Site ────────────────────────────────────────


@mcp.tool(annotations=WRITE, name="forge_create_geometry")
def create_geometry(
    geometry_type: VisualGeometryType,
    size_box: tuple[float, float, float] = (1.0, 1.0, 1.0),
    size_radius: float = 0.5,
    size_height: float = 1.0,
    select: list[str] | None = None,
) -> dict:
    """Create a `visual` geometry object, optionally based on selected object(s).

    - Select none: create at 3d cursor location.
    - Select `link` / `frame` / `replicate`: create one geometry per selected object as child of it, at local space
      [0, 0, 0].
    - Parameter used per `geometry_type`: BOX -> `size_box`; CAPSULE / CYLINDER -> `size_radius` + `size_height`;
      SPHERE -> `size_radius`.
    - Size unit: meter; sizes are full dimensions (BOX) / actual radius and height, exported to mjcf half-extents
      automatically.
    """
    return call_blender(
        op_call(
            "create_geometry",
            select=select,
            geometry_type=geometry_type,
            size_box=size_box,
            size_radius=size_radius,
            size_height=size_height,
        )
    )


@mcp.tool(annotations=WRITE, name="forge_create_collider")
def create_collider(
    collider_type: ColliderGeometryType = "BOX",
    create_method: ColliderMethod = "GEOMETRY_TYPE",
    auto_size: bool = False,
    min_is_height: bool = False,
    size_box: tuple[float, float, float] = (1.0, 1.0, 1.0),
    size_radius: float = 0.5,
    size_height: float = 1.0,
    select: list[str] | None = None,
) -> dict:
    """Create a `collider` object, optionally based on selected object(s).

    - `GEOMETRY_TYPE`: only for selected `visual` object(s), auto-detects shape from the selected visual and
      **ignores `collider_type`** — the collider takes the visual's own geometry type; size params not used.
      `collider_type` may be omitted in this method.
    - `COLLIDER_TYPE`: explicit `collider_type`; the only method when selecting none or `link` / `frame` /
      `replicate` objects.
    - `collider_type` MESH only available when `visual` object(s) selected; bakes visual geometry to a convex mesh
      collider, no size params needed.
    - `collider_type` SDF only available when `visual` object(s) selected; shares the visual's Mesh Data as a linked
      duplicate, preserving its parent and transform. Vertex edits affect both objects.
    - `auto_size`: auto-detect size from the selected `visual` geometry (default off). It is ignored when the
      selection is a `link` / `frame` / `replicate`: there is no selected visual to measure, so the collider is
      built at the default size (BOX 1 1 1; CAPSULE / CYLINDER radius 0.5, height 1.0) with no error raised — pass
      `size_box` / `size_radius` / `size_height` explicitly for those.
    - `min_is_height`: CAPSULE / CYLINDER only. When True the height comes from the selected visual's **smallest**
      bounding-box axis instead of its largest, and the shape is oriented along that axis. Only takes effect with
      `auto_size=True`; with explicit `size_radius` / `size_height` the values are used as given and the flag is
      ignored. `auto_size` from a `link` / `frame` / `replicate` is likewise unaffected.
    - Size unit: meter.
    """
    return call_blender(
        op_call(
            "create_collider",
            select=select,
            collider_type=collider_type,
            create_method=create_method,
            auto_size=auto_size,
            use_min_as_height=min_is_height,
            size_box=size_box,
            size_radius=size_radius,
            size_height=size_height,
        )
    )


@mcp.tool(annotations=WRITE, name="forge_create_height_field")
def create_height_field(select: list[str] | None = None) -> dict:
    """Create an `hfield` object (mjcf geom type hfield).

    - Only when nothing selected; exists as root node without parent.
    - Default location at 3d cursor location.
    """
    return call_blender(op_call("create_height_field", select=select))


@mcp.tool(annotations=WRITE, name="forge_create_plane")
def create_plane(select: list[str] | None = None) -> dict:
    """Create a `plane` object (mjcf geom type plane).

    - Only when nothing selected; exists as root node without parent.
    - Default location at 3d cursor location.
    """
    return call_blender(op_call("create_plane", select=select))


@mcp.tool(annotations=WRITE, name="forge_create_site")
def create_site(
    site_type: VisualGeometryType,
    size_box: tuple[float, float, float] = (0.2, 0.2, 0.2),
    size_radius: float = 0.1,
    size_height: float = 0.2,
    select: list[str] | None = None,
) -> dict:
    """Create a `site` object as child of the selected `link` object(s).

    - Parameter used per `site_type`: BOX -> `size_box`; CAPSULE / CYLINDER -> `size_radius` + `size_height`;
      SPHERE -> `size_radius`.
    - Size unit: meter.
    """
    return call_blender(
        op_call(
            "create_site",
            select=select,
            site_type=site_type,
            size_box=size_box,
            size_radius=size_radius,
            size_height=size_height,
        )
    )


# ── Actuator / Tendon / Equality / Contact / Sensor ───────────────────


@mcp.tool(annotations=WRITE, name="forge_create_actuator")
def create_actuator(actuator_type: ActuatorType = "POSITION", select: list[str] | None = None) -> dict:
    """Create an `actuator` object based on selected `link` | `joint` | `tendon` object(s)."""
    return call_blender(op_call("create_actuator", select=select, actuator_type=actuator_type))


@mcp.tool(annotations=WRITE, name="forge_create_tendon")
def create_tendon(tendon_type: TendonType = "FIXED", select: list[str] | None = None) -> dict:
    """Create a `tendon` object from selected `joint` object(s).

    - Need at least 2 selected `joint` objects; creates a single tendon from the ordered selection.
    - Only supports joint subtype [SLIDE, HINGE].
    - `tendon_type` currently only `FIXED`.
    """
    return call_blender(op_call("create_tendon", select=select, tendon_type=tendon_type))


@mcp.tool(annotations=WRITE, name="forge_create_equality")
def create_equality(equality_type: EqualityType, select: list[str] | None = None) -> dict:
    """Create an `equality` object from exactly 2 selected `link` | `joint` | `site` objects.

    - Selected `joint` objects -> `equality_type` is `JOINT`.
    - Selected `link` / `site` objects -> `equality_type` is `CONNECT` or `WELD`.
    """
    return call_blender(op_call("create_equality", select=select, equality_type=equality_type))


@mcp.tool(annotations=WRITE, name="forge_create_contact")
def create_contact(contact_type: ContactType, select: list[str] | None = None) -> dict:
    """Create `contact` object(s) from selected `link` | `visual` | `collider` | `plane` | `hfield` objects.

    - Need at least 2 selected objects.
    - Selected `link` objects -> `contact_type` is `EXCLUDE`.
    - Selected `visual` / `collider` / `plane` / `hfield` objects -> `contact_type` is `PAIR`.
    - Creates one `contact` for each pair combination of selected objects.
    """
    return call_blender(op_call("create_contact", select=select, contact_type=contact_type))


@mcp.tool(annotations=WRITE, name="forge_create_sensor")
def create_sensor(
    sensor_type: SensorType,
    set_ref: bool = False,
    set_xbody: bool = False,
    set_subtree: bool = False,
    select: list[str] | None = None,
) -> dict:
    """Create `sensor` object(s) based on selected `link` | `joint` | `site` | `visual` | `collider` | `camera` objects.

    - Available `sensor_type` is decided by the selected target model type:
      joint -> Jointpos / Jointvel; site -> Touch ~ Frameangvel + Contact; link -> Framepos ~ Frameangvel + Contact
      + Subtreecom / Subtreelinvel / Subtreeangmom;
      link with `set_xbody` -> frame types only; link with `set_subtree` -> Contact only; visual / collider -> frame
      types + Contact; camera -> frame types only.
    - `set_ref=True`: need 2 selected objects, first is target, second is reference.
    - `set_xbody` / `set_subtree` only for `link` target, mutually exclusive.
    """
    # The addon declares set_ref / set_xbody / set_subtree *before* Sensor_Type,
    # and Blender assigns operator arguments in RNA declaration order rather
    # than call order — so the dynamic enum is always assigned last, after the
    # flag update callbacks that reset it. False defaults are omitted only to
    # skip a pointless reset; the resulting type no longer depends on this order.
    params = {}
    if set_ref:
        params["set_ref"] = True
    if set_xbody:
        params["set_xbody"] = True
    if set_subtree:
        params["set_subtree"] = True
    params["Sensor_Type"] = sensor_type
    # The candidate types are read from the addon's own dynamic enum instead of
    # being restated here, so the two cannot drift apart. The target is derived
    # the way the operator derives it: ordered by the ``selected_order`` tag,
    # untagged objects last.
    validation = (
        "def _allowed_sensor_types():\n"
        "    try:\n"
        "        from Forge.ops.creation import Forge_OT_Sensor_Creation as _Op\n"
        "        probe = type('_Probe', (), {})()\n"
        "        probe.set_ref = set_ref\n"
        "        probe.set_xbody = set_xbody\n"
        "        probe.set_subtree = set_subtree\n"
        "        return {item[0] for item in _Op.sensor_enum_items(probe, bpy.context)}\n"
        "    except Exception:\n"
        "        # Fail open: the operator's own enum error is clearer than a wrong block.\n"
        "        return set()\n"
        "selected = list(bpy.context.selected_objects)\n"
        "tagged = sorted((o for o in selected if o.get('selected_order', -1) >= 0), "
        "key=lambda o: o['selected_order'])\n"
        "ordered = tagged + [o for o in selected if o.get('selected_order', -1) < 0]\n"
        "model_types = [obj.Forge_Model_Type for obj in ordered]\n"
        f"requested = {sensor_type!r}\n"
        f"set_ref = {set_ref!r}; set_xbody = {set_xbody!r}; set_subtree = {set_subtree!r}\n"
        "if set_xbody and set_subtree:\n"
        "    raise RuntimeError('sensor_type validation failed: set_xbody and set_subtree are mutually exclusive')\n"
        "if set_ref and len(model_types) != 2:\n"
        "    raise RuntimeError(f'sensor_type validation failed: set_ref requires exactly 2 selected objects, "
        "got {len(model_types)}')\n"
        "target = model_types[0] if model_types else None\n"
        "if (set_xbody or set_subtree) and target != 'LINK':\n"
        "    raise RuntimeError(f'sensor_type validation failed: set_xbody/set_subtree require a LINK target, "
        "got {target!r}')\n"
        "if set_ref and target == 'JOINT':\n"
        "    raise RuntimeError('sensor_type validation failed: JOINT cannot be used with set_ref')\n"
        "allowed = _allowed_sensor_types()\n"
        "if allowed and requested not in allowed:\n"
        "    raise RuntimeError(f'sensor_type {requested!r} is not valid for target {target!r} "
        "with the selected flags; allowed: {sorted(allowed)}')"
    )
    return call_blender(op_call("create_sensor", select=select, post_select_setup=validation, **params))


# ── Light / Camera / Frame / Replicate ────────────────────────────────


@mcp.tool(annotations=WRITE, name="forge_create_light")
def create_light(light_type: LightType, light_mode: TrackMode, select: list[str] | None = None) -> dict:
    """Create `light` object(s), optionally based on selected `link` object(s).

    - Select none: world light at 3d cursor location, `light_type` in [DIRECTIONAL, SPOT, POINT], `light_mode` in
      [FIXED, TRACK, TRACKCOM].
    - Select 1-2 `link`s: `light_type` in [SPOT, POINT], all `light_mode`; with 1 `link`, TARGETBODY / TARGETBODYCOM
      creates a single world light at the 3d cursor targeting the selected `link`; with 2 `link`s, first selected is
      light position, second is target; other modes create one light per selected `link` as child of it.
    - Select 3+ `link`s: `light_mode` in [FIXED, TRACK, TRACKCOM], one light per selected `link` as child of it.
    """
    return call_blender(op_call("create_light", select=select, light_type=light_type, light_mode=light_mode))


@mcp.tool(annotations=WRITE, name="forge_create_camera")
def create_camera(camera_type: CameraType, camera_mode: TrackMode, select: list[str] | None = None) -> dict:
    """Create `camera` object(s), optionally based on selected `link` object(s).

    - Select none: world camera at 3d cursor location, `camera_mode` in [FIXED, TRACK, TRACKCOM].
    - Select 1 `link`: all `camera_mode`; TARGETBODY / TARGETBODYCOM creates a single world camera at the 3d cursor
      targeting the selected `link`, other modes create one camera per selected `link` as child of it.
    - Select 2 `link`s: all `camera_mode`; TARGETBODY / TARGETBODYCOM creates a single camera, first selected is
      camera position, second is target; other modes create one camera per selected `link` as child of it.
    - Select 3+ `link`s: `camera_mode` in [FIXED, TRACK, TRACKCOM], one camera per selected `link` as child of it.
    """
    return call_blender(op_call("create_camera", select=select, camera_type=camera_type, camera_mode=camera_mode))


@mcp.tool(annotations=WRITE, name="forge_create_frame")
def create_frame(select: list[str] | None = None) -> dict:
    """Create a `frame` object, optionally based on selected `link` | `frame` | `replicate` object(s).

    - Select none: create at 3d cursor location.
    - Select objects: create one frame per selected object as child of it.
    """
    return call_blender(op_call("create_frame", select=select))


@mcp.tool(annotations=WRITE, name="forge_create_replicate")
def create_replicate(
    count: int = 0,
    sep: str = "",
    offset: tuple[float, float, float] = (0.0, 0.0, 0.0),
    euler: tuple[float, float, float] = (0.0, 0.0, 0.0),
    select: list[str] | None = None,
) -> dict:
    """Create a `replicate` object, selected objects as its source.

    - Selection types: `camera` | `light` | `visual` | `collider` | `site` | `link` | `frame` | `attach` | `replicate`.
    - `count`: replicate count; `sep`: separator string; `offset`: offset vector between copies; `euler`: euler
      rotation between copies.
    """
    return call_blender(op_call("create_replicate", select=select, count=count, sep=sep, offset=offset, euler=euler))


# ── Attach / Include ──────────────────────────────────────────────────


@mcp.tool(annotations=WRITE, name="forge_create_attach")
def create_attach(
    file: str,
    model: str | None = None,
    prefix: str | None = None,
    link: str | None = None,
    select: list[str] | None = None,
) -> dict:
    """Attach a model from an external mjcf file, optionally based on selected `link` | `frame` | `replicate` object.

    - Need exactly 1 selected object or none.
    - Sets `Forge_Temp_Props.tmp_file` (model / prefix / link auto-derived from the file); optional `model` / `prefix`
      / `link` override the derived values.
    - Imports the external model into the scene, then creates the attach reference.
    - Requires `Forge Library` asset library (Preferences -> File Paths -> Asset Libraries).
    - Long-running import (modal): waits for Blender to finish and returns the final created object names.
    """
    setup = [
        "scene = bpy.data.scenes[bpy.context.scene.Main_Scene]",
        "temp = scene.Forge_Temp_Props",
        f"temp.tmp_file = {file!r}",
    ]
    if model is not None:
        setup.append(f"temp.tmp_model = {model!r}")
    if prefix is not None:
        setup.append(f"temp.tmp_prefix = {prefix!r}")
    if link is not None:
        setup.append(f"temp.tmp_link = {link!r}")
    return call_blender(_deferred_creation_call("create_attach", "Attach", select, "\n".join(setup)))


@mcp.tool(annotations=WRITE, name="forge_create_include")
def create_include(file: str, select: list[str] | None = None) -> dict:
    """Add an `include` reference for an external mjcf file; only when nothing selected.

    - Sets `Forge_Temp_Props.tmp_include` then creates the include.
    - Only an `<include>` tag is added on export; the file content is not exported.
    - Waits for Blender's modal import to finish and returns the final created object names.
    """
    setup = (
        "scene = bpy.data.scenes[bpy.context.scene.Main_Scene]\n"
        "temp = scene.Forge_Temp_Props\n"
        f"temp.tmp_include = {file!r}"
    )
    return call_blender(_deferred_creation_call("create_include", "Include", select, setup))


@mcp.tool(annotations=WRITE, name="forge_create_material")
def create_material(
    category: str,
    material: str,
    use_existing: bool = True,
    select: list[str] | None = None,
) -> dict:
    """Create a Forge-library PBR material and assign it to selected `VISUAL`, `HFIELD`, or `PLANE` objects.

    - `category` and `material` must exactly match the bundled library entries.
    - `use_existing=True` reuses a same-named datablock without rebuilding it;
      false always creates a fresh datablock (which Blender may suffix).
    - Assignment uses the first object-level material slot, creating it when empty.
    """
    return call_blender(
        op_call(
            "create_material",
            select=select,
            category=category,
            material=material,
            use_existing=use_existing,
        )
    )
