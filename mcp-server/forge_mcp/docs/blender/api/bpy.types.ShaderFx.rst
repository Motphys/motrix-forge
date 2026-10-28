ShaderFx(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`ShaderFxBlur`, :class:`ShaderFxColorize`, :class:`ShaderFxFlip`, :class:`ShaderFxGlow`, :class:`ShaderFxPixel`, :class:`ShaderFxRim`, :class:`ShaderFxShadow`, :class:`ShaderFxSwirl`, :class:`ShaderFxWave`

.. class:: ShaderFx(bpy_struct)

   Effect affecting the Grease Pencil object

   .. attribute:: name

      Effect name

      :type: string, default "", (never None)

   .. attribute:: show_expanded

      Set effect expansion in the user interface

      :type: boolean, default False

   .. attribute:: show_in_editmode

      Display effect in Edit mode

      :type: boolean, default False

   .. attribute:: show_render

      Use effect during render

      :type: boolean, default False

   .. attribute:: show_viewport

      Display effect in viewport

      :type: boolean, default False

   .. data:: type

      :type: enum in :ref:`rna_enum_object_shaderfx_type_items`, default ``'FX_BLUR'``, (readonly)

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

   * :class:`Object.shader_effects`
   * :class:`ObjectShaderFx.new`
   * :class:`ObjectShaderFx.remove`

