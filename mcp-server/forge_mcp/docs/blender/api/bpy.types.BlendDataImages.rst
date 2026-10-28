BlendDataImages(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataImages(bpy_struct)

   Collection of images

   .. method:: new(name, width, height, *, alpha=False, float_buffer=False, stereo3d=False, is_data=False, tiled=False)

      Add a new image to the main database

      :arg name: New name for the data-block
      :type name: string, (never None)
      :arg width: Width of the image
      :type width: int in [1, inf]
      :arg height: Height of the image
      :type height: int in [1, inf]
      :arg alpha: Alpha, Use alpha channel
      :type alpha: boolean, (optional)
      :arg float_buffer: Float Buffer, Create an image with floating-point color
      :type float_buffer: boolean, (optional)
      :arg stereo3d: Stereo 3D, Create left and right views
      :type stereo3d: boolean, (optional)
      :arg is_data: Is Data, Create image with non-color data color space
      :type is_data: boolean, (optional)
      :arg tiled: Tiled, Create a tiled image
      :type tiled: boolean, (optional)
      :return: New image data-block
      :rtype: :class:`Image`

   .. method:: load(filepath, *, check_existing=False)

      Load a new image into the main database

      :arg filepath: Path of the file to load
      :type filepath: string, (never None, blend relative ``//`` prefix supported)
      :arg check_existing: Using existing data-block if this file is already loaded
      :type check_existing: boolean, (optional)
      :return: New image data-block
      :rtype: :class:`Image`

   .. method:: remove(image, *, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove an image from the current blendfile

      :arg image: Image to remove
      :type image: :class:`Image`, (never None)
      :arg do_unlink: Unlink all usages of this image before deleting it
      :type do_unlink: boolean, (optional)
      :arg do_id_user: Decrement user counter of all datablocks used by this image
      :type do_id_user: boolean, (optional)
      :arg do_ui_user: Make sure interface does not reference this image
      :type do_ui_user: boolean, (optional)

   .. method:: tag(value)

      tag

      :arg value: Value
      :type value: boolean

   .. classmethod:: bl_rna_get_subclass(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None, /)
   
      :arg id: The RNA type identifier.
      :type id: str
      :return: The class or default when not found.
      :rtype: type


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

Inherited Functions
-------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.id_properties_clear`
   * :class:`bpy_struct.id_properties_ensure`
   * :class:`bpy_struct.id_properties_ui`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_overridable_library`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.pop`
   * :class:`bpy_struct.property_overridable_library_set`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.rna_ancestors`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

References
----------

.. hlist::
   :columns: 2

   * :class:`BlendData.images`

