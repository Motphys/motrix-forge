.. _bpy.types.ShaderNodeOutputLight:

*****************
Light Output Node
*****************

.. figure:: /images/node-types_ShaderNodeOutputLight.webp
   :align: right
   :alt: Light Node.

The *Light Output* node is used customize a :doc:`Light object </render/lights/light_object>`.
Currently only supported for Cycles.

To start using this node, select the Light and click :menuselection:`Nodes --> Use Nodes`
in the *Data* tab of the :doc:`/editors/properties_editor` editor.


Inputs
======

Surface
   Shading for the (invisible) surface of the Light.


Properties
==========

Target
   Render engine the input shader is used for.
   By default, the shader is shared between Cycles and EEVEE --
   with multiple output nodes, a specialized shader setup can be created for each.


Outputs
=======

This node has no outputs.
