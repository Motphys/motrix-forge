CompositorNodeOutputFileLayerSlots(bpy_struct)
==============================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CompositorNodeOutputFileLayerSlots(bpy_struct)

   Collection of File Output node slots

   .. method:: new(name)

      Add a file slot to this node

      :arg name: Name
      :type name: string, (never None)
      :return: New socket
      :rtype: :class:`NodeSocket`

   .. method:: remove(socket)

      Remove a file slot from this node

      :arg socket: The socket to remove
      :type socket: :class:`NodeSocket`

   .. method:: clear()

      Remove all file slots from this node


   .. method:: move(from_index, to_index)

      Move a file slot to another position

      :arg from_index: From Index, Index of the socket to move
      :type from_index: int in [0, inf]
      :arg to_index: To Index, Target index for the socket
      :type to_index: int in [0, inf]

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

   * :class:`CompositorNodeOutputFile.layer_slots`

