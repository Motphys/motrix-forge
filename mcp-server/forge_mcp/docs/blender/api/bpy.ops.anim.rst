Anim Operators
==============

.. module:: bpy.ops.anim

.. function:: change_frame(*, frame=0.0, snap=False, seq_solo_preview=False)

   Interactively change the current frame number

   :arg frame: Frame
   :type frame: float in [-1.04857e+06, 1.04857e+06], (optional)
   :arg snap: Snap
   :type snap: boolean, (optional)
   :arg seq_solo_preview: Strip Preview
   :type seq_solo_preview: boolean, (optional)

.. function:: channel_select_keys(*, extend=False)

   Select all keyframes of channel under mouse

   :arg extend: Extend, Extend selection
   :type extend: boolean, (optional)

.. function:: channel_view_pick(*, include_handles=True, use_preview_range=True)

   Reset viewable area to show the channel under the cursor

   :arg include_handles: Include Handles, Include handles of keyframes when calculating extents
   :type include_handles: boolean, (optional)
   :arg use_preview_range: Use Preview Range, Ignore frames outside of the preview range
   :type use_preview_range: boolean, (optional)

.. function:: channels_bake(*, range=(0, 0), step=1.0, remove_outside_range=False, interpolation_type='BEZIER', bake_modifiers=True)

   Create keyframes following the current shape of F-Curves of selected channels

   :arg range: Frame Range, The range in which to create new keys
   :type range: int array of 2 items in [-inf, inf], (optional)
   :arg step: Frame Step, At which interval to add keys
   :type step: float in [0.01, inf], (optional)
   :arg remove_outside_range: Remove Outside Range, Removes keys outside the given range, leaving only the newly baked
   :type remove_outside_range: boolean, (optional)
   :arg interpolation_type: Interpolation Type, Choose the interpolation type with which new keys will be added

      * ``BEZIER``
        Bézier -- New keys will be Bézier.
      * ``LIN``
        Linear -- New keys will be linear.
      * ``CONST``
        Constant -- New keys will be constant.
   :type interpolation_type: enum in [``'BEZIER'``, ``'LIN'``, ``'CONST'``], (optional)
   :arg bake_modifiers: Bake Modifiers, Bake Modifiers into keyframes and delete them after
   :type bake_modifiers: boolean, (optional)

.. function:: channels_clean_empty()

   Delete all empty animation data containers from visible data-blocks

.. function:: channels_click(*, extend=False, extend_range=False, children_only=False)

   Handle mouse clicks over animation channels

   :arg extend: Extend Select
   :type extend: boolean, (optional)
   :arg extend_range: Extend Range, Selection of active channel to clicked channel
   :type extend_range: boolean, (optional)
   :arg children_only: Select Children Only
   :type children_only: boolean, (optional)

.. function:: channels_collapse(*, all=True)

   Collapse (close) all selected expandable animation channels

   :arg all: All, Collapse all channels (not just selected ones)
   :type all: boolean, (optional)

.. function:: channels_delete()

   Delete all selected animation channels

.. function:: channels_editable_toggle(*, mode='TOGGLE', type='PROTECT')

   Toggle editability of selected channels

   :arg mode: Mode
   :type mode: enum in [``'TOGGLE'``, ``'DISABLE'``, ``'ENABLE'``, ``'INVERT'``], (optional)
   :arg type: Type
   :type type: enum in [``'PROTECT'``, ``'MUTE'``], (optional)

.. function:: channels_expand(*, all=True)

   Expand (open) all selected expandable animation channels

   :arg all: All, Expand all channels (not just selected ones)
   :type all: boolean, (optional)

.. function:: channels_fcurves_enable()

   Clear 'disabled' tag from all F-Curves to get broken F-Curves working again

.. function:: channels_group(*, name="New Group")

   Add selected F-Curves to a new group

   :arg name: Name, Name of newly created group
   :type name: string, (optional, never None)

.. function:: channels_move(*, direction='DOWN')

   Rearrange selected animation channels

   :arg direction: Direction
   :type direction: enum in [``'TOP'``, ``'UP'``, ``'DOWN'``, ``'BOTTOM'``], (optional)

.. function:: channels_rename()

   Rename animation channel under mouse

.. function:: channels_select_all(*, action='TOGGLE')

   Toggle selection of all animation channels

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

