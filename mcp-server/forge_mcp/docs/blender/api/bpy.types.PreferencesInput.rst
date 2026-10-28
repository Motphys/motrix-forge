PreferencesInput(bpy_struct)
============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PreferencesInput(bpy_struct)

   Settings for input devices

   .. attribute:: drag_threshold

      Number of pixels to drag before a drag event is triggered for keyboard and other non mouse/tablet input (otherwise click events are detected)

      :type: int in [1, 255], default 30

   .. attribute:: drag_threshold_mouse

      Number of pixels to drag before a drag event is triggered for mouse/trackpad input (otherwise click events are detected)

      :type: int in [1, 255], default 3

   .. attribute:: drag_threshold_tablet

      Number of pixels to drag before a drag event is triggered for tablet input (otherwise click events are detected)

      :type: int in [1, 255], default 10

   .. attribute:: invert_mouse_zoom

      Invert the axis of mouse movement for zooming

      :type: boolean, default False

   .. attribute:: invert_zoom_wheel

      Swap the Mouse Wheel zoom direction

      :type: boolean, default False

   .. attribute:: mouse_double_click_time

      Time/delay (in ms) for a double click

      :type: int in [1, 1000], default 350

   .. attribute:: mouse_emulate_3_button_modifier

      Hold this modifier to emulate the middle mouse button

      :type: enum in [``'ALT'``, ``'OSKEY'``], default ``'ALT'``

   .. attribute:: move_threshold

      Number of pixels to before the cursor is considered to have moved (used for cycling selected items on successive clicks)

      :type: int in [0, 255], default 2

   .. attribute:: navigation_mode

      Which method to use for viewport navigation

      :type: enum in :ref:`rna_enum_navigation_mode_items`, default ``'WALK'``

   .. attribute:: ndof_deadzone

      Threshold of initial movement needed from the device's rest position

      :type: float in [0, 1], default 0.0

   .. attribute:: ndof_fly_helicopter

      Device up/down directly controls the Z position of the 3D viewport

      :type: boolean, default False

   .. attribute:: ndof_lock_camera_pan_zoom

      Pan/zoom the camera view instead of leaving the camera view when orbiting

      :type: boolean, default True

   .. attribute:: ndof_lock_horizon

      Lock Horizon forces the horizon to be kept leveled as it currently is

      :type: boolean, default True

   .. attribute:: ndof_navigation_mode

      3D Mouse Navigation Mode

      * ``OBJECT``
        Object -- This mode is like reaching into the screen and holding the model in your hand. Push the 3D Mouse cap left, and the model moves left. Push right and the model moves right.
      * ``FLY``
        Fly -- Enables using the 3D Mouse as if it is a camera. Push into the scene and the camera moves forward into the scene. You are entering the scene as if flying around in it. This also inverts pan & zoom for 2D views.

      :type: enum in [``'OBJECT'``, ``'FLY'``], default ``'OBJECT'``

   .. attribute:: ndof_orbit_center_auto

      Auto sets the orbit center dynamically. When the complete model is in view, the center of volume of the whole model is used as the rotation point. When you move closer, the orbit center will be set on an object close to your center of the view.

      :type: boolean, default True

   .. attribute:: ndof_orbit_center_selected

      Selected Item forces the orbit center to only take the currently selected objects into account.

      :type: boolean, default False

   .. attribute:: ndof_orbit_sensitivity

      Overall sensitivity of the 3D Mouse for orbiting

      :type: float in [0.01, 40], default 4.0

   .. attribute:: ndof_panx_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_pany_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_panz_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_rotx_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_roty_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_rotz_invert_axis

      :type: boolean, default False

   .. attribute:: ndof_sensitivity

      Overall sensitivity of the 3D Mouse for panning

      :type: float in [0.01, 40], default 4.0

   .. attribute:: ndof_show_guide_orbit_axis

      Display the center and axis during rotation

      :type: boolean, default False

   .. attribute:: ndof_show_guide_orbit_center

      Display the orbit center during rotation

      :type: boolean, default True

   .. attribute:: ndof_zoom_direction

      Which axis of the 3D Mouse cap zooms the view

      * ``NDOF_ZOOM_FORWARD``
        Forward/Backward -- Zoom by pulling the 3D Mouse cap upwards or pushing the cap downwards.
      * ``NDOF_ZOOM_UP``
        Up/Down -- Zoom by pulling the 3D Mouse cap upwards or pushing the cap downwards.

      :type: enum in [``'NDOF_ZOOM_FORWARD'``, ``'NDOF_ZOOM_UP'``], default ``'NDOF_ZOOM_FORWARD'``

   .. attribute:: pressure_softness

      Adjusts softness of the low pressure response onset using a gamma curve

      :type: float in [-inf, inf], default 0.0

   .. attribute:: pressure_threshold_max

      Raw input pressure value that is interpreted as 100% by Blender

      :type: float in [0, 1], default 1.0

   .. attribute:: tablet_api

      Select the tablet API to use for pressure sensitivity (may require restarting Blender for changes to take effect)

      * ``AUTOMATIC``
        Automatic -- Automatically choose Wintab or Windows Ink depending on the device.
      * ``WINDOWS_INK``
        Windows Ink -- Use native Windows Ink API, for modern tablet and pen devices. Requires Windows 8 or newer..
      * ``WINTAB``
        Wintab -- Use Wintab driver for older tablets and Windows versions.

      :type: enum in [``'AUTOMATIC'``, ``'WINDOWS_INK'``, ``'WINTAB'``], default ``'AUTOMATIC'``

   .. attribute:: touchpad_scroll_direction

      Scroll direction (Wayland only)

      * ``TRADITIONAL``
        Traditional -- Traditional scroll direction.
      * ``NATURAL``
        Natural -- Natural scroll direction.

      :type: enum in [``'TRADITIONAL'``, ``'NATURAL'``], default ``'TRADITIONAL'``

   .. attribute:: use_auto_perspective

      Automatically switch between orthographic and perspective when changing from top/front/side views

      :type: boolean, default True

   .. attribute:: use_drag_immediately

      Moving things with a mouse drag confirms when releasing the button

      :type: boolean, default True

   .. attribute:: use_emulate_numpad

      Main 1 to 0 keys act as the numpad ones (useful for laptops)

      :type: boolean, default False

   .. attribute:: use_mouse_continuous

      Let the mouse wrap around the view boundaries so mouse movements are not limited by the screen size (used by transform, dragging of UI controls, etc.)

      :type: boolean, default True

   .. attribute:: use_mouse_depth_navigate

      Use the depth under the mouse to improve view pan/rotate/zoom functionality

      :type: boolean, default False

   .. attribute:: use_mouse_emulate_3_button

      Emulate Middle Mouse with Alt+Left Mouse

      :type: boolean, default False

   .. attribute:: use_multitouch_gestures

      Use multi-touch gestures for navigation with touchpad, instead of scroll wheel emulation

      :type: boolean, default True

   .. attribute:: use_numeric_input_advanced

      When entering numbers while transforming, default to advanced mode for full math expression evaluation

      :type: boolean, default False

   .. attribute:: use_rotate_around_active

      Use selection as the pivot point

      :type: boolean, default False

   .. attribute:: use_zoom_to_mouse

      Zoom in towards the mouse pointer's position in the 3D view, rather than the 2D window center

      :type: boolean, default False

   .. attribute:: view_rotate_method

      Orbit method in the viewport

      * ``TURNTABLE``
        Turntable -- Turntable keeps the Z-axis upright while orbiting.
      * ``TRACKBALL``
        Trackball -- Trackball allows you to tumble your view at any angle.

      :type: enum in [``'TURNTABLE'``, ``'TRACKBALL'``], default ``'TURNTABLE'``

   .. attribute:: view_rotate_sensitivity_trackball

      Scale trackball orbit sensitivity

      :type: float in [0.1, 10], default 1.0

   .. attribute:: view_rotate_sensitivity_turntable

      Rotation amount per pixel to control how fast the viewport orbits

      :type: float in [1.74533e-05, 0.261799], default 0.00698132

   .. attribute:: view_zoom_axis

      Axis of mouse movement to zoom in or out on

      * ``VERTICAL``
        Vertical -- Zoom in and out based on vertical mouse movement.
      * ``HORIZONTAL``
        Horizontal -- Zoom in and out based on horizontal mouse movement.

      :type: enum in [``'VERTICAL'``, ``'HORIZONTAL'``], default ``'VERTICAL'``

   .. attribute:: view_zoom_method

      Which style to use for viewport scaling

      * ``CONTINUE``
        Continue -- Continuous zooming. The zoom direction and speed depends on how far along the set Zoom Axis the mouse has moved..
      * ``DOLLY``
        Dolly -- Zoom in and out based on mouse movement along the set Zoom Axis.
      * ``SCALE``
        Scale -- Zoom in and out as if you are scaling the view, mouse movements relative to center.

      :type: enum in [``'CONTINUE'``, ``'DOLLY'``, ``'SCALE'``], default ``'DOLLY'``

   .. data:: walk_navigation

      Settings for walk navigation mode

      :type: :class:`WalkNavigation`, (readonly, never None)

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.id_properties_clear`
   * :class:`bpy_struct.id_properties_ensure`
   * :class:`bpy_struct.id_properties_ui`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_overridable_library`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.pop`
   * :class:`bpy_struct.property_overridable_library_set`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.rna_ancestors`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   * :class:`Preferences.inputs`

