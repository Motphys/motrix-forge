Nla Operators
=============

.. module:: bpy.ops.nla

.. function:: action_pushdown(*, track_index=-1)

   Push action down onto the top of the NLA stack as a new strip

   :arg track_index: Track Index, Index of NLA action track to perform pushdown operation on
   :type track_index: int in [-1, inf], (optional)

.. function:: action_sync_length(*, active=True)

   Synchronize the length of the referenced Action with the length used in the strip

   :arg active: Active Strip Only, Only sync the active length for the active strip
   :type active: boolean, (optional)

.. function:: action_unlink(*, force_delete=False)

   Unlink this action from the active action slot (and/or exit Tweak Mode)

   :arg force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-block's NLA stack
   :type force_delete: boolean, (optional)

.. function:: actionclip_add(*, action='')

   Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track

   :arg action: Action
   :type action: enum in [], (optional)

.. function:: apply_scale()

   Apply scaling of selected strips to their referenced Actions

.. function:: bake(*, frame_start=1, frame_end=250, step=1, only_selected=True, visual_keying=False, clear_constraints=False, clear_parents=False, use_current_action=False, clean_curves=False, bake_types={'POSE'}, channel_types={'BBONE', 'LOCATION', 'PROPS', 'ROTATION', 'SCALE'})

   Bake all selected objects location/scale/rotation animation to an action

   :arg frame_start: Start Frame, Start frame for baking
   :type frame_start: int in [0, 300000], (optional)
   :arg frame_end: End Frame, End frame for baking
   :type frame_end: int in [1, 300000], (optional)
   :arg step: Frame Step, Number of frames to skip forward while baking each frame
   :type step: int in [1, 120], (optional)
   :arg only_selected: Only Selected Bones, Only key selected bones (Pose baking only)
   :type only_selected: boolean, (optional)
   :arg visual_keying: Visual Keying, Keyframe from the final transformations (with constraints applied)
   :type visual_keying: boolean, (optional)
   :arg clear_constraints: Clear Local Constraints, Remove all constraints from keyed object/bones. To get a correct bake with this setting Visual Keying should be enabled
   :type clear_constraints: boolean, (optional)
   :arg clear_parents: Clear Parents, Bake animation onto the object then clear parents (objects only)
   :type clear_parents: boolean, (optional)
   :arg use_current_action: Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature)
   :type use_current_action: boolean, (optional)
   :arg clean_curves: Clean Curves, After baking curves, remove redundant keys
   :type clean_curves: boolean, (optional)
   :arg bake_types: Bake Data, Which data's transformations to bake

      * ``POSE``
        Pose -- Bake bones transformations.
      * ``OBJECT``
        Object -- Bake object transformations.
   :type bake_types: enum set in {``'POSE'``, ``'OBJECT'``}, (optional)
   :arg channel_types: Channels, Which channels to bake

      * ``LOCATION``
        Location -- Bake location channels.
      * ``ROTATION``
        Rotation -- Bake rotation channels.
      * ``SCALE``
        Scale -- Bake scale channels.
      * ``BBONE``
        B-Bone -- Bake B-Bone channels.
      * ``PROPS``
        Custom Properties -- Bake custom properties.
   :type channel_types: enum set in {``'LOCATION'``, ``'ROTATION'``, ``'SCALE'``, ``'BBONE'``, ``'PROPS'``}, (optional)
   :File: `startup\bl_operators\anim.py\:273 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L273>`__


.. function:: channels_click(*, extend=False)

   Handle clicks to select NLA tracks

   :arg extend: Extend Select
   :type extend: boolean, (optional)

.. function:: clear_scale()

   Reset scaling of selected strips

.. function:: click_select(*, wait_to_deselect_others=False, mouse_x=0, mouse_y=0, extend=False, deselect_all=False)

   Handle clicks to select NLA Strips

   :arg wait_to_deselect_others: Wait to Deselect Others
   :type wait_to_deselect_others: boolean, (optional)
   :arg mouse_x: Mouse X
   :type mouse_x: int in [-inf, inf], (optional)
   :arg mouse_y: Mouse Y
   :type mouse_y: int in [-inf, inf], (optional)
   :arg extend: Extend Select
   :type extend: boolean, (optional)
   :arg deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
   :type deselect_all: boolean, (optional)

.. function:: delete()

   Delete selected strips

.. function:: duplicate(*, linked=False)

   Duplicate selected NLA-Strips, adding the new strips to new track(s)

   :arg linked: Linked, When duplicating strips, assign new copies of the actions they use
   :type linked: boolean, (optional)

