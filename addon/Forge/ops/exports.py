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

import os
import xml.etree.ElementTree as ET
from collections.abc import Callable
from math import degrees, pi
from typing import Any, Literal
from xml.dom import minidom

import bpy
from bpy.types import Context, Image, Object
from mathutils import Vector

from ..core import constants as cons
from ..core import function as funcs
from ..core import props_data as def_props
from ..core.common import get_modifier_socket
from ..core.props import (
    ActuatorItem,
    AttachItem,
    CameraItem,
    CompilerItem,
    ContactItem,
    EqualityItem,
    GeomItem,
    GlobalItem,
    HeadlightItem,
    IncludeItem,
    InertialItem,
    JointItem,
    LightItem,
    LinkItem,
    MapItem,
    OptionItem,
    QualityItem,
    ReplicateItem,
    RgbaItem,
    SensorItem,
    SsgiItem,
    StatisticItem,
    TendonItem,
    TonemappingItem,
)
from ..core.serialization import is_property_default
from ..core.utils import WmReportItems


def export_images(material: dict, update_xml_only: bool):
    """Export material images to the export directory.

    Args:
        material: Dictionary mapping material names to Material objects.
        update_xml_only: If True, skip file export.
    """
    if update_xml_only:
        return

    for key in [
        cons.ShaderPropName.COLORTEX,
        cons.ShaderPropName.NORMALTEX,
        cons.ShaderPropName.ROUGHNESSTEX,
        cons.ShaderPropName.METALLICTEX,
        cons.ShaderPropName.EMISSIONTEX,
    ]:
        _textureFile, img, path = material[key]
        if img:
            img: Image
            img.save(filepath=path, save_copy=True)


def export_hfields(hfield: list, update_xml_only: bool):
    """Export height field data to the export directory.

    Args:
        hfield: List of height field entries (name, data, path).
        update_xml_only: If True, skip file export.
    """
    if update_xml_only:
        return

    (_, obj, path) = hfield
    funcs.export_hfield(obj, path, update_xml_only)


def export_meshs(mesh: list, update_xml_only: bool, export_glb: bool):
    """Export visual meshes to the export directory.

    Args:
        mesh: List of mesh entries (name, obj, path).
        update_xml_only: If True, skip file export.
        export_glb: If True, export as GLB instead of OBJ.
    """
    if update_xml_only:
        return

    (_, obj, path) = mesh
    funcs.export_assets(obj, path, update_xml_only, export_glb)


def export_collider(mesh: list, update_xml_only: bool):
    """Export collider meshes to STL format.

    Args:
        mesh: List of collider entries (name, obj, path).
        update_xml_only: If True, skip file export.
    """
    if update_xml_only:
        return

    (_, obj, path) = mesh
    funcs.export_collider(obj, path, update_xml_only)


def add_sub_element(data: Any, parentElement: ET.Element, tag: str, useAngleList: list[str] | None = None):
    """Write non-default properties of a data object as attributes of an XML sub-element.

    Only creates the sub-element if at least one property is non-default.
    Returns True if the element was written, False otherwise.

    Args:
        data: Data object containing properties.
        parentElement: Parent XML element.
        tag: Tag name for the sub-element.
        useAngleList: List of property names requiring radian-to-degree conversion.

    Returns:
        True if any attributes were written, False otherwise.
    """

    # Collect non-default attributes first
    attrs = {}
    for prop in data.__annotations__.keys():
        attr = getattr(data, prop)
        if not is_property_default(data, prop, attr):
            if useAngleList and prop in useAngleList:
                attr = degrees(attr) if isinstance(attr, float) else attr
            attrs[prop] = funcs.parse_value_by_attr(attr)

    if not attrs:
        return False

    sub_element = ET.SubElement(parentElement, tag)
    for prop, value in attrs.items():
        sub_element.set(prop, value)
    return True


def add_include(context: Context, parentElement: ET.Element, base_dir: str):
    """Adds <include> elements referencing external MJCF files from the INCLUDE collection.

    Args:
        context: Blender context.
        parentElement: Parent XML element.
        base_dir: Base directory for relative path resolution.
    """

    if cons.CollectionNames.INCLUDE in bpy.data.collections:
        for obj in bpy.data.collections[cons.CollectionNames.INCLUDE].objects:
            data: IncludeItem = obj.Forge_Include
            include = ET.SubElement(parentElement, "include")
            include.set("file", os.path.relpath(data.rawfile, base_dir))


def add_compiler(context: Context, parentElement: ET.Element):
    """Writes compiler settings (non-default properties) as attributes on the parent element.

    Args:
        context: Blender context.
        parentElement: Parent XML element (typically <compiler>).
    """

    data: CompilerItem = context.scene.Forge_GlobalConfig.g_compiler

    add_sub_element(data, parentElement, "compiler")


def add_option(context: Context, parentElement: ET.Element):
    """Adds an <option> element with its <flag> sub-element, writing only non-default properties.

    Args:
        context: Blender context.
        parentElement: Parent XML element.
    """

    data: OptionItem = context.scene.Forge_GlobalConfig.g_option

    # Collect non-default option attributes first
    option_attrs = {}
    for prop in def_props.OPTION_PROPS:
        if prop == "flag":
            continue
        attr = getattr(data, prop)
        if not is_property_default(data, prop, attr):
            option_attrs[prop] = funcs.parse_value_by_attr(attr)

    # Collect non-default flag attributes first
    flag_attrs = {}
    for prop in def_props.FLAG_PROPS:
        attr = getattr(data.flag, prop)
        if not is_property_default(data.flag, prop, attr):
            flag_attrs[prop] = "enable" if attr else "disable"

    if not option_attrs and not flag_attrs:
        return

    option = ET.SubElement(parentElement, "option")
    if option_attrs:
        for prop, value in option_attrs.items():
            option.set(prop, value)

    if flag_attrs:
        flag = ET.SubElement(option, "flag")
        for prop, value in flag_attrs.items():
            flag.set(prop, value)


def add_statistic(context: Context, parentElement: ET.Element):
    """Adds a <statistic> sub-element with non-default statistic-related properties.

    Args:
        context: Blender context.
        parentElement: Parent XML element.
    """

    data: StatisticItem = context.scene.Forge_GlobalConfig.g_statistic
    add_sub_element(data, parentElement, "statistic")


