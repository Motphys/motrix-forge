NodeTreeInterface(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NodeTreeInterface(bpy_struct)

   Declaration of sockets and ui panels of a node group

   .. attribute:: active

      Active item

      :type: :class:`NodeTreeInterfaceItem`

   .. attribute:: active_index

      Index of the active item

      :type: int in [0, inf], default 0

   .. data:: items_tree

      Items in the node interface

      :type: :class:`bpy_prop_collection` of :class:`NodeTreeInterfaceItem`, (readonly)

   .. method:: new_socket(name, *, description="", in_out='INPUT', socket_type='DEFAULT', parent=None)

      Add a new socket to the interface

      :arg name: Name, Name of the socket
      :type name: string, (never None)
      :arg description: Description, Description of the socket
      :type description: string, (optional, never None)
      :arg in_out: Input/Output Type, Create an input or output socket

         * ``INPUT``
           Input -- Generate a input node socket.
         * ``OUTPUT``
           Output -- Generate a output node socket.
      :type in_out: enum in [``'INPUT'``, ``'OUTPUT'``], (optional)
      :arg socket_type: Socket Type, Type of socket generated on nodes
      :type socket_type: enum in [``'DEFAULT'``], (optional)
      :arg parent: Parent, Panel to add the socket in
      :type parent: :class:`NodeTreeInterfacePanel`, (optional)
      :return: Socket, New socket
      :rtype: :class:`NodeTreeInterfaceSocket`

   .. method:: new_panel(name, *, description="", default_closed=False)

      Add a new panel to the interface

      :arg name: Name, Name of the new panel
      :type name: string, (never None)
      :arg description: Description, Description of the panel
      :type description: string, (optional, never None)
      :arg default_closed: Default Closed, Panel is closed by default on new nodes
      :type default_closed: boolean, (optional)
      :return: Panel, New panel
      :rtype: :class:`NodeTreeInterfacePanel`

   .. method:: copy(item)

      Add a copy of an item to the interface

      :arg item: Item, Item to copy
      :type item: :class:`NodeTreeInterfaceItem`, (never None)
      :return: Item Copy, Copy of the item
      :rtype: :class:`NodeTreeInterfaceItem`

   .. method:: remove(item, *, move_content_to_parent=True)

      Remove an item from the interface

      :arg item: Item, The item to remove
      :type item: :class:`NodeTreeInterfaceItem`, (never None)
      :arg move_content_to_parent: Move Content, If the item is a panel, move the contents to the parent instead of deleting it
      :type move_content_to_parent: boolean, (optional)

   .. method:: clear()

      Remove all items from the interface


   .. method:: move(item, to_position)

      Move an item to another position

      :arg item: Item, The item to move
      :type item: :class:`NodeTreeInterfaceItem`, (never None)
      :arg to_position: To Position, Target position for the item in its current panel
      :type to_position: int in [0, inf]

   .. method:: move_to_parent(item, parent, to_position)

      Move an item to a new panel and/or position.

      :arg item: Item, The item to move
      :type item: :class:`NodeTreeInterfaceItem`, (never None)
      :arg parent: Parent, New parent of the item
      :type parent: :class:`NodeTreeInterfacePanel`
      :arg to_position: To Position, Target position for the item in the new parent panel
      :type to_position: int in [0, inf]

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

   * :class:`NodeTree.interface`
   * :class:`UILayout.template_node_tree_interface`

