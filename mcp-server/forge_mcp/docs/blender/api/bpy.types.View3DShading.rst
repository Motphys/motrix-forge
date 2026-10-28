View3DShading(bpy_struct)
=========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: View3DShading(bpy_struct)

   Settings for shading in the 3D viewport

   .. attribute:: aov_name

      Name of the active Shader AOV

      :type: string, default "", (never None)

   .. attribute:: background_color

      Color for custom background color

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.05, 0.05, 0.05)

   .. attribute:: background_type

      Way to display the background

      * ``THEME``
        Theme -- Use the theme for background color.
      * ``WORLD``
        World -- Use the world for background color.
      * ``VIEWPORT``
        Custom -- Use a custom color limited to this viewport only.

      :type: enum in [``'THEME'``, ``'WORLD'``, ``'VIEWPORT'``], default ``'THEME'``

   .. attribute:: cavity_ridge_factor

      Factor for the cavity ridges

      :type: float in [0, 250], default 1.0

   .. attribute:: cavity_type

      Way to display the cavity shading

      * ``WORLD``
        World -- Cavity shading computed in world space, useful for larger-scale occlusion.
      * ``SCREEN``
        Screen -- Curvature-based shading, useful for making fine details more visible.
      * ``BOTH``
        Both -- Use both effects simultaneously.

      :type: enum in [``'WORLD'``, ``'SCREEN'``, ``'BOTH'``], default ``'SCREEN'``

   .. attribute:: cavity_valley_factor

      Factor for the cavity valleys

      :type: float in [0, 250], default 1.0

   .. attribute:: color_type

      Color Type

      * ``MATERIAL``
        Material -- Show material color.
      * ``OBJECT``
        Object -- Show object color.
      * ``RANDOM``
        Random -- Show random object color.
      * ``VERTEX``
        Attribute -- Show active color attribute.
      * ``TEXTURE``
        Texture -- Show the texture from the active image texture node using the active UV map coordinates.
      * ``SINGLE``
        Custom -- Show scene in a single custom color.

      :type: enum in [``'MATERIAL'``, ``'OBJECT'``, ``'RANDOM'``, ``'VERTEX'``, ``'TEXTURE'``, ``'SINGLE'``], default ``'MATERIAL'``

   .. attribute:: curvature_ridge_factor

      Factor for the curvature ridges

      :type: float in [0, 2], default 1.0

   .. attribute:: curvature_valley_factor

      Factor for the curvature valleys

      :type: float in [0, 2], default 1.0

   .. data:: cycles

      :type: :class:`CyclesView3DShadingSettings`, (readonly)

   .. attribute:: light

      Lighting Method for Solid/Texture Viewport Shading

      * ``STUDIO``
        Studio -- Display using studio lighting.
      * ``MATCAP``
        MatCap -- Display using matcap material and lighting.
      * ``FLAT``
        Flat -- Display using flat lighting.

      :type: enum in [``'STUDIO'``, ``'MATCAP'``, ``'FLAT'``], default ``'STUDIO'``

   .. attribute:: object_outline_color

      Color for object outline

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: render_pass

      Render Pass to show in the viewport

      :type: enum in [``'COMBINED'``, ``'EMISSION'``, ``'ENVIRONMENT'``, ``'AO'``, ``'SHADOW'``, ``'TRANSPARENT'``, ``'DIFFUSE_LIGHT'``, ``'DIFFUSE_COLOR'``, ``'SPECULAR_LIGHT'``, ``'SPECULAR_COLOR'``, ``'VOLUME_LIGHT'``, ``'POSITION'``, ``'NORMAL'``, ``'MIST'``, ``'CryptoObject'``, ``'CryptoAsset'``, ``'CryptoMaterial'``, ``'AOV'``], default ``'COMBINED'``

   .. data:: selected_studio_light

      Selected StudioLight

      :type: :class:`StudioLight`, (readonly)

   .. attribute:: shadow_intensity

      Darkness of shadows

      :type: float in [0, 1], default 0.5

   .. attribute:: show_backface_culling

      Use back face culling to hide the back side of faces

      :type: boolean, default False

   .. attribute:: show_cavity

      Show Cavity

      :type: boolean, default False

   .. attribute:: show_object_outline

      Show Object Outline

      :type: boolean, default False

   .. attribute:: show_shadows

      Show Shadow

      :type: boolean, default False

   .. attribute:: show_specular_highlight

      Render specular highlights

      :type: boolean, default True

   .. attribute:: show_xray

      Show whole scene transparent

      :type: boolean, default False

   .. attribute:: show_xray_wireframe

      Show whole scene transparent

      :type: boolean, default True

   .. attribute:: single_color

      Color for single color mode

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.8, 0.8, 0.8)

   .. attribute:: studio_light

      Studio lighting setup

      :type: enum in [``'DEFAULT'``], default ``'DEFAULT'``

   .. attribute:: studiolight_background_alpha

      Show the studiolight in the background

      :type: float in [0, 1], default 0.0

   .. attribute:: studiolight_background_blur

      Blur the studiolight in the background

      :type: float in [0, 1], default 0.5

   .. attribute:: studiolight_intensity

      Strength of the studiolight

      :type: float in [0, inf], default 1.0

   .. attribute:: studiolight_rotate_z

      Rotation of the studiolight around the Z-Axis

      :type: float in [-3.14159, 3.14159], default 0.0

   .. attribute:: type

      Method to display/shade objects in the 3D View

      :type: enum in :ref:`rna_enum_shading_type_items`, default ``'SOLID'``

   .. attribute:: use_compositor

      When to preview the compositor output inside the viewport

      * ``DISABLED``
        Disabled -- The compositor is disabled.
      * ``CAMERA``
        Camera -- The compositor is enabled only in camera view.
      * ``ALWAYS``
        Always -- The compositor is always enabled regardless of the view.

      :type: enum in [``'DISABLED'``, ``'CAMERA'``, ``'ALWAYS'``], default ``'DISABLED'``

   .. attribute:: use_dof

      Use depth of field on viewport using the values from the active camera

      :type: boolean, default False

   .. attribute:: use_scene_lights

      Render lights and light probes of the scene

      :type: boolean, default False

   .. attribute:: use_scene_lights_render

      Render lights and light probes of the scene

      :type: boolean, default True

   .. attribute:: use_scene_world

      Use scene world for lighting

      :type: boolean, default False

   .. attribute:: use_scene_world_render

      Use scene world for lighting

      :type: boolean, default True

   .. attribute:: use_studiolight_view_rotation

      Make the HDR rotation fixed and not follow the camera

      :type: boolean, default True

   .. attribute:: use_world_space_lighting

      Make the lighting fixed and not follow the camera

      :type: boolean, default False

   .. attribute:: wireframe_color_type

      Wire Color Type

      * ``THEME``
        Theme -- Show scene wireframes with the theme's wire color.
      * ``OBJECT``
        Object -- Show object color on wireframe.
      * ``RANDOM``
        Random -- Show random object color on wireframe.

      :type: enum in [``'THEME'``, ``'OBJECT'``, ``'RANDOM'``], default ``'THEME'``

   .. attribute:: xray_alpha

      Amount of opacity to use

      :type: float in [0, 1], default 0.5

   .. attribute:: xray_alpha_wireframe

      Amount of opacity to use

      :type: float in [0, 1], default 0.5

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

   * :class:`SceneDisplay.shading`
   * :class:`SpaceView3D.shading`
   * :class:`XrSessionSettings.shading`

