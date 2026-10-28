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

"""Generic scene-editing tools — direct bpy access for operations the Forge
operators don't cover: transforms, shape sizes, renames, deletes, inspection
and measurements. See forge_mcp/skills/forge_modify.md for parameter conventions.
"""

from __future__ import annotations

from typing import Literal

from .. import call_blender, mcp
from ._hints import DESTRUCTIVE, READ_ONLY, WRITE

SceneConfigGroup = Literal[
    "forge_props",
    "g_compiler",
    "g_option",
    "g_option.flag",
    "g_statistic",
    "v_global",
    "v_headlight",
    "v_map",
    "v_rgba",
    "v_quality",
    "v_tonemapping",
    "v_ssgi",
]

_SCENE_CONFIG_PATHS = {
    "forge_props": "Forge_Props",
    "g_compiler": "Forge_GlobalConfig.g_compiler",
    "g_option": "Forge_GlobalConfig.g_option",
    "g_option.flag": "Forge_GlobalConfig.g_option.flag",
    "g_statistic": "Forge_GlobalConfig.g_statistic",
    "v_global": "Forge_VisualConfig.v_global",
    "v_headlight": "Forge_VisualConfig.v_headlight",
    "v_map": "Forge_VisualConfig.v_map",
    "v_rgba": "Forge_VisualConfig.v_rgba",
    "v_quality": "Forge_VisualConfig.v_quality",
    "v_tonemapping": "Forge_VisualConfig.v_tonemapping",
    "v_ssgi": "Forge_VisualConfig.v_ssgi",
}

# ── Inspection ────────────────────────────────────────────────────────

# Blender-side mapping shared by the code templates below: a Forge model type
# to its property group. Geometry-flavored types (visual / collider / site /
# plane / hfield) all share Forge_Geometry (GeomItem); FRAME and UNDEFINED
# carry no parameter group. Brace-free so it can live inside .format() templates.
#
# The mapping is written once, as an expression, because `forge_set_property`
# binds its group inline instead of calling the helper below: writing the group
# through a literal-bearing expression is what lets `required_skills_for_code`
# see the `Forge_` access and gate the write as the direct property access the
# modify guide governs (see "Direct property access" in skills/forge_modify.md).
# A helper call is opaque to it, which left that gate riding an unrelated branch
# of the same template.
_PROP_GROUP_EXPR = (
    '"Forge_Geometry" if model_type in ("VISUAL", "COLLIDER", "HFIELD", "PLANE", "SITE") '
    'else "Forge_" + model_type.title() if model_type and model_type not in ("UNDEFINED", "FRAME") else None'
)

# Read-only inspection is not gated, so `forge_object_info` can call the helper.
_PROP_GROUP_FN = f"""
def _prop_group_name(model_type):
    return {_PROP_GROUP_EXPR}
"""

_OBJECT_INFO_CODE = (
    _PROP_GROUP_FN
    + """
import bpy
from mathutils import Vector


def to_json(v):
    if isinstance(v, float):
        return round(v, 6)
    if isinstance(v, str) or isinstance(v, bool) or v is None:
        return v
    if isinstance(v, int):
        return v
    try:  # Vector / bpy_prop_array / tuple / list -> plain list
        return [to_json(x) for x in v]
    except TypeError:
        return str(v)


obj = bpy.data.objects[{name!r}]
model_type = str(getattr(obj, "Forge_Model_Type", "UNDEFINED"))

info = {{
    "name": obj.name,
    "type": model_type,
    "parent": obj.parent.name if obj.parent else None,
    "children": [c.name for c in obj.children],
    "location": to_json(obj.location),
    "rotation_euler": to_json(obj.rotation_euler),
    "world_matrix": [to_json(row) for row in obj.matrix_world],
    "world_location": to_json(obj.matrix_world.to_translation()),
    "dimensions": to_json(obj.dimensions),
    "lock_location": to_json(obj.lock_location),
    "lock_rotation": to_json(obj.lock_rotation),
    "lock_scale": to_json(obj.lock_scale),
}}

def group_to_json(grp, depth=2):
    out = {{}}
    for p in grp.bl_rna.properties:
        pid = p.identifier
        if pid == "rna_type":
            continue
        try:
            v = getattr(grp, pid)
        except Exception:
            continue
        if p.type == "POINTER":
            if p.fixed_type.identifier == "Object":
                out[pid] = v.name if v else None
            elif depth > 0 and v is not None:
                out[pid] = group_to_json(v, depth - 1)
        elif p.type == "COLLECTION":
            out[pid] = [group_to_json(it, depth - 1) for it in v]
        else:
            out[pid] = to_json(v)
    return out

props = None
group_name = _prop_group_name(model_type)
if group_name and hasattr(obj, group_name):
    item = getattr(obj, group_name)
    if hasattr(item, "bl_rna"):
        props = group_to_json(item)
info["props"] = props

mods = {{}}
for m in obj.modifiers:
    sockets = {{}}
    inputs = getattr(getattr(m, "properties", None), "inputs", None)
    if inputs is not None:
        # Blender 5.2+ stores node inputs as RNA socket-value properties.
        for prop in inputs.bl_rna.properties:
            key = prop.identifier
            if key.startswith("Socket"):
                sockets[key] = to_json(getattr(inputs, key).value)
    else:
        try:
            for key, v in m.items():
                if key.startswith("Socket"):
                    sockets[key] = to_json(v)
        except TypeError:
            # Modifiers without IDProperties have no legacy socket values.
            pass
    mods[m.name] = sockets
info["modifiers"] = mods

if model_type == "JOINT" and hasattr(obj, "Forge_Joint"):
    ax = obj.matrix_local.to_3x3().transposed()[2].normalized()
    info["joint_axis_localZ_in_parent"] = [round(c, 6) for c in ax]
    info["joint_pos_in_parent"] = [round(c, 6) for c in obj.matrix_local.transposed()[3].xyz]

result = info
"""
)


