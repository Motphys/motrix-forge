AnimVizMotionPaths(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AnimVizMotionPaths(bpy_struct)

   Motion Path settings for animation visualization

   .. attribute:: bake_location

      When calculating Bone Paths, use Head or Tips

      :type: enum in :ref:`rna_enum_motionpath_bake_location_items`, default ``'TAILS'``

   .. attribute:: frame_after

      Number of frames to show after the current frame (only for 'Around Frame' Onion-skinning method)

      :type: int in [1, 524287], default 0

   .. attribute:: frame_before

      Number of frames to show before the current frame (only for 'Around Frame' Onion-skinning method)

      :type: int in [1, 524287], default 0

   .. attribute:: frame_end

      End frame of range of paths to display/calculate (not for 'Around Frame' Onion-skinning method)

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      Starting frame of range of paths to display/calculate (not for 'Around Frame' Onion-skinning method)

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_step

      Number of frames between paths shown (not for 'On Keyframes' Onion-skinning method)

      :type: int in [1, 100], default 0

   .. data:: has_motion_paths

      Are there any bone paths that will need updating (read-only)

      :type: boolean, default False, (readonly)

   .. attribute:: range

      Type of range to calculate for Motion Paths

      :type: enum in :ref:`rna_enum_motionpath_range_items`, default ``'SCENE'``

   .. attribute:: show_frame_numbers

      Show frame numbers on Motion Paths

      :type: boolean, default False

   .. attribute:: show_keyframe_action_all

      For bone motion paths, search whole Action for keyframes instead of in group with matching name only (is slower)

      :type: boolean, default False

   .. attribute:: show_keyframe_highlight

      Emphasize position of keyframes on Motion Paths

      :type: boolean, default False

   .. attribute:: show_keyframe_numbers

      Show frame numbers of Keyframes on Motion Paths

      :type: boolean, default False

   .. attribute:: type

      Type of range to show for Motion Paths

      :type: enum in :ref:`rna_enum_motionpath_display_type_items`, default ``'RANGE'``

   .. attribute:: use_camera_space_bake

      Motion path points will be baked into the camera space of the active camera. This means they will only look right when looking through that camera. Switching cameras using markers is not supported.

      :type: boolean, default False

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

   * :class:`AnimViz.motion_path`

