Armature Operators
==================

.. module:: bpy.ops.armature

.. function:: align()

   Align selected bones to the active bone (or to their parent)

.. function:: assign_to_collection(*, collection_index=-1, new_collection_name="")

   Assign all selected bones to a collection, or unassign them, depending on whether the active bone is already assigned or not

   :arg collection_index: Collection Index, Index of the collection to assign selected bones to. When the operator should create a new bone collection, use new_collection_name to define the collection name, and set this parameter to the parent index of the new bone collection
   :type collection_index: int in [-1, inf], (optional)
   :arg new_collection_name: Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and assign the selected bones to it. To assign to an existing collection, do not include this parameter and use collection_index
   :type new_collection_name: string, (optional, never None)

.. function:: autoside_names(*, type='XAXIS')

   Automatically renames the selected bones according to which side of the target axis they fall on

   :arg type: Axis, Axis to tag names with

      * ``XAXIS``
        X-Axis -- Left/Right.
      * ``YAXIS``
        Y-Axis -- Front/Back.
      * ``ZAXIS``
        Z-Axis -- Top/Bottom.
   :type type: enum in [``'XAXIS'``, ``'YAXIS'``, ``'ZAXIS'``], (optional)

.. function:: bone_primitive_add(*, name="")

   Add a new bone located at the 3D cursor

   :arg name: Name, Name of the newly created bone
   :type name: string, (optional, never None)

