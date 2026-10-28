Node Operators
==============

.. module:: bpy.ops.node

.. function:: activate_viewer()

   Activate selected viewer node in compositor and geometry nodes

.. function:: add_closure_zone(*, use_transform=False, settings=None, offset=(150.0, 0.0))

   Add a Closure zone

   :arg use_transform: Use Transform, Start transform operator after inserting the node
   :type use_transform: boolean, (optional)
   :arg settings: Settings, Settings to be applied on the newly created node
   :type settings: :class:`bpy_prop_collection` of :class:`NodeSetting`, (optional)
   :arg offset: Offset, Offset of nodes from the cursor when added
   :type offset: float array of 2 items in [-inf, inf], (optional)
   :File: `startup\bl_operators\node.py\:218 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L218>`__


.. function:: add_collection(*, name="", session_uid=0)

   Add a collection info node to the current node editor

   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)

.. function:: add_color(*, color=(0.0, 0.0, 0.0, 0.0), gamma=False, has_alpha=False)

   Add a color node to the current node editor

   :arg color: Color, Source color
   :type color: float array of 4 items in [0, inf], (optional)
   :arg gamma: Gamma Corrected, The source color is gamma corrected
   :type gamma: boolean, (optional)
   :arg has_alpha: Has Alpha, The source color contains an Alpha component
   :type has_alpha: boolean, (optional)

.. function:: add_empty_group(*, use_transform=False, settings=None)

   Add a group node with an empty group

   :arg use_transform: Use Transform, Start transform operator after inserting the node
   :type use_transform: boolean, (optional)
   :arg settings: Settings, Settings to be applied on the newly created node
   :type settings: :class:`bpy_prop_collection` of :class:`NodeSetting`, (optional)
   :File: `startup\bl_operators\node.py\:185 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L185>`__


.. function:: add_foreach_geometry_element_zone(*, use_transform=False, settings=None, offset=(150.0, 0.0))

   Add a For Each Geometry Element zone that allows executing nodes e.g. for each vertex separately

   :arg use_transform: Use Transform, Start transform operator after inserting the node
   :type use_transform: boolean, (optional)
   :arg settings: Settings, Settings to be applied on the newly created node
   :type settings: :class:`bpy_prop_collection` of :class:`NodeSetting`, (optional)
   :arg offset: Offset, Offset of nodes from the cursor when added
   :type offset: float array of 2 items in [-inf, inf], (optional)
   :File: `startup\bl_operators\node.py\:218 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L218>`__


.. function:: add_group(*, name="", session_uid=0, show_datablock_in_node=True)

   Add an existing node group to the current node editor

   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)
   :arg show_datablock_in_node: Show the datablock selector in the node
   :type show_datablock_in_node: boolean, (optional)

.. function:: add_group_asset(*, asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="")

   Add a node group asset to the active node tree

   :arg asset_library_type: Asset Library Type
   :type asset_library_type: enum in :ref:`rna_enum_asset_library_type_items`, (optional)
   :arg asset_library_identifier: Asset Library Identifier
   :type asset_library_identifier: string, (optional, never None)
   :arg relative_asset_identifier: Relative Asset Identifier
   :type relative_asset_identifier: string, (optional, never None)

.. function:: add_group_input_node(*, socket_identifier="", panel_identifier=0)

   Add a Group Input node with selected sockets to the current node editor

   :arg socket_identifier: Socket Identifier, Socket to include in the added group input/output node
   :type socket_identifier: string, (optional, never None)
   :arg panel_identifier: Panel Identifier, Panel from which to add sockets to the added group input/output node
   :type panel_identifier: int in [-inf, inf], (optional)

