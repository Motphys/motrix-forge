MeshUVLoopLayer(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshUVLoopLayer(bpy_struct)


   .. attribute:: active

      Set the map as active for display and editing

      :type: boolean, default False

   .. attribute:: active_clone

      Set the map as active for cloning

      :type: boolean, default False

   .. attribute:: active_render

      Set the UV map as active for rendering

      :type: boolean, default False

   .. data:: data

      Deprecated, use 'uv', 'vertex_select', 'edge_select' or 'pin' properties instead

      :type: :class:`bpy_prop_collection` of :class:`MeshUVLoop`, (readonly)

   .. data:: edge_selection

      Selection state of the edge in the UV editor

      :type: :class:`bpy_prop_collection` of :class:`BoolAttributeValue`, (readonly)

   .. attribute:: name

      Name of UV map

      :type: string, default "", (never None)

   .. data:: pin

      UV pinned state in the UV editor

      :type: :class:`bpy_prop_collection` of :class:`BoolAttributeValue`, (readonly)

   .. data:: uv

      UV coordinates on face corners

      :type: :class:`bpy_prop_collection` of :class:`Float2AttributeValue`, (readonly)

   .. data:: vertex_selection

      Selection state of the face corner the UV editor

      :type: :class:`bpy_prop_collection` of :class:`BoolAttributeValue`, (readonly)

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

   * :class:`Mesh.uv_layer_clone`
   * :class:`Mesh.uv_layer_stencil`
   * :class:`Mesh.uv_layers`
   * :class:`UVLoopLayers.active`
   * :class:`UVLoopLayers.new`
   * :class:`UVLoopLayers.remove`

