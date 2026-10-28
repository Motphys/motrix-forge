GPU Texture Utilities (gpu.texture)
===================================

.. module:: gpu.texture

This module provides utils for textures.

.. function:: from_image(image)

   Get GPUTexture corresponding to an Image datablock. The GPUTexture memory is shared with Blender.
   Note: Colors read from the texture will be in scene linear color space and have premultiplied or straight alpha matching the image alpha mode.

   :arg image: The Image datablock.
   :type image: :class:`bpy.types.Image`
   :return: The GPUTexture used by the image.
   :rtype: :class:`gpu.types.GPUTexture`


