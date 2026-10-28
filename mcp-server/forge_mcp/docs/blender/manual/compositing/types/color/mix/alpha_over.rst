.. index:: Compositor Nodes; Alpha Over
.. _bpy.types.CompositorNodeAlphaOver:

***************
Alpha Over Node
***************

.. figure:: /images/node-types_CompositorNodeAlphaOver.webp
   :align: right
   :alt: Alpha Over Node.

The *Alpha Over* node is used to layer an image on top of another with alpha blending.


Inputs
======

Factor
   The alpha of the foreground image, going from 0 (fully transparent) to 1 (fully opaque).
Image
   The background image.
Image
   The foreground image.
Convert Premultiplied
   Defines whether the foreground is in straight alpha form,
   which is necessary to know for proper alpha compositing.
   Images in the compositor are in premultiplied alpha form by default,
   so this should be false in most cases. But if, and only if,
   the foreground was converted to straight alpha form for some reason, this should be set to true.


Properties
==========

This node has no properties.


Outputs
=======

Image
   The blended result.


Examples
========

Overlay
-------

In the node tree below, the :doc:`/compositing/types/color/color_ramp` is used to convert an opaque,
grayscale swirl image to a red one with transparency. Then, the *Alpha Over* node is used to overlay
it on top of another image.

.. figure:: /images/compositing_types_converter_color-ramp_create-alpha-mask.png
   :width: 600px

   Assembling a composite image using Alpha Over.


Fade In
-------

The example below uses the :doc:`/compositing/types/input/scene/time_curve` to gradually increase the
*Alpha Over* node's *Factor* from 0 to 1 over the course of 30 frames. This will result in the text
fading in on top of the background image.

.. figure:: /images/compositing_types_color_alpha-over_example.png
   :width: 600px

   Animated fade in effect using Alpha Over.
