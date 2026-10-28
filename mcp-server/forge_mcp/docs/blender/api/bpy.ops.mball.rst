Mball Operators
===============

.. module:: bpy.ops.mball

.. function:: delete_metaelems(*, confirm=True)

   Delete selected metaball element(s)

   :arg confirm: Confirm, Prompt for confirmation
   :type confirm: boolean, (optional)

.. function:: duplicate_metaelems()

   Duplicate selected metaball element(s)

.. function:: duplicate_move(*, MBALL_OT_duplicate_metaelems=None, TRANSFORM_OT_translate=None)

   Make copies of the selected metaball elements and move them

   :arg MBALL_OT_duplicate_metaelems: Duplicate Metaball Elements, Duplicate selected metaball element(s)
   :type MBALL_OT_duplicate_metaelems: :class:`MBALL_OT_duplicate_metaelems`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: hide_metaelems(*, unselected=False)

   Hide (un)selected metaball element(s)

   :arg unselected: Unselected, Hide unselected rather than selected
   :type unselected: boolean, (optional)

.. function:: reveal_metaelems(*, select=True)

   Reveal all hidden metaball elements

   :arg select: Select
   :type select: boolean, (optional)

.. function:: select_all(*, action='TOGGLE')

   Change selection of all metaball elements

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

.. function:: select_random_metaelems(*, ratio=0.5, seed=0, action='SELECT')

   Randomly select metaball elements

   :arg ratio: Ratio, Portion of items to select randomly
   :type ratio: float in [0, 1], (optional)
   :arg seed: Random Seed, Seed for the random number generator
   :type seed: int in [0, inf], (optional)
   :arg action: Action, Selection action to execute

      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
   :type action: enum in [``'SELECT'``, ``'DESELECT'``], (optional)

.. function:: select_similar(*, type='TYPE', threshold=0.1)

   Select similar metaballs by property types

   :arg type: Type
   :type type: enum in [``'TYPE'``, ``'RADIUS'``, ``'STIFFNESS'``, ``'ROTATION'``], (optional)
   :arg threshold: Threshold
   :type threshold: float in [0, inf], (optional)

