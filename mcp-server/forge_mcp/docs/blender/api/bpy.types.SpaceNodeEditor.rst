SpaceNodeEditor(Space)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceNodeEditor(Space)

   Node editor space data

   .. attribute:: backdrop_channels

      Channels of the image to draw

      * ``COLOR_ALPHA``
        Color & Alpha -- Display image with RGB colors and alpha transparency.
      * ``COLOR``
        Color -- Display image with RGB colors.
      * ``ALPHA``
        Alpha -- Display alpha transparency channel.
      * ``RED``
        Red.
      * ``GREEN``
        Green.
      * ``BLUE``
        Blue.

      :type: enum in [``'COLOR_ALPHA'``, ``'COLOR'``, ``'ALPHA'``, ``'RED'``, ``'GREEN'``, ``'BLUE'``], default ``'COLOR'``

   .. attribute:: backdrop_offset

      Backdrop offset

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: backdrop_zoom

      Backdrop zoom factor

      :type: float in [0.01, inf], default 1.0

   .. attribute:: cursor_location

      Location for adding new nodes

      :type: :class:`mathutils.Vector` of 2 items in [-inf, inf], default (0.0, 0.0)

   .. data:: edit_tree

      Node tree being displayed and edited

      :type: :class:`NodeTree`, (readonly)

   .. attribute:: geometry_nodes_tool_tree

      Node group to edit as node tool

      :type: :class:`NodeTree`

   .. attribute:: geometry_nodes_type

      * ``MODIFIER``
        Modifier -- Edit node group from active object's active modifier.
      * ``TOOL``
        Tool -- Edit any geometry node group for use as an operator.

      :type: enum in [``'MODIFIER'``, ``'TOOL'``], default ``'MODIFIER'``

   .. data:: id

      Data-block whose nodes are being edited

      :type: :class:`ID`, (readonly)

   .. data:: id_from

      Data-block from which the edited data-block is linked

      :type: :class:`ID`, (readonly)

   .. attribute:: insert_offset_direction

      Direction to offset nodes on insertion

      :type: enum in [``'RIGHT'``, ``'LEFT'``], default ``'RIGHT'``

   .. attribute:: node_tree

      Base node tree from context

      :type: :class:`NodeTree`

   .. data:: overlay

      Settings for display of overlays in the Node Editor

      :type: :class:`SpaceNodeOverlay`, (readonly, never None)

   .. data:: path

      Path from the data-block to the currently edited node tree

      :type: :class:`SpaceNodeEditorPath` :class:`bpy_prop_collection` of :class:`NodeTreePath`, (readonly)

   .. attribute:: pin

      Use the pinned node tree

      :type: boolean, default False

   .. attribute:: shader_type

      Type of data to take shader from

      * ``OBJECT``
        Object -- Edit shader nodes from Object.
      * ``WORLD``
        World -- Edit shader nodes from World.
      * ``LINESTYLE``
        Line Style -- Edit shader nodes from Line Style.

      :type: enum in [``'OBJECT'``, ``'WORLD'``, ``'LINESTYLE'``], default ``'OBJECT'``

   .. attribute:: show_annotation

      Show annotations for this view

      :type: boolean, default False

   .. attribute:: show_backdrop

      Use active Viewer Node output as backdrop for compositing nodes

      :type: boolean, default False

   .. attribute:: show_gizmo

      Show gizmos of all types

      :type: boolean, default False

   .. attribute:: show_gizmo_active_node

      Context sensitive gizmo for the active node

      :type: boolean, default True

   .. attribute:: show_region_toolbar

      :type: boolean, default False

   .. attribute:: show_region_ui

      :type: boolean, default False

   .. data:: supports_previews

      Whether the node editor's type supports displaying node previews

      :type: boolean, default False, (readonly)

   .. attribute:: texture_type

      Type of data to take texture from

      * ``WORLD``
        World -- Edit texture nodes from World.
      * ``BRUSH``
        Brush -- Edit texture nodes from Brush.
      * ``LINESTYLE``
        Line Style -- Edit texture nodes from Line Style.

      :type: enum in [``'WORLD'``, ``'BRUSH'``, ``'LINESTYLE'``], default ``'WORLD'``

   .. attribute:: tree_type

      Node tree type to display and edit

      * ``GeometryNodeTree``
        Geometry Node Editor -- Geometry nodes.
      * ``CompositorNodeTree``
        Compositor -- Compositing nodes.
      * ``ShaderNodeTree``
        Shader Editor -- Shader nodes.
      * ``TextureNodeTree``
        Texture Node Editor -- Texture nodes.

      :type: enum in [``'GeometryNodeTree'``, ``'CompositorNodeTree'``, ``'ShaderNodeTree'``, ``'TextureNodeTree'``], default ``'DEFAULT'``

   .. method:: cursor_location_from_region(x, y)

      Set the cursor location using region coordinates

      :arg x: x, Region x coordinate
      :type x: int in [-inf, inf]
      :arg y: y, Region y coordinate
      :type y: int in [-inf, inf]

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


   .. classmethod:: draw_handler_add(callback, args, region_type, draw_type)
   
      Add a new draw handler to this space type.
      It will be called every time the specified region in the space type will be drawn.
      Note: All arguments are positional only for now.
   
      :arg callback:
         A function that will be called when the region is drawn.
         It gets the specified arguments as input, it's return value is ignored.
      :type callback: Callable[..., Any]
      :arg args: Arguments that will be passed to the callback.
      :type args: tuple[Any, ...]
      :arg region_type: The region type the callback draws in; usually ``WINDOW``. (:class:`bpy.types.Region.type`)
      :type region_type: str
      :arg draw_type: Usually ``POST_PIXEL`` for 2D drawing and ``POST_VIEW`` for 3D drawing. In some cases ``PRE_VIEW`` can be used. ``BACKDROP`` can be used for backdrops in the node editor.
      :type draw_type: str
      :return: Handler that can be removed later on.
      :rtype: object


   .. classmethod:: draw_handler_remove(handler, region_type)
   
      Remove a draw handler that was added previously.
   
      :arg handler: The draw handler that should be removed.
      :type handler: object
      :arg region_type: Region type the callback was added to.
      :type region_type: str


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`
   * :class:`Space.show_region_header`

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
   * :class:`Space.bl_rna_get_subclass`
   * :class:`Space.bl_rna_get_subclass_py`
   * :class:`Space.draw_handler_add`
   * :class:`Space.draw_handler_remove`

