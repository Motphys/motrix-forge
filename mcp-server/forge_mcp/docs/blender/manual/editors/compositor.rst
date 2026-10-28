.. index:: Editors; Compositor

**********
Compositor
**********

The Compositor lets you manage :doc:`nodes </interface/controls/nodes/introduction>`
for compositing.

.. figure:: /images/compositing_types_distort_map-uv_example-2.png

   Nodes in the Compositor.

The use of the Compositor is explained in :doc:`/compositing/index`.


Interface
=========

Header
------

.. _bpy.types.SpaceNodeEditor.show_gizmo:

Gizmos
^^^^^^

Controls the display of gizmos in the Compositor.

Clicking :bl-icon:`gizmo` (Show Gizmos) toggles all gizmos in the Compositor
The drop-down button displays a popover with more detailed settings,
which are described below.

.. rubric:: Viewport Gizmos

.. _bpy.types.SpaceNodeEditor.show_gizmo_active_node:

Active Node
   Display a context-sensitive gizmo for the currently selected node.
   This may include transform controls or other visual aids depending on the node type.