.. function:: add_image(*, filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', name="", session_uid=0)

   Add a image/movie file as node to the current node editor

   :arg filepath: File Path, Path to file
   :type filepath: string, (optional, never None)
   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
   :arg hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
   :type hide_props_region: boolean, (optional)
   :arg check_existing: Check Existing, Check and warn on overwriting existing files
   :type check_existing: boolean, (optional)
   :arg filter_blender: Filter .blend files
   :type filter_blender: boolean, (optional)
   :arg filter_backup: Filter .blend files
   :type filter_backup: boolean, (optional)
   :arg filter_image: Filter image files
   :type filter_image: boolean, (optional)
   :arg filter_movie: Filter movie files
   :type filter_movie: boolean, (optional)
   :arg filter_python: Filter Python files
   :type filter_python: boolean, (optional)
   :arg filter_font: Filter font files
   :type filter_font: boolean, (optional)
   :arg filter_sound: Filter sound files
   :type filter_sound: boolean, (optional)
   :arg filter_text: Filter text files
   :type filter_text: boolean, (optional)
   :arg filter_archive: Filter archive files
   :type filter_archive: boolean, (optional)
   :arg filter_btx: Filter btx files
   :type filter_btx: boolean, (optional)
   :arg filter_collada: Filter COLLADA files
   :type filter_collada: boolean, (optional)
   :arg filter_alembic: Filter Alembic files
   :type filter_alembic: boolean, (optional)
   :arg filter_usd: Filter USD files
   :type filter_usd: boolean, (optional)
   :arg filter_obj: Filter OBJ files
   :type filter_obj: boolean, (optional)
   :arg filter_volume: Filter OpenVDB volume files
   :type filter_volume: boolean, (optional)
   :arg filter_folder: Filter folders
   :type filter_folder: boolean, (optional)
   :arg filter_blenlib: Filter Blender IDs
   :type filter_blenlib: boolean, (optional)
   :arg filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
   :type filemode: int in [1, 9], (optional)
   :arg relative_path: Relative Path, Select the file relative to the blend file
   :type relative_path: boolean, (optional)
   :arg show_multiview: Enable Multi-View
   :type show_multiview: boolean, (optional)
   :arg use_multiview: Use Multi-View
   :type use_multiview: boolean, (optional)
   :arg display_type: Display Type

      * ``DEFAULT``
        Default -- Automatically determine display type for files.
      * ``LIST_VERTICAL``
        Short List -- Display files as short list.
      * ``LIST_HORIZONTAL``
        Long List -- Display files as a detailed list.
      * ``THUMBNAIL``
        Thumbnails -- Display files as thumbnails.
   :type display_type: enum in [``'DEFAULT'``, ``'LIST_VERTICAL'``, ``'LIST_HORIZONTAL'``, ``'THUMBNAIL'``], (optional)
   :arg sort_method: File sorting mode

      * ``DEFAULT``
        Default -- Automatically determine sort method for files.
      * ``FILE_SORT_ALPHA``
        Name -- Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION``
        Extension -- Sort the file list by extension/type.
      * ``FILE_SORT_TIME``
        Modified Date -- Sort files by modification time.
      * ``FILE_SORT_SIZE``
        Size -- Sort files by size.
      * ``ASSET_CATALOG``
        Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
   :type sort_method: enum in [``'DEFAULT'``, ``'FILE_SORT_ALPHA'``, ``'FILE_SORT_EXTENSION'``, ``'FILE_SORT_TIME'``, ``'FILE_SORT_SIZE'``, ``'ASSET_CATALOG'``], (optional)
   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)

.. function:: add_import_node(*, directory="", files=None)

   Add an import node to the node tree

   :arg directory: Directory, Directory of the file
   :type directory: string, (optional, never None)
   :arg files: Files
   :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)

.. function:: add_mask(*, name="", session_uid=0)

   Add a mask node to the current node editor

   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)

.. function:: add_material(*, name="", session_uid=0)

   Add a material node to the current node editor

   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)

.. function:: add_node(*, use_transform=False, settings=None, type="", visible_output="")

   Add a node to the active tree

   :arg use_transform: Use Transform, Start transform operator after inserting the node
   :type use_transform: boolean, (optional)
   :arg settings: Settings, Settings to be applied on the newly created node
   :type settings: :class:`bpy_prop_collection` of :class:`NodeSetting`, (optional)
   :arg type: Node Type, Node type
   :type type: string, (optional, never None)
   :arg visible_output: Output Name, If provided, all outputs that are named differently will be hidden
   :type visible_output: string, (optional, never None)
   :File: `startup\bl_operators\node.py\:149 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L149>`__


