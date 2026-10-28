Additional Math Functions (bl_math)
===================================

.. module:: bl_math

Miscellaneous math utilities module

.. function:: clamp(value, min=0, max=1)

   Clamps the float value between minimum and maximum. To avoid
   confusion, any call must use either one or all three arguments.

   :arg value: The value to clamp.
   :type value: float
   :arg min: The minimum value, defaults to 0.
   :type min: float
   :arg max: The maximum value, defaults to 1.
   :type max: float
   :return: The clamped value.
   :rtype: float


.. function:: lerp(from_value, to_value, factor)

   Linearly interpolate between two float values based on factor.

   :arg from_value: The value to return when factor is 0.
   :type from_value: float
   :arg to_value: The value to return when factor is 1.
   :type to_value: float
   :arg factor: The interpolation value, normally in [0.0, 1.0].
   :type factor: float
   :return: The interpolated value.
   :rtype: float


.. function:: smoothstep(from_value, to_value, value)

   Performs smooth interpolation between 0 and 1 as value changes between from and to values.
   Outside the range the function returns the same value as the nearest edge.

   :arg from_value: The edge value where the result is 0.
   :type from_value: float
   :arg to_value: The edge value where the result is 1.
   :type to_value: float
   :arg factor: The interpolation value.
   :type factor: float
   :return: The interpolated value in [0.0, 1.0].
   :rtype: float


