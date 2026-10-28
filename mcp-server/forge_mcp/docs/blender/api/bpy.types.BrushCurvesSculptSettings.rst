BrushCurvesSculptSettings(bpy_struct)
=====================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BrushCurvesSculptSettings(bpy_struct)


   .. attribute:: add_amount

      Number of curves added by the Add brush

      :type: int in [1, inf], default 0

   .. attribute:: curve_length

      Length of newly added curves when it is not interpolated from other curves

      :type: float in [0, inf], default 0.0

   .. data:: curve_parameter_falloff

      Falloff that is applied from the tip to the root of each curve

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: curve_radius

      Radius of newly added curves when it is not interpolated from other curves

      :type: float in [0, inf], default 0.01

   .. attribute:: density_add_attempts

      How many times the Density brush tries to add a new curve

      :type: int in [0, inf], default 0

   .. attribute:: density_mode

      Determines whether the brush adds or removes curves

      * ``AUTO``
        Auto -- Either add or remove curves depending on the minimum distance of the curves under the cursor.
      * ``ADD``
        Add -- Add new curves between existing curves, taking the minimum distance into account.
      * ``REMOVE``
        Remove -- Remove curves whose root points are too close.

      :type: enum in [``'AUTO'``, ``'ADD'``, ``'REMOVE'``], default ``'AUTO'``

   .. attribute:: minimum_distance

      Goal distance between curve roots for the Density brush

      :type: float in [0, inf], default 0.0

   .. attribute:: minimum_length

      Avoid shrinking curves shorter than this length

      :type: float in [0, inf], default 0.0

   .. attribute:: points_per_curve

      Number of control points in a newly added curve

      :type: int in [2, inf], default 0

   .. attribute:: use_length_interpolate

      Use length of the curves in close proximity

      :type: boolean, default False

   .. attribute:: use_point_count_interpolate

      Use the number of points from the curves in close proximity

      :type: boolean, default False

   .. attribute:: use_radius_interpolate

      Use radius of the curves in close proximity

      :type: boolean, default True

   .. attribute:: use_shape_interpolate

      Use shape of the curves in close proximity

      :type: boolean, default False

   .. attribute:: use_uniform_scale

      Grow or shrink curves by changing their size uniformly instead of using trimming or extrapolation

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

   * :class:`Brush.curves_sculpt_settings`

