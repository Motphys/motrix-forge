Pose(bpy_struct)
================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Pose(bpy_struct)

   A collection of pose channels, including settings for animating bones

   .. data:: animation_visualization

      Animation data for this data-block

      :type: :class:`AnimViz`, (readonly, never None)

   .. data:: bones

      Individual pose bones for the armature

      :type: :class:`bpy_prop_collection` of :class:`PoseBone`, (readonly)

   .. data:: ik_param

      Parameters for IK solver

      :type: :class:`IKParam`, (readonly)

   .. attribute:: ik_solver

      Selection of IK solver for IK chain

      * ``LEGACY``
        Standard -- Original IK solver.
      * ``ITASC``
        iTaSC -- Multi constraint, stateful IK solver.

      :type: enum in [``'LEGACY'``, ``'ITASC'``], default ``'LEGACY'``

   .. attribute:: use_auto_ik

      Add temporary IK constraints while grabbing bones in Pose Mode

      :type: boolean, default False

   .. attribute:: use_mirror_relative

      Apply relative transformations in X-mirror mode (not supported with Auto IK)

      :type: boolean, default False

   .. attribute:: use_mirror_x

      Apply changes to matching bone on opposite side of X-Axis

      :type: boolean, default False

   .. classmethod:: apply_pose_from_action(action, *, evaluation_time=0.0)

      Apply the given action to this pose by evaluating it at a specific time. Only updates the pose of selected bones, or all bones if none are selected.

      :arg action: Action, The Action containing the pose
      :type action: :class:`Action`
      :arg evaluation_time: Evaluation Time, Time at which the given action is evaluated to obtain the pose
      :type evaluation_time: float in [-inf, inf], (optional)

   .. classmethod:: blend_pose_from_action(action, *, blend_factor=1.0, evaluation_time=0.0)

      Blend the given action into this pose by evaluating it at a specific time. Only updates the pose of selected bones, or all bones if none are selected.

      :arg action: Action, The Action containing the pose
      :type action: :class:`Action`
      :arg blend_factor: Blend Factor, How much the given Action affects the final pose
      :type blend_factor: float in [0, 1], (optional)
      :arg evaluation_time: Evaluation Time, Time at which the given action is evaluated to obtain the pose
      :type evaluation_time: float in [-inf, inf], (optional)

   .. classmethod:: backup_create(action)

      Create a backup of the current pose. Only those bones that are animated in the Action are backed up. The object owns the backup, and each object can have only one backup at a time. When you no longer need it, it must be freed use `backup_clear()`.

      :arg action: Action, An Action with animation data for the bones. Only the animated bones will be included in the backup.
      :type action: :class:`Action`

   .. classmethod:: backup_restore()

      Restore the previously made pose backup. This can be called multiple times. See `Pose.backup_create()` for more info.

      :return: `True` when the backup was restored, `False` if there was no backup to restore
      :rtype: boolean

   .. classmethod:: backup_clear()

      Free a previously made pose backup. See `Pose.backup_create()` for more info.


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

   * :class:`Object.pose`

