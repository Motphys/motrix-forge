NodeTreeInterfaceSocket(NodeTreeInterfaceItem)
==============================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`NodeTreeInterfaceItem`

subclasses --- 
:class:`NodeTreeInterfaceSocketBool`, :class:`NodeTreeInterfaceSocketBundle`, :class:`NodeTreeInterfaceSocketClosure`, :class:`NodeTreeInterfaceSocketCollection`, :class:`NodeTreeInterfaceSocketColor`, :class:`NodeTreeInterfaceSocketFloat`, :class:`NodeTreeInterfaceSocketFloatAngle`, :class:`NodeTreeInterfaceSocketFloatColorTemperature`, :class:`NodeTreeInterfaceSocketFloatDistance`, :class:`NodeTreeInterfaceSocketFloatFactor`, :class:`NodeTreeInterfaceSocketFloatFrequency`, :class:`NodeTreeInterfaceSocketFloatPercentage`, :class:`NodeTreeInterfaceSocketFloatTime`, :class:`NodeTreeInterfaceSocketFloatTimeAbsolute`, :class:`NodeTreeInterfaceSocketFloatUnsigned`, :class:`NodeTreeInterfaceSocketFloatWavelength`, :class:`NodeTreeInterfaceSocketGeometry`, :class:`NodeTreeInterfaceSocketImage`, :class:`NodeTreeInterfaceSocketInt`, :class:`NodeTreeInterfaceSocketIntFactor`, :class:`NodeTreeInterfaceSocketIntPercentage`, :class:`NodeTreeInterfaceSocketIntUnsigned`, :class:`NodeTreeInterfaceSocketMaterial`, :class:`NodeTreeInterfaceSocketMatrix`, :class:`NodeTreeInterfaceSocketMenu`, :class:`NodeTreeInterfaceSocketObject`, :class:`NodeTreeInterfaceSocketRotation`, :class:`NodeTreeInterfaceSocketShader`, :class:`NodeTreeInterfaceSocketString`, :class:`NodeTreeInterfaceSocketStringFilePath`, :class:`NodeTreeInterfaceSocketTexture`, :class:`NodeTreeInterfaceSocketVector`, :class:`NodeTreeInterfaceSocketVector2D`, :class:`NodeTreeInterfaceSocketVector4D`, :class:`NodeTreeInterfaceSocketVectorAcceleration`, :class:`NodeTreeInterfaceSocketVectorAcceleration2D`, :class:`NodeTreeInterfaceSocketVectorAcceleration4D`, :class:`NodeTreeInterfaceSocketVectorDirection`, :class:`NodeTreeInterfaceSocketVectorDirection2D`, :class:`NodeTreeInterfaceSocketVectorDirection4D`, :class:`NodeTreeInterfaceSocketVectorEuler`, :class:`NodeTreeInterfaceSocketVectorEuler2D`, :class:`NodeTreeInterfaceSocketVectorEuler4D`, :class:`NodeTreeInterfaceSocketVectorFactor`, :class:`NodeTreeInterfaceSocketVectorFactor2D`, :class:`NodeTreeInterfaceSocketVectorFactor4D`, :class:`NodeTreeInterfaceSocketVectorPercentage`, :class:`NodeTreeInterfaceSocketVectorPercentage2D`, :class:`NodeTreeInterfaceSocketVectorPercentage4D`, :class:`NodeTreeInterfaceSocketVectorTranslation`, :class:`NodeTreeInterfaceSocketVectorTranslation2D`, :class:`NodeTreeInterfaceSocketVectorTranslation4D`, :class:`NodeTreeInterfaceSocketVectorVelocity`, :class:`NodeTreeInterfaceSocketVectorVelocity2D`, :class:`NodeTreeInterfaceSocketVectorVelocity4D`, :class:`NodeTreeInterfaceSocketVectorXYZ`, :class:`NodeTreeInterfaceSocketVectorXYZ2D`, :class:`NodeTreeInterfaceSocketVectorXYZ4D`