.. function:: add_object(*, name="", session_uid=0)

   Add an object info node to the current node editor

   :arg name: Name, Name of the data-block to use by the operator
   :type name: string, (optional, never None)
   :arg session_uid: Session UID, Session UID of the data-block to use by the operator
   :type session_uid: int in [-inf, inf], (optional)

.. function:: add_repeat_zone(*, use_transform=False, settings=None, offset=(150.0, 0.0))

   Add a repeat zone that allows executing nodes a dynamic number of times

   :arg use_transform: Use Transform, Start transform operator after inserting the node
   :type use_transform: boolean, (optional)
   :arg settings: Settings, Settings to be applied on the newly created node
   :type settings: :class:`bpy_prop_collection` of :class:`NodeSetting`, (optional)
   :arg offset: Offset, Offset of nodes from the cursor when added
   :type offset: float array of 2 items in [-inf, inf], (optional)
   :File: `startup\bl_operators\node.py\:218 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L218>`__


.. function:: add_reroute(*, path=None, cursor=11)

   Add a reroute node

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg cursor: Cursor
   :type cursor: int in [0, inf], (optional)

.. function:: add_simulation_zone(*, use_transform=False, settings=None, offset=(150.0, 0.0))

   Add simulation zone input and output nodes to the active tree

   :arg use_transform: Use Transform, Start transform operator after inserting the node
   :type use_transform: boolean, (optional)
   :arg settings: Settings, Settings to be applied on the newly created node
   :type settings: :class:`bpy_prop_collection` of :class:`NodeSetting`, (optional)
   :arg offset: Offset, Offset of nodes from the cursor when added
   :type offset: float array of 2 items in [-inf, inf], (optional)
   :File: `startup\bl_operators\node.py\:218 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L218>`__


.. function:: attach()

   Attach active node to a frame

.. function:: backimage_fit()

   Fit the background image to the view

.. function:: backimage_move()

   Move node backdrop

.. function:: backimage_sample()

   Use mouse to sample background image

.. function:: backimage_zoom(*, factor=1.2)

   Zoom in/out the background image

   :arg factor: Factor
   :type factor: float in [0, 10], (optional)

.. function:: bake_node_item_add()

   Add item below active item

.. function:: bake_node_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: bake_node_item_remove()

   Remove active item

.. function:: capture_attribute_item_add()

   Add item below active item

.. function:: capture_attribute_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: capture_attribute_item_remove()

   Remove active item

.. function:: clear_viewer_border()

   Clear the boundaries for viewer operations

.. function:: clipboard_copy()

   Copy the selected nodes to the internal clipboard

.. function:: clipboard_paste(*, offset=(0.0, 0.0))

   Paste nodes from the internal clipboard to the active node tree

   :arg offset: Location, The 2D view location for the center of the new nodes, or unchanged if not set
   :type offset: float array of 2 items in [-inf, inf], (optional)

.. function:: closure_input_item_add()

   Add item below active item

.. function:: closure_input_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: closure_input_item_remove()

   Remove active item

.. function:: closure_output_item_add()

   Add item below active item

.. function:: closure_output_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: closure_output_item_remove()

   Remove active item

.. function:: collapse_hide_unused_toggle()

   Toggle collapsed nodes and hide unused sockets

   :File: `startup\bl_operators\node.py\:299 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L299>`__

.. function:: combine_bundle_item_add()

   Add item below active item

.. function:: combine_bundle_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: combine_bundle_item_remove()

   Remove active item

.. function:: connect_to_output(*, run_in_geometry_nodes=True)

   Connect active node to the active output node of the node tree

   :arg run_in_geometry_nodes: Run in Geometry Nodes Editor
   :type run_in_geometry_nodes: boolean, (optional)
   :File: `startup\bl_operators\connect_to_output.py\:251 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\connect_to_output.py#L251>`__


.. function:: cryptomatte_layer_add()

   Add a new input layer to a Cryptomatte node

.. function:: cryptomatte_layer_remove()

   Remove layer from a Cryptomatte node

.. function:: deactivate_viewer()

   Deactivate selected viewer node in geometry nodes

.. function:: default_group_width_set()

   Set the width based on the parent group node in the current context

.. function:: delete()

   Remove selected nodes

.. function:: delete_reconnect()

   Remove nodes and reconnect nodes as if deletion was muted

.. function:: detach()

   Detach selected nodes from parents

