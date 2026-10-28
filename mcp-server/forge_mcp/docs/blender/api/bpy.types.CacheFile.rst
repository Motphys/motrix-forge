CacheFile(ID)
=============

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: CacheFile(ID)


   .. attribute:: active_index

      :type: int in [0, inf], default 0

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: filepath

      Path to external displacements file

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: forward_axis

      :type: enum in :ref:`rna_enum_object_axis_items`, default ``'POS_X'``

   .. attribute:: frame

      The time to use for looking up the data in the cache file, or to determine which file to use in a file sequence

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: frame_offset

      Subtracted from the current frame to use for looking up the data in the cache file, or to determine which file to use in a file sequence

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: is_sequence

      Whether the cache is separated in a series of files

      :type: boolean, default False

   .. data:: layers

      Layers of the cache

      :type: :class:`CacheFileLayers` :class:`bpy_prop_collection` of :class:`CacheFileLayer`, (readonly)

   .. data:: object_paths

      Paths of the objects inside the Alembic archive

      :type: :class:`CacheObjectPaths` :class:`bpy_prop_collection` of :class:`CacheObjectPath`, (readonly)

   .. attribute:: override_frame

      Whether to use a custom frame for looking up data in the cache file, instead of using the current scene frame

      :type: boolean, default False

   .. attribute:: prefetch_cache_size

      Memory usage limit in megabytes for the Cycles Procedural cache, if the data does not fit within the limit, rendering is aborted

      :type: int in [0, inf], default 4096

   .. attribute:: scale

      Value by which to enlarge or shrink the object with respect to the world's origin (only applicable through a Transform Cache constraint)

      :type: float in [0.0001, 1000], default 1.0

   .. attribute:: up_axis

      :type: enum in :ref:`rna_enum_object_axis_items`, default ``'POS_X'``

   .. attribute:: use_prefetch

      When enabled, the Cycles Procedural will preload animation data for faster updates

      :type: boolean, default False

   .. attribute:: use_render_procedural

      Display boxes in the viewport as placeholders for the objects, Cycles will use a procedural to load the objects during viewport rendering in experimental mode, other render engines will also receive a placeholder and should take care of loading the Alembic data themselves if possible

      :type: boolean, default False

   .. attribute:: velocity_name

      Name of the Alembic attribute used for generating motion blur data

      :type: string, default "", (never None)

   .. attribute:: velocity_unit

      Define how the velocity vectors are interpreted with regard to time, 'frame' means the delta time is 1 frame, 'second' means the delta time is 1 / FPS

      :type: enum in :ref:`rna_enum_velocity_unit_items`, default ``'FRAME'``

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
   * :class:`ID.name`
   * :class:`ID.name_full`
   * :class:`ID.id_type`
   * :class:`ID.session_uid`
   * :class:`ID.is_evaluated`
   * :class:`ID.original`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.use_extra_user`
   * :class:`ID.is_embedded_data`
   * :class:`ID.is_missing`
   * :class:`ID.is_runtime_data`
   * :class:`ID.is_editable`
   * :class:`ID.tag`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.library_weak_reference`
   * :class:`ID.asset_data`
   * :class:`ID.override_library`
   * :class:`ID.preview`

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
   * :class:`ID.rename`
   * :class:`ID.evaluated_get`
   * :class:`ID.copy`
   * :class:`ID.asset_mark`
   * :class:`ID.asset_clear`
   * :class:`ID.asset_generate_preview`
   * :class:`ID.override_create`
   * :class:`ID.override_hierarchy_create`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`
   * :class:`ID.preview_ensure`
   * :class:`ID.bl_rna_get_subclass`
   * :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :class:`BlendData.cache_files`
   * :class:`MeshSequenceCacheModifier.cache_file`
   * :class:`TransformCacheConstraint.cache_file`

