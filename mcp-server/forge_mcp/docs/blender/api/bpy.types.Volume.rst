Volume(ID)
==========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Volume(ID)

   Volume data-block for 3D volume grids

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. data:: display

      Volume display settings for 3D viewport

      :type: :class:`VolumeDisplay`, (readonly)

   .. attribute:: filepath

      Volume file used by this Volume data-block

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: frame_duration

      Number of frames of the sequence to use

      :type: int in [0, 1048574], default 0

   .. attribute:: frame_offset

      Offset the number of the frame to use in the animation

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      Global starting frame of the sequence, assuming first has a #1

      :type: int in [-1048574, 1048574], default 1

   .. data:: grids

      3D volume grids

      :type: :class:`VolumeGrids` :class:`bpy_prop_collection` of :class:`VolumeGrid`, (readonly)

   .. attribute:: is_sequence

      Whether the cache is separated in a series of files

      :type: boolean, default False

   .. data:: materials

      :type: :class:`IDMaterials` :class:`bpy_prop_collection` of :class:`Material`, (readonly)

   .. data:: packed_file

      :type: :class:`PackedFile`, (readonly)

   .. data:: render

      Volume render settings for 3D viewport

      :type: :class:`VolumeRender`, (readonly)

   .. attribute:: sequence_mode

      Sequence playback mode

      * ``CLIP``
        Clip -- Hide frames outside the specified frame range.
      * ``EXTEND``
        Extend -- Repeat the start frame before, and the end frame after the frame range.
      * ``REPEAT``
        Repeat -- Cycle the frames in the sequence.
      * ``PING_PONG``
        Ping-Pong -- Repeat the frames, reversing the playback direction every other cycle.

      :type: enum in [``'CLIP'``, ``'EXTEND'``, ``'REPEAT'``, ``'PING_PONG'``], default ``'CLIP'``

   .. attribute:: velocity_grid

      Name of the velocity field, or the base name if the velocity is split into multiple grids

      :type: string, default "", (never None)

   .. attribute:: velocity_scale

      Factor to control the amount of motion blur

      :type: float in [0, inf], default 1.0

   .. attribute:: velocity_unit

      Define how the velocity vectors are interpreted with regard to time, 'frame' means the delta time is 1 frame, 'second' means the delta time is 1 / FPS

      :type: enum in :ref:`rna_enum_velocity_unit_items`, default ``'FRAME'``

   .. data:: velocity_x_grid

      Name of the grid for the X axis component of the velocity field if it was split into multiple grids

      :type: string, default "", (readonly, never None)

   .. data:: velocity_y_grid

      Name of the grid for the Y axis component of the velocity field if it was split into multiple grids

      :type: string, default "", (readonly, never None)

   .. data:: velocity_z_grid

      Name of the grid for the Z axis component of the velocity field if it was split into multiple grids

      :type: string, default "", (readonly, never None)

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

   * :mod:`bpy.context.volume`
   * :class:`BlendData.volumes`
   * :class:`BlendDataVolumes.new`
   * :class:`BlendDataVolumes.remove`

