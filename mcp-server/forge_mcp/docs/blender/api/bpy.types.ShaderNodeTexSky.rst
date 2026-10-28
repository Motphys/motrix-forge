ShaderNodeTexSky(ShaderNode)
============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`ShaderNode`

.. class:: ShaderNodeTexSky(ShaderNode)

   Generate a procedural sky texture

   .. attribute:: air_density

      Density of air molecules.
      • 0 - No air.
      • 1 - Clear day atmosphere.
      • 2 - Highly polluted day

      :type: float in [0, 10], default 1.0

   .. attribute:: altitude

      Height from sea level

      :type: float in [0, 60000], default 0.0

   .. data:: color_mapping

      Color mapping settings

      :type: :class:`ColorMapping`, (readonly, never None)

   .. attribute:: dust_density

      Density of dust molecules and water droplets.
      • 0 - No dust.
      • 1 - Clear day atmosphere.
      • 5 - City like atmosphere.
      • 10 - Hazy day

      :type: float in [0, 10], default 1.0

   .. attribute:: ground_albedo

      Ground color that is subtly reflected in the sky

      :type: float in [0, 1], default 0.0

   .. attribute:: ozone_density

      Density of ozone layer.
      • 0 - No ozone.
      • 1 - Clear day atmosphere.
      • 2 - City like atmosphere

      :type: float in [0, 10], default 1.0

   .. attribute:: sky_type

      Which sky model should be used

      * ``PREETHAM``
        Preetham -- Preetham 1999.
      * ``HOSEK_WILKIE``
        Hosek / Wilkie -- Hosek / Wilkie 2012.
      * ``NISHITA``
        Nishita -- Nishita 1993 improved.

      :type: enum in [``'PREETHAM'``, ``'HOSEK_WILKIE'``, ``'NISHITA'``], default ``'PREETHAM'``

   .. attribute:: sun_direction

      Direction from where the sun is shining

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 1.0)

   .. attribute:: sun_disc

      Include the sun itself in the output

      :type: boolean, default True

   .. attribute:: sun_elevation

      Sun angle from horizon

      :type: float in [-inf, inf], default 1.5708

   .. attribute:: sun_intensity

      Strength of sun

      :type: float in [0, 1000], default 1.0

   .. attribute:: sun_rotation

      Rotation of sun around zenith

      :type: float in [-inf, inf], default 0.0

   .. attribute:: sun_size

      Size of sun disc

      :type: float in [0, 1.5708], default 0.00951204

   .. data:: texture_mapping

      Texture coordinate mapping settings

      :type: :class:`TexMapping`, (readonly, never None)

   .. attribute:: turbidity

      Atmospheric turbidity

      :type: float in [1, 10], default 0.0

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
   * :class:`ShaderNode.poll`
   * :class:`ShaderNode.bl_rna_get_subclass`
   * :class:`ShaderNode.bl_rna_get_subclass_py`