.. function:: detach_translate_attach(*, NODE_OT_detach=None, TRANSFORM_OT_translate=None, NODE_OT_attach=None)

   Detach nodes, move and attach to frame

   :arg NODE_OT_detach: Detach Nodes, Detach selected nodes from parents
   :type NODE_OT_detach: :class:`NODE_OT_detach`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)
   :arg NODE_OT_attach: Attach Nodes, Attach active node to a frame
   :type NODE_OT_attach: :class:`NODE_OT_attach`, (optional)

.. function:: duplicate(*, keep_inputs=False, linked=True)

   Duplicate selected nodes

   :arg keep_inputs: Keep Inputs, Keep the input links to duplicated nodes
   :type keep_inputs: boolean, (optional)
   :arg linked: Linked, Duplicate node but not node trees, linking to the original data
   :type linked: boolean, (optional)

.. function:: duplicate_move(*, NODE_OT_duplicate=None, NODE_OT_translate_attach=None)

   Duplicate selected nodes and move them

   :arg NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
   :type NODE_OT_duplicate: :class:`NODE_OT_duplicate`, (optional)
   :arg NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
   :type NODE_OT_translate_attach: :class:`NODE_OT_translate_attach`, (optional)

.. function:: duplicate_move_keep_inputs(*, NODE_OT_duplicate=None, NODE_OT_translate_attach=None)

   Duplicate selected nodes keeping input links and move them

   :arg NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
   :type NODE_OT_duplicate: :class:`NODE_OT_duplicate`, (optional)
   :arg NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
   :type NODE_OT_translate_attach: :class:`NODE_OT_translate_attach`, (optional)

.. function:: duplicate_move_linked(*, NODE_OT_duplicate=None, NODE_OT_translate_attach=None)

   Duplicate selected nodes, but not their node trees, and move them

   :arg NODE_OT_duplicate: Duplicate Nodes, Duplicate selected nodes
   :type NODE_OT_duplicate: :class:`NODE_OT_duplicate`, (optional)
   :arg NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
   :type NODE_OT_translate_attach: :class:`NODE_OT_translate_attach`, (optional)

.. function:: enum_definition_item_add()

   Add item below active item

.. function:: enum_definition_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: enum_definition_item_remove()

   Remove active item

.. function:: evaluate_closure_input_item_add()

   Add item below active item

.. function:: evaluate_closure_input_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: evaluate_closure_input_item_remove()

   Remove active item

.. function:: evaluate_closure_output_item_add()

   Add item below active item

.. function:: evaluate_closure_output_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: evaluate_closure_output_item_remove()

   Remove active item

.. function:: find_node()

   Search for a node by name and focus and select it

.. function:: foreach_geometry_element_zone_generation_item_add()

   Add item below active item

.. function:: foreach_geometry_element_zone_generation_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: foreach_geometry_element_zone_generation_item_remove()

   Remove active item

.. function:: foreach_geometry_element_zone_input_item_add()

   Add item below active item

.. function:: foreach_geometry_element_zone_input_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: foreach_geometry_element_zone_input_item_remove()

   Remove active item

.. function:: foreach_geometry_element_zone_main_item_add()

   Add item below active item

.. function:: foreach_geometry_element_zone_main_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: foreach_geometry_element_zone_main_item_remove()

   Remove active item

.. function:: format_string_item_add()

   Add item below active item

.. function:: format_string_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: format_string_item_remove()

   Remove active item

.. function:: gltf_settings_node_operator()

   Add a node to the active tree for glTF export

   :File: `addons_core\io_scene_gltf2\blender\com\gltf2_blender_ui.py\:35 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\io_scene_gltf2\blender\com\gltf2_blender_ui.py#L35>`__

.. function:: group_edit(*, exit=False)

   Edit node group

   :arg exit: Exit
   :type exit: boolean, (optional)

.. function:: group_insert()

   Insert selected nodes into a node group

.. function:: group_make()

   Make group from selected nodes

.. function:: group_separate(*, type='COPY')

   Separate selected nodes from the node group

   :arg type: Type

      * ``COPY``
        Copy -- Copy to parent node tree, keep group intact.
      * ``MOVE``
        Move -- Move to parent node tree, remove from group.
   :type type: enum in [``'COPY'``, ``'MOVE'``], (optional)