def add_visual(context: Context, parentElement: ET.Element):
    """Adds visual-related sub-elements (<global>, <headlight>, <map>, <rgba>).

    Args:
        context: Blender context.
        parentElement: Parent XML element.
    """
    visual = ET.SubElement(parentElement, "visual")

    count = 0
    data: GlobalItem = context.scene.Forge_VisualConfig.v_global
    if add_sub_element(data, visual, "global", ["fovy", "azimuth", "elevation"]):
        count += 1

    data: HeadlightItem = context.scene.Forge_VisualConfig.v_headlight
    if add_sub_element(data, visual, "headlight"):
        visual.find("headlight").set("active", "1" if data.active else "0")
        count += 1

    data: MapItem = context.scene.Forge_VisualConfig.v_map
    if add_sub_element(data, visual, "map"):
        count += 1

    data: RgbaItem = context.scene.Forge_VisualConfig.v_rgba
    if add_sub_element(data, visual, "rgba"):
        count += 1

    data: QualityItem = context.scene.Forge_VisualConfig.v_quality
    if add_sub_element(data, visual, "quality"):
        count += 1

    data: SsgiItem = context.scene.Forge_VisualConfig.v_ssgi
    if add_sub_element(data, visual, "ssgi"):
        count += 1

    data: TonemappingItem = context.scene.Forge_VisualConfig.v_tonemapping
    if add_sub_element(data, visual, "tonemapping"):
        count += 1

    if count == 0:
        parentElement.remove(visual)


def set_texture_tags(
    parentElement: ET.Element,
    export: list[str],
    textureFile: str,
    colorspace: Literal["sRGB", "linear"] | None = "sRGB",
):
    """Adds a <texture> tag under the parent element, tracking exported textures to avoid duplicates.

    Args:
        parentElement: Parent XML element.
        export: List of already-exported texture names for deduplication.
        textureFile: Texture file path.
        colorspace: Texture colorspace, defaults to "sRGB".

    Returns:
        True if a new texture was added, False otherwise.
    """

    if textureFile is None:
        return

    textureName = textureFile.split(".")[0]
    if textureName in export:
        return

    export.append(textureName)
    texture = ET.SubElement(parentElement, "texture")
    texture.set("type", "2d")
    texture.set("colorspace", colorspace)
    texture.set("name", textureName)
    texture.set("file", textureFile)
    return texture


def set_material_tags(
    parentElement: ET.Element,
    key: str,
    mat: dict,
):
    """Adds a <material> tag under the parent element with color, roughness, metallic,
    and other properties, adding <layer> sub-elements based on texture maps.

    Args:
        parentElement: Parent XML element.
        key: Material name.
        mat: Dictionary of material properties (color, textures, etc.).
    """

    material = ET.SubElement(parentElement, "material")

    material.set("name", key)
    # sRGB conversion of a linear/HDR base color can exceed MJCF's RGBA range.
    rgba = [max(0.0, min(1.0, value)) for value in mat[cons.NodeInputName.COLOR]]
    material.set("rgba", funcs.parse_value_by_attr(rgba))
    material.set("reflectance", "0.5")
    material.set("roughness", funcs.parse_value_by_attr(mat[cons.NodeInputName.ROUGHNESS]))
    material.set("metallic", funcs.parse_value_by_attr(mat[cons.NodeInputName.METALLIC]))

    if key[-6:] == "_blend":
        material.set("alpha_mode", "blend")

    if key[-5:] == "_mask":
        material.set("alpha_mode", "mask")

    if key[-9:] == "_multiply":
        material.set("alpha_mode", "multiply")

    if mat[cons.NodeInputName.EMISSIONST] > 0.0 and (
        mat[cons.ShaderPropName.EMISSIONTEX][0]
        or Vector(mat[cons.NodeInputName.EMISSION][:3]).dot(Vector((1.0, 1.0, 1.0))) > 0.0
    ):
        material.set("emission", funcs.parse_value_by_attr(mat[cons.NodeInputName.EMISSION]))
        material.set("emissionintensity", funcs.parse_value_by_attr(mat[cons.NodeInputName.EMISSIONST]))

    if (
        mat[cons.ShaderPropName.COLORTEX][0]
        or mat[cons.ShaderPropName.ALPHATEX][0]
        or mat[cons.ShaderPropName.NORMALTEX][0]
        or mat[cons.ShaderPropName.ROUGHNESSTEX][0]
        or mat[cons.ShaderPropName.METALLICTEX][0]
        or mat[cons.ShaderPropName.EMISSIONTEX][0]
        or mat.get(cons.ShaderPropName.CHECKER)
    ):
        if cons.ShaderPropName.TILING in mat and mat[cons.ShaderPropName.TILING] is not None:
            texuniform = "true" if mat[cons.ShaderPropName.TILING][0] == mat[cons.ShaderPropName.TILING][1] else "false"
            texrepeat = funcs.parse_vector_array_to_xml(mat[cons.ShaderPropName.TILING])
            material.set("texuniform", texuniform)
            material.set("texrepeat", texrepeat)

        checker = mat.get(cons.ShaderPropName.CHECKER)
        if checker:
            # MJCF builtin procedural checker texture — no image file needed.
            textureName = f"{key}_checker"
            texture = ET.SubElement(parentElement, "texture")
            texture.set("type", "2d")
            texture.set("builtin", "checker")
            texture.set("name", textureName)
            texture.set("rgb1", funcs.parse_value_by_attr(list(checker[0])))
            texture.set("rgb2", funcs.parse_value_by_attr(list(checker[1])))
            if cons.ShaderPropName.TILING in mat and mat[cons.ShaderPropName.TILING] is not None:
                texture.set("width", "512")
                texture.set("height", "512")
            layer = ET.SubElement(material, "layer")
            layer.set("texture", textureName)
            layer.set("role", "rgb")
            # MJCF resolves asset references in document order: the texture
            # must precede the material that uses it.
            parentElement.remove(texture)
            parentElement.insert(list(parentElement).index(material), texture)
            return material

        textureFile = mat[cons.ShaderPropName.COLORTEX][0]
        if textureFile is not None:
            layer = ET.SubElement(material, "layer")
            textureName = textureFile.split(".")[0]
            layer.set("texture", textureName)
            role = "rgb"
            if (
                cons.NodeInputName.ALPHA in mat
                and mat[cons.NodeInputName.ALPHA] < 1.0
                or mat[cons.ShaderPropName.COLORTEX][0] == mat[cons.ShaderPropName.ALPHATEX][0]
            ):
                role = "rgba"
            layer.set("role", role)

        textureFile = mat[cons.ShaderPropName.NORMALTEX][0]
        if textureFile is not None:
            layer = ET.SubElement(material, "layer")
            textureName = textureFile.split(".")[0]
            layer.set("texture", textureName)
            layer.set("role", "normal")

        if mat[cons.ShaderPropName.ROUGHNESSTEX][0] or mat[cons.ShaderPropName.METALLICTEX][0]:
            if mat[cons.ShaderPropName.ROUGHNESSTEX][0] == mat[cons.ShaderPropName.METALLICTEX][0]:
                textureFile = mat[cons.ShaderPropName.ROUGHNESSTEX][0]
                if textureFile is not None:
                    layer = ET.SubElement(material, "layer")
                    textureName = textureFile.split(".")[0]
                    layer.set("texture", textureName)
                    layer.set("role", "orm")
            else:
                textureFile = mat[cons.ShaderPropName.ROUGHNESSTEX][0]
                if textureFile is not None:
                    layer = ET.SubElement(material, "layer")
                    textureName = textureFile.split(".")[0]
                    layer.set("texture", textureName)
                    layer.set("role", "roughness")
                textureFile = mat[cons.ShaderPropName.METALLICTEX][0]
                if textureFile is not None:
                    layer = ET.SubElement(material, "layer")
                    textureName = textureFile.split(".")[0]
                    layer.set("texture", textureName)
                    layer.set("role", "metallic")

        textureFile = mat[cons.ShaderPropName.EMISSIONTEX][0]
        if textureFile is not None:
            layer = ET.SubElement(material, "layer")
            textureName = textureFile.split(".")[0]
            layer.set("texture", textureName)
            layer.set("role", "emissive")


