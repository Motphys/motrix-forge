DriverTarget(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DriverTarget(bpy_struct)

   Source of input values for driver variables

   .. attribute:: bone_target

      Name of PoseBone to use as target

      :type: string, default "", (never None)

   .. attribute:: context_property

      Type of a context-dependent data-block to access property from

      * ``ACTIVE_SCENE``
        Active Scene -- Currently evaluating scene.
      * ``ACTIVE_VIEW_LAYER``
        Active View Layer -- Currently evaluating view layer.

      :type: enum in [``'ACTIVE_SCENE'``, ``'ACTIVE_VIEW_LAYER'``], default ``'ACTIVE_SCENE'``

   .. attribute:: data_path

      RNA Path (from ID-block) to property used

      :type: string, default "", (never None)

   .. attribute:: fallback_value

      The value to use if the data path can't be resolved

      :type: float in [-inf, inf], default 0.0

   .. attribute:: id

      ID-block that the specific property used can be found from (id_type property must be set first)

      :type: :class:`ID`

   .. attribute:: id_type

      Type of ID-block that can be used

      :type: enum in :ref:`rna_enum_id_type_items`, default ``'OBJECT'``

   .. data:: is_fallback_used

      Indicates that the most recent variable evaluation used the fallback value

      :type: boolean, default False, (readonly)

   .. attribute:: rotation_mode

      Mode for calculating rotation channel values

      :type: enum in :ref:`rna_enum_driver_target_rotation_mode_items`, default ``'AUTO'``

   .. attribute:: transform_space

      Space in which transforms are used

      * ``WORLD_SPACE``
        World Space -- Transforms include effects of parenting/restpose and constraints.
      * ``TRANSFORM_SPACE``
        Transform Space -- Transforms don't include parenting/restpose or constraints.
      * ``LOCAL_SPACE``
        Local Space -- Transforms include effects of constraints but not parenting/restpose.

      :type: enum in [``'WORLD_SPACE'``, ``'TRANSFORM_SPACE'``, ``'LOCAL_SPACE'``], default ``'WORLD_SPACE'``

   .. attribute:: transform_type

      Driver variable type

      :type: enum in [``'LOC_X'``, ``'LOC_Y'``, ``'LOC_Z'``, ``'ROT_X'``, ``'ROT_Y'``, ``'ROT_Z'``, ``'ROT_W'``, ``'SCALE_X'``, ``'SCALE_Y'``, ``'SCALE_Z'``, ``'SCALE_AVG'``], default ``'LOC_X'``

   .. attribute:: use_fallback_value

      Use the fallback value if the data path can't be resolved, instead of failing to evaluate the driver

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

   * :class:`DriverVariable.targets`

