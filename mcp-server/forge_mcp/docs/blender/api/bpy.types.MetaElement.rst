MetaElement(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MetaElement(bpy_struct)

   Blobby element in a metaball data-block

   .. attribute:: co

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: hide

      Hide element

      :type: boolean, default False

   .. attribute:: radius

      :type: float in [0, inf], default 0.0

   .. attribute:: rotation

      Normalized quaternion rotation

      :type: :class:`mathutils.Quaternion` rotation of 4 items in [-inf, inf], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: select

      Select element

      :type: boolean, default False

   .. attribute:: size_x

      Size of element, use of components depends on element type

      :type: float in [0, 20], default 0.0

   .. attribute:: size_y

      Size of element, use of components depends on element type

      :type: float in [0, 20], default 0.0

   .. attribute:: size_z

      Size of element, use of components depends on element type

      :type: float in [0, 20], default 0.0

   .. attribute:: stiffness

      Stiffness defines how much of the element to fill

      :type: float in [0, 10], default 0.0

   .. attribute:: type

      Metaball type

      :type: enum in :ref:`rna_enum_metaelem_type_items`, default ``'BALL'``

   .. attribute:: use_negative

      Set metaball as negative one

      :type: boolean, default False

   .. attribute:: use_scale_stiffness

      Scale stiffness instead of radius

      :type: boolean, default False

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

   * :class:`MetaBall.elements`
   * :class:`MetaBallElements.active`
   * :class:`MetaBallElements.new`
   * :class:`MetaBallElements.remove`

