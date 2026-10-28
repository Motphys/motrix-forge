MeshCacheModifier(Modifier)
===========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: MeshCacheModifier(Modifier)

   Cache Mesh

   .. attribute:: cache_format

      :type: enum in [``'MDD'``, ``'PC2'``], default ``'MDD'``

   .. attribute:: deform_mode

      * ``OVERWRITE``
        Overwrite -- Replace vertex coordinates with cached values.
      * ``INTEGRATE``
        Integrate -- Integrate deformation from this modifier's input with the mesh-cache coordinates (useful for shape keys).

      :type: enum in [``'OVERWRITE'``, ``'INTEGRATE'``], default ``'OVERWRITE'``

   .. attribute:: eval_factor

      Evaluation time in seconds

      :type: float in [0, 1], default 0.0

   .. attribute:: eval_frame

      The frame to evaluate (starting at 0)

      :type: float in [0, 1.04857e+06], default 0.0

   .. attribute:: eval_time

      Evaluation time in seconds

      :type: float in [0, inf], default 0.0

   .. attribute:: factor

      Influence of the deformation

      :type: float in [0, 1], default 1.0

   .. attribute:: filepath

      Path to external displacements file

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: flip_axis

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: forward_axis

      :type: enum in :ref:`rna_enum_object_axis_items`, default ``'POS_Y'``

   .. attribute:: frame_scale

      Evaluation time in seconds

      :type: float in [0, 100], default 1.0

   .. attribute:: frame_start

      Add this to the start frame

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: interpolation

      :type: enum in [``'NONE'``, ``'LINEAR'``], default ``'LINEAR'``

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. attribute:: play_mode

      * ``SCENE``
        Scene -- Use the time from the scene.
      * ``CUSTOM``
        Custom -- Use the modifier's own time evaluation.

      :type: enum in [``'SCENE'``, ``'CUSTOM'``], default ``'SCENE'``

   .. attribute:: time_mode

      Method to control playback time

      * ``FRAME``
        Frame -- Control playback using a frame-number (ignoring time FPS and start frame from the file).
      * ``TIME``
        Time -- Control playback using time in seconds.
      * ``FACTOR``
        Factor -- Control playback using a value between 0 and 1.

      :type: enum in [``'FRAME'``, ``'TIME'``, ``'FACTOR'``], default ``'FRAME'``

   .. attribute:: up_axis

      :type: enum in :ref:`rna_enum_object_axis_items`, default ``'POS_Z'``

   .. attribute:: vertex_group

      Name of the Vertex Group which determines the influence of the modifier per point

      :type: string, default "", (never None)

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.is_active`
   * :class:`Modifier.use_pin_to_last`
   * :class:`Modifier.is_override_data`
   * :class:`Modifier.use_apply_on_spline`
   * :class:`Modifier.execution_time`
   * :class:`Modifier.persistent_uid`

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
   * :class:`Modifier.bl_rna_get_subclass`
   * :class:`Modifier.bl_rna_get_subclass_py`