@mcp.tool(annotations=READ_ONLY, name="forge_object_info")
def object_info(name: str) -> dict:
    """Inspect one object: model type, transforms (local + world), locks, dimensions, Forge property group values,
    shape-modifier sockets, and (for joints) the exported pos / axis.
    """
    return call_blender(_OBJECT_INFO_CODE.format(name=name))


@mcp.tool(annotations=READ_ONLY, name="forge_measure")
def measure(names: list[str]) -> dict:
    """World-space bounding boxes (min / max corners) and centers of the named objects — use to verify clearances,
    gaps and alignment.
    """
    code = """
import bpy
from mathutils import Vector

dg = bpy.context.evaluated_depsgraph_get()
out = {{}}
for n in {names!r}:
    obj = bpy.data.objects[n]
    eo = obj.evaluated_get(dg)
    corners = [eo.matrix_world @ Vector(c) for c in eo.bound_box]
    mins = [min(c[i] for c in corners) for i in range(3)]
    maxs = [max(c[i] for c in corners) for i in range(3)]
    out[n] = {{
        "min": [round(v, 6) for v in mins],
        "max": [round(v, 6) for v in maxs],
        "center": [round((a + b) / 2, 6) for a, b in zip(mins, maxs)],
    }}
result = out
""".format(names=names)
    return call_blender(code)


@mcp.tool(annotations=READ_ONLY, name="forge_scene_config")
def scene_config(group: SceneConfigGroup | None = None) -> dict:
    """Read one Forge scene configuration group, or every group when omitted."""
    code = """
import bpy

paths = {paths!r}
requested = {group!r}
scene = bpy.data.scenes[bpy.context.scene.Main_Scene]

def resolve(path):
    value = scene
    for part in path.split("."):
        value = getattr(value, part)
    return value

def to_json(value):
    if isinstance(value, (str, bool, int, float)) or value is None:
        return value
    if isinstance(value, bpy.types.ID):
        return value.name
    try:
        return [to_json(item) for item in value]
    except TypeError:
        return str(value)

def group_to_json(value):
    out = {{}}
    for prop in value.bl_rna.properties:
        key = prop.identifier
        if key == "rna_type" or prop.type == "COLLECTION":
            continue
        try:
            item = getattr(value, key)
        except Exception:
            continue
        if prop.type == "POINTER" and not isinstance(item, bpy.types.ID):
            continue
        out[key] = to_json(item)
    return out

names = [requested] if requested is not None else list(paths)
result = {{name: group_to_json(resolve(paths[name])) for name in names}}
""".format(paths=_SCENE_CONFIG_PATHS, group=group)
    return call_blender(code)


# ── Editing ───────────────────────────────────────────────────────────


