Outliner Operators
==================

.. module:: bpy.ops.outliner

.. function:: action_set(*, action='')

   Change the active action used

   :arg action: Action
   :type action: enum in [], (optional)

.. function:: animdata_operation(*, type='CLEAR_ANIMDATA')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg type: Animation Operation

      * ``CLEAR_ANIMDATA``
        Clear Animation Data -- Remove this animation data container.
      * ``SET_ACT``
        Set Action.
      * ``CLEAR_ACT``
        Unlink Action.
      * ``REFRESH_DRIVERS``
        Refresh Drivers.
      * ``CLEAR_DRIVERS``
        Clear Drivers.
   :type type: enum in [``'CLEAR_ANIMDATA'``, ``'SET_ACT'``, ``'CLEAR_ACT'``, ``'REFRESH_DRIVERS'``, ``'CLEAR_DRIVERS'``], (optional)

.. function:: clear_filter()

   Clear the search filter

.. function:: collection_color_tag_set(*, color='NONE')

   Set a color tag for the selected collections

   :arg color: Color Tag
   :type color: enum in :ref:`rna_enum_collection_color_items`, (optional)

.. function:: collection_disable()

   Disable viewport display in the view layers

.. function:: collection_disable_render()

   Do not render this collection

.. function:: collection_drop()

   Drag to move to collection in Outliner

.. function:: collection_duplicate()

   Recursively duplicate the collection, all its children, objects and object data

.. function:: collection_duplicate_linked()

   Recursively duplicate the collection, all its children and objects, with linked object data

.. function:: collection_enable()

   Enable viewport display in the view layers

.. function:: collection_enable_render()

   Render the collection

.. function:: collection_exclude_clear()

   Include collection in the active view layer

.. function:: collection_exclude_set()

   Exclude collection from the active view layer

.. function:: collection_hide()

   Hide the collection in this view layer

.. function:: collection_hide_inside()

   Hide all the objects and collections inside the collection

.. function:: collection_hierarchy_delete()

   Delete selected collection hierarchies

.. function:: collection_holdout_clear()

   Clear masking of collection in the active view layer

.. function:: collection_holdout_set()

   Mask collection in the active view layer

.. function:: collection_indirect_only_clear()

   Clear collection contributing only indirectly in the view layer

.. function:: collection_indirect_only_set()

   Set collection to only contribute indirectly (through shadows and reflections) in the view layer

.. function:: collection_instance()

   Instance selected collections to active scene

.. function:: collection_isolate(*, extend=False)

   Hide all but this collection and its parents

   :arg extend: Extend, Extend current visible collections
   :type extend: boolean, (optional)

.. function:: collection_link()

   Link selected collections to active scene

.. function:: collection_new(*, nested=True)

   Add a new collection inside selected collection

   :arg nested: Nested, Add as child of selected collection
   :type nested: boolean, (optional)

.. function:: collection_objects_deselect()

   Deselect objects in collection

.. function:: collection_objects_select()

   Select objects in collection

.. function:: collection_show()

   Show the collection in this view layer

.. function:: collection_show_inside()

   Show all the objects and collections inside the collection

.. function:: constraint_operation(*, type='ENABLE')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg type: Constraint Operation
   :type type: enum in [``'ENABLE'``, ``'DISABLE'``, ``'DELETE'``], (optional)

.. function:: data_operation(*, type='DEFAULT')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg type: Data Operation
   :type type: enum in [``'DEFAULT'``], (optional)

.. function:: datastack_drop()

   Copy or reorder modifiers, constraints, and effects

.. function:: delete(*, hierarchy=False)

   Delete selected objects and collections

   :arg hierarchy: Hierarchy, Delete child objects and collections
   :type hierarchy: boolean, (optional)

.. function:: drivers_add_selected()

   Add drivers to selected items

.. function:: drivers_delete_selected()

   Delete drivers assigned to selected items

.. function:: expanded_toggle()

   Expand/Collapse all items

.. function:: hide()

   Hide selected objects and collections

.. function:: highlight_update()

   Update the item highlight based on the current mouse position

.. function:: id_copy()

   Copy the selected data-blocks to the internal clipboard

.. function:: id_delete()

   Delete the ID under cursor

.. function:: id_linked_relocate()

   Replace the active linked ID (and its dependencies if any) by another one, from the same or a different library

