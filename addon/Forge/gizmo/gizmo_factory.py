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
Gizmo group factory — eliminates the 15 nearly-identical GizmoGroup subclasses.
"""

from __future__ import annotations

from collections.abc import Callable

import bpy
from bpy.types import Context, Gizmo, GizmoGroup
from mathutils import Matrix


def normalized_object_matrix(obj) -> Matrix:
    """Return an unscaled world matrix without producing NaNs for zero scale."""
    matrix = obj.matrix_world
    if abs(matrix.to_3x3().determinant()) > 1e-12:
        return matrix.normalized()
    rotation = matrix.to_quaternion()
    if rotation.magnitude < 1e-12:
        rotation.identity()
    else:
        rotation.normalize()
    result = rotation.to_matrix().to_4x4()
    result.translation = matrix.translation
    return result


def make_gizmo_group(
    *,
    name: str,
    widget_cls: type[Gizmo],
    operator_id: str,
    poll_fn: Callable[[bpy.types.Context], bool],
    color: tuple[float, float, float] = (1.0, 0.8, 0.2),
    alpha: float = 0.8,
    color_highlight: tuple[float, float, float] = (0.0, 0.8, 0.25),
    alpha_highlight: float = 1.0,
    scale_basis: float = 0.2,
    offset_fn: Callable | None = None,
    matrix_fn: Callable | None = None,
) -> type[GizmoGroup]:
    """Create a GizmoGroup class with the given parameters.

    Args:
        name: Short label used to derive ``bl_idname`` and ``bl_label``.
        widget_cls: One of ``PropertiesShapeWidget`` / ``PropertiesBoxWidget`` /
                    ``PropertiesLinkWidget`` from ``gizmo.py``.
        operator_id: The bl_idname of the operator to invoke on click.
        poll_fn: Callable[[Context], bool] — classmethod for poll.
        color / alpha / color_highlight / alpha_highlight: Gizmo colours.
        scale_basis: Gizmo size.
        offset_fn: ``Callable[[Object], list[float]]`` — Used in the default
                   *refresh* implementation (gizmo follows object at offset).
        matrix_fn: Alternative to *offset_fn* — ``Callable[[Object, Context], Matrix]``
                   providing a fully custom matrix for refresh.
                   If both are None, refresh is a no-op.
    """

    def _poll(cls, context: Context):
        """Test whether the gizmo group should be visible in the current context.

        Args:
            context: The active Blender context.

        Returns:
            True if the gizmo group should be drawn, False otherwise.
        """
        return poll_fn(context)

    def _setup(self, context: Context):
        """Create the gizmo widget, assign colours, and bind the target operator.

        Args:
            context: The active Blender context.
        """
        gz = self.gizmos.new(widget_cls.bl_idname)
        gz.target_set_operator(operator_id)
        gz.color = color
        gz.alpha = alpha
        gz.color_highlight = color_highlight
        gz.alpha_highlight = alpha_highlight
        gz.scale_basis = scale_basis
        gz.use_draw_modal = True
        self.gizmo = gz

    def _refresh(self, context: Context):
        """Update the gizmo matrix basis to follow the active selected object.

        Uses *matrix_fn* if provided, otherwise *offset_fn* to compute the
        gizmo position relative to the object. Falls back to a no-op when
        nothing is selected or when both functions are None.

        Args:
            context: The active Blender context.
        """
        if not context.selected_objects:
            return
        obj = context.active_object
        if not obj:
            return
        gz = self.gizmo
        if matrix_fn:
            gz.matrix_basis = matrix_fn(obj, context)
        elif offset_fn:
            offset = offset_fn(obj)
            if offset is None:
                return
            gz.matrix_basis = normalized_object_matrix(obj) @ Matrix.Translation(offset)

    bl_idname = f"OBJECT_GGT_PROPERTIES_{name.upper()}"
    bl_label = f"Properties {name} Widget"

    cls = type(
        f"Properties{name}WidgetGroup",
        (GizmoGroup,),
        {
            "bl_idname": bl_idname,
            "bl_label": bl_label,
            "bl_space_type": "VIEW_3D",
            "bl_region_type": "WINDOW",
            "bl_options": {"3D", "PERSISTENT"},
            "gizmo": None,
            "poll": classmethod(_poll),
            "setup": _setup,
            "refresh": _refresh,
        },
    )
    return cls


# ── Convenience poll builders ───────────────────────────────────────


def mesh_model_poll(*model_types: str):
    """Build a poll function that accepts MESH objects in OBJECT mode with one of the given model types.

    Args:
        *model_types: One or more model type strings (e.g. "VISUAL", "COLLIDER", "JOINT").

    Returns:
        A callable ``(context) -> bool`` suitable as a GizmoGroup poll.
    """

    def _poll(ctx):
        """Poll for MESH objects in OBJECT mode with one of the given model types.

        Args:
            ctx: The active Blender context.

        Returns:
            True if requirements are met, False otherwise.
        """
        if not ctx.selected_objects:
            return False
        obj = ctx.active_object
        if not obj or obj.type != "MESH" or obj.mode != "OBJECT":
            return False
        return obj.Forge_Model_Type in model_types

    return _poll


def empty_model_poll(model_type: str):
    """Build a poll function that accepts EMPTY objects with a specific model type.

    Args:
        model_type: A single model type string (e.g. "LINK").

    Returns:
        A callable ``(context) -> bool`` suitable as a GizmoGroup poll.
    """

    def _poll(ctx):
        """Poll for EMPTY objects with a specific model type.

        Args:
            ctx: The active Blender context.

        Returns:
            True if requirements are met, False otherwise.
        """
        if not ctx.selected_objects:
            return False
        obj = ctx.active_object
        if not obj or obj.type != "EMPTY":
            return False
        return obj.Forge_Model_Type == model_type

    return _poll


def bl_data_model_poll(bl_type: str, model_type: str):
    """Poll for Blender data types (LIGHT, CAMERA)."""

    def _poll(ctx):
        """Poll for Blender data type objects (e.g. LIGHT, CAMERA) with a specific model type.

        Args:
            ctx: The active Blender context.

        Returns:
            True if requirements are met, False otherwise.
        """
        if not ctx.selected_objects:
            return False
        obj = ctx.active_object
        if not obj or obj.type != bl_type:
            return False
        return obj.Forge_Model_Type == model_type

    return _poll
