.. index:: Geometry Nodes; Curl Hair Curves

****************
Curl Hair Curves
****************

Deforms existing hair curves into curls using guide curves.

.. peertube:: 3AcYeH2nqMzjEXFUNqTbj7


Inputs
======

**Geometry**

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

Subdivision
   Subdivision level applied before deformation.

Curl Start
   Percentage along each curve to blend deformation from the root.

Radius
   Overall radius of the curls.

Factor Start
   Factor for the radius at the curl start.

Factor End
   Factor for the radius at the curl end.

Frequency
   Frequency factor of the curls.
   This input can vary for different points of the same curve.

Random Offset
   Amount of random offset per curve.

Seed
   Random Seed for the operation.


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
