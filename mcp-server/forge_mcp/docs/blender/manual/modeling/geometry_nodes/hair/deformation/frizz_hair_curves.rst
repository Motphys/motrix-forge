.. index:: Geometry Nodes; Frizz Hair Curves

*****************
Frizz Hair Curves
*****************

Deforms hair curves using a random vector per point to frizz them.

.. peertube:: jdiMkR9aQnCm1QXc71Fz5h


Inputs
======

Geometry
   Input Geometry (only curves will be affected).

Cumulative Offset
   Apply offset cumulatively (previous points affect points after).

Factor
   Factor to blend overall effect.

Distance
   Overall distance factor for the deformation.

Shape
   Shape of the influence along curves (0=constant, 0.5=linear).

Seed
   Random Seed for the operation.

Preserve Length
   Preserve each curve's length during deformation.


Properties
==========

This node has no properties.


Outputs
=======

**Geometry**

Offset Vector
   Vector by which each point was offset during deformation.
