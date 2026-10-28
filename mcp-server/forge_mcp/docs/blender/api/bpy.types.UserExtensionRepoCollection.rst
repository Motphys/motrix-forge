UserExtensionRepoCollection(bpy_struct)
=======================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserExtensionRepoCollection(bpy_struct)

   Collection of user extension repositories

   .. classmethod:: new(*, name="", module="", custom_directory="", remote_url="", source='USER')

      Add a new repository

      :arg name: Name
      :type name: string, (optional, never None)
      :arg module: Module
      :type module: string, (optional, never None)
      :arg custom_directory: Custom Directory
      :type custom_directory: string, (optional, never None)
      :arg remote_url: Remote URL
      :type remote_url: string, (optional, never None)
      :arg source: Source, How the repository is managed

         * ``USER``
           User -- Repository managed by the user, stored in user directories.
         * ``SYSTEM``
           System -- Read-only repository provided by the system.
      :type source: enum in [``'USER'``, ``'SYSTEM'``], (optional)
      :return: Newly added repository
      :rtype: :class:`UserExtensionRepo`

   .. classmethod:: remove(repo)

      Remove repos

      :arg repo: Repository to remove
      :type repo: :class:`UserExtensionRepo`, (never None)

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

   * :class:`PreferencesExtensions.repos`