.. function:: group_ungroup()

   Ungroup selected nodes

.. function:: hide_socket_toggle()

   Toggle unused node socket display

.. function:: hide_toggle()

   Toggle hiding of selected nodes

.. function:: index_switch_item_add()

   Add bake item

.. function:: index_switch_item_remove(*, index=0)

   Remove an item from the index switch

   :arg index: Index, Index to remove
   :type index: int in [0, inf], (optional)

.. function:: insert_offset()

   Automatically offset nodes on insertion

.. function:: interface_item_duplicate()

   Add a copy of the active item to the interface

   :File: `startup\bl_operators\node.py\:456 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L456>`__

.. function:: interface_item_make_panel_toggle()

   Make the active boolean socket a toggle for its parent panel

   :File: `startup\bl_operators\node.py\:527 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L527>`__

.. function:: interface_item_new(*, item_type='')

   Add a new item to the interface

   :arg item_type: Item Type, Type of the item to create
   :type item_type: enum in [], (optional)
   :File: `startup\bl_operators\node.py\:399 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L399>`__


.. function:: interface_item_remove()

   Remove active item from the interface

   :File: `startup\bl_operators\node.py\:475 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L475>`__

.. function:: interface_item_unlink_panel_toggle()

   Make the panel toggle a stand-alone socket

   :File: `startup\bl_operators\node.py\:575 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L575>`__

.. function:: join()

   Attach selected nodes to a new common frame

.. function:: join_named(*, NODE_OT_join=None, WM_OT_call_panel=None)

   Create a new frame node around the selected nodes and name it immediately

   :arg NODE_OT_join: Join Nodes, Attach selected nodes to a new common frame
   :type NODE_OT_join: :class:`NODE_OT_join`, (optional)
   :arg WM_OT_call_panel: Call Panel, Open a predefined panel
   :type WM_OT_call_panel: :class:`WM_OT_call_panel`, (optional)

.. function:: link(*, detach=False, drag_start=(0.0, 0.0), inside_padding=2.0, outside_padding=0.0, speed_ramp=1.0, max_speed=26.0, delay=0.5, zoom_influence=0.5)

   Use the mouse to create a link between two nodes

   :arg detach: Detach, Detach and redirect existing links
   :type detach: boolean, (optional)
   :arg drag_start: Drag Start, The position of the mouse cursor at the start of the operation
   :type drag_start: float array of 2 items in [-6, 6], (optional)
   :arg inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
   :type inside_padding: float in [0, 100], (optional)
   :arg outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
   :type outside_padding: float in [0, 100], (optional)
   :arg speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
   :type speed_ramp: float in [0, 100], (optional)
   :arg max_speed: Max Speed, Maximum speed in UI units per second
   :type max_speed: float in [0, 10000], (optional)
   :arg delay: Delay, Delay in seconds before maximum speed is reached
   :type delay: float in [0, 10], (optional)
   :arg zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
   :type zoom_influence: float in [0, 1], (optional)

.. function:: link_make(*, replace=False)

   Make a link between selected output and input sockets

   :arg replace: Replace, Replace socket connections with the new links
   :type replace: boolean, (optional)

.. function:: link_viewer()

   Link to viewer node

.. function:: links_cut(*, path=None, cursor=15)

   Use the mouse to cut (remove) some links

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg cursor: Cursor
   :type cursor: int in [0, inf], (optional)

.. function:: links_detach()

   Remove all links to selected nodes, and try to connect neighbor nodes together

.. function:: links_mute(*, path=None, cursor=39)

   Use the mouse to mute links

   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg cursor: Cursor
   :type cursor: int in [0, inf], (optional)

.. function:: move_detach_links(*, NODE_OT_links_detach=None, TRANSFORM_OT_translate=None)

   Move a node to detach links

   :arg NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
   :type NODE_OT_links_detach: :class:`NODE_OT_links_detach`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: move_detach_links_release(*, NODE_OT_links_detach=None, NODE_OT_translate_attach=None)

   Move a node to detach links

   :arg NODE_OT_links_detach: Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together
   :type NODE_OT_links_detach: :class:`NODE_OT_links_detach`, (optional)
   :arg NODE_OT_translate_attach: Move and Attach, Move nodes and attach to frame
   :type NODE_OT_translate_attach: :class:`NODE_OT_translate_attach`, (optional)

