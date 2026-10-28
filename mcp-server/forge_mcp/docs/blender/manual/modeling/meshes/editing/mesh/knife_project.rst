.. _bpy.ops.mesh.knife_project:

*************
Knife Project
*************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Mesh --> Knife Project`

Knife Project is a non-interactive tool where you can use objects to cookie-cut into
one or more meshes rather than hand drawing the line. The outline of the selected objects
that *are not* in Edit Mode is projected along the view axis onto the meshes that *are*
in Edit Mode, and then cuts into the faces there. Afterwards, the resulting geometry
inside the cut gets selected.

.. note::

   The cutting objects must be curves or non-manifold meshes (e.g. flat shapes, loose edges).
   :ref:`Select Non-Manifold <bpy.ops.mesh.select_non_manifold>`
   will highlight the cutting edges of mesh objects.

Keep in mind that Knife Project works from the current view's perspective. For best results, make sure
to rotate your view to exactly the position you require before using this tool. Orthographic views such
as Right, Front, and Top are commonly used for this.

.. hint::
   :doc:`3D Viewport Alignment </editors/3dview/navigate/align>` to adjust the projection axis.

To use Knife Project, select the objects to be cut, switch to *Edit Mode*,
select the cutting objects in the Outliner (:kbd:`Ctrl-LMB`),
and choose :menuselection:`Mesh --> Knife Project`.

If Blender switches back to *Object Mode* when selecting the cutting objects,
make sure that :menuselection:`Edit --> Lock Object Modes` is checked in the topbar.
Alternatively, if you have only one cutting object, you can select it in the
viewport with :kbd:`Ctrl-LMB`.

Options
=======

Cut Through
   Projects the cut through the entire mesh, including back faces not currently visible.


Examples
========

.. list-table::

   * - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_text-before.jpg
          :width: 320px

          Before projecting from a text object.

     - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_text-after.jpg
          :width: 320px

          Resulting knife projection.

   * - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_mesh-before.jpg
          :width: 320px

          Before projecting from a mesh object.

     - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_mesh-after.jpg
          :width: 320px

          Resulting knife projection (extruded after).

   * - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_curve-before.png
          :width: 320px

          Before projecting from a 3D curve object.

     - .. figure:: /images/modeling_meshes_editing_mesh_knife-project_curve-after.jpg
          :width: 320px

          Resulting knife projection (extruded after).


Known Limitations
=================

When cutting multiple meshes in Edit Mode at once,
geometry from these meshes does not occlude separate mesh objects behind them.
