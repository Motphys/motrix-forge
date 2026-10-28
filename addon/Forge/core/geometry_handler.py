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

"""
Geometry size/offset handler — strategy pattern for BOX/CAPSULE/CYLINDER/SPHERE
operations shared across Visual, Collider, and Site contexts.

Each shape type uses a different set of modifier sockets depending on the
context (Visual → Socket_0/Socket_2, Collider/Site → Socket_3/Socket_4).
This handler consolidates the logic in ONE place instead of repeating the
same match-case in 8+ locations across forge_function.py.
"""

from __future__ import annotations

from pathlib import Path

import bpy
from bpy.types import NodesModifier
from mathutils import Vector

from .common import get_modifier_socket, set_modifier_socket
from .constants import ModifierSockets


class GeometryHandler:
    """Per-shape-type handler for geometry size / gizmo-offset calculations.

    Usage::

        handler = GeometryHandler("BOX", ModifierSockets.Visual)
        size = handler.get_size(modifier)
        offset = handler.get_gizmo_offset(modifier)
        handler.set_size(modifier, size, bpy.context)
    """

    # Shared socket-table for each context.
    CONTEXT_SOCKETS: dict[str, type] = {
        "Visual": ModifierSockets.Visual,
        "Collider": ModifierSockets.Collider,
        "Site": ModifierSockets.Site,
    }

    __slots__ = ("geometry_type", "sockets")

    def __init__(self, geometry_type: str, sockets):
        """Initialize the GeometryHandler.

        Args:
            geometry_type: "BOX", "CAPSULE", "CYLINDER", or "SPHERE".
            sockets: One of ModifierSockets.Visual / Collider / Site.
        """

        self.geometry_type = geometry_type
        self.sockets = sockets

    @classmethod
    def for_visual(cls, geometry_type: str) -> GeometryHandler:
        """Create a handler configured for the Visual context.

        Args:
            geometry_type: "BOX", "CAPSULE", "CYLINDER", or "SPHERE".

        Returns:
            A GeometryHandler instance with sockets set to
            ModifierSockets.Visual.
        """

        return cls(geometry_type, ModifierSockets.Visual)

    @classmethod
    def for_collider(cls, geometry_type: str) -> GeometryHandler:
        """Create a handler configured for the Collider context.

        Args:
            geometry_type: "BOX", "CAPSULE", "CYLINDER", or "SPHERE".

        Returns:
            A GeometryHandler instance with sockets set to
            ModifierSockets.Collider.
        """

        return cls(geometry_type, ModifierSockets.Collider)

    @classmethod
    def for_site(cls, geometry_type: str) -> GeometryHandler:
        """Create a handler configured for the Site context.

        Args:
            geometry_type: "BOX", "CAPSULE", "CYLINDER", or "SPHERE".

        Returns:
            A GeometryHandler instance with sockets set to
            ModifierSockets.Site.
        """

        return cls(geometry_type, ModifierSockets.Site)

    # ── half-extent (get_size) ────────────────────────────────────────

    def get_size(self, modifier: NodesModifier) -> float | Vector:
        """Return the size representation used by the export code.

        * BOX → ``Vector((x*0.5, y*0.5, z*0.5))``
        * CAPSULE/CYLINDER → ``Vector((radius, height*0.5))``
        * SPHERE → ``radius``
        """

        S = self.sockets
        match self.geometry_type:
            case "BOX":
                return Vector([v * 0.5 for v in get_modifier_socket(modifier, S.SIZE)])
            case "CAPSULE" | "CYLINDER":
                return Vector((get_modifier_socket(modifier, S.SIZE), get_modifier_socket(modifier, S.HEIGHT) * 0.5))
            case "SPHERE":
                return get_modifier_socket(modifier, S.SIZE)
        return Vector()

    # ── gizmo offset (get_gizmo_offset) ───────────────────────────────

    def get_gizmo_offset(self, modifier: NodesModifier) -> list[float]:
        """Return 3-element offset vector for gizmo widget positioning."""
        S = self.sockets
        match self.geometry_type:
            case "BOX":
                return [v * 0.5 for v in get_modifier_socket(modifier, S.SIZE)]
            case "CAPSULE":
                r = get_modifier_socket(modifier, S.SIZE)
                return [r, r, get_modifier_socket(modifier, S.HEIGHT) * 0.5 + r]
            case "CYLINDER":
                r = get_modifier_socket(modifier, S.SIZE)
                return [r, r, get_modifier_socket(modifier, S.HEIGHT) * 0.5]
            case "SPHERE":
                r = get_modifier_socket(modifier, S.SIZE)
                return [r, r, r]
        return [0.0, 0.0, 0.0]

    # ── write-back (set_size) ─────────────────────────────────────────

    def set_size(
        self,
        modifier: NodesModifier,
        size: float | Vector,
        based_on_dimensions: bool = True,
        min_is_height: bool = False,
    ):
        """Write *size* into *modifier* sockets.

        When *based_on_dimensions* is True (default for shape-creation) the
        input is treated as object dimensions and converted to the internal
        representation (radius/half-height etc.).  When False the caller is
        responsible for passing the internal representation directly.
        """

        S = self.sockets
        match self.geometry_type:
            case "BOX":
                if not based_on_dimensions:
                    size *= 2.0
                set_modifier_socket(modifier, S.SIZE, size)

            case "CAPSULE":
                if based_on_dimensions:
                    if min_is_height:
                        d = max(size.x, size.y, size.z)
                        radius = d * 0.5
                        height = min(size.x, size.y, size.z) - d
                    else:
                        d = min(size.x, size.y, size.z)
                        radius = d * 0.5
                        height = max(size.x, size.y, size.z) - d
                else:
                    radius = size.x
                    height = size.y * 2.0
                set_modifier_socket(modifier, S.SIZE, radius)
                set_modifier_socket(modifier, S.HEIGHT, max(0.01, height))

            case "CYLINDER":
                if based_on_dimensions:
                    if min_is_height:
                        radius = max(size.x, size.y, size.z) * 0.5
                        height = min(size.x, size.y, size.z)
                    else:
                        radius = min(size.x, size.y, size.z) * 0.5
                        height = max(size.x, size.y, size.z)
                else:
                    radius = size.x
                    height = size.y * 2.0
                set_modifier_socket(modifier, S.SIZE, radius)
                set_modifier_socket(modifier, S.HEIGHT, max(0.01, height))

            case "SPHERE":
                radius = max(size.x, size.y, size.z) * 0.5 if based_on_dimensions else size
                set_modifier_socket(modifier, S.SIZE, radius)

    # ── dimension vector (for change_xxx) ─────────────────────────────

    def get_dimensions(self, modifier: NodesModifier) -> Vector:
        """Rebuild object-space dimension vector from modifier values.

        Inverse of *set_size* with ``based_on_dimensions=True``.
        """

        S = self.sockets
        match self.geometry_type:
            case "BOX":
                return Vector(get_modifier_socket(modifier, S.SIZE))
            case "CAPSULE":
                d = get_modifier_socket(modifier, S.SIZE) * 2.0
                return Vector((d, d, get_modifier_socket(modifier, S.HEIGHT) + d))
            case "CYLINDER":
                d = get_modifier_socket(modifier, S.SIZE) * 2.0
                return Vector((d, d, get_modifier_socket(modifier, S.HEIGHT)))
            case "SPHERE":
                d = get_modifier_socket(modifier, S.SIZE) * 2.0
                return Vector((d, d, d))
        return Vector()

    # ── utils ─────────────────────────────────────────────────────────

    def modifier_name(self, shape_modifiers: dict[str, str]) -> str | None:
        """Resolve modifier name from a *GeometryShapeModifiers*-like dict."""
        return shape_modifiers.get(self.geometry_type)


