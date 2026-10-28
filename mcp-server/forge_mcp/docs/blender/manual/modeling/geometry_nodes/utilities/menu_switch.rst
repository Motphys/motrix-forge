.. index:: Geometry Nodes; Menu Switch
.. _bpy.types.GeometryNodeMenuSwitch:

****************
Menu Switch Node
****************

.. figure:: /images/node-types_GeometryNodeMenuSwitch.webp
   :align: right
   :alt: Menu Switch Node.

The *Menu Switch* node outputs one of its inputs depending on a menu
selection. Only the input that is passed through the node is computed.

The available menu entries are defined by the user. Menu items can be
added and removed, as well as renamed and reordered in the editor side
bar. Renaming a menu entry keeps existing links of the matching input
socket.

The menu can be used in node groups and the nodes modifier UI.
Connecting the menu input with a *Group Input* node will expose the menu
as a group input. A menu socket in a node group, reroute node, or other
pass-through nodes needs to be connected to a *Menu Switch* node in
order to work. An unconnected menu socket will show an empty menu by
default.

Connecting multiple *Menu Switch* nodes to the same output
socket creates a conflict (even when the menu entries are the same).
To avoid this a menu switch can be wrapped in a node group. Multiple
node groups of the same type can be connected to the same menu, since
they contain the same menu switch node.

.. list-table::

   * - .. figure:: /images/node-types_GeometryNodeMenuSwitch_conflict.webp

          Conflict caused by connecting different menus.

     - .. figure:: /images/node-types_GeometryNodeMenuSwitch_group_wrapper.webp

          Same node group can be connected without conflict.


.. seealso::

   The :doc:`/modeling/geometry_nodes/utilities/index_switch`
   is similar but it exposes the choices as an integer index.


Inputs
======

Menu
   Determines which of the input options below will be passed through.

Item Inputs
   One input is created for every menu entry. The input is used when the matching option is selected.
   Items can be renamed by :kbd:`Ctrl-LMB` on the socket name or in the nodes *Properties* panel.


Properties
==========

Type
   Determines the type of the data that is handled by the node.


Outputs
=======

Output
   One of the inputs without any modifications.
