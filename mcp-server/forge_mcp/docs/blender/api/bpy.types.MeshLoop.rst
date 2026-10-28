MeshLoop(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshLoop(bpy_struct)

   Loop in a Mesh data-block

   .. data:: bitangent

      Bitangent vector of this vertex for this face (must be computed beforehand using calc_tangents, use it only if really needed, slower access than bitangent_sign)

      :type: :class:`mathutils.Vector` of 3 items in [-1, 1], default (0.0, 0.0, 0.0), (readonly)

   .. data:: bitangent_sign

      Sign of the bitangent vector of this vertex for this face (must be computed beforehand using calc_tangents, bitangent = bitangent_sign * cross(normal, tangent))

      :type: float in [-1, 1], default 0.0, (readonly)

   .. attribute:: edge_index

      Edge index

      :type: int in [0, inf], default 0

   .. data:: index

      Index of this loop

      :type: int in [0, inf], default 0, (readonly)

   .. data:: normal

      The normal direction of the face corner, taking into account sharp faces, sharp edges, and custom normal data

      :type: :class:`mathutils.Vector` of 3 items in [-1, 1], default (0.0, 0.0, 0.0), (readonly)

   .. data:: tangent

      Local space unit length tangent vector of this vertex for this face (must be computed beforehand using calc_tangents)

      :type: :class:`mathutils.Vector` of 3 items in [-1, 1], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: vertex_index

      Vertex index

      :type: int in [0, inf], default 0

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

   * :class:`Mesh.loops`

