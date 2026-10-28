BlendDataNodeTrees(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataNodeTrees(bpy_struct)

   Collection of node trees

   .. method:: new(name, type)

      Add a new node tree to the main database

      :arg name: New name for the data-block
      :type name: string, (never None)
      :arg type: Type, The type of node_group to add

         * ``GeometryNodeTree``
           Geometry Node Editor -- Geometry nodes.
         * ``CompositorNodeTree``
           Compositor -- Compositing nodes.
         * ``ShaderNodeTree``
           Shader Editor -- Shader nodes.
         * ``TextureNodeTree``
           Texture Node Editor -- Texture nodes.
      :type type: enum in [``'GeometryNodeTree'``, ``'CompositorNodeTree'``, ``'ShaderNodeTree'``, ``'TextureNodeTree'``]
      :return: New node tree data-block
      :rtype: :class:`NodeTree`

   .. method:: remove(tree, *, do_unlink=True, do_id_user=True, do_ui_user=True)

      Remove a node tree from the current blendfile

      :arg tree: Node tree to remove
      :type tree: :class:`NodeTree`, (never None)
      :arg do_unlink: Unlink all usages of this node tree before deleting it
      :type do_unlink: boolean, (optional)
      :arg do_id_user: Decrement user counter of all datablocks used by this node tree
      :type do_id_user: boolean, (optional)
      :arg do_ui_user: Make sure interface does not reference this node tree
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

   * :class:`BlendData.node_groups`

