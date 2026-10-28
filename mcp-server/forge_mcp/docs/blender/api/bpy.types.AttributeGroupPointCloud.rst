AttributeGroupPointCloud(bpy_struct)
====================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: AttributeGroupPointCloud(bpy_struct)

   Group of geometry attributes

   .. attribute:: active

      Active attribute

      :type: :class:`Attribute`

   .. attribute:: active_index

      Active attribute index or -1 when none are active

      :type: int in [-1, inf], default 0

   .. method:: new(name, type, domain)

      Add attribute to geometry

      :arg name: Name, Name of geometry attribute
      :type name: string, (never None)
      :arg type: Type, Attribute type
      :type type: enum in :ref:`rna_enum_attribute_type_items`
      :arg domain: Domain, Type of element that attribute is stored on
      :type domain: enum in :ref:`rna_enum_attribute_domain_items`
      :return: New geometry attribute
      :rtype: :class:`Attribute`

   .. method:: remove(attribute)

      Remove attribute from geometry

      :arg attribute: Geometry Attribute
      :type attribute: :class:`Attribute`, (never None)

   .. method:: domain_size(domain)

      Get the size of a given domain

      :arg domain: Domain, Type of element that attribute is stored on
      :type domain: enum in :ref:`rna_enum_attribute_domain_items`
      :return: Size, Size of the domain
      :rtype: int in [0, inf]

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

   * :class:`PointCloud.attributes`
   * :class:`PointCloud.color_attributes`