@mcp.tool(annotations=WRITE, name="forge_set_transform")
def set_transform(
    name: str,
    location: tuple[float, float, float] | None = None,
    rotation_euler: tuple[float, float, float] | None = None,
    scale: tuple[float, float, float] | None = None,
) -> dict:
    """Set an object's local transform components (radians for euler). Only the provided components are changed;
    locked axes (Forge locks scale on most model objects) are skipped and reported while unlocked axes are updated.

    - Joint axis note: a joint's exported rotation axis is its local +Z in parent space — rotate euler so Z points
      along the desired world axis.
    """
    code = """
import bpy

obj = bpy.data.objects[{name!r}]
changed = {{}}
skipped = {{}}

def apply_unlocked(attribute, requested, locks):
    current = getattr(obj, attribute)
    locked_axes = []
    updated = False
    for index, (value, locked) in enumerate(zip(requested, locks)):
        if locked:
            locked_axes.append("XYZ"[index])
        else:
            current[index] = value
            updated = True
    if updated:
        changed[attribute] = list(current)
    if locked_axes:
        skipped[attribute] = {{"locked_axes": locked_axes}}

if {has_loc}:
    apply_unlocked("location", {location!r}, obj.lock_location)
if {has_rot}:
    apply_unlocked("rotation_euler", {rotation_euler!r}, obj.lock_rotation)
if {has_scale}:
    apply_unlocked("scale", {scale!r}, obj.lock_scale)
result = {{"name": obj.name, "changed": changed, "skipped": skipped}}
""".format(
        name=name,
        has_loc=location is not None,
        location=location,
        has_rot=rotation_euler is not None,
        rotation_euler=rotation_euler,
        has_scale=scale is not None,
        scale=scale,
    )
    return call_blender(code)


@mcp.tool(annotations=WRITE, name="forge_set_shape_size")
def set_shape_size(
    name: str,
    size: float | tuple[float, float] | tuple[float, float, float],
) -> dict:
    """Set the shape size of a `visual` / `collider` / `site` object by writing its shape-modifier sockets.

    - `size` meaning per shape type (same convention as the create operators):
        BOX -> full (x, y, z) dimensions tuple;
        SPHERE -> radius float;
        CAPSULE / CYLINDER -> (radius, height) tuple; height is the full length of the
        straight section (a capsule's caps extend beyond it: overall length = height + 2*radius).
    - Sizes are in meters, in the object's LOCAL space (the socket values, not world dims).
    """
    is_tuple = isinstance(size, (tuple, list))
    box = is_tuple and len(size) == 3
    pair = is_tuple and len(size) == 2
    code = """
import bpy

obj = bpy.data.objects[{name!r}]
shape = obj.Forge_Geometry.type
shape_mods = [m for m in obj.modifiers if m.name.startswith(("Geometry_", "Collider_", "Site_"))]
mod = next((m for m in shape_mods if m.name.lower().endswith("_" + shape.lower())), None)
if mod is None:
    raise RuntimeError(f"no shape modifier for {{shape}} on {{obj.name}}: {{[m.name for m in shape_mods]}}")

def _set_socket(mod, key, value):
    # Blender 5.2 moved modifier sockets to modifier.properties.inputs.
    inputs = getattr(getattr(mod, "properties", None), "inputs", None)
    if inputs is not None and hasattr(inputs, key):
        getattr(inputs, key).value = value
    else:
        mod[key] = value

size_sock, height_sock = ("Socket_0", "Socket_2") if obj.Forge_Model_Type == "VISUAL" else ("Socket_3", "Socket_4")

if {box!r}:  # BOX full dimensions
    if shape != "BOX":
        raise RuntimeError(f"3-tuple size only valid for BOX, object shape is {{shape}}")
    _set_socket(mod, size_sock, tuple(float(v) for v in {size!r}))
elif {pair!r}:  # CAPSULE / CYLINDER (radius, height)
    if shape not in ("CAPSULE", "CYLINDER"):
        raise RuntimeError(f"(radius, height) size only valid for CAPSULE / CYLINDER, object shape is {{shape}}")
    radius, height = {size!r}
    _set_socket(mod, size_sock, float(radius))
    _set_socket(mod, height_sock, max(0.01, float(height)))
else:        # SPHERE radius scalar
    if shape == "SPHERE":
        _set_socket(mod, size_sock, float({size!r}))
    else:
        raise RuntimeError(f"scalar size only valid for SPHERE, object shape is {{shape}}")
mod.node_group.interface_update(bpy.context)
result = {{"name": obj.name, "shape": shape, "modifier": mod.name}}
""".format(name=name, box=box, pair=pair, size=size)
    return call_blender(code)


