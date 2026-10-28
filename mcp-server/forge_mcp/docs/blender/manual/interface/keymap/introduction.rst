
****************
Common Shortcuts
****************

Conventions Used in This Manual
===============================

.. Note that these conventions are for people reading the manual.
   we have more detailed list of conventions for authors under the writing style section.

Keyboard
--------

Hotkey letters are shown in this manual like they appear on a keyboard. For example:

.. list-table::
   :align: left
   :width: 95%
   :widths: 30 70

   * - :kbd:`G`
     - The "G" key without any others (as though you were typing a lowercase "g").
   * - :kbd:`Shift`, :kbd:`Ctrl`, :kbd:`Alt`
     - Modifier keys.
   * - :kbd:`Ctrl-W`, :kbd:`Shift-Alt-A`, ...
     - Indicates that these keys should be pressed simultaneously.
   * - :kbd:`0` to :kbd:`9`
     - The keys on the number row above the letters.
   * - :kbd:`Numpad0` to :kbd:`Numpad9`, :kbd:`NumpadPlus`
     - The keys on the separate numeric keypad.

Other keys are referred to by their names,
such as :kbd:`Esc`, :kbd:`Tab`, and :kbd:`F1` to :kbd:`F12`.
Of special note are the arrow keys: :kbd:`Left`, :kbd:`Right` and so on.


Mouse
-----

This manual refers to mouse buttons as:

.. list-table::
   :align: left
   :width: 95%
   :widths: 30 70

   * - :kbd:`LMB`
     - Left Mouse Button
   * - :kbd:`RMB`
     - Right Mouse Button
   * - :kbd:`MMB`
     - Middle Mouse Button
   * - :kbd:`Wheel`, :kbd:`WheelUp` & :kbd:`WheelDown`
     - Scrolling the wheel.

.. note::

   Blender has two main selection modes: left-click select and right-click select.
   See the :ref:`Select with Mouse Button <keymap-blender_default-prefs-select_with>` preference.

   While left-click select is the default as it's the most common in other applications,
   right-click select does have its advantages.
   See: `Learn the benefits of right-click select <https://vimeo.com/76335056>`__.


Hovering
========

The following shortcuts can be pressed while hovering the mouse cursor
over an editable field.


.. _keymap-common-properties:

Properties
----------

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Ctrl-C`
     - Copy the (single) value of the field.
   * - :kbd:`Ctrl-V`
     - Paste the (single) value of the field.
   * - :kbd:`Ctrl-Alt-C`
     - Copy the entire vector or color of the field.
   * - :kbd:`Ctrl-Alt-V`
     - Paste the entire vector or color of the field.
   * - :kbd:`RMB`
     - Open the context menu.
   * - :kbd:`Backspace`
     - Reset the value to its default.
   * - :kbd:`Minus`
     - Invert the value's sign (multiply by -1.0).
   * - :kbd:`Ctrl-Wheel`
     - Change the value in incremental steps.

       For fields with a pop-up list of values, this cycles the value.
   * - :kbd:`Return`
     - Activates menus and toggles checkboxes.
   * - :kbd:`Alt`
     - Hold while editing values to apply the change to all selected items
       (objects, bones, sequence-strips).

       This can be used for number fields and toggles.


Animation
---------

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`I`
     - Insert a :doc:`keyframe </animation/keyframes/introduction>`.
   * - :kbd:`Alt-I`
     - Clear the keyframe.
   * - :kbd:`Shift-Alt-I`
     - Clear all keyframes.
   * - :kbd:`Ctrl-D`
     - Assign a :doc:`driver </animation/drivers/introduction>`.
   * - :kbd:`Ctrl-Alt-D`
     - Clear the driver.
   * - :kbd:`K`
     - Add the property to the current
       :doc:`keying set </animation/keyframes/keying_sets>`.
   * - :kbd:`Alt-K`
     - Remove the property from the current keying set.


Python Scripting
----------------

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Ctrl-C`
     - When pressed while hovering over an :ref:`operator button <ui-operator-buttons>`,
       copies its Python command to the clipboard. This command can then be used in the
       :doc:`Python Console </editors/python_console>` or in the :doc:`Text Editor </editors/text_editor>`
       when writing scripts.
   * - :kbd:`Shift-Ctrl-C`
     - When pressed while hovering over a field, copies its relative data path (also available from
       the context menu). Useful when writing drivers or scripts.
   * - :kbd:`Shift-Ctrl-Alt-C`
     - When pressed while hovering over a field, copies its full data path.


Dragging
========

The following shortcuts can be used while moving/rotating/scaling an object in the 3D Viewport,
dragging the slider of a value, and so on. Note that they should be pressed after starting
the drag, not before.

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Ctrl`
     - Snap to coarse increments, making it easier to (say) rotate an object by exactly 90°.
   * - :kbd:`Shift`
     - Make the value change more slowly in response to mouse movement, giving you more precision.
   * - :kbd:`Shift-Ctrl`
     - Snap to fine increments.


.. _ui-text-editing:

Text Editing
============

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Home`
     - Go to the start of the line.
   * - :kbd:`End`
     - Go to the end of the line.
   * - :kbd:`Left`, :kbd:`Right`
     - Move the cursor a single character.
   * - :kbd:`Ctrl-Left`, :kbd:`Ctrl-Right`
     - Move the cursor an entire word.
   * - :kbd:`Backspace`, :kbd:`Delete`
     - Delete characters.
   * - :kbd:`Ctrl-Backspace`, :kbd:`Ctrl-Delete`
     - Delete words.
   * - :kbd:`Shift`
     - Select while holding the key and moving the cursor.
   * - :kbd:`Ctrl-A`
     - Select all text.
   * - :kbd:`Ctrl-C`
     - Copy the selected text.
   * - :kbd:`Ctrl-X`
     - Cut the selected text.
   * - :kbd:`Ctrl-V`
     - Paste text at the cursor position.


Confirm & Cancel
================

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Esc`, :kbd:`RMB`
     - Cancel.
   * - :kbd:`Return`, :kbd:`LMB`
     - Confirm.

.. (todo?) deactivation: Some controls can be disabled, in Blender deactivated controls are still editable.
   That can be due to the current state or context. In that case, they appear in a lighter color.

Customizing
===========

You can customize keyboard and mouse shortcuts in the :doc:`Preferences </editors/preferences/keymap>`.
