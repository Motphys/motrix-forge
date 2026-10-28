.. index:: Compositor Nodes; Glare
.. _bpy.types.CompositorNodeGlare:

**********
Glare Node
**********

.. figure:: /images/node-types_CompositorNodeGlare.webp
   :align: right
   :alt: Glare Node.

The *Glare Node* enhances bright areas of an image by adding effects such as lens flares, bloom, and fog glow.
It simulates the way light interacts with lenses, creating realistic or artistic highlights and reflections.


Inputs
======

Image
   Standard color input.


Highlights
----------

Threshold
   Defines the minimum luminance required for an area to contribute to the glare effect.
   Lower values include more areas, while higher values restrict glare to the brightest regions.

Smoothness
   Controls how gradually pixels transition into the glare effect.
   Higher values create a smoother highlight extraction.


Clamp
^^^^^

Clamp bright highlights defined by the *Maximum* input.

This can help create a more consistent looking bloom effect when there is a large variations in luminance.

Maximum
   Clamps the intensity of the highlights to this value.


Adjust
------

Strength
   Adjusts the overall intensity of the glare effect.
   Values greater than 1 boost the luminance of the glare,
   while values less than 1 blends the glare with the original image.

Saturation
   Modifies the color saturation of the glare effect.

Tint
   Tints the glare effect, allowing for colored highlights.


Glare
-----

Size :guilabel:`Bloom` :guilabel:`Fog Glow`
   Defines the relative spread of the glare across the image.
   A value of 1 makes the glare cover the full image, while 0.5 restricts it to half, and so on.

Streaks :guilabel:`Streaks`
   The number of streaks radiating from highlights.

Streaks Angle :guilabel:`Streaks`
   The angle that the first streak makes with the horizontal axis.

Iterations :guilabel:`Ghosts` :guilabel:`Streaks` :guilabel:`Simple Star`
   The number of ghosts for *Ghost* glare or the quality and
   spread of glare for *Streaks* and *Simple Star* glare types.

Color Modulation :guilabel:`Ghosts` :guilabel:`Streaks`
   Introduces subtle color variations, simulating chromatic dispersion effects.

Fade :guilabel:`Streaks` :guilabel:`Simple Star`
   The fade-out intensity of the streaks.

Diagonal :guilabel:`Simple Star`
   Rotates the *Simple Star* streaks by 45° for an alternate pattern.


Properties
==========

Glare Type
   Defines the type of glare effect applied to the image.

   :Bloom:
      Simulates the soft glow around bright areas due to light scattering in eyes and camera lenses.
   :Ghosts:
      Creates multiple overlapping glare artifacts resembling lens reflections or a hazy glow.
   :Streaks:
      Produces bright streaks radiating from highlights, commonly used to simulate lens flares.
   :Fog Glow:
      Simulates the soft glow around bright areas due to light scattering in eyes and camera lenses.
      This glare is a more physically accurate version of *Bloom*, creating a softer,
      more realistic glow at the cost of increased computation time.
   :Simple Star:
      Similar to *Streaks*, but produces a simpler star-shaped glare effect.

Quality
   Controls the resolution at which the glare effect is processed.
   This can be helpful to save render times while only doing preview renders.

   :High: Full-resolution processing for best quality.
   :Medium: Uses a lower resolution to reduce computation time.
   :Low: Fastest processing but with lower detail.


Outputs
=======

Image
   The final image with the generated glare added.

Glare
   The generated glare effect isolated from the input image.
   Useful for further compositing or adjustments.

Highlights
   The extracted bright areas used to generate the glare effect.
   Can be used to fine-tune the glare or as a base for custom effects.
