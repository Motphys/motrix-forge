Sculpt Curves Operators
=======================

.. module:: bpy.ops.sculpt_curves

.. function:: brush_stroke(*, stroke=None, mode='NORMAL', pen_flip=False)

   Sculpt curves using a brush

   :arg stroke: Stroke
   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg mode: Stroke Mode, Action taken when a paint stroke is made

      * ``NORMAL``
        Regular -- Apply brush normally.
      * ``INVERT``
        Invert -- Invert action of brush for duration of stroke.
      * ``SMOOTH``
        Smooth -- Switch brush to smooth mode for duration of stroke.
      * ``ERASE``
        Erase -- Switch brush to erase mode for duration of stroke.
   :type mode: enum in [``'NORMAL'``, ``'INVERT'``, ``'SMOOTH'``, ``'ERASE'``], (optional)
   :arg pen_flip: Pen Flip, Whether a tablet's eraser mode is being used
   :type pen_flip: boolean, (optional)

.. function:: min_distance_edit()

   Change the minimum distance used by the density brush

.. function:: select_grow(*, distance=0.1)

   Select curves which are close to curves that are selected already

   :arg distance: Distance, By how much to grow the selection
   :type distance: float in [-inf, inf], (optional)

.. function:: select_random(*, seed=0, partial=False, probability=0.5, min=0.0, constant_per_curve=True)

   Randomizes existing selection or create new random selection

   :arg seed: Seed, Source of randomness
   :type seed: int in [-inf, inf], (optional)
   :arg partial: Partial, Allow points or curves to be selected partially
   :type partial: boolean, (optional)
   :arg probability: Probability, Chance of every point or curve being included in the selection
   :type probability: float in [0, 1], (optional)
   :arg min: Min, Minimum value for the random selection
   :type min: float in [0, 1], (optional)
   :arg constant_per_curve: Constant per Curve, The generated random number is the same for every control point of a curve
   :type constant_per_curve: boolean, (optional)

