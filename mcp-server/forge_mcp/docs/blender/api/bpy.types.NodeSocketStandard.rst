NodeSocketStandard(NodeSocket)
==============================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`NodeSocket`

subclasses --- 
:class:`NodeSocketBool`, :class:`NodeSocketBundle`, :class:`NodeSocketClosure`, :class:`NodeSocketCollection`, :class:`NodeSocketColor`, :class:`NodeSocketFloat`, :class:`NodeSocketFloatAngle`, :class:`NodeSocketFloatColorTemperature`, :class:`NodeSocketFloatDistance`, :class:`NodeSocketFloatFactor`, :class:`NodeSocketFloatFrequency`, :class:`NodeSocketFloatPercentage`, :class:`NodeSocketFloatTime`, :class:`NodeSocketFloatTimeAbsolute`, :class:`NodeSocketFloatUnsigned`, :class:`NodeSocketFloatWavelength`, :class:`NodeSocketGeometry`, :class:`NodeSocketImage`, :class:`NodeSocketInt`, :class:`NodeSocketIntFactor`, :class:`NodeSocketIntPercentage`, :class:`NodeSocketIntUnsigned`, :class:`NodeSocketMaterial`, :class:`NodeSocketMatrix`, :class:`NodeSocketMenu`, :class:`NodeSocketObject`, :class:`NodeSocketRotation`, :class:`NodeSocketShader`, :class:`NodeSocketString`, :class:`NodeSocketStringFilePath`, :class:`NodeSocketTexture`, :class:`NodeSocketVector`, :class:`NodeSocketVector2D`, :class:`NodeSocketVector4D`, :class:`NodeSocketVectorAcceleration`, :class:`NodeSocketVectorAcceleration2D`, :class:`NodeSocketVectorAcceleration4D`, :class:`NodeSocketVectorDirection`, :class:`NodeSocketVectorDirection2D`, :class:`NodeSocketVectorDirection4D`, :class:`NodeSocketVectorEuler`, :class:`NodeSocketVectorEuler2D`, :class:`NodeSocketVectorEuler4D`, :class:`NodeSocketVectorFactor`, :class:`NodeSocketVectorFactor2D`, :class:`NodeSocketVectorFactor4D`, :class:`NodeSocketVectorPercentage`, :class:`NodeSocketVectorPercentage2D`, :class:`NodeSocketVectorPercentage4D`, :class:`NodeSocketVectorTranslation`, :class:`NodeSocketVectorTranslation2D`, :class:`NodeSocketVectorTranslation4D`, :class:`NodeSocketVectorVelocity`, :class:`NodeSocketVectorVelocity2D`, :class:`NodeSocketVectorVelocity4D`, :class:`NodeSocketVectorXYZ`, :class:`NodeSocketVectorXYZ2D`, :class:`NodeSocketVectorXYZ4D`, :class:`NodeSocketVirtual`

.. class:: NodeSocketStandard(NodeSocket)


   .. data:: links

      List of node links from or to this socket.
      
      :type: :class:`NodeLinks`
      
      .. note:: Takes ``O(len(nodetree.links))`` time.

      (readonly)

   .. method:: draw(context, layout, node, text)

      Draw socket

      :type context: :class:`Context`, (never None)
      :arg layout: Layout, Layout in the UI
      :type layout: :class:`UILayout`, (never None)
      :arg node: Node, Node the socket belongs to
      :type node: :class:`Node`, (never None)
      :arg text: Text, Text label to draw alongside properties
      :type text: string, (never None)

   .. method:: draw_color(context, node)

      Color of the socket icon

      :type context: :class:`Context`, (never None)
      :arg node: Node, Node the socket belongs to
      :type node: :class:`Node`, (never None)
      :return: Color
      :rtype: float array of 4 items in [0, 1]

   .. classmethod:: draw_color_simple()

      Color of the socket icon

      :return: Color
      :rtype: float array of 4 items in [0, 1]

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
   * :class:`NodeSocket.name`
   * :class:`NodeSocket.label`
   * :class:`NodeSocket.identifier`
   * :class:`NodeSocket.description`
   * :class:`NodeSocket.is_output`
   * :class:`NodeSocket.select`
   * :class:`NodeSocket.hide`
   * :class:`NodeSocket.enabled`
   * :class:`NodeSocket.link_limit`
   * :class:`NodeSocket.is_linked`
   * :class:`NodeSocket.is_unavailable`
   * :class:`NodeSocket.is_multi_input`
   * :class:`NodeSocket.show_expanded`
   * :class:`NodeSocket.is_inactive`
   * :class:`NodeSocket.is_icon_visible`
   * :class:`NodeSocket.hide_value`
   * :class:`NodeSocket.pin_gizmo`
   * :class:`NodeSocket.node`
   * :class:`NodeSocket.type`
   * :class:`NodeSocket.display_shape`
   * :class:`NodeSocket.bl_idname`
   * :class:`NodeSocket.bl_label`
   * :class:`NodeSocket.bl_subtype_label`
   * :class:`NodeSocket.links`

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
   * :class:`NodeSocket.draw`
   * :class:`NodeSocket.draw_color`
   * :class:`NodeSocket.draw_color_simple`
   * :class:`NodeSocket.bl_rna_get_subclass`
   * :class:`NodeSocket.bl_rna_get_subclass_py`

