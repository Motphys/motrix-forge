PointCache(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: PointCache(bpy_struct)

   Active point cache for physics simulations

   .. attribute:: compression

      Compression method to be used

      * ``NO``
        None -- No compression.
      * ``LIGHT``
        Lite -- Fast but not so effective compression.
      * ``HEAVY``
        Heavy -- Effective but slow compression.

      :type: enum in [``'NO'``, ``'LIGHT'``, ``'HEAVY'``], default ``'NO'``

   .. attribute:: filepath

      Cache file path

      :type: string, default "", (never None, blend relative ``//`` prefix supported)

   .. attribute:: frame_end

      Frame on which the simulation stops

      :type: int in [1, 1048574], default 0

   .. attribute:: frame_start

      Frame on which the simulation starts

      :type: int in [-1048574, 1048574], default 0

   .. attribute:: frame_step

      Number of frames between cached frames

      :type: int in [1, 20], default 0

   .. attribute:: index

      Index number of cache files

      :type: int in [-1, 100], default 0

   .. data:: info

      Info on current cache status

      :type: string, default "", (readonly, never None)

   .. data:: is_baked

      The cache is baked

      :type: boolean, default False, (readonly)

   .. data:: is_baking

      The cache is being baked

      :type: boolean, default False, (readonly)

   .. data:: is_frame_skip

      Some frames were skipped while baking/saving that cache

      :type: boolean, default False, (readonly)

   .. data:: is_outdated

      :type: boolean, default False, (readonly)

   .. attribute:: name

      Cache name

      :type: string, default "", (never None)

   .. data:: point_caches

      :type: :class:`PointCaches` :class:`bpy_prop_collection` of :class:`PointCacheItem`, (readonly)

   .. attribute:: use_disk_cache

      Save cache files to disk (.blend file must be saved first)

      :type: boolean, default False

   .. attribute:: use_external

      Read cache from an external location

      :type: boolean, default False

   .. attribute:: use_library_path

      Use this file's path for the disk cache when library linked into another file (for local bakes per scene file, disable this option)

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

   * :class:`ClothModifier.point_cache`
   * :class:`DynamicPaintSurface.point_cache`
   * :class:`ParticleSystem.point_cache`
   * :class:`RigidBodyWorld.point_cache`
   * :class:`SoftBodyModifier.point_cache`

