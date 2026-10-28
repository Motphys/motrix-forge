PropertyGroup(bpy_struct)
=========================

.. currentmodule:: bpy.types


Custom Properties
+++++++++++++++++

PropertyGroups are the base class for dynamically defined sets of properties.

They can be used to extend existing Blender data with your own types which can
be animated, accessed from the user interface and from Python.

.. note::

   The values assigned to Blender data are saved to disk but the class
   definitions are not, this means whenever you load Blender the class needs
   to be registered too.

   This is best done by creating an add-on which loads on startup and registers
   your properties.

.. note::

   PropertyGroups must be registered before assigning them to Blender data.

.. seealso::

   Property types used in class declarations are all in :mod:`bpy.props`

.. literalinclude:: ..\examples\bpy.types.PropertyGroup.py
   :lines: 27-

base class --- :class:`bpy_struct`

subclasses --- 
:class:`AssetHandle`, :class:`OperatorFileListElement`, :class:`OperatorMousePath`, :class:`OperatorStrokeElement`, :class:`SelectedUvElement`

.. class:: PropertyGroup(bpy_struct)

   Group of ID properties

   .. attribute:: name

      Unique name used in the code and scripting

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

   * :class:`CollectionExport.export_properties`
   * :class:`PropertyGroupItem.collection`
   * :class:`PropertyGroupItem.group`
   * :class:`PropertyGroupItem.idp_array`

