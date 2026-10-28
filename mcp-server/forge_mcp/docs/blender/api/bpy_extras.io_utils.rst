bpy_extras submodule (bpy_extras.io_utils)
==========================================

.. module:: bpy_extras.io_utils

.. function:: orientation_helper(axis_forward='Y', axis_up='Z')

   A decorator for import/export classes, generating properties needed by the axis conversion system and IO helpers,
   with specified default values (axes).

.. function:: axis_conversion(from_forward='Y', from_up='Z', to_forward='Y', to_up='Z')

   Each argument us an axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z']
   where the first 2 are a source and the second 2 are the target.

.. function:: axis_conversion_ensure(operator, forward_attr, up_attr)

   Function to ensure an operator has valid axis conversion settings, intended
   to be used from :class:`bpy.types.Operator.check`.
   
   :arg operator: the operator to access axis attributes from.
   :type operator: :class:`bpy.types.Operator`
   :arg forward_attr: attribute storing the forward axis
   :type forward_attr: str
   :arg up_attr: attribute storing the up axis
   :type up_attr: str
   :return: True if the value was modified.
   :rtype: bool

.. function:: create_derived_objects(depsgraph, objects)

   This function takes a sequence of objects, returning their instances.
   
   :arg depsgraph: The evaluated depsgraph.
   :type depsgraph: :class:`bpy.types.Depsgraph`
   :arg objects: A sequencer of objects.
   :type objects: Sequence[:class:`bpy.types.Object`]
   :return: A dictionary where each key is an object from ``objects``,
      values are lists of (object, matrix) tuples representing instances.
   :rtype: dict[:class:`bpy.types.Object`, list[tuple[:class:`bpy.types.Object`, :class:`mathutils.Matrix`]]]

.. function:: poll_file_object_drop(context)

   A default implementation for FileHandler poll_drop methods. Allows for both the 3D Viewport and
   the Outliner (in ViewLayer display mode) to be targets for file drag and drop.

.. function:: unpack_list(list_of_tuples)

.. function:: unpack_face_list(list_of_tuples)

.. function:: path_reference(filepath, base_src, base_dst, mode='AUTO', copy_subdir='', copy_set=None, library=None)

   Return a filepath relative to a destination directory, for use with
   exporters.
   
   :arg filepath: the file path to return,
      supporting blenders relative '//' prefix.
   :type filepath: str
   :arg base_src: the directory the *filepath* is relative too
      (normally the blend file).
   :type base_src: str
   :arg base_dst: the directory the *filepath* will be referenced from
      (normally the export path).
   :type base_dst: str
   :arg mode: the method used get the path in
      ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY']
   :type mode: str
   :arg copy_subdir: the subdirectory of *base_dst* to use when mode='COPY'.
   :type copy_subdir: str
   :arg copy_set: collect from/to pairs when mode='COPY',
      pass to *path_reference_copy* when exporting is done.
   :type copy_set: set[tuple[str, str]]
   :arg library: The library this path is relative to.
   :type library: :class:`bpy.types.Library` | None
   :return: the new filepath.
   :rtype: str

.. function:: path_reference_copy(copy_set, report=<built-in function print>)

   Execute copying files of path_reference
   
   :arg copy_set: set of (from, to) pairs to copy.
   :type copy_set: set[tuple[str, str]]
   :arg report: function used for reporting warnings, takes a string argument.
   :type report: Callable[[str], None]

.. function:: unique_name(key, name, name_dict, name_max=-1, clean_func=None, sep='.')

   Helper function for storing unique names which may have special characters
   stripped and restricted to a maximum length.
   
   :arg key: Unique item this name belongs to, name_dict[key] will be reused
      when available.
      This can be the object, mesh, material, etc instance itself.
      Any hashable object associated with the *name*.
   :type key: Any
   :arg name: The name used to create a unique value in *name_dict*.
   :type name: str
   :arg name_dict: This is used to cache namespace to ensure no collisions
      occur, this should be an empty dict initially and only modified by this
      function.
   :type name_dict: dict
   :arg clean_func: Function to call on *name* before creating a unique value.
   :type clean_func: function
   :arg sep: Separator to use when between the name and a number when a
      duplicate name is found.
   :type sep: str

.. class:: bpy_extras.io_utils.ExportHelper


   .. method:: check(_context)

   .. method:: invoke(context, _event)



.. class:: bpy_extras.io_utils.ImportHelper


   .. method:: check(_context)

   .. method:: invoke(context, _event)

   .. method:: invoke_popup(context, confirm_text='')



