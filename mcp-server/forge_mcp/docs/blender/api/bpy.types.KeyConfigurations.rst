KeyConfigurations(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyConfigurations(bpy_struct)

   Collection of KeyConfigs

   .. attribute:: active

      Active key configuration (preset)

      :type: :class:`KeyConfig`

   .. data:: addon

      Key configuration that can be extended by add-ons, and is added to the active configuration when handling events

      :type: :class:`KeyConfig`, (readonly)

   .. data:: default

      Default builtin key configuration

      :type: :class:`KeyConfig`, (readonly)

   .. data:: user

      Final key configuration that combines keymaps from the active and add-on configurations, and can be edited by the user

      :type: :class:`KeyConfig`, (readonly)

   .. method:: new(name)

      new

      :arg name: Name
      :type name: string, (never None)
      :return: Key Configuration, Added key configuration
      :rtype: :class:`KeyConfig`

   .. method:: remove(keyconfig)

      remove

      :arg keyconfig: Key Configuration, Removed key configuration
      :type keyconfig: :class:`KeyConfig`, (never None)

   .. method:: find_item_from_operator(idname, *, context='INVOKE_DEFAULT', properties=None, include={'ACTIONZONE', 'KEYBOARD', 'MOUSE', 'NDOF'}, exclude={})

      find_item_from_operator

      :arg idname: Operator Identifier
      :type idname: string, (never None)
      :arg context: context
      :type context: enum in :ref:`rna_enum_operator_context_items`, (optional)
      :type properties: :class:`OperatorProperties`, (optional)
      :arg include: Include
      :type include: enum set in :ref:`rna_enum_event_type_mask_items`, (optional)
      :arg exclude: Exclude
      :type exclude: enum set in :ref:`rna_enum_event_type_mask_items`, (optional)
      :return:
         `keymap`, :class:`KeyMap`

         `item`, :class:`KeyMapItem`

      :rtype: (:class:`KeyMap`, :class:`KeyMapItem`)

   .. method:: update(*, keep_properties=False)

      update

      :arg keep_properties: Keep Properties, Operator properties are kept to allow the operators to be registered again in the future
      :type keep_properties: boolean, (optional)

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

   * :class:`WindowManager.keyconfigs`

