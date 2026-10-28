.. index:: Editors; Timeline
.. _bpy.types.SpaceTimeline:
.. _bpy.ops.time:

********
Timeline
********

The *Timeline* editor is used to jump to different frames, manipulate keyframes,
and control animation playback.

.. figure:: /images/editors_timeline_interface.png

   The Timeline.


Main View
=========

The X axis represents time, with the numbers 0/50/100/... being frame numbers.
The blue line is the *Playhead* indicating the current frame,
and the diamond shapes are *Keyframes*, points where you specified
a certain value for a certain property at a certain time.


Adjusting the View
------------------

Panning is done by dragging :kbd:`MMB`.

Zooming is done by dragging :kbd:`Ctrl-MMB`, rolling the mouse :kbd:`Wheel`,
or pressing :kbd:`NumpadMinus`/:kbd:`NumpadPlus`.

You can also use the scrollbars located at the bottom and the right of the editor.

.. _playhead:

Playhead
--------

.. figure:: /images/editors_timeline_cursor.png
   :align: right

   Playhead.

The *Playhead* is the blue vertical line showing the current frame number.

It can be moved to a new position by clicking or
dragging :kbd:`LMB` in the scrubbing area at the top or by
click and drag :kbd:`Shift-RMB` anywhere in the timeline.

While dragging it can snap to elements of the editor in which it is dragged.
- Seconds
- Frames
- Markers
- Strips
- Keys

It is only possible to snap to elements that are visible in the editor in which the playhead is dragged.
For example having "Strips" enabled but dragging in the Graph Editor will do nothing.
Snapping can be toggled during scrubbing by holding down :kbd:`Ctrl`.

Snapping to seconds or frames can have a custom increment for example snapping to every third frame.
This is always relative to the first frame of the scene and ignores the preview range.
In contrast to the other snapping options, seconds and frames will always snap to the closest position,
regardless of the snap distance set. When mixing options, the system will first try to snap to
elements that are snapped by distance. Only if no element is close enough will it snap to seconds or frames.

You can also move it in single-frame increments by pressing :kbd:`Left` or :kbd:`Right` or :kbd:`Alt-Wheel`.
To jump to the beginning or end frame (of the ends of the preview range if that is active)
press :kbd:`Shift-Left` or :kbd:`Shift-Right`.


.. _playhead-snapping:

Snapping
^^^^^^^^

.. reference::

   :Menu:      :menuselection:`Header --> Playhead Snapping`

Playhead snapping helps you position the playhead precisely when scrubbing the timeline
by snapping it to specific elements like frames, markers, or keyframes.

.. _bpy.types.ToolSettings.use_snap_playhead:

Use Snapping
   Enables or disables snapping behavior when moving the playhead.

.. _bpy.types.ToolSettings.playhead_snap_distance:

Snap Distance
   The maximum distance (in pixels) the playhead can be from a target before snapping to it.

.. _bpy.types.ToolSettings.snap_playhead_element:

Snap Target
   Specifies which elements the playhead can snap to:

   :Frames: Snap to frame intervals.
   :Seconds: Snap to second intervals.
   :Markers: Snap to timeline markers.
   :Keyframes: Snap to animation keyframes.
   :Strips: Snap to the start and end points of strips (e.g. in the Video Sequencer).

.. _bpy.types.ToolSettings.snap_playhead_frame_step:

Frame Step :guilabel:`Frames`
   The interval in frames between each snap point when using the *Frames* target.

.. _bpy.types.ToolSettings.snap_playhead_second_step:

Second Step :guilabel:`Seconds`
   The interval in seconds between each snap point when using the *Seconds* target.


Frame Range
-----------

The *Frame Range* determines the length of the scene's animation.
By default, it's set to start at frame 1 and end at frame 250.
You can change this using the Start/End inputs in the Timeline header,
or in the :doc:`Output Properties </render/output/properties/frame_range>`.


Keyframes
---------

By default, the timeline only shows keyframes for selected items.
You can make it show all keyframes by unchecking
:menuselection:`View --> Only Show Selected`.

You can click a keyframe to select it (and deselect all others),
or click it while holding :kbd:`Shift` to add it to the selection
(or remove it if it was already selected). You can also drag a box
to select multiple keyframes in one go.

To move the selected keyframes, simply drag one of them. Alternatively,
you can press :kbd:`G`, move the mouse, and click :kbd:`LMB` to confirm
(or :kbd:`RMB` to cancel). You can also press :kbd:`S` to scale the keyframes
in relation to the Playhead.


Markers
-------

See the :doc:`Markers page </animation/markers>` for more information.


Header
======

.. _animation-editors-timeline-headercontrols:

.. figure:: /images/editors_timeline_header.png

   Popovers for Playback and Keying; transport controls; and frame controls

Popovers
--------

.. _timeline-playback:

Playback Popover
^^^^^^^^^^^^^^^^

.. figure:: /images/editors_timeline_playback.png

.. _bpy.types.Scene.sync_mode:

