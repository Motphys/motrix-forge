PreferencesExperimental(bpy_struct)
===================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PreferencesExperimental(bpy_struct)

   Experimental features

   .. attribute:: override_auto_resync

      Disable library overrides automatic resync detection and process on file load (can be useful to help fixing broken files). Also see the `--disable-liboverride-auto-resync` command line option

      :type: boolean, default False

   .. attribute:: show_asset_debug_info

      Enable some extra fields in the Asset Browser to aid in debugging

      :type: boolean, default False

   .. attribute:: use_all_linked_data_direct

      Forces all linked data to be considered as directly linked. Workaround for current issues/limitations in BAT (Blender studio pipeline tool)

      :type: boolean, default False

   .. attribute:: use_asset_indexing

      Disable the asset indexer, to force every asset library refresh to completely reread assets from disk

      :type: boolean, default False

   .. attribute:: use_attribute_storage_write

      Instead of writing with the older "CustomData" format for forward compatibility, use the new "AttributeStorage" format

      :type: boolean, default False

   .. attribute:: use_bundle_and_closure_nodes

      Enables bundle and closure nodes in Geometry Nodes

      :type: boolean, default False

   .. attribute:: use_cycles_debug

      Enable Cycles debugging options for developers

      :type: boolean, default False

   .. attribute:: use_eevee_debug

      Enable EEVEE debugging options for developers

      :type: boolean, default False

   .. attribute:: use_extended_asset_browser

      Enable Asset Browser editor and operators to manage regular data-blocks as assets, not just poses

      :type: boolean, default False

   .. attribute:: use_extensions_debug

      Extra debugging information & developer support utilities for extensions

      :type: boolean, default False

   .. attribute:: use_new_curves_tools

      Enable additional features for the new curves data block

      :type: boolean, default False

   .. attribute:: use_new_volume_nodes

      Enables visibility of the new Volume nodes in the UI

      :type: boolean, default False

   .. attribute:: use_recompute_usercount_on_save_debug

      Recompute all ID usercounts before saving to a blendfile. Allows to work around invalid usercount handling in code that may lead to loss of data due to wrongly detected unused data-blocks

      :type: boolean, default False

   .. attribute:: use_sculpt_texture_paint

      Use texture painting in Sculpt Mode

      :type: boolean, default False

   .. attribute:: use_shader_node_previews

      Enables previews in the shader node editor

      :type: boolean, default False

   .. attribute:: use_socket_structure_type

      Enables new visualization of socket data compatibility in Geometry Nodes

      :type: boolean, default False

   .. attribute:: use_undo_legacy

      Use legacy undo (slower than the new default one, but may be more stable in some cases)

      :type: boolean, default False

   .. attribute:: use_viewport_debug

      Enable viewport debugging options for developers in the overlays pop-over

      :type: boolean, default False

   .. attribute:: write_large_blend_file_blocks

      Enables support for writing .blend files that contain buffers larger than 2 GB. If enabled, any saved files can not be opened by older Blender versions

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

   * :class:`Preferences.experimental`

