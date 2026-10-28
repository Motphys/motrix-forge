Scene(ID)
=========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Scene(ID)

   Scene data-block, consisting in objects and defining time and render related settings

   .. attribute:: active_clip

      Active Movie Clip that can be used by motion tracking constraints or as a camera's background image

      :type: :class:`MovieClip`

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: audio_distance_model

      Distance model for distance attenuation calculation

      * ``NONE``
        None -- No distance attenuation.
      * ``INVERSE``
        Inverse -- Inverse distance model.
      * ``INVERSE_CLAMPED``
        Inverse Clamped -- Inverse distance model with clamping.
      * ``LINEAR``
        Linear -- Linear distance model.
      * ``LINEAR_CLAMPED``
        Linear Clamped -- Linear distance model with clamping.
      * ``EXPONENT``
        Exponential -- Exponential distance model.
      * ``EXPONENT_CLAMPED``
        Exponential Clamped -- Exponential distance model with clamping.

      :type: enum in [``'NONE'``, ``'INVERSE'``, ``'INVERSE_CLAMPED'``, ``'LINEAR'``, ``'LINEAR_CLAMPED'``, ``'EXPONENT'``, ``'EXPONENT_CLAMPED'``], default ``'NONE'``

   .. attribute:: audio_doppler_factor

      Pitch factor for Doppler effect calculation

      :type: float in [0, inf], default 1.0

   .. attribute:: audio_doppler_speed

      Speed of sound for Doppler effect calculation

      :type: float in [0.01, inf], default 343.3

   .. attribute:: audio_volume

      Audio volume

      :type: float in [0, 100], default 1.0

   .. attribute:: background_set

      Background set scene

      :type: :class:`Scene`

   .. attribute:: camera

      Active camera, used for rendering the scene

      :type: :class:`Object`

   .. data:: collection

      Scene root collection that owns all the objects and other collections instantiated in the scene

      :type: :class:`Collection`, (readonly, never None)

   .. data:: cursor

      :type: :class:`View3DCursor`, (readonly, never None)

   .. data:: cycles

      Cycles render settings

      :type: :class:`CyclesRenderSettings`, (readonly)

   .. data:: cycles_curves

      Cycles curves rendering settings

      :type: :class:`CyclesCurveRenderSettings`, (readonly)

   .. data:: display

      Scene display settings for 3D viewport

      :type: :class:`SceneDisplay`, (readonly)

   .. data:: display_settings

      Settings of device saved image would be displayed on

      :type: :class:`ColorManagedDisplaySettings`, (readonly)

   .. data:: eevee

      EEVEE settings for the scene

      :type: :class:`SceneEEVEE`, (readonly)

   .. attribute:: frame_current

      Current frame, to update animation data from Python frame_set() instead

      :type: int in [-1048574, 1048574], default 1

   .. data:: frame_current_final

      Current frame with subframe and time remapping applied

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0, (readonly)

   .. attribute:: frame_end

      Final frame of the playback/rendering range

      :type: int in [0, 1048574], default 250

   .. attribute:: frame_float

      :type: float in [-1.04857e+06, 1.04857e+06], default 0.0

   .. attribute:: frame_preview_end

      Alternative end frame for UI playback

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_preview_start

      Alternative start frame for UI playback

      :type: int in [-inf, inf], default 0

   .. attribute:: frame_start

      First frame of the playback/rendering range

      :type: int in [0, 1048574], default 1

   .. attribute:: frame_step

      Number of frames to skip forward while rendering/playing back each frame

      :type: int in [0, 1048574], default 1

   .. attribute:: frame_subframe

      :type: float in [0, 1], default 0.0

   .. attribute:: gravity

      Constant acceleration in a given direction

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, -9.81)

   .. attribute:: grease_pencil

      Grease Pencil data-block used for annotations in the 3D view

      :type: :class:`GreasePencil`

   .. data:: grease_pencil_settings

      Grease Pencil settings for the scene

      :type: :class:`SceneGpencil`, (readonly)

   .. data:: hydra

      Hydra settings for the scene

      :type: :class:`SceneHydra`, (readonly)

   .. data:: is_nla_tweakmode

      Whether there is any action referenced by NLA being edited (strictly read-only)

      :type: boolean, default False, (readonly)

   .. data:: keying_sets

      Absolute Keying Sets for this Scene

      :type: :class:`KeyingSets` :class:`bpy_prop_collection` of :class:`KeyingSet`, (readonly)

   .. data:: keying_sets_all

      All Keying Sets available for use (Builtins and Absolute Keying Sets for this Scene)

      :type: :class:`KeyingSetsAll` :class:`bpy_prop_collection` of :class:`KeyingSet`, (readonly)

   .. attribute:: lock_frame_selection_to_range

      Don't allow frame to be selected with mouse outside of frame range

      :type: boolean, default False

   .. data:: node_tree

      Compositing node tree

      :type: :class:`NodeTree`, (readonly)

   .. data:: objects

      :type: :class:`SceneObjects` :class:`bpy_prop_collection` of :class:`Object`, (readonly)

   .. data:: render

      :type: :class:`RenderSettings`, (readonly, never None)

   .. data:: rigidbody_world

      :type: :class:`RigidBodyWorld`, (readonly)

   .. data:: safe_areas

      :type: :class:`DisplaySafeAreas`, (readonly, never None)

   .. data:: sequence_editor

      :type: :class:`SequenceEditor`, (readonly)

   .. data:: sequencer_colorspace_settings

      Settings of color space sequencer is working in

      :type: :class:`ColorManagedSequencerColorspaceSettings`, (readonly)

   .. attribute:: show_keys_from_selected_only

      Only include channels relating to selected objects and data

      :type: boolean, default True

   .. attribute:: show_subframe

      Display and allow setting fractional frame values for the current frame

      :type: boolean, default False

   .. attribute:: simulation_frame_end

      Frame at which simulations end

      :type: int in [-inf, inf], default 250

   .. attribute:: simulation_frame_start

      Frame at which simulations start

      :type: int in [-inf, inf], default 1

   .. attribute:: sync_mode

      How to sync playback

      * ``NONE``
        Play Every Frame -- Do not sync, play every frame.
      * ``FRAME_DROP``
        Frame Dropping -- Drop frames if playback is too slow.
      * ``AUDIO_SYNC``
        Sync to Audio -- Sync to audio playback, dropping frames.

      :type: enum in [``'NONE'``, ``'FRAME_DROP'``, ``'AUDIO_SYNC'``], default ``'AUDIO_SYNC'``

   .. data:: timeline_markers

      Markers used in all timelines for the current scene

      :type: :class:`TimelineMarkers` :class:`bpy_prop_collection` of :class:`TimelineMarker`, (readonly)

   .. data:: tool_settings

      :type: :class:`ToolSettings`, (readonly, never None)

   .. data:: transform_orientation_slots

      :type: :class:`bpy_prop_collection` of :class:`TransformOrientationSlot`, (readonly)

   .. data:: unit_settings

      Unit editing settings

      :type: :class:`UnitSettings`, (readonly, never None)

   .. attribute:: use_audio

      Play back of audio from Sequence Editor, otherwise mute audio

      :type: boolean, default False

   .. attribute:: use_audio_scrub

      Play audio from Sequence Editor while scrubbing

      :type: boolean, default False

   .. attribute:: use_custom_simulation_range

      Use a simulation range that is different from the scene range for simulation nodes that don't override the frame range themselves

      :type: boolean, default False

   .. attribute:: use_gravity

      Use global gravity for all dynamics

      :type: boolean, default True

   .. attribute:: use_nodes

      Enable the compositing node tree

      :type: boolean, default False

   .. attribute:: use_preview_range

      Use an alternative start/end frame range for animation playback and view renders

      :type: boolean, default False

   .. attribute:: use_stamp_note

      User defined note for the render stamping

      :type: string, default "", (never None)

   .. data:: view_layers

      :type: :class:`ViewLayers` :class:`bpy_prop_collection` of :class:`ViewLayer`, (readonly)

   .. data:: view_settings

      Color management settings applied on image before saving

      :type: :class:`ColorManagedViewSettings`, (readonly)

   .. attribute:: world

      World used for rendering the scene

      :type: :class:`World`

   .. classmethod:: update_render_engine()

      Trigger a render engine update


   .. method:: statistics(view_layer)

      statistics

      :arg view_layer: View Layer
      :type view_layer: :class:`ViewLayer`, (never None)
      :return: Statistics
      :rtype: string, (never None)

   .. method:: frame_set(frame, *, subframe=0.0)

      Set scene frame updating all objects and view layers immediately

      :arg frame: Frame number to set
      :type frame: int in [-1048574, 1048574]
      :arg subframe: Subframe time, between 0.0 and 1.0
      :type subframe: float in [0, 1], (optional)

   .. method:: uvedit_aspect(object)

      Get uv aspect for current object

      :arg object: Object
      :type object: :class:`Object`, (never None)
      :return: aspect
      :rtype: :class:`mathutils.Vector` of 2 items in [0, inf]

   .. method:: ray_cast(depsgraph, origin, direction, *, distance=1.70141e+38)

      Cast a ray onto evaluated geometry in world-space

      :arg depsgraph: The current dependency graph
      :type depsgraph: :class:`Depsgraph`, (never None)
      :type origin: :class:`mathutils.Vector` of 3 items in [-inf, inf]
      :type direction: :class:`mathutils.Vector` of 3 items in [-inf, inf]
      :arg distance: Maximum distance
      :type distance: float in [0, inf], (optional)
      :return:
         `result`, boolean

         `location`, The hit location of this ray cast, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `normal`, The face normal at the ray cast hit location, :class:`mathutils.Vector` of 3 items in [-inf, inf]

         `index`, The face index, -1 when original data isn't available, int in [-inf, inf]

         `object`, Ray cast object, :class:`Object`

         `matrix`, Matrix, :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]

      :rtype: (boolean, :class:`mathutils.Vector` of 3 items in [-inf, inf], :class:`mathutils.Vector` of 3 items in [-inf, inf], int in [-inf, inf], :class:`Object`, :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf])

   .. method:: sequence_editor_create()

      Ensure sequence editor is valid in this scene

      :return: New sequence editor data or nullptr
      :rtype: :class:`SequenceEditor`

   .. method:: sequence_editor_clear()

      Clear sequence editor in this scene


   .. method:: alembic_export(filepath, *, frame_start=1, frame_end=1, xform_samples=1, geom_samples=1, shutter_open=0.0, shutter_close=1.0, selected_only=False, uvs=True, normals=True, vcolors=False, apply_subdiv=True, flatten=False, visible_objects_only=False, face_sets=False, subdiv_schema=False, export_hair=True, export_particles=True, packuv=False, scale=1.0, triangulate=False, quad_method='BEAUTY', ngon_method='BEAUTY')

      Export to Alembic file (deprecated, use the Alembic export operator)

      :arg filepath: File Path, File path to write Alembic file
      :type filepath: string, (never None)
      :arg frame_start: Start, Start Frame
      :type frame_start: int in [-inf, inf], (optional)
      :arg frame_end: End, End Frame
      :type frame_end: int in [-inf, inf], (optional)
      :arg xform_samples: Xform samples, Transform samples per frame
      :type xform_samples: int in [1, 128], (optional)
      :arg geom_samples: Geom samples, Geometry samples per frame
      :type geom_samples: int in [1, 128], (optional)
      :arg shutter_open: Shutter open
      :type shutter_open: float in [-1, 1], (optional)
      :arg shutter_close: Shutter close
      :type shutter_close: float in [-1, 1], (optional)
      :arg selected_only: Selected only, Export only selected objects
      :type selected_only: boolean, (optional)
      :arg uvs: UVs, Export UVs
      :type uvs: boolean, (optional)
      :arg normals: Normals, Export normals
      :type normals: boolean, (optional)
      :arg vcolors: Color Attributes, Export color attributes
      :type vcolors: boolean, (optional)
      :arg apply_subdiv: Subsurfs as meshes, Export subdivision surfaces as meshes
      :type apply_subdiv: boolean, (optional)
      :arg flatten: Flatten hierarchy, Flatten hierarchy
      :type flatten: boolean, (optional)
      :arg visible_objects_only: Visible layers only, Export only objects in visible layers
      :type visible_objects_only: boolean, (optional)
      :arg face_sets: Facesets, Export face sets
      :type face_sets: boolean, (optional)
      :arg subdiv_schema: Use Alembic subdivision Schema, Use Alembic subdivision Schema
      :type subdiv_schema: boolean, (optional)
      :arg export_hair: Export Hair, Exports hair particle systems as animated curves
      :type export_hair: boolean, (optional)
      :arg export_particles: Export Particles, Exports non-hair particle systems
      :type export_particles: boolean, (optional)
      :arg packuv: Export with packed UV islands, Export with packed UV islands
      :type packuv: boolean, (optional)
      :arg scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
      :type scale: float in [0.0001, 1000], (optional)
      :arg triangulate: Triangulate, Export polygons (quads and n-gons) as triangles
      :type triangulate: boolean, (optional)
      :arg quad_method: Quad Method, Method for splitting the quads into triangles
      :type quad_method: enum in :ref:`rna_enum_modifier_triangulate_quad_method_items`, (optional)
      :arg ngon_method: N-gon Method, Method for splitting the n-gons into triangles
      :type ngon_method: enum in :ref:`rna_enum_modifier_triangulate_ngon_method_items`, (optional)

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
   * :class:`ID.name`
   * :class:`ID.name_full`
   * :class:`ID.id_type`
   * :class:`ID.session_uid`
   * :class:`ID.is_evaluated`
   * :class:`ID.original`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.use_extra_user`
   * :class:`ID.is_embedded_data`
   * :class:`ID.is_missing`
   * :class:`ID.is_runtime_data`
   * :class:`ID.is_editable`
   * :class:`ID.tag`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.library_weak_reference`
   * :class:`ID.asset_data`
   * :class:`ID.override_library`
   * :class:`ID.preview`

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
   * :class:`ID.rename`
   * :class:`ID.evaluated_get`
   * :class:`ID.copy`
   * :class:`ID.asset_mark`
   * :class:`ID.asset_clear`
   * :class:`ID.asset_generate_preview`
   * :class:`ID.override_create`
   * :class:`ID.override_hierarchy_create`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`
   * :class:`ID.preview_ensure`
   * :class:`ID.bl_rna_get_subclass`
   * :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :mod:`bpy.context.scene`
   * :class:`BlendData.scenes`
   * :class:`BlendDataScenes.new`
   * :class:`BlendDataScenes.remove`
   * :class:`Camera.view_frame`
   * :class:`CompositorNodeCryptomatteV2.scene`
   * :class:`CompositorNodeDefocus.scene`
   * :class:`CompositorNodeRLayers.scene`
   * :class:`Context.scene`
   * :class:`Depsgraph.scene`
   * :class:`Depsgraph.scene_eval`
   * :class:`ID.override_hierarchy_create`
   * :class:`IDOverrideLibrary.resync`
   * :class:`Image.save_render`
   * :class:`Object.crazyspace_eval`
   * :class:`Object.is_deform_modified`
   * :class:`Object.is_modified`
   * :class:`RenderEngine.bind_display_space_shader`
   * :class:`RenderEngine.get_preview_pixel_size`
   * :class:`RenderEngine.register_pass`
   * :class:`RenderEngine.support_display_space_shader`
   * :class:`RenderEngine.update_render_passes`
   * :class:`Scene.background_set`
   * :class:`SceneStrip.scene`
   * :class:`StripsMeta.new_scene`
   * :class:`StripsTopLevel.new_scene`
   * :class:`Window.scene`

