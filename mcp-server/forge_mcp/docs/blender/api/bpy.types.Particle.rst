Particle(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Particle(bpy_struct)

   Particle in a particle system

   .. attribute:: alive_state

      :type: enum in [``'DEAD'``, ``'UNBORN'``, ``'ALIVE'``, ``'DYING'``], default ``'DEAD'``

   .. attribute:: angular_velocity

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: birth_time

      :type: float in [-inf, inf], default 0.0

   .. attribute:: die_time

      :type: float in [-inf, inf], default 0.0

   .. data:: hair_keys

      :type: :class:`bpy_prop_collection` of :class:`ParticleHairKey`, (readonly)

   .. data:: is_exist

      :type: boolean, default False, (readonly)

   .. data:: is_visible

      :type: boolean, default False, (readonly)

   .. attribute:: lifetime

      :type: float in [-inf, inf], default 0.0

   .. attribute:: location

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. data:: particle_keys

      :type: :class:`bpy_prop_collection` of :class:`ParticleKey`, (readonly)

   .. attribute:: prev_angular_velocity

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: prev_location

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: prev_rotation

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: prev_velocity

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: rotation

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: size

      :type: float in [-inf, inf], default 0.0

   .. attribute:: velocity

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. method:: uv_on_emitter(modifier)

      Obtain UV coordinates for a particle on an evaluated mesh.

      :arg modifier: Particle modifier from an evaluated object
      :type modifier: :class:`ParticleSystemModifier`, (never None)
      :return: uv
      :rtype: :class:`mathutils.Vector` of 2 items in [-inf, inf]

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

   * :class:`ParticleHairKey.co_object`
   * :class:`ParticleHairKey.co_object_set`
   * :class:`ParticleSystem.mcol_on_emitter`
   * :class:`ParticleSystem.particles`
   * :class:`ParticleSystem.uv_on_emitter`

