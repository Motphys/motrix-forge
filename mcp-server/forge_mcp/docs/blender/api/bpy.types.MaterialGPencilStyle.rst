MaterialGPencilStyle(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MaterialGPencilStyle(bpy_struct)


   .. attribute:: alignment_mode

      Defines how align Dots and Boxes with drawing path and object rotation

      * ``PATH``
        Path -- Follow stroke drawing path and object rotation.
      * ``OBJECT``
        Object -- Follow object rotation only.
      * ``FIXED``
        Fixed -- Do not follow drawing path or object rotation and keeps aligned with viewport.

      :type: enum in [``'PATH'``, ``'OBJECT'``, ``'FIXED'``], default ``'PATH'``

   .. attribute:: alignment_rotation

      Additional rotation applied to dots and square texture of strokes. Only applies in texture shading mode.

      :type: float in [-1.5708, 1.5708], default 0.0

   .. attribute:: color

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: fill_color

      Color for filling region bounded by each stroke

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: fill_image

      :type: :class:`Image`

   .. attribute:: fill_style

      Select style used to fill strokes

      * ``SOLID``
        Solid -- Fill area with solid color.
      * ``GRADIENT``
        Gradient -- Fill area with gradient color.
      * ``TEXTURE``
        Texture -- Fill area with image texture.

      :type: enum in [``'SOLID'``, ``'GRADIENT'``, ``'TEXTURE'``], default ``'SOLID'``

   .. attribute:: flip

      Flip filling colors

      :type: boolean, default False

   .. attribute:: ghost

      Display strokes using this color when showing onion skins

      :type: boolean, default False

   .. attribute:: gradient_type

      Select type of gradient used to fill strokes

      * ``LINEAR``
        Linear -- Fill area with gradient color.
      * ``RADIAL``
        Radial -- Fill area with radial gradient.

      :type: enum in [``'LINEAR'``, ``'RADIAL'``], default ``'LINEAR'``

   .. attribute:: hide

      Set color Visibility

      :type: boolean, default False

   .. data:: is_fill_visible

      True when opacity of fill is set high enough to be visible

      :type: boolean, default False, (readonly)

   .. data:: is_stroke_visible

      True when opacity of stroke is set high enough to be visible

      :type: boolean, default False, (readonly)

   .. attribute:: lock

      Protect color from further editing and/or frame changes

      :type: boolean, default False

   .. attribute:: mix_color

      Color for mixing with primary filling color

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: mix_factor

      Mix Factor

      :type: float in [0, 1], default 0.0

   .. attribute:: mix_stroke_factor

      Mix Stroke Factor

      :type: float in [0, 1], default 0.0

   .. attribute:: mode

      Select line type for strokes

      * ``LINE``
        Line -- Draw strokes using a continuous line.
      * ``DOTS``
        Dots -- Draw strokes using separated dots.
      * ``BOX``
        Squares -- Draw strokes using separated squares.

      :type: enum in [``'LINE'``, ``'DOTS'``, ``'BOX'``], default ``'LINE'``

   .. attribute:: pass_index

      Index number for the "Color Index" pass

      :type: int in [0, 32767], default 0

   .. attribute:: pixel_size

      Texture Pixel Size factor along the stroke

      :type: float in [1, 5000], default 0.0

   .. attribute:: show_fill

      Show stroke fills of this material

      :type: boolean, default False

   .. attribute:: show_stroke

      Show stroke lines of this material

      :type: boolean, default False

   .. attribute:: stroke_image

      :type: :class:`Image`

   .. attribute:: stroke_style

      Select style used to draw strokes

      * ``SOLID``
        Solid -- Draw strokes with solid color.
      * ``TEXTURE``
        Texture -- Draw strokes using texture.

      :type: enum in [``'SOLID'``, ``'TEXTURE'``], default ``'SOLID'``

   .. attribute:: texture_angle

      Texture Orientation Angle

      :type: float in [-inf, inf], default 0.0

   .. attribute:: texture_clamp

      Do not repeat texture and clamp to one instance only

      :type: boolean, default False

   .. attribute:: texture_offset

      Shift Texture in 2d Space

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: texture_scale

      Scale Factor for Texture

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: use_fill_holdout

      Remove the color from underneath this stroke by using it as a mask

      :type: boolean, default False

   .. attribute:: use_overlap_strokes

      Disable stencil and overlap self intersections with alpha materials

      :type: boolean, default False

   .. attribute:: use_stroke_holdout

      Remove the color from underneath this stroke by using it as a mask

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

   * :class:`Material.grease_pencil`

