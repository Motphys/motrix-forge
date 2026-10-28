BoidRuleFollowLeader(BoidRule)
==============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`BoidRule`

.. class:: BoidRuleFollowLeader(BoidRule)


   .. attribute:: distance

      Distance behind leader to follow

      :type: float in [0, 100], default 0.0

   .. attribute:: object

      Follow this object instead of a boid

      :type: :class:`Object`

   .. attribute:: queue_count

      How many boids in a line

      :type: int in [0, 100], default 0

   .. attribute:: use_line

      Follow leader in a line

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
   * :class:`BoidRule.name`
   * :class:`BoidRule.type`
   * :class:`BoidRule.use_in_air`
   * :class:`BoidRule.use_on_land`

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
   * :class:`BoidRule.bl_rna_get_subclass`
   * :class:`BoidRule.bl_rna_get_subclass_py`

