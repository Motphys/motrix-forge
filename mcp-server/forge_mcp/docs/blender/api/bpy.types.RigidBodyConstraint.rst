RigidBodyConstraint(bpy_struct)
===============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: RigidBodyConstraint(bpy_struct)

   Constraint influencing Objects inside Rigid Body Simulation

   .. attribute:: breaking_threshold

      Impulse threshold that must be reached for the constraint to break

      :type: float in [0, inf], default 10.0

   .. attribute:: disable_collisions

      Disable collisions between constrained rigid bodies

      :type: boolean, default False

   .. attribute:: enabled

      Enable this constraint

      :type: boolean, default False

   .. attribute:: limit_ang_x_lower

      Lower limit of X axis rotation

      :type: float in [-6.28319, 6.28319], default -0.785398

   .. attribute:: limit_ang_x_upper

      Upper limit of X axis rotation

      :type: float in [-6.28319, 6.28319], default 0.785398

   .. attribute:: limit_ang_y_lower

      Lower limit of Y axis rotation

      :type: float in [-6.28319, 6.28319], default -0.785398

   .. attribute:: limit_ang_y_upper

      Upper limit of Y axis rotation

      :type: float in [-6.28319, 6.28319], default 0.785398

   .. attribute:: limit_ang_z_lower

      Lower limit of Z axis rotation

      :type: float in [-6.28319, 6.28319], default -0.785398

   .. attribute:: limit_ang_z_upper

      Upper limit of Z axis rotation

      :type: float in [-6.28319, 6.28319], default 0.785398

   .. attribute:: limit_lin_x_lower

      Lower limit of X axis translation

      :type: float in [-inf, inf], default -1.0

   .. attribute:: limit_lin_x_upper

      Upper limit of X axis translation

      :type: float in [-inf, inf], default 1.0

   .. attribute:: limit_lin_y_lower

      Lower limit of Y axis translation

      :type: float in [-inf, inf], default -1.0

   .. attribute:: limit_lin_y_upper

      Upper limit of Y axis translation

      :type: float in [-inf, inf], default 1.0

   .. attribute:: limit_lin_z_lower

      Lower limit of Z axis translation

      :type: float in [-inf, inf], default -1.0

   .. attribute:: limit_lin_z_upper

      Upper limit of Z axis translation

      :type: float in [-inf, inf], default 1.0

   .. attribute:: motor_ang_max_impulse

      Maximum angular motor impulse

      :type: float in [0, inf], default 1.0

   .. attribute:: motor_ang_target_velocity

      Target angular motor velocity

      :type: float in [-inf, inf], default 1.0

   .. attribute:: motor_lin_max_impulse

      Maximum linear motor impulse

      :type: float in [0, inf], default 1.0

   .. attribute:: motor_lin_target_velocity

      Target linear motor velocity

      :type: float in [-inf, inf], default 1.0

   .. attribute:: object1

      First Rigid Body Object to be constrained

      :type: :class:`Object`

   .. attribute:: object2

      Second Rigid Body Object to be constrained

      :type: :class:`Object`

   .. attribute:: solver_iterations

      Number of constraint solver iterations made per simulation step (higher values are more accurate but slower)

      :type: int in [1, 1000], default 10

   .. attribute:: spring_damping_ang_x

      Damping on the X rotational axis

      :type: float in [0, inf], default 0.5

   .. attribute:: spring_damping_ang_y

      Damping on the Y rotational axis

      :type: float in [0, inf], default 0.5

   .. attribute:: spring_damping_ang_z

      Damping on the Z rotational axis

      :type: float in [0, inf], default 0.5

   .. attribute:: spring_damping_x

      Damping on the X axis

      :type: float in [0, inf], default 0.5

   .. attribute:: spring_damping_y

      Damping on the Y axis

      :type: float in [0, inf], default 0.5

   .. attribute:: spring_damping_z

      Damping on the Z axis

      :type: float in [0, inf], default 0.5

   .. attribute:: spring_stiffness_ang_x

      Stiffness on the X rotational axis

      :type: float in [0, inf], default 10.0

   .. attribute:: spring_stiffness_ang_y

      Stiffness on the Y rotational axis

      :type: float in [0, inf], default 10.0

   .. attribute:: spring_stiffness_ang_z

      Stiffness on the Z rotational axis

      :type: float in [0, inf], default 10.0

   .. attribute:: spring_stiffness_x

      Stiffness on the X axis

      :type: float in [0, inf], default 10.0

   .. attribute:: spring_stiffness_y

      Stiffness on the Y axis

      :type: float in [0, inf], default 10.0

   .. attribute:: spring_stiffness_z

      Stiffness on the Z axis

      :type: float in [0, inf], default 10.0

   .. attribute:: spring_type

      Which implementation of spring to use

      * ``SPRING1``
        Blender 2.7 -- Spring implementation used in Blender 2.7. Damping is capped at 1.0.
      * ``SPRING2``
        Blender 2.8 -- New implementation available since 2.8.

      :type: enum in [``'SPRING1'``, ``'SPRING2'``], default ``'SPRING1'``

   .. attribute:: type

      Type of Rigid Body Constraint

      :type: enum in :ref:`rna_enum_rigidbody_constraint_type_items`, default ``'POINT'``

   .. attribute:: use_breaking

      Constraint can be broken if it receives an impulse above the threshold

      :type: boolean, default False

   .. attribute:: use_limit_ang_x

      Limit rotation around X axis

      :type: boolean, default False

   .. attribute:: use_limit_ang_y

      Limit rotation around Y axis

      :type: boolean, default False

   .. attribute:: use_limit_ang_z

      Limit rotation around Z axis

      :type: boolean, default False

   .. attribute:: use_limit_lin_x

      Limit translation on X axis

      :type: boolean, default False

   .. attribute:: use_limit_lin_y

      Limit translation on Y axis

      :type: boolean, default False

   .. attribute:: use_limit_lin_z

      Limit translation on Z axis

      :type: boolean, default False

   .. attribute:: use_motor_ang

      Enable angular motor

      :type: boolean, default False

   .. attribute:: use_motor_lin

      Enable linear motor

      :type: boolean, default False

   .. attribute:: use_override_solver_iterations

      Override the number of solver iterations for this constraint

      :type: boolean, default False

   .. attribute:: use_spring_ang_x

      Enable spring on X rotational axis

      :type: boolean, default False

   .. attribute:: use_spring_ang_y

      Enable spring on Y rotational axis

      :type: boolean, default False

   .. attribute:: use_spring_ang_z

      Enable spring on Z rotational axis

      :type: boolean, default False

   .. attribute:: use_spring_x

      Enable spring on X axis

      :type: boolean, default False

   .. attribute:: use_spring_y

      Enable spring on Y axis

      :type: boolean, default False

   .. attribute:: use_spring_z

      Enable spring on Z axis

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

   * :class:`Object.rigid_body_constraint`