.. function:: calculate_roll(*, type='POS_X', axis_flip=False, axis_only=False)

   Automatically fix alignment of select bones' axes

   :arg type: Type
   :type type: enum in [``'POS_X'``, ``'POS_Z'``, ``'GLOBAL_POS_X'``, ``'GLOBAL_POS_Y'``, ``'GLOBAL_POS_Z'``, ``'NEG_X'``, ``'NEG_Z'``, ``'GLOBAL_NEG_X'``, ``'GLOBAL_NEG_Y'``, ``'GLOBAL_NEG_Z'``, ``'ACTIVE'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg axis_flip: Flip Axis, Negate the alignment axis
   :type axis_flip: boolean, (optional)
   :arg axis_only: Shortest Rotation, Ignore the axis direction, use the shortest rotation to align
   :type axis_only: boolean, (optional)

.. function:: click_extrude()

   Create a new bone going from the last selected joint to the mouse position

.. function:: collection_add()

   Add a new bone collection

.. function:: collection_assign(*, name="")

   Add selected bones to the chosen bone collection

   :arg name: Bone Collection, Name of the bone collection to assign this bone to; empty to assign to the active bone collection
   :type name: string, (optional, never None)

.. function:: collection_create_and_assign(*, name="")

   Create a new bone collection and assign all selected bones

   :arg name: Bone Collection, Name of the bone collection to create
   :type name: string, (optional, never None)

.. function:: collection_deselect()

   Deselect bones of active Bone Collection

.. function:: collection_move(*, direction='UP')

   Change position of active Bone Collection in list of Bone collections

   :arg direction: Direction, Direction to move the active Bone Collection towards
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: collection_remove()

   Remove the active bone collection

.. function:: collection_remove_unused()

   Remove all bone collections that have neither bones nor children. This is done recursively, so bone collections that only have unused children are also removed

   :File: `startup\bl_operators\anim.py\:606 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L606>`__

.. function:: collection_select()

   Select bones in active Bone Collection

.. function:: collection_show_all()

   Show all bone collections

   :File: `startup\bl_operators\anim.py\:561 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L561>`__

.. function:: collection_unassign(*, name="")

   Remove selected bones from the active bone collection

   :arg name: Bone Collection, Name of the bone collection to unassign this bone from; empty to unassign from the active bone collection
   :type name: string, (optional, never None)

.. function:: collection_unassign_named(*, name="", bone_name="")

   Unassign the named bone from this bone collection

   :arg name: Bone Collection, Name of the bone collection to unassign this bone from; empty to unassign from the active bone collection
   :type name: string, (optional, never None)
   :arg bone_name: Bone Name, Name of the bone to unassign from the collection; empty to use the active bone
   :type bone_name: string, (optional, never None)

.. function:: collection_unsolo_all()

   Clear the 'solo' setting on all bone collections

   :File: `startup\bl_operators\anim.py\:584 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L584>`__

.. function:: copy_bone_color_to_selected(*, bone_type='EDIT')

   Copy the bone color of the active bone to all selected bones

   :arg bone_type: Type

      * ``EDIT``
        Bone -- Copy Bone colors from the active bone to all selected bones.
      * ``POSE``
        Pose Bone -- Copy Pose Bone colors from the active pose bone to all selected pose bones.
   :type bone_type: enum in [``'EDIT'``, ``'POSE'``], (optional)
   :File: `startup\bl_operators\anim.py\:480 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\anim.py#L480>`__


.. function:: delete(*, confirm=True)

   Remove selected bones from the armature

   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: dissolve()

   Dissolve selected bones from the armature

.. function:: duplicate(*, do_flip_names=False)

   Make copies of the selected bones within the same armature

   :arg do_flip_names: Flip Names, Try to flip names of the bones, if possible, instead of adding a number extension
   :type do_flip_names: boolean, (optional)

.. function:: duplicate_move(*, ARMATURE_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Make copies of the selected bones within the same armature and move them

   :arg ARMATURE_OT_duplicate: Duplicate Selected Bone(s), Make copies of the selected bones within the same armature
   :type ARMATURE_OT_duplicate: :class:`ARMATURE_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude(*, forked=False)

   Create new bones from the selected joints

   :arg forked: Forked
   :type forked: boolean, (optional)

.. function:: extrude_forked(*, ARMATURE_OT_extrude=None, TRANSFORM_OT_translate=None)

   Create new bones from the selected joints and move them

   :arg ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints
   :type ARMATURE_OT_extrude: :class:`ARMATURE_OT_extrude`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude_move(*, ARMATURE_OT_extrude=None, TRANSFORM_OT_translate=None)

   Create new bones from the selected joints and move them

   :arg ARMATURE_OT_extrude: Extrude, Create new bones from the selected joints
   :type ARMATURE_OT_extrude: :class:`ARMATURE_OT_extrude`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: fill()

   Add bone between selected joint(s) and/or 3D cursor

.. function:: flip_names(*, do_strip_numbers=False)

   Flips (and corrects) the axis suffixes of the names of selected bones

   :arg do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names.Warning: May result in incoherent naming in some cases
   :type do_strip_numbers: boolean, (optional)

.. function:: hide(*, unselected=False)

   Tag selected bones to not be visible in Edit Mode

   :arg unselected: Unselected, Hide unselected rather than selected
   :type unselected: boolean, (optional)

.. function:: move_to_collection(*, collection_index=-1, new_collection_name="")

   Move bones to a collection

   :arg collection_index: Collection Index, Index of the collection to move selected bones to. When the operator should create a new bone collection, do not include this parameter and pass new_collection_name
   :type collection_index: int in [-1, inf], (optional)
   :arg new_collection_name: Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and move the selected bones to it. To move to an existing collection, do not include this parameter and use collection_index
   :type new_collection_name: string, (optional, never None)

.. function:: parent_clear(*, type='CLEAR')

   Remove the parent-child relationship between selected bones and their parents

   :arg type: Clear Type, What way to clear parenting
   :type type: enum in [``'CLEAR'``, ``'DISCONNECT'``], (optional)

.. function:: parent_set(*, type='CONNECTED')

   Set the active bone as the parent of the selected bones

   :arg type: Parent Type, Type of parenting
   :type type: enum in [``'CONNECTED'``, ``'OFFSET'``], (optional)

.. function:: reveal(*, select=True)

   Reveal all bones hidden in Edit Mode

   :arg select: Select
   :type select: boolean, (optional)

.. function:: roll_clear(*, roll=0.0)

   Clear roll for selected bones

   :arg roll: Roll
   :type roll: float in [-6.28319, 6.28319], (optional)

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

.. function:: select_hierarchy(*, direction='PARENT', extend=False)

   Select immediate parent/children of selected bones

   :arg direction: Direction
   :type direction: enum in [``'PARENT'``, ``'CHILD'``], (optional)
   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: select_less()

   Deselect those bones at the boundary of each selection region

.. function:: select_linked(*, all_forks=False)

   Select all bones linked by parent/child connections to the current selection

   :arg all_forks: All Forks, Follow forks in the parents chain
   :type all_forks: boolean, (optional)

.. function:: select_linked_pick(*, deselect=False, all_forks=False)

   (De)select bones linked by parent/child connections under the mouse cursor

   :arg deselect: Deselect
   :type deselect: boolean, (optional)
   :arg all_forks: All Forks, Follow forks in the parents chain
   :type all_forks: boolean, (optional)

.. function:: select_mirror(*, only_active=False, extend=False)

   Mirror the bone selection

   :arg only_active: Active Only, Only operate on the active bone
   :type only_active: boolean, (optional)
   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: select_more()

   Select those bones connected to the initial selection

.. function:: select_similar(*, type='LENGTH', threshold=0.1)

   Select similar bones by property types

   :arg type: Type
   :type type: enum in [``'CHILDREN'``, ``'CHILDREN_IMMEDIATE'``, ``'SIBLINGS'``, ``'LENGTH'``, ``'DIRECTION'``, ``'PREFIX'``, ``'SUFFIX'``, ``'BONE_COLLECTION'``, ``'COLOR'``, ``'SHAPE'``], (optional)
   :arg threshold: Threshold
   :type threshold: float in [0, 1], (optional)

.. function:: separate()

   Isolate selected bones into a separate armature

.. function:: shortest_path_pick()

   Select shortest path between two bones

.. function:: split()

   Split off selected bones from connected unselected bones

.. function:: subdivide(*, number_cuts=1)

   Break selected bones into chains of smaller bones

   :arg number_cuts: Number of Cuts
   :type number_cuts: int in [1, 1000], (optional)

.. function:: switch_direction()

   Change the direction that a chain of bones points in (head and tail swap)

.. function:: symmetrize(*, direction='NEGATIVE_X', copy_bone_colors=False)

   Enforce symmetry, make copies of the selection or use existing

   :arg direction: Direction, Which sides to copy from and to (when both are selected)
   :type direction: enum in [``'NEGATIVE_X'``, ``'POSITIVE_X'``], (optional)
   :arg copy_bone_colors: Bone Colors, Copy colors to existing bones
   :type copy_bone_colors: boolean, (optional)

