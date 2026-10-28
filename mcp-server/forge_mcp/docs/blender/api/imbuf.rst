Image Buffer (imbuf)
====================

.. module:: imbuf

This module provides access to Blender's image manipulation API.

It provides access to image buffers outside of Blender's
:class:`bpy.types.Image` data-block context.

.. toctree::
   :maxdepth: 1
   :caption: Submodules

   imbuf.types.rst

.. function:: load(filepath)

   Load an image from a file.

   :arg filepath: the filepath of the image.
   :type filepath: str | bytes
   :return: the newly loaded image.
   :rtype: :class:`ImBuf`


.. function:: load_from_buffer(buffer)

   Load an image from a buffer.

   :arg buffer: A buffer containing the image data.
   :type buffer: collections.abc.Buffer
   :return: the newly loaded image.
   :rtype: :class:`ImBuf`


.. function:: new(size)

   Load a new image.

   :arg size: The size of the image in pixels.
   :type size: tuple[int, int]
   :return: the newly loaded image.
   :rtype: :class:`ImBuf`


.. function:: write(image, filepath=image.filepath)

   Write an image.

   :arg image: the image to write.
   :type image: :class:`ImBuf`
   :arg filepath: Optional filepath of the image (fallback to the images file path).
   :type filepath: str | bytes | None


