BlendDataMovieClips(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataMovieClips(bpy_struct)

   Collection of movie clips

   .. method:: tag(value)

      tag

      :arg value: Value
      :type value: boolean

   .. method:: remove(clip, *, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a movie clip from the current blendfile.

      :arg clip: Movie clip to remove
      :type clip: :class:`MovieClip`, (never None)
      :arg do_unlink: Unlink all usages of this movie clip before deleting it
      :type do_unlink: boolean, (optional)
      :arg do_id_user: Decrement user counter of all datablocks used by this movie clip
      :type do_id_user: boolean, (optional)
      :arg do_ui_user: Make sure interface does not reference this movie clip
      :type do_ui_user: boolean, (optional)

   .. method:: load(filepath, *, check_existing=False)

      Add a new movie clip to the main database from a file (while ``check_existing`` is disabled for consistency with other load functions, behavior with multiple movie-clips using the same file may incorrectly generate proxies)

      :arg filepath: path for the data-block
      :type filepath: string, (never None, blend relative ``//`` prefix supported)
      :arg check_existing: Using existing data-block if this file is already loaded
      :type check_existing: boolean, (optional)
      :return: New movie clip data-block
      :rtype: :class:`MovieClip`

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

   * :class:`BlendData.movieclips`

