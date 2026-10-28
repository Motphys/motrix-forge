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
Serialization utilities for Forge — formatting Blender property values
to/from MJCF XML attribute strings.

Consolidated from function.py / export.py / import.py.
"""

from __future__ import annotations

import math
import os
from typing import Any

from bpy.types import Object, bpy_prop_array
from mathutils import Color, Euler, Quaternion, Vector

# ── Boolean helpers ─────────────────────────────────────────────────


def get_active(value: str) -> bool:
    """Parse an MJCF boolean attribute string into a boolean.

    Accepts both spellings an MJCF file may use: ``"true"/"false"`` and the
    ``"1"/"0"`` form the ``<headlight active>``.

    Args:
        value: MJCF attribute value as a string.

    Returns:
        ``True`` if value is ``"true"`` or ``"1"``, ``False`` otherwise.
    """

    return value in ["true", "1"]


def get_bool_str(condition: bool) -> str:
    """Convert a Python boolean to the MJCF string ``"true"/"false"``.

    Args:
        condition: Boolean value to convert.

    Returns:
        ``"true"`` if condition is truthy, ``"false"`` otherwise.
    """

    return "true" if condition else "false"


# ── Numeric rounding ────────────────────────────────────────────────

# Values below this magnitude are float32 conversion noise (euler/matrix math
# leaves ~1e-07 residue around zero), not meaningful model data.
ZERO_TOLERANCE = 1e-6


def round_float(value: float, precision: int = 7, zero_tolerance: float = 0.0) -> float:
    """Round a float to the given number of decimal places.

    Used internally to control the precision of numeric values
    written to MJCF XML output.  Callers that are formatting values derived
    from matrix/euler math may pass ``zero_tolerance`` to remove numerical
    residue; ordinary physical parameters retain their small non-zero values.

    Args:
        value: The float to round.
        precision: Number of decimal places (default 7).
        zero_tolerance: Optional magnitude below which the rounded value is
            snapped to zero. Defaults to no snapping.

    Returns:
        The rounded float.
    """

    rounded = round(value, precision)
    if zero_tolerance and -zero_tolerance < rounded < zero_tolerance:
        return 0.0
    return rounded


# ── Vector / array formatting ───────────────────────────────────────


def parse_vector_array_to_xml(
    vector, scale: float = 1.0, usescale: bool = False, zero_tolerance: float = 0.0, precision: int = 7
) -> str:
    """Format a vector or sequence into a space-separated string for MJCF.

    Args:
        vector: Iterable of numeric values (list, tuple, Vector, Color, Euler, Quaternion, etc.).
        scale: Multiplier applied to every element when ``usescale`` is ``True``.
        usescale: When ``True``, each element is multiplied by *scale* before formatting.
        zero_tolerance: Optional magnitude below which each rounded element is
            snapped to zero; forwarded to :func:`round_float`. Defaults to no
            snapping, so ordinary physical parameters keep small non-zero values.
        precision: Number of decimal places (default 7).

    Returns:
        Space-separated string of rounded float values.
    """

    fmt = " ".join
    if usescale:
        return fmt([f"{round_float(v * scale, precision, zero_tolerance=zero_tolerance)}" for v in vector])
    return fmt([f"{round_float(v, precision, zero_tolerance=zero_tolerance)}" for v in vector])


def parse_list_array_to_xml(items) -> str:
    """Format a Blender ``CollectionProperty`` into a space-separated string.

    Each item in the collection is expected to have a ``.value`` attribute.

    Args:
        items: Iterable of objects with a ``value`` attribute (e.g. a
            Blender CollectionProperty of float properties).

    Returns:
        Space-separated string of rounded float values.
    """

    return " ".join(f"{round_float(v.value)}" for v in items)


def parse_rotation_euler_to_xml(euler) -> str:
    """Format an Euler rotation into a space-separated degrees string for MJCF.

    Args:
        euler: An Euler, Quaternion, Vector, or any iterable of three
            angles in radians.

    Returns:
        Space-separated string of the three angles converted to degrees
        and rounded.
    """

    return " ".join(f"{math.degrees(round_float(v))}" for v in euler)


# ── Generic attribute formatting (M → MJCF) ─────────────────────────


def parse_value_by_attr(attr, precision: int = 7) -> str:
    """Convert any Blender property value to its MJCF string representation.

    Handles bool, int, float, str, list, tuple, Object (by name),
    ``bpy_prop_array``, Vector, Color, Euler, and Quaternion types.
    Unrecognised types return an empty string.

    Args:
        attr: The Blender property value to convert.
        precision: Number of decimal places for floats and array elements (default 7).

    Returns:
        MJCF-compatible string representation of the value.
    """

    if isinstance(attr, bool):
        return get_bool_str(attr)
    if isinstance(attr, (int, float)):
        return f"{round_float(attr, precision)}" if isinstance(attr, float) else f"{attr}"
    if isinstance(attr, str):
        return attr.lower()
    if isinstance(attr, (list, tuple)):
        return parse_vector_array_to_xml(attr, precision=precision)

    # Blender-specific types
    if isinstance(attr, Object):
        return attr.name
    if isinstance(attr, bpy_prop_array):
        return parse_vector_array_to_xml(attr, precision=precision)
    if isinstance(attr, (Vector, Color, Euler, Quaternion)):
        return parse_vector_array_to_xml(attr, precision=precision)
    return ""


def parse_prop_by_type(item, prop: str) -> str:
    """Read property *prop* from *item* and format it for MJCF output.

    Args:
        item: Blender data-block or any object with the attribute *prop*.
        prop: Name of the property to read.

    Returns:
        MJCF-compatible string representation of the property value.
    """

    value = getattr(item, prop)
    rna = getattr(item, "bl_rna", None)
    rna_prop = rna.properties.get(prop) if rna is not None else None
    if rna_prop is not None and rna_prop.type == "STRING":
        return value
    return parse_value_by_attr(value)


# ── Default-value comparison (export) ────────────────────────────────


def is_property_default(id_data, prop_name: str, value) -> bool:
    """Check if *prop_name* on *id_data* is still at its default value.

    Used by the MJCF export to skip attributes that don't need to be written.

    Args:
        id_data: Blender data-block (e.g. an Object or Material) whose RNA
            properties are inspected.
        prop_name: Name of the property to check.
        value: Current value of the property to compare against the default.

    Returns:
        ``True`` if the property value matches its registered default,
        ``False`` otherwise (also returns ``False`` if the property has no
        registered default).
    """

    prop = id_data.bl_rna.properties.get(prop_name)
    if not prop or not hasattr(prop, "default"):
        return False
    if hasattr(prop, "default_array"):
        if tuple(prop.default_array) == ():
            return value == prop.default
        return tuple(value) == tuple(prop.default_array)
    return value == prop.default


# ── XML attribute parsing (MJCF → M) ────────────────────────────────


def parse_attr_from_xml(item, prop: str, tag_attrs: dict) -> Any:
    """Parse an MJCF XML attribute string back into a Blender property value.

    The target property type is inferred from the existing value of
    *prop* on *item*.

    Args:
        item: Blender data-block or object that owns the property.
        prop: Name of the property to set.
        tag_attrs: Dictionary of MJCF XML attribute name-value pairs.

    Returns:
        The parsed value in the appropriate Python type (bool, float,
        int, str, list of floats, or an object name string).
    """

    attr = getattr(item, prop)
    if isinstance(attr, bool):
        return tag_attrs[prop] in ("true", "enable")
    if isinstance(attr, (float, int)):
        return type(attr)(tag_attrs[prop])
    if isinstance(attr, str):
        rna = getattr(item, "bl_rna", None)
        rna_prop = rna.properties.get(prop) if rna is not None else None
        if rna_prop is not None and rna_prop.type == "STRING":
            return tag_attrs[prop]
        return tag_attrs[prop].upper()
    if isinstance(attr, Object):
        return tag_attrs[prop]
    if isinstance(attr, (bpy_prop_array, Vector, Color, Euler, Quaternion)):
        return parse_float_list(tag_attrs[prop])
    return ""


def set_props_from_xml(data, prop: str, tag_attrs: dict) -> None:
    """Set property *prop* on *data* by parsing the value from *tag_attrs*.

    Handles array properties by writing element-by-element, and scalar
    properties via ``setattr``.

    Args:
        data: Blender data-block or object whose property will be set.
        prop: Name of the property to set.
        tag_attrs: Dictionary of MJCF XML attribute name-value pairs
            (must contain *prop* as a key).
    """

    value = parse_attr_from_xml(data, prop, tag_attrs)
    if isinstance(value, list):
        attr = getattr(data, prop)
        rna = getattr(data, "bl_rna", None)
        rna_prop = rna.properties.get(prop) if rna is not None else None
        defaults = tuple(rna_prop.default_array) if rna_prop is not None and hasattr(rna_prop, "default_array") else ()
        for i in range(len(attr)):
            attr[i] = value[i] if i < len(value) else defaults[i] if i < len(defaults) else 0.0
    else:
        setattr(data, prop, value)


# ── Float-list parsing (shared) ─────────────────────────────────────


def parse_float_list(text: str) -> list[float]:
    """Split a space-separated float string into a list of floats.

    Args:
        text: Space-separated float values (e.g. ``"1.0 2.0 3.0"``).

    Returns:
        List of parsed float values.
    """

    return [float(v) for v in text.strip().split()]


# ── Object naming helpers ───────────────────────────────────────────


def fix_object_name(obj: Object) -> None:
    """Replace dots in a Blender object name (and its data name) with underscores.

    Dots in names can cause issues in MJCF XML parsing, so they are
    replaced by underscores in-place.

    Args:
        obj: The Blender Object whose name (and optionally data-block name)
            will be sanitised.
    """

    obj.name = obj.name.replace(".", "_")
    if obj.data:
        obj.data.name = obj.data.name.replace(".", "_")


def fix_image_name(image_name: str) -> str:
    """Ensure an image filename has a standard ``.png`` extension.

    If the filename already contains a recognised image extension
    (``.png``, ``.jpg``, ``.tga``), it is replaced with ``.png``.
    Otherwise ``.png`` is appended.

    Args:
        image_name: The original image filename (with or without extension).

    Returns:
        Filename guaranteed to end with ``.png``.
    """

    root, ext = os.path.splitext(image_name)
    if ext.casefold() in {".png", ".jpg", ".jpeg", ".tga"}:
        return root + ".png"
    return image_name + ".png"
