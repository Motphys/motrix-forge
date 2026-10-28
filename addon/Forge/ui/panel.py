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

from bpy.types import Context, Panel

from ..core.common import get_socket
from ..core.props import Forge_Props
from ..mcp import operator as ops
from ..mcp.utils import get_server
from ..ops import coacd, operator
from ..settings import Get_Logo_Icon_ID, get_addon_prefs


class Forge_Panel(Panel):
    """Forge Main Panel

    The main information panel for the Forge toolset displayed in the Blender 3D viewport UI sidebar.
    Shows an overview of the toolset name, purpose, and version info for multi-articulated body and
    world configuration tools.
    """

    bl_label = "Forge"
    bl_idname = "FORGE_PT_PANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Forge"

    def draw_header(self, context: Context):
        """Draw the panel header"""
        layout = self.layout
        layout.label(icon_value=Get_Logo_Icon_ID())

    def draw(self, context: Context):
        """Draw the panel content

        Displays basic info including the toolset name, feature description, and usage tips.
        """
        layout = self.layout
        _prefs = get_addon_prefs()

        cold = layout.column(align=True)
        cold.label(text="Infos:")
        cold.label(text="Multi-Articulated & World Configuration Tools")
        cold.label(text="Tools to use to create and modify multi-articulated body simulation world with *.xml")


class Forge_MCP_Panel(Panel):
    """MCP Server Control Panel

    Manages and controls the start/stop of the MCP (Model Context Protocol) server.
    Displays the server connection status (running/stopped via header icon),
    and provides configuration for host address, port number, and logging options.
    """

    bl_label = "MCP Server"
    bl_idname = "FORGE_MCP_PT_PANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Forge"

    def draw_header(self, context: Context):
        """Draw the panel header showing linked/unlinked icon based on server status."""

        layout = self.layout
        mcp_server = get_server()
        if mcp_server and mcp_server.is_running():
            layout.label(icon="LINKED")
        else:
            layout.label(icon="UNLINKED")

    def draw(self, context: Context):
        """Draw the panel content

        Renders the MCP server host/port configuration, start/stop button, and log toggle.
        """
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        prefs = get_addon_prefs()
        mcp_server = get_server()

        box = layout.box()
        if prefs is None:
            box.label(text="Add-on preferences unavailable", icon="ERROR")
            return

        col = box.column()
        col.prop(prefs, "host")
        col.prop(prefs, "port")

        row = box.row(align=True).split(factor=0.4)
        row.alignment = "RIGHT"
        if mcp_server and mcp_server.is_running():
            row.label(text=ops.MCP_OT_Server_Stop.bl_label)
            row.operator(ops.MCP_OT_Server_Stop.bl_idname, icon="PAUSE", text="")
        else:
            row.label(text=ops.MCP_OT_Server_Start.bl_label)
            row.operator(ops.MCP_OT_Server_Start.bl_idname, icon="PLAY", text="")

        col = box.column()
        col.prop(prefs, "use_log")
        if prefs.autostart_error:
            box.label(text=prefs.autostart_error, icon="ERROR")


