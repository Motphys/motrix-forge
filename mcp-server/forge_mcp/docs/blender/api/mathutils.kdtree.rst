KDTree Utilities (mathutils.kdtree)
===================================

.. module:: mathutils.kdtree

Generic 3-dimensional kd-tree to perform spatial searches.


.. literalinclude:: ..\examples\mathutils.kdtree.py

.. class:: mathutils.kdtree.KDTree

   KdTree(size) -> new kd-tree initialized to hold ``size`` items.
   
   .. note::
   
      :class:`KDTree.balance` must have been called before using any of the ``find`` methods.

   .. method:: balance()
   
      Balance the tree.
   
   .. note::
   
      This builds the entire tree, avoid calling after each insertion.


   .. method:: find(co, filter=None)
   
      Find nearest point to ``co``.
   
      :arg co: 3D coordinates.
      :type co: Sequence[float]
      :arg filter: function which takes an index and returns True for indices to include in the search.
      :type filter: Callable[[int], bool]
      :return: Returns (position, index, distance).
      :rtype: tuple[:class:`Vector`, int, float]


   .. method:: find_n(co, n)
   
      Find nearest ``n`` points to ``co``.
   
      :arg co: 3D coordinates.
      :type co: Sequence[float]
      :arg n: Number of points to find.
      :type n: int
      :return: Returns a list of tuples (position, index, distance).
      :rtype: list[tuple[:class:`Vector`, int, float]]


   .. method:: find_range(co, radius)
   
      Find all points within ``radius`` of ``co``.
   
      :arg co: 3D coordinates.
      :type co: Sequence[float]
      :arg radius: Distance to search for points.
      :type radius: float
      :return: Returns a list of tuples (position, index, distance).
      :rtype: list[tuple[:class:`Vector`, int, float]]


   .. method:: insert(co, index)
   
      Insert a point into the KDTree.
   
      :arg co: Point 3d position.
      :type co: Sequence[float]
      :arg index: The index of the point.
      :type index: int




