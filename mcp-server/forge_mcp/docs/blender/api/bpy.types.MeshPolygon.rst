MeshPolygon(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MeshPolygon(bpy_struct)

   Polygon in a Mesh data-block

   .. data:: area

      Read only area of this face

      :type: float in [0, inf], default 0.0, (readonly)

   .. data:: center

      Center of this face

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: hide

      :type: boolean, default False

   .. data:: index

      Index of this face

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: loop_start

      Index of the first loop of this face

      :type: int in [0, inf], default 0

   .. data:: loop_total

      Number of loops used by this face

      :type: int in [0, inf], default 0, (readonly)

   .. attribute:: material_index

      Material slot index of this face

      :type: int in [0, inf], default 0

   .. data:: normal

      Local space unit length normal vector for this face

      :type: :class:`mathutils.Vector` of 3 items in [-1, 1], default (0.0, 0.0, 0.0), (readonly)

   .. attribute:: select

      :type: boolean, default False

   .. attribute:: use_freestyle_mark

      Face mark for Freestyle line rendering

      :type: boolean, default False

   .. attribute:: use_smooth

      :type: boolean, default False

   .. attribute:: vertices

      Vertex indices

      :type: int array of 3 items in [0, inf], default (0, 0, 0)

   .. data:: edge_keys


      (readonly)

   .. data:: loop_indices


      (readonly)

   .. method:: flip()

      Invert winding of this face (flip its normal)


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

   * :class:`Mesh.polygons`