.. function:: id_operation(*, type='UNLINK')

   General data-block management operations

   :arg type: ID Data Operation

      * ``UNLINK``
        Unlink.
      * ``LOCAL``
        Make Local.
      * ``SINGLE``
        Make Single User.
      * ``DELETE``
        Delete.
      * ``REMAP``
        Remap Users -- Make all users of selected data-blocks to use instead current (clicked) one.
      * ``COPY``
        Copy.
      * ``PASTE``
        Paste.
      * ``ADD_FAKE``
        Add Fake User -- Ensure data-block gets saved even if it isn't in use (e.g. for motion and material libraries).
      * ``CLEAR_FAKE``
        Clear Fake User.
      * ``RENAME``
        Rename.
      * ``SELECT_LINKED``
        Select Linked.
   :type type: enum in [``'UNLINK'``, ``'LOCAL'``, ``'SINGLE'``, ``'DELETE'``, ``'REMAP'``, ``'COPY'``, ``'PASTE'``, ``'ADD_FAKE'``, ``'CLEAR_FAKE'``, ``'RENAME'``, ``'SELECT_LINKED'``], (optional)

.. function:: id_paste()

   Paste data-blocks from the internal clipboard

.. function:: id_remap(*, id_type='OBJECT', old_id='', new_id='')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg id_type: ID Type
   :type id_type: enum in :ref:`rna_enum_id_type_items`, (optional)
   :arg old_id: Old ID, Old ID to replace
   :type old_id: enum in [], (optional)
   :arg new_id: New ID, New ID to remap all selected IDs' users to
   :type new_id: enum in [], (optional)

.. function:: item_activate(*, extend=False, extend_range=False, deselect_all=False, recurse=False)

   Handle mouse clicks to select and activate items

   :arg extend: Extend, Extend selection for activation
   :type extend: boolean, (optional)
   :arg extend_range: Extend Range, Select a range from active element
   :type extend_range: boolean, (optional)
   :arg deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
   :type deselect_all: boolean, (optional)
   :arg recurse: Recurse, Select objects recursively from active element
   :type recurse: boolean, (optional)

.. function:: item_drag_drop()

   Drag and drop element to another place

.. function:: item_openclose(*, all=False)

   Toggle whether item under cursor is enabled or closed

   :arg all: All, Close or open all items
   :type all: boolean, (optional)

.. function:: item_rename(*, use_active=False)

   Rename the active element

   :arg use_active: Use Active, Rename the active item, rather than the one the mouse is over
   :type use_active: boolean, (optional)

.. function:: keyingset_add_selected()

   Add selected items (blue-gray rows) to active Keying Set

.. function:: keyingset_remove_selected()

   Remove selected items (blue-gray rows) from active Keying Set

.. function:: lib_operation(*, type='DELETE')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg type: Library Operation

      * ``DELETE``
        Delete -- Delete this library and all its items.
      * ``RELOCATE``
        Relocate -- Select a new path for this library, and reload all its data.
      * ``RELOAD``
        Reload -- Reload all data from this library.
   :type type: enum in [``'DELETE'``, ``'RELOCATE'``, ``'RELOAD'``], (optional)

.. function:: lib_relocate()

   Relocate the library under cursor

.. function:: liboverride_operation(*, type='OVERRIDE_LIBRARY_CREATE_HIERARCHY', selection_set='SELECTED')

   Create, reset or clear library override hierarchies

   :arg type: Library Override Operation

      * ``OVERRIDE_LIBRARY_CREATE_HIERARCHY``
        Make -- Create a local override of the selected linked data-blocks, and their hierarchy of dependencies.
      * ``OVERRIDE_LIBRARY_RESET``
        Reset -- Reset the selected local overrides to their linked references values.
      * ``OVERRIDE_LIBRARY_CLEAR_SINGLE``
        Clear -- Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable.
   :type type: enum in [``'OVERRIDE_LIBRARY_CREATE_HIERARCHY'``, ``'OVERRIDE_LIBRARY_RESET'``, ``'OVERRIDE_LIBRARY_CLEAR_SINGLE'``], (optional)
   :arg selection_set: Selection Set, Over which part of the tree items to apply the operation

      * ``SELECTED``
        Selected -- Apply the operation over selected data-blocks only.
      * ``CONTENT``
        Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree).
      * ``SELECTED_AND_CONTENT``
        Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
   :type selection_set: enum in [``'SELECTED'``, ``'CONTENT'``, ``'SELECTED_AND_CONTENT'``], (optional)

