Property(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`BoolProperty`, :class:`CollectionProperty`, :class:`EnumProperty`, :class:`FloatProperty`, :class:`IntProperty`, :class:`PointerProperty`, :class:`StringProperty`

.. class:: Property(bpy_struct)

   RNA property definition

   .. data:: description

      Description of the property for tooltips

      :type: string, default "", (readonly, never None)

   .. data:: icon

      Icon of the item

      :type: enum in :ref:`rna_enum_icon_items`, default ``'NONE'``, (readonly)

   .. data:: identifier

      Unique name used in the code and scripting

      :type: string, default "", (readonly, never None)

   .. data:: is_animatable

      Property is animatable through RNA

      :type: boolean, default False, (readonly)

   .. data:: is_argument_optional

      True when the property is optional in a Python function implementing an RNA function

      :type: boolean, default False, (readonly)

   .. data:: is_enum_flag

      True when multiple enums

      :type: boolean, default False, (readonly)

   .. data:: is_hidden

      True when the property is hidden

      :type: boolean, default False, (readonly)

   .. data:: is_library_editable

      Property is editable from linked instances (changes not saved)

      :type: boolean, default False, (readonly)

   .. data:: is_never_none

      True when this value can't be set to None

      :type: boolean, default False, (readonly)

   .. data:: is_output

      True when this property is an output value from an RNA function

      :type: boolean, default False, (readonly)

   .. data:: is_overridable

      Property is overridable through RNA

      :type: boolean, default False, (readonly)

   .. data:: is_path_output

      Property is a filename, filepath or directory output

      :type: boolean, default False, (readonly)

   .. data:: is_path_supports_blend_relative

      Property is a path which supports the "//" prefix, signifying the location as relative to the ".blend" file's directory

      :type: boolean, default False, (readonly)

   .. data:: is_path_supports_templates

      Property is a path which supports the "{variable_name}" variable expression syntax, which substitutes the value of the referenced variable in place of the expression

      :type: boolean, default False, (readonly)

   .. data:: is_readonly

      Property is editable through RNA

      :type: boolean, default False, (readonly)

   .. data:: is_registered

      Property is registered as part of type registration

      :type: boolean, default False, (readonly)

   .. data:: is_registered_optional

      Property is optionally registered as part of type registration

      :type: boolean, default False, (readonly)

   .. data:: is_required

      False when this property is an optional argument in an RNA function

      :type: boolean, default False, (readonly)

   .. data:: is_runtime

      Property has been dynamically created at runtime

      :type: boolean, default False, (readonly)

   .. data:: is_skip_preset

      True when the property is not saved in presets

      :type: boolean, default False, (readonly)

   .. data:: is_skip_save

      True when the property uses ghost values

      :type: boolean, default False, (readonly)

   .. data:: name

      Human readable name

      :type: string, default "", (readonly, never None)

   .. data:: srna

      Struct definition used for properties assigned to this item

      :type: :class:`Struct`, (readonly)

   .. data:: subtype

      Semantic interpretation of the property

      :type: enum in :ref:`rna_enum_property_subtype_items`, default ``'NONE'``, (readonly)

   .. data:: tags

      Subset of tags (defined in parent struct) that are set for this property

      :type: enum set in {}, default set(), (readonly)

   .. data:: translation_context

      Translation context of the property's name

      :type: string, default "", (readonly, never None)

   .. data:: type

      Data type of the property

      :type: enum in :ref:`rna_enum_property_type_items`, default ``'BOOLEAN'``, (readonly)

   .. data:: unit

      Type of units for this property

      :type: enum in :ref:`rna_enum_property_unit_items`, default ``'NONE'``, (readonly)

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

   * :mod:`bpy.context.texture_user_property`
   * :class:`Function.parameters`
   * :class:`Struct.properties`

