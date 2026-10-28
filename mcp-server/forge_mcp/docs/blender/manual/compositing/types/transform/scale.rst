.. index:: Compositor Nodes; Scale
.. _bpy.types.CompositorNodeScale:

**********
Scale Node
**********

.. figure:: /images/node-types_CompositorNodeScale.webp
   :align: right
   :alt: Scale Node.

This node scales the size of an image.


Inputs
======

Image
   Standard color input.
X, Y
   Scale in the axis directions, only available if *Space* is set to *Relative* or *Absolute*.


Properties
==========

Interpolation
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

Space
   Coordinate Space to scale relative to.

   :Relative:
      Percentage values relative to the dimensions of the image input.
   :Absolute:
      Size of an image by using absolute pixel values.
   :Scene Size:
      Sizes an image to the size of the final render resolution for the scene.
      For example, rendering a scene at the standard 1080p resolution but setting the render percentage at 50%,
      will produce a 1080p image with the scene scaled down 50% and leaving the rest of the image as alpha.
   :Render Size:
      Image dimensions set in the Render panel.

      Stretch, Fit, Crop
         Stretch distorts the image so that it fits into the render size.
         Fit scales the image until the bigger axis "fits" into the render size.
         Crop cuts the image so that it is the same aspect ratio as the render size.


Outputs
=======

Image
   Standard color output.


Examples
========

For instance X: 0.5 and Y: 0.5 would produce an image which width and
height would be half of what they used to be.

Use this node to match image sizes.
Most nodes produce an image that is the same size as the image input into their top image socket.
To uniformly combine two images of different size,
the second image has to be scaled up to match the resolution of the first.
