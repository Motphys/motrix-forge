GreasePencilLengthModifier(Modifier)
====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: GreasePencilLengthModifier(Modifier)

   Stretch or shrink strokes

   .. attribute:: end_factor

      Added length to the end of each stroke relative to its length

      :type: float in [-inf, inf], default 0.1

   .. attribute:: end_length

      Absolute added length to the end of each stroke

      :type: float in [-inf, inf], default 0.1

   .. attribute:: invert_curvature

      Invert the curvature of the stroke's extension

      :type: boolean, default False

   .. attribute:: invert_layer_filter

      Invert layer filter

      :type: boolean, default False

   .. attribute:: invert_layer_pass_filter

      Invert layer pass filter

      :type: boolean, default False

   .. attribute:: invert_material_filter

      Invert material filter

      :type: boolean, default False

   .. attribute:: invert_material_pass_filter

      Invert material pass filter

      :type: boolean, default False

   .. attribute:: layer_pass_filter

      Layer pass filter

      :type: int in [0, 100], default 0

   .. attribute:: material_filter

      Material used for filtering

      :type: :class:`Material`

   .. attribute:: material_pass_filter

      Material pass

      :type: int in [0, 100], default 0

   .. attribute:: max_angle

      Ignore points on the stroke that deviate from their neighbors by more than this angle when determining the extrapolation shape

      :type: float in [0, 3.14159], default 2.96706

   .. attribute:: mode

      Mode to define length

      * ``RELATIVE``
        Relative -- Length in ratio to the stroke's length.
      * ``ABSOLUTE``
        Absolute -- Length in geometry space.

      :type: enum in [``'RELATIVE'``, ``'ABSOLUTE'``], default ``'RELATIVE'``

   .. attribute:: open_curvature_panel

      :type: boolean, default False

   .. attribute:: open_influence_panel

      :type: boolean, default False

   .. attribute:: open_random_panel

      :type: boolean, default False

   .. attribute:: overshoot_factor

      Defines what portion of the stroke is used for the calculation of the extension

      :type: float in [0, 1], default 0.1

   .. attribute:: point_density

      Multiplied by Start/End for the total added point count

      :type: float in [0.1, 1000], default 30.0

   .. attribute:: random_end_factor

      Size of random length added to the end of each stroke

      :type: float in [-inf, inf], default 0.0

   .. attribute:: random_offset

      Smoothly offset each stroke's random value

      :type: float in [-inf, inf], default 0.0

   .. attribute:: random_start_factor

      Size of random length added to the start of each stroke

      :type: float in [-inf, inf], default 0.0

   .. attribute:: seed

      Random seed

      :type: int in [0, inf], default 0

   .. attribute:: segment_influence

      Factor to determine how much the length of the individual segments should influence the final computed curvature. Higher factors makes small segments influence the overall curvature less.

      :type: float in [-2, 3], default 0.0

   .. attribute:: start_factor

      Added length to the start of each stroke relative to its length

      :type: float in [-inf, inf], default 0.1

   .. attribute:: start_length

      Absolute added length to the start of each stroke

      :type: float in [-inf, inf], default 0.1

   .. attribute:: step

      Number of frames between randomization steps

      :type: int in [1, 100], default 4

   .. attribute:: tree_node_filter

      Layer name

      :type: string, default "", (never None)

   .. attribute:: use_curvature

      Follow the curvature of the stroke

      :type: boolean, default True

   .. attribute:: use_layer_group_filter

      Filter by layer group name

      :type: boolean, default False

   .. attribute:: use_layer_pass_filter

      Use layer pass filter

      :type: boolean, default False

   .. attribute:: use_material_pass_filter

      Use material pass filter

      :type: boolean, default False

   .. attribute:: use_random

      Use random values over time

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.is_active`
   * :class:`Modifier.use_pin_to_last`
   * :class:`Modifier.is_override_data`
   * :class:`Modifier.use_apply_on_spline`
   * :class:`Modifier.execution_time`
   * :class:`Modifier.persistent_uid`

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
   * :class:`Modifier.bl_rna_get_subclass`
   * :class:`Modifier.bl_rna_get_subclass_py`

