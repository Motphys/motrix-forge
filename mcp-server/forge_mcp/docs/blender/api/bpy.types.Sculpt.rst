Sculpt(Paint)
=============

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Paint`

.. class:: Sculpt(Paint)


   .. attribute:: automasking_boundary_edges_propagation_steps

      Distance where boundary edge automasking is going to protect vertices from the fully masked edge

      :type: int in [1, 20], default 1

   .. attribute:: automasking_cavity_blur_steps

      The number of times the cavity mask is blurred

      :type: int in [0, 25], default 0

   .. data:: automasking_cavity_curve

      Curve used for the sensitivity

      :type: :class:`CurveMapping`, (readonly)

   .. data:: automasking_cavity_curve_op

      Curve used for the sensitivity

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: automasking_cavity_factor

      The contrast of the cavity mask

      :type: float in [0, 5], default 1.0

   .. attribute:: automasking_start_normal_falloff

      Extend the angular range with a falloff gradient

      :type: float in [0.0001, 1], default 0.25

   .. attribute:: automasking_start_normal_limit

      The range of angles that will be affected

      :type: float in [0.0001, 3.14159], default 0.349066

   .. attribute:: automasking_view_normal_falloff

      Extend the angular range with a falloff gradient

      :type: float in [0.0001, 1], default 0.25

   .. attribute:: automasking_view_normal_limit

      The range of angles that will be affected

      :type: float in [0.0001, 3.14159], default 1.5708

   .. attribute:: constant_detail_resolution

      Maximum edge length for dynamic topology sculpting (as divisor of Blender unit - higher value means smaller edge length)

      :type: float in [0.0001, inf], default 3.0

   .. attribute:: detail_percent

      Maximum edge length for dynamic topology sculpting (in brush percentage)

      :type: float in [0.5, 100], default 25.0

   .. attribute:: detail_refine_method

      In dynamic-topology mode, how to add or remove mesh detail

      * ``SUBDIVIDE``
        Subdivide Edges -- Subdivide long edges to add mesh detail where needed.
      * ``COLLAPSE``
        Collapse Edges -- Collapse short edges to remove mesh detail where possible.
      * ``SUBDIVIDE_COLLAPSE``
        Subdivide Collapse -- Both subdivide long edges and collapse short edges to refine mesh detail.

      :type: enum in [``'SUBDIVIDE'``, ``'COLLAPSE'``, ``'SUBDIVIDE_COLLAPSE'``], default ``'SUBDIVIDE'``

   .. attribute:: detail_size

      Maximum edge length for dynamic topology sculpting (in pixels)

      :type: float in [0.5, 40], default 12.0

   .. attribute:: detail_type_method

      In dynamic-topology mode, how mesh detail size is calculated

      * ``RELATIVE``
        Relative Detail -- Mesh detail is relative to the brush size and detail size.
      * ``CONSTANT``
        Constant Detail -- Mesh detail is constant in world space according to detail size.
      * ``BRUSH``
        Brush Detail -- Mesh detail is relative to brush radius.
      * ``MANUAL``
        Manual Detail -- Mesh detail does not change on each stroke, only when using Flood Fill.

      :type: enum in [``'RELATIVE'``, ``'CONSTANT'``, ``'BRUSH'``, ``'MANUAL'``], default ``'RELATIVE'``

   .. attribute:: gravity

      Amount of gravity after each dab

      :type: float in [0, 1], default 0.0

   .. attribute:: gravity_object

      Object whose Z axis defines orientation of gravity

      :type: :class:`Object`

   .. attribute:: lock_x

      Disallow changes to the X axis of vertices

      :type: boolean, default False

   .. attribute:: lock_y

      Disallow changes to the Y axis of vertices

      :type: boolean, default False

   .. attribute:: lock_z

      Disallow changes to the Z axis of vertices

      :type: boolean, default False

   .. attribute:: radial_symmetry

      Number of times to copy strokes across the surface

      :type: int array of 3 items in [1, 64], default (0, 0, 0)

   .. attribute:: symmetrize_direction

      Source and destination for symmetrize operator

      :type: enum in :ref:`rna_enum_symmetrize_direction_items`, default ``'NEGATIVE_X'``

   .. attribute:: transform_mode

      How the transformation is going to be applied to the target

      * ``ALL_VERTICES``
        All Vertices -- Applies the transformation to all vertices in the mesh.
      * ``RADIUS_ELASTIC``
        Elastic -- Applies the transformation simulating elasticity using the radius of the cursor.

      :type: enum in [``'ALL_VERTICES'``, ``'RADIUS_ELASTIC'``], default ``'ALL_VERTICES'``

   .. attribute:: use_automasking_boundary_edges

      Do not affect non manifold boundary edges

      :type: boolean, default False

   .. attribute:: use_automasking_boundary_face_sets

      Do not affect vertices that belong to a Face Set boundary

      :type: boolean, default False

   .. attribute:: use_automasking_cavity

      Do not affect vertices on peaks, based on the surface curvature

      :type: boolean, default False

   .. attribute:: use_automasking_cavity_inverted

      Do not affect vertices within crevices, based on the surface curvature

      :type: boolean, default False

   .. attribute:: use_automasking_custom_cavity_curve

      Use custom curve

      :type: boolean, default False

   .. attribute:: use_automasking_face_sets

      Affect only vertices that share Face Sets with the active vertex

      :type: boolean, default False

   .. attribute:: use_automasking_start_normal

      Affect only vertices with a similar normal to where the stroke starts

      :type: boolean, default False

   .. attribute:: use_automasking_topology

      Affect only vertices connected to the active vertex under the brush

      :type: boolean, default False

   .. attribute:: use_automasking_view_normal

      Affect only vertices with a normal that faces the viewer

      :type: boolean, default False

   .. attribute:: use_automasking_view_occlusion

      Only affect vertices that are not occluded by other faces (slower performance)

      :type: boolean, default False

   .. attribute:: use_deform_only

      Use only deformation modifiers (temporary disable all constructive modifiers except multi-resolution)

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
   * :class:`Paint.brush`
   * :class:`Paint.brush_asset_reference`
   * :class:`Paint.eraser_brush`
   * :class:`Paint.eraser_brush_asset_reference`
   * :class:`Paint.palette`
   * :class:`Paint.show_brush`
   * :class:`Paint.show_brush_on_surface`
   * :class:`Paint.show_low_resolution`
   * :class:`Paint.use_sculpt_delay_updates`
   * :class:`Paint.use_symmetry_x`
   * :class:`Paint.use_symmetry_y`
   * :class:`Paint.use_symmetry_z`
   * :class:`Paint.use_symmetry_feather`
   * :class:`Paint.cavity_curve`
   * :class:`Paint.use_cavity`
   * :class:`Paint.tile_offset`
   * :class:`Paint.tile_x`
   * :class:`Paint.tile_y`
   * :class:`Paint.tile_z`

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
   * :class:`Paint.bl_rna_get_subclass`
   * :class:`Paint.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :class:`ToolSettings.sculpt`

