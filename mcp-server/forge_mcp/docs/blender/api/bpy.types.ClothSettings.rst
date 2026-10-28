ClothSettings(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ClothSettings(bpy_struct)

   Cloth simulation settings for an object

   .. attribute:: air_damping

      Air has normally some thickness which slows falling things down

      :type: float in [0, 10], default 1.0

   .. attribute:: bending_damping

      Amount of damping in bending behavior

      :type: float in [0, 1000], default 0.5

   .. attribute:: bending_model

      Physical model for simulating bending forces

      * ``ANGULAR``
        Angular -- Cloth model with angular bending springs.
      * ``LINEAR``
        Linear -- Cloth model with linear bending springs (legacy).

      :type: enum in [``'ANGULAR'``, ``'LINEAR'``], default ``'ANGULAR'``

   .. attribute:: bending_stiffness

      How much the material resists bending

      :type: float in [0, 10000], default 0.5

   .. attribute:: bending_stiffness_max

      Maximum bending stiffness value

      :type: float in [0, 10000], default 0.5

   .. attribute:: collider_friction

      :type: float in [0, 1], default 0.0

   .. attribute:: compression_damping

      Amount of damping in compression behavior

      :type: float in [0, 50], default 5.0

   .. attribute:: compression_stiffness

      How much the material resists compression

      :type: float in [0, 10000], default 15.0

   .. attribute:: compression_stiffness_max

      Maximum compression stiffness value

      :type: float in [0, 10000], default 15.0

   .. attribute:: density_strength

      Influence of target density on the simulation

      :type: float in [0, 1], default 0.0

   .. attribute:: density_target

      Maximum density of hair

      :type: float in [0, 10000], default 0.0

   .. data:: effector_weights

      :type: :class:`EffectorWeights`, (readonly)

   .. attribute:: fluid_density

      Density (kg/l) of the fluid contained inside the object, used to create a hydrostatic pressure gradient simulating the weight of the internal fluid, or buoyancy from the surrounding fluid if negative

      :type: float in [-inf, inf], default 0.0

   .. attribute:: goal_default

      Default Goal (vertex target position) value, when no Vertex Group used

      :type: float in [0, 1], default 0.0

   .. attribute:: goal_friction

      Goal (vertex target position) friction

      :type: float in [0, 50], default 0.0

   .. attribute:: goal_max

      Goal maximum, vertex group weights are scaled to match this range

      :type: float in [0, 1], default 1.0

   .. attribute:: goal_min

      Goal minimum, vertex group weights are scaled to match this range

      :type: float in [0, 1], default 0.0

   .. attribute:: goal_spring

      Goal (vertex target position) spring stiffness

      :type: float in [0, 0.999], default 1.0

   .. attribute:: gravity

      Gravity or external force vector

      :type: :class:`mathutils.Vector` of 3 items in [-100, 100], default (0.0, 0.0, -9.81)

   .. attribute:: internal_compression_stiffness

      How much the material resists compression

      :type: float in [0, 10000], default 15.0

   .. attribute:: internal_compression_stiffness_max

      Maximum compression stiffness value

      :type: float in [0, 10000], default 15.0

   .. attribute:: internal_friction

      :type: float in [0, 1], default 0.0

   .. attribute:: internal_spring_max_diversion

      How much the rays used to connect the internal points can diverge from the vertex normal

      :type: float in [0, 0.785398], default 0.785398

   .. attribute:: internal_spring_max_length

      The maximum length an internal spring can have during creation. If the distance between internal points is greater than this, no internal spring will be created between these points. A length of zero means that there is no length limit.

      :type: float in [0, 1000], default 0.0

   .. attribute:: internal_spring_normal_check

      Require the points the internal springs connect to have opposite normal directions

      :type: boolean, default True

   .. attribute:: internal_tension_stiffness

      How much the material resists stretching

      :type: float in [0, 10000], default 15.0

   .. attribute:: internal_tension_stiffness_max

      Maximum tension stiffness value

      :type: float in [0, 10000], default 15.0

   .. attribute:: mass

      The mass of each vertex on the cloth material

      :type: float in [0, inf], default 0.3

   .. attribute:: pin_stiffness

      Pin (vertex target position) spring stiffness

      :type: float in [0, 50], default 1.0

   .. attribute:: pressure_factor

      Ambient pressure (kPa) that balances out between the inside and outside of the object when it has the target volume

      :type: float in [0, 10000], default 1.0

   .. attribute:: quality

      Quality of the simulation in steps per frame (higher is better quality but slower)

      :type: int in [1, inf], default 5

   .. attribute:: rest_shape_key

      Shape key to use the rest spring lengths from

      :type: :class:`ShapeKey`

   .. attribute:: sewing_force_max

      Maximum sewing force

      :type: float in [0, 10000], default 0.0

   .. attribute:: shear_damping

      Amount of damping in shearing behavior

      :type: float in [0, 50], default 5.0

   .. attribute:: shear_stiffness

      How much the material resists shearing

      :type: float in [0, 10000], default 5.0

   .. attribute:: shear_stiffness_max

      Maximum shear scaling value

      :type: float in [0, 10000], default 5.0

   .. attribute:: shrink_max

      Max amount to shrink cloth by

      :type: float in [-inf, 1], default 0.0

   .. attribute:: shrink_min

      Factor by which to shrink cloth

      :type: float in [-inf, 1], default 0.0

   .. attribute:: target_volume

      The mesh volume where the inner/outer pressure will be the same. If set to zero the change in volume will not affect pressure.

      :type: float in [0, 10000], default 0.0

   .. attribute:: tension_damping

      Amount of damping in stretching behavior

      :type: float in [0, 50], default 5.0

   .. attribute:: tension_stiffness

      How much the material resists stretching

      :type: float in [0, 10000], default 15.0

   .. attribute:: tension_stiffness_max

      Maximum tension stiffness value

      :type: float in [0, 10000], default 15.0

   .. attribute:: time_scale

      Cloth speed is multiplied by this value

      :type: float in [0, inf], default 1.0

   .. attribute:: uniform_pressure_force

      The uniform pressure that is constantly applied to the mesh, in units of Pressure Scale. Can be negative.

      :type: float in [-10000, 10000], default 0.0

   .. attribute:: use_dynamic_mesh

      Make simulation respect deformations in the base mesh

      :type: boolean, default False

   .. attribute:: use_internal_springs

      Simulate an internal volume structure by creating springs connecting the opposite sides of the mesh

      :type: boolean, default False

   .. attribute:: use_pressure

      Simulate pressure inside a closed cloth mesh

      :type: boolean, default False

   .. attribute:: use_pressure_volume

      Use the Target Volume parameter as the initial volume, instead of calculating it from the mesh itself

      :type: boolean, default False

   .. attribute:: use_sewing_springs

      Pulls loose edges together

      :type: boolean, default False

   .. attribute:: vertex_group_bending

      Vertex group for fine control over bending stiffness

      :type: string, default "", (never None)

   .. attribute:: vertex_group_intern

      Vertex group for fine control over the internal spring stiffness

      :type: string, default "", (never None)

   .. attribute:: vertex_group_mass

      Vertex Group for pinning of vertices

      :type: string, default "", (never None)

   .. attribute:: vertex_group_pressure

      Vertex Group for where to apply pressure. Zero weight means no pressure while a weight of one means full pressure. Faces with a vertex that has zero weight will be excluded from the volume calculation.

      :type: string, default "", (never None)

   .. attribute:: vertex_group_shear_stiffness

      Vertex group for fine control over shear stiffness

      :type: string, default "", (never None)

   .. attribute:: vertex_group_shrink

      Vertex Group for shrinking cloth

      :type: string, default "", (never None)

   .. attribute:: vertex_group_structural_stiffness

      Vertex group for fine control over structural stiffness

      :type: string, default "", (never None)

   .. attribute:: voxel_cell_size

      Size of the voxel grid cells for interaction effects

      :type: float in [0.0001, 10000], default 0.1

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

   * :class:`ClothModifier.settings`

