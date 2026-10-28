SpaceProperties(Space)
======================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Space`

.. class:: SpaceProperties(Space)

   Properties space data

   .. attribute:: context

      * ``TOOL``
        Tool -- Active Tool and Workspace settings.
      * ``SCENE``
        Scene -- Scene Properties.
      * ``RENDER``
        Render -- Render Properties.
      * ``OUTPUT``
        Output -- Output Properties.
      * ``VIEW_LAYER``
        View Layer -- View Layer Properties.
      * ``WORLD``
        World -- World Properties.
      * ``COLLECTION``
        Collection -- Collection Properties.
      * ``OBJECT``
        Object -- Object Properties.
      * ``CONSTRAINT``
        Constraints -- Object Constraint Properties.
      * ``MODIFIER``
        Modifiers -- Modifier Properties.
      * ``DATA``
        Data -- Object Data Properties.
      * ``BONE``
        Bone -- Bone Properties.
      * ``BONE_CONSTRAINT``
        Bone Constraints -- Bone Constraint Properties.
      * ``MATERIAL``
        Material -- Material Properties.
      * ``TEXTURE``
        Texture -- Texture Properties.
      * ``PARTICLES``
        Particles -- Particle Properties.
      * ``PHYSICS``
        Physics -- Physics Properties.
      * ``SHADERFX``
        Effects -- Visual Effects Properties.

      :type: enum in [``'TOOL'``, ``'SCENE'``, ``'RENDER'``, ``'OUTPUT'``, ``'VIEW_LAYER'``, ``'WORLD'``, ``'COLLECTION'``, ``'OBJECT'``, ``'CONSTRAINT'``, ``'MODIFIER'``, ``'DATA'``, ``'BONE'``, ``'BONE_CONSTRAINT'``, ``'MATERIAL'``, ``'TEXTURE'``, ``'PARTICLES'``, ``'PHYSICS'``, ``'SHADERFX'``], default ``'RENDER'``

   .. attribute:: outliner_sync

      Change to the corresponding tab when outliner data icons are clicked

      * ``ALWAYS``
        Always -- Always change tabs when clicking an icon in an outliner.
      * ``NEVER``
        Never -- Never change tabs when clicking an icon in an outliner.
      * ``AUTO``
        Auto -- Change tabs only when this editor shares a border with an outliner.

      :type: enum in [``'ALWAYS'``, ``'NEVER'``, ``'AUTO'``], default ``'AUTO'``

   .. attribute:: pin_id

      :type: :class:`ID`

   .. attribute:: search_filter

      Live search filtering string

      :type: string, default "", (never None)

   .. attribute:: show_properties_bone

      :type: boolean, default False

   .. attribute:: show_properties_bone_constraints

      :type: boolean, default False

   .. attribute:: show_properties_collection

      :type: boolean, default False

   .. attribute:: show_properties_constraints

      :type: boolean, default False

   .. attribute:: show_properties_data

      :type: boolean, default False

   .. attribute:: show_properties_effects

      :type: boolean, default False

   .. attribute:: show_properties_material

      :type: boolean, default False

   .. attribute:: show_properties_modifiers

      :type: boolean, default False

   .. attribute:: show_properties_object

      :type: boolean, default False

   .. attribute:: show_properties_output

      :type: boolean, default False

   .. attribute:: show_properties_particles

      :type: boolean, default False

   .. attribute:: show_properties_physics

      :type: boolean, default False

   .. attribute:: show_properties_render

      :type: boolean, default False

   .. attribute:: show_properties_scene

      :type: boolean, default False

   .. attribute:: show_properties_texture

      :type: boolean, default False

   .. attribute:: show_properties_tool

      :type: boolean, default False

   .. attribute:: show_properties_view_layer

      :type: boolean, default False

   .. attribute:: show_properties_world

      :type: boolean, default False

   .. data:: tab_search_results

      Whether or not each visible tab has a search result

      :type: boolean, default False, (readonly)

   .. attribute:: use_pin_id

      Use the pinned context

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

