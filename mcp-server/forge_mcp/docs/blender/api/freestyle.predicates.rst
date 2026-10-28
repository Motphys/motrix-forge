Freestyle Predicates (freestyle.predicates)
===========================================

.. module:: freestyle.predicates

This module contains predicates operating on vertices (0D elements)
and polylines (1D elements).  It is also intended to be a collection
of examples for predicate definition in Python.

User-defined predicates inherit one of the following base classes,
depending on the object type (0D or 1D) to operate on and the arity
(unary or binary):

- :class:`freestyle.types.BinaryPredicate0D`
- :class:`freestyle.types.BinaryPredicate1D`
- :class:`freestyle.types.UnaryPredicate0D`
- :class:`freestyle.types.UnaryPredicate1D`

.. class:: freestyle.predicates.AndBP1D




.. class:: freestyle.predicates.AndUP1D




.. class:: freestyle.predicates.ContourUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`ContourUP1D`
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D is a contour. An Interface1D is a
      contour if it is bordered by a different shape on each of its sides.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the Interface1D is a contour, false otherwise.
      :rtype: bool



.. class:: freestyle.predicates.DensityLowerThanUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`DensityLowerThanUP1D`
   
   .. method:: __init__(threshold, sigma=2.0)
   
      Builds a DensityLowerThanUP1D object.
   
      :arg threshold: The value of the threshold density. Any Interface1D
         having a density lower than this threshold will match.
      :type threshold: float
      :arg sigma: The sigma value defining the density evaluation window
         size used in the :class:`freestyle.functions.DensityF0D` functor.
      :type sigma: float
   
   .. method:: __call__(inter)
   
      Returns true if the density evaluated for the Interface1D is less
      than a user-defined density value.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the density is lower than a threshold.
      :rtype: bool



.. class:: freestyle.predicates.EqualToChainingTimeStampUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`freestyle.types.EqualToChainingTimeStampUP1D`
   
   .. method:: __init__(ts)
   
      Builds a EqualToChainingTimeStampUP1D object.
   
      :arg ts: A time stamp value.
      :type ts: int
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D's time stamp is equal to a certain
      user-defined value.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the time stamp is equal to a user-defined value.
      :rtype: bool



.. class:: freestyle.predicates.EqualToTimeStampUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`EqualToTimeStampUP1D`
   
   .. method:: __init__(ts)
   
      Builds a EqualToTimeStampUP1D object.
   
      :arg ts: A time stamp value.
      :type ts: int
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D's time stamp is equal to a certain
      user-defined value.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the time stamp is equal to a user-defined value.
      :rtype: bool



.. class:: freestyle.predicates.ExternalContourUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`ExternalContourUP1D`
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D is an external contour.
      An Interface1D is an external contour if it is bordered by no shape on
      one of its sides.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the Interface1D is an external contour, false
         otherwise.
      :rtype: bool



.. class:: freestyle.predicates.FalseBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`FalseBP1D`
   
   .. method:: __call__(inter1, inter2)
   
      Always returns false.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: False.
      :rtype: bool



.. class:: freestyle.predicates.FalseUP0D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate0D` > :class:`FalseUP0D`
   
   .. method:: __call__(it)
   
      Always returns false.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: False.
      :rtype: bool



.. class:: freestyle.predicates.FalseUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`FalseUP1D`
   
   .. method:: __call__(inter)
   
      Always returns false.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: False.
      :rtype: bool



.. class:: freestyle.predicates.Length2DBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`Length2DBP1D`
   
   .. method:: __call__(inter1, inter2)
   
      Returns true if the 2D length of inter1 is less than the 2D length
      of inter2.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: True or false.
      :rtype: bool



.. class:: freestyle.predicates.MaterialBP1D

   Checks whether the two supplied ViewEdges have the same material.



.. class:: freestyle.predicates.NotBP1D




.. class:: freestyle.predicates.NotUP1D




.. class:: freestyle.predicates.ObjectNamesUP1D




.. class:: freestyle.predicates.OrBP1D




.. class:: freestyle.predicates.OrUP1D




.. class:: freestyle.predicates.QuantitativeInvisibilityRangeUP1D




.. class:: freestyle.predicates.QuantitativeInvisibilityUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`QuantitativeInvisibilityUP1D`
   
   .. method:: __init__(qi=0)
   
      Builds a QuantitativeInvisibilityUP1D object.
   
      :arg qi: The Quantitative Invisibility you want the Interface1D to
         have.
      :type qi: int
   
   .. method:: __call__(inter)
   
      Returns true if the Quantitative Invisibility evaluated at an
      Interface1D, using the
      :class:`freestyle.functions.QuantitativeInvisibilityF1D` functor,
      equals a certain user-defined value.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if Quantitative Invisibility equals a user-defined
         value.
      :rtype: bool



.. class:: freestyle.predicates.SameShapeIdBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`SameShapeIdBP1D`
   
   .. method:: __call__(inter1, inter2)
   
      Returns true if inter1 and inter2 belong to the same shape.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: True or false.
      :rtype: bool



.. class:: freestyle.predicates.ShapeUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`ShapeUP1D`
   
   .. method:: __init__(first, second=0)
   
      Builds a ShapeUP1D object.
   
      :arg first: The first Id component.
      :type first: int
      :arg second: The second Id component.
      :type second: int
   
   .. method:: __call__(inter)
   
      Returns true if the shape to which the Interface1D belongs to has the
      same :class:`freestyle.types.Id` as the one specified by the user.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if Interface1D belongs to the shape of the
         user-specified Id.
      :rtype: bool



.. class:: freestyle.predicates.TrueBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`TrueBP1D`
   
   .. method:: __call__(inter1, inter2)
   
      Always returns true.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: True.
      :rtype: bool



.. class:: freestyle.predicates.TrueUP0D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate0D` > :class:`TrueUP0D`
   
   .. method:: __call__(it)
   
      Always returns true.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: True.
      :rtype: bool



