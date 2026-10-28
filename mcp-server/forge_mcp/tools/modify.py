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

"""Modify commands — mirror ``bpy.ops.forge.define_*`` and other modify ops (see forge_mcp/skills/forge_modify.md).

Popup dialogs (``bpy.ops.forge.properties_*``) are UI-only and ineffective for
agents — change parameters via direct property assignment instead
(``obj.Forge_<Type>.<property>``, shape / gizmo sizes via ``obj.modifiers[...]``).
Every tool takes ``select`` (object names): selection is replaced with that list
(order matters — first becomes active) before the operator runs. ``None`` leaves
the current selection untouched.
"""

from __future__ import annotations

from typing import Literal

from .. import call_blender, mcp
from ..blender import op_call
from ._hints import WRITE

# ── Enums ─────────────────────────────────────────────────────────────

ModelType = Literal["LINK", "VISUAL", "COLLIDER", "LIGHT", "CAMERA"]
GeometryType = Literal["BOX", "CAPSULE", "CYLINDER", "SPHERE", "MESH", "SDF"]
ColliderType = GeometryType
SiteType = Literal["BOX", "CAPSULE", "CYLINDER", "SPHERE"]
JointType = Literal["FREE", "BALL", "SLIDE", "HINGE"]
ActuatorType = Literal["GENERAL", "MOTOR", "POSITION", "VELOCITY", "ADHESION"]


# ── Type change ───────────────────────────────────────────────────────


@mcp.tool(annotations=WRITE, name="forge_define_model_type")
def define_model_type(model_type: ModelType, select: list[str] | None = None) -> dict:
    """Set the model type of selected `UNDEFINED` object(s).

    - Available `model_type` decided by the selected Blender object type: EMPTY -> LINK; MESH -> VISUAL or COLLIDER;
      LIGHT -> LIGHT; CAMERA -> CAMERA.
    - VISUAL: set geometry type MESH, group 2, contype / conaffinity 0, rename with prefix `GEO_`.
    - COLLIDER: set geometry type MESH, group 3, rename with prefix `COL_`.
    - LINK: rename with prefix `LNK_`.
    - LIGHT: set light type by Blender light type (SUN -> DIRECTIONAL, else SPOT / POINT), mode FIXED, rename with
      prefix `LIT_`; `AREA` light not supported.
    - CAMERA: set camera type by Blender camera type (ORTHO -> ORTHOGRAPHIC, PERSP -> PERSPECTIVE), mode FIXED,
      rename with prefix `CAM_`; only `PERSP` / `ORTHO` camera supported.
    - Object with parent moves to the corresponding type collection, without parent to `WORLD`.
    """
    return call_blender(op_call("define_model_type", select=select, Model_Type=model_type))


@mcp.tool(annotations=WRITE, name="forge_define_geometry_type")
def define_geometry_type(
    geometry_type: GeometryType, apply_to_all: bool = False, select: list[str] | None = None
) -> dict:
    """Change the geometry type of selected `visual` object(s).

    - `apply_to_all`: default `False` only applies to the active object, `True` applies to all selected.
    - Size preserved as the bounding-box equivalent; exact shape parameters may differ across a round-trip
      through another shape (e.g. CYLINDER r=0.05 -> SPHERE -> CYLINDER yields r=0.1).
    - Switch to `MESH` / `SDF`: bake current geometry into mesh, scale unlock.
    - Switch from `MESH` / `SDF`: use object dimensions as size.
    """
    return call_blender(
        op_call("define_geometry_type", select=select, geometry_type=geometry_type, apply_to_all=apply_to_all)
    )


@mcp.tool(annotations=WRITE, name="forge_define_collider_type")
def define_collider_type(
    collider_type: ColliderType, apply_to_all: bool = False, select: list[str] | None = None
) -> dict:
    """Change the collider type of selected `collider` object(s).

    - `apply_to_all`: default `False` only applies to the active object, `True` applies to all selected.
    - Size preserved as the bounding-box equivalent; exact shape parameters may differ across a round-trip
      through another shape (e.g. CYLINDER r=0.05 -> SPHERE -> CYLINDER yields r=0.1).
    - Switch to `MESH` / `SDF`: bake current primitive or convex modifier into mesh, scale unlock.
    - Switch from `MESH` / `SDF`: use object dimensions as size.
    """
    return call_blender(
        op_call("define_collider_type", select=select, collider_type=collider_type, apply_to_all=apply_to_all)
    )