# ── Shape modifier asset registry ────────────────────────────────────
# Maps (context, geometry_type) → Blender asset identifier under
# "Shapes.blend/NodeTree/".
SHAPE_ASSET_IDS: dict[tuple[str, str], str] = {
    ("Visual", "BOX"): "Geometry_Box",
    ("Visual", "CAPSULE"): "Geometry_Capsule",
    ("Visual", "CYLINDER"): "Geometry_Cylinder",
    ("Visual", "SPHERE"): "Geometry_Sphere",
    ("Collider", "BOX"): "Collider_Box",
    ("Collider", "CAPSULE"): "Collider_Capsule",
    ("Collider", "CYLINDER"): "Collider_Cylinder",
    ("Collider", "SPHERE"): "Collider_Sphere",
    ("Collider", "MESH"): "Collider_Convex",
    ("Site", "BOX"): "Site_Box",
    ("Site", "CAPSULE"): "Site_Capsule",
    ("Site", "CYLINDER"): "Site_Cylinder",
    ("Site", "SPHERE"): "Site_Sphere",
}


def add_shape_modifier(obj, context_type: str, geometry_type: str):
    """Add a Geometry Nodes modifier from the Forge Library asset.

    Args:
        obj: Target Blender object.
        context_type: ``"Visual"``, ``"Collider"``, or ``"Site"``.
        geometry_type: ``"BOX"``, ``"CAPSULE"``, ``"CYLINDER"``, ``"SPHERE"``,
                       or ``"MESH"`` (Collider only).
    """

    asset_id = SHAPE_ASSET_IDS.get((context_type, geometry_type))
    if asset_id is None:
        return
    try:
        bpy.ops.object.modifier_add_node_group(
            asset_library_type="CUSTOM",
            asset_library_identifier="Forge Library",
            relative_asset_identifier=f"Shapes.blend/NodeTree/{asset_id}",
        )
    except RuntimeError:
        # Background Blender may report an asset-browser failure before the
        # node-group modifier is attached. Fall back to the bundled library so
        # MCP/E2E calls do not continue with a missing shape modifier.
        pass

    # The asset operator can also return FINISHED while no modifier is added
    # (asset loading is still asynchronous in headless mode). Reuse an already
    # loaded group, or link it directly from the bundled Shapes.blend file.
    modifier = next(
        (
            item
            for item in obj.modifiers
            if item.type == "NODES" and item.node_group and item.node_group.name == asset_id
        ),
        None,
    )
    if modifier is None:
        library_path = Path(__file__).resolve().parents[1] / "lib" / "assets" / "Shapes.blend"
        node_group = bpy.data.node_groups.get(asset_id)
        if node_group is None:
            with bpy.data.libraries.load(str(library_path), link=False) as (data_from, data_to):
                if asset_id in data_from.node_groups:
                    data_to.node_groups = [asset_id]
            node_group = bpy.data.node_groups.get(asset_id)
        if node_group is None:
            raise RuntimeError(f"Forge shape asset {asset_id!r} is not available in {library_path}")
        modifier = obj.modifiers.new(asset_id, "NODES")
        modifier.node_group = node_group

    # Downstream code indexes by the asset name; normalize generic names
    # produced by Blender's asset operator before returning.
    if modifier.name != asset_id and asset_id not in obj.modifiers:
        modifier.name = asset_id