.. class:: freestyle.predicates.TrueUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`TrueUP1D`
   
   .. method:: __call__(inter)
   
      Always returns true.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True.
      :rtype: bool



.. class:: freestyle.predicates.ViewMapGradientNormBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`ViewMapGradientNormBP1D`
   
   .. method:: __init__(level, integration_type=IntegrationType.MEAN, sampling=2.0)
   
      Builds a ViewMapGradientNormBP1D object.
   
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
      :arg sampling: The resolution used to sample the chain:
         GetViewMapGradientNormF0D is evaluated at each sample point and
         the result is obtained by combining the resulting values into a
         single one, following the method specified by integration_type.
      :type sampling: float
   
   .. method:: __call__(inter1, inter2)
   
      Returns true if the evaluation of the Gradient norm Function is
      higher for inter1 than for inter2.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: True or false.
      :rtype: bool



.. class:: freestyle.predicates.WithinImageBoundaryUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`WithinImageBoundaryUP1D`
   
   .. method:: __init__(xmin, ymin, xmax, ymax)
   
      Builds an WithinImageBoundaryUP1D object.
   
      :arg xmin: X lower bound of the image boundary.
      :type xmin: float
      :arg ymin: Y lower bound of the image boundary.
      :type ymin: float
      :arg xmax: X upper bound of the image boundary.
      :type xmax: float
      :arg ymax: Y upper bound of the image boundary.
      :type ymax: float
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D intersects with image boundary.



.. class:: freestyle.predicates.pyBackTVertexUP0D

   Check whether an Interface0DIterator references a TVertex and is
   the one that is hidden (inferred from the context).



.. class:: freestyle.predicates.pyClosedCurveUP1D




.. class:: freestyle.predicates.pyDensityFunctorUP1D




.. class:: freestyle.predicates.pyDensityUP1D




.. class:: freestyle.predicates.pyDensityVariableSigmaUP1D




.. class:: freestyle.predicates.pyHighDensityAnisotropyUP1D




.. class:: freestyle.predicates.pyHighDirectionalViewMapDensityUP1D




.. class:: freestyle.predicates.pyHighSteerableViewMapDensityUP1D




.. class:: freestyle.predicates.pyHighViewMapDensityUP1D




.. class:: freestyle.predicates.pyHighViewMapGradientNormUP1D




.. class:: freestyle.predicates.pyHigherCurvature2DAngleUP0D




.. class:: freestyle.predicates.pyHigherLengthUP1D




.. class:: freestyle.predicates.pyHigherNumberOfTurnsUP1D




.. class:: freestyle.predicates.pyIsInOccludersListUP1D




.. class:: freestyle.predicates.pyIsOccludedByIdListUP1D




.. class:: freestyle.predicates.pyIsOccludedByItselfUP1D




.. class:: freestyle.predicates.pyIsOccludedByUP1D




.. class:: freestyle.predicates.pyLengthBP1D




.. class:: freestyle.predicates.pyLowDirectionalViewMapDensityUP1D




.. class:: freestyle.predicates.pyLowSteerableViewMapDensityUP1D




.. class:: freestyle.predicates.pyNFirstUP1D




.. class:: freestyle.predicates.pyNatureBP1D




.. class:: freestyle.predicates.pyNatureUP1D




.. class:: freestyle.predicates.pyParameterUP0D




.. class:: freestyle.predicates.pyParameterUP0DGoodOne




.. class:: freestyle.predicates.pyProjectedXBP1D




.. class:: freestyle.predicates.pyProjectedYBP1D




.. class:: freestyle.predicates.pyShapeIdListUP1D




.. class:: freestyle.predicates.pyShapeIdUP1D




.. class:: freestyle.predicates.pyShuffleBP1D




.. class:: freestyle.predicates.pySilhouetteFirstBP1D




.. class:: freestyle.predicates.pyUEqualsUP0D




.. class:: freestyle.predicates.pyVertexNatureUP0D




.. class:: freestyle.predicates.pyViewMapGradientNormBP1D




.. class:: freestyle.predicates.pyZBP1D




.. class:: freestyle.predicates.pyZDiscontinuityBP1D




.. class:: freestyle.predicates.pyZSmallerUP1D




