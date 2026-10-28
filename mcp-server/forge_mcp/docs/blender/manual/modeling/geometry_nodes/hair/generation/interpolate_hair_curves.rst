.. index:: Geometry Nodes; Interpolate Hair Curves

***********************
Interpolate Hair Curves
***********************

Interpolates existing guide curves on a surface mesh.
The :doc:`/modeling/geometry_nodes/hair/generation/duplicate_hair_curves` is a similar option with simpler
behavior that may offer better performance.

.. note::

   This node/modifier will not function without the *Surface* geometry/object and *Surface UV Map* inputs.

.. peertube:: 4dt7vp3qmry5MPZC3usxVb

Inputs
======

Geometry
   Input Geometry (only curves will be affected).

Surface
   Surface geometry for generation. This input takes priority over the corresponding object input if both are
   provided.

Surface
   Surface object for generation (Needs matching transforms).

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

Follow Surface Normal
   Align the interpolated curves to the surface normal.

Part by Mesh Islands
   Use mesh islands of the surface geometry for parting.

Interpolation Guides
   Amount of guides to be used for interpolation per curve.

Distance to Guides
   Distance around each guide to spawn interpolated curves.

Poisson Disk Distribution
   Use poisson disk distribution method to keep a minimum distance.

Density
   Surface density of generated hair curves.

Density Mask
   Factor applied on the density for curve distribution.

Mask Texture
   Discard points based on an mask texture after distribution.
   The image is sampled with the *Surface UV Map* input.

   .. tip::

      The accuracy of sampling the image doesn't depend on the density of the surface mesh's vertices
      because it is sampled after the curve root points are generated, the accuracy . However, using
      the *Density Mask* input instead can give better performance. Using them in combination can
      give the benefits of both methods.

Viewport Amount
   Factor applied on the density for the viewport.

Seed
   Random seed for the operation.


Properties
==========

This node has no properties.


Outputs
=======

**Geometry**

Guide Index
   Index of the main guide curve per curve.

Surface Normal
   Normal direction of the surface mesh at the attachment point.
