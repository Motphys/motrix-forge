BlendData(bpy_struct)
=====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendData(bpy_struct)

   Main data structure representing a .blend file and all its data-blocks

   .. data:: actions

      Action data-blocks

      :type: :class:`BlendDataActions` :class:`bpy_prop_collection` of :class:`Action`, (readonly)

   .. data:: armatures

      Armature data-blocks

      :type: :class:`BlendDataArmatures` :class:`bpy_prop_collection` of :class:`Armature`, (readonly)

   .. data:: brushes

      Brush data-blocks

      :type: :class:`BlendDataBrushes` :class:`bpy_prop_collection` of :class:`Brush`, (readonly)

   .. data:: cache_files

      Cache Files data-blocks

      :type: :class:`BlendDataCacheFiles` :class:`bpy_prop_collection` of :class:`CacheFile`, (readonly)

   .. data:: cameras

      Camera data-blocks

      :type: :class:`BlendDataCameras` :class:`bpy_prop_collection` of :class:`Camera`, (readonly)

   .. data:: collections

      Collection data-blocks

      :type: :class:`BlendDataCollections` :class:`bpy_prop_collection` of :class:`Collection`, (readonly)

   .. data:: curves

      Curve data-blocks

      :type: :class:`BlendDataCurves` :class:`bpy_prop_collection` of :class:`Curve`, (readonly)

   .. data:: filepath

      Path to the .blend file

      :type: string, default "", (readonly, never None)

   .. data:: fonts

      Vector font data-blocks

      :type: :class:`BlendDataFonts` :class:`bpy_prop_collection` of :class:`VectorFont`, (readonly)

   .. data:: grease_pencils

      Annotation data-blocks (legacy Grease Pencil)

      :type: :class:`BlendDataGreasePencils` :class:`bpy_prop_collection` of :class:`GreasePencil`, (readonly)

   .. data:: grease_pencils_v3

      Grease Pencil data-blocks

      :type: :class:`BlendDataGreasePencilsV3` :class:`bpy_prop_collection` of :class:`GreasePencilv3`, (readonly)

   .. data:: hair_curves

      Hair curve data-blocks

      :type: :class:`BlendDataHairCurves` :class:`bpy_prop_collection` of :class:`Curves`, (readonly)

   .. data:: images

      Image data-blocks

      :type: :class:`BlendDataImages` :class:`bpy_prop_collection` of :class:`Image`, (readonly)

   .. data:: is_dirty

      Have recent edits been saved to disk

      :type: boolean, default False, (readonly)

   .. data:: is_saved

      Has the current session been saved to disk as a .blend file

      :type: boolean, default False, (readonly)

   .. data:: lattices

      Lattice data-blocks

      :type: :class:`BlendDataLattices` :class:`bpy_prop_collection` of :class:`Lattice`, (readonly)

   .. data:: libraries

      Library data-blocks

      :type: :class:`BlendDataLibraries` :class:`bpy_prop_collection` of :class:`Library`, (readonly)

   .. data:: lightprobes

      Light Probe data-blocks

      :type: :class:`BlendDataProbes` :class:`bpy_prop_collection` of :class:`LightProbe`, (readonly)

   .. data:: lights

      Light data-blocks

      :type: :class:`BlendDataLights` :class:`bpy_prop_collection` of :class:`Light`, (readonly)

   .. data:: linestyles

      Line Style data-blocks

      :type: :class:`BlendDataLineStyles` :class:`bpy_prop_collection` of :class:`FreestyleLineStyle`, (readonly)

   .. data:: masks

      Masks data-blocks

      :type: :class:`BlendDataMasks` :class:`bpy_prop_collection` of :class:`Mask`, (readonly)

   .. data:: materials

      Material data-blocks

      :type: :class:`BlendDataMaterials` :class:`bpy_prop_collection` of :class:`Material`, (readonly)

   .. data:: meshes

      Mesh data-blocks

      :type: :class:`BlendDataMeshes` :class:`bpy_prop_collection` of :class:`Mesh`, (readonly)

   .. data:: metaballs

      Metaball data-blocks

      :type: :class:`BlendDataMetaBalls` :class:`bpy_prop_collection` of :class:`MetaBall`, (readonly)

   .. data:: movieclips

      Movie Clip data-blocks

      :type: :class:`BlendDataMovieClips` :class:`bpy_prop_collection` of :class:`MovieClip`, (readonly)

   .. data:: node_groups

      Node group data-blocks

      :type: :class:`BlendDataNodeTrees` :class:`bpy_prop_collection` of :class:`NodeTree`, (readonly)

   .. data:: objects

      Object data-blocks

      :type: :class:`BlendDataObjects` :class:`bpy_prop_collection` of :class:`Object`, (readonly)

   .. data:: paint_curves

      Paint Curves data-blocks

      :type: :class:`BlendDataPaintCurves` :class:`bpy_prop_collection` of :class:`PaintCurve`, (readonly)

   .. data:: palettes

      Palette data-blocks

      :type: :class:`BlendDataPalettes` :class:`bpy_prop_collection` of :class:`Palette`, (readonly)

   .. data:: particles

      Particle data-blocks

      :type: :class:`BlendDataParticles` :class:`bpy_prop_collection` of :class:`ParticleSettings`, (readonly)

   .. data:: pointclouds

      Point cloud data-blocks

      :type: :class:`BlendDataPointClouds` :class:`bpy_prop_collection` of :class:`PointCloud`, (readonly)

   .. data:: scenes

      Scene data-blocks

      :type: :class:`BlendDataScenes` :class:`bpy_prop_collection` of :class:`Scene`, (readonly)

   .. data:: screens

      Screen data-blocks

      :type: :class:`BlendDataScreens` :class:`bpy_prop_collection` of :class:`Screen`, (readonly)

   .. data:: shape_keys

      Shape Key data-blocks

      :type: :class:`bpy_prop_collection` of :class:`Key`, (readonly)

   .. data:: sounds

      Sound data-blocks

      :type: :class:`BlendDataSounds` :class:`bpy_prop_collection` of :class:`Sound`, (readonly)

   .. data:: speakers

      Speaker data-blocks

      :type: :class:`BlendDataSpeakers` :class:`bpy_prop_collection` of :class:`Speaker`, (readonly)

   .. data:: texts

      Text data-blocks

      :type: :class:`BlendDataTexts` :class:`bpy_prop_collection` of :class:`Text`, (readonly)

   .. data:: textures

      Texture data-blocks

      :type: :class:`BlendDataTextures` :class:`bpy_prop_collection` of :class:`Texture`, (readonly)

   .. attribute:: use_autopack

      Automatically pack all external data into .blend file

      :type: boolean, default False

   .. data:: version

      File format version the .blend file was saved with

      :type: int array of 3 items in [0, inf], default (0, 0, 0), (readonly)

   .. data:: volumes

      Volume data-blocks

      :type: :class:`BlendDataVolumes` :class:`bpy_prop_collection` of :class:`Volume`, (readonly)

   .. data:: window_managers

      Window manager data-blocks

      :type: :class:`BlendDataWindowManagers` :class:`bpy_prop_collection` of :class:`WindowManager`, (readonly)

   .. data:: workspaces

      Workspace data-blocks

      :type: :class:`BlendDataWorkSpaces` :class:`bpy_prop_collection` of :class:`WorkSpace`, (readonly)

   .. data:: worlds

      World data-blocks

      :type: :class:`BlendDataWorlds` :class:`bpy_prop_collection` of :class:`World`, (readonly)

   .. method:: batch_remove(ids)
   
      Remove (delete) several IDs at once.
   
      Note that this function is quicker than individual calls to :func:`remove()` (from :class:`bpy.types.BlendData`
      ID collections), but less safe/versatile (it can break Blender, e.g. by removing all scenes...).
   
      :arg ids: Sequence of IDs (types can be mixed).
      :type ids: Sequence[:class:`bpy.types.ID`]


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


   .. method:: file_path_map(subset=None, key_types=None, include_libraries=False)
   
      Returns a mapping of all ID data-blocks in current ``bpy.data`` to a set of all file paths used by them.
   
      For list of valid set members for key_types, see: :class:`bpy.types.KeyingSetPath.id_type`.
   
      :arg subset: When given, only these data-blocks and their used file paths will be included as keys/values in the map.
      :type subset: sequence
      :arg key_types: When given, filter the keys mapped by ID types. Ignored if ``subset`` is also given.
      :type key_types: set of strings
      :arg include_libraries: Include library file paths of linked data. False by default.
      :type include_libraries: bool
      :return: dictionary of :class:`bpy.types.ID` instances, with sets of file path strings as their values.
      :rtype: dict


   .. method:: orphans_purge()
   
      Remove (delete) all IDs with no user.
   
      :arg do_local_ids: Include unused local IDs in the deletion, defaults to True
      :type do_local_ids: bool, optional
      :arg do_linked_ids: Include unused linked IDs in the deletion, defaults to True
      :type do_linked_ids: bool, optional
      :arg do_recursive: Recursively check for unused IDs, ensuring no orphaned one remain after a single run of that function, defaults to False
      :type do_recursive: bool, optional
      :return: The number of deleted IDs.


   .. method:: temp_data(filepath=None)
   
      A context manager that temporarily creates blender file data.
   
      :arg filepath: The file path for the newly temporary data. When None, the path of the currently open file is used.
      :type filepath: str | bytes | None
   
      :return: Blend file data which is freed once the context exists.
      :rtype: :class:`bpy.types.BlendData`


   .. method:: user_map(*, subset=None, key_types=None, value_types=None)
   
      Returns a mapping of all ID data-blocks in current ``bpy.data`` to a set of all data-blocks using them.
   
      For list of valid set members for key_types & value_types, see: :class:`bpy.types.KeyingSetPath.id_type`.
   
      :arg subset: When passed, only these data-blocks and their users will be included as keys/values in the map.
      :type subset: Sequence[:class:`bpy.types.ID`]
      :arg key_types: Filter the keys mapped by ID types.
      :type key_types: set[str]
      :arg value_types: Filter the values in the set by ID types.
      :type value_types: set[str]
      :return: dictionary that maps data-blocks ID's to their users.
      :rtype: dict[:class:`bpy.types.ID`, set[:class:`bpy.types.ID`]]


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

   * :class:`Context.blend_data`
   * :class:`RenderEngine.update`

