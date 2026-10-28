
***************
Selecting Nodes
***************

.. _bpy.ops.node.select_all:

All :kbd:`A`
   Selects all nodes.
None :kbd:`Alt-A`
   Deselects all nodes.
Invert :kbd:`Ctrl-I`
   Inverts the current selection.
Box Select :kbd:`B`
   See :ref:`Box Select <bpy.ops.*.select_box>`.
Circle Select
   See :ref:`Circle Select <bpy.ops.*.select_circle>`.
Lasso Select
   See :ref:`Lasso Select <bpy.ops.*.select_lasso>`.
Select Linked From :kbd:`L`
   Expand the selection to nodes which are linked to the inputs of the currently selected nodes.
Select Linked To :kbd:`Shift-L`
   Expand the selection to nodes which are linked to the outputs of the currently selected nodes.
Select Grouped :kbd:`Shift-G`
   Selects nodes that have similar :doc:`properties </interface/controls/nodes/sidebar>`
   as the active node.

   Type
      The node type, e.g. all Math nodes.
   Color
      The node color. (Nodes can be given a custom color to visually organize them in the editor;
      this is not related to any color information they might consume or produce as part of their function.
      The color can be set in the :doc:`Sidebar </interface/controls/nodes/sidebar>`.)
   Prefix, Suffix
      Matches the name property from start/end of the text.
Activate Same Type Previous/Next :kbd:`Shift-]`/:kbd:`Shift-[`
   Finds the previous/next node of same type, activates it, and ensures it's visible.
Find Node :kbd:`Ctrl-F`
   Shows a search pop-up for finding a node by name.

Select Multiple :kbd:`Shift-LMB`
   Add/remove a node to/from the selection.
