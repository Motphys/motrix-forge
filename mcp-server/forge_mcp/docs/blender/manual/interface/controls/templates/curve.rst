.. _ui-curve-widget:

************
Curve Widget
************

.. figure:: /images/interface_controls_templates_curve_ui.png
   :align: right

   Curve widget.

The *Curve Widget* allows to intuitively map a range of input values to a set of output values
by adjusting a curve, where the X axis represents the input and the Y axis the output.


Control Points
==============

Like all curves in Blender, the curve of the *Curve Widget* is controlled using *control points*.

By default, there are two control points: one at (0.0, 0.0) and one at (1.0, 1.0),
meaning the input is mapped directly to the output (unchanged).

Move
   Simply click and drag it around.
Add
   Click anywhere on the curve where there is not already a control point.
Remove
   Select it and click the :bl-icon:`x` button at the bottom right.


Controls
========

Above the curve graph is a row of controls. These are:

:bl-icon:`zoom_in` Zoom In
   Zoom into the center of the graph to show more details and provide more accurate control.
   To navigate around the curve while zoomed in, click and drag in an empty part of the graph.
:bl-icon:`zoom_out` Zoom Out
   Zoom out of the graph to show fewer details and view the graph as a whole.
   You cannot zoom out further than the clipping region (see *Clipping* below).

:bl-icon:`downarrow_hlt` Specials
   A menu with operators to edit control points or to set properties.

   Reset View
      Resets the view of the curve.

   Extend Options
      Controls how the curve is extended before the first control point and after the last control point.

      Extend Horizontal
         Causes the curve to stay horizontal before the first point and after the last point.
      Extend Extrapolated
         Causes the curve to extrapolate before the first point and after the last point,
         based on the shape of the curve.

      .. list-table::

         * - .. figure:: /images/interface_controls_templates_curve_extend-horizontal.png

                Extend Horizontal.

           - .. figure:: /images/interface_controls_templates_curve_extend-extrapolate.png

                Extend Extrapolated.

   Reset Curve
      Resets the curve to default (removes all points added to the curve).
:bl-icon:`clipuv_hlt` Clipping Options
   Use Clipping
      Forces curve points to stay between specified values.
   Min X/Y and Max X/Y
      Set the minimum and maximum bounds of the curve points.

Below the curve are options for the selected control point:

.. _ui-curve-widget-handle-type:

Handle Type
   Controls how the control points affect the curve shape.
   It determines the interpolation of the curve segment at the selected control point.

   :Vector Handle:
      Vector handles create straight lines and sharp corners.
   :Auto Handle:
      Automatic handles that create smooth curves.
   :Auto-Clamped Handle:
      Automatic handles that create smooth curves while also preventing overshoot.
   :Free Handle:
      The handles can be moved completely independently, and thus can result in a sharp change of direction.
   :Aligned Free Handles:
      The two handles of the curve point are locked together to always point in exactly opposite directions.
      This results in a curve that is always smooth at the control point.

   .. list-table::

      * - .. figure:: /images/interface_controls_templates_curve_handle-vector.png

             Vector Handles.

        - .. figure:: /images/interface_controls_templates_curve_handle-auto.png

             Auto Handles.

        - .. figure:: /images/interface_controls_templates_curve_handle-auto-clamped.png

             Auto Clamped Handles.
X, Y
   The coordinates of the selected control point.
Delete :bl-icon:`x`
   Remove the selected control point. The first and last points cannot be deleted.
Copy/Paste :kbd:`Ctrl-C`, :kbd:`Ctrl-V`
   The whole curve can be copied from one Curve Widget to another by hovering over
   the curve graph and pressing :kbd:`Ctrl-C`, :kbd:`Ctrl-V`.
