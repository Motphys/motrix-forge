.. index:: Object Constraints; Limit Rotation Constraint
.. _bpy.types.LimitRotationConstraint:

*************************
Limit Rotation Constraint
*************************

This constraint restricts the rotation of an object or bone to be inside
specified angular limits.  The limits are given as Euler rotation ranges (a min
and max angle), and a separate range can be given for each of the three axes.

As with all constraints in Blender, this does not (by default) restrict the
user-set rotation values of the object/bone as seen in the *Transform* panel.
When the object/bone is rotated outside the limit range, it will be constrained
to that range in its final displayed/rendered position, but the user-set
rotation values will still be outside that range. If the constraint is removed,
the object/bone will then jump back to match those user-set values.

Something unique about the Limit Rotation constraint (as compared to the Limit
Location and Limit Scale constraints) is that rotations loop, and therefore the
meaning of the limit range is subtly different. All constraints in Blender
internally work on transform matrices, which can't distinguish between e.g. 180
and -180 degrees, or 0, 360, and 720 degrees. In other words, any angles that
result in the same visual rotation are indistinguishable to the constraint
system.

What this means for the Limit Rotation constraint is that when the user-set
rotation is outside of the limit range, the final displayed rotation will snap
to the closest *visual* rotation in that range, not the closest numerical angle.
For example, if you have a limit range of 0 to 90 degrees then a user-set
rotation of 340 degrees will actually snap to *0 degrees* because that is the
closer *visual* rotation, even though 340 is numerically closer to 90.

Note that this constraint does not constrain the bone if it is manipulated by
the IK solver. For constraining the rotation of a bone for IK purposes, see
:doc:`Inverse Kinematics
</animation/armatures/posing/bone_constraints/inverse_kinematics/introduction>`.


Options
=======

.. figure:: /images/animation_constraints_transform_limit-rotation_panel.png

   Limit Rotation panel.

Limit X, Y, Z
   These buttons enable the rotation limit around respectively the X, Y and Z axes of the owner,
   in the chosen *Owner* space.
   The *Min* and *Max* number fields to their right control the value of
   their lower and upper boundaries, respectively.

   .. note::

      - If a min value is higher than its corresponding max value,
        the constraint behaves as if it had the same value as the max one.
      - Unlike the :doc:`Limit Location constraint </animation/constraints/transform/limit_location>`,
        you cannot separately enable lower or upper limits.
      - The constraint can be used to simply remove shear from the owner transformation
        by leaving all limits disabled.

Order
   Allows specifying which :term:`Euler` order to use when applying the limits.
   Defaults to the order of the owner, or XYZ if the owner uses non-Euler
   rotations.

Affect Transform
   The constraint is taken into account when the object is manually rotated using
   transformation tools in the editors. This prevents assigning transformation
   property values (as shown in the *Transform* panel) that exceed the specified limits.

Legacy Behavior
   For backwards compatibility: make the constraint behave in the semi-broken
   way it did prior to Blender 4.2. This old behavior does not properly account
   for the looping nature of rotations, and therefore causes
   unpredictable/erratic rotation snapping. However, this behavior can still be
   useful in some specific circumstances when `Owner` is set to local space, and
   some older rig setups utilize that. However, that behavior is better and more
   robustly accomplished with drivers directly on the object/bone's rotation
   properties, so new rigs should favor that approach over using this option.

Owner
   This constraint allows you to choose in which space evaluate its owner's transform properties.
   See :ref:`common constraint properties <rigging-constraints-interface-common-space>` for more information.

Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. peertube:: 3ce2539e-3bb9-4caf-9911-1217a1e8907c
