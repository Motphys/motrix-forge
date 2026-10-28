Action Operators
================

.. module:: bpy.ops.action

.. function:: bake_keys()

   Add keyframes on every frame between the selected keyframes

.. function:: clean(*, threshold=0.001, channels=False)

   Simplify F-Curves by removing closely spaced keyframes

   :arg threshold: Threshold
   :type threshold: float in [0, inf], (optional)
   :arg channels: Channels
   :type channels: boolean, (optional)

.. function:: clickselect(*, wait_to_deselect_others=False, mouse_x=0, mouse_y=0, extend=False, deselect_all=False, column=False, channel=False)

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
   :arg channel: Only Channel, Select all the keyframes in the channel under the mouse
   :type channel: boolean, (optional)

.. function:: copy()

   Copy selected keyframes to the internal clipboard

.. function:: delete(*, confirm=True)

   Remove all selected keyframes

   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: duplicate()

   Make a copy of all selected keyframes

.. function:: duplicate_move(*, ACTION_OT_duplicate=None, TRANSFORM_OT_transform=None)

   Make a copy of all selected keyframes and move them

   :arg ACTION_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
   :type ACTION_OT_duplicate: :class:`ACTION_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_transform: Transform, Transform selected items by mode type
   :type TRANSFORM_OT_transform: :class:`TRANSFORM_OT_transform`, (optional)

.. function:: easing_type(*, type='AUTO')

   Set easing type for the F-Curve segments starting from the selected keyframes

   :arg type: Type
   :type type: enum in :ref:`rna_enum_beztriple_interpolation_easing_items`, (optional)

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

.. function:: frame_jump()

   Set the current frame to the average frame value of selected keyframes

.. function:: handle_type(*, type='FREE')

   Set type of handle for selected keyframes

   :arg type: Type
   :type type: enum in :ref:`rna_enum_keyframe_handle_type_items`, (optional)

.. function:: interpolation_type(*, type='CONSTANT')

   Set interpolation mode for the F-Curve segments starting from the selected keyframes

   :arg type: Type
   :type type: enum in :ref:`rna_enum_beztriple_interpolation_mode_items`, (optional)

.. function:: keyframe_insert(*, type='ALL')

   Insert keyframes for the specified channels

   :arg type: Type
   :type type: enum in [``'ALL'``, ``'SEL'``, ``'GROUP'``], (optional)

.. function:: keyframe_type(*, type='KEYFRAME')

   Set type of keyframe for the selected keyframes

   :arg type: Type
   :type type: enum in :ref:`rna_enum_beztriple_keyframe_type_items`, (optional)

.. function:: layer_next()

   Switch to editing action in animation layer above the current action in the NLA Stack

.. function:: layer_prev()

   Switch to editing action in animation layer below the current action in the NLA Stack

.. function:: markers_make_local()

   Move selected scene markers to the active Action as local 'pose' markers

.. function:: mirror(*, type='CFRA')

   Flip selected keyframes over the selected mirror line

   :arg type: Type

      * ``CFRA``
        By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line.
      * ``XAXIS``
        By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa).
      * ``MARKER``
        By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
   :type type: enum in [``'CFRA'``, ``'XAXIS'``, ``'MARKER'``], (optional)

.. function:: new()

   Create new action

.. function:: paste(*, offset='START', merge='MIX', flipped=False)

   Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

   :arg offset: Offset, Paste time offset of keys
   :type offset: enum in :ref:`rna_enum_keyframe_paste_offset_items`, (optional)
   :arg merge: Type, Method of merging pasted keys and existing
   :type merge: enum in :ref:`rna_enum_keyframe_paste_merge_items`, (optional)
   :arg flipped: Flipped, Paste keyframes from mirrored bones if they exist
   :type flipped: boolean, (optional)

.. function:: previewrange_set()

   Set Preview Range based on extents of selected Keyframes

.. function:: push_down()

   Push action down on to the NLA stack as a new strip

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

.. function:: select_box(*, axis_range=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False)

   Select all keyframes within the specified region

   :arg axis_range: Axis Range
   :type axis_range: boolean, (optional)
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
   :arg tweak: Tweak, Operator has been activated using a click-drag event
   :type tweak: boolean, (optional)

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

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

.. function:: select_column(*, mode='KEYS')

   Select all keyframes on the specified frame(s)

   :arg mode: Mode
   :type mode: enum in [``'KEYS'``, ``'CFRA'``, ``'MARKERS_COLUMN'``, ``'MARKERS_BETWEEN'``], (optional)

.. function:: select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

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

.. function:: snap(*, type='CFRA')

   Snap selected keyframes to the times specified

   :arg type: Type

      * ``CFRA``
        Selection to Current Frame -- Snap selected keyframes to the current frame.
      * ``NEAREST_FRAME``
        Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).
      * ``NEAREST_SECOND``
        Selection to Nearest Second -- Snap selected keyframes to the nearest second.
      * ``NEAREST_MARKER``
        Selection to Nearest Marker -- Snap selected keyframes to the nearest marker.
   :type type: enum in [``'CFRA'``, ``'NEAREST_FRAME'``, ``'NEAREST_SECOND'``, ``'NEAREST_MARKER'``], (optional)

.. function:: stash(*, create_new=True)

   Store this action in the NLA stack as a non-contributing strip for later use

   :arg create_new: Create New Action, Create a new action once the existing one has been safely stored
   :type create_new: boolean, (optional)

.. function:: stash_and_create()

   Store this action in the NLA stack as a non-contributing strip for later use, and create a new action

.. function:: unlink(*, force_delete=False)

   Unlink this action from the active action slot (and/or exit Tweak Mode)

   :arg force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-block's NLA stack
   :type force_delete: boolean, (optional)

.. function:: view_all()

   Reset viewable area to show full keyframe range

.. function:: view_frame()

   Move the view to the current frame

.. function:: view_selected()

   Reset viewable area to show selected keyframes range

