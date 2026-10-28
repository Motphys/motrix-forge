.. index:: Geometry Nodes; Clump Hair Curves

*****************
Clump Hair Curves
*****************

Clumps together existing hair curves using guide curves.

.. peertube:: gnhg72C8JoNYmNy441QHgt


Inputs
======

Geometry
   Input Geometry (only curves will be affected).

Guide Index
   Guide index map witch describes which curve to use as the center of each braid group.
   If this input is provided, it priority over an existing map in the ``guide_curve_index``
   attribute, and the *Guide Distance* and *Guide Mask* attribute will be unused.

Guide Distance
   Minimum distance between two guides for new guide map.

Guide Mask
   Mask for which curve are eligible to be selected as guides.

Existing Guide Map
   Use the existing guide map attribute if available. If this is false, and the *Guide Index*
   input isn't provided, the *Guide Distance* and *Guide Mask* input will be used to generate
   a new :doc:`guide map </modeling/geometry_nodes/hair/guides/create_guide_index_map>` for this node.
   Creating the guide map in a separate node or modifier gives more complete control over its creation.

Factor
   Factor to blend overall effect.

Shape
   Shape of the influence along curves (0=constant, 0.5=linear).

Tip Spread
   Distance of random spread at the curve tips.

Clump Offset
   Offset of each clump in a random direction.

Distance Falloff
   Falloff distance for the clumping effect (0 means no falloff).

Distance Threshold
   Distance threshold for the falloff around the guide.

Seed
   Random seed for the operation.

Preserve Length
   Preserve each curve's length during deformation.


Properties
==========

This node has no properties.


Outputs
=======

**Geometry**

Guide Index
   Guide index map that was used for the operation.
   If a new guide map is created by this node, it will be stored for
   this output.
