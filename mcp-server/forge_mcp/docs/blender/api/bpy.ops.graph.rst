Graph Operators
===============

.. module:: bpy.ops.graph

.. function:: bake_keys()

   Add keyframes on every frame between the selected keyframes

.. function:: blend_offset(*, factor=0.0)

   Shift selected keys to the value of the neighboring keys as a block

   :arg factor: Offset Factor, Control which key to offset towards and how far
   :type factor: float in [-inf, inf], (optional)

.. function:: blend_to_default(*, factor=0.0)

   Blend selected keys to their default value from their current position

   :arg factor: Factor, How much to blend to the default value
   :type factor: float in [-inf, inf], (optional)

.. function:: blend_to_ease(*, factor=0.0)

   Blends keyframes from current state to an ease-in or ease-out curve

   :arg factor: Blend, Favor either original data or ease curve
   :type factor: float in [-inf, inf], (optional)

.. function:: blend_to_neighbor(*, factor=0.0)

   Blend selected keyframes to their left or right neighbor

   :arg factor: Blend, The blend factor with 0 being the current frame
   :type factor: float in [-inf, inf], (optional)

.. function:: breakdown(*, factor=0.0)

   Move selected keyframes to an inbetween position relative to adjacent keys

   :arg factor: Factor, Favor either the left or the right key
   :type factor: float in [-inf, inf], (optional)

.. function:: butterworth_smooth(*, cutoff_frequency=3.0, filter_order=4, samples_per_frame=1, blend=1.0, blend_in_out=1)

   Smooth an F-Curve while maintaining the general shape of the curve

   :arg cutoff_frequency: Frequency Cutoff (Hz), Lower values give a smoother curve
   :type cutoff_frequency: float in [0, inf], (optional)
   :arg filter_order: Filter Order, Higher values produce a harder frequency cutoff
   :type filter_order: int in [1, 32], (optional)
   :arg samples_per_frame: Samples per Frame, How many samples to calculate per frame, helps with subframe data
   :type samples_per_frame: int in [1, 64], (optional)
   :arg blend: Blend, How much to blend to the smoothed curve
   :type blend: float in [0, inf], (optional)
   :arg blend_in_out: Blend In/Out, Linearly blend the smooth data to the border frames of the selection
   :type blend_in_out: int in [0, inf], (optional)

.. function:: clean(*, threshold=0.001, channels=False)

   Simplify F-Curves by removing closely spaced keyframes

   :arg threshold: Threshold
   :type threshold: float in [0, inf], (optional)
   :arg channels: Channels
   :type channels: boolean, (optional)

.. function:: click_insert(*, frame=1.0, value=1.0, extend=False)

   Insert new keyframe at the cursor position for the active F-Curve

   :arg frame: Frame Number, Frame to insert keyframe on
   :type frame: float in [-inf, inf], (optional)
   :arg value: Value, Value for keyframe on
   :type value: float in [-inf, inf], (optional)
   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)

.. function:: clickselect(*, wait_to_deselect_others=False, mouse_x=0, mouse_y=0, extend=False, deselect_all=False, column=False, curves=False)

   Select keyframes by clicking on them

   :arg wait_to_deselect_others: Wait to Deselect Others
   :type wait_to_deselect_others: boolean, (optional)
   :arg mouse_x: Mouse X
   :type mouse_x: int in [-inf, inf], (optional)
   :arg mouse_y: Mouse Y
   :type mouse_y: int in [-inf, inf], (optional)
   :arg extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
   :type extend: boolean, (optional)
   :arg deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
   :type deselect_all: boolean, (optional)
   :arg column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
   :type column: boolean, (optional)
   :arg curves: Only Curves, Select all the keyframes in the curve
   :type curves: boolean, (optional)

.. function:: copy()

   Copy selected keyframes to the internal clipboard

.. function:: cursor_set(*, frame=0.0, value=0.0)

   Interactively set the current frame and value cursor

   :arg frame: Frame
   :type frame: float in [-1.04857e+06, 1.04857e+06], (optional)
   :arg value: Value
   :type value: float in [-inf, inf], (optional)

.. function:: decimate(*, mode='RATIO', factor=0.333333, remove_error_margin=0.0)

   Decimate F-Curves by removing keyframes that influence the curve shape the least

   :arg mode: Mode, Which mode to use for decimation

      * ``RATIO``
        Ratio -- Use a percentage to specify how many keyframes you want to remove.
      * ``ERROR``
        Error Margin -- Use an error margin to specify how much the curve is allowed to deviate from the original path.
   :type mode: enum in [``'RATIO'``, ``'ERROR'``], (optional)
   :arg factor: Factor, The ratio of keyframes to remove
   :type factor: float in [0, 1], (optional)
   :arg remove_error_margin: Max Error Margin, How much the new decimated curve is allowed to deviate from the original
   :type remove_error_margin: float in [0, inf], (optional)

