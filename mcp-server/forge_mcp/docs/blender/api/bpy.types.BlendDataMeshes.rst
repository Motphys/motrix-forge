BlendDataMeshes(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataMeshes(bpy_struct)

   Collection of meshes

   .. method:: new(name)

      Add a new mesh to the main database

      :arg name: New name for the data-block
      :type name: string, (never None)
      :return: New mesh data-block
      :rtype: :class:`Mesh`

   .. method:: new_from_object(object, *, preserve_all_data_layers=False, depsgraph=None)

      Add a new mesh created from given object (undeformed geometry if object is original, and final evaluated geometry, with all modifiers etc., if object is evaluated)

      :arg object: Object to create mesh from
      :type object: :class:`Object`, (never None)
      :arg preserve_all_data_layers: Preserve all data layers in the mesh, like UV maps and vertex groups. By default Blender only computes the subset of data layers needed for viewport display and rendering, for better performance.
      :type preserve_all_data_layers: boolean, (optional)
      :arg depsgraph: Dependency Graph, Evaluated dependency graph which is required when preserve_all_data_layers is true
      :type depsgraph: :class:`Depsgraph`, (optional)
      :return: Mesh created from object, remove it if it is only used for export
      :rtype: :class:`Mesh`

   .. method:: remove(mesh, *, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a mesh from the current blendfile

      :arg mesh: Mesh to remove
      :type mesh: :class:`Mesh`, (never None)
      :arg do_unlink: Unlink all usages of this mesh before deleting it (WARNING: will also delete objects instancing that mesh data)
      :type do_unlink: boolean, (optional)
      :arg do_id_user: Decrement user counter of all datablocks used by this mesh data
      :type do_id_user: boolean, (optional)
      :arg do_ui_user: Make sure interface does not reference this mesh data
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

   * :class:`BlendData.meshes`

