ThemeSequenceEditor(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeSequenceEditor(bpy_struct)

   Theme settings for the Sequence Editor

   .. attribute:: active_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: audio_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: color_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: draw_action

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: effect_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: frame_current

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: grid

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: image_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe

      Color of Keyframe

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_border

      Color of keyframe border

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: keyframe_border_selected

      Color of selected keyframe border

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: keyframe_breakdown

      Color of breakdown keyframe

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_breakdown_selected

      Color of selected breakdown keyframe

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_generated

      Color of generated keyframe

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_generated_selected

      Color of selected generated keyframe

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_movehold

      Color of moving hold keyframe

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_movehold_selected

      Color of selected moving hold keyframe

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: keyframe_selected

      Color of selected keyframe

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: mask_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: meta_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: metadatabg

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: metadatatext

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: movie_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: movieclip_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: preview_back

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: preview_range

      Color of preview range overlay

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: row_alternate

      Overlay color on every other row

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: scene_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: selected_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: selected_text

      Text strip editing selection

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. data:: space

      Settings for space

      :type: :class:`ThemeSpaceGeneric`, (readonly, never None)

   .. data:: space_list

      Settings for space list

      :type: :class:`ThemeSpaceListGeneric`, (readonly, never None)

   .. attribute:: text_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: text_strip_cursor

      Text strip editing cursor

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: time_marker_line

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: time_marker_line_selected

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: time_scrub_background

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: transition_strip

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: window_sliders

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

   * :class:`Theme.sequence_editor`