class Forge_Define_Panel(Panel):
    """Model Define Panel

    Provides a comprehensive set of operators for model definition, including:
        - Global settings: global properties and visual properties
        - General operations: type define and batch rename
        - Geometry operations: geometry/collider creation & define, heightfield/plane creation, mesh check
        - Kinematics operations: link/joint creation, root marking, joint/parent/inertial define
        - Hardware operations: actuator, site, tendon, equality, sensor, contact, light, camera creation & define
        - Tag selection and gizmo scale controls
    """

    bl_label = "Model Define"
    bl_idname = "FORGE_DEFINE_PT_PANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Forge"

    def draw_header(self, context: Context):
        """Draw the panel header"""
        layout = self.layout
        layout.label(icon="OBJECT_DATA")

    def draw(self, context: Context):
        """Draw the panel content

        Renders all model define operator groups and gizmo scale controls.
        """

        forge_props: Forge_Props = context.scene.Forge_Props
        layout = self.layout
        box = layout.box()

        # * Global Operators
        col = box.column(align=True)
        col.label(text="Global", icon="SCENE_DATA")
        row = col.row(align=True)
        row.operator(operator.Forge_OT_PROPERTIES_Global.bl_idname)
        row.operator(operator.Forge_OT_PROPERTIES_Visual.bl_idname)

        # * General Operators
        col = box.column(align=True)
        col.label(text="General", icon="META_CUBE")
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Type_Define.bl_idname)
        row.operator(operator.Forge_OT_Batch_Rename.bl_idname)

        # * Geometry Operators
        col = box.column(align=True)
        col.label(text="Geometry", icon="GEOMETRY_SET")
        row = col.row(align=True)
        crow = row.row(align=True)
        crow.operator(operator.Forge_OT_Geometry_Creation.bl_idname)
        crow = row.row(align=True)
        crow.operator(operator.Forge_OT_Collider_Creation.bl_idname)
        row = col.row(align=True)
        crow = row.row(align=True)
        crow.operator(operator.Forge_OT_Geometry_Define.bl_idname)
        crow = row.row(align=True)
        crow.operator(operator.Forge_OT_Collider_Define.bl_idname)
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator(operator.Forge_OT_HeightField_Creation.bl_idname)
        row.operator(operator.Forge_OT_Plane_Creation.bl_idname)
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Mesh_Check.bl_idname)

        # * Material Operators
        col = box.column(align=True)
        col.label(text="Material", icon="MATERIAL")
        grid = col.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=True, align=True)
        grid.operator(operator.Forge_OT_Material_Creation.bl_idname)
        grid.operator(operator.Forge_OT_Checker_Material_Creation.bl_idname)
        col.operator(operator.Forge_OT_Material_Assign.bl_idname)

        # * Kinematics Operators
        col = box.column(align=True)
        col.label(text="Kinematics", icon="OUTLINER_DATA_ARMATURE")
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Link_Creation.bl_idname)
        row.operator(operator.Forge_OT_Joint_Creation.bl_idname)
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Link_MarkRoot.bl_idname)
        row.operator(operator.Forge_OT_Joint_Define.bl_idname)
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Parent_Define.bl_idname)
        row.operator(operator.Forge_OT_Inertial_Creation.bl_idname)

        # * Kinematics Instance
        col = box.column(align=True)
        col.label(text="Instance", icon="MOD_INSTANCE")
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Instance_Mark.bl_idname)
        row = col.row(align=True)
        row.prop(forge_props, "instance_body", text="Instance")
        row = col.row(align=True)
        row.operator(operator.Forge_OT_InstanceSet.bl_idname)

        # * Hardware Operators
        col = box.column(align=True)
        col.label(text="Hardware", icon="MOD_SCREW")
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Actuator_Creation.bl_idname)
        row.operator(operator.Forge_OT_Site_Creation.bl_idname)
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Actuator_Define.bl_idname)
        row.operator(operator.Forge_OT_Site_Define.bl_idname)
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Tendon_Creation.bl_idname)
        row.operator(operator.Forge_OT_Equality_Creation.bl_idname)
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Sensor_Creation.bl_idname)
        row.operator(operator.Forge_OT_Contact_Creation.bl_idname)
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator(operator.Forge_OT_Light_Creation.bl_idname)
        row.operator(operator.Forge_OT_Camera_Creation.bl_idname)

        col = box.column(align=True)
        row = col.row(align=True)
        row.prop(forge_props, "select_tag", text="Tag")
        row = col.row(align=True)
        row.operator(operator.Forge_OT_SelectByTAG.bl_idname, text="Select")

        col = box.column(align=True)
        row = col.row(align=True)
        row.prop(forge_props, "select_model_type", text="Type")
        row = col.row(align=True)
        row.operator(operator.Forge_OT_SelectByModelType.bl_idname, text="Select")

        col = box.column(align=True)
        col.label(text="Gizmo display size *= scale ")
        row = col.row(align=True)
        row.prop(forge_props, "scale_factor", expand=True)
        row = col.row(align=True)
        row.prop(forge_props, "gizmo_scale", text="Ratio")
        row.operator(operator.Forge_OT_Change_Gizmo_Size.bl_idname, text="", icon="PLAY")


