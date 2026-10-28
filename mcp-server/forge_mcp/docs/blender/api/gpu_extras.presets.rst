gpu_extras submodule (gpu_extras.presets)
=========================================

.. module:: gpu_extras.presets

.. function:: draw_circle_2d(position, color, radius, *, segments=None)

   Draw a circle.
   
   :arg position: 2D position where the circle will be drawn.
   :type position: Sequence[float]
   :arg color: Color of the circle (RGBA).
      To use transparency blend must be set to ``ALPHA``, see: :func:`gpu.state.blend_set`.
   :type color: Sequence[float]
   :arg radius: Radius of the circle.
   :type radius: float
   :arg segments: How many segments will be used to draw the circle.
       Higher values give better results but the drawing will take longer.
       If None or not specified, an automatic value will be calculated.
   :type segments: int | None

.. function:: draw_texture_2d(texture, position, width, height)

   Draw a 2d texture.
   
   :arg texture: GPUTexture to draw (e.g. gpu.texture.from_image(image) for :class:`bpy.types.Image`).
   :type texture: :class:`gpu.types.GPUTexture`
   :arg position: Position of the lower left corner.
   :type position: 2D Vector
   :arg width: Width of the image when drawn (not necessarily
       the original width of the texture).
   :type width: float
   :arg height: Height of the image when drawn.
   :type height: float

