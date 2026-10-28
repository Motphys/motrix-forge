GPU State Utilities (gpu.state)
===============================

.. module:: gpu.state

This module provides access to the gpu state.

.. function:: active_framebuffer_get(enable)

   Return the active frame-buffer in context.


.. function:: blend_get()

    Current blending equation.


.. function:: blend_set(mode)

   Defines the fixed pipeline blending equation.

   :arg mode: The type of blend mode.

      * ``NONE`` No blending.
      * ``ALPHA`` The original color channels are interpolated according to the alpha value.
      * ``ALPHA_PREMULT`` The original color channels are interpolated according to the alpha value with the new colors pre-multiplied by this value.
      * ``ADDITIVE`` The original color channels are added by the corresponding ones.
      * ``ADDITIVE_PREMULT`` The original color channels are added by the corresponding ones that are pre-multiplied by the alpha value.
      * ``MULTIPLY`` The original color channels are multiplied by the corresponding ones.
      * ``SUBTRACT`` The original color channels are subtracted by the corresponding ones.
      * ``INVERT`` The original color channels are replaced by its complementary color.
   :type mode: str


.. function:: clip_distances_set(distances_enabled)

   Sets the number of `gl_ClipDistance` planes used for clip geometry.

   :arg distances_enabled: Number of clip distances enabled.
   :type distances_enabled: int


.. function:: color_mask_set(r, g, b, a)

   Enable or disable writing of frame buffer color components.

   :arg r, g, b, a: components red, green, blue, and alpha.
   :type r, g, b, a: bool


.. function:: depth_mask_get()

   Writing status in the depth component.


.. function:: depth_mask_set(value)

   Write to depth component.

   :arg value: True for writing to the depth component.
   :type near: bool


.. function:: depth_test_get()

    Current depth_test equation.


.. function:: depth_test_set(mode)

   Defines the depth_test equation.

   :arg mode: The depth test equation name.
      Possible values are `NONE`, `ALWAYS`, `LESS`, `LESS_EQUAL`, `EQUAL`, `GREATER` and `GREATER_EQUAL`.
   :type mode: str


.. function:: face_culling_set(culling)

   Specify whether none, front-facing or back-facing facets can be culled.

   :arg mode: `NONE`, `FRONT` or `BACK`.
   :type mode: str


.. function:: front_facing_set(invert)

   Specifies the orientation of front-facing polygons.

   :arg invert: True for clockwise polygons as front-facing.
   :type mode: bool


.. function:: line_width_get()

   Current width of rasterized lines.


.. function:: line_width_set(width)

   Specify the width of rasterized lines.

   :arg size: New width.
   :type mode: float


.. function:: point_size_set(size)

   Specify the diameter of rasterized points.

   :arg size: New diameter.
   :type mode: float


.. function:: program_point_size_set(enable)

   If enabled, the derived point size is taken from the (potentially clipped) shader builtin gl_PointSize.

   :arg enable: True for shader builtin gl_PointSize.
   :type enable: bool


.. function:: scissor_get()

   Retrieve the scissors of the active framebuffer.
   Note: Only valid between 'scissor_set' and a framebuffer rebind.

   :return: The scissor of the active framebuffer as a tuple
        (x, y, xsize, ysize).
        x, y: lower left corner of the scissor rectangle, in pixels.
        xsize, ysize: width and height of the scissor rectangle.
   :rtype: tuple[int, int, int, int]


.. function:: scissor_set(x, y, xsize, ysize)

   Specifies the scissor area of the active framebuffer.
   Note: The scissor state is not saved upon framebuffer rebind.

   :arg x, y: lower left corner of the scissor rectangle, in pixels.
   :type x, y: int
   :arg xsize, ysize: width and height of the scissor rectangle.
   :type xsize, ysize: int


.. function:: scissor_test_set(enable)

   Enable/disable scissor testing on the active framebuffer.

   :arg enable:
        True - enable scissor testing.
        False - disable scissor testing.
   :type enable: bool


.. function:: viewport_get()

   Viewport of the active framebuffer.


.. function:: viewport_set(x, y, xsize, ysize)

   Specifies the viewport of the active framebuffer.
   Note: The viewport state is not saved upon framebuffer rebind.

   :arg x, y: lower left corner of the viewport_set rectangle, in pixels.
   :type x, y: int
   :arg xsize, ysize: width and height of the viewport_set.
   :type xsize, ysize: int


