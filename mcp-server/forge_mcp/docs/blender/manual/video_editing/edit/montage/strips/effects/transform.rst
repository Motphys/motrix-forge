.. _bpy.types.TransformSequence:

***************
Transform Strip
***************

Transform is a Swiss Army knife of image manipulation.
It moves, rotates, and scales the images within a strip.


Options
=======

.. _bpy.types.TransformSequence.interpolation:

Filter
   Determines how pixel values are interpolated when scaling or transforming images.

   :None:
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

.. _bpy.types.TransformSequence.translation_unit:

Translation Unit
   Control whether the input values are in *Percent* or *Pixels*.

.. _bpy.types.TransformSequence.translate_start:

Position
   Moves the input along the X and Y axis.

.. _bpy.types.TransformSequence.use_uniform_scale:

Uniform Scale
   Scale the input evenly along the X and Y axis.

.. _bpy.types.TransformSequence.scale_start:

Scale
   Scale the image on the X and Y axis.

.. _bpy.types.TransformSequence.rotation_start:

Rotation
   Rotates the input two-dimensionally along the Z axis.


Example
=======

.. figure:: /images/video-editing_sequencer_strips_effects_transform_example.png

   Transform Effect.
