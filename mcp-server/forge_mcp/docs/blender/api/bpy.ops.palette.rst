Palette Operators
=================

.. module:: bpy.ops.palette

.. function:: color_add()

   Add new color to active palette

.. function:: color_delete()

   Remove active color from palette

.. function:: color_move(*, type='UP')

   Move the active Color up/down in the list

   :arg type: Type
   :type type: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: extract_from_image(*, threshold=1)

   Extract all colors used in Image and create a Palette

   :arg threshold: Threshold
   :type threshold: int in [-inf, inf], (optional)

.. function:: join(*, palette="")

   Join Palette Swatches

   :arg palette: Palette, Name of the Palette
   :type palette: string, (optional, never None)

.. function:: new()

   Add new palette

.. function:: sort(*, type='HSV')

   Sort Palette Colors

   :arg type: Type
   :type type: enum in [``'HSV'``, ``'SVH'``, ``'VHS'``, ``'LUMINANCE'``], (optional)

