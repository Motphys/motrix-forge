.. index:: Geometry Nodes; Attach Hair Curves to Surface

*****************************
Attach Hair Curves to Surface
*****************************

Attaches hair curves to a surface mesh.

.. note::

   This node/modifier will not function without the *Surface* geometry/object and *Surface UV Map* inputs.

.. peertube:: keeNa3Rpe7grQvX5d35w8H


Inputs
======

Geometry
   Input Geometry (only curves will be affected).

Surface
   Surface Geometry to attach hair curves to. This input takes priority over the corresponding object input, if used.

Surface
   Surface Object to attach to (needs to have matching transforms).

Surface UV Map
   Surface UV map stored on the mesh used for finding curve attachment locations.

Surface Rest Position
   Set the surface mesh into its rest position before attachment.

   .. tip::

      In a typical hair generation setup, this node or modifier will be
      combined with the :doc:`/modeling/geometry_nodes/curve/operations/deform_curves_on_surface`.
      If that operation comes after this one, it makes sense to turn this option on so the
      position used is the pre-deformed position consistent with the expectations for the
      deformation's input.

Sample Attachment UV
   Sample the surface UV map at the attachment point.

Snap to Surface
   Snap the root of each curve to the closest surface point.

Align to Surface Normal
   Align the curve to the surface normal (need guide as reference).

Blend along Curve
   Blend deformation along each curve from the root.


Properties
==========

This node has no properties.


Outputs
=======

**Geometry**

Surface UV Coordinate
   Surface UV coordinate at the attachment point.

Surface Normal
   Surface normal at the attachment point.
