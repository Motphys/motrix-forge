GreasePencilv3Layers(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GreasePencilv3Layers(bpy_struct)

   Collection of Grease Pencil layers

   .. attribute:: active

      Active Grease Pencil layer

      :type: :class:`GreasePencilLayer`

   .. method:: new(name, *, set_active=True, layer_group=None)

      Add a new Grease Pencil layer

      :arg name: Name, Name of the layer
      :type name: string, (never None)
      :arg set_active: Set Active, Set the newly created layer as the active layer
      :type set_active: boolean, (optional)
      :arg layer_group: The layer group the new layer will be created in (use None for the main stack)
      :type layer_group: :class:`GreasePencilLayerGroup`, (optional)
      :return: The newly created layer
      :rtype: :class:`GreasePencilLayer`

   .. method:: remove(layer)

      Remove a Grease Pencil layer

      :arg layer: The layer to remove
      :type layer: :class:`GreasePencilLayer`, (never None)

   .. method:: move(layer, type)

      Move a Grease Pencil layer in the layer group or main stack

      :arg layer: The layer to move
      :type layer: :class:`GreasePencilLayer`, (never None)
      :arg type: Direction of movement
      :type type: enum in [``'DOWN'``, ``'UP'``]

   .. method:: move_top(layer)

      Move a Grease Pencil layer to the top of the layer group or main stack

      :arg layer: The layer to move
      :type layer: :class:`GreasePencilLayer`, (never None)

   .. method:: move_bottom(layer)

      Move a Grease Pencil layer to the bottom of the layer group or main stack

      :arg layer: The layer to move
      :type layer: :class:`GreasePencilLayer`, (never None)

   .. method:: move_to_layer_group(layer, layer_group)

      Move a Grease Pencil layer into a layer group

      :arg layer: The layer to move
      :type layer: :class:`GreasePencilLayer`, (never None)
      :arg layer_group: The layer group the layer will be moved into (use None for the main stack)
      :type layer_group: :class:`GreasePencilLayerGroup`

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

   * :class:`GreasePencilv3.layers`

