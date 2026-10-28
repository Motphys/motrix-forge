GreasePencilTreeNode(bpy_struct)
================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`GreasePencilLayer`, :class:`GreasePencilLayerGroup`

.. class:: GreasePencilTreeNode(bpy_struct)

   Grease Pencil node in the layer tree. Either a layer or a group

   .. attribute:: channel_color

      Color of the channel in the dope sheet

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: hide

      Set tree node visibility

      :type: boolean, default False

   .. attribute:: lock

      Protect tree node from editing

      :type: boolean, default False

   .. attribute:: name

      The name of the tree node

      :type: string, default "", (never None)

   .. data:: next_node

      The layer tree node after (i.e. above) this one

      :type: :class:`GreasePencilTreeNode`, (readonly)

   .. data:: parent_group

      The parent group of this layer tree node

      :type: :class:`GreasePencilLayerGroup`, (readonly)

   .. data:: prev_node

      The layer tree node before (i.e. below) this one

      :type: :class:`GreasePencilTreeNode`, (readonly)

   .. attribute:: select

      Tree node is selected

      :type: boolean, default False

   .. attribute:: use_masks

      The visibility of drawings in this tree node is affected by the layers in the masks list

      :type: boolean, default False

   .. attribute:: use_onion_skinning

      Display onion skins before and after the current frame

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

   * :class:`GreasePencilTreeNode.next_node`
   * :class:`GreasePencilTreeNode.prev_node`

