BlendDataLibraries(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataLibraries(bpy_struct)

   Collection of libraries

   .. method:: tag(value)

      tag

      :arg value: Value
      :type value: boolean

   .. method:: remove(library, *, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a library from the current blendfile

      :arg library: Library to remove
      :type library: :class:`Library`, (never None)
      :arg do_unlink: Unlink all usages of this library before deleting it
      :type do_unlink: boolean, (optional)
      :arg do_id_user: Decrement user counter of all datablocks used by this library
      :type do_id_user: boolean, (optional)
      :arg do_ui_user: Make sure interface does not reference this library
      :type do_ui_user: boolean, (optional)

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


   .. method:: load(filepath, link=False, relative=False, assets_only=False, create_liboverrides=False, reuse_liboverrides=False, create_liboverrides_runtime=False)
   
      Returns a context manager which exposes 2 library objects on entering.
      Each object has attributes matching bpy.data which are lists of strings to be linked.
   
      :arg filepath: The path to a blend file.
      :type filepath: str | bytes
      :arg link: When False reference to the original file is lost.
      :type link: bool
      :arg relative: When True the path is stored relative to the open blend file.
      :type relative: bool
      :arg assets_only: If True, only list data-blocks marked as assets.
      :type assets_only: bool
      :arg create_liboverrides: If True and ``link`` is True, liboverrides will
         be created for linked data.
      :type create_liboverrides: bool
      :arg reuse_liboverrides: If True and ``create_liboverride`` is True,
         search for existing liboverride first.
      :type reuse_liboverrides: bool
      :arg create_liboverrides_runtime: If True and ``create_liboverride`` is True,
         create (or search for existing) runtime liboverride.
      :type create_liboverrides_runtime: bool


      .. literalinclude:: ..\examples\bpy.types.BlendDataLibraries.load.py


   .. method:: write(filepath, datablocks, path_remap=False, fake_user=False, compress=False)
   
      Write data-blocks into a blend file.
   
      .. note::
   
         Indirectly referenced data-blocks will be expanded and written too.
   
      :arg filepath: The path to write the blend-file.
      :type filepath: str | bytes
      :arg datablocks: set of data-blocks.
      :type datablocks: set[:class:`bpy.types.ID`]
      :arg path_remap: Optionally remap paths when writing the file:
   
         - ``NONE`` No path manipulation (default).
         - ``RELATIVE`` Remap paths that are already relative to the new location.
         - ``RELATIVE_ALL`` Remap all paths to be relative to the new location.
         - ``ABSOLUTE`` Make all paths absolute on writing.
   
      :type path_remap: str
      :arg fake_user: When True, data-blocks will be written with fake-user flag enabled.
      :type fake_user: bool
      :arg compress: When True, write a compressed blend file.
      :type compress: bool


      .. literalinclude:: ..\examples\bpy.types.BlendDataLibraries.write.py


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

   * :class:`BlendData.libraries`

