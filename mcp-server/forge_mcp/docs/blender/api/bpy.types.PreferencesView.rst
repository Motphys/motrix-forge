PreferencesView(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PreferencesView(bpy_struct)

   Preferences related to viewing data

   .. attribute:: border_width

      Size of the padding around each editor.

      :type: int in [1, 10], default 2

   .. attribute:: color_picker_type

      Different styles of displaying the color picker widget

      * ``CIRCLE_HSV``
        Circle (HSV) -- A circular Hue/Saturation color wheel, with Value slider.
      * ``CIRCLE_HSL``
        Circle (HSL) -- A circular Hue/Saturation color wheel, with Lightness slider.
      * ``SQUARE_SV``
        Square (SV + H) -- A square showing Saturation/Value, with Hue slider.
      * ``SQUARE_HS``
        Square (HS + V) -- A square showing Hue/Saturation, with Value slider.
      * ``SQUARE_HV``
        Square (HV + S) -- A square showing Hue/Value, with Saturation slider.

      :type: enum in [``'CIRCLE_HSV'``, ``'CIRCLE_HSL'``, ``'SQUARE_SV'``, ``'SQUARE_HS'``, ``'SQUARE_HV'``], default ``'CIRCLE_HSV'``

   .. attribute:: factor_display_type

      How factor values are displayed

      * ``FACTOR``
        Factor -- Display factors as values between 0 and 1.
      * ``PERCENTAGE``
        Percentage -- Display factors as percentages.

      :type: enum in [``'FACTOR'``, ``'PERCENTAGE'``], default ``'FACTOR'``

   .. attribute:: filebrowser_display_type

      Default location where the File Editor will be displayed in

      * ``SCREEN``
        Maximized Area -- Open the temporary editor in a maximized screen.
      * ``WINDOW``
        New Window -- Open the temporary editor in a new window.

      :type: enum in [``'SCREEN'``, ``'WINDOW'``], default ``'WINDOW'``

   .. attribute:: font_path_ui

      Path to interface font

      :type: string, default "", (never None)

   .. attribute:: font_path_ui_mono

      Path to interface monospaced Font

      :type: string, default "", (never None)

   .. attribute:: gizmo_size

      Diameter of the gizmo

      :type: int in [10, 200], default 75

   .. attribute:: gizmo_size_navigate_v3d

      The Navigate Gizmo size

      :type: int in [30, 200], default 80

   .. attribute:: header_align

      Default header position for new space-types

      * ``NONE``
        Keep Existing -- Keep existing header alignment.
      * ``TOP``
        Top -- Top aligned on load.
      * ``BOTTOM``
        Bottom -- Bottom align on load (except for property editors).

      :type: enum in [``'NONE'``, ``'TOP'``, ``'BOTTOM'``], default ``'NONE'``

   .. attribute:: language

      Language used for translation

      * ``DEFAULT``
        Automatic (Automatic) -- Automatically choose the system-defined language if available, or fall-back to English (US).

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``

   .. attribute:: lookdev_sphere_size

      Diameter of the HDRI preview spheres

      :type: int in [50, 400], default 150

   .. attribute:: mini_axis_brightness

      Brightness of the icon

      :type: int in [0, 10], default 8

   .. attribute:: mini_axis_size

      The axes icon's size

      :type: int in [10, 64], default 25

   .. attribute:: mini_axis_type

      Show small rotating 3D axes in the top right corner of the 3D viewport

      :type: enum in [``'NONE'``, ``'MINIMAL'``, ``'GIZMO'``], default ``'GIZMO'``

   .. attribute:: open_sublevel_delay

      Time delay in 1/10 seconds before automatically opening sub level menus

      :type: int in [1, 40], default 2

   .. attribute:: open_toplevel_delay

      Time delay in 1/10 seconds before automatically opening top level menus

      :type: int in [1, 40], default 5

   .. attribute:: pie_animation_timeout

      Time needed to fully animate the pie to unfolded state (in 1/100ths of sec)

      :type: int in [0, 1000], default 6

   .. attribute:: pie_initial_timeout

      Pie menus will use the initial mouse position as center for this amount of time (in 1/100ths of sec)

      :type: int in [0, 1000], default 0

   .. attribute:: pie_menu_confirm

      Distance threshold after which selection is made (zero to disable)

      :type: int in [0, 1000], default 0

   .. attribute:: pie_menu_radius

      Pie menu size in pixels

      :type: int in [0, 1000], default 100

   .. attribute:: pie_menu_threshold

      Distance from center needed before a selection can be made

      :type: int in [0, 1000], default 12

   .. attribute:: pie_tap_timeout

      Pie menu button held longer than this will dismiss menu on release (in 1/100ths of sec)

      :type: int in [0, 1000], default 20

   .. attribute:: playback_fps_samples

      The number of frames to use for calculating FPS average. Zero to calculate this automatically, where the number of samples matches the target FPS.

      :type: int in [0, 5000], default 8

   .. attribute:: render_display_type

      Default location where rendered images will be displayed in

      * ``NONE``
        Keep User Interface -- Images are rendered without changing the user interface.
      * ``SCREEN``
        Maximized Area -- Images are rendered in a maximized Image Editor.
      * ``AREA``
        Image Editor -- Images are rendered in an Image Editor.
      * ``WINDOW``
        New Window -- Images are rendered in a new window.

      :type: enum in [``'NONE'``, ``'SCREEN'``, ``'AREA'``, ``'WINDOW'``], default ``'WINDOW'``

   .. attribute:: rotation_angle

      Rotation step for numerical pad keys (2 4 6 8)

      :type: float in [0, 90], default 15.0

   .. attribute:: show_addons_enabled_only

      Only show enabled add-ons. Un-check to see all installed add-ons.

      :type: boolean, default False

   .. attribute:: show_column_layout

      Use a column layout for toolbox

      :type: boolean, default True

   .. attribute:: show_developer_ui

      Display advanced settings and tools for developers

      :type: boolean, default False

   .. attribute:: show_extensions_updates

      Show Extensions Update Count

      :type: boolean, default True

   .. attribute:: show_gizmo

      Use transform gizmos by default

      :type: boolean, default True

   .. attribute:: show_navigate_ui

      Show navigation controls in 2D and 3D views which do not have scroll bars

      :type: boolean, default True

   .. attribute:: show_object_info

      Include the name of the active object and the current frame number in the text info overlay

      :type: boolean, default True

   .. attribute:: show_playback_fps

      Include the number of frames displayed per second in the text info overlay while animation is played back

      :type: boolean, default True

   .. attribute:: show_splash

      Display splash screen on startup

      :type: boolean, default True

   .. attribute:: show_statusbar_memory

      Show Blender memory usage

      :type: boolean, default False

   .. attribute:: show_statusbar_scene_duration

      Show scene duration

      :type: boolean, default False

   .. attribute:: show_statusbar_stats

      Show scene statistics

      :type: boolean, default False

   .. attribute:: show_statusbar_version

      Show Blender version string

      :type: boolean, default True

   .. attribute:: show_statusbar_vram

      Show GPU video memory usage

      :type: boolean, default False

   .. attribute:: show_tooltips

      Display tooltips (when disabled, hold Alt to force display)

      :type: boolean, default True

   .. attribute:: show_tooltips_python

      Show Python references in tooltips

      :type: boolean, default False

   .. attribute:: show_view_name

      Include the name of the view orientation in the text info overlay

      :type: boolean, default True

   .. attribute:: smooth_view

      Time to animate the view in milliseconds, zero to disable

      :type: int in [0, 1000], default 200

   .. attribute:: text_hinting

      Method for making user interface text render sharp

      :type: enum in [``'AUTO'``, ``'NONE'``, ``'SLIGHT'``, ``'FULL'``], default ``'AUTO'``

   .. attribute:: timecode_style

      Format of timecode displayed when not displaying timing in terms of frames

      * ``MINIMAL``
        Minimal Info -- Most compact representation, uses '+' as separator for sub-second frame numbers, with left and right truncation of the timecode as necessary.
      * ``SMPTE``
        SMPTE (Full) -- Full SMPTE timecode (format is HH:MM:SS:FF).
      * ``SMPTE_COMPACT``
        SMPTE (Compact) -- SMPTE timecode showing minutes, seconds, and frames only - hours are also shown if necessary, but not by default.
      * ``MILLISECONDS``
        Compact with Decimals -- Similar to SMPTE (Compact), except that the decimal part of the second is shown instead of frames.
      * ``SECONDS_ONLY``
        Only Seconds -- Direct conversion of frame numbers to seconds.

      :type: enum in [``'MINIMAL'``, ``'SMPTE'``, ``'SMPTE_COMPACT'``, ``'MILLISECONDS'``, ``'SECONDS_ONLY'``], default ``'MINIMAL'``

   .. attribute:: ui_line_width

      Changes the thickness of widget outlines, lines and dots in the interface

      * ``THIN``
        Thin -- Thinner lines than the default.
      * ``AUTO``
        Default -- Automatic line width based on UI scale.
      * ``THICK``
        Thick -- Thicker lines than the default.

      :type: enum in [``'THIN'``, ``'AUTO'``, ``'THICK'``], default ``'AUTO'``

   .. attribute:: ui_scale

      Changes the size of the fonts and widgets in the interface

      :type: float in [0.5, 6], default 1.0

   .. attribute:: use_filter_brushes_by_tool

      Only show brushes applicable for the currently active tool in the asset shelf. Stored in the Preferences, which may have to be saved manually if Auto-Save Preferences is disabled

      :type: boolean, default False

   .. attribute:: use_fresnel_edit

      Enable a fresnel effect on edit mesh overlays.
      It improves shape readability of very dense meshes, but increases eye fatigue when modeling lower poly

      :type: boolean, default False

   .. attribute:: use_mouse_over_open

      Open menu buttons and pull-downs automatically when the mouse is hovering

      :type: boolean, default False

   .. attribute:: use_save_prompt

      Ask for confirmation when quitting with unsaved changes

      :type: boolean, default True

   .. attribute:: use_text_antialiasing

      Smooth jagged edges of user interface text

      :type: boolean, default True

   .. attribute:: use_text_render_subpixelaa

      Render text for optimal horizontal placement

      :type: boolean, default False

   .. attribute:: use_translate_interface

      Translate all labels in menus, buttons and panels (note that this might make it hard to follow tutorials or the manual)

      :type: boolean, default True

   .. attribute:: use_translate_new_dataname

      Translate the names of new data-blocks (objects, materials...)

      :type: boolean, default True

   .. attribute:: use_translate_reports

      Translate additional information, such as error messages

      :type: boolean, default True

   .. attribute:: use_translate_tooltips

      Translate the descriptions when hovering UI elements (recommended)

      :type: boolean, default True

   .. attribute:: use_weight_color_range

      Enable color range used for weight visualization in weight painting mode

      :type: boolean, default False

   .. attribute:: view2d_grid_spacing_min

      Minimum number of pixels between each gridline in 2D Viewports

      :type: int in [1, 500], default 45

   .. attribute:: view_frame_keyframes

      Keyframes around cursor that we zoom around

      :type: int in [1, 500], default 0

   .. attribute:: view_frame_seconds

      Seconds around cursor that we zoom around

      :type: float in [0, 10000], default 0.0

   .. attribute:: view_frame_type

      How zooming to frame focuses around current frame

      :type: enum in [``'KEEP_RANGE'``, ``'SECONDS'``, ``'KEYFRAMES'``], default ``'KEEP_RANGE'``

   .. data:: weight_color_range

      Color range used for weight visualization in weight painting mode

      :type: :class:`ColorRamp`, (readonly, never None)

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

   * :class:`Preferences.view`