.. class:: NodeTreeInterfaceSocket(NodeTreeInterfaceItem)

   Declaration of a node socket

   .. attribute:: attribute_domain

      Attribute domain used by the geometry nodes modifier to create an attribute output

      :type: enum in :ref:`rna_enum_attribute_domain_items`, default ``'POINT'``

   .. attribute:: bl_socket_idname

      Name of the socket type

      :type: string, default "", (never None)

   .. attribute:: default_attribute_name

      The attribute name used by default when the node group is used by a geometry nodes modifier

      :type: string, default "", (never None)

   .. attribute:: default_input

      Input to use when the socket is unconnected. Requires "Hide Value".

      * ``VALUE``
        Default Value -- The node socket's default value.
      * ``INDEX``
        Index -- The index from the context.
      * ``ID_OR_INDEX``
        ID or Index -- The "id" attribute if available, otherwise the index.
      * ``NORMAL``
        Normal -- The geometry's normal direction.
      * ``POSITION``
        Position -- The position from the context.
      * ``INSTANCE_TRANSFORM``
        Instance Transform -- Transformation of each instance from the geometry context.
      * ``HANDLE_LEFT``
        Left Handle -- The left Bezier control point handle from the context.
      * ``HANDLE_RIGHT``
        Right Handle -- The right Bezier control point handle from the context.

      :type: enum in [``'VALUE'``, ``'INDEX'``, ``'ID_OR_INDEX'``, ``'NORMAL'``, ``'POSITION'``, ``'INSTANCE_TRANSFORM'``, ``'HANDLE_LEFT'``, ``'HANDLE_RIGHT'``], default ``'VALUE'``

   .. attribute:: description

      Socket description

      :type: string, default "", (never None)

   .. attribute:: force_non_field

      Only allow single value inputs rather than field.
      Deprecated. Will be remove in 5.0.

      :type: boolean, default False

   .. attribute:: hide_in_modifier

      Don't show the input value in the geometry nodes modifier interface

      :type: boolean, default False

   .. attribute:: hide_value

      Hide the socket input value even when the socket is not connected

      :type: boolean, default False

   .. data:: identifier

      Unique identifier for mapping sockets

      :type: string, default "", (readonly, never None)

   .. data:: in_out

      Input or output socket type

      * ``INPUT``
        Input -- Generate a input node socket.
      * ``OUTPUT``
        Output -- Generate a output node socket.

      :type: enum in [``'INPUT'``, ``'OUTPUT'``], default ``'INPUT'``, (readonly)

   .. attribute:: is_inspect_output

      Take link out of node group to connect to root tree output node

      :type: boolean, default False

   .. attribute:: is_panel_toggle

      This socket is meant to be used as the toggle in its panel header

      :type: boolean, default False

   .. attribute:: layer_selection_field

      Take Grease Pencil Layer or Layer Group as selection field

      :type: boolean, default False

   .. attribute:: menu_expanded

      Draw the menu socket as an expanded drop-down menu

      :type: boolean, default False

   .. attribute:: name

      Socket name

      :type: string, default "", (never None)

   .. attribute:: socket_type

      Type of the socket generated by this interface item

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``

   .. attribute:: structure_type

      What kind of higher order types are expected to flow through this socket

      * ``AUTO``
        Auto -- Automatically detect a good structure type based on how the socket is used.
      * ``SINGLE``
        Single -- Socket expects a single value.
      * ``DYNAMIC``
        Dynamic -- Socket can work with different kinds of structures.
      * ``FIELD``
        Field -- Socket expects a field.
      * ``GRID``
        Grid -- Socket expects a grid.

      :type: enum in [``'AUTO'``, ``'SINGLE'``, ``'DYNAMIC'``, ``'FIELD'``, ``'GRID'``], default ``'AUTO'``

   .. method:: draw(context, layout)

      Draw properties of the socket interface

      :type context: :class:`Context`, (never None)
      :arg layout: Layout, Layout in the UI
      :type layout: :class:`UILayout`, (never None)

   .. method:: init_socket(node, socket, data_path)

      Initialize a node socket instance

      :arg node: Node, Node of the socket to initialize
      :type node: :class:`Node`, (never None)
      :arg socket: Socket, Socket to initialize
      :type socket: :class:`NodeSocket`, (never None)
      :arg data_path: Data Path, Path to specialized socket data
      :type data_path: string, (never None)

   .. method:: from_socket(node, socket)

      Setup template parameters from an existing socket

      :arg node: Node, Node of the original socket
      :type node: :class:`Node`, (never None)
      :arg socket: Socket, Original socket
      :type socket: :class:`NodeSocket`, (never None)

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
   * :class:`NodeTreeInterfaceItem.item_type`
   * :class:`NodeTreeInterfaceItem.parent`
   * :class:`NodeTreeInterfaceItem.position`
   * :class:`NodeTreeInterfaceItem.index`

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
   * :class:`NodeTreeInterfaceItem.bl_rna_get_subclass`
   * :class:`NodeTreeInterfaceItem.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :class:`NodeTreeInterface.new_socket`

