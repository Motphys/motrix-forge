ClothCollisionSettings(bpy_struct)
==================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ClothCollisionSettings(bpy_struct)

   Cloth simulation settings for self collision and collision with other objects

   .. attribute:: collection

      Limit colliders to this Collection

      :type: :class:`Collection`

   .. attribute:: collision_quality

      How many collision iterations should be done (higher is better quality but slower)

      :type: int in [1, 32767], default 2

   .. attribute:: damping

      Amount of velocity lost on collision

      :type: float in [0, 1], default 1.0

   .. attribute:: distance_min

      Minimum distance between collision objects before collision response takes effect

      :type: float in [0.001, 1], default 0.015

   .. attribute:: friction

      Friction force if a collision happened (higher = less movement)

      :type: float in [0, 80], default 5.0

   .. attribute:: impulse_clamp

      Clamp collision impulses to avoid instability (0.0 to disable clamping)

      :type: float in [0, 100], default 0.0

   .. attribute:: self_distance_min

      Minimum distance between cloth faces before collision response takes effect

      :type: float in [0.001, 0.1], default 0.015

   .. attribute:: self_friction

      Friction with self contact

      :type: float in [0, 80], default 5.0

   .. attribute:: self_impulse_clamp

      Clamp collision impulses to avoid instability (0.0 to disable clamping)

      :type: float in [0, 100], default 0.0

   .. attribute:: use_collision

      Enable collisions with other objects

      :type: boolean, default True

   .. attribute:: use_self_collision

      Enable self collisions

      :type: boolean, default False

   .. attribute:: vertex_group_object_collisions

      Triangles with all vertices in this group are not used during object collisions

      :type: string, default "", (never None)

   .. attribute:: vertex_group_self_collisions

      Triangles with all vertices in this group are not used during self collisions

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

   * :class:`ClothModifier.collision_settings`

