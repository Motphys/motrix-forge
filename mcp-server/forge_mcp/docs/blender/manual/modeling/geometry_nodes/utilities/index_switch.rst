.. index:: Geometry Nodes; Index Switch
.. _bpy.types.GeometryNodeIndexSwitch:

*****************
Index Switch Node
*****************

.. figure:: /images/node-types_GeometryNodeIndexSwitch.webp
   :align: right
   :alt: Index Switch Node.


The *Index Switch* node outputs one of its inputs depending on an index value.
Only the input that is passed through the node is computed.

.. seealso::

   The :doc:`/modeling/geometry_nodes/utilities/menu_switch` is similar but it exposes the choices as a menu.


Inputs
======

Index
   Determines which of the input options below will be passed through.

Item Inputs
   One input is created for every menu entry. The input is used when the
   matching option is selected.


Properties
==========

Type
   Determines the type of the data that is handled by the node.


Outputs
=======

Output
   One of the inputs without any modifications.
