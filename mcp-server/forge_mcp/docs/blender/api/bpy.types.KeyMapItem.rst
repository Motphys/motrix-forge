KeyMapItem(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyMapItem(bpy_struct)

   Item in a Key Map

   .. attribute:: active

      Activate or deactivate item

      :type: boolean, default False

   .. attribute:: alt

      Alt key pressed, -1 for any state

      :type: int in [-1, 1], default 0

   .. attribute:: alt_ui

      Alt key pressed

      :type: boolean, default False

   .. attribute:: any

      Any modifier keys pressed

      :type: boolean, default False

   .. attribute:: ctrl

      Control key pressed, -1 for any state

      :type: int in [-1, 1], default 0

   .. attribute:: ctrl_ui

      Control key pressed

      :type: boolean, default False

   .. attribute:: direction

      The direction (only applies to drag events)

      :type: enum in :ref:`rna_enum_event_direction_items`, default ``'ANY'``

   .. attribute:: hyper

      Hyper key pressed, -1 for any state

      :type: int in [-1, 1], default 0

   .. attribute:: hyper_ui

      Hyper key pressed. An additional modifier which can be configured on Linux, typically replacing CapsLock

      :type: boolean, default False

   .. data:: id

      ID of the item

      :type: int in [-32768, 32767], default 0, (readonly)

   .. attribute:: idname

      Identifier of operator to call on input event

      :type: string, default "", (never None)

   .. data:: is_user_defined

      Is this keymap item user defined (doesn't just replace a builtin item)

      :type: boolean, default False, (readonly)

   .. data:: is_user_modified

      Is this keymap item modified by the user

      :type: boolean, default False, (readonly)

   .. attribute:: key_modifier

      Regular key pressed as a modifier

      :type: enum in :ref:`rna_enum_event_type_items`, default ``'NONE'``

   .. attribute:: map_type

      Type of event mapping

      :type: enum in [``'KEYBOARD'``, ``'MOUSE'``, ``'NDOF'``, ``'TEXTINPUT'``, ``'TIMER'``], default ``'KEYBOARD'``

   .. data:: name

      Name of operator (translated) to call on input event

      :type: string, default "", (readonly, never None)

   .. attribute:: oskey

      Operating system key pressed, -1 for any state

      :type: int in [-1, 1], default 0

   .. attribute:: oskey_ui

      Operating system key pressed

      :type: boolean, default False

   .. data:: properties

      Properties to set when the operator is called

      :type: :class:`OperatorProperties`, (readonly)

   .. attribute:: propvalue

      The value this event translates to in a modal keymap

      :type: enum in :ref:`rna_enum_keymap_propvalue_items`, default ``'NONE'``

   .. attribute:: repeat

      Active on key-repeat events (when a key is held)

      :type: boolean, default False

   .. attribute:: shift

      Shift key pressed, -1 for any state

      :type: int in [-1, 1], default 0

   .. attribute:: shift_ui

      Shift key pressed

      :type: boolean, default False

   .. attribute:: show_expanded

      Show key map event and property details in the user interface

      :type: boolean, default False

   .. attribute:: type

      Type of event

      :type: enum in :ref:`rna_enum_event_type_items`, default ``'NONE'``

   .. attribute:: value

      :type: enum in :ref:`rna_enum_event_value_items`, default ``'NOTHING'``

   .. method:: compare(item)

      compare

      :arg item: Item
      :type item: :class:`KeyMapItem`
      :return: Comparison result
      :rtype: boolean

   .. method:: to_string(*, compact=False)

      to_string

      :arg compact: Compact
      :type compact: boolean, (optional)
      :return: result
      :rtype: string, (never None)

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

   * :class:`KeyConfigurations.find_item_from_operator`
   * :class:`KeyMap.keymap_items`
   * :class:`KeyMap.restore_item_to_default`
   * :class:`KeyMapItem.compare`
   * :class:`KeyMapItems.find_from_operator`
   * :class:`KeyMapItems.find_match`
   * :class:`KeyMapItems.find_match`
   * :class:`KeyMapItems.from_id`
   * :class:`KeyMapItems.match_event`
   * :class:`KeyMapItems.new`
   * :class:`KeyMapItems.new_from_item`
   * :class:`KeyMapItems.new_from_item`
   * :class:`KeyMapItems.new_modal`
   * :class:`KeyMapItems.remove`
   * :class:`UILayout.template_event_from_keymap_item`
   * :class:`UILayout.template_keymap_item_properties`

