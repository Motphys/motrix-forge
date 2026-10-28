
*******
Sidebar
*******

View
====

.. reference::

   :Panel:     :menuselection:`Sidebar region --> View`


Backdrop
--------

.. figure:: /images/compositing_sidebar_view.png
   :width: 200px
   :align: right

   Backdrop panel.

The backdrop is the output of a Viewer node in the background of the Compositor.
For example, when :kbd:`Shift-Ctrl-LMB` on an Image node, it displays a preview of the image,
or on a Mix node, will show the result of the mixing.
You can toggle the backdrop by clicking the checkbox in the *Backdrop* panel title
or by clicking on the *Backdrop* button in the header.

Channels
   The color channels to display of the backdrop image.
Zoom :kbd:`Alt-V` :kbd:`V`
   Sets the size of the backdrop image.
Offset
   Change the screen space position of the backdrop.
Move :kbd:`Alt-MMB`
   Changes the position of the backdrop.
Fit
   Scales the backdrop to fit the size of the Compositor.
Reset Backdrop
   Sets back to the default values of Zoom to 1 and Offset to 0.


Options
=======

.. reference::

   :Panel:     :menuselection:`Sidebar region --> Options`


Performance
-----------

.. figure:: /images/compositing_sidebar_options.png
   :width: 200px
   :align: right

   Performance panel.

This panel helps you tweak the performance of the Compositor.

.. include:: /render/eevee/render_settings/performance.rst
   :start-after: .. --- copy below this line ---
   :end-before: .. --- end copy above this line - compositor sidebar ---

.. _bpy.types.CompositorNodeTree.use_viewer_border:

Viewer Region
   This allows to set an area of interest for the backdrop.
   Press :kbd:`Ctrl-B` and select a rectangular area in the preview
   which will become the next preview in the backdrop.
   :kbd:`Ctrl-Alt-B` discards the region back to a full preview.
   This is only a preview option, final compositing during a render ignores this region.