.. function:: mute_toggle()

   Toggle muting of selected nodes

.. function:: new_geometry_node_group_assign()

   Create a new geometry node group and assign it to the active modifier

   :File: `startup\bl_operators\geometry_nodes.py\:337 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\geometry_nodes.py#L337>`__

.. function:: new_geometry_node_group_tool()

   Create a new geometry node group for a tool

   :File: `startup\bl_operators\geometry_nodes.py\:358 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\geometry_nodes.py#L358>`__

.. function:: new_geometry_nodes_modifier()

   Create a new modifier with a new geometry node group

   :File: `startup\bl_operators\geometry_nodes.py\:314 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\geometry_nodes.py#L314>`__

.. function:: new_node_tree(*, type='', name="NodeTree")

   Create a new node tree

   :arg type: Tree Type
   :type type: enum in [], (optional)
   :arg name: Name
   :type name: string, (optional, never None)

.. function:: node_color_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove a Node Color Preset

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :File: `startup\bl_operators\presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L119>`__


.. function:: node_copy_color()

   Copy color to all selected nodes

.. function:: options_toggle()

   Toggle option buttons display for selected nodes

.. function:: output_file_add_socket(*, file_path="")

   Add a new input to a file output node

   :arg file_path: File Path, Subpath of the output file
   :type file_path: string, (optional, never None)

.. function:: output_file_move_active_socket(*, direction='DOWN')

   Move the active input of a file output node up or down the list

   :arg direction: Direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: output_file_remove_active_socket()

   Remove the active input from a file output node

.. function:: parent_set()

   Attach selected nodes

.. function:: preview_toggle()

   Toggle preview display for selected nodes

.. function:: read_viewlayers()

   Read all render layers of all used scenes

.. function:: render_changed()

   Render current scene, when input node's layer has been changed

.. function:: repeat_zone_item_add()

   Add item below active item

.. function:: repeat_zone_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: repeat_zone_item_remove()

   Remove active item

.. function:: resize()

   Resize a node

.. function:: select(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, location=(0, 0), socket_select=False, clear_viewer=False)

   Select the node under the cursor

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg deselect: Deselect, Remove from selection
   :type deselect: boolean, (optional)
   :arg toggle: Toggle Selection, Toggle the selection
   :type toggle: boolean, (optional)
   :arg deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
   :type deselect_all: boolean, (optional)
   :arg select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
   :type select_passthrough: boolean, (optional)
   :arg location: Location, Mouse location
   :type location: int array of 2 items in [-inf, inf], (optional)
   :arg socket_select: Socket Select
   :type socket_select: boolean, (optional)
   :arg clear_viewer: Clear Viewer, Deactivate geometry nodes viewer when clicking in empty space
   :type clear_viewer: boolean, (optional)

.. function:: select_all(*, action='TOGGLE')

   (De)select all nodes

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: select_box(*, tweak=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

   Use box selection to select nodes

   :arg tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
   :type tweak: boolean, (optional)
   :arg xmin: X Min
   :type xmin: int in [-inf, inf], (optional)
   :arg xmax: X Max
   :type xmax: int in [-inf, inf], (optional)
   :arg ymin: Y Min
   :type ymin: int in [-inf, inf], (optional)
   :arg ymax: Y Max
   :type ymax: int in [-inf, inf], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)
   :arg mode: Mode

      * ``SET``
        Set -- Set a new selection.
      * ``ADD``
        Extend -- Extend existing selection.
      * ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``], (optional)

.. function:: select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

   Use circle selection to select nodes

   :arg x: X
   :type x: int in [-inf, inf], (optional)
   :arg y: Y
   :type y: int in [-inf, inf], (optional)
   :arg radius: Radius
   :type radius: int in [1, inf], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)
   :arg mode: Mode

      * ``SET``
        Set -- Set a new selection.
      * ``ADD``
        Extend -- Extend existing selection.
      * ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``], (optional)

