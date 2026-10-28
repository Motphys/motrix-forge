StretchToConstraint(Constraint)
===============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: StretchToConstraint(Constraint)

   Stretch to meet the target object

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

   .. attribute:: head_tail

      Target along length of bone: Head is 0, Tail is 1

      :type: float in [0, 1], default 0.0

   .. attribute:: keep_axis

      The rotation type and axis order to use

      * ``PLANE_X``
        XZ -- Rotate around local X, then Z.
      * ``PLANE_Z``
        ZX -- Rotate around local Z, then X.
      * ``SWING_Y``
        Swing -- Use the smallest single axis rotation, similar to Damped Track.

      :type: enum in [``'PLANE_X'``, ``'PLANE_Z'``, ``'SWING_Y'``], default ``'PLANE_X'``

   .. attribute:: rest_length

      Length at rest position

      :type: float in [0, 1000], default 0.0

   .. attribute:: subtarget

      Armature bone, mesh or lattice vertex group, ...

      :type: string, default "", (never None)

   .. attribute:: target

      Target object

      :type: :class:`Object`

   .. attribute:: use_bbone_shape

      Follow shape of B-Bone segments when calculating Head/Tail position

      :type: boolean, default False

   .. attribute:: use_bulge_max

      Use upper limit for volume variation

      :type: boolean, default False

   .. attribute:: use_bulge_min

      Use lower limit for volume variation

      :type: boolean, default False

   .. attribute:: volume

      Maintain the object's volume as it stretches

      :type: enum in [``'VOLUME_XZX'``, ``'VOLUME_X'``, ``'VOLUME_Z'``, ``'NO_VOLUME'``], default ``'VOLUME_XZX'``

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