@mcp.tool(annotations=WRITE, name="forge_set_property")
def set_property(name: str, values: dict[str, object]) -> dict:
    """Set Forge parameter-group properties on an object, e.g. `{{"mass": 2.0}}` for an inertial or
    `{{"damping": 0.1}}` for a joint.
    Property names per type are listed in forge_mcp/skills/forge_modify.md (`obj.Forge_<Type>.<property>`);
    visual / collider / site / plane / hfield
    objects all take GeomItem properties (contype, conaffinity, friction, density, ...).

    - Object-target properties (sensor/equality/contact/light/camera/actuator `target`, ...) accept the target object's
      name as a string, or null to clear.
    - Multi-select enum flags (e.g. contact sensor `data`) accept a list of identifiers.
    - For Blender-native data (light energy, camera angle) prefix keys with `data:` to write onto `obj.data`.
    """
    entries = ", ".join(f"{k!r}: {v!r}" for k, v in values.items())
    code = """
import bpy

obj = bpy.data.objects[{name!r}]
model_type = getattr(obj, "Forge_Model_Type", "UNDEFINED")
group_name = (
    {group_expr}
)
group = getattr(obj, group_name, None) if group_name else None

set_vals = {{}}
skipped = {{}}

for key, val in {entries}.items():
    if key.startswith("data:"):
        target, attr = obj.data, key[5:]
    elif group is not None and hasattr(group, key):
        target, attr = group, key
    elif group is not None:
        avail = [
            p.identifier for p in group.bl_rna.properties
            if p.identifier != "rna_type"
        ]
        skipped[key] = f"no such property; available: {{', '.join(avail)}}"
        continue
    else:
        skipped[key] = f"model type {{model_type!r}} has no property group"
        continue

    pdef = target.bl_rna.properties[attr]
    if pdef.type == "POINTER":
        if pdef.fixed_type.identifier != "Object":
            skipped[key] = "only Object pointer properties are supported"
            continue
        if isinstance(val, str):
            resolved = bpy.data.objects.get(val)
            if resolved is None:
                skipped[key] = f"object {{val!r}} not found"
                continue
            val = resolved
        elif val is not None:
            skipped[key] = "pointer expects an object name string or null"
            continue
    elif pdef.type == "ENUM" and pdef.is_enum_flag and isinstance(val, list):
        val = set(val)

    try:
        previous = getattr(target, attr)
        # Blender exposes FloatVectorProperty values as ``bpy_prop_array``
        # objects.  Keep an independent snapshot so a failed write can be
        # restored; retaining the live RNA array would observe the new value.
        previous_snapshot = list(previous) if isinstance(val, (list, tuple)) else previous
        setattr(target, attr, val)
        # Blender applies a PointerProperty / enum write only when the property's
        # poll accepts the value and silently keeps the old one otherwise. Read
        # back so a dropped write is reported instead of looking like success.
        actual = getattr(target, attr)
        if isinstance(val, bpy.types.Object):
            landed = actual is val
            shown = actual.name if isinstance(actual, bpy.types.Object) else None
        elif isinstance(val, set):
            landed = set(actual) == val
            shown = sorted(actual)
        elif isinstance(val, float):
            landed = actual is not None and abs(actual - val) <= 1e-6 * max(1.0, abs(val))
            shown = actual
        elif isinstance(val, (list, tuple)):
            # JSON arrays arrive as Python lists while Blender returns
            # ``bpy_prop_array``.  Compare element-wise after normalizing both
            # sides, with a float tolerance matching scalar writes.
            try:
                expected = list(val)
                observed = list(actual)
                landed = (
                    len(observed) == len(expected)
                    and all(
                        abs(float(observed_item) - float(expected_item))
                        <= 1e-6 * max(1.0, abs(float(expected_item)))
                        for observed_item, expected_item in zip(observed, expected)
                    )
                )
                shown = observed
            except (TypeError, ValueError):
                landed = False
                shown = actual
        else:
            landed = actual == val
            shown = actual
        if not landed:
            # A pointer property whose poll rejects the value lands as NULL, so
            # the failed write would silently wipe an existing reference. Put the
            # previous value back and report the no-op.
            try:
                setattr(target, attr, previous_snapshot)
            except Exception:
                pass
            skipped[key] = "value was not applied; the property rejects this value (previous value restored)"
            continue
        set_vals[key] = shown
    except Exception as e:
        skipped[key] = str(e)
result = {{"name": obj.name, "type": model_type, "set": set_vals, "skipped": skipped}}
""".format(name=name, entries="{" + entries + "}", group_expr=_PROP_GROUP_EXPR)
    return call_blender(code)