class Forge_Meta_Elements_Panel(Panel):
    """Meta Elements Panel

    Provides tools to add other scenes or bodies as references into the current scene.
    Includes frame creation, replication, attach, and include operations.
    """

    bl_label = "Meta Elements"
    bl_idname = "FORGE_META_ELEMENTS_PT_PANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_description = "Add Other Scene Or Body As Reference"
    bl_category = "Forge"

    def draw_header(self, context: Context):
        """Draw the panel header"""
        layout = self.layout
        layout.label(icon="META_DATA")

    def draw(self, context: Context):
        """Draw the panel content

        Renders the meta element operator grid (frame, replicate, attach, include).
        """

        layout = self.layout
        # Attach/include tasks run in a temporary child scene, while their
        # progress state belongs to the main scene.  Resolve that scene before
        # checking the operation flags so the progress bars remain visible
        # while the active window scene changes.
        scene = context.scene
        main_scene = context.blend_data.scenes.get(scene.Main_Scene)
        forge_props: Forge_Props = (main_scene or scene).Forge_Props

        box = layout.box()
        gird = box.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=True, align=True)
        gird.operator(operator.Forge_OT_Frame_Creation.bl_idname)
        gird.operator(operator.Forge_OT_Replicate_Creation.bl_idname)
        gird.operator(operator.Forge_OT_Attach.bl_idname)
        gird.operator(operator.Forge_OT_Include.bl_idname)

        if forge_props.is_attaching or forge_props.is_including:
            box = layout.box()
            col = box.column(align=True)
            col.progress(factor=forge_props.progress, type="BAR", text=forge_props.progress_info)
            col.progress(
                factor=forge_props.sub_progress,
                type="BAR",
                text=forge_props.sub_progress_info,
            )


class Forge_CoACD_Panel(Panel):
    """CoACD Convex Hull Generation Panel

    Generates convex hulls (convex decomposition) for complex mesh models
    using the COACD (Convex Optimization for Approximate Convex Decomposition) algorithm.
    This panel is collapsed by default to keep the interface tidy.
    """

    bl_label = "CoACD"
    bl_idname = "FORGE_COACD_PT_PANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_description = "Generate convex for complex mesh"
    bl_category = "Forge"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context: Context):
        """Draw the panel header"""
        layout = self.layout
        layout.label(icon="MESH_ICOSPHERE")

    def draw(self, context: Context):
        """
        Draw the panel content

                    Renders the CoACD convex generation and hull selection buttons.
        """

        layout = self.layout

        col = layout.column(align=True)
        col.operator(coacd.Forge_OT_COACD.bl_idname)
        col.operator(operator.Forge_OT_SelectHulls.bl_idname)


