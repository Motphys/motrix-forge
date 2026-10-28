.. index:: Object Constraints; Follow Path Constraint
.. _bpy.types.FollowPathConstraint:

**********************
Follow Path Constraint
**********************

The *Follow Path* constraint moves an object along a curve and, if enabled,
adjusts its rotation to align with the curve's direction. This constraint is commonly used for:

- Animating objects along a predefined path, such as vehicles on a track or a camera following a scene.
- Simulating mechanical systems like conveyor belts or bicycle chains.
- Controlling motion smoothly without keyframing each movement manually.

.. tip::

   The *Follow Path* constraint works well in combination with the
   :doc:`Locked Track Constraint </animation/constraints/tracking/locked_track>`.
   For example, when animating a camera along a path, a *Locked Track* constraint
   can help control its roll angle by locking it to a secondary target.

.. admonition:: Follow Path vs. Clamp To
   :class: note

   While both constraints move objects along a curve,
   *Follow Path* is **time-based** (movement is determined by the current frame),
   whereas the :doc:`Clamp To Constraint </animation/constraints/tracking/clamp_to>`
   sets an object's position based on a **location property**.


Object Space Evaluation
=======================

Note, the object's position and rotation are evaluated in :term:`World Space`:

- **Position Offset**: The object's location acts as an offset from its normal position on the curve.
  For example, an object with a location of *(1.0, 1.0, 0.0)* will be displaced
  by one unit along the X and Y axes from its default path position.
  To place the object exactly on the curve, reset its location with :kbd:`Alt-G`.
- **Scale Influence**: The object's offset is affected by the curve's scale.
  If the curve has a scale of *(2.0, 1.0, 1.0)*, the same *(1.0, 1.0, 0.0)*
  offset will be doubled along the X-axis but remain unchanged along Y.
- **Rotation Alignment**: When *Follow Curve* is enabled, the object's rotation follows the curve's direction.
  To ensure correct alignment, the object's axis should be properly oriented before applying the constraint.
  Resetting rotation with :kbd:`Alt-R` may help.


Controlling Movement Along the Path
===================================

The object's motion along the curve can be controlled in different ways:

#. **Path Animation Timing**:
   The movement is determined by the curve's *Path Animation* settings in the object properties.
   The *Frames* value defines the duration, and the constraint's *Offset* shifts the start frame.
#. **Custom Animation via F-Curves**: For precise control, an *Evaluation Time*
   F-Curve can be added in the *Graph Editor* to control movement dynamically.
#. **Stationary Object on the Path**: If an object should remain fixed at a point on the curve,
   a flat *Speed* F-Curve can be used, where the curve's value determines the position along the path.


Options
=======

.. figure:: /images/animation_constraints_relationship_follow-path_panel.png

   Follow Path panel.

Target
   :ref:`ui-data-id` used to select the constraint's target, which *must* be a curve object,
   and is not functional (red state) when it has none.
   See :ref:`common constraint properties <rigging-constraints-interface-common-target>` for more information.

Offset
   Offsets the object's position along the curve in frames (relative to the animation settings).

Forward Axis
   The axis of the object that has to be aligned with the forward direction of the path
   (i.e. tangent to the curve at the owner's position). It is affected if Follow Curve option activated.

Up Axis
   The axis of the object that has to be aligned (as much as possible) with the world Z axis.
   In fact, with this option activated, the behavior of the owner shares some properties with
   the one caused by a :doc:`Locked Track constraint </animation/constraints/tracking/locked_track>`,
   with the path as "axle", and the world Z axis as "magnet". It is affected if Follow Curve option activated.

Fixed Position
   Locks the object to a specific position along the curve, regardless of animation.

Curve Radius
   Scales the object based on the curve's radius. See :doc:`Curve Editing </modeling/curves/properties/geometry>`.

Follow Curve
   If this option is not activated, the owner's rotation is not modified by the curve; otherwise,
   it is affected depending on the Forward and Up Axes.

.. _bpy.ops.constraint.followpath_path_animate:

Animate Path
   Automatically creates an F-Curve to control the object's motion along the path.

   .. admonition:: Keyframing Evaluation Time
      :class: tip

      To animate movement along a path manually, keyframe the curve's *Evaluation Time*:

      #. Select the curve and go to the *Path Animation* panel in the curve properties.
      #. At the first frame (e.g., frame 1), set *Evaluation Time* to the start value (e.g., 1).
      #. Right-click *Evaluation Time* and select *Insert Keyframe*.
      #. Move to the final frame (e.g., frame 100), set *Evaluation Time* to the end value (e.g., 100).
      #. Insert another keyframe.

      This allows full control over the object's movement along the curve.
Influence
   Controls the percentage of affect the constraint has on the object.
   See :ref:`common constraint properties <bpy.types.constraint.influence>` for more information.


Example
=======

.. peertube:: 24507160-624d-423e-a8dd-5110ff8823d1
