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

"""Physical inertial frames and their independent viewport preview."""

import math

import bpy
from bpy.app.handlers import persistent
from mathutils import Matrix, Quaternion, Vector

from ..settings import get_addon_prefs
from . import constants as cons

_draw_handle = None
_draw_resources = None
_CORNERS = tuple((x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1))
_EDGES = tuple(
    (a, b) for a in range(8) for b in range(a + 1, 8) if sum(x != y for x, y in zip(_CORNERS[a], _CORNERS[b])) == 1
)
_FACES = ((0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3))
_TRIANGLES = tuple(triangle for a, b, c, d in _FACES for triangle in ((a, b, c), (a, c, d)))


def local_frame(obj) -> Matrix:
    """Read the current parent-relative frame, including pending RNA edits."""
    if getattr(obj, "get", lambda *_: False)("_forge_inertial_box", False):
        if obj.rotation_mode == "QUATERNION":
            rotation = obj.rotation_quaternion
        elif obj.rotation_mode == "AXIS_ANGLE":
            rotation = Quaternion(obj.rotation_axis_angle[1:], obj.rotation_axis_angle[0])
        else:
            rotation = obj.rotation_euler.to_quaternion()
        return Matrix.LocRotScale(obj.location, rotation, (1, 1, 1))
    return obj.matrix_parent_inverse @ obj.matrix_basis


def full_tensor(obj) -> Matrix:
    axes = local_frame(obj).to_quaternion().to_matrix()
    return axes @ Matrix.Diagonal(obj.Forge_Inertial.diaginertia) @ axes.transposed()


def preview_matrix(obj) -> Matrix | None:
    """Return the equivalent box in world space without scaling the object."""
    data = obj.Forge_Inertial
    moments = tuple(data.diaginertia)
    if not math.isfinite(data.mass) or data.mass <= 0 or not all(math.isfinite(v) and v > 0 for v in moments):
        return None
    squared = [3 * (moments[(i + 1) % 3] + moments[(i + 2) % 3] - moments[i]) / (2 * data.mass) for i in range(3)]
    if any(v < 0 for v in squared):
        return None
    frame = local_frame(obj)
    rotation = frame.to_quaternion()
    location = frame.translation
    if obj.parent:
        rotation = obj.parent.matrix_world.to_quaternion() @ rotation
        location = obj.parent.matrix_world @ location
    return Matrix.LocRotScale(location, rotation, Vector(tuple(math.sqrt(v) for v in squared)))


def update_empty_display(obj):
    """Size the selectable native Empty to the equivalent inertia box."""
    frame = local_frame(obj)
    matrix = preview_matrix(obj)
    size = matrix.to_scale() if matrix is not None else Vector((0, 0, 0))
    if not obj.get("_forge_inertial_box", False):
        obj.matrix_basis = frame
        obj["_forge_inertial_box"] = True
    if obj.empty_display_type != "CUBE":
        obj.empty_display_type = "CUBE"
    if obj.empty_display_size != 1.0:
        obj.empty_display_size = 1.0
    # RNA location/rotation remain the physical link-local pose. Compensate
    # parent stretch in the display transform so its box matches the preview.
    inverse = Matrix.Identity(4)
    if obj.parent:
        parent = obj.parent.matrix_world
        rigid = Matrix.LocRotScale(parent @ frame.translation, parent.to_quaternion(), (1, 1, 1))
        inverse = parent.inverted_safe() @ rigid @ Matrix.Translation(-frame.translation)
    # Assign scale alone: decomposing a zero-size basis would erase rotation.
    if obj.scale != size:
        obj.scale = size
    if obj.matrix_parent_inverse != inverse:
        obj.matrix_parent_inverse = inverse


@persistent
def _sync_empty_displays(scene, depsgraph):
    if depsgraph is None:
        objects = scene.objects
    else:
        objects = set()
        for update in depsgraph.updates:
            obj = update.id.original
            if not isinstance(obj, bpy.types.Object) or not (update.is_updated_transform or update.is_updated_geometry):
                continue
            objects.add(obj)
            # The display compensation depends on the parent link's transform.
            objects.update(child for child in obj.children if child.Forge_Model_Type == cons.ModelTypes.INERTIAL)
    for obj in objects:
        if obj.type == "EMPTY" and obj.Forge_Model_Type == cons.ModelTypes.INERTIAL:
            update_empty_display(obj)


@persistent
def _clear_draw_resources(*_args):
    global _draw_resources
    _draw_resources = None


def _get_draw_resources():
    global _draw_resources
    if _draw_resources is None:
        import gpu
        from gpu_extras.batch import batch_for_shader

        shader = gpu.shader.from_builtin("UNIFORM_COLOR")
        vertices = {"pos": _CORNERS}
        faces = batch_for_shader(shader, "TRIS", vertices, indices=_TRIANGLES)
        edges = batch_for_shader(shader, "LINES", vertices, indices=_EDGES)
        _draw_resources = shader, faces, edges
    return _draw_resources


def _draw_previews():
    prefs = get_addon_prefs()
    if prefs is not None and not prefs.show_inertial_preview:
        return

    import gpu

    context = bpy.context
    if not context.space_data.overlay.show_overlays or not context.space_data.overlay.show_extras:
        return
    shader, faces, edges = _get_draw_resources()
    depth_test = gpu.state.depth_test_get()
    depth_mask = gpu.state.depth_mask_get()
    blend = gpu.state.blend_get()
    try:
        gpu.state.blend_set("ALPHA")
        gpu.state.depth_test_set("LESS_EQUAL")
        gpu.state.depth_mask_set(False)
        for obj in context.visible_objects:
            if obj.Forge_Model_Type != cons.ModelTypes.INERTIAL:
                continue
            matrix = preview_matrix(obj)
            if matrix is None:
                continue
            color = (1.0, 0.6, 0.1, 0.4) if obj.select_get() else (0.8, 0.2, 0.1, 0.4)
            shader.bind()
            with gpu.matrix.push_pop():
                gpu.matrix.multiply_matrix(matrix)
                shader.uniform_float("color", (*color[:3], 0.05))
                faces.draw(shader)
                shader.uniform_float("color", color)
                edges.draw(shader)
    finally:
        gpu.state.depth_mask_set(depth_mask)
        gpu.state.depth_test_set(depth_test)
        gpu.state.blend_set(blend)


def register_preview():
    global _draw_handle
    if _draw_handle is None:
        _draw_handle = bpy.types.SpaceView3D.draw_handler_add(_draw_previews, (), "WINDOW", "POST_VIEW")
    if _sync_empty_displays not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(_sync_empty_displays)
    if _clear_draw_resources not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(_clear_draw_resources)


def unregister_preview():
    global _draw_handle
    if _draw_handle is not None:
        bpy.types.SpaceView3D.draw_handler_remove(_draw_handle, "WINDOW")
        _draw_handle = None
    if _sync_empty_displays in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(_sync_empty_displays)
    if _clear_draw_resources in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(_clear_draw_resources)
    _clear_draw_resources()
