SpaceDopeSheetEditor(Space)
===========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceDopeSheetEditor(Space)

   Dope Sheet space data

   .. attribute:: action

      Action displayed and edited in this space

      :type: :class:`Action`

   .. attribute:: cache_cloth

      Show the active object's cloth point cache

      :type: boolean, default False

   .. attribute:: cache_dynamicpaint

      Show the active object's Dynamic Paint cache

      :type: boolean, default False

   .. attribute:: cache_particles

      Show the active object's particle point cache

      :type: boolean, default False

   .. attribute:: cache_rigidbody

      Show the active object's Rigid Body cache

      :type: boolean, default False

   .. attribute:: cache_simulation_nodes

      Show the active object's simulation nodes cache and bake data

      :type: boolean, default False

   .. attribute:: cache_smoke

      Show the active object's smoke cache

      :type: boolean, default False

   .. attribute:: cache_softbody

      Show the active object's softbody point cache

      :type: boolean, default False

   .. data:: dopesheet

      Settings for filtering animation data

      :type: :class:`DopeSheet`, (readonly)

   .. attribute:: mode

      Editing context being displayed

      * ``DOPESHEET``
        Dope Sheet -- Edit all keyframes in scene.
      * ``TIMELINE``
        Timeline -- Timeline and playback controls.
      * ``ACTION``
        Action Editor -- Edit keyframes in active object's Object-level action.
      * ``SHAPEKEY``
        Shape Key Editor -- Edit keyframes in active object's Shape Keys action.
      * ``GPENCIL``
        Grease Pencil -- Edit timings for all Grease Pencil sketches in file.
      * ``MASK``
        Mask -- Edit timings for Mask Editor splines.
      * ``CACHEFILE``
        Cache File -- Edit timings for Cache File data-blocks.

      :type: enum in [``'DOPESHEET'``, ``'TIMELINE'``, ``'ACTION'``, ``'SHAPEKEY'``, ``'GPENCIL'``, ``'MASK'``, ``'CACHEFILE'``], default ``'ACTION'``

   .. attribute:: show_cache

      Show the status of cached frames in the timeline

      :type: boolean, default False

   .. attribute:: show_extremes

      Mark keyframes where the key value flow changes direction, based on comparison with adjacent keys

      :type: boolean, default False

   .. attribute:: show_interpolation

      Display keyframe handle types and non-Bézier interpolation modes

      :type: boolean, default False

   .. attribute:: show_markers

      If any exists, show markers in a separate row at the bottom of the editor

      :type: boolean, default False

   .. attribute:: show_pose_markers

      Show markers belonging to the active action instead of Scene markers (Action and Shape Key Editors only)

      :type: boolean, default False

   .. attribute:: show_region_channels

      :type: boolean, default False

   .. attribute:: show_region_hud

      :type: boolean, default False

   .. attribute:: show_region_ui

      :type: boolean, default False

   .. attribute:: show_seconds

      Show timing as a timecode instead of frames

      :type: boolean, default False

   .. attribute:: show_sliders

      Show sliders beside F-Curve channels

      :type: boolean, default False

   .. attribute:: ui_mode

      Editing context being displayed

      * ``DOPESHEET``
        Dope Sheet -- Edit all keyframes in scene.
      * ``ACTION``
        Action Editor -- Edit keyframes in active object's Object-level action.
      * ``SHAPEKEY``
        Shape Key Editor -- Edit keyframes in active object's Shape Keys action.
      * ``GPENCIL``
        Grease Pencil -- Edit timings for all Grease Pencil sketches in file.
      * ``MASK``
        Mask -- Edit timings for Mask Editor splines.
      * ``CACHEFILE``
        Cache File -- Edit timings for Cache File data-blocks.

      :type: enum in [``'DOPESHEET'``, ``'ACTION'``, ``'SHAPEKEY'``, ``'GPENCIL'``, ``'MASK'``, ``'CACHEFILE'``], default ``'ACTION'``

   .. attribute:: use_auto_merge_keyframes

      Automatically merge nearby keyframes

      :type: boolean, default False

   .. attribute:: use_marker_sync

      Sync Markers with keyframe edits

      :type: boolean, default False

   .. attribute:: use_realtime_update

      When transforming keyframes, changes to the animation data are flushed to other views

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


   .. classmethod:: draw_handler_add(callback, args, region_type, draw_type)
   
      Add a new draw handler to this space type.
      It will be called every time the specified region in the space type will be drawn.
      Note: All arguments are positional only for now.
   
      :arg callback:
         A function that will be called when the region is drawn.
         It gets the specified arguments as input, it's return value is ignored.
      :type callback: Callable[..., Any]
      :arg args: Arguments that will be passed to the callback.
      :type args: tuple[Any, ...]
      :arg region_type: The region type the callback draws in; usually ``WINDOW``. (:class:`bpy.types.Region.type`)
      :type region_type: str
      :arg draw_type: Usually ``POST_PIXEL`` for 2D drawing and ``POST_VIEW`` for 3D drawing. In some cases ``PRE_VIEW`` can be used. ``BACKDROP`` can be used for backdrops in the node editor.
      :type draw_type: str
      :return: Handler that can be removed later on.
      :rtype: object


   .. classmethod:: draw_handler_remove(handler, region_type)
   
      Remove a draw handler that was added previously.
   
      :arg handler: The draw handler that should be removed.
      :type handler: object
      :arg region_type: Region type the callback was added to.
      :type region_type: str


Inherited Properties
--------------------

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Space.type`
   * :class:`Space.show_locked_time`
   * :class:`Space.show_region_header`

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
   * :class:`Space.bl_rna_get_subclass`
   * :class:`Space.bl_rna_get_subclass_py`
   * :class:`Space.draw_handler_add`
   * :class:`Space.draw_handler_remove`

