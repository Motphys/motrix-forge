ThemeView3D(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeView3D(bpy_struct)

   Theme settings for the 3D viewport

   .. attribute:: act_spline

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: after_current_frame

      The color for things after the current frame (for onion skinning, motion paths, etc.)

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: asset_shelf

      Settings for asset shelf

      :type: :class:`ThemeAssetShelf`, (readonly, never None)

   .. attribute:: before_current_frame

      The color for things before the current frame (for onion skinning, motion paths, etc.)

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: bone_locked_weight

      Shade for bones corresponding to a locked weight group during painting

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: bone_pose

      Outline color of selected pose bones

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: bone_pose_active

      Outline color of active pose bones

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: bone_solid

      Default color of the solid shapes of bones

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: bundle_solid

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: camera

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: camera_passepartout

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: camera_path

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: clipping_border_3d

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: edge_bevel

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_crease

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_facesel

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_mode_select

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_seam

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_select

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_sharp

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: edge_width

      :type: int in [1, 32], default 0

   .. attribute:: editmesh_active

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: empty

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: extra_edge_angle

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: extra_edge_len

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: extra_face_angle

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: extra_face_area

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: face

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: face_back

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: face_dot

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: face_front

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: face_mode_select

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: face_retopology

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: face_select

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: facedot_size

      :type: int in [1, 10], default 0

   .. attribute:: frame_current

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: freestyle_edge_mark

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: freestyle_face_mark

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: gp_vertex

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_select

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: gp_vertex_size

      :type: int in [1, 10], default 0

   .. attribute:: grid

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: handle_align

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_auto

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_free

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_align

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_auto

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_free

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_sel_vect

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: handle_vect

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: lastsel_point

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: light

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: normal

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: nurb_sel_uline

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: nurb_sel_vline

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: nurb_uline

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: nurb_vline

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: object_active

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: object_origin_size

      Diameter in pixels for object/light origin display

      :type: int in [4, 10], default 0

   .. attribute:: object_selected

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: outline_width

      :type: int in [1, 5], default 0

   .. attribute:: paint_curve_handle

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: paint_curve_pivot

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: skin_root

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: space

      Settings for space

      :type: :class:`ThemeSpaceGradient`, (readonly, never None)

   .. attribute:: speaker

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: split_normal

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text_grease_pencil

      Color for indicating Grease Pencil keyframes

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text_keyframe

      Color for indicating object keyframes

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: transform

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex_bevel

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex_normal

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex_select

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vertex_size

      :type: int in [1, 32], default 0

   .. attribute:: vertex_unreferenced

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: view_overlay

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: wire

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: wire_edit

      Color for wireframe when in edit mode, but edge selection is active

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

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

   * :class:`Theme.view_3d`

