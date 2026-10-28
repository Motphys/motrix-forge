GreasePencilFrames(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GreasePencilFrames(bpy_struct)

   Collection of Grease Pencil frames

   .. method:: new(frame_number)

      Add a new Grease Pencil frame

      :arg frame_number: Frame Number, The frame on which the drawing appears
      :type frame_number: int in [-1048574, 1048574]
      :return: The newly created frame
      :rtype: :class:`GreasePencilFrame`

   .. method:: remove(frame_number)

      Remove a Grease Pencil frame

      :arg frame_number: Frame Number, The frame number of the frame to remove
      :type frame_number: int in [-1048574, 1048574]

   .. method:: copy(from_frame_number, to_frame_number, *, instance_drawing=False)

      Copy a Grease Pencil frame

      :arg from_frame_number: Source Frame Number, The frame number of the source frame
      :type from_frame_number: int in [-1048574, 1048574]
      :arg to_frame_number: Frame Number of Copy, The frame number to copy the frame to
      :type to_frame_number: int in [-1048574, 1048574]
      :arg instance_drawing: Instance Drawing, Let the copied frame use the same drawing as the source
      :type instance_drawing: boolean, (optional)
      :return: The newly copied frame
      :rtype: :class:`GreasePencilFrame`

   .. method:: move(from_frame_number, to_frame_number)

      Move a Grease Pencil frame

      :arg from_frame_number: Source Frame Number, The frame number of the source frame
      :type from_frame_number: int in [-1048574, 1048574]
      :arg to_frame_number: Target Frame Number, The frame number to move the frame to
      :type to_frame_number: int in [-1048574, 1048574]
      :return: The moved frame
      :rtype: :class:`GreasePencilFrame`

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

   * :class:`GreasePencilLayer.frames`

