EditBone(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: EditBone(bpy_struct)

   Edit mode bone in an armature data-block

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

      :type: :class:`EditBone`

   .. attribute:: bbone_custom_handle_start

      Bone that serves as the start handle for the B-Bone curve

      :type: :class:`EditBone`

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

   .. data:: collections

      Bone Collections that contain this bone

      :type: :class:`bpy_prop_collection` of :class:`BoneCollection`, (readonly)

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

   .. attribute:: head

      Location of head end of the bone

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: head_radius

      Radius of head of bone (for Envelope deform only)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: hide

      Bone is not visible when in Edit Mode

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

   .. attribute:: length

      Length of the bone. Changing moves the tail end.

      :type: float in [0, inf], default 0.0

   .. attribute:: lock

      Bone is not able to be transformed when in Edit Mode

      :type: boolean, default False

   .. attribute:: matrix

      Matrix combining location and rotation of the bone (head position, direction and roll), in armature space (does not include/support bone's length/size)

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: name

      :type: string, default "", (never None)

   .. attribute:: parent

      Parent edit bone (in same Armature)

      :type: :class:`EditBone`

   .. attribute:: roll

      Bone rotation around head-tail axis

      :type: float in [-inf, inf], default 0.0

   .. attribute:: select

      :type: boolean, default False

   .. attribute:: select_head

      :type: boolean, default False

   .. attribute:: select_tail

      :type: boolean, default False

   .. attribute:: show_wire

      Bone is always displayed in wireframe regardless of viewport shading mode (useful for non-obstructive custom bone shapes)

      :type: boolean, default False

   .. attribute:: tail

      Location of tail end of the bone

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: tail_radius

      Radius of tail of bone (for Envelope deform only)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: use_connect

      When bone has a parent, bone's head is stuck to the parent's tail

      :type: boolean, default False

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

   .. data:: children

      A list of all the bones children.
      
              .. note:: Takes ``O(len(bones))`` time.

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

   .. method:: align_roll(vector)

      Align the bone to a local-space roll so the Z axis points in the direction of the vector given

      :arg vector: Vector
      :type vector: :class:`mathutils.Vector` of 3 items in [-inf, inf]

   .. method:: align_orientation(other)

      Align this bone to another by moving its tail and settings its roll
      the length of the other bone is not used.

   .. method:: parent_index(parent_test)

      The same as 'bone in other_bone.parent_recursive'
      but saved generating a list.

   .. method:: transform(matrix, *, scale=True, roll=True)

      Transform the bones head, tail, roll and envelope
      (when the matrix has a scale component).
      
      :arg matrix: 3x3 or 4x4 transformation matrix.
      :type matrix: :class:`mathutils.Matrix`
      :arg scale: Scale the bone envelope by the matrix.
      :type scale: bool
      :arg roll:
      
         Correct the roll to point in the same relative
         direction to the head and tail.
      
      :type roll: bool

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
   * :mod:`bpy.context.edit_bone`
   * :mod:`bpy.context.editable_bones`
   * :mod:`bpy.context.selected_bones`
   * :mod:`bpy.context.selected_editable_bones`
   * :mod:`bpy.context.visible_bones`
   * :class:`Armature.edit_bones`
   * :class:`ArmatureEditBones.active`
   * :class:`ArmatureEditBones.new`
   * :class:`ArmatureEditBones.remove`
   * :class:`EditBone.bbone_custom_handle_end`
   * :class:`EditBone.bbone_custom_handle_start`
   * :class:`EditBone.parent`

