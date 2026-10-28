GeometryNodeStringToCurves(GeometryNode)
========================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`GeometryNode`

.. class:: GeometryNodeStringToCurves(GeometryNode)

   Generate a paragraph of text with a specific font, using a curve instance to store each character

   .. attribute:: align_x

      Text horizontal alignment from the object or text box center

      * ``LEFT``
        Left -- Align text to the left.
      * ``CENTER``
        Center -- Align text to the center.
      * ``RIGHT``
        Right -- Align text to the right.
      * ``JUSTIFY``
        Justify -- Align text to the left and the right.
      * ``FLUSH``
        Flush -- Align text to the left and the right, with equal character spacing.

      :type: enum in [``'LEFT'``, ``'CENTER'``, ``'RIGHT'``, ``'JUSTIFY'``, ``'FLUSH'``], default ``'LEFT'``

   .. attribute:: align_y

      Text vertical alignment from the object center

      * ``TOP``
        Top -- Align text to the top.
      * ``TOP_BASELINE``
        Top Baseline -- Align text to the top line's baseline.
      * ``MIDDLE``
        Middle -- Align text to the middle.
      * ``BOTTOM_BASELINE``
        Bottom Baseline -- Align text to the bottom line's baseline.
      * ``BOTTOM``
        Bottom -- Align text to the bottom.

      :type: enum in [``'TOP'``, ``'TOP_BASELINE'``, ``'MIDDLE'``, ``'BOTTOM_BASELINE'``, ``'BOTTOM'``], default ``'TOP_BASELINE'``

   .. attribute:: font

      Font of the text. Falls back to the UI font by default.

      :type: :class:`VectorFont`

   .. attribute:: overflow

      Handle the text behavior when it doesn't fit in the text boxes

      * ``OVERFLOW``
        Overflow -- Let the text use more space than the specified height.
      * ``SCALE_TO_FIT``
        Scale To Fit -- Scale the text size to fit inside the width and height.
      * ``TRUNCATE``
        Truncate -- Only output curves that fit within the width and height. Output the remainder to the "Remainder" output..

      :type: enum in [``'OVERFLOW'``, ``'SCALE_TO_FIT'``, ``'TRUNCATE'``], default ``'OVERFLOW'``

   .. attribute:: pivot_mode

      Pivot point position relative to character

      * ``MIDPOINT``
        Midpoint -- Midpoint.
      * ``TOP_LEFT``
        Top Left -- Top Left.
      * ``TOP_CENTER``
        Top Center -- Top Center.
      * ``TOP_RIGHT``
        Top Right -- Top Right.
      * ``BOTTOM_LEFT``
        Bottom Left -- Bottom Left.
      * ``BOTTOM_CENTER``
        Bottom Center -- Bottom Center.
      * ``BOTTOM_RIGHT``
        Bottom Right -- Bottom Right.

      :type: enum in [``'MIDPOINT'``, ``'TOP_LEFT'``, ``'TOP_CENTER'``, ``'TOP_RIGHT'``, ``'BOTTOM_LEFT'``, ``'BOTTOM_CENTER'``, ``'BOTTOM_RIGHT'``], default ``'BOTTOM_LEFT'``

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
   * :class:`GeometryNode.poll`
   * :class:`GeometryNode.bl_rna_get_subclass`
   * :class:`GeometryNode.bl_rna_get_subclass_py`

