PivotConstraint(Constraint)
===========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: PivotConstraint(Constraint)

   Rotate around a different point

   .. attribute:: head_tail

      Target along length of bone: Head is 0, Tail is 1

      :type: float in [0, 1], default 0.0

   .. attribute:: offset

      Offset of pivot from target (when set), or from owner's location (when Fixed Position is off), or the absolute pivot point

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: rotation_range

      Rotation range on which pivoting should occur

      * ``ALWAYS_ACTIVE``
        Always -- Use the pivot point in every rotation.
      * ``NX``
        -X Rotation -- Use the pivot point in the negative rotation range around the X-axis.
      * ``NY``
        -Y Rotation -- Use the pivot point in the negative rotation range around the Y-axis.
      * ``NZ``
        -Z Rotation -- Use the pivot point in the negative rotation range around the Z-axis.
      * ``X``
        X Rotation -- Use the pivot point in the positive rotation range around the X-axis.
      * ``Y``
        Y Rotation -- Use the pivot point in the positive rotation range around the Y-axis.
      * ``Z``
        Z Rotation -- Use the pivot point in the positive rotation range around the Z-axis.

      :type: enum in [``'ALWAYS_ACTIVE'``, ``'NX'``, ``'NY'``, ``'NZ'``, ``'X'``, ``'Y'``, ``'Z'``], default ``'NX'``

   .. attribute:: subtarget

      :type: string, default "", (never None)

   .. attribute:: target

      Target Object, defining the position of the pivot when defined

      :type: :class:`Object`

   .. attribute:: use_bbone_shape

      Follow shape of B-Bone segments when calculating Head/Tail position

      :type: boolean, default False

   .. attribute:: use_relative_location

      Offset will be an absolute point in space instead of relative to the target

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

