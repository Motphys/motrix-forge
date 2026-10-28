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

import bpy

try:
    import coacd
except ImportError:
    coacd = None
import numpy as np
from bpy.props import BoolProperty, EnumProperty, FloatProperty, IntProperty
from bpy.types import Context, Operator

from ..core import constants as cons
from ..core import selection as sel
from ..settings import DEFAULT_COACD_NAME_TEMPLATE, get_addon_prefs


class Forge_OT_COACD(Operator):
    """Decompose a mesh into convex parts using CoACD.

    Collision-Aware Concavity and Tree Search (CoACD) decomposes a mesh into
    near-convex parts suitable for collision geometry. The algorithm uses MCTS
    (Monte Carlo Tree Search) guided by a concavity metric computed via
    Hausdorff distance sampling.
    """

    bl_idname = "forge.coacds"
    bl_label = "Convex Hull (CoACD)"
    bl_description = "Create accurate convex hulls using Collision-Aware Concavity and Tree Search"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context: Context):
        """Check whether the operator can run; requires Object mode."""
        return context.mode == "OBJECT" and sel.check_selected_model_types(
            context,
            [
                cons.ModelTypes.VISUAL,
            ],
        )

    Preprocess_Mode = (
        ("Auto", "Auto", "", -1),
        ("On", "On", "", 0),
        ("Off", "Off", "", 1),
    )

    Approximate_Mode = (
        ("CH", "Convex Hulls", "", -1),
        ("Box", "Box", "", 0),
    )

    threshold: FloatProperty(
        name="Threshold",
        description="Concavity threshold for terminating the decomposition (0.01~1)\n  default = 0.05.",
        default=0.05,
        min=0.01,
        max=1.0,
    )  # type: ignore
    max_convex_hull: IntProperty(
        name="Max Convex Hull",
        description="""Max # convex hulls, -1 for no maximum limitation, works only when merge is enabled,
        default = -1 (may introduce convex hull with a concavity larger than the threshold.""",
        default=-1,
    )  # type: ignore
    preprocess_mode: EnumProperty(
        items=Preprocess_Mode,
        name="Preprocess Mode",
        description="""Choose manifold preprocessing mode:
        'auto': automatically check mesh manifoldness;
        'on': force turn on the pre-processing;
        'off': force turn off the pre-processing.""",
        default="Auto",
    )  # type: ignore
    preprocess_resolution: IntProperty(
        name="Preprocess Resolution",
        description="Resolution for manifold preprocess (20~100),\n  default = 50.",
        default=50,
        min=20,
        max=100,
    )  # type: ignore
    resolution: IntProperty(
        name="Sample Resolution",
        description="Sampling resolution for Hausdorff distance calculation (1e3~1e4), \n  default = 2000.",
        default=2000,
        min=1000,
        max=10000,
    )  # type: ignore
    mcts_nodes: IntProperty(
        name="MCTS nodes",
        description="Max number of child nodes in MCTS (10~40), \n  default = 20.",
        default=20,
        min=10,
        max=40,
    )  # type: ignore
    mcts_iterations: IntProperty(
        name="MCTS Iteration",
        description="Number of search iterations in MCTS (60~2000), \n  default = 100.",
        default=100,
        min=60,
        max=2000,
    )  # type: ignore
    mcts_max_depth: IntProperty(
        name="MCTS Max Depth",
        description="Max search depth in MCTS (2~7), \n  default = 3.",
        default=3,
        min=2,
        max=7,
    )  # type: ignore
    pca: BoolProperty(
        name="PCA",
        description="Flag to enable PCA pre-processing, \n  default = false.",
        default=False,
    )  # type: ignore
    merge: BoolProperty(
        name="Merge",
        description="Flag to disable merge postprocessing, \n  default = false.",
        default=True,
    )  # type: ignore
    decimate: BoolProperty(
        name="Decimate",
        description="Enable max vertex constraint per convex hull, \n  default = false.",
        default=False,
    )  # type: ignore
    max_ch_vertex: IntProperty(
        name="Max Convex Hull vertex",
        description="Max vertex value for each convex hull, **only when decimate is enabled**, \n  default = 128.",
        default=128,
        min=4,
    )  # type: ignore
    extrude: BoolProperty(
        name="Extrude",
        description="""Extrude neighboring convex hulls along the overlapping faces (other faces unchanged),
        default = false.""",
        default=False,
    )  # type: ignore
    extrude_margin: FloatProperty(
        name="Extrude Margin",
        description="Extrude margin, **only when extrude is enabled**, \n  default = 0.01.",
        default=0.01,
    )  # type: ignore
    apx_mode: EnumProperty(
        items=Approximate_Mode,
        name="Approximation Shape",
        description="Approximation shape type (convex hulls or cubes), \n  default = convex hulls.",
        default="CH",
    )  # type: ignore
    seed: IntProperty(
        name="Seed",
        description="Random seed used for sampling, \n  default = random().",
        default=0,
    )  # type: ignore

    def execute(self, context: Context):
        """Run the CoACD decomposition on the active mesh object.

        Triangulates the mesh, runs CoACD decomposition, then creates new mesh
        objects for each convex hull part in the same collection. Each hull is
        tagged as a collider mesh.
        """

        if coacd is None:
            self.report({"ERROR"}, "The coacd package is not installed")
            return {"CANCELLED"}

        prefs = get_addon_prefs()

        # Headless sessions register the operators without an add-on entry, so
        # the preferences can be missing; fall back to the property's default
        # rather than failing the whole decomposition.
        coacd_name_template = prefs.coacd_name_template if prefs else DEFAULT_COACD_NAME_TEMPLATE
        if coacd_name_template.find("?") == -1:
            self.report({"ERROR"}, "Can only match hulls to a name template containing a '?' character.")
            return {"CANCELLED"}

        selected = context.selected_objects

        if not selected:
            self.report({"ERROR"}, "None Object selected")
            return {"CANCELLED"}

        for source_obj in context.selected_objects:
            if source_obj is not None and source_obj.type == "MESH":
                depsgraph = context.evaluated_depsgraph_get()
                evaluated_obj = source_obj.evaluated_get(depsgraph)
                evaluated_mesh = evaluated_obj.to_mesh()
                try:
                    evaluated_mesh.calc_loop_triangles()
                    vertices = [list(vertex.co[:]) for vertex in evaluated_mesh.vertices]
                    faces = [list(triangle.vertices[:]) for triangle in evaluated_mesh.loop_triangles]
                finally:
                    evaluated_obj.to_mesh_clear()

                if not vertices or not faces:
                    self.report({"ERROR"}, "The evaluated mesh has no triangles")
                    return {"CANCELLED"}

                coll = source_obj.users_collection[0]
                source_matrix = source_obj.matrix_world.copy()
                mesh = coacd.Mesh(np.asarray(vertices), np.asarray(faces))
                result = coacd.run_coacd(
                    mesh,
                    self.threshold,
                    self.max_convex_hull,
                    self.preprocess_mode.lower(),
                    self.preprocess_resolution,
                    self.resolution,
                    self.mcts_nodes,
                    self.mcts_iterations,
                    self.mcts_max_depth,
                    self.pca,
                    self.merge,
                    self.decimate,
                    self.max_ch_vertex,
                    self.extrude,
                    self.extrude_margin,
                    self.apx_mode.lower(),
                    self.seed,
                )  # a list of convex hulls.
                if not result:
                    self.report({"ERROR"}, "CoACD did not generate any convex hulls")
                    continue

                for index, hull in enumerate(result):
                    vs, fs = hull
                    vertices = [v[:] for v in vs]
                    faces = [f[:] for f in fs]
                    mesh = bpy.data.meshes.new("new_mesh")
                    mesh.from_pydata(vertices, [], faces)
                    mesh.update()

                    indexed_template = coacd_name_template.replace("#", "%03d" % (index + 1), 1)
                    name = indexed_template.replace("?", source_obj.name, 1)

                    hull_obj = bpy.data.objects.new(name, mesh)
                    hull_obj.name = name
                    hull_obj.data.name = name
                    # Follow whatever the source visual follows (usually its
                    # link), keeping the hull at the source's world position.
                    parent = source_obj.parent
                    if parent is not None:
                        hull_obj.parent = parent
                        hull_obj.matrix_parent_inverse = parent.matrix_world.inverted()
                    hull_obj.matrix_world = source_matrix
                    hull_obj.Forge_Model_Type = cons.ModelTypes.COLLIDER
                    hull_obj.Forge_Geometry.type = cons.GeometryTypes.MESH
                    hull_obj.Forge_Geometry.group = cons.GeometryGroup.COLLIDER
                    coll.objects.link(hull_obj)
            else:
                self.report({"ERROR"}, "Object is not a mesh")
                continue

        return {"FINISHED"}

    def invoke(self, context: Context, event):
        """Show the CoACD parameter dialog with a width of 320 pixels."""
        wm = context.window_manager
        bpy.ops.wm.console_toggle()
        return wm.invoke_props_dialog(self, width=320)

    def draw(self, context: Context):
        """Draw the CoACD parameter panel in the operator dialog."""
        layout = self.layout

        col = layout.column()
        col.label(text="CoACD Parameters:")
        col.prop(self, "threshold")
        row = col.row()
        row.active = self.merge
        row.prop(self, "max_convex_hull")
        col.prop(self, "preprocess_mode")
        col.prop(self, "preprocess_resolution")
        col.prop(self, "resolution")
        col.prop(self, "mcts_nodes")
        col.prop(self, "mcts_iterations")
        col.prop(self, "mcts_max_depth")
        col.prop(self, "pca")
        col.prop(self, "merge")
        col.prop(self, "decimate")
        row = col.row()
        row.active = self.decimate
        row.prop(self, "max_ch_vertex")
        col.prop(self, "extrude")
        row = col.row()
        row.active = self.extrude
        row.prop(self, "extrude_margin")
        # col.prop(self, "apx_mode")
        col.prop(self, "seed")
        layout.separator()
        col = layout.column()
        col.label(text="WARNING:", icon="ERROR")
        col.label(text="  Processing can take several minutes per object!")
        col.label(text="  See Console Window for progress..,")
