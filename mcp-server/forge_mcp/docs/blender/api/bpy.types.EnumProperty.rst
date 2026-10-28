EnumProperty(Property)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Property`

.. class:: EnumProperty(Property)

   RNA enumeration property definition, to choose from a number of predefined options

   .. data:: default

      Default value for this enum

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``, (readonly)

   .. data:: default_flag

      Default value for this enum

      :type: enum set in {``'DEFAULT'``}, default set(), (readonly)

   .. data:: enum_items

      Possible values for the property

      :type: :class:`bpy_prop_collection` of :class:`EnumPropertyItem`, (readonly)

   .. data:: enum_items_static

      Possible values for the property (never calls optional dynamic generation of those)

      :type: :class:`bpy_prop_collection` of :class:`EnumPropertyItem`, (readonly)

   .. data:: enum_items_static_ui

      Possible values for the property (never calls optional dynamic generation of those). Includes UI elements (separators and section headings).

      :type: :class:`bpy_prop_collection` of :class:`EnumPropertyItem`, (readonly)

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
   * :class:`Property.name`
   * :class:`Property.identifier`
   * :class:`Property.description`
   * :class:`Property.translation_context`
   * :class:`Property.type`
   * :class:`Property.subtype`
   * :class:`Property.srna`
   * :class:`Property.unit`
   * :class:`Property.icon`
   * :class:`Property.is_readonly`
   * :class:`Property.is_animatable`
   * :class:`Property.is_overridable`
   * :class:`Property.is_required`
   * :class:`Property.is_argument_optional`
   * :class:`Property.is_never_none`
   * :class:`Property.is_hidden`
   * :class:`Property.is_skip_save`
   * :class:`Property.is_skip_preset`
   * :class:`Property.is_output`
   * :class:`Property.is_registered`
   * :class:`Property.is_registered_optional`
   * :class:`Property.is_runtime`
   * :class:`Property.is_enum_flag`
   * :class:`Property.is_library_editable`
   * :class:`Property.is_path_output`
   * :class:`Property.is_path_supports_blend_relative`
   * :class:`Property.is_path_supports_templates`
   * :class:`Property.tags`

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
   * :class:`Property.bl_rna_get_subclass`
   * :class:`Property.bl_rna_get_subclass_py`

