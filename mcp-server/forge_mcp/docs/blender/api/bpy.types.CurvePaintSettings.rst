CurvePaintSettings(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CurvePaintSettings(bpy_struct)


   .. attribute:: corner_angle

      Angles above this are considered corners

      :type: float in [0, 3.14159], default 1.22173

   .. attribute:: curve_type

      Type of curve to use for new strokes

      :type: enum in [``'POLY'``, ``'BEZIER'``], default ``'BEZIER'``

   .. attribute:: depth_mode

      Method of projecting depth

      :type: enum in [``'CURSOR'``, ``'SURFACE'``], default ``'CURSOR'``

   .. attribute:: error_threshold

      Allow deviation for a smoother, less precise line

      :type: int in [1, 100], default 8

   .. attribute:: fit_method

      Curve fitting method

      :type: enum in :ref:`rna_enum_curve_fit_method_items`, default ``'REFIT'``

   .. attribute:: radius_max

      Radius to use when the maximum pressure is applied (or when a tablet isn't used)

      :type: float in [0, 100], default 1.0

   .. attribute:: radius_min

      Minimum radius when the minimum pressure is applied (also the minimum when tapering)

      :type: float in [0, 100], default 0.0

   .. attribute:: radius_taper_end

      Taper factor for the radius of each point along the curve

      :type: float in [0, 10], default 0.0

   .. attribute:: radius_taper_start

      Taper factor for the radius of each point along the curve

      :type: float in [0, 1], default 0.0

   .. attribute:: surface_offset

      Offset the stroke from the surface

      :type: float in [-10, 10], default 0.0

   .. attribute:: surface_plane

      Plane for projected stroke

      * ``NORMAL_VIEW``
        Normal to Surface -- Draw in a plane perpendicular to the surface.
      * ``NORMAL_SURFACE``
        Tangent to Surface -- Draw in the surface plane.
      * ``VIEW``
        View -- Draw in a plane aligned to the viewport.

      :type: enum in [``'NORMAL_VIEW'``, ``'NORMAL_SURFACE'``, ``'VIEW'``], default ``'NORMAL_VIEW'``

   .. attribute:: use_corners_detect

      Detect corners and use non-aligned handles

      :type: boolean, default True

   .. attribute:: use_offset_absolute

      Apply a fixed offset (don't scale by the radius)

      :type: boolean, default False

   .. attribute:: use_pressure_radius

      Map tablet pressure to curve radius

      :type: boolean, default False

   .. attribute:: use_project_only_selected

      Project the strokes only onto selected objects

      :type: boolean, default False

   .. attribute:: use_stroke_endpoints

      Use the start of the stroke for the depth

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

References
----------

.. hlist::
   :columns: 2

   * :class:`ToolSettings.curve_paint_settings`

