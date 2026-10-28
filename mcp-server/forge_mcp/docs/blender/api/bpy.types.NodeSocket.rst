NodeSocket(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`NodeSocketStandard`

.. class:: NodeSocket(bpy_struct)

   Input or output socket of a node

   .. attribute:: bl_idname

      :type: string, default "", (never None)

   .. attribute:: bl_label

      Label to display for the socket type in the UI

      :type: string, default "", (never None)

   .. attribute:: bl_subtype_label

      Label to display for the socket subtype in the UI

      :type: string, default "", (never None)

   .. attribute:: description

      Socket tooltip

      :type: string, default "", (never None)

   .. attribute:: display_shape

      Socket shape

      :type: enum in [``'CIRCLE'``, ``'SQUARE'``, ``'DIAMOND'``, ``'CIRCLE_DOT'``, ``'SQUARE_DOT'``, ``'DIAMOND_DOT'``], default ``'CIRCLE'``

   .. attribute:: enabled

      Enable the socket

      :type: boolean, default False

   .. attribute:: hide

      Hide the socket

      :type: boolean, default False

   .. attribute:: hide_value

      Hide the socket input value

      :type: boolean, default False

   .. data:: identifier

      Unique identifier for mapping sockets

      :type: string, default "", (readonly, never None)

   .. data:: is_icon_visible

      Socket is drawn as interactive icon in the node editor

      :type: boolean, default False, (readonly)

   .. data:: is_inactive

      Socket is grayed out because it has been detected to not have any effect on the output

      :type: boolean, default False, (readonly)

   .. data:: is_linked

      True if the socket is connected

      :type: boolean, default False, (readonly)

   .. data:: is_multi_input

      True if the socket can accept multiple ordered input links

      :type: boolean, default False, (readonly)

   .. data:: is_output

      True if the socket is an output, otherwise input

      :type: boolean, default False, (readonly)

   .. data:: is_unavailable

      True if the socket is unavailable

      :type: boolean, default False, (readonly)

   .. data:: label

      Custom dynamic defined socket label

      :type: string, default "", (readonly, never None)

   .. attribute:: link_limit

      Max number of links allowed for this socket

      :type: int in [1, 4095], default 0

   .. attribute:: name

      Socket name

      :type: string, default "", (never None)

   .. data:: node

      Node owning this socket

      :type: :class:`Node`, (readonly)

   .. attribute:: pin_gizmo

      Keep gizmo visible even when the node is not selected

      :type: boolean, default False

   .. data:: select

      True if the socket is selected

      :type: boolean, default False, (readonly)

   .. attribute:: show_expanded

      Socket links are expanded in the user interface

      :type: boolean, default False

   .. attribute:: type

      Data type

      :type: enum in :ref:`rna_enum_node_socket_type_items`, default ``'VALUE'``

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

      Color of the socket icon. Used to draw sockets in places where the socket does not belong to a node, like the node interface panel. Also used to draw node sockets if draw_color is not defined.

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

   * :class:`CompositorNodeOutputFileFileSlots.new`
   * :class:`CompositorNodeOutputFileFileSlots.remove`
   * :class:`CompositorNodeOutputFileLayerSlots.new`
   * :class:`CompositorNodeOutputFileLayerSlots.remove`
   * :class:`Node.inputs`
   * :class:`Node.outputs`
   * :class:`NodeInputs.new`
   * :class:`NodeInputs.remove`
   * :class:`NodeLink.from_socket`
   * :class:`NodeLink.to_socket`
   * :class:`NodeLinks.new`
   * :class:`NodeLinks.new`
   * :class:`NodeOutputs.new`
   * :class:`NodeOutputs.remove`
   * :class:`NodeTreeInterfaceSocket.from_socket`
   * :class:`NodeTreeInterfaceSocket.init_socket`
   * :class:`NodeTreeInterfaceSocketBool.from_socket`
   * :class:`NodeTreeInterfaceSocketBool.init_socket`
   * :class:`NodeTreeInterfaceSocketBundle.from_socket`
   * :class:`NodeTreeInterfaceSocketBundle.init_socket`
   * :class:`NodeTreeInterfaceSocketClosure.from_socket`
   * :class:`NodeTreeInterfaceSocketClosure.init_socket`
   * :class:`NodeTreeInterfaceSocketCollection.from_socket`
   * :class:`NodeTreeInterfaceSocketCollection.init_socket`
   * :class:`NodeTreeInterfaceSocketColor.from_socket`
   * :class:`NodeTreeInterfaceSocketColor.init_socket`
   * :class:`NodeTreeInterfaceSocketFloat.from_socket`
   * :class:`NodeTreeInterfaceSocketFloat.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatAngle.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatAngle.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatColorTemperature.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatColorTemperature.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatDistance.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatDistance.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatFactor.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatFactor.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatFrequency.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatFrequency.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatPercentage.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatPercentage.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatTime.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatTime.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatTimeAbsolute.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatTimeAbsolute.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatUnsigned.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatUnsigned.init_socket`
   * :class:`NodeTreeInterfaceSocketFloatWavelength.from_socket`
   * :class:`NodeTreeInterfaceSocketFloatWavelength.init_socket`
   * :class:`NodeTreeInterfaceSocketGeometry.from_socket`
   * :class:`NodeTreeInterfaceSocketGeometry.init_socket`
   * :class:`NodeTreeInterfaceSocketImage.from_socket`
   * :class:`NodeTreeInterfaceSocketImage.init_socket`
   * :class:`NodeTreeInterfaceSocketInt.from_socket`
   * :class:`NodeTreeInterfaceSocketInt.init_socket`
   * :class:`NodeTreeInterfaceSocketIntFactor.from_socket`
   * :class:`NodeTreeInterfaceSocketIntFactor.init_socket`
   * :class:`NodeTreeInterfaceSocketIntPercentage.from_socket`
   * :class:`NodeTreeInterfaceSocketIntPercentage.init_socket`
   * :class:`NodeTreeInterfaceSocketIntUnsigned.from_socket`
   * :class:`NodeTreeInterfaceSocketIntUnsigned.init_socket`
   * :class:`NodeTreeInterfaceSocketMaterial.from_socket`
   * :class:`NodeTreeInterfaceSocketMaterial.init_socket`
   * :class:`NodeTreeInterfaceSocketMatrix.from_socket`
   * :class:`NodeTreeInterfaceSocketMatrix.init_socket`
   * :class:`NodeTreeInterfaceSocketMenu.from_socket`
   * :class:`NodeTreeInterfaceSocketMenu.init_socket`
   * :class:`NodeTreeInterfaceSocketObject.from_socket`
   * :class:`NodeTreeInterfaceSocketObject.init_socket`
   * :class:`NodeTreeInterfaceSocketRotation.from_socket`
   * :class:`NodeTreeInterfaceSocketRotation.init_socket`
   * :class:`NodeTreeInterfaceSocketShader.from_socket`
   * :class:`NodeTreeInterfaceSocketShader.init_socket`
   * :class:`NodeTreeInterfaceSocketString.from_socket`
   * :class:`NodeTreeInterfaceSocketString.init_socket`
   * :class:`NodeTreeInterfaceSocketStringFilePath.from_socket`
   * :class:`NodeTreeInterfaceSocketStringFilePath.init_socket`
   * :class:`NodeTreeInterfaceSocketTexture.from_socket`
   * :class:`NodeTreeInterfaceSocketTexture.init_socket`
   * :class:`NodeTreeInterfaceSocketVector.from_socket`
   * :class:`NodeTreeInterfaceSocketVector.init_socket`
   * :class:`NodeTreeInterfaceSocketVector2D.from_socket`
   * :class:`NodeTreeInterfaceSocketVector2D.init_socket`
   * :class:`NodeTreeInterfaceSocketVector4D.from_socket`
   * :class:`NodeTreeInterfaceSocketVector4D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration2D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration2D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration4D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorAcceleration4D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorDirection.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorDirection.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorDirection2D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorDirection2D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorDirection4D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorDirection4D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorEuler.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorEuler.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorEuler2D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorEuler2D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorEuler4D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorEuler4D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorFactor.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorFactor.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorFactor2D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorFactor2D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorFactor4D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorFactor4D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorPercentage.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorPercentage.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorPercentage2D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorPercentage2D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorPercentage4D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorPercentage4D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorTranslation.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorTranslation.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorTranslation2D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorTranslation2D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorTranslation4D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorTranslation4D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorVelocity.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorVelocity.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorVelocity2D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorVelocity2D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorVelocity4D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorVelocity4D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorXYZ.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorXYZ.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorXYZ2D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorXYZ2D.init_socket`
   * :class:`NodeTreeInterfaceSocketVectorXYZ4D.from_socket`
   * :class:`NodeTreeInterfaceSocketVectorXYZ4D.init_socket`
   * :class:`UILayout.template_node_link`
   * :class:`UILayout.template_node_view`

