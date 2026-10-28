SplineIKConstraint(Constraint)
==============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: SplineIKConstraint(Constraint)

   Align 'n' bones along a curve

   .. attribute:: bulge

      Factor between volume variation and stretching

      :type: float in [0, 100], default 0.0

   .. attribute:: bulge_max

      Maximum volume stretching factor

      :type: float in [1, 100], default 0.0

   .. attribute:: bulge_min

      Minimum volume stretching factor

      :type: float in [0, 1], default 0.0

   .. attribute:: bulge_smooth

      Strength of volume stretching clamping

      :type: float in [0, 1], default 0.0

   .. attribute:: chain_count

      How many bones are included in the chain

      :type: int in [1, 255], default 0

   .. attribute:: joint_bindings

      (EXPERIENCED USERS ONLY) The relative positions of the joints along the chain, as percentages

      :type: float array of 32 items in [0, 1], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

   .. attribute:: target

      Curve that controls this relationship

      :type: :class:`Object`

   .. attribute:: use_bulge_max

      Use upper limit for volume variation

      :type: boolean, default False

   .. attribute:: use_bulge_min

      Use lower limit for volume variation

      :type: boolean, default False

   .. attribute:: use_chain_offset

      Offset the entire chain relative to the root joint

      :type: boolean, default False

   .. attribute:: use_curve_radius

      Average radius of the endpoints is used to tweak the X and Z Scaling of the bones, on top of XZ Scale mode

      :type: boolean, default False

   .. attribute:: use_even_divisions

      Ignore the relative lengths of the bones when fitting to the curve

      :type: boolean, default False

   .. attribute:: use_original_scale

      Apply volume preservation over the original scaling

      :type: boolean, default False

   .. attribute:: xz_scale_mode

      Method used for determining the scaling of the X and Z axes of the bones

      * ``NONE``
        None -- Don't scale the X and Z axes.
      * ``BONE_ORIGINAL``
        Bone Original -- Use the original scaling of the bones.
      * ``INVERSE_PRESERVE``
        Inverse Scale -- Scale of the X and Z axes is the inverse of the Y-Scale.
      * ``VOLUME_PRESERVE``
        Volume Preservation -- Scale of the X and Z axes are adjusted to preserve the volume of the bones.

      :type: enum in [``'NONE'``, ``'BONE_ORIGINAL'``, ``'INVERSE_PRESERVE'``, ``'VOLUME_PRESERVE'``], default ``'NONE'``

   .. attribute:: y_scale_mode

      Method used for determining the scaling of the Y axis of the bones, on top of the shape and scaling of the curve itself

      * ``NONE``
        None -- Don't scale in the Y axis.
      * ``FIT_CURVE``
        Fit Curve -- Scale the bones to fit the entire length of the curve.
      * ``BONE_ORIGINAL``
        Bone Original -- Use the original Y scale of the bone.

      :type: enum in [``'NONE'``, ``'FIT_CURVE'``, ``'BONE_ORIGINAL'``], default ``'NONE'``

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
   * :class:`Constraint.name`
   * :class:`Constraint.type`
   * :class:`Constraint.is_override_data`
   * :class:`Constraint.owner_space`
   * :class:`Constraint.target_space`
   * :class:`Constraint.space_object`
   * :class:`Constraint.space_subtarget`
   * :class:`Constraint.mute`
   * :class:`Constraint.enabled`
   * :class:`Constraint.show_expanded`
   * :class:`Constraint.is_valid`
   * :class:`Constraint.active`
   * :class:`Constraint.influence`
   * :class:`Constraint.error_location`
   * :class:`Constraint.error_rotation`

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
   * :class:`Constraint.bl_rna_get_subclass`
   * :class:`Constraint.bl_rna_get_subclass_py`

