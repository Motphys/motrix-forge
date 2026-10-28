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

"""Focused coverage for the properties-panel formatting helpers."""

import bpy
import pytest
from Forge.ui import propspanel
from mathutils import Matrix


class _LayoutRecorder:
    def __init__(self):
        self.labels = []

    def label(self, *, text):
        self.labels.append(text)


class TestPropsPanelHelpers:
    def test_matrix_data_uses_local_and_world_transforms(self, registered_props):
        obj = bpy.data.objects.new("matrix-test", None)
        bpy.context.scene.collection.objects.link(obj)
        obj.location = (1.0, 2.0, 3.0)
        obj.rotation_euler = (0.1, 0.2, 0.3)
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        bpy.context.view_layer.update()

        assert tuple(propspanel.getMatrixData("local", "translation")) == pytest.approx((1, 2, 3))
        assert tuple(propspanel.getMatrixData("world", "translation")) == pytest.approx((1, 2, 3))
        assert tuple(propspanel.getMatrixData("local", "rotation")) == pytest.approx((0.1, 0.2, 0.3))
        assert tuple(propspanel.getMatrixData("", "dimensions")) == pytest.approx((0, 0, 0))

        bpy.context.view_layer.objects.active = None
        obj.select_set(False)
        assert propspanel.getMatrixData("local", "translation") == Matrix.Identity(4).to_translation()
        assert propspanel.getMatrixData("invalid", "translation") == Matrix.Identity(4).to_translation()

    def test_draw_value_formats_supported_types(self):
        layout = _LayoutRecorder()
        propspanel.draw_value(layout, "text")
        propspanel.draw_value(layout, True)
        propspanel.draw_value(layout, 1.23456)
        propspanel.draw_value(layout, 7)
        propspanel.draw_value(layout, [1, 2.5])
        propspanel.draw_value(layout, {"x", "y"})
        propspanel.draw_value(layout, None)

        assert layout.labels[:4] == ["text", "True", "1.2346", "7"]
        assert layout.labels[4] == "1, 2.5000"
        assert set(layout.labels[5].split(", ")) == {"x", "y"}
        assert layout.labels[6] == "None"

    def test_draw_value_formats_blender_object_and_array(self, registered_props):
        layout = _LayoutRecorder()
        obj = bpy.data.objects.new("displayed", None)
        bpy.context.scene.collection.objects.link(obj)
        propspanel.draw_value(layout, obj)
        propspanel.draw_value(layout, None)
        assert layout.labels == ["displayed", "None"]
