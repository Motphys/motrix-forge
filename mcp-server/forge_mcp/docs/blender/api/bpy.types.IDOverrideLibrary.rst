IDOverrideLibrary(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: IDOverrideLibrary(bpy_struct)

   Struct gathering all data needed by overridden linked IDs

   .. data:: hierarchy_root

      Library override ID used as root of the override hierarchy this ID is a member of

      :type: :class:`ID`, (readonly)

   .. attribute:: is_in_hierarchy

      Whether this library override is defined as part of a library hierarchy, or as a single, isolated and autonomous override

      :type: boolean, default True

   .. attribute:: is_system_override

      Whether this library override exists only for the override hierarchy, or if it is actually editable by the user

      :type: boolean, default False

   .. data:: properties

      List of overridden properties

      :type: :class:`IDOverrideLibraryProperties` :class:`bpy_prop_collection` of :class:`IDOverrideLibraryProperty`, (readonly)

   .. data:: reference

      Linked ID used as reference by this override

      :type: :class:`ID`, (readonly)

   .. method:: operations_update()

      Update the library override operations based on the differences between this override ID and its reference


   .. method:: reset(*, do_hierarchy=True, set_system_override=False)

      Reset this override to match again its linked reference ID

      :arg do_hierarchy: Also reset all the dependencies of this override to match their reference linked IDs
      :type do_hierarchy: boolean, (optional)
      :arg set_system_override: Reset all user-editable overrides as (non-editable) system overrides
      :type set_system_override: boolean, (optional)

   .. method:: destroy(*, do_hierarchy=True)

      Delete this override ID and remap its usages to its linked reference ID instead

      :arg do_hierarchy: Also delete all the dependencies of this override and remap their usages to their reference linked IDs
      :type do_hierarchy: boolean, (optional)

   .. method:: resync(scene, *, view_layer=None, residual_storage=None, do_hierarchy_enforce=False, do_whole_hierarchy=False)

      Resync the data-block and its sub-hierarchy, or the whole hierarchy if requested

      :arg scene: The scene to operate in (for contextual things like keeping active object active, ensuring all overridden objects remain instantiated, etc.)
      :type scene: :class:`Scene`, (never None)
      :arg view_layer: The view layer to operate in (same usage as the ``scene`` data, in case it is not provided the scene's collection will be used instead)
      :type view_layer: :class:`ViewLayer`, (optional)
      :arg residual_storage: Collection where to store objects that are instantiated in any other collection anymore (garbage collection, will be created if needed and none is provided)
      :type residual_storage: :class:`Collection`, (optional)
      :arg do_hierarchy_enforce: Enforce restoring the dependency hierarchy between data-blocks to match the one from the reference linked hierarchy (WARNING: if some ID pointers have been purposedly overridden, these will be reset to their default value)
      :type do_hierarchy_enforce: boolean, (optional)
      :arg do_whole_hierarchy: Resync the whole hierarchy this data-block belongs to, not only its own sub-hierarchy
      :type do_whole_hierarchy: boolean, (optional)
      :return: Success, Whether the resync process was successful or not
      :rtype: boolean

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

   * :class:`ID.override_library`

