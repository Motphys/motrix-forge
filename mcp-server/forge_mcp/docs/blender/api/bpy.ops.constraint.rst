Constraint Operators
====================

.. module:: bpy.ops.constraint

.. function:: add_target()

   Add a target to the constraint

   :File: `startup\bl_operators\constraint.py\:26 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\constraint.py#L26>`__

.. function:: apply(*, constraint="", owner='OBJECT', report=False)

   Apply constraint and remove from the stack

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)
   :arg report: Report, Create a notification after the operation
   :type report: boolean, (optional)

.. function:: childof_clear_inverse(*, constraint="", owner='OBJECT')

   Clear inverse correction for Child Of constraint

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)

.. function:: childof_set_inverse(*, constraint="", owner='OBJECT')

   Set inverse correction for Child Of constraint

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)

.. function:: copy(*, constraint="", owner='OBJECT', report=False)

   Duplicate constraint at the same position in the stack

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)
   :arg report: Report, Create a notification after the operation
   :type report: boolean, (optional)

.. function:: copy_to_selected(*, constraint="", owner='OBJECT')

   Copy constraint to other selected objects/bones

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)

.. function:: delete(*, constraint="", owner='OBJECT', report=False)

   Remove constraint from constraint stack

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)
   :arg report: Report, Create a notification after the operation
   :type report: boolean, (optional)

.. function:: disable_keep_transform()

   Set the influence of this constraint to zero while trying to maintain the object's transformation. Other active constraints can still influence the final transformation

   :File: `startup\bl_operators\constraint.py\:86 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\constraint.py#L86>`__

.. function:: followpath_path_animate(*, constraint="", owner='OBJECT', frame_start=1, length=100)

   Add default animation for path used by constraint if it isn't animated already

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)
   :arg frame_start: Start Frame, First frame of path animation
   :type frame_start: int in [-1048574, 1048574], (optional)
   :arg length: Length, Number of frames that path animation should take
   :type length: int in [0, 1048574], (optional)

.. function:: limitdistance_reset(*, constraint="", owner='OBJECT')

   Reset limiting distance for Limit Distance Constraint

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)

.. function:: move_down(*, constraint="", owner='OBJECT')

   Move constraint down in constraint stack

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)

.. function:: move_to_index(*, constraint="", owner='OBJECT', index=0)

   Change the constraint's position in the list so it evaluates after the set number of others

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)
   :arg index: Index, The index to move the constraint to
   :type index: int in [0, inf], (optional)

.. function:: move_up(*, constraint="", owner='OBJECT')

   Move constraint up in constraint stack

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)

.. function:: normalize_target_weights()

   Normalize weights of all target bones

   :File: `startup\bl_operators\constraint.py\:61 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\constraint.py#L61>`__

.. function:: objectsolver_clear_inverse(*, constraint="", owner='OBJECT')

   Clear inverse correction for Object Solver constraint

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)

.. function:: objectsolver_set_inverse(*, constraint="", owner='OBJECT')

   Set inverse correction for Object Solver constraint

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)

.. function:: remove_target(*, index=0)

   Remove the target from the constraint

   :arg index: index
   :type index: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\constraint.py\:44 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\constraint.py#L44>`__


.. function:: stretchto_reset(*, constraint="", owner='OBJECT')

   Reset original length of bone for Stretch To Constraint

   :arg constraint: Constraint, Name of the constraint to edit
   :type constraint: string, (optional, never None)
   :arg owner: Owner, The owner of this constraint

      * ``OBJECT``
        Object -- Edit a constraint on the active object.
      * ``BONE``
        Bone -- Edit a constraint on the active bone.
   :type owner: enum in [``'OBJECT'``, ``'BONE'``], (optional)

