XrActionMaps(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: XrActionMaps(bpy_struct)

   Collection of XR action maps

   .. classmethod:: new(xr_session_state, name, replace_existing)

      new

      :arg xr_session_state: XR Session State
      :type xr_session_state: :class:`XrSessionState`, (never None)
      :arg name: Name
      :type name: string, (never None)
      :arg replace_existing: Replace Existing, Replace any existing actionmap with the same name
      :type replace_existing: boolean
      :return: Action Map, Added action map
      :rtype: :class:`XrActionMap`

   .. classmethod:: new_from_actionmap(xr_session_state, actionmap)

      new_from_actionmap

      :arg xr_session_state: XR Session State
      :type xr_session_state: :class:`XrSessionState`, (never None)
      :arg actionmap: Action Map, Action map to use as a reference
      :type actionmap: :class:`XrActionMap`, (never None)
      :return: Action Map, Added action map
      :rtype: :class:`XrActionMap`

   .. classmethod:: remove(xr_session_state, actionmap)

      remove

      :arg xr_session_state: XR Session State
      :type xr_session_state: :class:`XrSessionState`, (never None)
      :arg actionmap: Action Map, Removed action map
      :type actionmap: :class:`XrActionMap`, (never None)

   .. classmethod:: find(xr_session_state, name)

      find

      :arg xr_session_state: XR Session State
      :type xr_session_state: :class:`XrSessionState`, (never None)
      :arg name: Name
      :type name: string, (never None)
      :return: Action Map, The action map with the given name
      :rtype: :class:`XrActionMap`

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

   * :class:`XrSessionState.actionmaps`

