
*************
Grease Pencil
*************

.. reference::

   :Panel:     :menuselection:`Render --> Grease Pencil`

This panel contains settings that control the rendering of :doc:`Grease Pencil lines </grease_pencil/index>`.


Viewport
========

.. _bpy.types.SceneGpencil.antialias_threshold:

SMAA Threshold
   Threshold for the edge detection algorithm used to correct aliasing for the 3D Viewport,
   Higher values may result in loss of detail due to excessive blurring.


Render
======

.. _bpy.types.SceneGpencil.antialias_threshold_render:

SMAA Threshold
   Threshold for the edge detection algorithm used to correct aliasing for the final render,
   Higher values may result in loss of detail due to excessive blurring.

.. _bpy.types.SceneGpencil.aa_samples:

SSAA Samples
   Number of samples used for super-sampling anti-aliasing in the final render.
   Higher values produce smoother lines but increase render time.
