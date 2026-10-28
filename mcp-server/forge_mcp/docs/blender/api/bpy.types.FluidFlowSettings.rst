FluidFlowSettings(bpy_struct)
=============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FluidFlowSettings(bpy_struct)

   Fluid flow settings

   .. attribute:: density

      :type: float in [0, 10], default 1.0

   .. attribute:: density_vertex_group

      Name of vertex group which determines surface emission rate

      :type: string, default "", (never None)

   .. attribute:: flow_behavior

      Change flow behavior in the simulation

      * ``INFLOW``
        Inflow -- Add fluid to simulation.
      * ``OUTFLOW``
        Outflow -- Delete fluid from simulation.
      * ``GEOMETRY``
        Geometry -- Only use given geometry for fluid.

      :type: enum in [``'INFLOW'``, ``'OUTFLOW'``, ``'GEOMETRY'``], default ``'GEOMETRY'``

   .. attribute:: flow_source

      Change how fluid is emitted

      :type: enum in [``'NONE'``], default ``'NONE'``

   .. attribute:: flow_type

      Change type of fluid in the simulation

      * ``SMOKE``
        Smoke -- Add smoke.
      * ``BOTH``
        Fire + Smoke -- Add fire and smoke.
      * ``FIRE``
        Fire -- Add fire.
      * ``LIQUID``
        Liquid -- Add liquid.

      :type: enum in [``'SMOKE'``, ``'BOTH'``, ``'FIRE'``, ``'LIQUID'``], default ``'SMOKE'``

   .. attribute:: fuel_amount

      :type: float in [0, 10], default 1.0

   .. attribute:: noise_texture

      Texture that controls emission strength

      :type: :class:`Texture`

   .. attribute:: particle_size

      Particle size in simulation cells

      :type: float in [0.1, inf], default 1.0

   .. attribute:: particle_system

      Particle systems emitted from the object

      :type: :class:`ParticleSystem`

   .. attribute:: smoke_color

      Color of smoke

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.7, 0.7, 0.7)

   .. attribute:: subframes

      Number of additional samples to take between frames to improve quality of fast moving flows

      :type: int in [0, 200], default 0

   .. attribute:: surface_distance

      Height (in domain grid units) of fluid emission above the mesh surface. Higher values result in emission further away from the mesh surface. If this value and the emitter size are smaller than the domain grid unit, fluid will not be created

      :type: float in [0, 10], default 1.0

   .. attribute:: temperature

      Temperature difference to ambient temperature

      :type: float in [-10, 10], default 1.0

   .. attribute:: texture_map_type

      Texture mapping type

      * ``AUTO``
        Generated -- Generated coordinates centered to flow object.
      * ``UV``
        UV -- Use UV layer for texture coordinates.

      :type: enum in [``'AUTO'``, ``'UV'``], default ``'AUTO'``

   .. attribute:: texture_offset

      Z-offset of texture mapping

      :type: float in [0, 200], default 0.0

   .. attribute:: texture_size

      Size of texture mapping

      :type: float in [0.01, 10], default 1.0

   .. attribute:: use_absolute

      Only allow given density value in emitter area and will not add up

      :type: boolean, default True

   .. attribute:: use_inflow

      Control when to apply fluid flow

      :type: boolean, default True

   .. attribute:: use_initial_velocity

      Fluid has some initial velocity when it is emitted

      :type: boolean, default False

   .. attribute:: use_particle_size

      Set particle size in simulation cells or use nearest cell

      :type: boolean, default True

   .. attribute:: use_plane_init

      Treat this object as a planar and unclosed mesh. Fluid will only be emitted from the mesh surface and based on the surface emission value.

      :type: boolean, default False

   .. attribute:: use_texture

      Use a texture to control emission strength

      :type: boolean, default False

   .. attribute:: uv_layer

      UV map name

      :type: string, default "", (never None)

   .. attribute:: velocity_coord

      Additional initial velocity in X, Y and Z direction (added to source velocity)

      :type: :class:`mathutils.Vector` of 3 items in [-1000.1, 1000.1], default (0.0, 0.0, 0.0)

   .. attribute:: velocity_factor

      Multiplier of source velocity passed to fluid (source velocity is non-zero only if object is moving)

      :type: float in [-100, 100], default 1.0

   .. attribute:: velocity_normal

      Amount of normal directional velocity

      :type: float in [-100, 100], default 0.0

   .. attribute:: velocity_random

      Amount of random velocity

      :type: float in [0, 10], default 0.0

   .. attribute:: volume_density

      Controls fluid emission from within the mesh (higher value results in greater emissions from inside the mesh)

      :type: float in [0, 1], default 0.0

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

   * :class:`FluidModifier.flow_settings`