def add_asset(
    parentElement: ET.Element,
    geometry_map: dict,
    attach_model_map: dict,
    hfield_map: dict,
    collider_map: dict,
    materials_props_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Adds texture, material, mesh, height-field, and attach-model asset definitions
    under an <asset> element.

    Args:
        parentElement: Parent XML element (typically <asset>).
        geometry_map: Mapping of geometry names to mesh file paths.
        attach_model_map: Mapping of attach model names to file paths.
        hfield_map: Mapping of height-field names to file paths.
        collider_map: Mapping of collider names to mesh file paths.
        materials_props_map: Mapping of material names to property dicts.
        report: Export report callback function.

    Returns:
        True if any assets were added, False otherwise.
    """

    if cons.CollectionNames.WORLD not in bpy.data.collections:
        report({"INFO"}, "Not find World collection")
        return

    if not geometry_map and not attach_model_map and not hfield_map and not collider_map and not materials_props_map:
        report({"INFO"}, "Not find any assets: meshes, textures, materials, model")
        return

    asset = ET.SubElement(parentElement, "asset")

    export_tex = []
    for mat_key, mat in materials_props_map.items():
        if mat_key == cons.ShaderPropName.ENV:
            color_space = "linear"
            textureFile, _img, _path = mat[cons.ShaderPropName.BACKGROUND]
            texture = set_texture_tags(asset, export_tex, textureFile, color_space)
            if texture is not None:
                texture.set("type", "envhdr")
            continue

        for key in [
            cons.ShaderPropName.COLORTEX,
            cons.ShaderPropName.NORMALTEX,
            cons.ShaderPropName.ROUGHNESSTEX,
            cons.ShaderPropName.METALLICTEX,
            cons.ShaderPropName.EMISSIONTEX,
        ]:
            color_space = "sRGB" if key in [cons.ShaderPropName.COLORTEX, cons.ShaderPropName.EMISSIONTEX] else "linear"
            textureFile, _img, _path = mat[key]
            set_texture_tags(asset, export_tex, textureFile, color_space)

    for mat_key, mat in materials_props_map.items():
        if mat_key == cons.ShaderPropName.ENV:
            continue
        if mat:
            set_material_tags(asset, mat_key, mat)

    for key, geom in geometry_map.items():
        file, _, _ = geom
        mesh = ET.SubElement(asset, "mesh")
        mesh.set("name", key)
        mesh.set("file", file)

    for key, geom in collider_map.items():
        # Linked visual and SDF collider objects share the same mesh asset.
        if key in geometry_map:
            continue
        file, _, _ = geom
        mesh = ET.SubElement(asset, "mesh")
        mesh.set("name", key)
        mesh.set("file", file)

    coll = bpy.data.collections[cons.CollectionNames.WORLD]
    objects: list[Object] = []
    for obj in coll.objects:
        if obj.Forge_Model_Type == cons.ModelTypes.HFIELD:
            objects.append(obj)

    for obj in objects:
        if obj.hide_viewport:
            continue
        if obj.name in hfield_map:
            hfield = ET.SubElement(asset, "hfield")
            hfield.set("name", "terrain_" + obj.name)
            file, _, _ = hfield_map[obj.name]

            hfield.set("file", file)
            hfield.set("content_type", "image/vnd.mujoco.hfield")
            modifier_name = cons.AdditionalShapeModifiers[obj.Forge_Model_Type]
            S = cons.ModifierSockets.HField
            Radius_x = get_modifier_socket(obj.modifiers[modifier_name], S.RADIUS_X)
            Radius_y = get_modifier_socket(obj.modifiers[modifier_name], S.RADIUS_Y)
            Elevation_z = get_modifier_socket(obj.modifiers[modifier_name], S.ELEVATION_Z)
            Base_z = get_modifier_socket(obj.modifiers[modifier_name], S.BASE_Z)
            size = Vector((Radius_x, Radius_y, Elevation_z, Base_z))
            hfield.set("size", funcs.parse_value_by_attr(size))

    for key, file in attach_model_map.items():
        model = ET.SubElement(asset, "model")
        model.set("name", key)
        model.set("file", file)


def set_camera_tags(parentElement: ET.Element, obj: Object):
    """Adds a <camera> tag for a camera object, including position, orientation, FOV, and mode.

    Args:
        parentElement: Parent XML element.
        obj: Blender camera object.
    """

    data: CameraItem = obj.Forge_Camera
    element = ET.SubElement(parentElement, "camera")
    element.set("name", obj.name)
    element.set("pos", funcs.parse_prop_by_type(obj.matrix_local, "translation"))
    rotation_quaternion = obj.matrix_local.to_quaternion()
    element.set("quat", funcs.parse_value_by_attr(rotation_quaternion))

    if data.type == cons.CameraTypes.ORTHOGRAPHIC:
        element.set("orthographic", "true")
        element.set("fovy", funcs.parse_prop_by_type(obj.data, "ortho_scale"))
    else:
        angle = degrees(obj.data.angle_y)
        element.set("fovy", funcs.parse_value_by_attr(angle))

    element.set("mode", funcs.parse_prop_by_type(data, "mode"))
    if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
        if data.target:
            element.set("target", funcs.parse_prop_by_type(data, "target"))


def get_candela(w: float, pf: float = 683, isSun: bool = False):
    """Converts light power (watts) to luminous intensity (candela).
    Uses omnidirectional formula for sunlight; otherwise uses 4pi spherical average.

    Args:
        w: Light power in watts.
        pf: Luminous efficacy factor, default 683 lm / W.
        isSun: Whether this is a sun light.

    Returns:
        Luminous intensity in candela.
    """

    if isSun:
        return w * pf * pi

    return w * pf / 12.57


def set_light_tags(parentElement: ET.Element, obj: Object):
    """Adds a <light> tag for a light object, including position, direction, type, color,
    intensity, and shadow settings.

    Args:
        parentElement: Parent XML element.
        obj: Blender light object.
    """

    data: LightItem = obj.Forge_Light
    element = ET.SubElement(parentElement, "light")
    element.set("name", obj.name)
    element.set("pos", funcs.parse_prop_by_type(obj.matrix_local, "translation"))
    dir = obj.matrix_local.to_3x3().transposed()[2] * -1.0
    element.set("dir", funcs.parse_value_by_attr(dir))
    element.set("type", funcs.parse_prop_by_type(data, "type"))
    element.set("diffuse", funcs.parse_prop_by_type(obj.data, "color"))
    candela = get_candela(obj.data.energy, isSun=obj.data.type == "SUN")
    element.set("intensity", funcs.parse_value_by_attr(candela))

    if data.type != cons.LightTypes.DIRECTIONAL:
        element.set("range", funcs.parse_prop_by_type(obj.data, "cutoff_distance"))

    if data.type == cons.LightTypes.SPOT:
        angle = degrees(obj.data.spot_size) * 0.5
        element.set("cutoff", funcs.parse_value_by_attr(angle))
        element.set("innerangle", funcs.parse_value_by_attr(angle * (1.0 - obj.data.spot_blend)))
    if data.type == cons.LightTypes.POINT:
        pass
    if obj.data.use_shadow:
        element.set("castshadow", "true")
    else:
        element.set("castshadow", "false")

    element.set("mode", funcs.parse_prop_by_type(data, "mode"))
    if data.mode in [cons.TargetModes.TARGETBODY, cons.TargetModes.TARGETBODYCOM]:
        if data.target:
            element.set("target", funcs.parse_prop_by_type(data, "target"))


def set_plane_tags(
    parentElement: ET.Element,
    obj: Object,
    geo_materials_map: dict = None,
):
    """Adds a <geom type="plane"> tag for a plane object.

    Args:
        parentElement: Parent XML element.
        obj: Blender plane object.
        geo_materials_map: Optional mapping of geometry names to material names.
    """

    element = ET.SubElement(parentElement, "geom")
    element.set("name", obj.name)
    element.set("pos", funcs.parse_prop_by_type(obj.matrix_local, "translation"))
    rotation_quaternion = obj.matrix_local.to_quaternion()
    element.set("quat", funcs.parse_value_by_attr(rotation_quaternion))

    element.set("type", "plane")
    size = funcs.get_size(obj)
    size[2] = 0.01
    element.set("size", funcs.parse_value_by_attr(size))

    if obj.name in geo_materials_map:
        element.set("material", geo_materials_map[obj.name])

    data: GeomItem = obj.Forge_Geometry
    for prop in def_props.GEOM_PROPS:
        attr = getattr(data, prop)
        if not is_property_default(data, prop, attr):
            element.set(prop, funcs.parse_value_by_attr(attr))


def set_hfield_tags(
    parentElement: ET.Element,
    obj: Object,
    geometry_map: dict,
    geo_materials_map: dict = None,
):
    """Adds a <geom type="hfield"> tag for a height-field object.

    Args:
        parentElement: Parent XML element.
        obj: Blender height-field object.
        geometry_map: Mapping of geometry names to file paths.
        geo_materials_map: Optional mapping of geometry names to material names.
    """

    if obj.name in geometry_map:
        element = ET.SubElement(parentElement, "geom")
        element.set("name", obj.name)
        element.set("pos", funcs.parse_prop_by_type(obj.matrix_local, "translation"))
        element.set("type", "hfield")
        element.set("hfield", "terrain_" + obj.name)
        if geo_materials_map:
            if obj.name in geo_materials_map:
                element.set("material", geo_materials_map[obj.name])

        data: GeomItem = obj.Forge_Geometry
        for prop in def_props.GEOM_PROPS:
            attr = getattr(data, prop)
            if not is_property_default(data, prop, attr):
                element.set(prop, funcs.parse_value_by_attr(attr))


def set_geom_tags(
    parentElement: ET.Element,
    obj: Object,
    geom_map: dict = None,
    geo_materials_map: dict = None,
):
    """Adds a <geom> tag for a general geometry object, supporting both mesh and primitive
    (box, sphere, cylinder, etc.) types.

    Args:
        parentElement: Parent XML element.
        obj: Blender geometry object.
        geom_map: Optional mapping of geometry names to mesh file paths.
        geo_materials_map: Optional mapping of geometry names to material names.
    """

    # Asset collection deliberately omits empty mesh objects.  Keep the XML
    # hierarchy consistent with that map: a skipped mesh must not leave behind
    # a ``<geom mesh="...">`` reference to a file that will never be written.
    data: GeomItem = obj.Forge_Geometry
    if data.type in cons.MeshGeometryTypes:
        if not funcs.has_exportable_mesh(obj):
            return
        if geom_map is not None and (obj.data is None or obj.data.name not in geom_map):
            return

    element = ET.SubElement(parentElement, "geom")
    element.set("name", obj.name)
    location = obj.matrix_local.to_translation()
    rotation_quaternion = obj.matrix_local.to_quaternion()
    if obj.parent and obj.parent.Forge_Model_Type == cons.ModelTypes.VISUAL:
        location = obj.matrix_world.to_translation()
        rotation_quaternion = obj.matrix_world.to_quaternion()
    element.set("pos", funcs.parse_value_by_attr(location))
    element.set("quat", funcs.parse_value_by_attr(rotation_quaternion))

    element.set("type", funcs.parse_prop_by_type(data, "type"))
    if data.type in cons.MeshGeometryTypes:
        element.set("mesh", obj.data.name)
    else:
        size = funcs.get_size(obj)
        element.set("size", funcs.parse_value_by_attr(size))

    if geo_materials_map:
        element.set("material", geo_materials_map[obj.name])
    for prop in def_props.GEOM_PROPS:
        attr = getattr(data, prop)
        if not is_property_default(data, prop, attr):
            element.set(prop, funcs.parse_value_by_attr(attr))


def _is_angle_property(joint_type: str, prop: str) -> bool:
    """Whether a joint property holds an angle rather than a length or a force.

    A ball / hinge `range` is a pair of angles; a hinge `ref` / `springref` is a
    single one. Everything else a joint carries — a slide's `range`, `ref` and
    `springref`, and every `*frcrange` — is linear and must not be converted.

    A ball's `ref` / `springref` never reach here: MJCF's ball joint does not
    carry them, so they are absent from `JOINT_TYPE_PROPS["BALL"]` and are
    neither written nor converted.
    """
    if joint_type in (cons.JointTypes.BALL, cons.JointTypes.HINGE) and prop == "range":
        return True
    return joint_type == cons.JointTypes.HINGE and prop in ("ref", "springref")


def set_joint_tags(
    context: Context,
    parentElement: ET.Element,
    obj: Object,
):
    """Adds a <joint> tag for a joint object, including position, axis, type, and type-specific properties.

    Args:
        context: Blender context for compiler settings (angle unit).
        parentElement: Parent XML element.
        obj: Blender joint object.
    """

    element = ET.SubElement(parentElement, "joint")
    element.set("name", obj.name)
    element.set("pos", funcs.parse_prop_by_type(obj.matrix_local, "translation"))
    axis = obj.matrix_local.to_3x3().transposed()[2].normalized()
    # Euler/matrix conversion can leave tiny residues around zero.  Apply a
    # tolerance only to this derived axis vector; physical MJCF parameters
    # must retain intentionally small non-zero values.
    element.set("axis", funcs.parse_vector_array_to_xml(axis, zero_tolerance=funcs.ZERO_TOLERANCE))

    compiler: CompilerItem = context.scene.Forge_GlobalConfig.g_compiler
    data: JointItem = obj.Forge_Joint
    element.set("type", funcs.parse_prop_by_type(data, "type"))
    for prop in def_props.JOINT_TYPE_PROPS[data.type]:
        attr = getattr(data, prop)
        if is_property_default(data, prop, attr):
            continue
        # Angle-valued properties are stored in radians and follow the
        # compiler's unit on the way out. `range` is a pair; `ref` and
        # `springref` are scalars, and only a hinge's are angles — a slide's are
        # lengths, written unchanged.
        if compiler.angle == "DEGREE" and _is_angle_property(data.type, prop):
            # `range` is a pair (a bpy_prop_array, not a list); `ref` and
            # `springref` are plain scalars.
            attr = [degrees(v) for v in attr] if prop == "range" else degrees(attr)
        element.set(prop, funcs.parse_value_by_attr(attr))


def set_site_tags(
    parentElement: ET.Element,
    obj: Object,
):
    """Adds a <site> tag for a site object, including position, orientation, type, and size.

    Args:
        parentElement: Parent XML element.
        obj: Blender site object.
    """

    element = ET.SubElement(parentElement, "site")
    element.set("name", obj.name)
    element.set("pos", funcs.parse_prop_by_type(obj.matrix_local, "translation"))
    rotation_quaternion = obj.matrix_local.to_quaternion()
    element.set("quat", funcs.parse_value_by_attr(rotation_quaternion))

    data: GeomItem = obj.Forge_Geometry
    element.set("type", funcs.parse_prop_by_type(data, "type"))
    size = funcs.get_size(obj)
    element.set("size", funcs.parse_value_by_attr(size))
    for prop in def_props.SITE_PROPS:
        attr = getattr(data, prop)
        if not is_property_default(data, prop, attr):
            element.set(prop, funcs.parse_value_by_attr(attr))


def set_attach_tags(
    parentElement: ET.Element,
    obj: Object,
):
    """Adds an <attach> tag for an attach object, specifying the referenced model, body, and prefix.

    Args:
        parentElement: Parent XML element.
        obj: Blender attach object.
    """

    element = ET.SubElement(parentElement, "attach")
    data: AttachItem = obj.Forge_Attach
    element.set("model", data.model)
    if data.link != "":
        element.set("body", data.link)
    element.set("prefix", data.prefix)


def set_inertial_tags(
    parentElement: ET.Element,
    obj: Object,
):
    """Adds an <inertial> tag for an inertial object, including position, orientation, and inertial properties.

    Args:
        parentElement: Parent XML element.
        obj: Blender inertial object.
    """

    from ..core.inertial import local_frame

    frame = local_frame(obj)
    element = ET.SubElement(parentElement, "inertial")
    element.set("pos", funcs.parse_prop_by_type(frame, "translation"))
    data: InertialItem = obj.Forge_Inertial
    element.set("mass", funcs.parse_value_by_attr(data.mass))
    if any(data.diaginertia):
        # The editable principal frame remains authoritative when available.
        element.set("quat", funcs.parse_value_by_attr(frame.to_quaternion()))
        element.set("diaginertia", funcs.parse_value_by_attr(data.diaginertia, 10))
    elif any(data.fullinertia):
        # MuJoCo derives the principal frame from this link-frame tensor.
        element.set("fullinertia", funcs.parse_value_by_attr(data.fullinertia, 10))


def write_multibody_children(
    context: Context,
    parentElement: ET.Element,
    parent_obj: Object,
    geometry_map: dict,
    collider_map: dict,
    geo_materials_map: dict,
    instance_templates: dict[str, Object] | None = None,
):
    """Writes the children of a composite body node (inertial, joint, geoms, child bodies, …).

    Template links (the copy source of some instance) are skipped: their
    content is exported only through the instance links referencing them.

    Args:
        context: Blender context.
        parentElement: Parent XML element to write children into.
        parent_obj: Blender object whose children are exported.
        geometry_map: Mapping of geometry names to mesh file paths.
        collider_map: Mapping of collider names to mesh file paths.
        geo_materials_map: Mapping of geometry names to material names.
        instance_templates: Mapping of instance link names to their template
            link objects; ``None`` disables instance resolution (used when
            copying a template subtree, where nested markers are ignored).
    """

    template_names = {template.name for template in instance_templates.values()} if instance_templates else set()

    children = [child for child in parent_obj.children]
    children = sorted(children, key=lambda obj: funcs.order_map.get(obj.Forge_Model_Type, len(funcs.custom_order)))
    for obj in children:
        if obj.Forge_Model_Type == cons.ModelTypes.LINK and (obj.name in template_names or obj.get("INSTANCE_LINK")):
            continue
        match obj.Forge_Model_Type:
            case cons.ModelTypes.INERTIAL:
                set_inertial_tags(parentElement, obj)
            case cons.ModelTypes.JOINT:
                set_joint_tags(context, parentElement, obj)
            case cons.ModelTypes.CAMERA:
                set_camera_tags(parentElement, obj)
            case cons.ModelTypes.LIGHT:
                set_light_tags(parentElement, obj)
            case cons.ModelTypes.VISUAL:
                set_geom_tags(parentElement, obj, geometry_map, geo_materials_map)
            case cons.ModelTypes.COLLIDER:
                set_geom_tags(parentElement, obj, collider_map)
            case cons.ModelTypes.SITE:
                set_site_tags(parentElement, obj)
            case cons.ModelTypes.LINK | cons.ModelTypes.FRAME | cons.ModelTypes.REPLICATE:
                set_multi_body(
                    context, parentElement, obj, geometry_map, collider_map, geo_materials_map, instance_templates
                )
            case cons.ModelTypes.ATTACH:
                set_attach_tags(parentElement, obj)


def append_instance_subtree(
    context: Context,
    parentElement: ET.Element,
    obj: Object,
    template: Object,
    geometry_map: dict,
    collider_map: dict,
    geo_materials_map: dict,
):
    """Writes a copy of the template link's subtree under an instance link's body element.

    The instance link replaces the template body node itself: the template's
    children are copied under the instance body with every element name
    prefixed by the instance link name (``<instance>_<name>``) to keep names
    unique across copies. Camera / light ``target`` references pointing
    inside the subtree are renamed accordingly.

    Args:
        context: Blender context.
        parentElement: XML body element of the instance link.
        obj: The instance link object.
        template: The template link object referenced by ``INSTANCE_IDNAME``.
        geometry_map: Mapping of geometry names to mesh file paths.
        collider_map: Mapping of collider names to mesh file paths.
        geo_materials_map: Mapping of geometry names to material names.
    """

    prefix = f"{obj.name}_"
    name_map: dict[str, str] = {}
    used_names = {node.name for node in bpy.data.objects}
    stack = list(template.children)
    while stack:
        node = stack.pop()
        name = prefix + node.name
        while name in used_names:
            name += "_inst"
        used_names.add(name)
        name_map[node.name] = name
        stack.extend(node.children)

    fragment = ET.Element("instance")
    write_multibody_children(context, fragment, template, geometry_map, collider_map, geo_materials_map, None)

    for element in fragment.iter():
        for attr in ("name", "target"):
            value = element.get(attr)
            if value in name_map:
                element.set(attr, name_map[value])

    parentElement.extend(list(fragment))


def set_multi_body(
    context: Context,
    parentElement: ET.Element,
    obj: Object,
    geometry_map: dict,
    collider_map: dict,
    geo_materials_map: dict,
    instance_templates: dict[str, Object] | None = None,
):
    """Recursively processes composite body nodes (body, frame, replicate) and their
    children (inertial, joint, camera, etc.).

    A link marked as an instance (``INSTANCE_IDNAME``) exports the template
    link's subtree copy instead of its own children.

    Args:
        context: Blender context.
        parentElement: Parent XML element.
        obj: Blender object (link, frame, or replicate type).
        geometry_map: Mapping of geometry names to mesh file paths.
        collider_map: Mapping of collider names to mesh file paths.
        geo_materials_map: Mapping of geometry names to material names.
        instance_templates: Mapping of instance link names to their template
            link objects; ``None`` disables instance resolution.
    """

    if obj.Forge_Model_Type in [cons.ModelTypes.LINK, cons.ModelTypes.FRAME]:
        tag = "body" if obj.Forge_Model_Type == cons.ModelTypes.LINK else "frame"
        element = ET.SubElement(parentElement, tag)
        element.set("name", obj.name)
        element.set("pos", funcs.parse_prop_by_type(obj.matrix_local, "translation"))
        rotation_quaternion = obj.matrix_local.to_quaternion()
        element.set("quat", funcs.parse_value_by_attr(rotation_quaternion))

    elif obj.Forge_Model_Type == cons.ModelTypes.REPLICATE:
        element = ET.SubElement(parentElement, "replicate")
        data: ReplicateItem = obj.Forge_Replicate
        compiler: CompilerItem = context.scene.Forge_GlobalConfig.g_compiler

        for prop in def_props.REPLICATE_PROPS:
            if prop in def_props.REPLICATE_PROPS_REF:
                modifier_name = cons.AdditionalShapeModifiers[cons.ModelTypes.REPLICATE]
                if modifier_name not in obj.modifiers:
                    return
                attr = get_modifier_socket(obj.modifiers[modifier_name], def_props.REPLICATE_PROPS_REF[prop])
                if prop in {"offset", "euler"}:
                    attr = list(attr)
                if prop == "euler":
                    attr = [degrees(v) if compiler.angle == "DEGREE" else v for v in attr]
            else:
                attr = getattr(data, prop)
            if not is_property_default(data, prop, attr):
                element.set(prop, funcs.parse_value_by_attr(attr))

    if obj.Forge_Model_Type == cons.ModelTypes.LINK:
        data: LinkItem = obj.Forge_Link
        for prop in def_props.LINK_PROPS:
            attr = getattr(data, prop)
            if not is_property_default(data, prop, attr):
                element.set(prop, funcs.parse_value_by_attr(attr))

    template = instance_templates.get(obj.name) if instance_templates else None
    if template is not None:
        append_instance_subtree(context, element, obj, template, geometry_map, collider_map, geo_materials_map)
        return

    write_multibody_children(context, element, obj, geometry_map, collider_map, geo_materials_map, instance_templates)


def set_world(
    context: Context,
    parentElement: ET.Element,
    geometry_map: dict,
    hfield_map: dict,
    collider_map: dict,
    geo_materials_map: dict,
    report: Callable[[set[WmReportItems] | None, str], None],
    instance_templates: dict[str, Object] | None = None,
):
    """Exports root-level objects (cameras, lights, height-fields, planes, geometries,
    links, etc.) from the World collection into <worldbody>.

    Args:
        context: Blender context.
        parentElement: Parent XML element (typically <worldbody>).
        geometry_map: Mapping of geometry names to mesh file paths.
        hfield_map: Mapping of height-field names to file paths.
        collider_map: Mapping of collider names to mesh file paths.
        geo_materials_map: Mapping of geometry names to material names.
        report: Export report callback function.
        instance_templates: Mapping of instance link names to their template
            link objects; template links are not exported directly. Computed
            with :func:`funcs.collect_instance_templates` when omitted.

    Returns:
        True if objects were successfully exported, False otherwise.
    """

    if cons.CollectionNames.WORLD not in bpy.data.collections:
        report({"INFO"}, "Not find World collection")
        return False

    if instance_templates is None:
        instance_templates = funcs.collect_instance_templates(report)
    template_names = {template.name for template in instance_templates.values()}

    objects: list[Object] = []
    for coll_tag in [
        cons.CollectionNames.WORLD,
        cons.CollectionNames.LINK,
        cons.CollectionNames.INERTIAL,
        cons.CollectionNames.VISUAL,
        cons.CollectionNames.COLLIDER,
        cons.CollectionNames.JOINT,
        cons.CollectionNames.SITE,
        cons.CollectionNames.ACTUATOR,
        cons.CollectionNames.TENDON,
        cons.CollectionNames.EQUALITY,
        cons.CollectionNames.CONTACT,
        cons.CollectionNames.SENSOR,
        cons.CollectionNames.LIGHT,
        cons.CollectionNames.CAMERA,
        cons.CollectionNames.FRAME,
        cons.CollectionNames.REPLICATE,
        cons.CollectionNames.ATTACH,
        cons.CollectionNames.INCLUDE,
    ]:
        if coll_tag not in bpy.data.collections:
            continue
        coll = bpy.data.collections[coll_tag]
        for obj in coll.objects:
            if (
                obj.Forge_Model_Type
                in [
                    cons.ModelTypes.CAMERA,
                    cons.ModelTypes.LIGHT,
                    cons.ModelTypes.HFIELD,
                    cons.ModelTypes.PLANE,
                    cons.ModelTypes.VISUAL,
                    cons.ModelTypes.COLLIDER,
                    cons.ModelTypes.LINK,
                    cons.ModelTypes.FRAME,
                    cons.ModelTypes.ATTACH,
                    cons.ModelTypes.REPLICATE,
                ]
                and obj.parent is None
            ):
                objects.append(obj)

    objects = [
        obj
        for obj in objects
        if not (
            obj.Forge_Model_Type == cons.ModelTypes.LINK and (obj.name in template_names or obj.get("INSTANCE_LINK"))
        )
    ]

    if not objects:
        report({"ERROR"}, "Find 0 root object or mjcf tags object for export")
        return False

    worldbody = ET.SubElement(parentElement, "worldbody")

    objects = sorted(objects, key=lambda obj: funcs.order_map.get(obj.Forge_Model_Type, len(funcs.custom_order)))
    for obj in objects:
        if obj.hide_viewport:
            continue
        match obj.Forge_Model_Type:
            case cons.ModelTypes.CAMERA:
                set_camera_tags(worldbody, obj)
            case cons.ModelTypes.LIGHT:
                set_light_tags(worldbody, obj)
            case cons.ModelTypes.HFIELD:
                set_hfield_tags(worldbody, obj, hfield_map, geo_materials_map)
            case cons.ModelTypes.PLANE:
                set_plane_tags(worldbody, obj, geo_materials_map)
            case cons.ModelTypes.VISUAL:
                set_geom_tags(worldbody, obj, geometry_map, geo_materials_map)
                for child in obj.children:
                    if child.Forge_Model_Type != cons.ModelTypes.COLLIDER:
                        continue
                    set_geom_tags(worldbody, child, collider_map)
            case cons.ModelTypes.COLLIDER:
                set_geom_tags(worldbody, obj, collider_map)
            case cons.ModelTypes.SITE:
                set_site_tags(worldbody, obj)
            case cons.ModelTypes.LINK | cons.ModelTypes.FRAME | cons.ModelTypes.REPLICATE:
                set_multi_body(
                    context, worldbody, obj, geometry_map, collider_map, geo_materials_map, instance_templates
                )
            case cons.ModelTypes.ATTACH:
                set_attach_tags(worldbody, obj)

    return True


def add_contact(
    context: Context,
    parentElement: ET.Element,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Export contact pairs (pair/exclude/weld) from the CONTACT collection into XML.

    Args:
        context: The Blender context.
        parentElement: Parent XML element (typically ``<contact>``).
        report: Export report callback function.

    Returns:
        True if contact information was successfully exported, False otherwise.
    """

    if cons.CollectionNames.CONTACT not in bpy.data.collections:
        report({"INFO"}, "Not find Contact collection")
        return

    coll = bpy.data.collections[cons.CollectionNames.CONTACT]

    objects: list[Object] = []
    for obj in coll.objects:
        if obj.hide_viewport:
            continue
        if obj.Forge_Model_Type == cons.ModelTypes.CONTACT:
            objects.append(obj)

    if not objects:
        return

    contact = ET.SubElement(parentElement, "contact")
    for obj in objects:
        data: ContactItem = obj.Forge_Contact
        element = ET.SubElement(contact, data.type.lower())
        if data.type == cons.ContactTypes.EXCLUDE:
            element.set("body1", funcs.parse_prop_by_type(data, "target1"))
            element.set("body2", funcs.parse_prop_by_type(data, "target2"))
        else:
            element.set("geom1", funcs.parse_prop_by_type(data, "target1"))
            element.set("geom2", funcs.parse_prop_by_type(data, "target2"))
            for prop in def_props.CONTACT_TYPE_PROPS[data.type]:
                attr = getattr(data, prop)
                if not is_property_default(data, prop, attr):
                    element.set(prop, funcs.parse_value_by_attr(attr))


def add_equality(
    context: Context,
    parentElement: ET.Element,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Export equality constraints (connect/weld/joint) from the EQUALITY collection into XML.

    Args:
        context: The Blender context.
        parentElement: Parent XML element (typically ``<equality>``).
        report: Export report callback function.

    Returns:
        True if equality constraint information was successfully exported, False otherwise.
    """

    if cons.CollectionNames.EQUALITY not in bpy.data.collections:
        report({"INFO"}, "Not find Equality collection")
        return

    coll = bpy.data.collections[cons.CollectionNames.EQUALITY]

    objects: list[Object] = []
    for obj in coll.objects:
        if obj.hide_viewport:
            continue
        if obj.Forge_Model_Type == cons.ModelTypes.EQUALITY:
            objects.append(obj)

    if not objects:
        return

    equality = ET.SubElement(parentElement, "equality")
    for obj in objects:
        data: EqualityItem = obj.Forge_Equality
        element = ET.SubElement(equality, data.type.lower())
        element.set("name", obj.name)
        target_type = data.target_type.lower()
        if data.target_type == cons.EqualityTargetTypes.LINK:
            target_type = "body"
            element.set("anchor", funcs.parse_prop_by_type(data, "anchor"))
        element.set(f"{target_type}1", funcs.parse_prop_by_type(data, "target1"))
        if data.target2 is not None:
            element.set(f"{target_type}2", funcs.parse_prop_by_type(data, "target2"))

        for prop in def_props.EQUALITY_TYPE_PROPS[data.type]:
            if prop == "anchor":
                continue
            attr = getattr(data, prop)
            if not is_property_default(data, prop, attr):
                element.set(prop, funcs.parse_value_by_attr(attr))


def add_tendon(
    context: Context,
    parentElement: ET.Element,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Exports tendons from the TENDON collection into XML, including their referenced joints and coefficients.

    Args:
        context: Blender context.
        parentElement: Parent XML element (typically <tendon>).
        report: Export report callback function.

    Returns:
        True if tendon information was successfully exported, False otherwise.
    """

    if cons.CollectionNames.TENDON not in bpy.data.collections:
        report({"INFO"}, "Not find Tendon collection")
        return

    coll = bpy.data.collections[cons.CollectionNames.TENDON]

    objects: list[Object] = []
    for obj in coll.objects:
        if obj.hide_viewport:
            continue
        if obj.Forge_Model_Type == cons.ModelTypes.TENDON:
            objects.append(obj)

    if not objects:
        return

    tendon = ET.SubElement(parentElement, "tendon")
    for obj in objects:
        data: TendonItem = obj.Forge_Tendon
        element = ET.SubElement(tendon, data.type.lower())
        element.set("name", obj.name)

        for item in data.targets.items:
            childElement = ET.SubElement(element, "joint")
            childElement.set("joint", funcs.parse_prop_by_type(item, "target"))
            childElement.set("coef", funcs.parse_prop_by_type(item, "coef"))

        for prop in def_props.TENDON_TYPE_PROPS[data.type]:
            attr = getattr(data, prop)
            if not is_property_default(data, prop, attr):
                element.set(prop, funcs.parse_value_by_attr(attr))


def add_actuator(
    context: Context,
    parentElement: ET.Element,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Exports actuators from the ACTUATOR collection into XML, including target objects
    and type-specific properties.

    Args:
        context: Blender context.
        parentElement: Parent XML element (typically <actuator>).
        report: Export report callback function.

    Returns:
        True if actuator information was successfully exported, False otherwise.
    """

    if cons.CollectionNames.ACTUATOR not in bpy.data.collections:
        report({"INFO"}, "Not find Actuator collection")
        return

    coll = bpy.data.collections[cons.CollectionNames.ACTUATOR]

    objects: list[Object] = []
    for obj in coll.objects:
        if obj.hide_viewport:
            continue
        if obj.Forge_Model_Type == cons.ModelTypes.ACTUATOR:
            objects.append(obj)

    if not objects:
        return

    actuator = ET.SubElement(parentElement, "actuator")
    for obj in objects:
        data: ActuatorItem = obj.Forge_Actuator
        element = ET.SubElement(actuator, data.type.lower())
        element.set("name", obj.name)
        target_type = data.target_type.lower()
        if data.target_type == cons.EqualityTargetTypes.LINK:
            target_type = "body"
        element.set(target_type, funcs.parse_prop_by_type(data, "target"))

        for prop in def_props.ACTUATOR_TYPE_PROPS[data.type]:
            attr = getattr(data, prop)
            if not is_property_default(data, prop, attr):
                element.set(prop, funcs.parse_value_by_attr(attr))


def add_sensor(
    context: Context,
    parentElement: ET.Element,
    report: Callable[[set[WmReportItems] | None, str], None],
):
    """Exports sensors from the SENSOR collection into XML, including reference objects
    and type-specific properties.

    Args:
        context: Blender context.
        parentElement: Parent XML element (typically <sensor>).
        report: Export report callback function.

    Returns:
        True if sensor information was successfully exported, False otherwise.
    """

    if cons.CollectionNames.SENSOR not in bpy.data.collections:
        report({"INFO"}, "Not find Sensor collection")
        return

    coll = bpy.data.collections[cons.CollectionNames.SENSOR]

    objects: list[Object] = []
    for obj in coll.objects:
        if obj.hide_viewport:
            continue
        if obj.Forge_Model_Type == cons.ModelTypes.SENSOR:
            objects.append(obj)

    if not objects:
        return

    sensor = ET.SubElement(parentElement, "sensor")
    for obj in objects:
        data: SensorItem = obj.Forge_Sensor
        element = ET.SubElement(sensor, data.type.lower())
        element.set("name", obj.name)

        if data.type == "Contact":
            # Contact sensor -- export only the active filter group
            if data.target_type == cons.SensorTargetTypes.SUBTREE:
                element.set("subtree1", funcs.parse_prop_by_type(data, "target"))
                if data.ref:
                    element.set("subtree2", funcs.parse_prop_by_type(data, "ref"))
            elif data.target_type == cons.SensorTargetTypes.GEOM:
                element.set("geom1", funcs.parse_prop_by_type(data, "target"))
                if data.ref:
                    element.set("geom2", funcs.parse_prop_by_type(data, "ref"))
            elif data.target_type == cons.SensorTargetTypes.SITE:
                element.set("site", funcs.parse_prop_by_type(data, "target"))
            else:  # BODY or XBODY
                element.set("body1", funcs.parse_prop_by_type(data, "target"))
                if data.ref:
                    element.set("body2", funcs.parse_prop_by_type(data, "ref"))

            if not is_property_default(data, "num", data.num):
                element.set("num", funcs.parse_prop_by_type(data, "num"))
            if data.data and data.data != def_props.SENSOR_PROPS_DEFAULT["data"]:
                element.set("data", " ".join(sorted(data.data)))
            if not is_property_default(data, "reduce", data.reduce):
                element.set("reduce", funcs.parse_prop_by_type(data, "reduce"))
        else:
            for key, item in def_props.SENSOR_TYPE_PROPS[data.type].items():
                if key in ["reftype", "refname"]:
                    if data.ref:
                        element.set(key, funcs.parse_prop_by_type(data, item))
                else:
                    element.set(key, funcs.parse_prop_by_type(data, item))

        if not is_property_default(data, "noise", data.noise):
            element.set("noise", funcs.parse_prop_by_type(data, "noise"))
        if not is_property_default(data, "cutoff", data.cutoff):
            element.set("cutoff", funcs.parse_prop_by_type(data, "cutoff"))


def prettify(elem):
    """Formats an XML element tree into a prettily indented string (stripping the XML declaration header).

    Args:
        elem: XML root element.

    Returns:
        Formatted XML string.
    """

    rough_string = ET.tostring(elem, "utf-8")
    reparsed = minidom.parseString(rough_string)
    return (
        reparsed.toprettyxml(indent="  ").split("\n", 1)[1]
        if "\n" in reparsed.toprettyxml(indent="  ")
        else reparsed.toprettyxml(indent="  ")
    )