.. function:: channels_select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, deselect=False, extend=True)

   Select all animation channels within the specified region

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
   :arg deselect: Deselect, Deselect rather than select items
   :type deselect: boolean, (optional)
   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)

.. function:: channels_select_filter()

   Start entering text which filters the set of channels shown to only include those with matching names

.. function:: channels_setting_disable(*, mode='DISABLE', type='PROTECT')

   Disable specified setting on all selected animation channels

   :arg mode: Mode
   :type mode: enum in [``'TOGGLE'``, ``'DISABLE'``, ``'ENABLE'``, ``'INVERT'``], (optional)
   :arg type: Type
   :type type: enum in [``'PROTECT'``, ``'MUTE'``], (optional)

.. function:: channels_setting_enable(*, mode='ENABLE', type='PROTECT')

   Enable specified setting on all selected animation channels

   :arg mode: Mode
   :type mode: enum in [``'TOGGLE'``, ``'DISABLE'``, ``'ENABLE'``, ``'INVERT'``], (optional)
   :arg type: Type
   :type type: enum in [``'PROTECT'``, ``'MUTE'``], (optional)

.. function:: channels_setting_toggle(*, mode='TOGGLE', type='PROTECT')

   Toggle specified setting on all selected animation channels

   :arg mode: Mode
   :type mode: enum in [``'TOGGLE'``, ``'DISABLE'``, ``'ENABLE'``, ``'INVERT'``], (optional)
   :arg type: Type
   :type type: enum in [``'PROTECT'``, ``'MUTE'``], (optional)

.. function:: channels_ungroup()

   Remove selected F-Curves from their current groups

.. function:: channels_view_selected(*, include_handles=True, use_preview_range=True)

   Reset viewable area to show the selected channels

   :arg include_handles: Include Handles, Include handles of keyframes when calculating extents
   :type include_handles: boolean, (optional)
   :arg use_preview_range: Use Preview Range, Ignore frames outside of the preview range
   :type use_preview_range: boolean, (optional)

.. function:: clear_useless_actions(*, only_unused=True)

   Mark actions with no F-Curves for deletion after save and reload of file preserving "action libraries"

   :arg only_unused: Only Unused, Only unused (Fake User only) actions get considered
   :type only_unused: boolean, (optional)
   :File: `startup\bl_operators\anim.py\:354 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L354>`__


.. function:: convert_legacy_action()

   Convert a legacy Action to a layered Action on the active object

.. function:: copy_driver_button()

   Copy the driver for the highlighted button

.. function:: driver_button_add()

   Add driver for the property under the cursor

.. function:: driver_button_edit()

   Edit the drivers for the connected property represented by the highlighted button

.. function:: driver_button_remove(*, all=True)

   Remove the driver(s) for the connected property(s) represented by the highlighted button

   :arg all: All, Delete drivers for all elements of the array
   :type all: boolean, (optional)

.. function:: end_frame_set()

   Set the current frame as the preview or scene end frame

.. function:: keyframe_clear_button(*, all=True)

   Clear all keyframes on the currently active property

   :arg all: All, Clear keyframes from all elements of the array
   :type all: boolean, (optional)

.. function:: keyframe_clear_v3d(*, confirm=True)

   Remove all keyframe animation for selected objects

   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: keyframe_delete(*, type='DEFAULT')

   Delete keyframes on the current frame for all properties in the specified Keying Set

   :arg type: Keying Set, The Keying Set to use
   :type type: enum in [``'DEFAULT'``], (optional)

.. function:: keyframe_delete_button(*, all=True)

   Delete current keyframe of current UI-active property

   :arg all: All, Delete keyframes from all elements of the array
   :type all: boolean, (optional)

.. function:: keyframe_delete_by_name(*, type="")

   Alternate access to 'Delete Keyframe' for keymaps to use

   :arg type: Keying Set, The Keying Set to use
   :type type: string, (optional, never None)

.. function:: keyframe_delete_v3d(*, confirm=True)

   Remove keyframes on current frame for selected objects and bones

   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: keyframe_insert(*, type='DEFAULT')

   Insert keyframes on the current frame using either the active keying set, or the user preferences if no keying set is active

   :arg type: Keying Set, The Keying Set to use
   :type type: enum in [``'DEFAULT'``], (optional)

