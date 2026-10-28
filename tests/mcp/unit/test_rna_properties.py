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

"""Execute MCP templates against RNA-only properties with no IDProperty storage."""

import sys
from types import SimpleNamespace

import pytest
from forge_mcp.tools import scene, utilities


class _Properties(dict):
    def __iter__(self):
        return iter(self.values())


def _group(**values):
    definitions = _Properties()
    for name, value in values.items():
        kind = "STRING" if isinstance(value, str) else "FLOAT"
        definitions[name] = SimpleNamespace(identifier=name, type=kind)
    return SimpleNamespace(bl_rna=SimpleNamespace(properties=definitions), **values)


class _Matrix(list):
    def __init__(self):
        super().__init__([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    def to_translation(self):
        return (0, 0, 0)


class _Object:
    def __init__(self, model_type):
        self.name = "test_object"
        self.Forge_Model_Type = model_type
        self.parent = None
        self.children = []
        self.location = self.rotation_euler = (0, 0, 0)
        self.dimensions = (1, 1, 1)
        self.lock_location = self.lock_rotation = self.lock_scale = (False, False, False)
        self.matrix_world = _Matrix()
        self.modifiers = []
        self.data = _group(energy=1.0)

    def get(self, _key, *_args):
        raise AssertionError("RNA properties must not be read through IDProperties")


@pytest.fixture
def bridge(monkeypatch):
    def run(function, obj, *args):
        fake_bpy = SimpleNamespace(
            data=SimpleNamespace(objects={obj.name: obj}, filepath=""),
            types=SimpleNamespace(Object=_Object),
            context=SimpleNamespace(
                scene=SimpleNamespace(name="Scene", objects=[obj]),
                selected_objects=[obj],
                active_object=obj,
            ),
        )
        monkeypatch.setitem(sys.modules, "bpy", fake_bpy)
        monkeypatch.setitem(sys.modules, "mathutils", SimpleNamespace(Vector=tuple))

        def execute(code):
            namespace = {}
            exec(compile(code, "<MCP template>", "exec"), namespace)
            return namespace["result"]

        module = scene if function.__module__ == scene.__name__ else utilities
        monkeypatch.setattr(module, "call_blender", execute)
        return function(*args)

    return run


@pytest.mark.parametrize(
    ("model_type", "group_name", "property_name", "value"),
    [
        ("LINK", "Forge_Link", "gravcomp", 0.25),
        ("VISUAL", "Forge_Geometry", "density", 850.0),
        ("COLLIDER", "Forge_Geometry", "margin", 0.01),
        ("SITE", "Forge_Geometry", "group", 4),
        ("PLANE", "Forge_Geometry", "margin", 0.01),
        ("HFIELD", "Forge_Geometry", "margin", 0.01),
        ("JOINT", "Forge_Joint", "damping", 0.2),
        ("ACTUATOR", "Forge_Actuator", "kp", 20.0),
        ("TENDON", "Forge_Tendon", "stiffness", 10.0),
        ("EQUALITY", "Forge_Equality", "active", False),
        ("CONTACT", "Forge_Contact", "margin", 0.01),
        ("SENSOR", "Forge_Sensor", "noise", 0.01),
        ("LIGHT", "Forge_Light", "mode", "TRACK"),
        ("CAMERA", "Forge_Camera", "mode", "TRACK"),
        ("INERTIAL", "Forge_Inertial", "mass", 2.0),
        ("REPLICATE", "Forge_Replicate", "count", 4),
        ("ATTACH", "Forge_Attach", "prefix", "new_"),
        ("INCLUDE", "Forge_Include", "file", "new.xml"),
    ],
)
def test_set_property_uses_rna_model_type(bridge, model_type, group_name, property_name, value):
    obj = _Object(model_type)
    previous = "old" if isinstance(value, str) else True if isinstance(value, bool) else 0
    group = _group(**{property_name: previous})
    setattr(obj, group_name, group)

    result = bridge(scene.set_property, obj, obj.name, {property_name: value})

    assert result == {"name": obj.name, "type": model_type, "set": {property_name: value}, "skipped": {}}
    assert getattr(group, property_name) == value


@pytest.mark.parametrize("model_type", ["FRAME", "UNDEFINED", None])
def test_data_properties_work_without_a_forge_group(bridge, model_type):
    obj = _Object(model_type)
    if model_type is None:
        del obj.Forge_Model_Type

    result = bridge(scene.set_property, obj, obj.name, {"data:energy": 123.0, "unsupported": 1})

    assert obj.data.energy == 123.0
    assert result["set"] == {"data:energy": 123.0}
    assert "has no property group" in result["skipped"]["unsupported"]


def test_scene_info_reads_rna_type_and_default(bridge):
    obj = _Object("LINK")
    result = bridge(utilities.scene_info, obj)
    assert result["objects_by_model_type"] == {"LINK": 1}
    assert result["objects"][0]["type"] == "LINK"

    del obj.Forge_Model_Type
    assert bridge(utilities.scene_info, obj)["objects_by_model_type"] == {"UNDEFINED": 1}


class _NoIDPropertiesModifier:
    name = "modifier"

    def items(self):
        raise TypeError("this type doesn't support IDProperties")


@pytest.mark.parametrize("storage", ["legacy", "rna", "none"])
def test_object_info_reads_model_group_and_modifier_storage(bridge, storage):
    obj = _Object("VISUAL")
    obj.Forge_Geometry = _group(density=850.0)
    modifier = _NoIDPropertiesModifier()
    value = (1.0, 2.0, 3.0)
    if storage == "legacy":
        modifier.items = lambda: {"Socket_0": value, "unrelated": 99}.items()
    elif storage == "rna":
        inputs = SimpleNamespace(
            bl_rna=SimpleNamespace(
                properties=[SimpleNamespace(identifier="rna_type"), SimpleNamespace(identifier="Socket_0")]
            ),
            Socket_0=SimpleNamespace(value=value),
        )
        modifier.properties = SimpleNamespace(inputs=inputs)
    obj.modifiers = [modifier]

    result = bridge(scene.object_info, obj, obj.name)

    assert result["type"] == "VISUAL"
    assert result["props"] == {"density": 850.0}
    assert result["modifiers"] == {"modifier": {} if storage == "none" else {"Socket_0": list(value)}}
