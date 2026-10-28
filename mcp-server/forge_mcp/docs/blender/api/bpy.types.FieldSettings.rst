FieldSettings(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FieldSettings(bpy_struct)

   Field settings for an object in physics simulation

   .. attribute:: apply_to_location

      Affect particle's location

      :type: boolean, default False

   .. attribute:: apply_to_rotation

      Affect particle's dynamic rotation

      :type: boolean, default False

   .. attribute:: distance_max

      Maximum distance for the field to work

      :type: float in [0, inf], default 0.0

   .. attribute:: distance_min

      Minimum distance for the field's falloff

      :type: float in [0, 1000], default 0.0

   .. attribute:: falloff_power

      How quickly strength falls off with distance from the force field

      :type: float in [0, 10], default 0.0

   .. attribute:: falloff_type

      :type: enum in [``'CONE'``, ``'SPHERE'``, ``'TUBE'``], default ``'SPHERE'``

   .. attribute:: flow

      Convert effector force into air flow velocity

      :type: float in [-inf, inf], default 0.0

   .. attribute:: guide_clump_amount

      Amount of clumping

      :type: float in [-1, 1], default 0.0

   .. attribute:: guide_clump_shape

      Shape of clumping

      :type: float in [-0.999, 0.999], default 0.0

   .. attribute:: guide_free

      Guide-free time from particle life's end

      :type: float in [0, 0.99], default 0.0

   .. attribute:: guide_kink_amplitude

      The amplitude of the offset

      :type: float in [0, 10], default 0.0

   .. attribute:: guide_kink_axis

      Which axis to use for offset

      :type: enum in :ref:`rna_enum_axis_xyz_items`, default ``'X'``

   .. attribute:: guide_kink_frequency

      The frequency of the offset (1/total length)

      :type: float in [0, 10], default 0.0

   .. attribute:: guide_kink_shape

      Adjust the offset to the beginning/end

      :type: float in [-0.999, 0.999], default 0.0

   .. attribute:: guide_kink_type

      Type of periodic offset on the curve

      :type: enum in [``'NONE'``, ``'BRAID'``, ``'CURL'``, ``'RADIAL'``, ``'ROLL'``, ``'ROTATION'``, ``'WAVE'``], default ``'NONE'``

   .. attribute:: guide_minimum

      The distance from which particles are affected fully

      :type: float in [-inf, inf], default 0.0

   .. attribute:: harmonic_damping

      Damping of the harmonic force

      :type: float in [-inf, inf], default 0.0

   .. attribute:: inflow

      Inwards component of the vortex force

      :type: float in [-inf, inf], default 0.0

   .. attribute:: linear_drag

      Drag component proportional to velocity

      :type: float in [-inf, inf], default 0.0

   .. attribute:: noise

      Amount of noise for the force strength

      :type: float in [0, 10], default 0.0

   .. attribute:: quadratic_drag

      Drag component proportional to the square of velocity

      :type: float in [-inf, inf], default 0.0

   .. attribute:: radial_falloff

      Radial falloff power (real gravitational falloff = 2)

      :type: float in [0, 10], default 0.0

   .. attribute:: radial_max

      Maximum radial distance for the field to work

      :type: float in [0, 1000], default 0.0

   .. attribute:: radial_min

      Minimum radial distance for the field's falloff

      :type: float in [0, 1000], default 0.0

   .. attribute:: rest_length

      Rest length of the harmonic force

      :type: float in [0, inf], default 0.0

   .. attribute:: seed

      Seed of the noise

      :type: int in [1, 128], default 0

   .. attribute:: shape

      Which direction is used to calculate the effector force

      * ``POINT``
        Point -- Field originates from the object center.
      * ``LINE``
        Line -- Field originates from the local Z axis of the object.
      * ``PLANE``
        Plane -- Field originates from the local XY plane of the object.
      * ``SURFACE``
        Surface -- Field originates from the surface of the object.
      * ``POINTS``
        Every Point -- Field originates from all of the vertices of the object.

      :type: enum in [``'POINT'``, ``'LINE'``, ``'PLANE'``, ``'SURFACE'``, ``'POINTS'``], default ``'POINT'``

   .. attribute:: size

      Size of the turbulence

      :type: float in [0, inf], default 0.0

   .. attribute:: source_object

      Select domain object of the smoke simulation

      :type: :class:`Object`

   .. attribute:: strength

      Strength of force field

      :type: float in [-inf, inf], default 0.0

   .. attribute:: texture

      Texture to use as force

      :type: :class:`Texture`

   .. attribute:: texture_mode

      How the texture effect is calculated (RGB and Curl need a RGB texture, else Gradient will be used instead)

      :type: enum in [``'CURL'``, ``'GRADIENT'``, ``'RGB'``], default ``'RGB'``

   .. attribute:: texture_nabla

      Defines size of derivative offset used for calculating gradient and curl

      :type: float in [0.0001, 1], default 0.0

   .. attribute:: type

      Type of field

      * ``NONE``
        None.
      * ``BOID``
        Boid -- Create a force that acts as a boid's predators or target.
      * ``CHARGE``
        Charge -- Spherical forcefield based on the charge of particles, only influences other charge force fields.
      * ``GUIDE``
        Curve Guide -- Create a force along a curve object.
      * ``DRAG``
        Drag -- Create a force that dampens motion.
      * ``FLUID_FLOW``
        Fluid Flow -- Create a force based on fluid simulation velocities.
      * ``FORCE``
        Force -- Radial field toward the center of object.
      * ``HARMONIC``
        Harmonic -- The source of this force field is the zero point of a harmonic oscillator.
      * ``LENNARDJ``
        Lennard-Jones -- Forcefield based on the Lennard-Jones potential.
      * ``MAGNET``
        Magnetic -- Forcefield depends on the speed of the particles.
      * ``TEXTURE``
        Texture -- Force field based on a texture.
      * ``TURBULENCE``
        Turbulence -- Create turbulence with a noise field.
      * ``VORTEX``
        Vortex -- Spiraling force that twists the force object's local Z axis.
      * ``WIND``
        Wind -- Constant force along the force object's local Z axis.

      :type: enum in [``'NONE'``, ``'BOID'``, ``'CHARGE'``, ``'GUIDE'``, ``'DRAG'``, ``'FLUID_FLOW'``, ``'FORCE'``, ``'HARMONIC'``, ``'LENNARDJ'``, ``'MAGNET'``, ``'TEXTURE'``, ``'TURBULENCE'``, ``'VORTEX'``, ``'WIND'``], default ``'NONE'``

   .. attribute:: use_2d_force

      Apply force only in 2D

      :type: boolean, default False

   .. attribute:: use_absorption

      Force gets absorbed by collision objects

      :type: boolean, default False

   .. attribute:: use_global_coords

      Use effector/global coordinates for turbulence

      :type: boolean, default False

   .. attribute:: use_gravity_falloff

      Multiply force by 1/distance²

      :type: boolean, default False

   .. attribute:: use_guide_path_add

      Based on distance/falloff it adds a portion of the entire path

      :type: boolean, default False

   .. attribute:: use_guide_path_weight

      Use curve weights to influence the particle influence along the curve

      :type: boolean, default False

   .. attribute:: use_max_distance

      Use a maximum distance for the field to work

      :type: boolean, default False

   .. attribute:: use_min_distance

      Use a minimum distance for the field's falloff

      :type: boolean, default False

   .. attribute:: use_multiple_springs

      Every point is affected by multiple springs

      :type: boolean, default False

   .. attribute:: use_object_coords

      Use object/global coordinates for texture

      :type: boolean, default False

   .. attribute:: use_radial_max

      Use a maximum radial distance for the field to work

      :type: boolean, default False

   .. attribute:: use_radial_min

      Use a minimum radial distance for the field's falloff

      :type: boolean, default False

   .. attribute:: use_root_coords

      Texture coordinates from root particle locations

      :type: boolean, default False

   .. attribute:: use_smoke_density

      Adjust force strength based on smoke density

      :type: boolean, default False

   .. attribute:: wind_factor

      How much the force is reduced when acting parallel to a surface, e.g. cloth

      :type: float in [0, 1], default 0.0

   .. attribute:: z_direction

      Effect in full or only positive/negative Z direction

      :type: enum in [``'POSITIVE'``, ``'NEGATIVE'``, ``'BOTH'``], default ``'BOTH'``

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

   * :class:`Object.field`
   * :class:`ParticleSettings.force_field_1`
   * :class:`ParticleSettings.force_field_2`

