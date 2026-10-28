.. index:: Compositor Nodes; Map UV
.. _bpy.types.CompositorNodeMapUV:

***********
Map UV Node
***********

.. figure:: /images/node-types_CompositorNodeMapUV.webp
   :align: right
   :alt: Map UV node.

Distorts a texture so it can be composited onto the UV-mapped objects in the scene.

May be used in combination with the :doc:`Cryptomatte Node </compositing/types/mask/cryptomatte>`
to only apply the texture to specific objects.


Inputs
======

Image
   The texture to distort.
UV
   The UV coordinates at which to sample the texture. This slot is typically connected
   to the UV render pass, which is only available with the Cycles renderer;
   see :doc:`Cycles render passes </render/layers/passes>`.

.. hint::

   It's possible to store the UV information in a multi-layer OpenEXR file.


Properties
==========

Filter Type
   Determines how pixel values are interpolated when scaling or transforming images.

   :Nearest:
      Uses the value of the closest pixel with no smoothing.
      This is the fastest method and is well-suited for pixel art or low-resolution images
      where sharp, blocky edges are desirable.
      In animations, motion appears in single-pixel steps, which can cause visible jittering.
   :Anisotropic:
      Adjusts interpolation based on the direction and scale of the transformation.
      Helps reduce blurring or aliasing when scaling at steep angles or uneven resolutions,
      especially useful in textures viewed at oblique angles or in detailed 3D projections.


Outputs
=======

Image
   The distorted texture, which can then be overlaid on the render using e.g. the
   :doc:`/compositing/types/color/mix/alpha_over`.


Examples
========

In the first example, we overlay a grid pattern on top of two Suzanne heads after they have
been rendered. To achieve this, we enable the UV pass in the
:doc:`Property Editor </editors/properties_editor>`'s
:menuselection:`View Layer --> Passes` panel, use it to distort the grid image,
and combine the result with the rendered image using the Alpha Over Node.

.. figure:: /images/compositing_types_distort_map-uv_example-1.png
   :width: 700px

   Overlaying a grid texture.

In the next example, we do the same thing with the Blender logo, using a cryptomatte
to ensure it only gets applied to one of the cubes.

It's here that the limitations of the Map UV node become apparent: the overlaid image is
really just "plastered on" and is not affected by the lighting and shadows in the scene.
At most, you can cheat a little by making the image translucent like in the previous example.

So, while this node can be handy for certain post-production effects or fixes,
it's generally not a replacement for including the image during rendering.

.. figure:: /images/compositing_types_distort_map-uv_example-2.png
   :width: 700px

   Overlaying a logo.
