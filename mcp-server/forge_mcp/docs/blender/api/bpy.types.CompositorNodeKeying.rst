CompositorNodeKeying(CompositorNode)
====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`CompositorNode`

.. class:: CompositorNodeKeying(CompositorNode)

   Perform both chroma keying (to remove the backdrop) and despill (to correct color cast from the backdrop)

   .. attribute:: blur_post

      Matte blur size which applies after clipping and dilate/eroding. (Deprecated: Use Postprocess Blur Size input instead.)

      :type: int in [0, 2048], default 0

   .. attribute:: blur_pre

      Chroma pre-blur size which applies before running keyer. (Deprecated: Use Preprocess Blur Size input instead.)

      :type: int in [0, 2048], default 0

   .. attribute:: clip_black

      Value of non-scaled matte pixel which considers as fully background pixel. (Deprecated: Use Black Level input instead.)

      :type: float in [0, 1], default 0.0

   .. attribute:: clip_white

      Value of non-scaled matte pixel which considers as fully foreground pixel. (Deprecated: Use White Level input instead.)

      :type: float in [0, 1], default 0.0

   .. attribute:: despill_balance

      Balance between non-key colors used to detect amount of key color to be removed. (Deprecated: Use Despill Balance input instead.)

      :type: float in [0, 1], default 0.0

   .. attribute:: despill_factor

      Factor of despilling screen color from image. (Deprecated: Use Despill Strength input instead.)

      :type: float in [0, 1], default 0.0

   .. attribute:: dilate_distance

      Distance to grow/shrink the matte. (Deprecated: Use Postprocess Dilate Size input instead.)

      :type: int in [-100, 100], default 0

   .. attribute:: edge_kernel_radius

      Radius of kernel used to detect whether pixel belongs to edge. (Deprecated: Use Edge Search Size input instead.)

      :type: int in [0, 100], default 0

   .. attribute:: edge_kernel_tolerance

      Tolerance to pixels inside kernel which are treating as belonging to the same plane. (Deprecated: Use Edge Tolerance input instead.)

      :type: float in [0, 1], default 0.0

   .. attribute:: feather_distance

      Distance to grow/shrink the feather. (Deprecated: Use Postprocess Feather Size input instead.)

      :type: int in [-100, 100], default 0

   .. attribute:: feather_falloff

      Falloff type of the feather

      :type: enum in :ref:`rna_enum_proportional_falloff_curve_only_items`, default ``'SMOOTH'``

   .. attribute:: screen_balance

      Balance between two non-primary channels primary channel is comparing against. (Deprecated: Use Key Balance input instead.)

      :type: float in [0, 1], default 0.0

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

