.. _ui-color-picker:

************
Color Picker
************

.. figure:: /images/interface_controls_templates_color-picker_circle-hsv.png
   :align: right

   Circle HSV.

The color picker is a pop-up that lets you define a color value.
Holding :kbd:`Ctrl` while dragging snaps the hue to make it quick to select primary colors.

Color Picker
   Lets you pick the first and second color component. The shape can be changed; see `Types`_.
Value/Lightness
   The slider with a gradient in the background defines the value/lightness of the color mixing.
   Fine control can be inputted with :kbd:`Wheel`.
Color Model
   Selects the :term:`Color Model` for the number value fields.

   :RGB: Create the final color by mixing red, green, and blue colors.
   :HSV/HSL:
      Create the final color by adjusting hue, saturation, and value/lightness.

   .. note::

      In Blender, the RGB and HSV/HSL values are in Scene Linear color space,
      and are therefore not :term:`Gamma` corrected.
      On the contrary, *Hex* are automatically :term:`Gamma` corrected
      for the :term:`sRGB Color Space <Color Space>`.
      For more information, see :doc:`Color Management </render/color_management>`.
Color Values
   Blender uses values from 0 to 1.0 to express the color mixing for RGB and HSV/HSL colors.

   For color inputs with an :term:`Alpha Channel`, another slider is added.
Hex
   The hexadecimal (hex) equivalent value to the mixed color.
   Shorthand hex colors are can be typed in, e.g. dark yellow ``FFCC00`` can be written as ``FC0``.

.. _bpy.ops.ui.eyedropper_color:

Eyedropper (pipette icon)
   Samples a color from inside the Blender window using the :ref:`ui-eyedropper`. Note, colors sampled from the
   eyedropper are in linear color space and do not account for view transform adjustments. Picking colors from
   reference and background images might not work as they can be rendered as an overlay.


Shortcuts
=========

- :kbd:`Ctrl-LMB` (drag) snaps the hue to 30° intervals.
- :kbd:`Shift-LMB` (drag) precision motion.
- :kbd:`Wheel` adjust the value/lightness.
- :kbd:`Backspace` reset the value to the default value.


Types
=====

The default color picker type can be selected in the Preferences,
see: :ref:`Interface <bpy.types.PreferencesView.color_picker_type>`.

.. list-table:: Color Picker types.

   * - .. figure:: /images/interface_controls_templates_color-picker_circle-hsv.png

          Circle HSV.

     - .. figure:: /images/interface_controls_templates_color-picker_circle-hsl.png

          Circle HSL.

     - ..

   * - .. figure:: /images/interface_controls_templates_color-picker_square-sv-h.png

          Square (SV + H).

     - .. figure:: /images/interface_controls_templates_color-picker_square-hs-v.png

          Square (HS + V).

     - .. figure:: /images/interface_controls_templates_color-picker_square-hv-s.png

          Square (HV + S).
