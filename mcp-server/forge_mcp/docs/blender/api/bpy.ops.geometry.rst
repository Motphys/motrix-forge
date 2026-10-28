Geometry Operators
==================

.. module:: bpy.ops.geometry

.. function:: attribute_add(*, name="", domain='POINT', data_type='FLOAT')

   Add attribute to geometry

   :arg name: Name, Name of new attribute
   :type name: string, (optional, never None)
   :arg domain: Domain, Type of element that attribute is stored on
   :type domain: enum in :ref:`rna_enum_attribute_domain_items`, (optional)
   :arg data_type: Data Type, Type of data stored in attribute
   :type data_type: enum in :ref:`rna_enum_attribute_type_items`, (optional)

.. function:: attribute_convert(*, mode='GENERIC', domain='POINT', data_type='FLOAT')

   Change how the attribute is stored

   :arg mode: Mode
   :type mode: enum in [``'GENERIC'``, ``'VERTEX_GROUP'``], (optional)
   :arg domain: Domain, Which geometry element to move the attribute to
   :type domain: enum in :ref:`rna_enum_attribute_domain_items`, (optional)
   :arg data_type: Data Type
   :type data_type: enum in :ref:`rna_enum_attribute_type_items`, (optional)

.. function:: attribute_remove()

   Remove attribute from geometry

.. function:: color_attribute_add(*, name="", domain='POINT', data_type='FLOAT_COLOR', color=(0.0, 0.0, 0.0, 1.0))

   Add color attribute to geometry

   :arg name: Name, Name of new color attribute
   :type name: string, (optional, never None)
   :arg domain: Domain, Type of element that attribute is stored on
   :type domain: enum in :ref:`rna_enum_color_attribute_domain_items`, (optional)
   :arg data_type: Data Type, Type of data stored in attribute
   :type data_type: enum in :ref:`rna_enum_color_attribute_type_items`, (optional)
   :arg color: Color, Default fill color
   :type color: float array of 4 items in [0, inf], (optional)

.. function:: color_attribute_convert(*, domain='POINT', data_type='FLOAT_COLOR')

   Change how the color attribute is stored

   :arg domain: Domain, Type of element that attribute is stored on
   :type domain: enum in :ref:`rna_enum_color_attribute_domain_items`, (optional)
   :arg data_type: Data Type, Type of data stored in attribute
   :type data_type: enum in :ref:`rna_enum_color_attribute_type_items`, (optional)

.. function:: color_attribute_duplicate()

   Duplicate color attribute

.. function:: color_attribute_remove()

   Remove color attribute from geometry

.. function:: color_attribute_render_set(*, name="Color")

   Set default color attribute used for rendering

   :arg name: Name, Name of color attribute
   :type name: string, (optional, never None)

.. function:: execute_node_group(*, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="", name="", session_uid=0, mouse_position=(0, 0), region_size=(0, 0), cursor_position=(0.0, 0.0, 0.0), cursor_rotation=(0.0, 0.0, 0.0, 0.0), viewport_projection_matrix=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), viewport_view_matrix=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), viewport_is_perspective=False)

   Execute a node group on geometry

   :arg asset_library_type: Asset Library Type
   :type asset_library_type: enum in :ref:`rna_enum_asset_library_type_items`, (optional)
   :arg asset_library_identifier: Asset Library Identifier
   :type asset_library_identifier: string, (optional, never None)
   :arg relative_asset_identifier: Relative Asset Identifier
   :type relative_asset_identifier: string, (optional, never None)
   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg mouse_position: Mouse Position, Mouse coordinates in region space
   :type mouse_position: int array of 2 items in [-inf, inf], (optional)
   :arg region_size: Region Size
   :type region_size: int array of 2 items in [0, inf], (optional)
   :arg cursor_position: 3D Cursor Position
   :type cursor_position: float array of 3 items in [-inf, inf], (optional)
   :arg cursor_rotation: 3D Cursor Rotation
   :type cursor_rotation: float array of 4 items in [-inf, inf], (optional)
   :arg viewport_projection_matrix: Viewport Projection Transform
   :type viewport_projection_matrix: float array of 16 items in [-inf, inf], (optional)
   :arg viewport_view_matrix: Viewport View Transform
   :type viewport_view_matrix: float array of 16 items in [-inf, inf], (optional)
   :arg viewport_is_perspective: Viewport Is Perspective
   :type viewport_is_perspective: boolean, (optional)

.. function:: geometry_randomization(*, value=False)

   Toggle geometry randomization for debugging purposes

   :arg value: Value, Randomize the order of geometry elements (e.g. vertices or edges) after some operations where there are no guarantees about the order. This avoids accidentally depending on something that may change in the future
   :type value: boolean, (optional)

