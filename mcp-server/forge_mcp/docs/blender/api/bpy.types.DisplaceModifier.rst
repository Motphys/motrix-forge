DisplaceModifier(Modifier)
==========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: DisplaceModifier(Modifier)

   Displacement modifier

   .. attribute:: direction

      * ``X``
        X -- Use the texture's intensity value to displace in the X direction.
      * ``Y``
        Y -- Use the texture's intensity value to displace in the Y direction.
      * ``Z``
        Z -- Use the texture's intensity value to displace in the Z direction.
      * ``NORMAL``
        Normal -- Use the texture's intensity value to displace along the vertex normal.
      * ``CUSTOM_NORMAL``
        Custom Normal -- Use the texture's intensity value to displace along the (averaged) custom normal (falls back to vertex).
      * ``RGB_TO_XYZ``
        RGB to XYZ -- Use the texture's RGB values to displace the mesh in the XYZ direction.

      :type: enum in [``'X'``, ``'Y'``, ``'Z'``, ``'NORMAL'``, ``'CUSTOM_NORMAL'``, ``'RGB_TO_XYZ'``], default ``'NORMAL'``

   .. attribute:: invert_vertex_group

      Invert vertex group influence

      :type: boolean, default False

   .. attribute:: mid_level

      Material value that gives no displacement

      :type: float in [-inf, inf], default 0.5

   .. attribute:: space

      * ``LOCAL``
        Local -- Direction is defined in local coordinates.
      * ``GLOBAL``
        Global -- Direction is defined in global coordinates.

      :type: enum in [``'LOCAL'``, ``'GLOBAL'``], default ``'LOCAL'``

   .. attribute:: strength

      Amount to displace geometry

      :type: float in [-inf, inf], default 1.0

   .. attribute:: texture

      :type: :class:`Texture`

   .. attribute:: texture_coords

      * ``LOCAL``
        Local -- Use the local coordinate system for the texture coordinates.
      * ``GLOBAL``
        Global -- Use the global coordinate system for the texture coordinates.
      * ``OBJECT``
        Object -- Use the linked object's local coordinate system for the texture coordinates.
      * ``UV``
        UV -- Use UV coordinates for the texture coordinates.

      :type: enum in [``'LOCAL'``, ``'GLOBAL'``, ``'OBJECT'``, ``'UV'``], default ``'LOCAL'``

   .. attribute:: texture_coords_bone

      Bone to set the texture coordinates

      :type: string, default "", (never None)

   .. attribute:: texture_coords_object

      Object to set the texture coordinates

      :type: :class:`Object`

   .. attribute:: uv_layer

      UV map name

      :type: string, default "", (never None)

   .. attribute:: vertex_group

      Name of Vertex Group which determines influence of modifier per point

      :type: string, default "", (never None)

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.is_active`
   * :class:`Modifier.use_pin_to_last`
   * :class:`Modifier.is_override_data`
   * :class:`Modifier.use_apply_on_spline`
   * :class:`Modifier.execution_time`
   * :class:`Modifier.persistent_uid`

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
   * :class:`Modifier.bl_rna_get_subclass`
   * :class:`Modifier.bl_rna_get_subclass_py`