@mcp.tool(annotations=WRITE, name="forge_set_scene_property")
def set_scene_property(group: SceneConfigGroup, values: dict[str, object]) -> dict:
    """Set direct properties on a Forge scene configuration group.

    Use `forge_scene_config(group)` first. Groups cover file workflow settings
    (`forge_props`), global compiler/option/statistic settings and visual groups.
    Unknown/read-only properties are skipped and reported.
    """
    entries = ", ".join(f"{key!r}: {value!r}" for key, value in values.items())
    code = """
import bpy

paths = {paths!r}
scene = bpy.data.scenes[bpy.context.scene.Main_Scene]
target = scene
for part in paths[{group!r}].split("."):
    target = getattr(target, part)

set_vals = {{}}
skipped = {{}}

def normalize(value):
    if isinstance(value, bpy.types.ID):
        return value.name
    if isinstance(value, set):
        return sorted(value)
    if isinstance(value, (str, bool, int, float)) or value is None:
        return value
    try:
        return [normalize(item) for item in value]
    except TypeError:
        return str(value)

def matches(actual, expected):
    if isinstance(expected, bpy.types.ID):
        return actual is expected
    if isinstance(expected, set):
        try:
            return set(actual) == expected
        except TypeError:
            return False
    if isinstance(expected, float):
        try:
            return abs(float(actual) - expected) <= 1e-6 * max(1.0, abs(expected))
        except (TypeError, ValueError):
            return False
    if isinstance(expected, (list, tuple)):
        try:
            observed = list(actual)
            return len(observed) == len(expected) and all(
                abs(float(observed_item) - float(expected_item))
                <= 1e-6 * max(1.0, abs(float(expected_item)))
                for observed_item, expected_item in zip(observed, expected)
            )
        except (TypeError, ValueError):
            return False
    return actual == expected

for key, val in {entries}.items():
    if not hasattr(target, key):
        available = [p.identifier for p in target.bl_rna.properties if p.identifier != "rna_type"]
        skipped[key] = f"no such property; available: {{', '.join(available)}}"
        continue
    prop = target.bl_rna.properties[key]
    if prop.is_readonly:
        skipped[key] = "read-only"
        continue
    if prop.type == "POINTER":
        fixed = prop.fixed_type.identifier
        collections = {{"Object": bpy.data.objects, "Collection": bpy.data.collections, "Scene": bpy.data.scenes}}
        if val is None:
            pass
        elif isinstance(val, str) and fixed in collections:
            val = collections[fixed].get(val)
            if val is None:
                skipped[key] = f"{{fixed}} not found"
                continue
        else:
            skipped[key] = f"pointer expects a {{fixed}} name string or null"
            continue
    elif prop.type == "ENUM" and prop.is_enum_flag and isinstance(val, list):
        val = set(val)
    try:
        previous = getattr(target, key)
        previous_snapshot = list(previous) if isinstance(val, (list, tuple)) else previous
        setattr(target, key, val)
        actual = getattr(target, key)
        if not matches(actual, val):
            try:
                setattr(target, key, previous_snapshot)
            except Exception:
                pass
            skipped[key] = "value was not applied; the property rejected this value (previous value restored)"
            continue
        set_vals[key] = normalize(actual)
    except Exception as error:
        skipped[key] = str(error)
result = {{"group": {group!r}, "set": set_vals, "skipped": skipped}}
""".format(paths=_SCENE_CONFIG_PATHS, group=group, entries="{" + entries + "}")
    return call_blender(code)


