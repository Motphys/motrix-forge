
**************
Default Keymap
**************

While this isn't a comprehensive list,
this page shows common keys used in Blender's default keymap.

.. Even though this is not intended to be comprehensive,
   it could be expanded.


Global Keys
===========

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Ctrl-O`
     - Open file.
   * - :kbd:`Ctrl-S`
     - Save file.
   * - :kbd:`Ctrl-N`
     - New file.
   * - :kbd:`Ctrl-Z`
     - Undo.
   * - :kbd:`Shift-Ctrl-Z`
     - Redo.
   * - :kbd:`Ctrl-Q`
     - Quit.
   * - :kbd:`F1`
     - Help *(context sensitive)*.
   * - :kbd:`F2`
     - Rename active item.
   * - :kbd:`F3`
     - :ref:`Menu Search <bpy.ops.wm.search_menu>`.
   * - :kbd:`F4`
     - File context menu.
   * - :kbd:`F5` - :kbd:`F8`
     - *Reserved for user actions.*
   * - :kbd:`F9`
     - :ref:`Adjust Last Operation <bpy.ops.screen.redo_last>`.
   * - :kbd:`F10`
     - *Reserved for user actions.*
   * - :kbd:`F11`
     - Show render window.
   * - :kbd:`F12`
     - Render the current frame.
   * - :kbd:`Q`
     - Quick access (favorites).
   * - :kbd:`Ctrl-Spacebar`
     - Toggle Maximize :doc:`Area </interface/window_system/areas>`.
   * - :kbd:`Ctrl-PageUp` / :kbd:`Ctrl-PageDown`
     - Next/previous :doc:`Workspace </interface/window_system/workspaces>`.
   * - :kbd:`Spacebar`
     - User configurable; see :ref:`keymap-blender_default-spacebar_action`.
   * - :kbd:`Shift-Ctrl-Spacebar`
     - Playback animation (reverse).


Common Editing Keys
===================

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`X`
     - Delete the selected item with a confirmation dialog.
   * - :kbd:`Delete`
     - Delete the selected item without a confirmation dialog.


Common Editor Keys
==================

These keys are shared across editors such as the 3D Viewport, UV and Graph editor.

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`A`
     - Select all.
   * - :kbd:`Alt-A` /

       Double-tap :kbd:`A`
     - Select none.
   * - :kbd:`Ctrl-I`
     - Invert selection.
   * - :kbd:`H`
     - Hide selected items.
   * - :kbd:`Shift-H`
     - Hide unselected items.
   * - :kbd:`Alt-H`
     - Reveal hidden items.
   * - :kbd:`T`
     - Toggle Toolbar.
   * - :kbd:`N`
     - Toggle Sidebar.


3D Viewport Keys
================

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Tab`
     - Toggle Edit mode.
   * - :kbd:`Ctrl-Tab`
     - Toggle Pose mode for armatures, or show a :doc:`mode </editors/3dview/modes>` switching pie menu for others.
   * - :kbd:`1` - :kbd:`3`
     - In Edit Mode, switch between editing vertices (:kbd:`1`), edges (:kbd:`2`), or faces (:kbd:`3`).

       Hold :kbd:`Shift` to toggle one of these without disabling the others.

       Hold :kbd:`Ctrl` to alter how the selection is transformed from the old mode to the new.

       See :doc:`Mesh Selection Modes </modeling/meshes/selecting/introduction>` for details.
   * - :kbd:`AccentGrave`
     - Show 3D Viewport navigation pie menu.
   * - :kbd:`Ctrl-AccentGrave`
     - Toggle gizmos.
   * - :kbd:`Shift-AccentGrave`
     - Start :ref:`Fly/Walk Navigation <3dview-fly-walk>`.


Platform Specific Keys
======================

macOS
-----

The :kbd:`Cmd` key can be used instead of :kbd:`Ctrl` on macOS
for all but a few exceptions which conflict with the operating system.

List of additional macOS specific keys:

.. list-table::
   :align: left
   :width: 95%
   :widths: 20 80

   * - :kbd:`Cmd-Comma`
     - Preferences.