.. function:: delete(*, confirm=True)

   Remove all selected keyframes

   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: driver_delete_invalid()

   Delete all visible drivers considered invalid

.. function:: driver_variables_copy()

   Copy the driver variables of the active driver

.. function:: driver_variables_paste(*, replace=False)

   Add copied driver variables to the active driver

   :arg replace: Replace Existing, Replace existing driver variables, instead of just appending to the end of the existing list
   :type replace: boolean, (optional)

.. function:: duplicate(*, mode='TRANSLATION')

   Make a copy of all selected keyframes

   :arg mode: Mode
   :type mode: enum in :ref:`rna_enum_transform_mode_type_items`, (optional)

.. function:: duplicate_move(*, GRAPH_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Make a copy of all selected keyframes and move them

   :arg GRAPH_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
   :type GRAPH_OT_duplicate: :class:`GRAPH_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: ease(*, factor=0.0, sharpness=2.0)

   Align keyframes on a ease-in or ease-out curve

   :arg factor: Curve Bend, Defines if the keys should be aligned on an ease-in or ease-out curve
   :type factor: float in [-inf, inf], (optional)
   :arg sharpness: Sharpness, Higher values make the change more abrupt
   :type sharpness: float in [0.001, inf], (optional)

.. function:: easing_type(*, type='AUTO')

   Set easing type for the F-Curve segments starting from the selected keyframes

   :arg type: Type
   :type type: enum in :ref:`rna_enum_beztriple_interpolation_easing_items`, (optional)

.. function:: equalize_handles(*, side='LEFT', handle_length=5.0, flatten=False)

   Ensure selected keyframes' handles have equal length, optionally making them horizontal. Automatic, Automatic Clamped, or Vector handle types will be converted to Aligned

   :arg side: Side, Side of the keyframes' Bézier handles to affect

      * ``LEFT``
        Left -- Equalize selected keyframes' left handles.
      * ``RIGHT``
        Right -- Equalize selected keyframes' right handles.
      * ``BOTH``
        Both -- Equalize both of a keyframe's handles.
   :type side: enum in [``'LEFT'``, ``'RIGHT'``, ``'BOTH'``], (optional)
   :arg handle_length: Handle Length, Length to make selected keyframes' Bézier handles
   :type handle_length: float in [0.1, inf], (optional)
   :arg flatten: Flatten, Make the values of the selected keyframes' handles the same as their respective keyframes
   :type flatten: boolean, (optional)

.. function:: euler_filter()

   Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics

.. function:: extrapolation_type(*, type='CONSTANT')

   Set extrapolation mode for selected F-Curves

   :arg type: Type

      * ``CONSTANT``
        Constant Extrapolation -- Values on endpoint keyframes are held.
      * ``LINEAR``
        Linear Extrapolation -- Straight-line slope of end segments are extended past the endpoint keyframes.
      * ``MAKE_CYCLIC``
        Make Cyclic (F-Modifier) -- Add Cycles F-Modifier if one doesn't exist already.
      * ``CLEAR_CYCLIC``
        Clear Cyclic (F-Modifier) -- Remove Cycles F-Modifier if not needed anymore.
   :type type: enum in [``'CONSTANT'``, ``'LINEAR'``, ``'MAKE_CYCLIC'``, ``'CLEAR_CYCLIC'``], (optional)

.. function:: fmodifier_add(*, type='NULL', only_active=False)

   Add F-Modifier to the active/selected F-Curves

   :arg type: Type
   :type type: enum in :ref:`rna_enum_fmodifier_type_items`, (optional)
   :arg only_active: Only Active, Only add F-Modifier to active F-Curve
   :type only_active: boolean, (optional)

.. function:: fmodifier_copy()

   Copy the F-Modifier(s) of the active F-Curve

.. function:: fmodifier_paste(*, only_active=False, replace=False)

   Add copied F-Modifiers to the selected F-Curves

   :arg only_active: Only Active, Only paste F-Modifiers on active F-Curve
   :type only_active: boolean, (optional)
   :arg replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
   :type replace: boolean, (optional)

.. function:: frame_jump()

   Place the cursor on the midpoint of selected keyframes

.. function:: gaussian_smooth(*, factor=1.0, sigma=0.33, filter_width=6)

   Smooth the curve using a Gaussian filter

   :arg factor: Factor, How much to blend to the default value
   :type factor: float in [0, inf], (optional)
   :arg sigma: Sigma, The shape of the gaussian distribution, lower values make it sharper
   :type sigma: float in [0.001, inf], (optional)
   :arg filter_width: Filter Width, How far to each side the operator will average the key values
   :type filter_width: int in [1, 64], (optional)

.. function:: ghost_curves_clear()

   Clear F-Curve snapshots (Ghosts) for active Graph Editor

.. function:: ghost_curves_create()

   Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor

.. function:: handle_type(*, type='FREE')

   Set type of handle for selected keyframes

   :arg type: Type
   :type type: enum in :ref:`rna_enum_keyframe_handle_type_items`, (optional)

.. function:: hide(*, unselected=False)

   Hide selected curves from Graph Editor view

   :arg unselected: Unselected, Hide unselected rather than selected curves
   :type unselected: boolean, (optional)

.. function:: interpolation_type(*, type='CONSTANT')

   Set interpolation mode for the F-Curve segments starting from the selected keyframes

   :arg type: Type
   :type type: enum in :ref:`rna_enum_beztriple_interpolation_mode_items`, (optional)

.. function:: keyframe_insert(*, type='ALL')

   Insert keyframes for the specified channels

   :arg type: Type

      * ``ALL``
        All Channels -- Insert a keyframe on all visible and editable F-Curves using each curve's current value.
      * ``SEL``
        Only Selected Channels -- Insert a keyframe on selected F-Curves using each curve's current value.
      * ``ACTIVE``
        Only Active F-Curve -- Insert a keyframe on the active F-Curve using the curve's current value.
      * ``CURSOR_ACTIVE``
        Active Channels at Cursor -- Insert a keyframe for the active F-Curve at the cursor point.
      * ``CURSOR_SEL``
        Selected Channels at Cursor -- Insert a keyframe for selected F-Curves at the cursor point.
   :type type: enum in [``'ALL'``, ``'SEL'``, ``'ACTIVE'``, ``'CURSOR_ACTIVE'``, ``'CURSOR_SEL'``], (optional)

.. function:: keyframe_jump(*, next=True)

   Jump to previous/next keyframe

   :arg next: Next Keyframe
   :type next: boolean, (optional)

.. function:: keys_to_samples()

   Convert selected channels to an uneditable set of samples to save storage space

.. function:: match_slope(*, factor=0.0)

   Blend selected keys to the slope of neighboring ones

   :arg factor: Factor, Defines which keys to use as slope and how much to blend towards them
   :type factor: float in [-inf, inf], (optional)

.. function:: mirror(*, type='CFRA')

   Flip selected keyframes over the selected mirror line

   :arg type: Type

      * ``CFRA``
        By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line.
      * ``VALUE``
        By Values Over Cursor Value -- Flip values of selected keyframes using the cursor value (Y/Horizontal component) as the mirror line.
      * ``YAXIS``
        By Times Over Zero Time -- Flip times of selected keyframes, effectively reversing the order they appear in.
      * ``XAXIS``
        By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa).
      * ``MARKER``
        By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
   :type type: enum in [``'CFRA'``, ``'VALUE'``, ``'YAXIS'``, ``'XAXIS'``, ``'MARKER'``], (optional)

.. function:: paste(*, offset='START', value_offset='NONE', merge='MIX', flipped=False)

   Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

   :arg offset: Frame Offset, Paste time offset of keys
   :type offset: enum in :ref:`rna_enum_keyframe_paste_offset_items`, (optional)
   :arg value_offset: Value Offset, Paste keys with a value offset
   :type value_offset: enum in :ref:`rna_enum_keyframe_paste_offset_value_items`, (optional)
   :arg merge: Type, Method of merging pasted keys and existing
   :type merge: enum in :ref:`rna_enum_keyframe_paste_merge_items`, (optional)
   :arg flipped: Flipped, Paste keyframes from mirrored bones if they exist
   :type flipped: boolean, (optional)

.. function:: previewrange_set()

   Set Preview Range based on range of selected keyframes

.. function:: push_pull(*, factor=1.0)

   Exaggerate or minimize the value of the selected keys

   :arg factor: Factor, Control how far to push or pull the keys
   :type factor: float in [-inf, inf], (optional)

.. function:: reveal(*, select=True)

   Make previously hidden curves visible again in Graph Editor view

   :arg select: Select
   :type select: boolean, (optional)

.. function:: samples_to_keys()

   Convert selected channels from samples to keyframes

.. function:: scale_average(*, factor=1.0)

   Scale selected key values by their combined average

   :arg factor: Scale Factor, The scale factor applied to the curve segments
   :type factor: float in [-inf, inf], (optional)

.. function:: scale_from_neighbor(*, factor=0.0, anchor='LEFT')

   Increase or decrease the value of selected keys in relationship to the neighboring one

   :arg factor: Factor, The factor to scale keys with
   :type factor: float in [-inf, inf], (optional)
   :arg anchor: Reference Key, Which end of the segment to use as a reference to scale from
   :type anchor: enum in [``'LEFT'``, ``'RIGHT'``], (optional)

.. function:: select_all(*, action='TOGGLE')

   Toggle selection of all keyframes

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: select_box(*, axis_range=False, include_handles=True, tweak=False, use_curve_selection=True, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Select all keyframes within the specified region

   :arg axis_range: Axis Range
   :type axis_range: boolean, (optional)
   :arg include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys
   :type include_handles: boolean, (optional)
   :arg tweak: Tweak, Operator has been activated using a click-drag event
   :type tweak: boolean, (optional)
   :arg use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the calculated F-curve
   :type use_curve_selection: boolean, (optional)
   :arg xmin: X Min
   :type xmin: int in [-inf, inf], (optional)
   :arg xmax: X Max
   :type xmax: int in [-inf, inf], (optional)
   :arg ymin: Y Min
   :type ymin: int in [-inf, inf], (optional)
   :arg ymax: Y Max
   :type ymax: int in [-inf, inf], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)
   :arg mode: Mode

      * ``SET``
        Set -- Set a new selection.
      * ``ADD``
        Extend -- Extend existing selection.
      * ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``], (optional)

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET', include_handles=True, use_curve_selection=True)

   Select keyframe points using circle selection

   :arg x: X
   :type x: int in [-inf, inf], (optional)
   :arg y: Y
   :type y: int in [-inf, inf], (optional)
   :arg radius: Radius
   :type radius: int in [1, inf], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)
   :arg mode: Mode

      * ``SET``
        Set -- Set a new selection.
      * ``ADD``
        Extend -- Extend existing selection.
      * ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``], (optional)
   :arg include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys
   :type include_handles: boolean, (optional)
   :arg use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
   :type use_curve_selection: boolean, (optional)

.. function:: select_column(*, mode='KEYS')

   Select all keyframes on the specified frame(s)

   :arg mode: Mode
   :type mode: enum in [``'KEYS'``, ``'CFRA'``, ``'MARKERS_COLUMN'``, ``'MARKERS_BETWEEN'``], (optional)

.. function:: select_key_handles(*, left_handle_action='SELECT', right_handle_action='SELECT', key_action='KEEP')

   For selected keyframes, select/deselect any combination of the key itself and its handles

   :arg left_handle_action: Left Handle, Effect on the left handle

      * ``SELECT``
        Select.
      * ``DESELECT``
        Deselect.
      * ``KEEP``
        Keep -- Leave as is.
   :type left_handle_action: enum in [``'SELECT'``, ``'DESELECT'``, ``'KEEP'``], (optional)
   :arg right_handle_action: Right Handle, Effect on the right handle

      * ``SELECT``
        Select.
      * ``DESELECT``
        Deselect.
      * ``KEEP``
        Keep -- Leave as is.
   :type right_handle_action: enum in [``'SELECT'``, ``'DESELECT'``, ``'KEEP'``], (optional)
   :arg key_action: Key, Effect on the key itself

      * ``SELECT``
        Select.
      * ``DESELECT``
        Deselect.
      * ``KEEP``
        Keep -- Leave as is.
   :type key_action: enum in [``'SELECT'``, ``'DESELECT'``, ``'KEEP'``], (optional)

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET', include_handles=True, use_curve_selection=True)

   Select keyframe points using lasso selection

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
   :type use_smooth_stroke: boolean, (optional)
   :arg smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
   :type smooth_stroke_factor: float in [0.5, 0.99], (optional)
   :arg smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
   :type smooth_stroke_radius: int in [10, 200], (optional)
   :arg mode: Mode

      * ``SET``
        Set -- Set a new selection.
      * ``ADD``
        Extend -- Extend existing selection.
      * ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``], (optional)
   :arg include_handles: Include Handles, Are handles tested individually against the selection criteria, independently from their keys. When unchecked, handles are (de)selected in unison with their keys
   :type include_handles: boolean, (optional)
   :arg use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
   :type use_curve_selection: boolean, (optional)

.. function:: select_leftright(*, mode='CHECK', extend=False)

   Select keyframes to the left or the right of the current frame

   :arg mode: Mode
   :type mode: enum in [``'CHECK'``, ``'LEFT'``, ``'RIGHT'``], (optional)
   :arg extend: Extend Select
   :type extend: boolean, (optional)

.. function:: select_less()

   Deselect keyframes on ends of selection islands

.. function:: select_linked()

   Select keyframes occurring in the same F-Curves as selected ones

.. function:: select_more()

   Select keyframes beside already selected ones

.. function:: shear(*, factor=0.0, direction='FROM_LEFT')

   Affect the value of the keys linearly, keeping the same relationship between them using either the left or the right key as reference

   :arg factor: Shear Factor, The amount of shear to apply
   :type factor: float in [-inf, inf], (optional)
   :arg direction: Direction, Which end of the segment to use as a reference to shear from

      * ``FROM_LEFT``
        From Left -- Shear the keys using the left key as reference.
      * ``FROM_RIGHT``
        From Right -- Shear the keys using the right key as reference.
   :type direction: enum in [``'FROM_LEFT'``, ``'FROM_RIGHT'``], (optional)

.. function:: smooth()

   Apply weighted moving means to make selected F-Curves less bumpy

.. function:: snap(*, type='CFRA')

   Snap selected keyframes to the chosen times/values

   :arg type: Type

      * ``CFRA``
        Selection to Current Frame -- Snap selected keyframes to the current frame.
      * ``VALUE``
        Selection to Cursor Value -- Set values of selected keyframes to the cursor value (Y/Horizontal component).
      * ``NEAREST_FRAME``
        Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).
      * ``NEAREST_SECOND``
        Selection to Nearest Second -- Snap selected keyframes to the nearest second.
      * ``NEAREST_MARKER``
        Selection to Nearest Marker -- Snap selected keyframes to the nearest marker.
      * ``HORIZONTAL``
        Flatten Handles -- Flatten handles for a smoother transition.
   :type type: enum in [``'CFRA'``, ``'VALUE'``, ``'NEAREST_FRAME'``, ``'NEAREST_SECOND'``, ``'NEAREST_MARKER'``, ``'HORIZONTAL'``], (optional)

.. function:: snap_cursor_value()

   Place the cursor value on the average value of selected keyframes

.. function:: sound_to_samples(*, filepath="", check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', low=0.0, high=100000.0, attack=0.005, release=0.2, threshold=0.0, use_accumulate=False, use_additive=False, use_square=False, sthreshold=0.1)

   Bakes a sound wave to samples on selected channels

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg show_multiview: Enable Multi-View
   :type show_multiview: boolean, (optional)
   :arg use_multiview: Use Multi-View
   :type use_multiview: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode
   :type sort_method: enum in [], (optional)
   :arg low: Lowest Frequency, Cutoff frequency of a high-pass filter that is applied to the audio data
   :type low: float in [0, 100000], (optional)
   :arg high: Highest Frequency, Cutoff frequency of a low-pass filter that is applied to the audio data
   :type high: float in [0, 100000], (optional)
   :arg attack: Attack Time, Value for the envelope calculation that tells how fast the envelope can rise (the lower the value the steeper it can rise)
   :type attack: float in [0, 2], (optional)
   :arg release: Release Time, Value for the envelope calculation that tells how fast the envelope can fall (the lower the value the steeper it can fall)
   :type release: float in [0, 5], (optional)
   :arg threshold: Threshold, Minimum amplitude value needed to influence the envelope
   :type threshold: float in [0, 1], (optional)
   :arg use_accumulate: Accumulate, Only the positive differences of the envelope amplitudes are summarized to produce the output
   :type use_accumulate: boolean, (optional)
   :arg use_additive: Additive, The amplitudes of the envelope are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated)
   :type use_additive: boolean, (optional)
   :arg use_square: Square, The output is a square curve (negative values always result in -1, and positive ones in 1)
   :type use_square: boolean, (optional)
   :arg sthreshold: Square Threshold, Square only: all values with an absolute amplitude lower than that result in 0
   :type sthreshold: float in [0, 1], (optional)

.. function:: time_offset(*, frame_offset=0.0)

   Shifts the value of selected keys in time

   :arg frame_offset: Frame Offset, How far in frames to offset the animation
   :type frame_offset: float in [-inf, inf], (optional)

.. function:: view_all(*, include_handles=True)

   Reset viewable area to show full keyframe range

   :arg include_handles: Include Handles, Include handles of keyframes when calculating extents
   :type include_handles: boolean, (optional)

.. function:: view_frame()

   Move the view to the current frame

.. function:: view_selected(*, include_handles=True)

   Reset viewable area to show selected keyframe range

   :arg include_handles: Include Handles, Include handles of keyframes when calculating extents
   :type include_handles: boolean, (optional)

