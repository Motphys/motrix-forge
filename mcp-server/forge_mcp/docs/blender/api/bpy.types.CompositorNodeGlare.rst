CompositorNodeGlare(CompositorNode)
===================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`CompositorNode`

.. class:: CompositorNodeGlare(CompositorNode)

   Add lens flares, fog and glows around bright parts of the image

   .. attribute:: angle_offset

      Streak angle offset. (Deprecated: Use Streaks Angle input instead)

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: color_modulation

      Amount of Color Modulation, modulates colors of streaks and ghosts for a spectral dispersion effect. (Deprecated: Use Color Modulation input instead)

      :type: float in [0, 1], default 0.0

   .. attribute:: fade

      Streak fade-out factor. (Deprecated: Use Fade input instead)

      :type: float in [0.75, 1], default 0.0

   .. attribute:: glare_type

      :type: enum in [``'BLOOM'``, ``'GHOSTS'``, ``'STREAKS'``, ``'FOG_GLOW'``, ``'SIMPLE_STAR'``], default ``'SIMPLE_STAR'``

   .. attribute:: iterations

      (Deprecated: Use Iterations input instead)

      :type: int in [2, 5], default 0

   .. attribute:: mix

      1 is original image only, 0 is exact 50/50 mix, 1 is processed image only. (Deprecated: Use Strength input instead)

      :type: float in [-1, 1], default 0.0

   .. attribute:: quality

      If not set to high quality, the effect will be applied to a low-res copy of the source image

      :type: enum in [``'HIGH'``, ``'MEDIUM'``, ``'LOW'``], default ``'HIGH'``

   .. attribute:: size

      Glow/glare size (not actual size; relative to initial size of bright area of pixels). (Deprecated: Use Size input instead)

      :type: int in [1, 9], default 0

   .. attribute:: streaks

      Total number of streaks. (Deprecated: Use Streaks input instead)

      :type: int in [1, 16], default 0

   .. attribute:: threshold

      The glare filter will only be applied to pixels brighter than this value. (Deprecated: Use Threshold input instead)

      :type: float in [0, inf], default 0.0

   .. attribute:: use_rotate_45

      Simple star filter: add 45 degree rotation offset. (Deprecated: Use Diagonal input instead)

      :type: boolean, default False

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

