GreasePencilv3LayerGroup(bpy_struct)
====================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GreasePencilv3LayerGroup(bpy_struct)

   Collection of Grease Pencil layers

   .. attribute:: active

      Active Grease Pencil layer group

      :type: :class:`GreasePencilLayerGroup`

   .. method:: new(name, *, parent_group=None)

      Add a new Grease Pencil layer group

      :arg name: Name, Name of the layer group
      :type name: string, (never None)
      :arg parent_group: The parent layer group the new group will be created in (use None for the main stack)
      :type parent_group: :class:`GreasePencilLayerGroup`, (optional)
      :return: The newly created layer group
      :rtype: :class:`GreasePencilLayerGroup`

   .. method:: remove(layer_group, *, keep_children=False)

      Remove a new Grease Pencil layer group

      :arg layer_group: The layer group to remove
      :type layer_group: :class:`GreasePencilLayerGroup`, (never None)
      :arg keep_children: Keep the children nodes of the group and only delete the group itself
      :type keep_children: boolean, (optional)

   .. method:: move(layer_group, type)

      Move a layer group in the parent layer group or main stack

      :arg layer_group: The layer group to move
      :type layer_group: :class:`GreasePencilLayerGroup`, (never None)
      :arg type: Direction of movement
      :type type: enum in [``'DOWN'``, ``'UP'``]

   .. method:: move_top(layer_group)

      Move a layer group to the top of the parent layer group or main stack

      :arg layer_group: The layer group to move
      :type layer_group: :class:`GreasePencilLayerGroup`, (never None)

   .. method:: move_bottom(layer_group)

      Move a layer group to the bottom of the parent layer group or main stack

      :arg layer_group: The layer group to move
      :type layer_group: :class:`GreasePencilLayerGroup`, (never None)

   .. method:: move_to_layer_group(layer_group, parent_group)

      Move a layer group into a parent layer group

      :arg layer_group: The layer group to move
      :type layer_group: :class:`GreasePencilLayerGroup`, (never None)
      :arg parent_group: The parent layer group the layer group will be moved into (use None for the main stack)
      :type parent_group: :class:`GreasePencilLayerGroup`

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

   * :class:`GreasePencilv3.layer_groups`

