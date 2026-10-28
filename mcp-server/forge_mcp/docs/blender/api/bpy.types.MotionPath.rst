MotionPath(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MotionPath(bpy_struct)

   Cache of the world-space positions of an element over a frame range

   .. attribute:: color

      Custom color for motion path before the current frame

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: color_post

      Custom color for motion path after the current frame

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. data:: frame_end

      End frame of the stored range

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: frame_start

      Starting frame of the stored range

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: is_modified

      Path is being edited

      :type: boolean, default False

   .. data:: length

      Number of frames cached

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: line_thickness

      Line thickness for motion path

      :type: int in [1, 6], default 0

   .. attribute:: lines

      Use straight lines between keyframe points

      :type: boolean, default False

   .. data:: points

      Cached positions per frame

      :type: :class:`bpy_prop_collection` of :class:`MotionPathVert`, (readonly)

   .. data:: use_bone_head

      For PoseBone paths, use the bone head location when calculating this path

      :type: boolean, default False, (readonly)

   .. attribute:: use_custom_color

      Use custom color for this motion path

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

   * :class:`Object.motion_path`
   * :class:`PoseBone.motion_path`

