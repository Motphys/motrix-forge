CompositorNodeColorCorrection(CompositorNode)
=============================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`CompositorNode`

.. class:: CompositorNodeColorCorrection(CompositorNode)

   Adjust the color of an image, separately in several tonal ranges (highlights, midtones and shadows)

   .. attribute:: blue

      Blue channel active. (Deprecated: Use Apply On Blue input instead.)

      :type: boolean, default True

   .. attribute:: green

      Green channel active. (Deprecated: Use Apply On Green input instead.)

      :type: boolean, default True

   .. attribute:: highlights_contrast

      Highlights contrast. (Deprecated: Use Highlights Contrast input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: highlights_gain

      Highlights gain. (Deprecated: Use Highlights Gain input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: highlights_gamma

      Highlights gamma. (Deprecated: Use Highlights Gamma input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: highlights_lift

      Highlights lift. (Deprecated: Use Highlights Lift input instead.)

      :type: float in [-1, 1], default 0.0

   .. attribute:: highlights_saturation

      Highlights saturation. (Deprecated: Use Highlights Saturation input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: master_contrast

      Master contrast. (Deprecated: Use Master Contrast input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: master_gain

      Master gain. (Deprecated: Use Master Gain input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: master_gamma

      Master gamma. (Deprecated: Use Master Gamma input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: master_lift

      Master lift. (Deprecated: Use Master Lift input instead.)

      :type: float in [-1, 1], default 0.0

   .. attribute:: master_saturation

      Master saturation. (Deprecated: Use Master Saturation input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_contrast

      Midtones contrast. (Deprecated: Use Midtones Contrast input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_end

      End of midtones. (Deprecated: Use Midtones End input instead.)

      :type: float in [0, 1], default 0.7

   .. attribute:: midtones_gain

      Midtones gain. (Deprecated: Use Midtones Gain input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_gamma

      Midtones gamma. (Deprecated: Use Midtones Gamma input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_lift

      Midtones lift. (Deprecated: Use Midtones Lift input instead.)

      :type: float in [-1, 1], default 0.0

   .. attribute:: midtones_saturation

      Midtones saturation. (Deprecated: Use Midtones Saturation input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: midtones_start

      Start of midtones. (Deprecated: Use Midtones Start input instead.)

      :type: float in [0, 1], default 0.2

   .. attribute:: red

      Red channel active. (Deprecated: Use Apply On Red input instead.)

      :type: boolean, default True

   .. attribute:: shadows_contrast

      Shadows contrast. (Deprecated: Use Shadows Contrast input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: shadows_gain

      Shadows gain. (Deprecated: Use Shadows Gain input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: shadows_gamma

      Shadows gamma. (Deprecated: Use Shadows Gamma input instead.)

      :type: float in [0, 4], default 1.0

   .. attribute:: shadows_lift

      Shadows lift. (Deprecated: Use Shadows Lift input instead.)

      :type: float in [-1, 1], default 0.0

   .. attribute:: shadows_saturation

      Shadows saturation. (Deprecated: Use Shadows Saturation input instead.)

      :type: float in [0, 4], default 1.0

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

