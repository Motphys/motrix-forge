KeyMaps(bpy_struct)
===================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyMaps(bpy_struct)

   Collection of keymaps

   .. method:: new(name, *, space_type='EMPTY', region_type='WINDOW', modal=False, tool=False)

      Ensure the keymap exists. This will return the one with the given name/space type/region type, or create a new one if it does not exist yet.

      :arg name: Name
      :type name: string, (never None)
      :arg space_type: Space Type
      :type space_type: enum in :ref:`rna_enum_space_type_items`, (optional)
      :arg region_type: Region Type
      :type region_type: enum in :ref:`rna_enum_region_type_items`, (optional)
      :arg modal: Modal, Keymap for modal operators
      :type modal: boolean, (optional)
      :arg tool: Tool, Keymap for active tools
      :type tool: boolean, (optional)
      :return: Key Map, Added key map
      :rtype: :class:`KeyMap`

   .. method:: remove(keymap)

      remove

      :arg keymap: Key Map, Removed key map
      :type keymap: :class:`KeyMap`, (never None)

   .. method:: clear()

      Remove all keymaps.


   .. method:: find(name, *, space_type='EMPTY', region_type='WINDOW')

      find

      :arg name: Name
      :type name: string, (never None)
      :arg space_type: Space Type
      :type space_type: enum in :ref:`rna_enum_space_type_items`, (optional)
      :arg region_type: Region Type
      :type region_type: enum in :ref:`rna_enum_region_type_items`, (optional)
      :return: Key Map, Corresponding key map
      :rtype: :class:`KeyMap`

   .. method:: find_match(keymap)

      find_match

      :arg keymap: Key Map, The key map for comparison
      :type keymap: :class:`KeyMap`
      :return: Key Map, Corresponding key map
      :rtype: :class:`KeyMap`

   .. method:: find_modal(name)

      find_modal

      :arg name: Operator Name
      :type name: string, (never None)
      :return: Key Map, Corresponding key map
      :rtype: :class:`KeyMap`

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

   * :class:`KeyConfig.keymaps`

