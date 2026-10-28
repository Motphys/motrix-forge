UserExtensionRepo(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserExtensionRepo(bpy_struct)

   Settings to define an extension repository

   .. attribute:: access_token

      Personal access token, may be required by some repositories

      :type: string, default "", (never None)

   .. attribute:: custom_directory

      The local directory containing extensions

      :type: string, default "", (never None)

   .. data:: directory

      The local directory containing extensions

      :type: string, default "", (readonly, never None)

   .. attribute:: enabled

      Enable the repository

      :type: boolean, default False

   .. attribute:: module

      Unique module identifier

      :type: string, default "", (never None)

   .. attribute:: name

      Unique repository name

      :type: string, default "", (never None)

   .. attribute:: remote_url

      Remote URL to the extension repository, the file-system may be referenced using the file URI scheme: "file://"

      :type: string, default "", (never None)

   .. attribute:: source

      Select if the repository is in a user managed or system provided directory

      * ``USER``
        User -- Repository managed by the user, stored in user directories.
      * ``SYSTEM``
        System -- Read-only repository provided by the system.

      :type: enum in [``'USER'``, ``'SYSTEM'``], default ``'USER'``

   .. attribute:: use_access_token

      Repository requires an access token

      :type: boolean, default False

   .. attribute:: use_cache

      Downloaded package files are deleted after installation

      :type: boolean, default False

   .. attribute:: use_custom_directory

      Manually set the path for extensions to be stored. When disabled a user's extensions directory is created.

      :type: boolean, default False

   .. attribute:: use_remote_url

      Synchronize the repository with a remote URL

      :type: boolean, default False

   .. attribute:: use_sync_on_startup

      Allow Blender to check for updates upon launch

      :type: boolean, default False

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
   * :class:`UserExtensionRepoCollection.new`
   * :class:`UserExtensionRepoCollection.remove`