class Forge_Import_Panel(Panel):
    """Import Panel

    Provides functionality to import models from mjcf files (XML format).
    Supports toggling material import, selecting XML file paths, and displays import progress.
    """

    bl_label = "Import"
    bl_idname = "FORGE_IMPORT_PT_PANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_description = "Import A MJCF File"
    bl_category = "Forge"

    def draw_header(self, context: Context):
        """Draw the panel header"""
        layout = self.layout
        layout.label(icon="IMPORT")

    def draw(self, context: Context):
        """Draw the panel content

        Renders the material toggle, file path selector, and import button;
        shows a progress bar during import.
        """

        scene = context.scene
        main_scene = context.blend_data.scenes.get(scene.Main_Scene)
        forge_props: Forge_Props = (main_scene or scene).Forge_Props
        layout = self.layout

        box = layout.box()
        col = box.column(align=True)
        col.prop(forge_props, "import_material")
        row = col.row(align=True)
        row.prop(forge_props, "import_file_path", text="File")
        row.operator(
            operator.Forge_OT_SelectImportPath.bl_idname,
            text="",
            icon="FILE_FOLDER",
        )

        if forge_props.is_importing:
            col.progress(factor=forge_props.progress, type="BAR", text=forge_props.progress_info)
            col.progress(
                factor=forge_props.sub_progress,
                type="BAR",
                text=forge_props.sub_progress_info,
            )
        else:
            col.operator(operator.Forge_OT_Import.bl_idname, text="Import")

        header, body = layout.panel("Attention_Info", default_closed=True)
        header.alert = True
        header.label(text="Attention", icon="WARNING_LARGE")
        if body:
            body.alert = True
            col = body.column(align=True)
            col.label(text="Import will purge all scene data")
            col.label(text="The current scene will be cleared before import.")
            col.label(text="!!! Make sure you have saved your work.")


class Forge_Export_Panel(Panel):
    """Export Panel

    Provides functionality to export the current scene to mjcf file format.
    Supports an incremental update mode for existing files and customizable export path.
    """

    bl_label = "Export"
    bl_idname = "FORGE_EXPORT_PT_PANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_description = "Export To MJCF File"
    bl_category = "Forge"

    def draw_header(self, context: Context):
        """Draw the panel header"""
        layout = self.layout
        layout.label(icon="EXPORT")

    def draw(self, context: Context):
        """Draw the panel content

        Renders the update mode toggle, export path selector, and export button.
        """

        scene = context.scene
        main_scene = context.blend_data.scenes.get(scene.Main_Scene)
        forge_props: Forge_Props = (main_scene or scene).Forge_Props
        layout = self.layout

        box = layout.box()
        col = box.column(align=True)
        col.prop(forge_props, "update_forge_only", text="Only Update File")
        col.separator()
        row = col.row(align=True)
        row.prop(forge_props, "export_path", text="Path")
        row.operator(
            operator.Forge_OT_SelectExportPath.bl_idname,
            text="",
            icon="FILE_FOLDER",
        )
        if forge_props.is_exporting:
            col.progress(factor=forge_props.progress, type="BAR", text=forge_props.progress_info)
            col.progress(
                factor=forge_props.sub_progress,
                type="BAR",
                text=forge_props.sub_progress_info,
            )
        else:
            col.operator(operator.Forge_OT_Export.bl_idname, text="Export")


class Forge_Properties_Panel(Panel):
    """Properties Mark Panel

    Displays all custom properties of the currently selected object in the sidebar
    as a key-value pair list, allowing users to quickly view and edit marker data
    attached to objects.
    """

    bl_label = "Properties Mark"
    bl_idname = "FORGE_PROPERTIES_PT_PANEL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_description = "View and edit custom properties of selected object"
    bl_category = "Forge"

    def draw_header(self, context: Context):
        """Draw the panel header"""
        layout = self.layout
        layout.label(icon="OBJECT_DATA")

    def draw(self, context: Context):
        """Draw the panel content

        Iterates over all custom properties of the currently selected object
        and displays them line by line. Each property shows its key name and
        an editable value field. Shows an empty box if no object is selected.
        """

        layout = self.layout
        obj = context.object

        box = layout.box()
        if obj is not None:
            for key, value in obj.items():
                col = box.column()
                row = col.row(align=True).split(factor=0.25)
                row.label(text=key)
                if isinstance(value, (bool, int, float, str)):
                    row.prop(obj, get_socket(key), text="")
                else:
                    row.label(text=str(value))


classes = (
    coacd.Forge_OT_COACD,
    Forge_Panel,
    Forge_MCP_Panel,
    Forge_Define_Panel,
    Forge_Meta_Elements_Panel,
    Forge_CoACD_Panel,
    Forge_Import_Panel,
    Forge_Export_Panel,
    Forge_Properties_Panel,
)
