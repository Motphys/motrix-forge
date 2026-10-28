ShaderNodeTexVoronoi(ShaderNode)
================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`, :class:`ShaderNode`

.. class:: ShaderNodeTexVoronoi(ShaderNode)

   Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells

   .. data:: color_mapping

      Color mapping settings

      :type: :class:`ColorMapping`, (readonly, never None)

   .. attribute:: distance

      The distance metric used to compute the texture

      * ``EUCLIDEAN``
        Euclidean -- Euclidean distance.
      * ``MANHATTAN``
        Manhattan -- Manhattan distance.
      * ``CHEBYCHEV``
        Chebychev -- Chebychev distance.
      * ``MINKOWSKI``
        Minkowski -- Minkowski distance.

      :type: enum in [``'EUCLIDEAN'``, ``'MANHATTAN'``, ``'CHEBYCHEV'``, ``'MINKOWSKI'``], default ``'EUCLIDEAN'``

   .. attribute:: feature

      The Voronoi feature that the node will compute

      * ``F1``
        F1 -- Computes the distance to the closest point as well as its position and color.
      * ``F2``
        F2 -- Computes the distance to the second closest point as well as its position and color.
      * ``SMOOTH_F1``
        Smooth F1 -- Smoothed version of F1. Weighted sum of neighbor voronoi cells..
      * ``DISTANCE_TO_EDGE``
        Distance to Edge -- Computes the distance to the edge of the voronoi cell.
      * ``N_SPHERE_RADIUS``
        N-Sphere Radius -- Computes the radius of the n-sphere inscribed in the voronoi cell.

      :type: enum in [``'F1'``, ``'F2'``, ``'SMOOTH_F1'``, ``'DISTANCE_TO_EDGE'``, ``'N_SPHERE_RADIUS'``], default ``'F1'``

   .. attribute:: normalize

      Normalize output Distance to 0.0 to 1.0 range

      :type: boolean, default False

   .. data:: texture_mapping

      Texture coordinate mapping settings

      :type: :class:`TexMapping`, (readonly, never None)

   .. attribute:: voronoi_dimensions

      Number of dimensions to output noise for

      * ``1D``
        1D -- Use the scalar value W as input.
      * ``2D``
        2D -- Use the 2D vector (X, Y) as input. The Z component is ignored..
      * ``3D``
        3D -- Use the 3D vector (X, Y, Z) as input.
      * ``4D``
        4D -- Use the 4D vector (X, Y, Z, W) as input.

      :type: enum in [``'1D'``, ``'2D'``, ``'3D'``, ``'4D'``], default ``'1D'``

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