Sync
   .. figure:: /images/editors_timeline_red-fps.png
      :figwidth: 109px
      :align: right

      3D Viewport red FPS.

   If animation playback can't keep up with the desired :ref:`Frame Rate <bpy.types.RenderSettings.fps>`,
   the actual frame rate (shown in the top left corner of the 3D Viewport) will turn red,
   and the *Sync* option determines how the situation should be handled.

   Play Every Frame
      Play every frame, even if this results in the animation playing slower than intended.
   Frame Dropping
      Drop frames if playback becomes slower than the scene's frame rate.
   Sync to Audio
      Drop frames if playback becomes too slow to remain synced with audio.

Audio
   Scrubbing
      Play bits of the sound in the animation (if there is any) while you drag the Playhead around.
   Play Audio
      Uncheck to mute all sound.

Playback
   Limit to Frame Range
      Don't allow moving the Playhead outside of the Frame Range using the mouse.

   .. _bpy.types.Screen.use_follow:

   Follow Current Frame
      Automatically pan the view to catch up when the Playhead goes off screen.

.. _bpy.types.Screen.use_play:

Play In
   Which editors to update on each animation frame. If an editor is unchecked,
   it'll only be updated once playback stops (with some exceptions where it'll
   update on each frame anyway). When starting playback in either the
   :doc:`Graph Editor </editors/graph_editor/introduction>`,
   :doc:`Dope Sheet </editors/dope_sheet/introduction>` or the
   :doc:`NLA Editor</editors/nla/introduction>`,
   all editors will play back regardless of the settings.
   This is a feature requested by animators to easily play back all views.

.. _bpy.types.Scene.show_subframe:

Show -- Subframes
   Display and allow setting fractional frame values for the current frame.

Set Start/End Frame
   Set the scene's start/end frame to the current frame.
   If the Preview Range is active (see `Frame Controls`_), that one is changed instead.

.. _timeline-keying:

Keying Popover
^^^^^^^^^^^^^^

.. figure:: /images/editors_timeline_keying.png

The *Keying* popover contains options that affect keyframe insertion.

.. _bpy.types.KeyingSetsAll.active:

Active Keying Set
   .. figure:: /images/editors_timeline_keying-sets.png
      :align: right

      Timeline Keying Sets.

   A *Keying Set* is a named collection of animatable properties. If you select
   one and then press :kbd:`I` while not hovering over any input field,
   Blender will create keyframes for the properties in that keying set.

   If you don't have a keying set selected, you'll get keyframes on a default
   set of properties instead (e.g. Location/Rotation/Scale for objects).

   There are a number of predefined keying sets, but you can also create your own
   in the :ref:`Keying Sets <bpy.types.KeyingSets>` panel.

   Insert Keyframes :bl-icon:`key_hlt` :kbd:`I`
      Insert keyframes on the current frame.
   Delete Keyframes :bl-icon:`key_dehlt` :kbd:`Alt-I`
      Delete keyframes on the current frame.

.. _bpy.types.ToolSettings.keyframe_type:

New Keyframe Type
   The :ref:`keyframe type <keyframe-type>` for newly created keyframes.

.. _bpy.types.ToolSettings.use_keyframe_cycle_aware:

Cycle-Aware Keying
   When inserting keyframes into :ref:`trivially cyclic curves <bpy.types.FModifierCycles>`,
   special handling is applied to preserve the cycle integrity (most useful while tweaking an established cycle):

   - If a key insertion is attempted outside of the main time range of the cycle,
     it is remapped back inside the range.
   - When overwriting one of the end keys, the other one is updated accordingly.

   In addition, when adding a new curve into an action with a
   :ref:`Manual Frame Range <bpy.types.Action.use_frame_range>`
   and *Cyclic Animation* enabled, the curve is automatically made cyclic with the period matching the frame range.
   For convenience, this check and conversion is also done before adding the second keyframe to such a curve.


.. Move to some content to animation?
.. _bpy.types.ToolSettings.use_keyframe_insert_auto:

Auto Keying
^^^^^^^^^^^

.. figure:: /images/editors_timeline_keyframes-auto.png
   :align: right

   Auto Keying button.

When the record button (:bl-icon:`rec`) is enabled, Blender will automatically create keyframes on the current
frame whenever you transform an object or bone in the 3D Viewport (or change one of its transform properties
in the :doc:`Properties Editor </editors/properties_editor>`).

One special use case is to record a camera path as you fly through the scene.
See :ref:`Fly/Walk Navigation <3dview-fly-walk>`.

.. note::

   Auto Keying only works for transform properties (Location, Rotation, Scale).
   It won't create a keyframe if you change, say, the color of a material --
   you still have to do that manually.

.. _bpy.types.ToolSettings.auto_keying_mode:

Mode
   Add & Replace
      Add or replace keyframes as needed.
   Replace
      Only replace existing keyframes.

.. _bpy.types.ToolSettings.use_keyframe_insert_keyingset:

Only Active Keying Set
   By default, Auto Keying will create keyframes even for properties that are not in the
   :ref:`active keying set <bpy.types.KeyingSetsAll.active>`. Use this checkbox to change that.

.. _bpy.types.ToolSettings.use_record_with_nla:

Layered Recording
   Adds a new :doc:`NLA Track </editors/nla/tracks>` for every pass made over the animation
   to allow non-destructive tweaking.


Menus
-----

.. _timeline-view-menu:

View Menu
^^^^^^^^^

Adjust Last Operation
   Displays a pop-up panel to alter properties of the last
   completed operation. See :ref:`bpy.ops.screen.redo_last`.
Channels
   Show or hide the Channels region (the tree of objects and animatable properties on the left).

----------

Frame All :kbd:`Home`
   Pans and zooms the view so that all keyframes are visible.

.. _bpy.ops.anim.scene_range_frame:

Frame Scene/Preview Range
   Reset the horizontal view to the current scene frame range,
   taking the preview range into account if it is active.
Go to Current Frame :kbd:`Numpad0`
   Centers the Timeline to the Playhead.

----------

Show Markers
   Shows the Markers region (if any markers are defined).
   When disabled, the `Marker Menu`_ is also hidden and marker operators are not
   available in this editor.
Show Seconds :kbd:`Ctrl-T`
   Shows the time on the X axis and the *Playhead* as timestamps instead of frame numbers.
   A timestamp such as ``01:03+02`` means "1 minute, 3 seconds, 2 frames."
Sync Visible Range
   Synchronizes the horizontal panning and scale of the editor
   with other time-based editors that also have this option enabled.
   That way, they always show the same section of time.

----------

Only Show Selected
   Only show keyframes related to the selected items.
   This could be objects, bones, nodes, and so on.

.. note::
   If this option is enabled, the Timeline may not show all :doc:`material </render/materials/introduction>`
   keyframes of the selected objects. Instead, it only shows the keyframes belonging to the selected nodes
   in the :doc:`/editors/shader_editor`.

Only Show Errors
   Only show curves and drivers that are disabled or have errors.
   Useful for debugging.

----------

Cache
   Show Cache
      Which simulation caches to show on the timeline.

      Baked simulations will be shown as fully opaque, cached simulations will be slightly transparent,
      and invalid caches will be slightly transparent with dark diagonal stripes.

   .. figure:: /images/editors_timeline_cache.png

      Timeline Cache.

----------

Area
   Area controls. See the :doc:`user interface </interface/window_system/areas>`
   documentation for more information.


Marker Menu
^^^^^^^^^^^

:doc:`Markers </animation/markers>` are used to denote frames with key points or significant events
within an animation. Like in most animation editors, they're shown at the bottom of the Timeline.

.. figure:: /images/editors_graph-editor_introduction_markers.png

   Markers in an animation editor.

For descriptions of the different marker tools, see :ref:`Editing Markers <animation-markers-editing>`.


.. _bpy.ops.screen.frame_jump:
.. _bpy.ops.screen.keyframe_jump:
.. _bpy.ops.screen.animation_play:

Transport Controls
------------------

These buttons are used to set the current frame and control playback.

.. figure:: /images/editors_timeline_player-controls.png
   :align: right

   Transport controls.

Jump to Start :bl-icon:`rew` :kbd:`Shift-Left`
   Sets the Playhead to the start of the frame range.
Jump to Previous Keyframe :bl-icon:`prev_keyframe` :kbd:`Down`
   Moves the Playhead to the previous keyframe.
Rewind :bl-icon:`play_reverse` :kbd:`Shift-Ctrl-Spacebar`
   Starts playing the animation in reverse.
Play :bl-icon:`play` :kbd:`Spacebar`
   Starts playing the animation.
Jump to Next Keyframe :bl-icon:`next_keyframe` :kbd:`Up`
   Moves the Playhead to the next keyframe.
Jump to End :bl-icon:`ff` :kbd:`Shift-Right`
   Sets the Playhead to the end of the frame range.
Pause :bl-icon:`pause` :kbd:`Spacebar`
   Stops playing the animation.


Frame Controls
--------------

.. _bpy.types.Scene.frame_current:

Current Frame :kbd:`Alt-Wheel`
   The number of the frame that's currently being displayed in the 3D Viewport.
   This is also the location of the Playhead.

.. _bpy.types.Scene.use_preview_range:

Use Preview Range :bl-icon:`preview_range`
   The Preview Range is an alternative Frame Range that you can use for focusing on a
   particular part of the animation. It lets you repeatedly play a short segment without
   having to manually rewind or change the frame range of the entire scene.

   This range only affects the preview in the 3D Viewport; it doesn't affect rendering.

   The boundaries of the Preview Range are shown in dark orange. You can quickly configure
   and enable it by pressing :kbd:`P` and dragging a box. To disable it,
   you can press :kbd:`Alt-P`.

Start, End
   The start/end frame of the scene (or the preview range, if active).
