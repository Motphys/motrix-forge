GreasePencilBuildModifier(Modifier)
===================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: GreasePencilBuildModifier(Modifier)

   Animate strokes appearing and disappearing

   .. attribute:: concurrent_time_alignment

      How should strokes start to appear/disappear

      * ``START``
        Align Start -- All strokes start at same time (i.e. short strokes finish earlier).
      * ``END``
        Align End -- All strokes end at same time (i.e. short strokes start later).

      :type: enum in [``'START'``, ``'END'``], default ``'START'``

   .. attribute:: fade_factor

      Defines how much of the stroke is fading in/out

      :type: float in [0, 1], default 0.0

   .. attribute:: fade_opacity_strength

      How much strength fading applies on top of stroke opacity

      :type: float in [0, 1], default 0.0

   .. attribute:: fade_thickness_strength

      How much strength fading applies on top of stroke thickness

      :type: float in [0, 1], default 0.0

   .. attribute:: frame_end

      End Frame (when Restrict Frame Range is enabled)

      :type: float in [-1.04857e+06, 1.04857e+06], default 125.0

   .. attribute:: frame_start

      Start Frame (when Restrict Frame Range is enabled)

      :type: float in [-1.04857e+06, 1.04857e+06], default 1.0

   .. attribute:: invert_layer_filter

      Invert layer filter

      :type: boolean, default False

   .. attribute:: invert_layer_pass_filter

      Invert layer pass filter

      :type: boolean, default False

   .. attribute:: invert_material_filter

      Invert material filter

      :type: boolean, default False

   .. attribute:: invert_material_pass_filter

      Invert material pass filter

      :type: boolean, default False

   .. attribute:: layer_pass_filter

      Layer pass filter

      :type: int in [0, 100], default 0

   .. attribute:: length

      Maximum number of frames that the build effect can run for (unless another GP keyframe occurs before this time has elapsed)

      :type: float in [1, 1.04857e+06], default 100.0

   .. attribute:: material_filter

      Material used for filtering

      :type: :class:`Material`

   .. attribute:: material_pass_filter

      Material pass

      :type: int in [0, 100], default 0

   .. attribute:: mode

      How strokes are being built

      * ``SEQUENTIAL``
        Sequential -- Strokes appear/disappear one after the other, but only a single one changes at a time.
      * ``CONCURRENT``
        Concurrent -- Multiple strokes appear/disappear at once.
      * ``ADDITIVE``
        Additive -- Builds only new strokes (assuming 'additive' drawing).

      :type: enum in [``'SEQUENTIAL'``, ``'CONCURRENT'``, ``'ADDITIVE'``], default ``'SEQUENTIAL'``

   .. attribute:: object

      Object used as build starting position

      :type: :class:`Object`

   .. attribute:: open_fading_panel

      :type: boolean, default False

   .. attribute:: open_frame_range_panel

      :type: boolean, default False

   .. attribute:: open_influence_panel

      :type: boolean, default False

   .. attribute:: percentage_factor

      Defines how much of the stroke is visible

      :type: float in [0, 1], default 0.0

   .. attribute:: speed_factor

      Multiply recorded drawing speed by a factor

      :type: float in [0, 100], default 1.2

   .. attribute:: speed_maxgap

      The maximum gap between strokes in seconds

      :type: float in [0, 100], default 0.5

   .. attribute:: start_delay

      Number of frames after each GP keyframe before the modifier has any effect

      :type: float in [0, 1.04857e+06], default 0.0

   .. attribute:: target_vertex_group

      Output Vertex group

      :type: string, default "", (never None)

   .. attribute:: time_mode

      Use drawing speed, a number of frames, or a manual factor to build strokes

      * ``DRAWSPEED``
        Natural Drawing Speed -- Use recorded speed multiplied by a factor.
      * ``FRAMES``
        Number of Frames -- Set a fixed number of frames for all build animations.
      * ``PERCENTAGE``
        Percentage Factor -- Set a manual percentage to build.

      :type: enum in [``'DRAWSPEED'``, ``'FRAMES'``, ``'PERCENTAGE'``], default ``'FRAMES'``

   .. attribute:: transition

      How are strokes animated (i.e. are they appearing or disappearing)

      * ``GROW``
        Grow -- Show points in the order they occur in each stroke (e.g. for animating lines being drawn).
      * ``SHRINK``
        Shrink -- Hide points from the end of each stroke to the start (e.g. for animating lines being erased).
      * ``FADE``
        Vanish -- Hide points in the order they occur in each stroke (e.g. for animating ink fading or vanishing after getting drawn).

      :type: enum in [``'GROW'``, ``'SHRINK'``, ``'FADE'``], default ``'GROW'``

   .. attribute:: tree_node_filter

      Layer name

      :type: string, default "", (never None)

   .. attribute:: use_fading

      Fade out strokes instead of directly cutting off

      :type: boolean, default False

   .. attribute:: use_layer_group_filter

      Filter by layer group name

      :type: boolean, default False

   .. attribute:: use_layer_pass_filter

      Use layer pass filter

      :type: boolean, default False

   .. attribute:: use_material_pass_filter

      Use material pass filter

      :type: boolean, default False

   .. attribute:: use_percentage

      Use a percentage factor to determine the visible points

      :type: boolean, default False

   .. attribute:: use_restrict_frame_range

      Only modify strokes during the specified frame range

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
   * :class:`Modifier.name`
   * :class:`Modifier.type`
   * :class:`Modifier.show_viewport`
   * :class:`Modifier.show_render`
   * :class:`Modifier.show_in_editmode`
   * :class:`Modifier.show_on_cage`
   * :class:`Modifier.show_expanded`
   * :class:`Modifier.is_active`
   * :class:`Modifier.use_pin_to_last`
   * :class:`Modifier.is_override_data`
   * :class:`Modifier.use_apply_on_spline`
   * :class:`Modifier.execution_time`
   * :class:`Modifier.persistent_uid`

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
   * :class:`Modifier.bl_rna_get_subclass`
   * :class:`Modifier.bl_rna_get_subclass_py`

