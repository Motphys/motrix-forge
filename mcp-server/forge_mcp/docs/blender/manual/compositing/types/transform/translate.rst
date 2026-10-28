.. index:: Compositor Nodes; Translate
.. _bpy.types.CompositorNodeTranslate:

**************
Translate Node
**************

.. figure:: /images/node-types_CompositorNodeTranslate.webp
   :align: right
   :alt: Translate Node.

The Translate node moves an image.

Could also be used to add a 2D camera shake.


Inputs
======

Image
   Standard color input.
X, Y
   Used to move the input image horizontally and vertically.


Properties
==========

Repeat
   Repeat pixels on the other side when they extend over the image dimensions, making endless translating possible.

   None, X Axis, Y Axis, Both Axis
Interpolation
   Interpolation Methods.

   :Nearest: No interpolation, uses nearest neighboring pixel.
   :Bilinear: Simple interpolation between adjacent pixels.
   :Bicubic: Highest quality interpolation.


Outputs
=======

Image
   Standard color output.