@mcp.tool(annotations=WRITE, name="forge_set_tendon_targets")
def set_tendon_targets(name: str, targets: list[dict[str, object]]) -> dict:
    """Replace a fixed tendon's ordered joint path.

    Each item is `{"target": "joint_object_name", "coef": 0.5}`. `coef`
    defaults to 0.5 when omitted. The target must be a Forge `JOINT`; order is
    preserved exactly and is the order written to MJCF.
    """
    code = """
import bpy

obj = bpy.data.objects[{name!r}]
if obj.Forge_Model_Type != "TENDON":
    raise RuntimeError(f"{{obj.name}} is not a Forge TENDON")
resolved = []
for index, spec in enumerate({targets!r}):
    target_name = spec.get("target")
    target = bpy.data.objects.get(target_name) if isinstance(target_name, str) else None
    if target is None:
        raise RuntimeError(f"tendon target #{{index}} not found: {{target_name!r}}")
    if target.Forge_Model_Type != "JOINT":
        raise RuntimeError(f"tendon target #{{index}} is not a JOINT: {{target.name}}")
    resolved.append((target, float(spec.get("coef", 0.5))))

path = obj.Forge_Tendon.targets
path.items.clear()
for target, coef in resolved:
    item = path.items.add()
    item.target = target
    item.coef = coef
path.active_index = max(0, len(path.items) - 1)
result = {{
    "name": obj.name,
    "targets": [{{"target": item.target.name, "coef": item.coef}} for item in path.items],
}}
""".format(name=name, targets=targets)
    return call_blender(code)


@mcp.tool(annotations=WRITE, name="forge_rename")
def rename(name_map: dict[str, str]) -> dict:
    """Rename objects: `{{old_name: new_name, ...}}`. Renames the object only (children / references are updated by
    Blender); refuses when the target name is already taken by another object (avoids silent `.001` suffixing —
    delete or rename the holder first).
    """
    code = """
import bpy

renamed = {{}}
skipped = {{}}
for old, new in {map!r}.items():
    if old not in bpy.data.objects:
        skipped[old] = "not found"
        continue
    holder = bpy.data.objects.get(new)
    if holder is not None and holder.name != old:
        skipped[old] = f"name {{new!r}} taken by {{holder.name!r}}"
        continue
    obj = bpy.data.objects[old]
    obj.name = new
    renamed[old] = obj.name
result = {{"renamed": renamed, "skipped": skipped}}
""".format(map=name_map)
    return call_blender(code)


@mcp.tool(annotations=DESTRUCTIVE, name="forge_delete")
def delete(names: list[str]) -> dict:
    """Recursively delete the named objects and all descendants. The meshes and materials of the deleted objects
    are purged once they become unused; unrelated orphaned datablocks are left untouched.
    """
    code = """
import bpy

missing = []
roots = []
for n in {names!r}:
    obj = bpy.data.objects.get(n)
    if obj is None:
        missing.append(n)
        continue
    roots.append(obj)

# Build a root-first list, then remove in reverse so every child is unlinked
# before its parent. A set avoids double-removal when both a parent and one of
# its descendants were explicitly named.
to_delete = []
seen = set()
stack = list(reversed(roots))
while stack:
    obj = stack.pop()
    if obj in seen:
        continue
    seen.add(obj)
    to_delete.append(obj)
    stack.extend(reversed(list(obj.children)))

candidate_meshes = {{obj.data for obj in to_delete if isinstance(getattr(obj, "data", None), bpy.types.Mesh)}}
candidate_materials = {{
    slot.material
    for obj in to_delete
    for slot in obj.material_slots
    if slot.material is not None
}}
deleted = [obj.name for obj in reversed(to_delete)]
for obj in reversed(to_delete):
    bpy.data.objects.remove(obj, do_unlink=True)
purged = {{"meshes": [], "materials": []}}
for mesh in candidate_meshes:
    if mesh.users == 0:
        purged["meshes"].append(mesh.name)
        bpy.data.meshes.remove(mesh)
for material in candidate_materials:
    if material.users == 0:
        purged["materials"].append(material.name)
        bpy.data.materials.remove(material)
result = {{"deleted": deleted, "missing": missing, "purged": purged, "remaining": len(bpy.context.scene.objects)}}
""".format(names=names)
    return call_blender(code)


@mcp.tool(annotations=DESTRUCTIVE, name="forge_execute")
def execute(code: str) -> dict:
    """Run Python inside Blender and return a JSON-serializable ``result`` dict.

    ``bpy`` and ``mathutils`` are injected into the execution namespace. The
    script must assign a dictionary to ``result``; use dedicated Forge tools
    whenever they express the requested operation.
    """
    # ``forge_execute`` is an escape hatch for both Forge and ordinary Blender
    # modelling. ``call_blender`` applies the same guide check here as it does
    # for the dedicated tools — Forge operators and Forge property writes ask
    # for the guide, ordinary mesh/object edits pass through.
    return call_blender(code)