.. function:: keyframe_insert_button(*, all=True)

   Insert a keyframe for current UI-active property

   :arg all: All, Insert a keyframe for all element of the array
   :type all: boolean, (optional)

.. function:: keyframe_insert_by_name(*, type="")

   Alternate access to 'Insert Keyframe' for keymaps to use

   :arg type: Keying Set, The Keying Set to use
   :type type: string, (optional, never None)

.. function:: keyframe_insert_menu(*, type='DEFAULT', always_prompt=False)

   Insert Keyframes for specified Keying Set, with menu of available Keying Sets if undefined

   :arg type: Keying Set, The Keying Set to use
   :type type: enum in [``'DEFAULT'``], (optional)
   :arg always_prompt: Always Show Menu
   :type always_prompt: boolean, (optional)

.. function:: keying_set_active_set(*, type='DEFAULT')

   Set a new active keying set

   :arg type: Keying Set, The Keying Set to use
   :type type: enum in [``'DEFAULT'``], (optional)

.. function:: keying_set_add()

   Add a new (empty) keying set to the active Scene

.. function:: keying_set_export(*, filepath="", filter_folder=True, filter_text=True, filter_python=True)

   Export Keying Set to a Python script

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_text: Filter text
   :type filter_text: boolean, (optional)
   :arg filter_python: Filter Python
   :type filter_python: boolean, (optional)
   :File: `startup\bl_operators\anim.py\:46 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L46>`__


.. function:: keying_set_path_add()

   Add empty path to active keying set

.. function:: keying_set_path_remove()

   Remove active Path from active keying set

.. function:: keying_set_remove()

   Remove the active keying set

.. function:: keyingset_button_add(*, all=True)

   Add current UI-active property to current keying set

   :arg all: All, Add all elements of the array to a Keying Set
   :type all: boolean, (optional)

.. function:: keyingset_button_remove()

   Remove current UI-active property from current keying set

.. function:: merge_animation()

   Merge the animation of the selected objects into the action of the active object. Actions are not deleted by this, but might end up with zero users

.. function:: paste_driver_button()

   Paste the driver in the internal clipboard to the highlighted button

.. function:: previewrange_clear()

   Clear preview range

.. function:: previewrange_set(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Interactively define frame range used for playback

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

.. function:: scene_range_frame()

   Reset the horizontal view to the current scene frame range, taking the preview range into account if it is active

.. function:: separate_slots()

   Move all slots of the action on the active object into newly created, separate actions. All users of those slots will be reassigned to the new actions. The current action won't be deleted but will be empty and might end up having zero users

.. function:: slot_channels_move_to_new_action()

   Move the selected slots into a newly created action

.. function:: slot_new_for_id()

   Create a new action slot for this data-block, to hold its animation

   :File: `startup\bl_operators\anim.py\:708 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L708>`__

.. function:: slot_unassign_from_constraint()

   Un-assign the action slot from this constraint

   :File: `startup\bl_operators\anim.py\:766 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L766>`__

.. function:: slot_unassign_from_id()

   Un-assign the action slot, effectively making this data-block non-animated

   :File: `startup\bl_operators\anim.py\:745 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L745>`__

.. function:: slot_unassign_from_nla_strip()

   Un-assign the action slot from this NLA strip, effectively making it non-animated

   :File: `startup\bl_operators\anim.py\:766 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L766>`__

.. function:: start_frame_set()

   Set the current frame as the preview or scene start frame

.. function:: update_animated_transform_constraints(*, use_convert_to_radians=True)

   Update f-curves/drivers affecting Transform constraints (use it with files from 2.70 and earlier)

   :arg use_convert_to_radians: Convert to Radians, Convert f-curves/drivers affecting rotations to radians.Warning: Use this only once
   :type use_convert_to_radians: boolean, (optional)
   :File: `startup\bl_operators\anim.py\:389 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L389>`__


.. function:: view_curve_in_graph_editor(*, all=False, isolate=False)

   Frame the property under the cursor in the Graph Editor

   :arg all: Show All, Frame the whole array property instead of only the index under the cursor
   :type all: boolean, (optional)
   :arg isolate: Isolate, Hides all F-Curves other than the ones being framed
   :type isolate: boolean, (optional)

