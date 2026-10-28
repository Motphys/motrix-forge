.. index:: Geometry Nodes; Sort Elements
.. _bpy.types.GeometryNodeSortElements:

******************
Sort Elements Node
******************

.. figure:: /images/node-types_GeometryNodeSortElements.webp
   :align: right
   :alt: Sort Elements node.

The *Sort Elements* node rearranges geometry elements by changing their indices.


Inputs
======

Geometry
   Standard geometry input.

Selection
   The selection of elements to sort, if left blank, all elements are sorted.
   Non selected elements will be keep their current indices.

Group ID
   Elements with the same group ID are sorted together.
   If this is not a field, the node has no affect.

Sort Weight
   The sorted values used to do the reordering.
   If this is not a field, the node has no affect.


Properties
==========


Domain
   The domain on which the selection and group ID fields are evaluated.

   :Point:
      The fields are evaluated on points, control points, and vertices.
   :Edge:
      The fields are evaluated on the edges of the mesh component.
   :Faces:
      The fields are evaluated on the faces of the mesh component.
   :Spline:
      The fields are evaluated on the splines in the curve component.
   :Instance:
      The fields are evaluated on the top-level instances. Realized instances are ignored.


Outputs
=======

Geometry
   Standard geometry output.
