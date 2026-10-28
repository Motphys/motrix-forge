UserAssetLibrary(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: UserAssetLibrary(bpy_struct)

   Settings to define a reusable library for Asset Browsers to use

   .. attribute:: import_method

      Determine how the asset will be imported, unless overridden by the Asset Browser

      * ``LINK``
        Link -- Import the assets as linked data-block.
      * ``APPEND``
        Append -- Import the assets as copied data-block, with no link to the original asset data-block.
      * ``APPEND_REUSE``
        Append (Reuse Data) -- Import the assets as copied data-block while avoiding multiple copies of nested, typically heavy data. For example the textures of a material asset, or the mesh of an object asset, don't have to be copied every time this asset is imported. The instances of the asset share the data instead..

      :type: enum in [``'LINK'``, ``'APPEND'``, ``'APPEND_REUSE'``], default ``'APPEND_REUSE'``

   .. attribute:: name

      Identifier (not necessarily unique) for the asset library

      :type: string, default "", (never None)

   .. attribute:: path

      Path to a directory with .blend files to use as an asset library

      :type: string, default "", (never None)

   .. attribute:: use_relative_path

      Use relative path when linking assets from this asset library

      :type: boolean, default True

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

   * :class:`AssetLibraryCollection.new`
   * :class:`AssetLibraryCollection.remove`
   * :class:`PreferencesFilePaths.asset_libraries`