.. function:: duplicate_linked_move(*, NLA_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Duplicate Linked selected NLA-Strips, adding the new strips to new track(s)

   :arg NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)
   :type NLA_OT_duplicate: :class:`NLA_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: duplicate_move(*, NLA_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Duplicate selected NLA-Strips, adding the new strips to new track(s)

   :arg NLA_OT_duplicate: Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)
   :type NLA_OT_duplicate: :class:`NLA_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: fmodifier_add(*, type='NULL', only_active=True)

   Add F-Modifier to the active/selected NLA-Strips

   :arg type: Type
   :type type: enum in :ref:`rna_enum_fmodifier_type_items`, (optional)
   :arg only_active: Only Active, Only add a F-Modifier of the specified type to the active strip
   :type only_active: boolean, (optional)

.. function:: fmodifier_copy()

   Copy the F-Modifier(s) of the active NLA-Strip

.. function:: fmodifier_paste(*, only_active=True, replace=False)

   Add copied F-Modifiers to the selected NLA-Strips

   :arg only_active: Only Active, Only paste F-Modifiers on active strip
   :type only_active: boolean, (optional)
   :arg replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
   :type replace: boolean, (optional)

.. function:: make_single_user(*, confirm=True)

   Make linked action local to each strip

   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: meta_add()

   Add new meta-strips incorporating the selected strips

.. function:: meta_remove()

   Separate out the strips held by the selected meta-strips

.. function:: move_down()

   Move selected strips down a track if there's room

.. function:: move_up()

   Move selected strips up a track if there's room

.. function:: mute_toggle()

   Mute or un-mute selected strips

.. function:: previewrange_set()

   Set Preview Range based on extends of selected strips

.. function:: select_all(*, action='TOGGLE')

   Select or deselect all NLA-Strips

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

.. function:: select_box(*, axis_range=False, tweak=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Use box selection to grab NLA-Strips

   :arg axis_range: Axis Range
   :type axis_range: boolean, (optional)
   :arg tweak: Tweak, Operator has been activated using a click-drag event
   :type tweak: boolean, (optional)
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

.. function:: select_leftright(*, mode='CHECK', extend=False)

   Select strips to the left or the right of the current frame

   :arg mode: Mode
   :type mode: enum in [``'CHECK'``, ``'LEFT'``, ``'RIGHT'``], (optional)
   :arg extend: Extend Select
   :type extend: boolean, (optional)

.. function:: selected_objects_add()

   Make selected objects appear in NLA Editor by adding Animation Data

.. function:: snap(*, type='CFRA')

   Move start of strips to specified time

   :arg type: Type
   :type type: enum in [``'CFRA'``, ``'NEAREST_FRAME'``, ``'NEAREST_SECOND'``, ``'NEAREST_MARKER'``], (optional)

.. function:: soundclip_add()

   Add a strip for controlling when speaker plays its sound clip

.. function:: split()

   Split selected strips at their midpoints

.. function:: swap()

   Swap order of selected strips within tracks

.. function:: tracks_add(*, above_selected=False)

   Add NLA-Tracks above/after the selected tracks

   :arg above_selected: Above Selected, Add a new NLA Track above every existing selected one
   :type above_selected: boolean, (optional)

.. function:: tracks_delete()

   Delete selected NLA-Tracks and the strips they contain

.. function:: transition_add()

   Add a transition strip between two adjacent selected strips

.. function:: tweakmode_enter(*, isolate_action=False, use_upper_stack_evaluation=False)

   Enter tweaking mode for the action referenced by the active strip to edit its keyframes

   :arg isolate_action: Isolate Action, Enable 'solo' on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack
   :type isolate_action: boolean, (optional)
   :arg use_upper_stack_evaluation: Evaluate Upper Stack, In tweak mode, display the effects of the tracks above the tweak strip
   :type use_upper_stack_evaluation: boolean, (optional)

.. function:: tweakmode_exit(*, isolate_action=False)

   Exit tweaking mode for the action referenced by the active strip

   :arg isolate_action: Isolate Action, Disable 'solo' on any of the NLA Tracks after exiting tweak mode to get things back to normal
   :type isolate_action: boolean, (optional)

.. function:: view_all()

   Reset viewable area to show full strips range

.. function:: view_frame()

   Move the view to the current frame

.. function:: view_selected()

   Reset viewable area to show selected strips range

