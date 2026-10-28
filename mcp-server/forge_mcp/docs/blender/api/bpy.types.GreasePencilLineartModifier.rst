GreasePencilLineartModifier(Modifier)
=====================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Modifier`

.. class:: GreasePencilLineartModifier(Modifier)

   Generate Line Art strokes from selected source

   .. attribute:: chaining_image_threshold

      Segments with an image distance smaller than this will be chained together

      :type: float in [0, 0.3], default 0.001

   .. attribute:: crease_threshold

      Angles smaller than this will be treated as creases. Crease angle priority: object Line Art crease override > mesh auto smooth angle > Line Art default crease.

      :type: float in [0, 3.14159], default 2.44346

   .. attribute:: invert_source_vertex_group

      Invert source vertex group values

      :type: boolean, default False

   .. attribute:: is_baked

      This modifier has baked data

      :type: boolean, default False

   .. attribute:: level_end

      Maximum number of occlusions for the generated strokes

      :type: int in [0, 128], default 0

   .. attribute:: level_start

      Minimum number of occlusions for the generated strokes

      :type: int in [0, 128], default 0

   .. attribute:: light_contour_object

      Use this light object to generate light contour

      :type: :class:`Object`

   .. attribute:: opacity

      The strength value for the generate strokes

      :type: float in [0, 1], default 1.0

   .. attribute:: overscan

      A margin to prevent strokes from ending abruptly at the edge of the image

      :type: float in [0, 0.5], default 0.1

   .. attribute:: radius

      The radius for the generated strokes

      :type: float in [0, 1], default 0.0025

   .. attribute:: shadow_camera_far

      Far clipping distance of shadow camera

      :type: float in [0, 10000], default 200.0

   .. attribute:: shadow_camera_near

      Near clipping distance of shadow camera

      :type: float in [0, 10000], default 0.1

   .. attribute:: shadow_camera_size

      Represents the "Orthographic Scale" of an orthographic camera. If the camera is positioned at the light's location with this scale, it will represent the coverage of the shadow "camera".

      :type: float in [0, 10000], default 200.0

   .. attribute:: shadow_region_filtering

      Select feature lines that comes from lit or shaded regions. Will not affect cast shadow and light contour since they are at the border.

      * ``NONE``
        None -- Not filtering any lines based on illumination region.
      * ``ILLUMINATED``
        Illuminated -- Only selecting lines from illuminated regions.
      * ``SHADED``
        Shaded -- Only selecting lines from shaded regions.
      * ``ILLUMINATED_ENCLOSED``
        Illuminated (Enclosed Shapes) -- Selecting lines from lit regions, and make the combination of contour, light contour and shadow lines into enclosed shapes.

      :type: enum in [``'NONE'``, ``'ILLUMINATED'``, ``'SHADED'``, ``'ILLUMINATED_ENCLOSED'``], default ``'NONE'``

   .. attribute:: silhouette_filtering

      Select contour or silhouette

      :type: enum in [``'NONE'``, ``'GROUP'``, ``'INDIVIDUAL'``], default ``'NONE'``

   .. attribute:: smooth_tolerance

      Strength of smoothing applied on jagged chains

      :type: float in [0, 30], default 0.0

   .. attribute:: source_camera

      Use specified camera object for generating Line Art strokes

      :type: :class:`Object`

   .. attribute:: source_collection

      Generate strokes from the objects in this collection

      :type: :class:`Collection`

   .. attribute:: source_object

      Generate strokes from this object

      :type: :class:`Object`

   .. attribute:: source_type

      Line Art stroke source type

      :type: enum in [``'COLLECTION'``, ``'OBJECT'``, ``'SCENE'``], default ``'COLLECTION'``

   .. attribute:: source_vertex_group

      Match the beginning of vertex group names from mesh objects, match all when left empty

      :type: string, default "", (never None)

   .. attribute:: split_angle

      Angle in screen space below which a stroke is split in two

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: stroke_depth_offset

      Move strokes slightly towards the camera to avoid clipping while preserve depth for the viewport

      :type: float in [-0.1, inf], default 0.05

   .. attribute:: target_layer

      Grease Pencil layer to which assign the generated strokes

      :type: string, default "", (never None)

   .. attribute:: target_material

      Grease Pencil material assigned to the generated strokes

      :type: :class:`Material`

   .. attribute:: thickness

      The thickness for the generated strokes

      :type: int in [1, 200], default 25

   .. attribute:: use_back_face_culling

      Remove all back faces to speed up calculation, this will create edges in different occlusion levels than when disabled

      :type: boolean, default False

   .. attribute:: use_cache

      Use cached scene data from the first Line Art modifier in the stack. Certain settings will be unavailable.

      :type: boolean, default False

   .. attribute:: use_clip_plane_boundaries

      Allow lines generated by the near/far clipping plane to be shown

      :type: boolean, default True

   .. attribute:: use_contour

      Generate strokes from contours lines

      :type: boolean, default False

   .. attribute:: use_crease

      Generate strokes from creased edges

      :type: boolean, default False

   .. attribute:: use_crease_on_sharp

      Allow crease to show on sharp edges

      :type: boolean, default True

   .. attribute:: use_crease_on_smooth

      Allow crease edges to show inside smooth surfaces

      :type: boolean, default False

   .. attribute:: use_custom_camera

      Use custom camera instead of the active camera

      :type: boolean, default False

   .. attribute:: use_detail_preserve

      Keep the zig-zag "noise" in initial chaining

      :type: boolean, default False

   .. attribute:: use_edge_mark

      Generate strokes from Freestyle marked edges

      :type: boolean, default False

   .. attribute:: use_edge_overlap

      Allow edges in the same location (i.e. from edge split) to show properly. May run slower.

      :type: boolean, default False

   .. attribute:: use_face_mark

      Filter feature lines using Freestyle face marks

      :type: boolean, default False

   .. attribute:: use_face_mark_boundaries

      Filter feature lines based on face mark boundaries

      :type: boolean, default False

   .. attribute:: use_face_mark_invert

      Invert face mark filtering

      :type: boolean, default False

   .. attribute:: use_face_mark_keep_contour

      Preserve contour lines while filtering

      :type: boolean, default True

   .. attribute:: use_fuzzy_all

      Treat all lines as the same line type so they can be chained together

      :type: boolean, default False

   .. attribute:: use_fuzzy_intersections

      Treat intersection and contour lines as if they were the same type so they can be chained together

      :type: boolean, default False

   .. attribute:: use_geometry_space_chain

      Use geometry distance for chaining instead of image space

      :type: boolean, default False

   .. attribute:: use_image_boundary_trimming

      Trim all edges right at the boundary of image (including overscan region)

      :type: boolean, default False

   .. attribute:: use_intersection

      Generate strokes from intersections

      :type: boolean, default False

   .. attribute:: use_intersection_mask

      Mask bits to match from Collection Line Art settings

      :type: boolean array of 8 items, default (False, False, False, False, False, False, False, False)

   .. attribute:: use_intersection_match

      Require matching all intersection masks instead of just one

      :type: boolean, default False

   .. attribute:: use_invert_collection

      Select everything except lines from specified collection

      :type: boolean, default False

   .. attribute:: use_invert_silhouette

      Select anti-silhouette lines

      :type: boolean, default False

   .. attribute:: use_light_contour

      Generate light/shadow separation lines from a reference light object

      :type: boolean, default False

   .. attribute:: use_loose

      Generate strokes from loose edges

      :type: boolean, default False

   .. attribute:: use_loose_as_contour

      Loose edges will have contour type

      :type: boolean, default False

   .. attribute:: use_loose_edge_chain

      Allow loose edges to be chained together

      :type: boolean, default False

   .. attribute:: use_material

      Generate strokes from borders between materials

      :type: boolean, default False

   .. attribute:: use_material_mask

      Use material masks to filter out occluded strokes

      :type: boolean, default False

   .. attribute:: use_material_mask_bits

      Mask bits to match from Material Line Art settings

      :type: boolean array of 8 items, default (False, False, False, False, False, False, False, False)

   .. attribute:: use_material_mask_match

      Require matching all material masks instead of just one

      :type: boolean, default False

   .. attribute:: use_multiple_levels

      Generate strokes from a range of occlusion levels

      :type: boolean, default False

   .. attribute:: use_object_instances

      Allow particle objects and face/vertex instances to show in Line Art

      :type: boolean, default True

   .. attribute:: use_offset_towards_custom_camera

      Offset strokes towards selected camera instead of the active camera

      :type: boolean, default False

   .. attribute:: use_output_vertex_group_match_by_name

      Match output vertex group based on name

      :type: boolean, default True

   .. attribute:: use_overlap_edge_type_support

      Allow an edge to have multiple overlapping types. This will create a separate stroke for each overlapping type.

      :type: boolean, default False

   .. attribute:: use_shadow

      Project contour lines using a light source object

      :type: boolean, default False

   .. attribute:: vertex_group

      Vertex group name for selected strokes

      :type: string, default "", (never None)

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

