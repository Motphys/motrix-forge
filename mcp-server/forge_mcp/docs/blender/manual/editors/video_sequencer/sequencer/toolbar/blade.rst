.. _tool-blade:

*****
Blade
*****

.. reference::

   :Mode:      Sequencer Mode
   :Tool:      :menuselection:`Toolbar --> Blade`
   :Shortcut:  :kbd:`K`, :kbd:`Shift-K`

Cuts a strip in two. Specifically, it first shortens the strip so it only shows the content
up to the cut point, then adds a second strip that shows the content after the cut point.

Splitting be done in two different ways:

- Select the tool in the Toolbar and click a strip at the time point where you want to split it.
- Alternatively, select one or more strips, place the Playhead at the time point where you want to
  split them, and press one of the keyboard shortcuts below.

You can choose between the following split types:

Soft :kbd:`K`
   After splitting, it's still possible to restore the cut content in the new strips
   by dragging their handles.

Hard :kbd:`Shift-K`
   After splitting, it's not possible to restore the cut content by dragging handles.
   However, you can still restore it by changing the :ref:`Hold Offset <sequencer-duration-hard>`
   in the Sidebar.
