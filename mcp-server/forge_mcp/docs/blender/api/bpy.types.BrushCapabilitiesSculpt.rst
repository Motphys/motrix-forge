BrushCapabilitiesSculpt(bpy_struct)
===================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BrushCapabilitiesSculpt(bpy_struct)

   Read-only indications of which brush operations are supported by the current sculpt tool

   .. data:: has_accumulate

      :type: boolean, default False, (readonly)

   .. data:: has_auto_smooth

      :type: boolean, default False, (readonly)

   .. data:: has_color

      :type: boolean, default False, (readonly)

   .. data:: has_direction

      :type: boolean, default False, (readonly)

   .. data:: has_dyntopo

      :type: boolean, default False, (readonly)

   .. data:: has_gravity

      :type: boolean, default False, (readonly)

   .. data:: has_height

      :type: boolean, default False, (readonly)

   .. data:: has_jitter

      :type: boolean, default False, (readonly)

   .. data:: has_normal_weight

      :type: boolean, default False, (readonly)

   .. data:: has_persistence

      :type: boolean, default False, (readonly)

   .. data:: has_pinch_factor

      :type: boolean, default False, (readonly)

   .. data:: has_plane_depth

      :type: boolean, default False, (readonly)

   .. data:: has_plane_height

      :type: boolean, default False, (readonly)

   .. data:: has_plane_offset

      :type: boolean, default False, (readonly)

   .. data:: has_rake_factor

      :type: boolean, default False, (readonly)

   .. data:: has_random_texture_angle

      :type: boolean, default False, (readonly)

   .. data:: has_sculpt_plane

      :type: boolean, default False, (readonly)

   .. data:: has_secondary_color

      :type: boolean, default False, (readonly)

   .. data:: has_smooth_stroke

      :type: boolean, default False, (readonly)

   .. data:: has_space_attenuation

      :type: boolean, default False, (readonly)

   .. data:: has_strength_pressure

      :type: boolean, default False, (readonly)

   .. data:: has_tilt

      :type: boolean, default False, (readonly)

   .. data:: has_topology_rake

      :type: boolean, default False, (readonly)

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

   * :class:`Brush.sculpt_capabilities`

