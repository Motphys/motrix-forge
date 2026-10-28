.. index:: Modifiers; Video Sequencer Modifiers
.. index:: Video Sequencer Modifiers

.. _bpy.types.StripModifier:

***************
Strip Modifiers
***************

.. reference::

   :Panel:     :menuselection:`Sidebar region --> Modifiers --> Modifiers`

.. figure:: /images/video-editing_sequencer_sidebar_modifiers_panel.png
   :align: right

Modifiers are used to make adjustments to the image, like contrast,
brightness, saturation, color balance and applying masks.

You can add these modifiers directly to a media strip,
or you can use them within an :doc:`Adjustment Layer </video_editing/edit/montage/strips/adjustment>`
strip, making them apply to several media strips in one go.

.. _bpy.types.Strip.use_linear_modifiers:

Linear Modifiers
   Calculates modifiers in :ref:`linear color space <color-management-linear-space>` instead of the
   :ref:`Sequencer color space <bpy.types.ColorManagedSequencerColorspaceSettings.name>`.

   Calculating modifiers in linear space will match the image processing of the compositor.
   In most cases, this should be enabled; working in a non-linear workflow could have unpredictable results.

.. _bpy.ops.sequencer.strip_modifier_copy:

Copy to Selected Strips
   Copies the modifiers to the selected strips, either replacing their current modifiers or appending to them.


Common Options
==============

Each modifier has several buttons at its top:

Mute (eye icon)
   Disables the modifier. Useful to compare the image with or without modifications.
Move (up/down arrow icon)
   These two buttons change the modifier's position in the stack which affects its computation order.
:bl-icon:`x` (Remove Strip Modifier)
   Deletes the modifier from the stack.


Masking
-------

You can mask each modifier to limit the area of the image it affects. This can be done using
either a :doc:`Mask </movie_clip/masking/introduction>` or another strip.

Mask Input Type
   Type of input data used for the mask.

   :Strip:
      Use the grayscale representation of another strip's image.
   :Mask:
      Use a Mask data-block.

Mask
   The Strip or Mask data-block to use.

Mask Time :guilabel:`Mask Input Only`
   How the start frame of the mask is calculated.

   :Relative: Mask animation is offset to the start of the strip.
   :Absolute: Mask animation is in sync with the scene frame.


Types
=====

Currently, the following modifiers are supported:


.. index:: Video Sequencer Modifiers; Brightness/Contrast Modifier
.. _bpy.types.BrightContrastModifier:

Brightness/Contrast Modifier
----------------------------

Adjusts the brightness and contrast of the image.


.. index:: Video Sequencer Modifiers; Color Balance Modifier
.. _bpy.types.ColorBalanceModifier:

Color Balance Modifier
----------------------

Color balance adjustments, either by the Lift/Gamma/Gain or the Offset/Power/Slope method.

This modifier works similar to the :doc:`Color Balance Node </compositing/types/color/adjust/color_balance>`.

.. figure:: /images/video-editing_sequencer_sidebar_color-balance-modifier.png
   :align: right

Depending on the selected method, the following operations can be applied to the color values in the
sequencer color space:

Lift/Gamma/Gain
   Lift
      Increases the value of dark colors.
   Gamma
      Adjusts midtones.
   Gain
      Adjusts highlights.

Offset/Power/Slope (ASC-CDL)
   The following formula is applied to each RGB color value separately: :math:`c_{out} =  (c_{in}×s + o)^p`

   Slope
      The multiplier :math:`s` influences all color values except black. Its effect is stronger
      the brighter the source color is.
   Offset
      Shifts color values after applying Slope by adding the Offset :math:`o` to them. Note that
      the selected value shown in the UI will be reduced by 1, so the default value of 1 means
      effectively no offset is applied.
   Power
      Overall exponent :math:`p`, which mainly adjusts the midtones.


.. index:: Video Sequencer Modifiers; Curves Modifier
.. _bpy.types.CurvesModifier:

Curves Modifier
---------------

Color and RGB curves.

This modifier works the same as the :doc:`/compositing/types/color/adjust/rgb_curves`.


.. index:: Video Sequencer Modifiers; Hue Correct Modifier
.. _bpy.types.HueCorrectModifier:

Hue Correct Modifier
--------------------

HSV multi points curves.

This modifier works the same as the :doc:`/compositing/types/color/adjust/hue_correct`.


.. index:: Video Sequencer Modifiers; Mask Modifier

Mask Modifier
-------------

The mask modifier is used to affect the :term:`Alpha Channel` of the current strip.

.. _bpy.types.StripModifier.input_mask_type:

Mask Input Type
   Type of input data used for the mask.

   :Strip:
      Use the grayscale representation of another strip to affect the alpha of the current strip.
   :Mask:
      Use a mask data-block to affect the alpha of the current strip.

.. _bpy.types.StripModifier.input_mask_id:
.. _bpy.types.StripModifier.input_mask_strip:

Mask
   The Strip or Mask data-block to use.

.. _bpy.types.StripModifier.mask_time:

Mask Time :guilabel:`Mask Input Only`
   How the start frame of the mask is calculated.

   :Relative: Mask animation is offset to the start of the strip.
   :Absolute: Mask animation is in sync with the scene frame.


.. index:: Video Sequencer Modifiers; Tone Map Modifier

Tone Map Modifier
-----------------

Used to map one set of colors to another in order to approximate the appearance
of high dynamic range images in a medium that has a more limited dynamic range.

This modifier works the same as the :doc:`Tone Map Node </compositing/types/color/adjust/tone_map>`.


.. index:: Video Sequencer Modifiers; White Balance Modifier
.. _bpy.types.WhiteBalanceModifier:

White Balance Modifier
----------------------

Used to adjust the white balance by choosing the color that should be white.


.. index:: Video Sequencer Modifiers; Sound Equalizer Modifier
.. _bpy.types.SoundEqualizerModifier:

Sound Equalizer Modifier
------------------------

This modifier can be used to emphasize or suppress sound frequencies.
The range is limited to 35Hz - 20kHz and +/-35dB.
