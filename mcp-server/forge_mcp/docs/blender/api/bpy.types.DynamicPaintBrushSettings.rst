DynamicPaintBrushSettings(bpy_struct)
=====================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: DynamicPaintBrushSettings(bpy_struct)

   Brush settings

   .. attribute:: invert_proximity

      Proximity falloff is applied inside the volume

      :type: boolean, default False

   .. attribute:: paint_alpha

      Paint alpha

      :type: float in [0, 1], default 0.0

   .. attribute:: paint_color

      Color of the paint

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: paint_distance

      Maximum distance from brush to mesh surface to affect paint

      :type: float in [0, 500], default 0.0

   .. data:: paint_ramp

      Color ramp used to define proximity falloff

      :type: :class:`ColorRamp`, (readonly)

   .. attribute:: paint_source

      :type: enum in [``'PARTICLE_SYSTEM'``, ``'POINT'``, ``'DISTANCE'``, ``'VOLUME_DISTANCE'``, ``'VOLUME'``], default ``'VOLUME'``

   .. attribute:: paint_wetness

      Paint wetness, visible in wetmap (some effects only affect wet paint)

      :type: float in [0, 1], default 0.0

   .. attribute:: particle_system

      The particle system to paint with

      :type: :class:`ParticleSystem`

   .. attribute:: proximity_falloff

      Proximity falloff type

      :type: enum in [``'SMOOTH'``, ``'CONSTANT'``, ``'RAMP'``], default ``'CONSTANT'``

   .. attribute:: ray_direction

      Ray direction to use for projection (if brush object is located in that direction it's painted)

      :type: enum in [``'CANVAS'``, ``'BRUSH'``, ``'Z_AXIS'``], default ``'CANVAS'``

   .. attribute:: smooth_radius

      Smooth falloff added after solid radius

      :type: float in [0, 10], default 0.0

   .. attribute:: smudge_strength

      Smudge effect strength

      :type: float in [0, 1], default 0.0

   .. attribute:: solid_radius

      Radius that will be painted solid

      :type: float in [0.01, 10], default 0.0

   .. attribute:: use_absolute_alpha

      Only increase alpha value if paint alpha is higher than existing

      :type: boolean, default False

   .. attribute:: use_negative_volume

      Negate influence inside the volume

      :type: boolean, default False

   .. attribute:: use_paint_erase

      Erase / remove paint instead of adding it

      :type: boolean, default False

   .. attribute:: use_particle_radius

      Use radius from particle settings

      :type: boolean, default False

   .. attribute:: use_proximity_project

      Brush is projected to canvas from defined direction within brush proximity

      :type: boolean, default False

   .. attribute:: use_proximity_ramp_alpha

      Only read color ramp alpha

      :type: boolean, default False

   .. attribute:: use_smudge

      Make this brush to smudge existing paint as it moves

      :type: boolean, default False

   .. attribute:: use_velocity_alpha

      Multiply brush influence by velocity color ramp alpha

      :type: boolean, default False

   .. attribute:: use_velocity_color

      Replace brush color by velocity color ramp

      :type: boolean, default False

   .. attribute:: use_velocity_depth

      Multiply brush intersection depth (displace, waves) by velocity ramp alpha

      :type: boolean, default False

   .. attribute:: velocity_max

      Velocity considered as maximum influence (Blender units per frame)

      :type: float in [0.0001, 10], default 0.0

   .. data:: velocity_ramp

      Color ramp used to define brush velocity effect

      :type: :class:`ColorRamp`, (readonly)

   .. attribute:: wave_clamp

      Maximum level of surface intersection used to influence waves (use 0.0 to disable)

      :type: float in [0, 50], default 0.0

   .. attribute:: wave_factor

      Multiplier for wave influence of this brush

      :type: float in [-2, 2], default 0.0

   .. attribute:: wave_type

      :type: enum in [``'CHANGE'``, ``'DEPTH'``, ``'FORCE'``, ``'REFLECT'``], default ``'DEPTH'``

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

   * :class:`DynamicPaintModifier.brush_settings`

