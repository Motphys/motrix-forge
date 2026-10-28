.. index:: Compositor Nodes; RGB
.. _bpy.types.CompositorNodeRGB:
.. Editor's Note: This page gets copied into :doc:`</render/cycles/nodes/types/input/rgb>`

.. --- copy below this line ---

********
RGB Node
********

.. figure:: /images/node-types_CompositorNodeRGB.webp
   :align: right
   :alt: RGB Node.

The *RGB* node outputs the color value chosen with the color picker widget.

.. tip::

   Dragging colors from a color picker button into a node editor creates a RGB node.
   Alpha values are preserved, if the source color has no alpha, a value of 1.0 is used.


Inputs
======

This node has no input sockets.


Properties
==========

The RGB node uses the :ref:`color picker widget <ui-color-picker>`.


Outputs
=======

Color / RGBA
   A single RGBA color value.
