DataTransferModifier(Modifier)
==============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: DataTransferModifier(Modifier)

   Modifier transferring some data from a source mesh

   .. attribute:: data_types_edges

      Which edge data layers to transfer

      * ``SHARP_EDGE``
        Sharp -- Transfer sharp mark.
      * ``SEAM``
        UV Seam -- Transfer UV seam mark.
      * ``CREASE``
        Crease -- Transfer subdivision crease values.
      * ``BEVEL_WEIGHT_EDGE``
        Bevel Weight -- Transfer bevel weights.
      * ``FREESTYLE_EDGE``
        Freestyle -- Transfer Freestyle edge mark.

      :type: enum set in {``'SHARP_EDGE'``, ``'SEAM'``, ``'CREASE'``, ``'BEVEL_WEIGHT_EDGE'``, ``'FREESTYLE_EDGE'``}, default {``'SHARP_EDGE'``}

   .. attribute:: data_types_loops

      Which face corner data layers to transfer

      * ``CUSTOM_NORMAL``
        Custom Normals -- Transfer custom normals.
      * ``COLOR_CORNER``
        Colors -- Transfer color attributes.
      * ``UV``
        UVs -- Transfer UV layers.

      :type: enum set in {``'CUSTOM_NORMAL'``, ``'COLOR_CORNER'``, ``'UV'``}, default {``'CUSTOM_NORMAL'``}

   .. attribute:: data_types_polys

      Which face data layers to transfer

      * ``SMOOTH``
        Smooth -- Transfer flat/smooth mark.
      * ``FREESTYLE_FACE``
        Freestyle Mark -- Transfer Freestyle face mark.

      :type: enum set in {``'SMOOTH'``, ``'FREESTYLE_FACE'``}, default {``'SMOOTH'``}

   .. attribute:: data_types_verts

      Which vertex data layers to transfer

      * ``VGROUP_WEIGHTS``
        Vertex Groups -- Transfer active or all vertex groups.
      * ``BEVEL_WEIGHT_VERT``
        Bevel Weight -- Transfer bevel weights.
      * ``COLOR_VERTEX``
        Colors -- Transfer color attributes.

      :type: enum set in {``'VGROUP_WEIGHTS'``, ``'BEVEL_WEIGHT_VERT'``, ``'COLOR_VERTEX'``}, default {``'VGROUP_WEIGHTS'``}

   .. attribute:: edge_mapping

      Method used to map source edges to destination ones

      :type: enum in :ref:`rna_enum_dt_method_edge_items`, default ``'NEAREST'``

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. attribute:: islands_precision

      Factor controlling precision of islands handling (typically, 0.1 should be enough, higher values can make things really slow)

      :type: float in [0, 1], default 0.0

   .. attribute:: layers_uv_select_dst

      How to match source and destination layers

      :type: enum in :ref:`rna_enum_dt_layers_select_dst_items`, default ``'NAME'``

   .. attribute:: layers_uv_select_src

      Which layers to transfer, in case of multi-layers types

      :type: enum in :ref:`rna_enum_dt_layers_select_src_items`, default ``'ALL'``

   .. attribute:: layers_vcol_loop_select_dst

      How to match source and destination layers

      :type: enum in :ref:`rna_enum_dt_layers_select_dst_items`, default ``'NAME'``

   .. attribute:: layers_vcol_loop_select_src

      Which layers to transfer, in case of multi-layers types

      :type: enum in :ref:`rna_enum_dt_layers_select_src_items`, default ``'ALL'``

   .. attribute:: layers_vcol_vert_select_dst

      How to match source and destination layers

      :type: enum in :ref:`rna_enum_dt_layers_select_dst_items`, default ``'NAME'``

   .. attribute:: layers_vcol_vert_select_src

      Which layers to transfer, in case of multi-layers types

      :type: enum in :ref:`rna_enum_dt_layers_select_src_items`, default ``'ALL'``

   .. attribute:: layers_vgroup_select_dst

      How to match source and destination layers

      :type: enum in :ref:`rna_enum_dt_layers_select_dst_items`, default ``'NAME'``

   .. attribute:: layers_vgroup_select_src

      Which layers to transfer, in case of multi-layers types

      :type: enum in :ref:`rna_enum_dt_layers_select_src_items`, default ``'ALL'``

   .. attribute:: loop_mapping

      Method used to map source faces' corners to destination ones

      :type: enum in :ref:`rna_enum_dt_method_loop_items`, default ``'NEAREST_POLYNOR'``

   .. attribute:: max_distance

      Maximum allowed distance between source and destination element, for non-topology mappings

      :type: float in [0, inf], default 1.0

   .. attribute:: mix_factor

      Factor to use when applying data to destination (exact behavior depends on mix mode, multiplied with weights from vertex group when defined)

      :type: float in [0, 1], default 0.0

   .. attribute:: mix_mode

      How to affect destination elements with source values

      :type: enum in :ref:`rna_enum_dt_mix_mode_items`, default ``'REPLACE'``

   .. attribute:: object

      Object to transfer data from

      :type: :class:`Object`

   .. attribute:: poly_mapping

      Method used to map source faces to destination ones

      :type: enum in :ref:`rna_enum_dt_method_poly_items`, default ``'NEAREST'``

   .. attribute:: ray_radius

      'Width' of rays (especially useful when raycasting against vertices or edges)

      :type: float in [0, inf], default 0.0

   .. attribute:: use_edge_data

      Enable edge data transfer

      :type: boolean, default False

   .. attribute:: use_loop_data

      Enable face corner data transfer

      :type: boolean, default False

   .. attribute:: use_max_distance

      Source elements must be closer than given distance from destination one

      :type: boolean, default False

   .. attribute:: use_object_transform

      Evaluate source and destination meshes in global space

      :type: boolean, default True

   .. attribute:: use_poly_data

      Enable face data transfer

      :type: boolean, default False

   .. attribute:: use_vert_data

      Enable vertex data transfer

      :type: boolean, default False

   .. attribute:: vert_mapping

      Method used to map source vertices to destination ones

      :type: enum in :ref:`rna_enum_dt_method_vertex_items`, default ``'NEAREST'``

   .. attribute:: vertex_group

      Vertex group name for selecting the affected areas

      :type: string, default "", (never None)

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