@mcp.tool(annotations=WRITE, name="forge_define_site_type")
def define_site_type(site_type: SiteType, apply_to_all: bool = False, select: list[str] | None = None) -> dict:
    """Change the shape type of selected `site` object(s).

    - `apply_to_all`: default `False` only applies to the active object, `True` applies to all selected.
    - Size preserved as the bounding-box equivalent; exact shape parameters may differ across a round-trip
      through another shape.
    """
    return call_blender(op_call("define_site_type", select=select, site_type=site_type, apply_to_all=apply_to_all))


@mcp.tool(annotations=WRITE, name="forge_define_joint_type")
def define_joint_type(joint_type: JointType, apply_to_all: bool = False, select: list[str] | None = None) -> dict:
    """Change the joint type of selected `joint` object(s).

    - `apply_to_all`: default `False` only applies to the active object, `True` applies to all selected.
    - Joint shape gizmo updated when type changed.
    """
    return call_blender(op_call("define_joint_type", select=select, joint_type=joint_type, apply_to_all=apply_to_all))


@mcp.tool(annotations=WRITE, name="forge_define_actuator_type")
def define_actuator_type(
    actuator_type: ActuatorType, apply_to_all: bool = False, select: list[str] | None = None
) -> dict:
    """Change the actuator type of selected `actuator` object(s).

    - `apply_to_all`: default `False` only applies to the active object, `True` applies to all selected.
    """
    return call_blender(
        op_call("define_actuator_type", select=select, actuator_type=actuator_type, apply_to_all=apply_to_all)
    )


# ── Hierarchy / validation ────────────────────────────────────────────


@mcp.tool(annotations=WRITE, name="forge_define_parent")
def define_parent(select: list[str] | None = None) -> dict:
    """Change parent of selected object(s) to the active object (first in `select`).

    - Active object is `link` | `frame` | `replicate`: parent selected `[LINK, VISUAL, COLLIDER, JOINT, SITE, LIGHT,
      CAMERA, FRAME, REPLICATE, ATTACH]` objects to it.
    - Active object is `visual`: refused — a `collider` under a `visual` is not exported; parent the `collider` to
      the `link` instead.
    - Children of a selected `visual` object (for example colliders still bound to it) are reparented to the active
      object first, so a legacy `collider`-under-`visual` nesting is repaired rather than recreated.
    - World position of child preserved after reparent.
    - Each reparented object moves into the collection of its model type (`visual` → `Visual`, `collider` →
      `Collider`, …), so an object created at the world root leaves the `World` collection.
    """
    return call_blender(op_call("define_parent", select=select))


@mcp.tool(annotations=WRITE, name="forge_mark_root_link")
def mark_root_link(select: list[str] | None = None) -> dict:
    """Mark selected `link` | `frame` object(s) without parent as root link.

    - Child link can not be marked as root.
    - Sets `obj["Root Link"] = True`.
    """
    return call_blender(op_call("mark_root_link", select=select))


@mcp.tool(annotations=WRITE, name="forge_mark_instance_link")
def mark_instance_link(select: list[str] | None = None) -> dict:
    """Toggle the instance-link mark on selected `link` object(s).

    - Sets / removes `obj["INSTANCE_LINK"] = True`.
    - A marked instance link never exports as a `<body>`; referenced ones feed the
      `<asset>` section with their subtree's meshes / materials, unreferenced ones
      export nothing at all (warned). Pick it via `Forge_Props.instance_body` (the
      picker only lists marked links), then run `forge_set_instance_idname` on the
      placeholder links.
    """
    return call_blender(op_call("mark_instance_link", select=select))


@mcp.tool(annotations=WRITE, name="forge_mesh_check")
def mesh_check(select: list[str] | None = None) -> dict:
    """Validate the mesh of selected `visual` object(s) and report errors.

    - Use before compute inertial / export.
    - Checks both self-intersections and pairwise intersections between all selected objects — scope the selection to
      one link's visuals to avoid cross-link contact false positives (e.g. balls touching in a cradle).
    - Boundary-only point-point, point-edge, point-face, edge-edge, and edge-face contact is allowed when incident
      geometry does not cross the other mesh. A coplanar shared face is also valid when its plane separates both
      complete objects, independent of winding. Actual crossings and non-separating coplanar area overlap count as
      intersections.
    """
    return call_blender(op_call("mesh_check", select=select))


@mcp.tool(annotations=WRITE, name="forge_scale_gizmo_size")
def scale_gizmo_size(select: list[str] | None = None) -> dict:
    """Scale gizmo display size of selected object(s), or all objects when none selected.

    - Scale from scene `Forge_Props.gizmo_scale`.
    """
    return call_blender(op_call("scale_gizmo_size", select=select))
