Region(bpy_struct)
==================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Region(bpy_struct)

   Region in a subdivided screen area

   .. attribute:: active_panel_category

      The current active panel category, may be Null if the region does not support this feature (NOTE: these categories are generated at runtime, so list may be empty at initialization, before any drawing took place)

      * ``UNSUPPORTED``
        Not Supported -- This region does not support panel categories.

      :type: enum in [``'UNSUPPORTED'``], default ``'UNSUPPORTED'``

   .. data:: alignment

      Alignment of the region within the area

      * ``NONE``
        None -- Don't use any fixed alignment, fill available space.
      * ``TOP``
        Top.
      * ``BOTTOM``
        Bottom.
      * ``LEFT``
        Left.
      * ``RIGHT``
        Right.
      * ``HORIZONTAL_SPLIT``
        Horizontal Split.
      * ``VERTICAL_SPLIT``
        Vertical Split.
      * ``FLOAT``
        Float -- Region floats on screen, doesn't use any fixed alignment.
      * ``QUAD_SPLIT``
        Quad Split -- Region is split horizontally and vertically.

      :type: enum in [``'NONE'``, ``'TOP'``, ``'BOTTOM'``, ``'LEFT'``, ``'RIGHT'``, ``'HORIZONTAL_SPLIT'``, ``'VERTICAL_SPLIT'``, ``'FLOAT'``, ``'QUAD_SPLIT'``], default ``'NONE'``, (readonly)

   .. data:: data

      Region specific data (the type depends on the region type)

      :type: :class:`AnyType`, (readonly)

   .. data:: height

      Region height

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: type

      Type of this region

      :type: enum in :ref:`rna_enum_region_type_items`, default ``'WINDOW'``, (readonly)

   .. data:: view2d

      2D view of the region

      :type: :class:`View2D`, (readonly, never None)

   .. data:: width

      Region width

      :type: int in [0, 32767], default 0, (readonly)

   .. data:: x

      The window relative vertical location of the region

      :type: int in [-inf, inf], default 0, (readonly)

   .. data:: y

      The window relative horizontal location of the region

      :type: int in [-inf, inf], default 0, (readonly)

   .. method:: tag_redraw()

      tag_redraw


   .. method:: tag_refresh_ui()

      tag_refresh_ui


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

   * :class:`Area.regions`
   * :class:`Context.region`
   * :class:`Context.region_popup`

