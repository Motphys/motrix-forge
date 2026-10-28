FileAssetSelectIDFilter(bpy_struct)
===================================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: FileAssetSelectIDFilter(bpy_struct)

   Which asset types to show/hide, when browsing an asset library

   .. attribute:: experimental_filter_armature

      Show Armature data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_cachefile

      Show Cache File data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_camera

      Show Camera data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_curve

      Show Curve data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_curves

      Show/hide Curves data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_font

      Show Font data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_grease_pencil

      Show Grease Pencil data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_image

      Show Image data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_lattice

      Show Lattice data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_light

      Show Light data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_light_probe

      Show Light Probe data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_linestyle

      Show Freestyle's Line Style data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_mask

      Show Mask data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_mesh

      Show Mesh data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_metaball

      Show Metaball data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_movie_clip

      Show Movie Clip data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_paint_curve

      Show Paint Curve data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_palette

      Show Palette data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_particle_settings

      Show Particle Settings data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_pointcloud

      Show/hide Point Cloud data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_scene

      Show Scene data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_sound

      Show Sound data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_speaker

      Show Speaker data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_text

      Show Text data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_texture

      Show Texture data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_volume

      Show/hide Volume data-blocks

      :type: boolean, default False

   .. attribute:: experimental_filter_work_space

      Show workspace data-blocks

      :type: boolean, default False

   .. attribute:: filter_action

      Show Action data-blocks

      :type: boolean, default False

   .. attribute:: filter_brush

      Show Brushes data-blocks

      :type: boolean, default False

   .. attribute:: filter_group

      Show Collection data-blocks

      :type: boolean, default False

   .. attribute:: filter_material

      Show Material data-blocks

      :type: boolean, default False

   .. attribute:: filter_node_tree

      Show Node Tree data-blocks

      :type: boolean, default False

   .. attribute:: filter_object

      Show Object data-blocks

      :type: boolean, default False

   .. attribute:: filter_world

      Show World data-blocks

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

   * :class:`FileAssetSelectParams.filter_asset_id`

