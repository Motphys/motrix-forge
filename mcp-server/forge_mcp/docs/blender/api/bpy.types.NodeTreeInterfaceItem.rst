NodeTreeInterfaceItem(bpy_struct)
=================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`NodeTreeInterfacePanel`, :class:`NodeTreeInterfaceSocket`

.. class:: NodeTreeInterfaceItem(bpy_struct)

   Item in a node tree interface

   .. data:: index

      Global index of the item among all items in the interface

      :type: int in [-1, inf], default 0, (readonly)

   .. data:: item_type

      Type of interface item

      :type: enum in :ref:`rna_enum_node_tree_interface_item_type_items`, default ``'PANEL'``, (readonly)

   .. data:: parent

      Panel that contains the item

      :type: :class:`NodeTreeInterfacePanel`, (readonly)

   .. data:: position

      Position of the item in its parent panel

      :type: int in [-1, inf], default 0, (readonly)

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

   * :class:`NodeTreeInterface.active`
   * :class:`NodeTreeInterface.copy`
   * :class:`NodeTreeInterface.copy`
   * :class:`NodeTreeInterface.items_tree`
   * :class:`NodeTreeInterface.move`
   * :class:`NodeTreeInterface.move_to_parent`
   * :class:`NodeTreeInterface.remove`
   * :class:`NodeTreeInterfacePanel.interface_items`

