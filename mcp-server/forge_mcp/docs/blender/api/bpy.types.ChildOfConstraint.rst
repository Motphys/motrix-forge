ChildOfConstraint(Constraint)
=============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: ChildOfConstraint(Constraint)

   Create constraint-based parent-child relationship

   .. attribute:: inverse_matrix

      Transformation matrix to apply before

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: set_inverse_pending

      Set to true to request recalculation of the inverse matrix

      :type: boolean, default False

   .. attribute:: subtarget

      Armature bone, mesh or lattice vertex group, ...

      :type: string, default "", (never None)

   .. attribute:: target

      Target object

      :type: :class:`Object`

   .. attribute:: use_location_x

      Use X Location of Parent

      :type: boolean, default False

   .. attribute:: use_location_y

      Use Y Location of Parent

      :type: boolean, default False

   .. attribute:: use_location_z

      Use Z Location of Parent

      :type: boolean, default False

   .. attribute:: use_rotation_x

      Use X Rotation of Parent

      :type: boolean, default False

   .. attribute:: use_rotation_y

      Use Y Rotation of Parent

      :type: boolean, default False

   .. attribute:: use_rotation_z

      Use Z Rotation of Parent

      :type: boolean, default False

   .. attribute:: use_scale_x

      Use X Scale of Parent

      :type: boolean, default False

   .. attribute:: use_scale_y

      Use Y Scale of Parent

      :type: boolean, default False

   .. attribute:: use_scale_z

      Use Z Scale of Parent

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

