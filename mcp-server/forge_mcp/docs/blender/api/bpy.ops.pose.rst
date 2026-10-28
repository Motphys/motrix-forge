Pose Operators
==============

.. module:: bpy.ops.pose

.. function:: armature_apply(*, selected=False)

   Apply the current pose as the new rest pose

   :arg selected: Selected Only, Only apply the selected bones (with propagation to children)
   :type selected: boolean, (optional)

.. function:: autoside_names(*, axis='XAXIS')

   Automatically renames the selected bones according to which side of the target axis they fall on

   :arg axis: Axis, Axis to tag names with

      * ``XAXIS``
        X-Axis -- Left/Right.
      * ``YAXIS``
        Y-Axis -- Front/Back.
      * ``ZAXIS``
        Z-Axis -- Top/Bottom.
   :type axis: enum in [``'XAXIS'``, ``'YAXIS'``, ``'ZAXIS'``], (optional)

.. function:: blend_to_neighbor(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Blend from current position to previous or next keyframe

   :arg factor: Factor, Weighting factor for which keyframe is favored more
   :type factor: float in [0, 1], (optional)
   :arg prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
   :type prev_frame: int in [-1048574, 1048574], (optional)
   :arg next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
   :type next_frame: int in [-1048574, 1048574], (optional)
   :arg channels: Channels, Set of properties that are affected

      * ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      * ``LOC``
        Location -- Location only.
      * ``ROT``
        Rotation -- Rotation only.
      * ``SIZE``
        Scale -- Scale only.
      * ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      * ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: enum in [``'ALL'``, ``'LOC'``, ``'ROT'``, ``'SIZE'``, ``'BBONE'``, ``'CUSTOM'``], (optional)
   :arg axis_lock: Axis Lock, Transform axis to restrict effects to

      * ``FREE``
        Free -- All axes are affected.
      * ``X``
        X -- Only X-axis transforms are affected.
      * ``Y``
        Y -- Only Y-axis transforms are affected.
      * ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: enum in [``'FREE'``, ``'X'``, ``'Y'``, ``'Z'``], (optional)

.. function:: blend_with_rest(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Make the current pose more similar to, or further away from, the rest pose

   :arg factor: Factor, Weighting factor for which keyframe is favored more
   :type factor: float in [0, 1], (optional)
   :arg prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
   :type prev_frame: int in [-1048574, 1048574], (optional)
   :arg next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
   :type next_frame: int in [-1048574, 1048574], (optional)
   :arg channels: Channels, Set of properties that are affected

      * ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      * ``LOC``
        Location -- Location only.
      * ``ROT``
        Rotation -- Rotation only.
      * ``SIZE``
        Scale -- Scale only.
      * ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      * ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: enum in [``'ALL'``, ``'LOC'``, ``'ROT'``, ``'SIZE'``, ``'BBONE'``, ``'CUSTOM'``], (optional)
   :arg axis_lock: Axis Lock, Transform axis to restrict effects to

      * ``FREE``
        Free -- All axes are affected.
      * ``X``
        X -- Only X-axis transforms are affected.
      * ``Y``
        Y -- Only Y-axis transforms are affected.
      * ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: enum in [``'FREE'``, ``'X'``, ``'Y'``, ``'Z'``], (optional)

.. function:: breakdown(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Create a suitable breakdown pose on the current frame

   :arg factor: Factor, Weighting factor for which keyframe is favored more
   :type factor: float in [0, 1], (optional)
   :arg prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
   :type prev_frame: int in [-1048574, 1048574], (optional)
   :arg next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
   :type next_frame: int in [-1048574, 1048574], (optional)
   :arg channels: Channels, Set of properties that are affected

      * ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      * ``LOC``
        Location -- Location only.
      * ``ROT``
        Rotation -- Rotation only.
      * ``SIZE``
        Scale -- Scale only.
      * ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      * ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: enum in [``'ALL'``, ``'LOC'``, ``'ROT'``, ``'SIZE'``, ``'BBONE'``, ``'CUSTOM'``], (optional)
   :arg axis_lock: Axis Lock, Transform axis to restrict effects to

      * ``FREE``
        Free -- All axes are affected.
      * ``X``
        X -- Only X-axis transforms are affected.
      * ``Y``
        Y -- Only Y-axis transforms are affected.
      * ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: enum in [``'FREE'``, ``'X'``, ``'Y'``, ``'Z'``], (optional)

.. function:: constraint_add(*, type='')

   Add a constraint to the active bone

   :arg type: Type
   :type type: enum in :ref:`rna_enum_constraint_type_items`, (optional)

.. function:: constraint_add_with_targets(*, type='')

   Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

   :arg type: Type
   :type type: enum in :ref:`rna_enum_constraint_type_items`, (optional)

.. function:: constraints_clear()

   Clear all constraints from the selected bones

.. function:: constraints_copy()

   Copy constraints to other selected bones

.. function:: copy()

   Copy the current pose of the selected bones to the internal clipboard

.. function:: flip_names(*, do_strip_numbers=False)

   Flips (and corrects) the axis suffixes of the names of selected bones

   :arg do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names.Warning: May result in incoherent naming in some cases
   :type do_strip_numbers: boolean, (optional)

.. function:: hide(*, unselected=False)

   Tag selected bones to not be visible in Pose Mode

   :arg unselected: Unselected
   :type unselected: boolean, (optional)

.. function:: ik_add(*, with_targets=True)

   Add IK Constraint to the active Bone

   :arg with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects
   :type with_targets: boolean, (optional)

.. function:: ik_clear()

   Remove all IK Constraints from selected bones

.. function:: loc_clear()

   Reset locations of selected bones to their default values

.. function:: paste(*, flipped=False, selected_mask=False)

   Paste the stored pose on to the current pose

   :arg flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose
   :type flipped: boolean, (optional)
   :arg selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose
   :type selected_mask: boolean, (optional)

.. function:: paths_calculate(*, display_type='RANGE', range='SCENE', bake_location='HEADS')

   Calculate paths for the selected bones

   :arg display_type: Display type
   :type display_type: enum in :ref:`rna_enum_motionpath_display_type_items`, (optional)
   :arg range: Computation Range
   :type range: enum in :ref:`rna_enum_motionpath_range_items`, (optional)
   :arg bake_location: Bake Location, Which point on the bones is used when calculating paths
   :type bake_location: enum in :ref:`rna_enum_motionpath_bake_location_items`, (optional)

.. function:: paths_clear(*, only_selected=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg only_selected: Only Selected, Only clear motion paths of selected bones
   :type only_selected: boolean, (optional)

.. function:: paths_range_update()

   Update frame range for motion paths from the Scene's current frame range

.. function:: paths_update()

   Recalculate paths for bones that already have them

.. function:: propagate(*, mode='NEXT_KEY', end_frame=250.0)

   Copy selected aspects of the current pose to subsequent poses already keyframed

   :arg mode: Terminate Mode, Method used to determine when to stop propagating pose to keyframes

      * ``NEXT_KEY``
        To Next Keyframe -- Propagate pose to first keyframe following the current frame only.
      * ``LAST_KEY``
        To Last Keyframe -- Propagate pose to the last keyframe only (i.e. making action cyclic).
      * ``BEFORE_FRAME``
        Before Frame -- Propagate pose to all keyframes between current frame and 'Frame' property.
      * ``BEFORE_END``
        Before Last Keyframe -- Propagate pose to all keyframes from current frame until no more are found.
      * ``SELECTED_KEYS``
        On Selected Keyframes -- Propagate pose to all selected keyframes.
      * ``SELECTED_MARKERS``
        On Selected Markers -- Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.
   :type mode: enum in [``'NEXT_KEY'``, ``'LAST_KEY'``, ``'BEFORE_FRAME'``, ``'BEFORE_END'``, ``'SELECTED_KEYS'``, ``'SELECTED_MARKERS'``], (optional)
   :arg end_frame: End Frame, Frame to stop propagating frames to (for 'Before Frame' mode)
   :type end_frame: float in [1.17549e-38, inf], (optional)

.. function:: push(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Exaggerate the current pose in regards to the breakdown pose

   :arg factor: Factor, Weighting factor for which keyframe is favored more
   :type factor: float in [0, 1], (optional)
   :arg prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
   :type prev_frame: int in [-1048574, 1048574], (optional)
   :arg next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
   :type next_frame: int in [-1048574, 1048574], (optional)
   :arg channels: Channels, Set of properties that are affected

      * ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      * ``LOC``
        Location -- Location only.
      * ``ROT``
        Rotation -- Rotation only.
      * ``SIZE``
        Scale -- Scale only.
      * ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      * ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: enum in [``'ALL'``, ``'LOC'``, ``'ROT'``, ``'SIZE'``, ``'BBONE'``, ``'CUSTOM'``], (optional)
   :arg axis_lock: Axis Lock, Transform axis to restrict effects to

      * ``FREE``
        Free -- All axes are affected.
      * ``X``
        X -- Only X-axis transforms are affected.
      * ``Y``
        Y -- Only Y-axis transforms are affected.
      * ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: enum in [``'FREE'``, ``'X'``, ``'Y'``, ``'Z'``], (optional)

.. function:: quaternions_flip()

   Flip quaternion values to achieve desired rotations, while maintaining the same orientations

.. function:: relax(*, factor=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE')

   Make the current pose more similar to its breakdown pose

   :arg factor: Factor, Weighting factor for which keyframe is favored more
   :type factor: float in [0, 1], (optional)
   :arg prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
   :type prev_frame: int in [-1048574, 1048574], (optional)
   :arg next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
   :type next_frame: int in [-1048574, 1048574], (optional)
   :arg channels: Channels, Set of properties that are affected

      * ``ALL``
        All Properties -- All properties, including transforms, bendy bone shape, and custom properties.
      * ``LOC``
        Location -- Location only.
      * ``ROT``
        Rotation -- Rotation only.
      * ``SIZE``
        Scale -- Scale only.
      * ``BBONE``
        Bendy Bone -- Bendy Bone shape properties.
      * ``CUSTOM``
        Custom Properties -- Custom properties.
   :type channels: enum in [``'ALL'``, ``'LOC'``, ``'ROT'``, ``'SIZE'``, ``'BBONE'``, ``'CUSTOM'``], (optional)
   :arg axis_lock: Axis Lock, Transform axis to restrict effects to

      * ``FREE``
        Free -- All axes are affected.
      * ``X``
        X -- Only X-axis transforms are affected.
      * ``Y``
        Y -- Only Y-axis transforms are affected.
      * ``Z``
        Z -- Only Z-axis transforms are affected.
   :type axis_lock: enum in [``'FREE'``, ``'X'``, ``'Y'``, ``'Z'``], (optional)

.. function:: reveal(*, select=True)

   Reveal all bones hidden in Pose Mode

   :arg select: Select
   :type select: boolean, (optional)

.. function:: rot_clear()

   Reset rotations of selected bones to their default values

.. function:: rotation_mode_set(*, type='QUATERNION')

   Set the rotation representation used by selected bones

   :arg type: Rotation Mode
   :type type: enum in :ref:`rna_enum_object_rotation_mode_items`, (optional)

.. function:: scale_clear()

   Reset scaling of selected bones to their default values

.. function:: select_all(*, action='TOGGLE')

   Toggle selection status of all bones

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

.. function:: select_constraint_target()

   Select bones used as targets for the currently selected bones

.. function:: select_grouped(*, extend=False, type='COLLECTION')

   Select all visible bones grouped by similar properties

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg type: Type

      * ``COLLECTION``
        Collection -- Same collections as the active bone.
      * ``COLOR``
        Color -- Same color as the active bone.
      * ``KEYINGSET``
        Keying Set -- All bones affected by active Keying Set.
      * ``CHILDREN``
        Children -- Select all children of currently selected bones.
      * ``CHILDREN_IMMEDIATE``
        Immediate Children -- Select direct children of currently selected bones.
      * ``PARENT``
        Parents -- Select the parents of currently selected bones.
      * ``SIBILINGS``
        Siblings -- Select all bones that have the same parent as currently selected bones.
   :type type: enum in [``'COLLECTION'``, ``'COLOR'``, ``'KEYINGSET'``, ``'CHILDREN'``, ``'CHILDREN_IMMEDIATE'``, ``'PARENT'``, ``'SIBILINGS'``], (optional)

.. function:: select_hierarchy(*, direction='PARENT', extend=False)

   Select immediate parent/children of selected bones

   :arg direction: Direction
   :type direction: enum in [``'PARENT'``, ``'CHILD'``], (optional)
   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: select_linked()

   Select all bones linked by parent/child connections to the current selection

.. function:: select_linked_pick(*, extend=False)

   Select bones linked by parent/child connections under the mouse cursor

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)

.. function:: select_mirror(*, only_active=False, extend=False)

   Mirror the bone selection

   :arg only_active: Active Only, Only operate on the active bone
   :type only_active: boolean, (optional)
   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: select_parent()

   Select bones that are parents of the currently selected bones

.. function:: selection_set_add()

   Create a new empty Selection Set

   :File: `startup\bl_operators\bone_selection_sets.py\:143 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L143>`__

.. function:: selection_set_add_and_assign()

   Create a new Selection Set with the currently selected bones

   :File: `startup\bl_operators\bone_selection_sets.py\:274 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L274>`__

.. function:: selection_set_assign()

   Add selected bones to Selection Set

   :File: `startup\bl_operators\bone_selection_sets.py\:190 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L190>`__

.. function:: selection_set_copy()

   Copy the selected Selection Set(s) to the clipboard

   :File: `startup\bl_operators\bone_selection_sets.py\:286 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L286>`__

.. function:: selection_set_delete_all()

   Remove all Selection Sets from this Armature

   :File: `startup\bl_operators\bone_selection_sets.py\:73 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L73>`__

.. function:: selection_set_deselect()

   Remove Selection Set bones from current selection

   :File: `startup\bl_operators\bone_selection_sets.py\:257 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L257>`__

.. function:: selection_set_move(*, direction='UP')

   Move the active Selection Set up/down the list of sets

   :arg direction: Move Direction, Direction to move the active Selection Set: UP (default) or DOWN
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)
   :File: `startup\bl_operators\bone_selection_sets.py\:122 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L122>`__


.. function:: selection_set_paste()

   Add new Selection Set(s) from the clipboard

   :File: `startup\bl_operators\bone_selection_sets.py\:298 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L298>`__

.. function:: selection_set_remove()

   Remove a Selection Set from this Armature

   :File: `startup\bl_operators\bone_selection_sets.py\:161 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L161>`__

.. function:: selection_set_remove_bones()

   Remove the selected bones from all Selection Sets

   :File: `startup\bl_operators\bone_selection_sets.py\:85 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L85>`__

.. function:: selection_set_select(*, selection_set_index=-1)

   Select the bones from this Selection Set

   :arg selection_set_index: Selection Set Index, Which Selection Set to select; -1 uses the active Selection Set
   :type selection_set_index: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\bone_selection_sets.py\:235 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L235>`__


.. function:: selection_set_unassign()

   Remove selected bones from Selection Set

   :File: `startup\bl_operators\bone_selection_sets.py\:209 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\bone_selection_sets.py#L209>`__

.. function:: transforms_clear()

   Reset location, rotation, and scaling of selected bones to their default values

.. function:: user_transforms_clear(*, only_selected=True)

   Reset pose bone transforms to keyframed state

   :arg only_selected: Only Selected, Only visible/selected bones
   :type only_selected: boolean, (optional)

.. function:: visual_transform_apply()

   Apply final constrained position of pose bones to their transform

