Pointcloud Operators
====================

.. module:: bpy.ops.pointcloud

.. function:: attribute_set(*, value_float=0.0, value_float_vector_2d=(0.0, 0.0), value_float_vector_3d=(0.0, 0.0, 0.0), value_int=0, value_int_vector_2d=(0, 0), value_color=(1.0, 1.0, 1.0, 1.0), value_bool=False)

   Set values of the active attribute for selected elements

   :arg value_float: Value
   :type value_float: float in [-inf, inf], (optional)
   :arg value_float_vector_2d: Value
   :type value_float_vector_2d: float array of 2 items in [-inf, inf], (optional)
   :arg value_float_vector_3d: Value
   :type value_float_vector_3d: float array of 3 items in [-inf, inf], (optional)
   :arg value_int: Value
   :type value_int: int in [-inf, inf], (optional)
   :arg value_int_vector_2d: Value
   :type value_int_vector_2d: int array of 2 items in [-inf, inf], (optional)
   :arg value_color: Value
   :type value_color: float array of 4 items in [-inf, inf], (optional)
   :arg value_bool: Value
   :type value_bool: boolean, (optional)

.. function:: delete()

   Remove selected points

.. function:: duplicate()

   Copy selected points

.. function:: duplicate_move(*, POINTCLOUD_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Make copies of selected elements and move them

   :arg POINTCLOUD_OT_duplicate: Duplicate, Copy selected points
   :type POINTCLOUD_OT_duplicate: :class:`POINTCLOUD_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: select_all(*, action='TOGGLE')

   (De)select all point cloud

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

.. function:: select_random(*, seed=0, probability=0.5)

   Randomizes existing selection or create new random selection

   :arg seed: Seed, Source of randomness
   :type seed: int in [-inf, inf], (optional)
   :arg probability: Probability, Chance of every point being included in the selection
   :type probability: float in [0, 1], (optional)

.. function:: separate()

   Separate selected geometry into a new point cloud

