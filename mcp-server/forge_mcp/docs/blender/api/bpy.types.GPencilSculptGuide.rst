GPencilSculptGuide(bpy_struct)
==============================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilSculptGuide(bpy_struct)

   Guides for drawing

   .. attribute:: angle

      Direction of lines

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: angle_snap

      Angle snapping

      :type: float in [-6.28319, 6.28319], default 0.0

   .. attribute:: location

      Custom reference point for guides

      :type: float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: reference_object

      Object used for reference point

      :type: :class:`Object`

   .. attribute:: reference_point

      Type of speed guide

      * ``CURSOR``
        Cursor -- Use cursor as reference point.
      * ``CUSTOM``
        Custom -- Use custom reference point.
      * ``OBJECT``
        Object -- Use object as reference point.

      :type: enum in [``'CURSOR'``, ``'CUSTOM'``, ``'OBJECT'``], default ``'CURSOR'``

   .. attribute:: spacing

      Guide spacing

      :type: float in [0, inf], default 20.0

   .. attribute:: type

      Type of speed guide

      * ``CIRCULAR``
        Circular -- Use single point to create rings.
      * ``RADIAL``
        Radial -- Use single point as direction.
      * ``PARALLEL``
        Parallel -- Parallel lines.
      * ``GRID``
        Grid -- Grid allows horizontal and vertical lines.
      * ``ISO``
        Isometric -- Grid allows isometric and vertical lines.

      :type: enum in [``'CIRCULAR'``, ``'RADIAL'``, ``'PARALLEL'``, ``'GRID'``, ``'ISO'``], default ``'CIRCULAR'``

   .. attribute:: use_guide

      Enable speed guides

      :type: boolean, default False

   .. attribute:: use_snapping

      Enable snapping to guides angle or spacing options

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

   * :class:`GPencilSculptSettings.guide`

