Bone(bpy_struct)
================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Bone(bpy_struct)

   Bone in an Armature data-block

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

   .. attribute:: bbone_custom_handle_end

      Bone that serves as the end handle for the B-Bone curve

      :type: :class:`Bone`

   .. attribute:: bbone_custom_handle_start

      Bone that serves as the start handle for the B-Bone curve

      :type: :class:`Bone`

   .. attribute:: bbone_easein

      Length of first Bézier Handle (for B-Bones only)

      :type: float in [-inf, inf], default 1.0

   .. attribute:: bbone_easeout

      Length of second Bézier Handle (for B-Bones only)

      :type: float in [-inf, inf], default 1.0

   .. attribute:: bbone_handle_type_end

      Selects how the end handle of the B-Bone is computed

      * ``AUTO``
        Automatic -- Use connected parent and children to compute the handle.
      * ``ABSOLUTE``
        Absolute -- Use the position of the specified bone to compute the handle.
      * ``RELATIVE``
        Relative -- Use the offset of the specified bone from rest pose to compute the handle.
      * ``TANGENT``
        Tangent -- Use the orientation of the specified bone to compute the handle, ignoring the location.

      :type: enum in [``'AUTO'``, ``'ABSOLUTE'``, ``'RELATIVE'``, ``'TANGENT'``], default ``'AUTO'``

   .. attribute:: bbone_handle_type_start

      Selects how the start handle of the B-Bone is computed

      * ``AUTO``
        Automatic -- Use connected parent and children to compute the handle.
      * ``ABSOLUTE``
        Absolute -- Use the position of the specified bone to compute the handle.
      * ``RELATIVE``
        Relative -- Use the offset of the specified bone from rest pose to compute the handle.
      * ``TANGENT``
        Tangent -- Use the orientation of the specified bone to compute the handle, ignoring the location.

      :type: enum in [``'AUTO'``, ``'ABSOLUTE'``, ``'RELATIVE'``, ``'TANGENT'``], default ``'AUTO'``

   .. attribute:: bbone_handle_use_ease_end

      Multiply the B-Bone Ease Out channel by the local Y scale value of the end handle. This is done after the Scale Easing option and isn't affected by it.

      :type: boolean, default False

   .. attribute:: bbone_handle_use_ease_start

      Multiply the B-Bone Ease In channel by the local Y scale value of the start handle. This is done after the Scale Easing option and isn't affected by it.

      :type: boolean, default False

   .. attribute:: bbone_handle_use_scale_end

      Multiply B-Bone Scale Out channels by the local scale values of the end handle. This is done after the Scale Easing option and isn't affected by it.

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: bbone_handle_use_scale_start

      Multiply B-Bone Scale In channels by the local scale values of the start handle. This is done after the Scale Easing option and isn't affected by it.

      :type: boolean array of 3 items, default (False, False, False)

   .. attribute:: bbone_mapping_mode

      Selects how the vertices are mapped to B-Bone segments based on their position

      * ``STRAIGHT``
        Straight -- Fast mapping that is good for most situations, but ignores the rest pose curvature of the B-Bone.
      * ``CURVED``
        Curved -- Slower mapping that gives better deformation for B-Bones that are sharply curved in rest pose.

      :type: enum in [``'STRAIGHT'``, ``'CURVED'``], default ``'STRAIGHT'``

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

   .. attribute:: bbone_segments

      Number of subdivisions of bone (for B-Bones only)

      :type: int in [1, 32], default 0

   .. attribute:: bbone_x

      B-Bone X size

      :type: float in [-inf, inf], default 0.0

   .. attribute:: bbone_z

      B-Bone Z size

      :type: float in [-inf, inf], default 0.0

   .. data:: children

      Bones which are children of this bone

      :type: :class:`bpy_prop_collection` of :class:`Bone`, (readonly)

   .. data:: collections

      Bone Collections that contain this bone

      :type: :class:`BoneCollectionMemberships` :class:`bpy_prop_collection` of :class:`BoneCollection`, (readonly)

   .. data:: color

      :type: :class:`BoneColor`, (readonly)

   .. attribute:: display_type

      * ``ARMATURE_DEFINED``
        Armature Defined -- Use display mode from armature (default).
      * ``OCTAHEDRAL``
        Octahedral -- Display bones as octahedral shape.
      * ``STICK``
        Stick -- Display bones as simple 2D lines with dots.
      * ``BBONE``
        B-Bone -- Display bones as boxes, showing subdivision and B-Splines.
      * ``ENVELOPE``
        Envelope -- Display bones as extruded spheres, showing deformation influence volume.
      * ``WIRE``
        Wire -- Display bones as thin wires, showing subdivision and B-Splines.

      :type: enum in [``'ARMATURE_DEFINED'``, ``'OCTAHEDRAL'``, ``'STICK'``, ``'BBONE'``, ``'ENVELOPE'``, ``'WIRE'``], default ``'OCTAHEDRAL'``

   .. attribute:: envelope_distance

      Bone deformation distance (for Envelope deform only)

      :type: float in [0, 1000], default 0.0

   .. attribute:: envelope_weight

      Bone deformation weight (for Envelope deform only)

      :type: float in [0, 1000], default 0.0

   .. data:: head

      Location of head end of the bone relative to its parent

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. data:: head_local

      Location of head end of the bone relative to armature

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: head_radius

      Radius of head of bone (for Envelope deform only)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: hide

      Bone is not visible when it is not in Edit Mode (i.e. in Object or Pose Modes)

      :type: boolean, default False

   .. attribute:: hide_select

      Bone is able to be selected

      :type: boolean, default False

   .. attribute:: inherit_scale

      Specifies how the bone inherits scaling from the parent bone

      * ``FULL``
        Full -- Inherit all effects of parent scaling.
      * ``FIX_SHEAR``
        Fix Shear -- Inherit scaling, but remove shearing of the child in the rest orientation.
      * ``ALIGNED``
        Aligned -- Rotate non-uniform parent scaling to align with the child, applying parent X scale to child X axis, and so forth.
      * ``AVERAGE``
        Average -- Inherit uniform scaling representing the overall change in the volume of the parent.
      * ``NONE``
        None -- Completely ignore parent scaling.
      * ``NONE_LEGACY``
        None (Legacy) -- Ignore parent scaling without compensating for parent shear. Replicates the effect of disabling the original Inherit Scale checkbox..

      :type: enum in [``'FULL'``, ``'FIX_SHEAR'``, ``'ALIGNED'``, ``'AVERAGE'``, ``'NONE'``, ``'NONE_LEGACY'``], default ``'FULL'``

   .. data:: length

      Length of the bone

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. data:: matrix

      3×3 bone matrix

      :type: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], default ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), (readonly)

   .. data:: matrix_local

      4×4 bone matrix relative to armature

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

   .. attribute:: name

      :type: string, default "", (never None)

   .. data:: parent

      Parent bone (in same Armature)

      :type: :class:`Bone`, (readonly)

   .. attribute:: select

      :type: boolean, default False

   .. attribute:: select_head

      :type: boolean, default False

   .. attribute:: select_tail

      :type: boolean, default False

   .. attribute:: show_wire

      Bone is always displayed in wireframe regardless of viewport shading mode (useful for non-obstructive custom bone shapes)

      :type: boolean, default False

   .. data:: tail

      Location of tail end of the bone relative to its parent

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. data:: tail_local

      Location of tail end of the bone relative to armature

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: tail_radius

      Radius of tail of bone (for Envelope deform only)

      :type: float in [-inf, inf], default 0.0

   .. data:: use_connect

      When bone has a parent, bone's head is stuck to the parent's tail

      :type: boolean, default False, (readonly)

   .. attribute:: use_cyclic_offset

      When bone doesn't have a parent, it receives cyclic offset effects (Deprecated)

      :type: boolean, default False

   .. attribute:: use_deform

      Enable Bone to deform geometry

      :type: boolean, default False

   .. attribute:: use_endroll_as_inroll

      Add Roll Out of the Start Handle bone to the Roll In value

      :type: boolean, default False

   .. attribute:: use_envelope_multiply

      When deforming bone, multiply effects of Vertex Group weights with Envelope influence

      :type: boolean, default False

   .. attribute:: use_inherit_rotation

      Bone inherits rotation or scale from parent bone

      :type: boolean, default False

   .. attribute:: use_local_location

      Bone location is set in local space

      :type: boolean, default False

   .. attribute:: use_relative_parent

      Object children will use relative transform, like deform

      :type: boolean, default False

   .. attribute:: use_scale_easing

      Multiply the final easing values by the Scale In/Out Y factors

      :type: boolean, default False

   .. data:: basename

      The name of this bone before any '.' character

      (readonly)

   .. data:: center

      The midpoint between the head and the tail.

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

   .. method:: convert_local_to_pose(matrix, matrix_local, *, parent_matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), parent_matrix_local=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), invert=False)

      Transform a matrix from Local to Pose space (or back), taking into account options like Inherit Scale and Local Location. Unlike Object.convert_space, this uses custom rest and pose matrices provided by the caller. If the parent matrices are omitted, the bone is assumed to have no parent.

      :arg matrix: The matrix to transform
      :type matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]
      :arg matrix_local: The custom rest matrix of this bone (Bone.matrix_local)
      :type matrix_local: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]
      :arg parent_matrix: The custom pose matrix of the parent bone (PoseBone.matrix)
      :type parent_matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], (optional)
      :arg parent_matrix_local: The custom rest matrix of the parent bone (Bone.matrix_local)
      :type parent_matrix_local: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], (optional)
      :arg invert: Convert from Pose to Local space
      :type invert: boolean, (optional)
      :return: The transformed matrix
      :rtype: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]

      This method enables conversions between Local and Pose space for bones in
      the middle of updating the armature without having to update dependencies
      after each change, by manually carrying updated matrices in a recursive walk.

      .. literalinclude:: ..\examples\bpy.types.Bone.convert_local_to_pose.py
         :lines: 8-


   .. classmethod:: MatrixFromAxisRoll(axis, roll)

      Convert the axis + roll representation to a matrix

      :arg axis: The main axis of the bone (tail - head)
      :type axis: :class:`mathutils.Vector` of 3 items in [-inf, inf], (never None)
      :arg roll: The roll of the bone
      :type roll: float in [-inf, inf]
      :return: The resulting orientation matrix
      :rtype: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf]

   .. classmethod:: AxisRollFromMatrix(matrix, *, axis=(0.0, 0.0, 0.0))

      Convert a rotational matrix to the axis + roll representation. Note that the resulting value of the roll may not be as expected if the matrix has shear or negative determinant.

      :arg matrix: The orientation matrix of the bone
      :type matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (never None)
      :arg axis: The optional override for the axis (finds closest approximation for the matrix)
      :type axis: float array of 3 items in [-inf, inf], (optional)
      :return:
         `result_axis`, The main axis of the bone, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `result_roll`, The roll of the bone, float in [-inf, inf]

      :rtype: (:class:`mathutils.Vector` of 3 items in [-inf, inf], float in [-inf, inf])

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

   * :mod:`bpy.context.active_bone`
   * :mod:`bpy.context.bone`
   * :class:`Armature.bones`
   * :class:`ArmatureBones.active`
   * :class:`Bone.bbone_custom_handle_end`
   * :class:`Bone.bbone_custom_handle_start`
   * :class:`Bone.children`
   * :class:`Bone.parent`
   * :class:`BoneCollection.bones`
   * :class:`PoseBone.bone`

