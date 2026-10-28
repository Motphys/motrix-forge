.. index:: Geometry Nodes; Warning
.. _bpy.types.GeometryNodeWarning:

************
Warning Node
************

.. figure:: /images/node-types_GeometryNodeWarning.webp
   :align: right
   :alt: Warning Node.

Outputs a custom message that can be referenced in the
:ref:`modifiers-geometry-nodes-warnings` panel of the Geometry Nodes Modifier.

This allows node groups to communicate expectations about input values.

By default, warnings are propagated through all parent node groups.
However, this can be controlled using the :ref:`bpy.types.Node.warning_propagation` setting on each node.


Inputs
======

Show
   Present the warning in the :ref:`modifiers-geometry-nodes-warnings` panel.


Properties
==========

Warning Type
   The type of message to display, the type affects the icon displayed.


Outputs
=======

Show
   A passthrough of the *Show* input.
