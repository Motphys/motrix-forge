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

"""Regression tests for non-destructive CoACD decomposition."""

from types import SimpleNamespace

import bpy
import numpy as np
from Forge.ops import coacd as coacd_ops


class _FakeCoacd:
    class Mesh:
        def __init__(self, vertices, faces):
            self.vertices = vertices
            self.faces = faces

    @staticmethod
    def run_coacd(mesh, *_args):
        return [(mesh.vertices, mesh.faces)]


def test_coacd_preserves_source_mesh_and_world_transform(registered_props, monkeypatch):
    monkeypatch.setattr(coacd_ops, "coacd", _FakeCoacd)
    monkeypatch.setattr(
        coacd_ops,
        "get_addon_prefs",
        lambda: SimpleNamespace(coacd_name_template="?_hull_#"),
    )
    bpy.utils.register_class(coacd_ops.Forge_OT_COACD)
    try:
        bpy.ops.mesh.primitive_cube_add(location=(2.0, 3.0, 4.0), rotation=(0.2, 0.3, 0.4), scale=(1.0, 2.0, 3.0))
        source = bpy.context.active_object
        source.name = "source#part"
        source.Forge_Model_Type = "VISUAL"
        parent = bpy.data.objects.new("link", None)
        bpy.context.collection.objects.link(parent)
        source.parent = parent
        original_polygons = len(source.data.polygons)
        original_matrix = source.matrix_world.copy()

        assert bpy.ops.forge.coacds() == {"FINISHED"}

        hull = bpy.data.objects["source#part_hull_001"]
        assert len(source.data.polygons) == original_polygons
        assert len(source.modifiers) == 0
        # Hulls follow whatever the source follows and keep their world placement.
        assert hull.parent == parent
        assert np.allclose(np.asarray(hull.matrix_world), np.asarray(original_matrix))
        assert hull.Forge_Model_Type == "COLLIDER"
        assert hull.Forge_Geometry.type == "MESH"
    finally:
        bpy.utils.unregister_class(coacd_ops.Forge_OT_COACD)
