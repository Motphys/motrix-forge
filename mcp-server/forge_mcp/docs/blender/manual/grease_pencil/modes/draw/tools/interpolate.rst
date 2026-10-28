.. _tool-grease-pencil-draw-interpolate:

***********
Interpolate
***********

.. reference::

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Interpolate`

The Interpolate tool interpolates strokes between the previous and next keyframe by adding a *single* keyframe.
When you are on a frame between two keyframes and click and drag a new breakdown keyframe will be added.
This way you define the final interpolation for the new stroke.


Usage
=====

Set the Playhead on the Timeline between the two keyframes you want to interpolate.
Click and drag from left to right to set the desired interpolation percentage
and release to confirm, a new breakdown keyframe will be added.


Tool Settings
=============

Layer
   Restrict the interpolation to Active or All layers.
Only Selected :guilabel:`Edit Mode`
   When enabled, only selected strokes will be interpolated.
Exclude Breakdowns
   Exclude existing :ref:`Breakdowns keyframes <keyframe-type>` as interpolation extremes.
Flip Mode
   Invert strokes start and end. Automatic will try to found the right mode for every stroke.
Smooth
   Amount of smoothing to apply to interpolated strokes for reducing jitter/noise.
Iterations
   Number of time to smooth newly created strokes.
