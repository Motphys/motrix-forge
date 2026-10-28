Image Buffer Types (imbuf.types)
================================

.. module:: imbuf.types

This module provides access to image buffer types.

.. note::

   Image buffer is also the structure used by :class:`bpy.types.Image`
   ID type to store and manipulate image data at runtime.

.. class:: imbuf.types.ImBuf


   .. method:: copy()
   
      :return: A copy of the image.
      :rtype: :class:`ImBuf`


   .. method:: crop(min, max)
   
      Crop the image.
   
      :arg min: X, Y minimum.
      :type min: tuple[int, int]
      :arg max: X, Y maximum.
      :type max: tuple[int, int]


   .. method:: free()
   
      Clear image data immediately (causing an error on re-use).


   .. method:: resize(size, method='FAST')
   
      Resize the image.
   
      :arg size: New size.
      :type size: tuple[int, int]
      :arg method: Method of resizing ('FAST', 'BILINEAR')
      :type method: str


   .. attribute:: channels

      Number of bit-planes.
      
      :type: int


   .. attribute:: filepath

      filepath associated with this image.
      
      :type: str


   .. attribute:: planes

      Number of bits associated with this image.
      
      :type: int


   .. attribute:: ppm

      pixels per meter.
      
      :type: pair of floats


   .. attribute:: size

      size of the image in pixels.
      
      :type: pair of ints




