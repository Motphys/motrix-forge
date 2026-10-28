Font Drawing (blf)
==================

.. module:: blf

This module provides access to Blender's text drawing functions.


Hello World Text Example
++++++++++++++++++++++++

Example of using the blf module. For this module to work we
need to use the GPU module :mod:`gpu` as well.

.. literalinclude:: ..\examples\blf.py
   :lines: 8-


Drawing Text to an Image
++++++++++++++++++++++++

Example showing how text can be draw into an image.
This can be done by binding an image buffer (:mod:`imbuf`) to the font's ID.

.. literalinclude:: ..\examples\blf.1.py
   :lines: 9-

.. function:: aspect(fontid, aspect)

   Set the aspect for drawing text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg aspect: The aspect ratio for text drawing to use.
   :type aspect: float


.. method:: bind_imbuf(fontid, image, display_name=None)

   Context manager to draw text into an image buffer instead of the GPU's context.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg imbuf: The image to draw into.
   :type imbuf: :class:`imbuf.types.ImBuf`
   :arg display_name: The color management display name to use or None.
   :type display_name: str | None
   :return: The BLF ImBuf context manager.
   :rtype: BLFImBufContext


.. function:: clipping(fontid, xmin, ymin, xmax, ymax)

   Set the clipping, enable/disable using CLIPPING.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg xmin: Clip the drawing area by these bounds.
   :type xmin: float
   :arg ymin: Clip the drawing area by these bounds.
   :type ymin: float
   :arg xmax: Clip the drawing area by these bounds.
   :type xmax: float
   :arg ymax: Clip the drawing area by these bounds.
   :type ymax: float


.. function:: color(fontid, r, g, b, a)

   Set the color for drawing text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg r: red channel 0.0 - 1.0.
   :type r: float
   :arg g: green channel 0.0 - 1.0.
   :type g: float
   :arg b: blue channel 0.0 - 1.0.
   :type b: float
   :arg a: alpha channel 0.0 - 1.0.
   :type a: float


.. function:: dimensions(fontid, text)

   Return the width and height of the text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg text: the text to draw.
   :type text: str
   :return: the width and height of the text.
   :rtype: tuple[float, float]


.. function:: disable(fontid, option)

   Disable option.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
   :type option: int


.. function:: draw(fontid, text)

   Draw text in the current context.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg text: the text to draw.
   :type text: str


.. function:: draw_buffer(fontid, text)

   Draw text into the buffer bound to the fontid.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg text: the text to draw.
   :type text: str


.. function:: enable(fontid, option)

   Enable option.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
   :type option: int


.. function:: load(filepath)

   Load a new font.

   :arg filepath: the filepath of the font.
   :type filepath: str | bytes
   :return: the new font's fontid or -1 if there was an error.
   :rtype: int


.. function:: position(fontid, x, y, z)

   Set the position for drawing text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg x: X axis position to draw the text.
   :type x: float
   :arg y: Y axis position to draw the text.
   :type y: float
   :arg z: Z axis position to draw the text.
   :type z: float


.. function:: rotation(fontid, angle)

   Set the text rotation angle, enable/disable using ROTATION.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg angle: The angle for text drawing to use.
   :type angle: float


.. function:: shadow(fontid, level, r, g, b, a)

   Shadow options, enable/disable using SHADOW .

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg level: The blur level (0, 3, 5) or outline (6).
   :type level: int
   :arg r: Shadow color (red channel 0.0 - 1.0).
   :type r: float
   :arg g: Shadow color (green channel 0.0 - 1.0).
   :type g: float
   :arg b: Shadow color (blue channel 0.0 - 1.0).
   :type b: float
   :arg a: Shadow color (alpha channel 0.0 - 1.0).
   :type a: float


.. function:: shadow_offset(fontid, x, y)

   Set the offset for shadow text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg x: Vertical shadow offset value in pixels.
   :type x: float
   :arg y: Horizontal shadow offset value in pixels.
   :type y: float


.. function:: size(fontid, size)

   Set the size for drawing text.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg size: Point size of the font.
   :type size: float


.. function:: unload(filepath)

   Unload an existing font.

   :arg filepath: the filepath of the font.
   :type filepath: str | bytes


.. function:: word_wrap(fontid, wrap_width)

   Set the wrap width, enable/disable using WORD_WRAP.

   :arg fontid: The id of the typeface as returned by :func:`blf.load`, for default font use 0.
   :type fontid: int
   :arg wrap_width: The width (in pixels) to wrap words at.
   :type wrap_width: int


.. data:: CLIPPING

   Constant value 2

.. data:: MONOCHROME

   Constant value 128

.. data:: ROTATION

   Constant value 1

.. data:: SHADOW

   Constant value 4

.. data:: WORD_WRAP

   Constant value 64

