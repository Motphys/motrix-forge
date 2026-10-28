KeyMapItems(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyMapItems(bpy_struct)

   Collection of keymap items

   .. method:: new(idname, type, value, *, any=False, shift=0, ctrl=0, alt=0, oskey=0, hyper=0, key_modifier='NONE', direction='ANY', repeat=False, head=False)

      new

      :arg idname: Operator Identifier
      :type idname: string, (never None)
      :arg type: Type
      :type type: enum in :ref:`rna_enum_event_type_items`
      :arg value: Value
      :type value: enum in :ref:`rna_enum_event_value_items`
      :arg any: Any
      :type any: boolean, (optional)
      :arg shift: Shift
      :type shift: int in [-1, 1], (optional)
      :arg ctrl: Ctrl
      :type ctrl: int in [-1, 1], (optional)
      :arg alt: Alt
      :type alt: int in [-1, 1], (optional)
      :arg oskey: OS Key
      :type oskey: int in [-1, 1], (optional)
      :arg hyper: Hyper
      :type hyper: int in [-1, 1], (optional)
      :arg key_modifier: Key Modifier
      :type key_modifier: enum in :ref:`rna_enum_event_type_items`, (optional)
      :arg direction: Direction
      :type direction: enum in :ref:`rna_enum_event_direction_items`, (optional)
      :arg repeat: Repeat, When set, accept key-repeat events
      :type repeat: boolean, (optional)
      :arg head: At Head, Force item to be added at start (not end) of key map so that it doesn't get blocked by an existing key map item
      :type head: boolean, (optional)
      :return: Item, Added key map item
      :rtype: :class:`KeyMapItem`

   .. method:: new_modal(propvalue, type, value, *, any=False, shift=0, ctrl=0, alt=0, oskey=0, hyper=0, key_modifier='NONE', direction='ANY', repeat=False)

      new_modal

      :arg propvalue: Property Value
      :type propvalue: string, (never None)
      :arg type: Type
      :type type: enum in :ref:`rna_enum_event_type_items`
      :arg value: Value
      :type value: enum in :ref:`rna_enum_event_value_items`
      :arg any: Any
      :type any: boolean, (optional)
      :arg shift: Shift
      :type shift: int in [-1, 1], (optional)
      :arg ctrl: Ctrl
      :type ctrl: int in [-1, 1], (optional)
      :arg alt: Alt
      :type alt: int in [-1, 1], (optional)
      :arg oskey: OS Key
      :type oskey: int in [-1, 1], (optional)
      :arg hyper: Hyper
      :type hyper: int in [-1, 1], (optional)
      :arg key_modifier: Key Modifier
      :type key_modifier: enum in :ref:`rna_enum_event_type_items`, (optional)
      :arg direction: Direction
      :type direction: enum in :ref:`rna_enum_event_direction_items`, (optional)
      :arg repeat: Repeat, When set, accept key-repeat events
      :type repeat: boolean, (optional)
      :return: Item, Added key map item
      :rtype: :class:`KeyMapItem`

   .. method:: new_from_item(item, *, head=False)

      new_from_item

      :arg item: Item, Item to use as a reference
      :type item: :class:`KeyMapItem`, (never None)
      :arg head: At Head
      :type head: boolean, (optional)
      :return: Item, Added key map item
      :rtype: :class:`KeyMapItem`

   .. method:: remove(item)

      remove

      :arg item: Item
      :type item: :class:`KeyMapItem`, (never None)

   .. method:: from_id(id)

      from_id

      :arg id: id, ID of the item
      :type id: int in [-inf, inf]
      :return: Item
      :rtype: :class:`KeyMapItem`

   .. method:: find_from_operator(idname, *, properties=None, include={'ACTIONZONE', 'KEYBOARD', 'MOUSE', 'NDOF'}, exclude={})

      find_from_operator

      :arg idname: Operator Identifier
      :type idname: string, (never None)
      :type properties: :class:`OperatorProperties`, (optional)
      :arg include: Include
      :type include: enum set in :ref:`rna_enum_event_type_mask_items`, (optional)
      :arg exclude: Exclude
      :type exclude: enum set in :ref:`rna_enum_event_type_mask_items`, (optional)
      :rtype: :class:`KeyMapItem`

   .. method:: find_match(keymap, item)

      find_match

      :arg keymap: The matching keymap
      :type keymap: :class:`KeyMap`
      :arg item: The matching keymap item
      :type item: :class:`KeyMapItem`
      :return: The keymap item from this keymap which matches the keymap item from the arguments passed in
      :rtype: :class:`KeyMapItem`

   .. method:: match_event(event)

      match_event

      :type event: :class:`Event`
      :rtype: :class:`KeyMapItem`

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

   * :class:`KeyMap.keymap_items`

