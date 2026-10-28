CompositorNodeColorBalance(CompositorNode)
==========================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`CompositorNode`

.. class:: CompositorNodeColorBalance(CompositorNode)

   Adjust color and values

   .. attribute:: correction_method

      * ``LIFT_GAMMA_GAIN``
        Lift/Gamma/Gain.
      * ``OFFSET_POWER_SLOPE``
        Offset/Power/Slope (ASC-CDL) -- ASC-CDL standard color correction.
      * ``WHITEPOINT``
        White Point -- Chromatic adaption from a different white point.

      :type: enum in [``'LIFT_GAMMA_GAIN'``, ``'OFFSET_POWER_SLOPE'``, ``'WHITEPOINT'``], default ``'LIFT_GAMMA_GAIN'``

   .. attribute:: gain

      Correction for highlights. (Deprecated: Use Gain input instead.)

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: gamma

      Correction for midtones. (Deprecated: Use Gamma input instead.)

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: input_temperature

      Color temperature of the input's white point. (Deprecated: Use Input Temperature input instead.)

      :type: float in [1800, 100000], default 6500.0

   .. attribute:: input_tint

      Color tint of the input's white point (the default of 10 matches daylight). (Deprecated: Use Input Tint input instead.)

      :type: float in [-500, 500], default 10.0

   .. attribute:: input_whitepoint

      The color which gets mapped to white (automatically converted to/from temperature and tint)

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: lift

      Correction for shadows. (Deprecated: Use Lift input instead.)

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: offset

      Correction for entire tonal range. (Deprecated: Use Offset input instead.)

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: offset_basis

      Support negative color by using this as the RGB basis. (Deprecated: Use Offset Basis input instead.)

      :type: float in [-inf, inf], default 0.0

   .. attribute:: output_temperature

      Color temperature of the output's white point. (Deprecated: Use Output Temperature input instead.)

      :type: float in [1800, 100000], default 6500.0

   .. attribute:: output_tint

      Color tint of the output's white point (the default of 10 matches daylight). (Deprecated: Use Output Tint input instead.)

      :type: float in [-500, 500], default 10.0

   .. attribute:: output_whitepoint

      The color which gets white gets mapped to (automatically converted to/from temperature and tint)

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: power

      Correction for midtones. (Deprecated: Use Power input instead.)

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. attribute:: slope

      Correction for highlights. (Deprecated: Use Slope input instead.)

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (1.0, 1.0, 1.0)

   .. classmethod:: is_registered_node_type()

      True if a registered node type

      :return: Result
      :rtype: boolean

   .. classmethod:: input_template(index)

      Input socket template

      :arg index: Index
      :type index: int in [0, inf]
      :return: result
      :rtype: :class:`NodeInternalSocketTemplate`

   .. classmethod:: output_template(index)

      Output socket template

      :arg index: Index
      :type index: int in [0, inf]
      :return: result
      :rtype: :class:`NodeInternalSocketTemplate`

   .. method:: update()

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
   * :class:`Node.type`
   * :class:`Node.location`
   * :class:`Node.location_absolute`
   * :class:`Node.width`
   * :class:`Node.height`
   * :class:`Node.dimensions`
   * :class:`Node.name`
   * :class:`Node.label`
   * :class:`Node.inputs`
   * :class:`Node.outputs`
   * :class:`Node.internal_links`
   * :class:`Node.parent`
   * :class:`Node.warning_propagation`
   * :class:`Node.use_custom_color`
   * :class:`Node.color`
   * :class:`Node.color_tag`
   * :class:`Node.select`
   * :class:`Node.show_options`
   * :class:`Node.show_preview`
   * :class:`Node.hide`
   * :class:`Node.mute`
   * :class:`Node.show_texture`
   * :class:`Node.bl_idname`
   * :class:`Node.bl_label`
   * :class:`Node.bl_description`
   * :class:`Node.bl_icon`
   * :class:`Node.bl_static_type`
   * :class:`Node.bl_width_default`
   * :class:`Node.bl_width_min`
   * :class:`Node.bl_width_max`
   * :class:`Node.bl_height_default`
   * :class:`Node.bl_height_min`
   * :class:`Node.bl_height_max`

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
   * :class:`Node.socket_value_update`
   * :class:`Node.is_registered_node_type`
   * :class:`Node.poll`
   * :class:`Node.poll_instance`
   * :class:`Node.update`
   * :class:`Node.insert_link`
   * :class:`Node.init`
   * :class:`Node.copy`
   * :class:`Node.free`
   * :class:`Node.draw_buttons`
   * :class:`Node.draw_buttons_ext`
   * :class:`Node.draw_label`
   * :class:`Node.debug_zone_body_lazy_function_graph`
   * :class:`Node.debug_zone_lazy_function_graph`
   * :class:`Node.poll`
   * :class:`Node.bl_rna_get_subclass`
   * :class:`Node.bl_rna_get_subclass_py`
   * :class:`NodeInternal.poll`
   * :class:`NodeInternal.poll_instance`
   * :class:`NodeInternal.update`
   * :class:`NodeInternal.draw_buttons`
   * :class:`NodeInternal.draw_buttons_ext`
   * :class:`NodeInternal.bl_rna_get_subclass`
   * :class:`NodeInternal.bl_rna_get_subclass_py`
   * :class:`CompositorNode.tag_need_exec`
   * :class:`CompositorNode.poll`
   * :class:`CompositorNode.update`
   * :class:`CompositorNode.bl_rna_get_subclass`
   * :class:`CompositorNode.bl_rna_get_subclass_py`

