.. index:: Geometry Nodes; Repeat
.. _bpy.types.GeometryNodeRepeatInput:
.. _bpy.types.GeometryNodeRepeatOutput:

***********
Repeat Zone
***********

Repeat zones allow running nodes many times in a loop. Compared with simply duplicating
a node, they support executing a node an arbitrary number of times, possibly determined
when the node group is evaluated. For example, the nodes could be repeated based on the
number of stories in a building generator.

.. figure:: /images/modeling_geometry-nodes_repeat_zone.png
   :align: center

   Repeat zone used to repeat a node group a few times

When adding a repeat zone, two nodes are added, with the "zone" defined between them.
The inputs connected to the *Repeat Input* node are read at the beginning, before starting
the repetitions. Then they are passed to the inside of the zone where they can be changed,
and passed to the next iteration. This process is repeated the specified number of times.

Other nodes can be connected as inputs to the inside of the repeat zone from the outside.
Those are constant throughout every iteration based on their value at the current frame.
However, outputs of the zone must be connected through the *Repeat Output* node.


Inputs
======

Iterations
   Number of times to repeat the execution of the zone. The current iteration is available with the
   *Iteration* input on the inside of the zone.

Geometry
   Standard geometry input, which is available by default to input geometry into the repeat zone.
   More bake items can be added by dragging sockets into the blank socket or in the *Bake Items* panel.
   Items can be renamed by :kbd:`Ctrl-LMB` on the socket name or in the nodes *Properties* panel.


Properties
==========

Inspection Index
   Iteration number that is used by inspection features like the :doc:`/modeling/geometry_nodes/output/viewer`
   or :doc:`socket inspection </modeling/geometry_nodes/inspection>`.
