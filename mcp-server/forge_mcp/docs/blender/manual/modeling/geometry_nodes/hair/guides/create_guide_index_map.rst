.. index:: Geometry Nodes; Create Guide Index Map

**********************
Create Guide Index Map
**********************

Creates an integer attribute named ``guide_curve_index`` that stores
the nearest guide curve for every curve to its nearest guide via index.

Other nodes in the :doc:`/modeling/geometry_nodes/hair/guides/index`
category can generate guide maps themselves for convenience, but the behavior is
always the same as this node.

.. peertube:: cPLeMHSnPYidQmJezdhcyL


Inputs
======

**Geometry**

Guides
   Guide Curves or Points used for the selection of Guide Curves.

Guide Distance
   Minimum distance between two guides.

Guide Mask
   Mask for which curve are eligible to be selected as guides.

Group ID
   ID to group together curves for guide map creation.
   Curves will only choose a guide with the same ID value.


Properties
==========

This node has no properties.


Outputs
=======

Geometry
   Output geometry including the new map attribute and the guide selection
   :ref:`anonymous attribute <anonymous-attributes>` as well. This geometry
   includes the guide curves, they are not separated.

Guide Curves
   Output geometry including only the selected guide curves.

Guide Index
   The index of the closest curve with the same *Group ID* value.

Guide Selection
   A selection in the *Geometry* output set to true for only the curves
   that were chosen as guides.
