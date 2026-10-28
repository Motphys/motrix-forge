ParticleHairKey(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ParticleHairKey(bpy_struct)

   Particle key for hair particle system

   .. attribute:: co

      Location of the hair key in object space

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: co_local

      Location of the hair key in its local coordinate system, relative to the emitting face

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: time

      Relative time of key over hair length

      :type: float in [0, inf], default 0.0

   .. attribute:: weight

      Weight for cloth simulation

      :type: float in [0, 1], default 0.0

   .. method:: co_object(object, modifier, particle)

      Obtain hairkey location with particle and modifier data

      :arg object: Object
      :type object: :class:`Object`, (never None)
      :arg modifier: Particle modifier
      :type modifier: :class:`ParticleSystemModifier`, (never None)
      :arg particle: hair particle
      :type particle: :class:`Particle`, (never None)
      :return: Co, Exported hairkey location
      :rtype: :class:`mathutils.Vector` of 3 items in [-inf, inf]

   .. method:: co_object_set(object, modifier, particle, co)

      Set hairkey location with particle and modifier data

      :arg object: Object
      :type object: :class:`Object`, (never None)
      :arg modifier: Particle modifier
      :type modifier: :class:`ParticleSystemModifier`, (never None)
      :arg particle: hair particle
      :type particle: :class:`Particle`, (never None)
      :arg co: Co, Specified hairkey location
      :type co: :class:`mathutils.Vector` of 3 items in [-inf, inf]

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

   * :class:`Particle.hair_keys`

