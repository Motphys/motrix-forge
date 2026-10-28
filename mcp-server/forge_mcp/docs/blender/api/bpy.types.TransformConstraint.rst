TransformConstraint(Constraint)
===============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Constraint`

.. class:: TransformConstraint(Constraint)

   Map transformations of the target to the object

   .. attribute:: from_max_x

      Top range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_x_rot

      Top range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_x_scale

      Top range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_y

      Top range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_y_rot

      Top range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_y_scale

      Top range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_z

      Top range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_z_rot

      Top range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_max_z_scale

      Top range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_x

      Bottom range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_x_rot

      Bottom range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_x_scale

      Bottom range of X axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_y

      Bottom range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_y_rot

      Bottom range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_y_scale

      Bottom range of Y axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_z

      Bottom range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_z_rot

      Bottom range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_min_z_scale

      Bottom range of Z axis source motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: from_rotation_mode

      Specify the type of rotation channels to use

      :type: enum in :ref:`rna_enum_driver_target_rotation_mode_items`, default ``'AUTO'``

   .. attribute:: map_from

      The transformation type to use from the target

      :type: enum in [``'LOCATION'``, ``'ROTATION'``, ``'SCALE'``], default ``'LOCATION'``

   .. attribute:: map_to

      The transformation type to affect on the constrained object

      :type: enum in [``'LOCATION'``, ``'ROTATION'``, ``'SCALE'``], default ``'LOCATION'``

   .. attribute:: map_to_x_from

      The source axis constrained object's X axis uses

      :type: enum in :ref:`rna_enum_axis_xyz_items`, default ``'X'``

   .. attribute:: map_to_y_from

      The source axis constrained object's Y axis uses

      :type: enum in :ref:`rna_enum_axis_xyz_items`, default ``'X'``

   .. attribute:: map_to_z_from

      The source axis constrained object's Z axis uses

      :type: enum in :ref:`rna_enum_axis_xyz_items`, default ``'X'``

   .. attribute:: mix_mode

      Specify how to combine the new location with original

      * ``REPLACE``
        Replace -- Replace component values.
      * ``ADD``
        Add -- Add component values together.

      :type: enum in [``'REPLACE'``, ``'ADD'``], default ``'ADD'``

   .. attribute:: mix_mode_rot

      Specify how to combine the new rotation with original

      * ``REPLACE``
        Replace -- Replace component values.
      * ``ADD``
        Add -- Add component values together.
      * ``BEFORE``
        Before Original -- Apply new rotation before original, as if it was on a parent.
      * ``AFTER``
        After Original -- Apply new rotation after original, as if it was on a child.

      :type: enum in [``'REPLACE'``, ``'ADD'``, ``'BEFORE'``, ``'AFTER'``], default ``'ADD'``

   .. attribute:: mix_mode_scale

      Specify how to combine the new scale with original

      * ``REPLACE``
        Replace -- Replace component values.
      * ``MULTIPLY``
        Multiply -- Multiply component values together.

      :type: enum in [``'REPLACE'``, ``'MULTIPLY'``], default ``'REPLACE'``

   .. attribute:: subtarget

      Armature bone, mesh or lattice vertex group, ...

      :type: string, default "", (never None)

   .. attribute:: target

      Target object

      :type: :class:`Object`

   .. attribute:: to_euler_order

      Explicitly specify the output euler rotation order

      * ``AUTO``
        Default -- Euler using the default rotation order.
      * ``XYZ``
        XYZ Euler -- Euler using the XYZ rotation order.
      * ``XZY``
        XZY Euler -- Euler using the XZY rotation order.
      * ``YXZ``
        YXZ Euler -- Euler using the YXZ rotation order.
      * ``YZX``
        YZX Euler -- Euler using the YZX rotation order.
      * ``ZXY``
        ZXY Euler -- Euler using the ZXY rotation order.
      * ``ZYX``
        ZYX Euler -- Euler using the ZYX rotation order.

      :type: enum in [``'AUTO'``, ``'XYZ'``, ``'XZY'``, ``'YXZ'``, ``'YZX'``, ``'ZXY'``, ``'ZYX'``], default ``'AUTO'``

   .. attribute:: to_max_x

      Top range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_x_rot

      Top range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_x_scale

      Top range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_y

      Top range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_y_rot

      Top range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_y_scale

      Top range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_z

      Top range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_z_rot

      Top range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_max_z_scale

      Top range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_x

      Bottom range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_x_rot

      Bottom range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_x_scale

      Bottom range of X axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_y

      Bottom range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_y_rot

      Bottom range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_y_scale

      Bottom range of Y axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_z

      Bottom range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_z_rot

      Bottom range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: to_min_z_scale

      Bottom range of Z axis destination motion

      :type: float in [-inf, inf], default 0.0

   .. attribute:: use_motion_extrapolate

      Extrapolate ranges

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