.. function:: select_grouped(*, extend=False, type='TYPE')

   Select nodes with similar properties

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg type: Type
   :type type: enum in [``'TYPE'``, ``'COLOR'``, ``'PREFIX'``, ``'SUFFIX'``], (optional)

.. function:: select_lasso(*, tweak=False, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

   Select nodes using lasso selection

   :arg tweak: Tweak, Only activate when mouse is not over a node (useful for tweak gesture)
   :type tweak: boolean, (optional)
   :arg path: Path
   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
   :type use_smooth_stroke: boolean, (optional)
   :arg smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
   :type smooth_stroke_factor: float in [0.5, 0.99], (optional)
   :arg smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
   :type smooth_stroke_radius: int in [10, 200], (optional)
   :arg mode: Mode

      * ``SET``
        Set -- Set a new selection.
      * ``ADD``
        Extend -- Extend existing selection.
      * ``SUB``
        Subtract -- Subtract existing selection.
   :type mode: enum in [``'SET'``, ``'ADD'``, ``'SUB'``], (optional)

.. function:: select_link_viewer(*, NODE_OT_select=None, NODE_OT_link_viewer=None)

   Select node and link it to a viewer node

   :arg NODE_OT_select: Select, Select the node under the cursor
   :type NODE_OT_select: :class:`NODE_OT_select`, (optional)
   :arg NODE_OT_link_viewer: Link to Viewer Node, Link to viewer node
   :type NODE_OT_link_viewer: :class:`NODE_OT_link_viewer`, (optional)

.. function:: select_linked_from()

   Select nodes linked from the selected ones

.. function:: select_linked_to()

   Select nodes linked to the selected ones

.. function:: select_same_type_step(*, prev=False)

   Activate and view same node type, step by step

   :arg prev: Previous
   :type prev: boolean, (optional)

.. function:: separate_bundle_item_add()

   Add item below active item

.. function:: separate_bundle_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: separate_bundle_item_remove()

   Remove active item

.. function:: shader_script_update()

   Update shader script node with new sockets and options from the script

.. function:: simulation_zone_item_add()

   Add item below active item

.. function:: simulation_zone_item_move(*, direction='UP')

   Move active item

   :arg direction: Direction, Move direction
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: simulation_zone_item_remove()

   Remove active item

.. function:: translate_attach(*, TRANSFORM_OT_translate=None, NODE_OT_attach=None)

   Move nodes and attach to frame

   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)
   :arg NODE_OT_attach: Attach Nodes, Attach active node to a frame
   :type NODE_OT_attach: :class:`NODE_OT_attach`, (optional)

.. function:: translate_attach_remove_on_cancel(*, TRANSFORM_OT_translate=None, NODE_OT_attach=None)

   Move nodes and attach to frame

   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)
   :arg NODE_OT_attach: Attach Nodes, Attach active node to a frame
   :type NODE_OT_attach: :class:`NODE_OT_attach`, (optional)

.. function:: tree_path_parent()

   Go to parent node tree

   :File: `startup\bl_operators\node.py\:329 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L329>`__

.. function:: view_all()

   Resize view so you can see all nodes

.. function:: view_selected()

   Resize view so you can see selected nodes

.. function:: viewer_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

   Set the boundaries for viewer operations

   :arg xmin: X Min
   :type xmin: int in [-inf, inf], (optional)
   :arg xmax: X Max
   :type xmax: int in [-inf, inf], (optional)
   :arg ymin: Y Min
   :type ymin: int in [-inf, inf], (optional)
   :arg ymax: Y Max
   :type ymax: int in [-inf, inf], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)

.. function:: viewer_shortcut_get(*, viewer_index=0)

   Activate a specific viewer node using 1,2,..,9 keys

   :arg viewer_index: Viewer Index, Index corresponding to the shortcut, e.g. number key 1 corresponds to index 1 etc..
   :type viewer_index: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\node.py\:689 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L689>`__


.. function:: viewer_shortcut_set(*, viewer_index=0)

   Create a viewer shortcut for the selected node by pressing ctrl+1,2,..9

   :arg viewer_index: Viewer Index, Index corresponding to the shortcut, e.g. number key 1 corresponds to index 1 etc..
   :type viewer_index: int in [-inf, inf], (optional)
   :File: `startup\bl_operators\node.py\:629 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\node.py#L629>`__