.. function:: liboverride_troubleshoot_operation(*, type='OVERRIDE_LIBRARY_RESYNC_HIERARCHY', selection_set='SELECTED')

   Advanced operations over library override to help fix broken hierarchies

   :arg type: Library Override Troubleshoot Operation

      * ``OVERRIDE_LIBRARY_RESYNC_HIERARCHY``
        Resync -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies.
      * ``OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE``
        Resync Enforce -- Rebuild the selected local overrides from their linked references, as well as their hierarchies of dependencies, enforcing these hierarchies to match the linked data (i.e. ignoring existing overrides on data-blocks pointer properties).
      * ``OVERRIDE_LIBRARY_DELETE_HIERARCHY``
        Delete -- Delete the selected local overrides (including their hierarchies of override dependencies) and relink their usages to the linked data-blocks.
   :type type: enum in [``'OVERRIDE_LIBRARY_RESYNC_HIERARCHY'``, ``'OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE'``, ``'OVERRIDE_LIBRARY_DELETE_HIERARCHY'``], (optional)
   :arg selection_set: Selection Set, Over which part of the tree items to apply the operation

      * ``SELECTED``
        Selected -- Apply the operation over selected data-blocks only.
      * ``CONTENT``
        Content -- Apply the operation over content of the selected items only (the data-blocks in their sub-tree).
      * ``SELECTED_AND_CONTENT``
        Selected & Content -- Apply the operation over selected data-blocks and all their dependencies.
   :type selection_set: enum in [``'SELECTED'``, ``'CONTENT'``, ``'SELECTED_AND_CONTENT'``], (optional)

.. function:: material_drop()

   Drag material to object in Outliner

.. function:: modifier_operation(*, type='APPLY')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg type: Modifier Operation
   :type type: enum in [``'APPLY'``, ``'DELETE'``, ``'TOGVIS'``, ``'TOGREN'``], (optional)

.. function:: object_operation(*, type='SELECT')

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg type: Object Operation

      * ``SELECT``
        Select.
      * ``DESELECT``
        Deselect.
      * ``SELECT_HIERARCHY``
        Select Hierarchy.
      * ``REMAP``
        Remap Users -- Make all users of selected data-blocks to use instead a new chosen one.
      * ``RENAME``
        Rename.
   :type type: enum in [``'SELECT'``, ``'DESELECT'``, ``'SELECT_HIERARCHY'``, ``'REMAP'``, ``'RENAME'``], (optional)

.. function:: operation()

   Context menu for item operations

.. function:: orphans_manage()

   Open a window to manage unused data

.. function:: orphans_purge(*, do_local_ids=True, do_linked_ids=True, do_recursive=True)

   Clear all orphaned data-blocks without any users from the file

   :arg do_local_ids: Local Data-blocks, Include unused local data-blocks into deletion
   :type do_local_ids: boolean, (optional)
   :arg do_linked_ids: Linked Data-blocks, Include unused linked data-blocks into deletion
   :type do_linked_ids: boolean, (optional)
   :arg do_recursive: Recursive Delete, Recursively check for indirectly unused data-blocks, ensuring that no orphaned data-blocks remain after execution
   :type do_recursive: boolean, (optional)

.. function:: parent_clear()

   Drag to clear parent in Outliner

.. function:: parent_drop()

   Drag to parent in Outliner

.. function:: scene_drop()

   Drag object to scene in Outliner

.. function:: scene_operation(*, type='DELETE')

   Context menu for scene operations

   :arg type: Scene Operation
   :type type: enum in [``'DELETE'``], (optional)

.. function:: scroll_page(*, up=False)

   Scroll page up or down

   :arg up: Up, Scroll up one page
   :type up: boolean, (optional)

.. function:: select_all(*, action='TOGGLE')

   Toggle the Outliner selection of items

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

   Use box selection to select tree elements

   :arg tweak: Tweak, Tweak gesture from empty space for box selection
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

.. function:: select_walk(*, direction='UP', extend=False, toggle_all=False)

   Use walk navigation to select tree elements

   :arg direction: Walk Direction, Select/Deselect element in this direction
   :type direction: enum in [``'UP'``, ``'DOWN'``, ``'LEFT'``, ``'RIGHT'``], (optional)
   :arg extend: Extend, Extend selection on walk
   :type extend: boolean, (optional)
   :arg toggle_all: Toggle All, Toggle open/close hierarchy
   :type toggle_all: boolean, (optional)

.. function:: show_active()

   Open up the tree and adjust the view so that the active object is shown centered

.. function:: show_hierarchy()

   Open all object entries and close all others

.. function:: show_one_level(*, open=True)

   Expand/collapse all entries by one level

   :arg open: Open, Expand all entries one level deep
   :type open: boolean, (optional)

.. function:: start_filter()

   Start entering filter text

.. function:: unhide_all()

   Unhide all objects and collections

