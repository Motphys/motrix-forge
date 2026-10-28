.. index:: Geometry Nodes; Braid Hair Curves

*****************
Braid Hair Curves
*****************

Deforms existing hair curves into braids using guide curves.

.. peertube:: wqJoqfqsWvT6msnD75RV2Q


Inputs
======

**Geometry**

Guide Index
   Guide index map which describes which curve to use as the center of each braid group.
   If this input is provided, it takes priority over an existing map in the ``guide_curve_index``
   attribute, and the *Guide Distance* and *Guide Mask* attribute will be unused.

Guide Distance
   Minimum distance between two guides for new guide map.

Guide Mask
   Mask for which curves are eligible to be selected as guides.

Existing Guide Map
   Use the existing guide map attribute if available. If this is false, and the *Guide Index*
   input isn't provided, the *Guide Distance* and *Guide Mask* input will be used to generate
   a new :doc:`guide map </modeling/geometry_nodes/hair/guides/create_guide_index_map>` for this node.
   Creating the guide map in a separate node or modifier gives more complete control over its creation.

Factor
   Factor by which to blend the overall effect.

Subdivision
   Subdivision level applied before deformation.

Braid Start
   Percentage along each curve to blend deformation from the root.

Radius
   Overall radius of the braids.

Shape
   Shape of the braid radius along each curve.

Factor Min
   Factor of the minimum radius of the braids.

Factor Max
   Factor of the maximum radius of the braids.

Frequency
   Frequency factor of the braids.
   This input can vary for different points of the same curve.

Thickness
   Thickness of each strand of hair.

Thickness Shape
   Shape adjustment of the strand thickness for the braids.

Shape Asymmetry
   Asymmetry of the shape adjustment of the strand thickness.

Flare Length
   Length of the flare at the end of the braid.

Flare Opening
   Opening radius of the flare at the tip of the braid.

Hair Tie
   Geometry used for the hair tie instance (priority).

Hair Tie
   Object used for the hair tie instance.

Hair Tie Scale
   Scale of the hair tie instance.


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

Flare Parameter
   Parameter from 0 to 1 along the flare.

Strand Index
   Index of the group of hair in the braid that each hair curve belongs to.
