ID(bpy_struct)
==============

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`Action`, :class:`Armature`, :class:`Brush`, :class:`CacheFile`, :class:`Camera`, :class:`Collection`, :class:`Curve`, :class:`Curves`, :class:`FreestyleLineStyle`, :class:`GreasePencil`, :class:`GreasePencilv3`, :class:`Image`, :class:`Key`, :class:`Lattice`, :class:`Library`, :class:`Light`, :class:`LightProbe`, :class:`Mask`, :class:`Material`, :class:`Mesh`, :class:`MetaBall`, :class:`MovieClip`, :class:`NodeTree`, :class:`Object`, :class:`PaintCurve`, :class:`Palette`, :class:`ParticleSettings`, :class:`PointCloud`, :class:`Scene`, :class:`Screen`, :class:`Sound`, :class:`Speaker`, :class:`Text`, :class:`Texture`, :class:`VectorFont`, :class:`Volume`, :class:`WindowManager`, :class:`WorkSpace`, :class:`World`

.. class:: ID(bpy_struct)

   Base type for data-blocks, defining a unique name, linking from other libraries and garbage collection

   .. attribute:: asset_data

      Additional data for an asset data-block

      :type: :class:`AssetMetaData`

   .. data:: id_type

      Type identifier of this data-block

      :type: enum in :ref:`rna_enum_id_type_items`, default ``'ACTION'``, (readonly)

   .. data:: is_editable

      This data-block is editable in the user interface. Linked datablocks are not editable, except if they were loaded as editable assets.

      :type: boolean, default False, (readonly)

   .. data:: is_embedded_data

      This data-block is not an independent one, but is actually a sub-data of another ID (typical example: root node trees or master collections)

      :type: boolean, default False, (readonly)

   .. data:: is_evaluated

      Whether this ID is runtime-only, evaluated data-block, or actual data from .blend file

      :type: boolean, default False, (readonly)

   .. data:: is_library_indirect

      Is this ID block linked indirectly

      :type: boolean, default False, (readonly)

   .. data:: is_missing

      This data-block is a place-holder for missing linked data (i.e. it is [an override of] a linked data that could not be found anymore)

      :type: boolean, default False, (readonly)

   .. attribute:: is_runtime_data

      This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base.

      :type: boolean, default False

   .. data:: library

      Library file the data-block is linked from

      :type: :class:`Library`, (readonly)

   .. data:: library_weak_reference

      Weak reference to a data-block in another library .blend file (used to re-use already appended data instead of appending new copies)

      :type: :class:`LibraryWeakReference`, (readonly)

   .. attribute:: name

      Unique data-block ID name (within a same type and library)

      :type: string, default "", (never None)

   .. data:: name_full

      Unique data-block ID name, including library one is any

      :type: string, default "", (readonly, never None)

   .. data:: original

      Actual data-block from .blend file (Main database) that generated that evaluated one

      :type: :class:`ID`, (readonly)

   .. data:: override_library

      Library override data

      :type: :class:`IDOverrideLibrary`, (readonly)

   .. data:: preview

      Preview image and icon of this data-block (always None if not supported for this type of data)

      :type: :class:`ImagePreview`, (readonly)

   .. data:: session_uid

      A session-wide unique identifier for the data block that remains the same across renames and internal reallocations, unchanged when reloading the file

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: tag

      Tools can use this to tag data for their own purposes (initial state is undefined)

      :type: boolean, default False

   .. attribute:: use_extra_user

      Indicates whether an extra user is set or not (mainly for internal/debug usages)

      :type: boolean, default False

   .. attribute:: use_fake_user

      Save this data-block even if it has no users

      :type: boolean, default False

   .. data:: users

      Number of times this data-block is referenced

      :type: int in [0, inf], default 0, (readonly)

   .. method:: rename(name, *, mode='NEVER')

      More refined handling in case the new name collides with another ID's name

      :arg name: New name to rename the ID to, if empty will re-use the current ID name
      :type name: string, (never None)
      :arg mode: How to handle name collision, in case the requested new name is already used by another ID of the same type

         * ``NEVER``
           Never Rename -- Never rename an exisitng ID whose name would conflict, the currently renamed ID will get a numeric suffix appended to its new name.
         * ``ALWAYS``
           Always Rename -- Always rename an exisitng ID whose name would conflict, ensuring that the currently renamed ID will get requested name.
         * ``SAME_ROOT``
           Rename If Same Root -- Only rename an exisitng ID whose name would conflict if its name root (everything besides the numerical suffix) is the same as the existing name of the currently renamed ID.
      :type mode: enum in [``'NEVER'``, ``'ALWAYS'``, ``'SAME_ROOT'``], (optional)
      :return: How did the renaming of the data-block went on

         * ``UNCHANGED``
           Unchanged -- The ID was not renamed, e.g. because it is already named as requested.
         * ``UNCHANGED_COLLISION``
           Unchanged Due to Collision -- The ID was not renamed, because requested name would have collided with another existing ID's name, and the automatically adjusted name was the same as the current ID's name.
         * ``RENAMED_NO_COLLISION``
           Renamed Without Collision -- The ID was renamed as requested, without creating any name collision.
         * ``RENAMED_COLLISION_ADJUSTED``
           Renamed With Collision -- The ID was renamed with adjustement of the requested name, to avoid a name collision.
         * ``RENAMED_COLLISION_FORCED``
           Renamed Enforced With Collision -- The ID was renamed as requested, also renaming another ID to avoid a name collision.
      :rtype: enum in [``'UNCHANGED'``, ``'UNCHANGED_COLLISION'``, ``'RENAMED_NO_COLLISION'``, ``'RENAMED_COLLISION_ADJUSTED'``, ``'RENAMED_COLLISION_FORCED'``]

   .. method:: evaluated_get(depsgraph)

      Get corresponding evaluated ID from the given dependency graph. Note that this does not ensure the dependency graph is fully evaluated, it just returns the result of the last evaluation.

      :arg depsgraph: Dependency graph to perform lookup in
      :type depsgraph: :class:`Depsgraph`, (never None)
      :return: New copy of the ID
      :rtype: :class:`ID`

   .. method:: copy()

      Create a copy of this data-block (not supported for all data-blocks). The result is added to the Blend-File Data (Main database), with all references to other data-blocks ensured to be from within the same Blend-File Data.

      :return: New copy of the ID
      :rtype: :class:`ID`

   .. method:: asset_mark()

      Enable easier reuse of the data-block through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)


   .. method:: asset_clear()

      Delete all asset metadata and turn the asset data-block back into a normal data-block


   .. method:: asset_generate_preview()

      Generate preview image (might be scheduled in a background thread)


   .. method:: override_create(*, remap_local_usages=False)

      Create an overridden local copy of this linked data-block (not supported for all data-blocks)

      :arg remap_local_usages: Whether local usages of the linked ID should be remapped to the new library override of it
      :type remap_local_usages: boolean, (optional)
      :return: New overridden local copy of the ID
      :rtype: :class:`ID`

   .. method:: override_hierarchy_create(scene, view_layer, *, reference=None, do_fully_editable=False)

      Create an overridden local copy of this linked data-block, and most of its dependencies when it is a Collection or and Object

      :arg scene: In which scene the new overrides should be instantiated
      :type scene: :class:`Scene`, (never None)
      :arg view_layer: In which view layer the new overrides should be instantiated
      :type view_layer: :class:`ViewLayer`, (never None)
      :arg reference: Another ID (usually an Object or Collection) used as a hint to decide where to instantiate the new overrides
      :type reference: :class:`ID`, (optional)
      :arg do_fully_editable: Make all library overrides generated by this call fully editable by the user (none will be 'system overrides')
      :type do_fully_editable: boolean, (optional)
      :return: New overridden local copy of the root ID
      :rtype: :class:`ID`

   .. method:: user_clear()

      Clear the user count of a data-block so its not saved, on reload the data will be removed


      This function is for advanced use only, misuse can crash Blender since the user
      count is used to prevent data being removed when it is used.

      .. literalinclude:: ..\examples\bpy.types.ID.user_clear.1.py
         :lines: 6-


   .. method:: user_remap(new_id)

      Replace all usage in the .blend file of this ID by new given one

      :arg new_id: New ID to use
      :type new_id: :class:`ID`, (never None)

   .. method:: make_local(*, clear_proxy=True, clear_liboverride=False, clear_asset_data=True)

      Make this datablock local, return local one (may be a copy of the original, in case it is also indirectly used)

      :arg clear_proxy: Deprecated, has no effect
      :type clear_proxy: boolean, (optional)
      :arg clear_liboverride: Remove potential library override data from the newly made local data
      :type clear_liboverride: boolean, (optional)
      :arg clear_asset_data: Remove potential asset metadata so the newly local data-block is not treated as asset data-block and won't show up in asset libraries
      :type clear_asset_data: boolean, (optional)
      :return: This ID, or the new ID if it was copied
      :rtype: :class:`ID`

   .. method:: user_of_id(id)

      Count the number of times that ID uses/references given one

      :arg id: ID to count usages
      :type id: :class:`ID`, (never None)
      :return: Number of usages/references of given id by current data-block
      :rtype: int in [0, inf]

   .. method:: animation_data_create()

      Create animation data to this ID, note that not all ID types support this

      :return: New animation data or nullptr
      :rtype: :class:`AnimData`

   .. method:: animation_data_clear()

      Clear animation on this ID


   .. method:: update_tag(*, refresh={})

      Tag the ID to update its display data, e.g. when calling :class:`bpy.types.Scene.update`

      :arg refresh: Type of updates to perform
      :type refresh: enum set in {``'OBJECT'``, ``'DATA'``, ``'TIME'``}, (optional)

   .. method:: preview_ensure()

      Ensure that this ID has preview data (if ID type supports it)

      :return: The existing or created preview
      :rtype: :class:`ImagePreview`

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

   * :mod:`bpy.context.annotation_data_owner`
   * :mod:`bpy.context.id`
   * :mod:`bpy.context.selected_ids`
   * :mod:`bpy.context.texture_user`
   * :class:`Action.fcurve_ensure_for_datablock`
   * :class:`ActionSlot.users`
   * :class:`AssetRepresentation.local_id`
   * :class:`BlendDataObjects.new`
   * :class:`BlendImportContextItem.id`
   * :class:`BlendImportContextItem.library_override_id`
   * :class:`BlendImportContextItem.reusable_local_id`
   * :class:`Depsgraph.id_eval_get`
   * :class:`Depsgraph.id_eval_get`
   * :class:`Depsgraph.ids`
   * :class:`DepsgraphUpdate.id`
   * :class:`DopeSheet.source`
   * :class:`DriverTarget.id`
   * :class:`ID.copy`
   * :class:`ID.evaluated_get`
   * :class:`ID.make_local`
   * :class:`ID.original`
   * :class:`ID.override_create`
   * :class:`ID.override_hierarchy_create`
   * :class:`ID.override_hierarchy_create`
   * :class:`ID.user_of_id`
   * :class:`ID.user_remap`
   * :class:`IDOverrideLibrary.hierarchy_root`
   * :class:`IDOverrideLibrary.reference`
   * :class:`IDOverrideLibraryPropertyOperation.subitem_local_id`
   * :class:`IDOverrideLibraryPropertyOperation.subitem_reference_id`
   * :class:`IDOverrideLibraryPropertyOperations.add`
   * :class:`IDOverrideLibraryPropertyOperations.add`
   * :class:`IDViewerPathElem.id`
   * :class:`Key.user`
   * :class:`KeyingSetPath.id`
   * :class:`KeyingSetPaths.add`
   * :class:`MaskParent.id`
   * :class:`NodeTree.get_from_context`
   * :class:`NodeTree.get_from_context`
   * :class:`NodesModifierDataBlock.id`
   * :class:`Object.data`
   * :class:`PropertyGroupItem.id`
   * :class:`SpaceFileBrowser.activate_asset_by_id`
   * :class:`SpaceNodeEditor.id`
   * :class:`SpaceNodeEditor.id_from`
   * :class:`SpaceProperties.pin_id`
   * :class:`UILayout.template_action`
   * :class:`UILayout.template_path_builder`
   * :class:`UILayout.template_preview`
   * :class:`UILayout.template_preview`

