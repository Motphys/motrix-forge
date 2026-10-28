View3DOverlay(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: View3DOverlay(bpy_struct)

   Settings for display of overlays in the 3D viewport

   .. attribute:: bone_wire_alpha

      Maximum opacity of bones in wireframe display mode

      :type: float in [0, inf], default 1.0

   .. attribute:: display_handle

      Limit the display of curve handles in edit mode

      :type: enum in [``'NONE'``, ``'SELECTED'``, ``'ALL'``], default ``'SELECTED'``

   .. attribute:: fade_inactive_alpha

      Strength of the fade effect

      :type: float in [0, 1], default 0.4

   .. attribute:: gpencil_fade_layer

      Fade layer opacity for Grease Pencil layers except the active one

      :type: float in [0, 1], default 0.5

   .. attribute:: gpencil_fade_objects

      Fade factor

      :type: float in [0, 1], default 0.5

   .. attribute:: gpencil_grid_color

      Canvas grid color

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.5, 0.5, 0.5)

   .. attribute:: gpencil_grid_offset

      Canvas grid offset

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: gpencil_grid_opacity

      Canvas grid opacity

      :type: float in [0.1, 1], default 0.9

   .. attribute:: gpencil_grid_scale

      Canvas grid scale

      :type: :class:`mathutils.Vector` of 2 items in [0, inf], default (1.0, 1.0)

   .. attribute:: gpencil_grid_subdivisions

      Canvas grid subdivisions

      :type: int in [1, 100], default 4

   .. attribute:: gpencil_vertex_paint_opacity

      Vertex Paint mix factor

      :type: float in [0, 1], default 1.0

   .. attribute:: grid_lines

      Number of grid lines to display in perspective view

      :type: int in [0, 1024], default 16

   .. attribute:: grid_scale

      Multiplier for the distance between 3D View grid lines

      :type: float in [0, inf], default 1.0

   .. data:: grid_scale_unit

      Grid cell size scaled by scene unit system settings

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. attribute:: grid_subdivisions

      Number of subdivisions between grid lines

      :type: int in [1, 1024], default 10

   .. attribute:: normals_constant_screen_size

      Screen size for normals in the 3D view

      :type: float in [0, 100000], default 7.0

   .. attribute:: normals_length

      Display size for normals in the 3D view

      :type: float in [1e-05, 100000], default 0.1

   .. attribute:: retopology_offset

      Offset used to draw edit mesh in front of other geometry

      :type: float in [0, inf], default 0.01

   .. attribute:: sculpt_curves_cage_opacity

      Opacity of the cage overlay in curves sculpt mode

      :type: float in [0, 1], default 0.0

   .. attribute:: sculpt_mode_face_sets_opacity

      :type: float in [0, 1], default 1.0

   .. attribute:: sculpt_mode_mask_opacity

      :type: float in [0, 1], default 0.75

   .. attribute:: show_annotation

      Show annotations for this view

      :type: boolean, default True

   .. attribute:: show_axis_x

      Show the X axis line

      :type: boolean, default True

   .. attribute:: show_axis_y

      Show the Y axis line

      :type: boolean, default True

   .. attribute:: show_axis_z

      Show the Z axis line

      :type: boolean, default False

   .. attribute:: show_bones

      Display bones (disable to show motion paths only)

      :type: boolean, default True

   .. attribute:: show_camera_guides

      Show camera composition guides

      :type: boolean, default True

   .. attribute:: show_camera_passepartout

      Show camera passepartout

      :type: boolean, default True

   .. attribute:: show_cursor

      Display 3D Cursor Overlay

      :type: boolean, default True

   .. attribute:: show_curve_normals

      Display 3D curve normals in editmode

      :type: boolean, default False

   .. attribute:: show_edge_bevel_weight

      Display weights created for the Bevel modifier

      :type: boolean, default True

   .. attribute:: show_edge_crease

      Display creases created for Subdivision Surface modifier

      :type: boolean, default True

   .. attribute:: show_edge_seams

      Display UV unwrapping seams

      :type: boolean, default True

   .. attribute:: show_edge_sharp

      Display sharp edges, used with the Edge Split modifier

      :type: boolean, default True

   .. attribute:: show_extra_edge_angle

      Display selected edge angle, using global values when set in the transform panel

      :type: boolean, default False

   .. attribute:: show_extra_edge_length

      Display selected edge lengths, using global values when set in the transform panel

      :type: boolean, default False

   .. attribute:: show_extra_face_angle

      Display the angles in the selected edges, using global values when set in the transform panel

      :type: boolean, default False

   .. attribute:: show_extra_face_area

      Display the area of selected faces, using global values when set in the transform panel

      :type: boolean, default False

   .. attribute:: show_extra_indices

      Display the index numbers of selected vertices, edges, and faces

      :type: boolean, default False

   .. attribute:: show_extras

      Object details, including empty wire, cameras and other visual guides

      :type: boolean, default True

   .. attribute:: show_face_center

      Display face center when face selection is enabled in solid shading modes

      :type: boolean, default False

   .. attribute:: show_face_normals

      Display face normals as lines

      :type: boolean, default False

   .. attribute:: show_face_orientation

      Show the Face Orientation Overlay

      :type: boolean, default False

   .. attribute:: show_faces

      Display a face selection overlay

      :type: boolean, default True

   .. attribute:: show_fade_inactive

      Fade inactive geometry using the viewport background color

      :type: boolean, default False

   .. attribute:: show_floor

      Show the ground plane grid

      :type: boolean, default True

   .. attribute:: show_freestyle_edge_marks

      Display Freestyle edge marks, used with the Freestyle renderer

      :type: boolean, default True

   .. attribute:: show_freestyle_face_marks

      Display Freestyle face marks, used with the Freestyle renderer

      :type: boolean, default True

   .. attribute:: show_light_colors

      Show light colors

      :type: boolean, default False

   .. attribute:: show_look_dev

      Show HDRI preview spheres

      :type: boolean, default False

   .. attribute:: show_motion_paths

      Show the Motion Paths Overlay

      :type: boolean, default True

   .. attribute:: show_object_origins

      Show object center dots

      :type: boolean, default True

   .. attribute:: show_object_origins_all

      Show the object origin center dot for all (selected and unselected) objects

      :type: boolean, default False

   .. attribute:: show_onion_skins

      Show the Onion Skinning Overlay

      :type: boolean, default False

   .. attribute:: show_ortho_grid

      Show grid in orthographic side view

      :type: boolean, default True

   .. attribute:: show_outline_selected

      Show an outline highlight around selected objects

      :type: boolean, default True

   .. attribute:: show_overlays

      Display overlays like gizmos and outlines

      :type: boolean, default True

   .. attribute:: show_paint_wire

      Use wireframe display in painting modes

      :type: boolean, default False

   .. attribute:: show_relationship_lines

      Show dashed lines indicating parent or constraint relationships

      :type: boolean, default True

   .. attribute:: show_retopology

      Hide the solid mesh and offset the overlay towards the view. Selection is occluded by inactive geometry, unless X-Ray is enabled

      :type: boolean, default False

   .. attribute:: show_sculpt_curves_cage

      Show original curves that are currently being edited

      :type: boolean, default False

   .. attribute:: show_sculpt_face_sets

      :type: boolean, default True

   .. attribute:: show_sculpt_mask

      :type: boolean, default True

   .. attribute:: show_split_normals

      Display vertex-per-face normals as lines

      :type: boolean, default False

   .. attribute:: show_stats

      Display scene statistics overlay text

      :type: boolean, default False

   .. attribute:: show_statvis

      Display statistical information about the mesh

      :type: boolean, default False

   .. attribute:: show_text

      Display overlay text

      :type: boolean, default True

   .. attribute:: show_vertex_normals

      Display vertex normals as lines

      :type: boolean, default False

   .. attribute:: show_viewer_attribute

      Show attribute overlay for active viewer node

      :type: boolean, default True

   .. attribute:: show_viewer_text

      Show attribute values as text in viewport

      :type: boolean, default False

   .. attribute:: show_weight

      Display weights in editmode

      :type: boolean, default False

   .. attribute:: show_wireframes

      Show face edges wires

      :type: boolean, default False

   .. attribute:: show_wpaint_contours

      Show contour lines formed by points with the same interpolated weight

      :type: boolean, default False

   .. attribute:: show_xray_bone

      Show the bone selection overlay

      :type: boolean, default False

   .. attribute:: texture_paint_mode_opacity

      Opacity of the texture paint mode stencil mask overlay

      :type: float in [0, 1], default 1.0

   .. attribute:: use_debug_freeze_view_culling

      Freeze view culling bounds

      :type: boolean, default False

   .. attribute:: use_gpencil_canvas_xray

      Show Canvas grid in front

      :type: boolean, default False

   .. attribute:: use_gpencil_edit_lines

      Show Edit Lines when editing strokes

      :type: boolean, default True

   .. attribute:: use_gpencil_fade_gp_objects

      Fade Grease Pencil Objects, except the active one

      :type: boolean, default False

   .. attribute:: use_gpencil_fade_layers

      Toggle fading of Grease Pencil layers except the active one

      :type: boolean, default False

   .. attribute:: use_gpencil_fade_objects

      Fade all viewport objects with a full color layer to improve visibility

      :type: boolean, default False

   .. attribute:: use_gpencil_grid

      Display a grid over Grease Pencil paper

      :type: boolean, default False

   .. attribute:: use_gpencil_multiedit_line_only

      Show Edit Lines only in multiframe

      :type: boolean, default False

   .. attribute:: use_gpencil_onion_skin

      Show ghosts of the keyframes before and after the current frame

      :type: boolean, default False

   .. attribute:: use_gpencil_onion_skin_active_object

      Show only the onion skins of the active object

      :type: boolean, default False

   .. attribute:: use_gpencil_show_directions

      Show stroke drawing direction with a bigger green dot (start) and smaller red dot (end) points

      :type: boolean, default False

   .. attribute:: use_gpencil_show_material_name

      Show material name assigned to each stroke

      :type: boolean, default False

   .. attribute:: use_normals_constant_screen_size

      Keep size of normals constant in relation to 3D view

      :type: boolean, default False

   .. attribute:: vertex_opacity

      Opacity for edit vertices

      :type: float in [0, 1], default 1.0

   .. attribute:: vertex_paint_mode_opacity

      Opacity of the texture paint mode stencil mask overlay

      :type: float in [0, 1], default 1.0

   .. attribute:: viewer_attribute_opacity

      Opacity of the attribute that is currently visualized

      :type: float in [0, 1], default 1.0

   .. attribute:: weight_paint_mode_opacity

      Opacity of the weight paint mode overlay

      :type: float in [0, 1], default 1.0

   .. attribute:: wireframe_opacity

      Opacity of the displayed edges (1.0 for opaque)

      :type: float in [0, 1], default 1.0

   .. attribute:: wireframe_threshold

      Adjust the angle threshold for displaying edges (1.0 for all)

      :type: float in [0, 1], default 1.0

   .. attribute:: xray_alpha_bone

      Opacity to use for bone selection

      :type: float in [0, 1], default 0.5

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.id_properties_clear`
   * :class:`bpy_struct.id_properties_ensure`
   * :class:`bpy_struct.id_properties_ui`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_overridable_library`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.pop`
   * :class:`bpy_struct.property_overridable_library_set`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.rna_ancestors`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   * :class:`SpaceView3D.overlay`

