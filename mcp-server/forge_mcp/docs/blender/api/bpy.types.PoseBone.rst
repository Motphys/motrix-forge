PoseBone(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PoseBone(bpy_struct)

   Channel defining pose data for a bone in a Pose

   .. attribute:: bbone_curveinx

      X-axis handle offset for start of the B-Bone's curve, adjusts curvature

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bbone_curveinz

      Z-axis handle offset for start of the B-Bone's curve, adjusts curvature

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bbone_curveoutx

      X-axis handle offset for end of the B-Bone's curve, adjusts curvature

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bbone_curveoutz

      Z-axis handle offset for end of the B-Bone's curve, adjusts curvature

      :type: float in [-inf, inf], default 0.0

   .. data:: bbone_custom_handle_end

      Bone that serves as the end handle for the B-Bone curve

      :type: :class:`PoseBone`, (readonly)

   .. data:: bbone_custom_handle_start

      Bone that serves as the start handle for the B-Bone curve

      :type: :class:`PoseBone`, (readonly)

   .. attribute:: bbone_easein

      Length of first Bézier Handle (for B-Bones only)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bbone_easeout

      Length of second Bézier Handle (for B-Bones only)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bbone_rollin

      Roll offset for the start of the B-Bone, adjusts twist

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bbone_rollout

      Roll offset for the end of the B-Bone, adjusts twist

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bbone_scalein

      Scale factors for the start of the B-Bone, adjusts thickness (for tapering effects)

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. attribute:: bbone_scaleout

      Scale factors for the end of the B-Bone, adjusts thickness (for tapering effects)

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. data:: bone

      Bone associated with this PoseBone

      :type: :class:`Bone`, (readonly, never None)

   .. data:: child

      Child of this pose bone

      :type: :class:`PoseBone`, (readonly)

   .. data:: color

      :type: :class:`BoneColor`, (readonly)

   .. data:: constraints

      Constraints that act on this pose channel

      :type: :class:`PoseBoneConstraints` :class:`bpy_prop_collection` of :class:`Constraint`, (readonly)

   .. attribute:: custom_shape

      Object that defines custom display shape for this bone

      :type: :class:`Object`

   .. attribute:: custom_shape_rotation_euler

      Adjust the rotation of the custom shape

      :type: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: custom_shape_scale_xyz

      Adjust the size of the custom shape

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. attribute:: custom_shape_transform

      Bone that defines the display transform of this custom shape

      :type: :class:`PoseBone`

   .. attribute:: custom_shape_translation

      Adjust the location of the custom shape

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: custom_shape_wire_width

      Adjust the line thickness of custom shapes

      :type: float in [1, 16], default 0.0

   .. data:: head

      Location of head of the channel's bone

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: ik_linear_weight

      Weight of scale constraint for IK

      :type: float in [0, 1], default 0.0

   .. attribute:: ik_max_x

      Maximum angles for IK Limit

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: ik_max_y

      Maximum angles for IK Limit

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: ik_max_z

      Maximum angles for IK Limit

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: ik_min_x

      Minimum angles for IK Limit

      :type: float in [-3.14159, 0], default 0.0

   .. attribute:: ik_min_y

      Minimum angles for IK Limit

      :type: float in [-3.14159, 0], default 0.0

   .. attribute:: ik_min_z

      Minimum angles for IK Limit

      :type: float in [-3.14159, 0], default 0.0

   .. attribute:: ik_rotation_weight

      Weight of rotation constraint for IK

      :type: float in [0, 1], default 0.0

   .. attribute:: ik_stiffness_x

      IK stiffness around the X axis

      :type: float in [0, 0.99], default 0.0

   .. attribute:: ik_stiffness_y

      IK stiffness around the Y axis

      :type: float in [0, 0.99], default 0.0

   .. attribute:: ik_stiffness_z

      IK stiffness around the Z axis

      :type: float in [0, 0.99], default 0.0

   .. attribute:: ik_stretch

      Allow scaling of the bone for IK

      :type: float in [0, 1], default 0.0

   .. data:: is_in_ik_chain

      Is part of an IK chain

      :type: boolean, default False, (readonly)

   .. data:: length

      Length of the bone

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. attribute:: location

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: lock_ik_x

      Disallow movement around the X axis

      :type: boolean, default False

   .. attribute:: lock_ik_y

      Disallow movement around the Y axis

      :type: boolean, default False

   .. attribute:: lock_ik_z

      Disallow movement around the Z axis

      :type: boolean, default False

   .. attribute:: lock_location

      Lock editing of location when transforming

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: lock_rotation

      Lock editing of rotation when transforming

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: lock_rotation_w

      Lock editing of 'angle' component of four-component rotations when transforming

      :type: boolean, default False

   .. attribute:: lock_rotations_4d

      Lock editing of four component rotations by components (instead of as Eulers)

      :type: boolean, default False

   .. attribute:: lock_scale

      Lock editing of scale when transforming

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: matrix

      Final 4×4 matrix after constraints and drivers are applied, in the armature object space

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: matrix_basis

      Alternative access to location/scale/rotation relative to the parent and own rest bone

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. data:: matrix_channel

      4×4 matrix of the bone's location/rotation/scale channels (including animation and drivers) and the effect of bone constraints

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

   .. data:: motion_path

      Motion Path for this element

      :type: :class:`MotionPath`, (readonly)

   .. attribute:: name

      :type: string, default "", (never None)

   .. data:: parent

      Parent of this pose bone

      :type: :class:`PoseBone`, (readonly)

   .. attribute:: rotation_axis_angle

      Angle of Rotation for Axis-Angle rotation representation

      :type: float array of 4 items in [-inf, inf], default (0.0, 0.0, 1.0, 0.0)

   .. attribute:: rotation_euler

      Rotation in Eulers

      :type: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: rotation_mode

      The kind of rotation to apply, values from other rotation modes aren't used

      :type: enum in :ref:`rna_enum_object_rotation_mode_items`, default ``'QUATERNION'``

   .. attribute:: rotation_quaternion

      Rotation in Quaternions

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (1.0, 0.0, 0.0, 0.0)

   .. attribute:: scale

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. data:: tail

      Location of tail of the channel's bone

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: use_custom_shape_bone_size

      Scale the custom object by the bone length

      :type: boolean, default False

   .. attribute:: use_ik_limit_x

      Limit movement around the X axis

      :type: boolean, default False

   .. attribute:: use_ik_limit_y

      Limit movement around the Y axis

      :type: boolean, default False

   .. attribute:: use_ik_limit_z

      Limit movement around the Z axis

      :type: boolean, default False

   .. attribute:: use_ik_linear_control

      Apply channel size as IK constraint if stretching is enabled

      :type: boolean, default False

   .. attribute:: use_ik_rotation_control

      Apply channel rotation as IK constraint

      :type: boolean, default False

   .. data:: basename

      The name of this bone before any '.' character

      (readonly)

   .. data:: center

      The midpoint between the head and the tail.

      (readonly)

   .. data:: children


      (readonly)

   .. data:: children_recursive

      A list of all children from this bone.
      
              .. note:: Takes ``O(len(bones)**2)`` time.

      (readonly)

   .. data:: children_recursive_basename

      Returns a chain of children with the same base name as this bone.
      Only direct chains are supported, forks caused by multiple children
      with matching base names will terminate the function
      and not be returned.
      
      .. note:: Takes ``O(len(bones)**2)`` time.

      (readonly)

   .. data:: parent_recursive

      A list of parents, starting with the immediate parent

      (readonly)

   .. data:: vector

      The direction this bone is pointing.
      Utility function for (tail - head)

      (readonly)

   .. data:: x_axis

      Vector pointing down the x-axis of the bone.

      (readonly)

   .. data:: y_axis

      Vector pointing down the y-axis of the bone.

      (readonly)

   .. data:: z_axis

      Vector pointing down the z-axis of the bone.

      (readonly)

   .. method:: evaluate_envelope(point)

      Calculate bone envelope at given point

      :arg point: Point, Position in 3d space to evaluate
      :type point: :class:`mathutils.Vector` of 3 items in [-inf, inf]
      :return: Factor, Envelope factor
      :rtype: float in [-inf, inf]

   .. method:: bbone_segment_index(point)

      Retrieve the index and blend factor of the B-Bone segments based on vertex position

      :arg point: Point, Vertex position in armature pose space
      :type point: :class:`mathutils.Vector` of 3 items in [-inf, inf]
      :return:
         `index`, The index of the first segment joint affecting the point, int in [-inf, inf]

         `blend_next`, The blend factor between the given and the following joint, float in [-inf, inf]

      :rtype: (int in [-inf, inf], float in [-inf, inf])

   .. method:: bbone_segment_matrix(index, *, rest=False)

      Retrieve the matrix of the joint between B-Bone segments if available

      :arg index: Index of the segment endpoint
      :type index: int in [0, inf]
      :arg rest: Return the rest pose matrix
      :type rest: boolean, (optional)
      :return: The resulting matrix in bone local space
      :rtype: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]

      This example shows how to use B-Bone segment matrices to emulate deformation
      produced by the Armature modifier or constraint when assigned to the given bone
      (without Preserve Volume). The coordinates are processed in armature Pose space:

      .. literalinclude:: ..\examples\bpy.types.PoseBone.bbone_segment_matrix.py
         :lines: 8-


   .. method:: compute_bbone_handles(*, rest=False, ease=False, offsets=False)

      Retrieve the vectors and rolls coming from B-Bone custom handles

      :arg rest: Return the rest pose state
      :type rest: boolean, (optional)
      :arg ease: Apply scale from ease values
      :type ease: boolean, (optional)
      :arg offsets: Apply roll and curve offsets from bone properties
      :type offsets: boolean, (optional)
      :return:
         `handle1`, The direction vector of the start handle in bone local space, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `roll1`, Roll of the start handle, float in [-inf, inf]

         `handle2`, The direction vector of the end handle in bone local space, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `roll2`, Roll of the end handle, float in [-inf, inf]

      :rtype: (:class:`mathutils.Vector` of 3 items in [-inf, inf], float in [-inf, inf], :class:`mathutils.Vector` of 3 items in [-inf, inf], float in [-inf, inf])

   .. method:: parent_index(parent_test)

      The same as 'bone in other_bone.parent_recursive'
      but saved generating a list.

   .. method:: translate(vec)

      Utility function to add *vec* to the head and tail of this bone

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

   * :mod:`bpy.context.active_pose_bone`
   * :mod:`bpy.context.pose_bone`
   * :mod:`bpy.context.selected_pose_bones`
   * :mod:`bpy.context.selected_pose_bones_from_active_object`
   * :mod:`bpy.context.visible_pose_bones`
   * :class:`Object.convert_space`
   * :class:`Pose.bones`
   * :class:`PoseBone.bbone_custom_handle_end`
   * :class:`PoseBone.bbone_custom_handle_start`
   * :class:`PoseBone.child`
   * :class:`PoseBone.custom_shape_transform`
   * :class:`PoseBone.parent`

