.. index:: Geometry Nodes; Generate Hair Curves

********************
Generate Hair Curves
********************

Generates new hair curves on a surface mesh.
The curves are generated from scratch at point locations; if creating curves that depend on
existing curves is desired, the :doc:`/modeling/geometry_nodes/hair/generation/interpolate_hair_curves`
is a better choice.

.. note::

   This node/modifier will not function without the *Surface* geometry/object and *Surface UV Map* inputs.

.. peertube:: nkB43evNMakLmvuoExgKuF


Inputs
======

Surface
   Surface geometry for generation. This input takes priority over the corresponding object input if both are
   provided.

Surface
   Surface object for generation (The transforms of this object must match the modifier object).

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

Hair Length
   Length of the generated hair curves.

Hair Material
   Material of the generated hair curves.

Control Points
   Amount of control points of the generated hair curves.

Poisson Disk Distribution
   Use poisson disk distribution method to keep a minimum distance.
   See the :doc:`/modeling/geometry_nodes/point/distribute_points_on_faces` for more information.

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

**Curves**

Surface Normal
   Normal direction of the surface mesh at the attachment point.
