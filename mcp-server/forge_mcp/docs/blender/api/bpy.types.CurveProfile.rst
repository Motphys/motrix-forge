CurveProfile(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CurveProfile(bpy_struct)

   Profile Path editor used to build a profile path

   .. data:: points

      Profile control points

      :type: :class:`CurveProfilePoints` :class:`bpy_prop_collection` of :class:`CurveProfilePoint`, (readonly)

   .. attribute:: preset

      * ``LINE``
        Line -- Default.
      * ``SUPPORTS``
        Support Loops -- Loops on each side of the profile.
      * ``CORNICE``
        Cornice Molding.
      * ``CROWN``
        Crown Molding.
      * ``STEPS``
        Steps -- A number of steps defined by the segments.

      :type: enum in [``'LINE'``, ``'SUPPORTS'``, ``'CORNICE'``, ``'CROWN'``, ``'STEPS'``], default ``'LINE'``

   .. data:: segments

      Segments sampled from control points

      :type: :class:`bpy_prop_collection` of :class:`CurveProfilePoint`, (readonly)

   .. attribute:: use_clip

      Force the path view to fit a defined boundary

      :type: boolean, default False

   .. attribute:: use_sample_even_lengths

      Sample edges with even lengths

      :type: boolean, default False

   .. attribute:: use_sample_straight_edges

      Sample edges with vector handles

      :type: boolean, default False

   .. method:: update()

      Refresh internal data, remove doubles and clip points


   .. method:: reset_view()

      Reset the curve profile grid to its clipping size


   .. method:: initialize(totsegments)

      Set the number of display segments and fill tables

      :arg totsegments: The number of segment values to initialize the segments table with
      :type totsegments: int in [1, 1000], (never None)

   .. method:: evaluate(length_portion)

      Evaluate the at the given portion of the path length

      :arg length_portion: Length Portion, Portion of the path length to travel before evaluation
      :type length_portion: float in [0, 1]
      :return: Location, The location at the given portion of the profile
      :rtype: :class:`mathutils.Vector` of 2 items in [-100, 100]

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

   * :class:`BevelModifier.custom_profile`
   * :class:`Curve.bevel_profile`
   * :class:`ToolSettings.custom_bevel_profile_preset`

