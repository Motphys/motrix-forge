.. index:: Modeling Modifiers; Multiresolution Modifier
.. _bpy.types.MultiresModifier:

************************
Multiresolution Modifier
************************

The *Multiresolution* modifier (often shortened to "Multires")
gives you the ability to subdivide a mesh similarly
to the :doc:`Subdivision Surface </modeling/modifiers/generate/subdivision_surface>` modifier,
but also allows you to edit the new subdivision levels in
:doc:`Sculpt Mode </sculpt_paint/sculpting/introduction/adaptive>`.

.. note::

   *Multiresolution* is the only modifier that cannot be repositioned in the stack after any modifier that will
   change geometry or other object data (i.e. all *Generate*, some *Modify* and some *Simulate* modifiers
   cannot come before the *Multiresolution*).

Deform modifiers will be applied onto the Multires subdivision levels instead of the base mesh,
if they come after the Multires.

.. tip::

   This is especially useful for re-projecting details from another sculpt
   with a :doc:`Shrinkwrap modifier </modeling/modifiers/deform/shrinkwrap>`. For the best result make sure to set the
   wrap method to *Project*, snap mode to *Above Surface* and enable *Negative*.


Options
=======

.. figure:: /images/modeling_modifiers_generate_multiresolution_panel.png
   :align: right
   :width: 300px

   The Multiresolution modifier.

Levels Viewport
   Set the level of subdivisions to show in the viewport.
Sculpt
   Set the level of subdivisions to use specifically in Sculpt Mode.
   While in Sculpt mode use :kbd:`Alt-1` to decrease the level or :kbd:`Alt-2` to increase.
Render
   Set the level of subdivisions to show when rendering.

Sculpt Base Mesh
   Deform the unsubdivided base mesh instead of the higher levels.
   Meanwhile the set level will be previewed. This allows you to
   make much broader changes in visual context to higher sculpted details
   without creating surface noise and artifacts.

Optimal Display
   Only display the edges of the original geometry.
   So when rendering the wireframe of this object, the wires of the subdivided edges will be skipped.


Subdivision
-----------

.. _bpy.ops.object.multires_subdivide:

Subdivide
   Creates a smooth level of subdivision
   (using the default Catmull-Clark algorithm).

Simple
   Creates a level of subdivision with unsmoothed base mesh edges (using a simple interpolation by subdividing edges
   without any smoothing).
Linear
   Creates a completely unsmoothed level of subdivision (using linear interpolation of the current sculpted
   displacement).

.. _bpy.ops.object.multires_unsubdivide:

Unsubdivide
   Rebuild a lower subdivision level of the current base mesh.

.. _bpy.ops.object.multires_higher_levels_delete:

Delete Higher
   Deletes all subdivision levels that are higher than the current one.


Shape
-----

.. _bpy.ops.object.multires_reshape:

Reshape
   Copy the shape of another object onto the multires levels by copying its vertex coordinates.

   To use it, first select a different mesh object with matching topology and vertex indices,
   then :kbd:`Shift` select the object you wish to copy vertex coordinates to, and click *Reshape*.

.. _bpy.ops.object.multires_base_apply:

Apply Base
   Modifies the original unsubdivided mesh to match the form of the subdivided mesh.


Generate
--------

.. _bpy.ops.object.multires_rebuild_subdiv:

Rebuild Subdivisions
   Rebuilds all possible subdivisions levels to generate a lower resolution base mesh.
   This is used to create an optimized multiresolution version of a preexisting sculpt.
   This option is only available when no subdivision level have been created through the modifier.

.. _bpy.ops.object.multires_external_save:

Save External
   Saves displacements to an external ``.btx`` file.


Advanced
--------

Quality
   How precisely the vertices are positioned (relatively to their theoretical position),
   can be lowered to get a better performance when working on high-poly meshes.

UV Smooth
   How to handle UVs during subdivision.

   :None: UVs remain unchanged.
   :Keep Corners: UV islands are smoothed, but their boundary remain unchanged.
   :Keep Corners, Junctions:
      UVs are smoothed, corners on discontinuous boundary and junctions of three or more regions are kept sharp.
   :Keep Corners, Junctions, Concave:
      UVs are smoothed, corners on discontinuous boundary,
      junctions of three or more regions and darts and concave corners are kept sharp.
   :Keep Boundaries: UVs are smoothed, boundaries are kept sharp.
   :All: UVs and their boundaries are smoothed.

Boundary Smooth
   Controls how open boundaries (and corners) are smoothed.

   :All: Smooth boundaries, including corners.
   :Keep Corners: Smooth boundaries, but corners are kept sharp.

Use Creases
   Use the :ref:`modifiers-generate-subsurf-creases` values stored in edges to control how smooth they are made.

Use Custom Normals
   Interpolates existing :ref:`modeling_meshes_normals_custom` of the resulting mesh.


Usage
=====

Baking
------

Baking converts high-resolution geometry details such
as sculpted displacement or surface normals into a 2D texture map.
These textures can then be used on a lower-resolution version of the mesh to simulate
high-detail geometry without the performance cost of actually subdividing the mesh at runtime.

This is an essential step in workflows where high-resolution details are baked
into textures for use on a lower-resolution base mesh, such as in real-time rendering or game engines.

To generate a displacement or normal map, use the
:ref:`Bake from Multires <bpy.types.RenderSettings.use_bake_multires>` render feature.
This feature compares two resolution levels of the modifier:

- Viewport Level is treated as the low-resolution base mesh.
- Render Level is treated as the high-resolution detail mesh.

The resulting normal or displacement map represents the difference between these two levels.

.. important::

   To bake correctly, the Viewport Levels of the Multiresolution modifier must be set to 0.
   This ensures the bake uses the original base mesh as the low-resolution target.
   Sculpted details are taken from the Render Levels.

   If the Viewport Level is higher than 0, the bake may not produce correct results,
   as the low-resolution geometry will already include some displacement.

.. tip::

   Make sure the object has proper UV unwrapping before baking,
   and that the correct image node is selected in the Shader Editor.

For more details on the general baking process, see: :doc:`/render/cycles/baking`.
