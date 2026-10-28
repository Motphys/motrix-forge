BlendImportContext(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendImportContext(bpy_struct)

   Contextual data for a blendfile library/linked-data related operation. Currently only exposed as read-only data for the pre/post blendimport handlers

   .. data:: import_items

      :type: :class:`BlendImportContextItems` :class:`bpy_prop_collection` of :class:`BlendImportContextItem`, (readonly)

   .. data:: options

      Options for this blendfile import operation

      * ``LINK``
        Only link data, instead of appending it.
      * ``MAKE_PATHS_RELATIVE``
        Make paths of used library blendfiles relative to current blendfile.
      * ``USE_PLACEHOLDERS``
        Generate a placeholder (empty ID) if not found in any library files.
      * ``FORCE_INDIRECT``
        Force loaded ID to be tagged as indirectly linked (used in reload context only).
      * ``APPEND_SET_FAKEUSER``
        Set fake user on appended IDs.
      * ``APPEND_RECURSIVE``
        Append (make local) also indirect dependencies of appended IDs coming from other libraries. NOTE: All IDs (including indirectly linked ones) coming from the same initial library are always made local.
      * ``APPEND_LOCAL_ID_REUSE``
        Try to re-use previously appended matching IDs when appending them again, instead of creating local duplicates.
      * ``APPEND_ASSET_DATA_CLEAR``
        Clear the asset data on append (it is always kept for linked data).
      * ``SELECT_OBJECTS``
        Automatically select imported objects.
      * ``USE_ACTIVE_COLLECTION``
        Use the active Collection of the current View Layer to instantiate imported collections and objects.
      * ``OBDATA_INSTANCE``
        Instantiate object data IDs (i.e. create objects for them if needed).
      * ``COLLECTION_INSTANCE``
        Instantiate collections as empties, instead of linking them into the current view layer.

      :type: enum set in {``'LINK'``, ``'MAKE_PATHS_RELATIVE'``, ``'USE_PLACEHOLDERS'``, ``'FORCE_INDIRECT'``, ``'APPEND_SET_FAKEUSER'``, ``'APPEND_RECURSIVE'``, ``'APPEND_LOCAL_ID_REUSE'``, ``'APPEND_ASSET_DATA_CLEAR'``, ``'SELECT_OBJECTS'``, ``'USE_ACTIVE_COLLECTION'``, ``'OBDATA_INSTANCE'``, ``'COLLECTION_INSTANCE'``}, default {``'LINK'``}, (readonly)

   .. data:: process_stage

      Current stage of the import process

      * ``INIT``
        Blendfile import context has been initialized and filled with a list of items to import, no data has been linked or appended yet.
      * ``DONE``
        All data has been imported and is available in the list of \`\`import_items\`\`.

      :type: enum in [``'INIT'``, ``'DONE'``], default ``'INIT'``, (readonly)

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

