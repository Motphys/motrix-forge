.. index:: Compositor Nodes; Composite
.. _bpy.types.CompositorNodeComposite:

**************
Composite Node
**************

.. figure:: /images/node-types_CompositorNodeComposite.webp
   :align: right
   :alt: Composite Node.

The *Composite* node defines the final output of the Compositor.
It is the node where the image result is sent to the renderer or image output after rendering.

This node is updated automatically after each render and will also update interactively
if changes occur in the connected node tree—provided that the inputs are fully evaluated/rendered.

.. note::

   If multiple Composite nodes are present in the node tree, only the *active* one is used.
   The active Composite node is highlighted with a red header and is the last selected among them.


Inputs
======

Image
   Outputs the result of this input directly to the render result.
   If this socket is left unconnected, the output will be a black image.

Properties
==========

This node has no properties.

Outputs
=======

This node has no output sockets.
