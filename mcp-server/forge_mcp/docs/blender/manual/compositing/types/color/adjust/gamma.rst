.. index:: Compositor Nodes; Gamma
.. _bpy.types.CompositorNodeGamma:

**********
Gamma Node
**********

Use this node to apply a gamma correction. The node is typically used to convert from gamma encoded to linear
color space, or in the reverse direction with 1/gamma.

.. Editor's Note: The rest of the page gets copied into:
.. - :doc:`</render/cycles/nodes/types/color/gamma>`

.. --- copy below this line ---

.. figure:: /images/node-types_CompositorNodeGamma.webp
   :align: right
   :alt: Gamma Node.

Inputs
======

Image
   Standard color input.
Gamma
   An exponential brightness factor, applied as :math:`output\_value = input\_value ^ {\gamma}`


Properties
==========

This node has no properties.


Outputs
=======

Image
   Standard color output.


Examples
========

.. figure:: /images/compositing_types_color_gamma_example.jpg
   :width: 700px

   Example of a Gamma node.
