.. index:: Compositor Nodes; Rotate
.. _bpy.types.CompositorNodeRotate:

***********
Rotate Node
***********

.. figure:: /images/node-types_CompositorNodeRotate.webp
   :align: right
   :alt: Rotate Node.

This node rotates an image.


Inputs
======

Image
   Standard color input.
Degr
   Rotation angle in degree. Positive values rotate clockwise and negative ones counterclockwise.


Properties
==========

Filter
   Determines how pixel values are interpolated when scaling or transforming images.

   :Nearest:
      Uses the value of the closest pixel with no smoothing.
      This is the fastest method and is well-suited for pixel art or low-resolution images
      where sharp, blocky edges are desirable.
      In animations, motion appears in single-pixel steps, which can cause visible jittering.
   :Bilinear:
      Averages the values of surrounding pixels to create a smoother result than *Nearest*.
      Provides a good balance between performance and visual quality.
   :Bicubic:
      Computes a weighted average of a larger neighborhood of pixels for even smoother results.
      Ideal for photographic images or gradients where preserving fine detail is important.


Outputs
=======

Image
   Standard color output.
