BrushGpencilSettings(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BrushGpencilSettings(bpy_struct)

   Settings for Grease Pencil brush

   .. attribute:: active_smooth_factor

      Amount of smoothing while drawing

      :type: float in [0, 1], default 0.0

   .. attribute:: angle

      Direction of the stroke at which brush gives maximal thickness (0° for horizontal)

      :type: float in [-1.5708, 1.5708], default 0.0

   .. attribute:: angle_factor

      Reduce brush thickness by this factor when stroke is perpendicular to 'Angle' direction

      :type: float in [0, 1], default 0.0

   .. attribute:: aspect

      :type: :class:`mathutils.Vector` of 2 items in [0.01, 1], default (1.0, 1.0)

   .. attribute:: brush_draw_mode

      Preselected mode when using this brush

      * ``ACTIVE``
        Active -- Use current mode.
      * ``MATERIAL``
        Material -- Use always material mode.
      * ``VERTEXCOLOR``
        Vertex Color -- Use always Vertex Color mode.

      :type: enum in [``'ACTIVE'``, ``'MATERIAL'``, ``'VERTEXCOLOR'``], default ``'ACTIVE'``

   .. attribute:: caps_type

      The shape of the start and end of the stroke

      :type: enum in [``'ROUND'``, ``'FLAT'``], default ``'ROUND'``

   .. data:: curve_jitter

      Curve used for the jitter effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_random_hue

      Curve used for modulating effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_random_pressure

      Curve used for modulating effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_random_saturation

      Curve used for modulating effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_random_strength

      Curve used for modulating effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_random_uv

      Curve used for modulating effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_random_value

      Curve used for modulating effect

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_sensitivity

      Curve used for the sensitivity

      :type: :class:`CurveMapping`, (readonly)

   .. data:: curve_strength

      Curve used for the strength

      :type: :class:`CurveMapping`, (readonly)

   .. attribute:: dilate

      Number of pixels to expand or contract fill area

      :type: int in [-40, 40], default 1

   .. attribute:: eraser_mode

      Eraser Mode

      * ``SOFT``
        Dissolve -- Erase strokes, fading their points strength and thickness.
      * ``HARD``
        Point -- Erase stroke points.
      * ``STROKE``
        Stroke -- Erase entire strokes.

      :type: enum in [``'SOFT'``, ``'HARD'``, ``'STROKE'``], default ``'SOFT'``

   .. attribute:: eraser_strength_factor

      Amount of erasing for strength

      :type: float in [0, 100], default 0.0

   .. attribute:: eraser_thickness_factor

      Amount of erasing for thickness

      :type: float in [0, 100], default 0.0

   .. attribute:: extend_stroke_factor

      Strokes end extension for closing gaps, use zero to disable

      :type: float in [0, 10], default 0.0

   .. attribute:: fill_direction

      Direction of the fill

      * ``NORMAL``
        Normal -- Fill internal area.
      * ``INVERT``
        Inverted -- Fill inverted area.

      :type: enum in [``'NORMAL'``, ``'INVERT'``], default ``'NORMAL'``

   .. attribute:: fill_draw_mode

      Mode to draw boundary limits

      * ``BOTH``
        All -- Use both visible strokes and edit lines as fill boundary limits.
      * ``STROKE``
        Strokes -- Use visible strokes as fill boundary limits.
      * ``CONTROL``
        Edit Lines -- Use edit lines as fill boundary limits.

      :type: enum in [``'BOTH'``, ``'STROKE'``, ``'CONTROL'``], default ``'BOTH'``

   .. attribute:: fill_extend_mode

      Types of stroke extensions used for closing gaps

      * ``EXTEND``
        Extend -- Extend strokes in straight lines.
      * ``RADIUS``
        Radius -- Connect endpoints that are close together.

      :type: enum in [``'EXTEND'``, ``'RADIUS'``], default ``'EXTEND'``

   .. attribute:: fill_factor

      Factor for fill boundary accuracy, higher values are more accurate but slower

      :type: float in [0.05, 8], default 0.0

   .. attribute:: fill_layer_mode

      Layers used as boundaries

      * ``VISIBLE``
        Visible -- Visible layers.
      * ``ACTIVE``
        Active -- Only active layer.
      * ``ABOVE``
        Layer Above -- Layer above active.
      * ``BELOW``
        Layer Below -- Layer below active.
      * ``ALL_ABOVE``
        All Above -- All layers above active.
      * ``ALL_BELOW``
        All Below -- All layers below active.

      :type: enum in [``'VISIBLE'``, ``'ACTIVE'``, ``'ABOVE'``, ``'BELOW'``, ``'ALL_ABOVE'``, ``'ALL_BELOW'``], default ``'VISIBLE'``

   .. attribute:: fill_simplify_level

      Number of simplify steps (large values reduce fill accuracy)

      :type: int in [0, 10], default 0

   .. attribute:: fill_threshold

      Threshold to consider color transparent for filling

      :type: float in [0, 1], default 0.0

   .. attribute:: hardness

      Gradient from the center of Dot and Box strokes (set to 1 for a solid stroke)

      :type: float in [0.001, 1], default 1.0

   .. attribute:: input_samples

      Generated intermediate points for very fast mouse movements (Set to 0 to disable)

      :type: int in [0, 10], default 0

   .. attribute:: material

      Material used for strokes drawn using this brush

      :type: :class:`Material`

   .. attribute:: material_alt

      Material used for secondary uses for this brush

      :type: :class:`Material`

   .. attribute:: outline_thickness_factor

      Thickness of the outline stroke relative to current brush thickness

      :type: float in [0, 1], default 0.0

   .. attribute:: pen_jitter

      Jitter factor of brush radius for new strokes

      :type: float in [0, 100], default 0.0

   .. attribute:: pen_smooth_factor

      Amount of smoothing to apply after finish newly created strokes, to reduce jitter/noise

      :type: float in [0, 2], default 0.0

   .. attribute:: pen_smooth_steps

      Number of times to smooth newly created strokes

      :type: int in [0, 100], default 0

   .. attribute:: pen_strength

      Color strength for new strokes (affect alpha factor of color)

      :type: float in [0, 1], default 0.0

   .. attribute:: pen_subdivision_steps

      Number of times to subdivide newly created strokes, for less jagged strokes

      :type: int in [0, 3], default 0

   .. attribute:: pin_draw_mode

      Pin the mode to the brush

      :type: boolean, default False

   .. attribute:: random_hue_factor

      Random factor to modify original hue

      :type: float in [0, 1], default 0.0

   .. attribute:: random_pressure

      Randomness factor for pressure in new strokes

      :type: float in [0, 1], default 0.0

   .. attribute:: random_saturation_factor

      Random factor to modify original saturation

      :type: float in [0, 1], default 0.0

   .. attribute:: random_strength

      Randomness factor strength in new strokes

      :type: float in [0, 1], default 0.0

   .. attribute:: random_value_factor

      Random factor to modify original value

      :type: float in [0, 1], default 0.0

   .. attribute:: show_fill

      Show transparent lines to use as boundary for filling

      :type: boolean, default True

   .. attribute:: show_fill_boundary

      Show help lines for filling to see boundaries

      :type: boolean, default True

   .. attribute:: show_fill_extend

      Show help lines for stroke extension

      :type: boolean, default True

   .. attribute:: show_lasso

      Do not display fill color while drawing the stroke

      :type: boolean, default False

   .. attribute:: simplify_factor

      Factor of Simplify using adaptive algorithm

      :type: float in [0, 100], default 0.0

   .. attribute:: simplify_pixel_threshold

      Threshold in screen space used for the simplify algorithm. Points within this threshold are treated as if they were in a straight line.

      :type: float in [0, 10], default 0.0

   .. attribute:: use_active_layer_only

      Only edit the active layer of the object

      :type: boolean, default False

   .. attribute:: use_auto_remove_fill_guides

      Automatically remove fill guide strokes after fill operation

      :type: boolean, default True

   .. attribute:: use_collide_strokes

      Check if extend lines collide with strokes

      :type: boolean, default False

   .. attribute:: use_edit_position

      The brush affects the position of the point

      :type: boolean, default False

   .. attribute:: use_edit_strength

      The brush affects the color strength of the point

      :type: boolean, default False

   .. attribute:: use_edit_thickness

      The brush affects the thickness of the point

      :type: boolean, default False

   .. attribute:: use_edit_uv

      The brush affects the UV rotation of the point

      :type: boolean, default False

   .. attribute:: use_fill_limit

      Fill only visible areas in viewport

      :type: boolean, default True

   .. attribute:: use_jitter_pressure

      Use tablet pressure for jitter

      :type: boolean, default False

   .. attribute:: use_keep_caps_eraser

      Keep the caps as they are and don't flatten them when erasing

      :type: boolean, default False

   .. attribute:: use_material_pin

      Keep material assigned to brush

      :type: boolean, default False

   .. attribute:: use_occlude_eraser

      Erase only strokes visible and not occluded

      :type: boolean, default False

   .. attribute:: use_pressure

      Use tablet pressure

      :type: boolean, default False

   .. attribute:: use_random_press_hue

      Use pressure to modulate randomness

      :type: boolean, default False

   .. attribute:: use_random_press_radius

      Use pressure to modulate randomness

      :type: boolean, default False

   .. attribute:: use_random_press_sat

      Use pressure to modulate randomness

      :type: boolean, default False

   .. attribute:: use_random_press_strength

      Use pressure to modulate randomness

      :type: boolean, default False

   .. attribute:: use_random_press_uv

      Use pressure to modulate randomness

      :type: boolean, default False

   .. attribute:: use_random_press_val

      Use pressure to modulate randomness

      :type: boolean, default False

   .. attribute:: use_settings_outline

      Convert stroke to outline

      :type: boolean, default False

   .. attribute:: use_settings_postprocess

      Additional post processing options for new strokes

      :type: boolean, default False

   .. attribute:: use_settings_random

      Random brush settings

      :type: boolean, default False

   .. attribute:: use_settings_stabilizer

      Draw lines with a delay to allow smooth strokes (press Shift key to override while drawing)

      :type: boolean, default True

   .. attribute:: use_strength_pressure

      Use tablet pressure for color strength

      :type: boolean, default False

   .. attribute:: use_stroke_random_hue

      Use randomness at stroke level

      :type: boolean, default False

   .. attribute:: use_stroke_random_radius

      Use randomness at stroke level

      :type: boolean, default False

   .. attribute:: use_stroke_random_sat

      Use randomness at stroke level

      :type: boolean, default False

   .. attribute:: use_stroke_random_strength

      Use randomness at stroke level

      :type: boolean, default False

   .. attribute:: use_stroke_random_uv

      Use randomness at stroke level

      :type: boolean, default False

   .. attribute:: use_stroke_random_val

      Use randomness at stroke level

      :type: boolean, default False

   .. attribute:: use_trim

      Trim intersecting stroke ends

      :type: boolean, default False

   .. attribute:: uv_random

      Random factor for auto-generated UV rotation

      :type: float in [0, 1], default 0.0

   .. attribute:: vertex_color_factor

      Factor used to mix vertex color to get final color

      :type: float in [0, 1], default 0.0

   .. attribute:: vertex_mode

      Defines how vertex color affect to the strokes

      * ``STROKE``
        Stroke -- Vertex Color affects to Stroke only.
      * ``FILL``
        Fill -- Vertex Color affects to Fill only.
      * ``BOTH``
        Stroke & Fill -- Vertex Color affects to Stroke and Fill.

      :type: enum in [``'STROKE'``, ``'FILL'``, ``'BOTH'``], default ``'STROKE'``

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

   * :class:`Brush.gpencil_settings`

