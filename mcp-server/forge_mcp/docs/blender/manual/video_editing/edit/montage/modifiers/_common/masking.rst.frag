Mask Input
----------

You can mask each modifier to limit the area of the image it affects. This can be done using
either a :doc:`Mask </movie_clip/masking/introduction>` or another strip.

Type
   Type of input data used for the mask.

   :Strip:
      Use the grayscale representation of another strip's image.
   :Mask:
      Use a Mask data-block.

Mask
   The Strip or Mask data-block to use.

Mask Time :guilabel:`Mask Type Only`
   How the start frame of the mask is calculated.

   :Relative: Mask animation is offset to the start of the strip.
   :Absolute: Mask animation is in sync with the scene frame.
