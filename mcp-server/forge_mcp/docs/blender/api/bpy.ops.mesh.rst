Mesh Operators
==============

.. module:: bpy.ops.mesh

.. function:: attribute_set(*, value_float=0.0, value_float_vector_2d=(0.0, 0.0), value_float_vector_3d=(0.0, 0.0, 0.0), value_int=0, value_int_vector_2d=(0, 0), value_color=(1.0, 1.0, 1.0, 1.0), value_bool=False)

   Set values of the active attribute for selected elements

   :arg value_float: Value
   :type value_float: float in [-inf, inf], (optional)
   :arg value_float_vector_2d: Value
   :type value_float_vector_2d: float array of 2 items in [-inf, inf], (optional)
   :arg value_float_vector_3d: Value
   :type value_float_vector_3d: float array of 3 items in [-inf, inf], (optional)
   :arg value_int: Value
   :type value_int: int in [-inf, inf], (optional)
   :arg value_int_vector_2d: Value
   :type value_int_vector_2d: int array of 2 items in [-inf, inf], (optional)
   :arg value_color: Value
   :type value_color: float array of 4 items in [-inf, inf], (optional)
   :arg value_bool: Value
   :type value_bool: boolean, (optional)

.. function:: average_normals(*, average_type='CUSTOM_NORMAL', weight=50, threshold=0.01)

   Average custom normals of selected vertices

   :arg average_type: Type, Averaging method

      * ``CUSTOM_NORMAL``
        Custom Normal -- Take average of vertex normals.
      * ``FACE_AREA``
        Face Area -- Set all vertex normals by face area.
      * ``CORNER_ANGLE``
        Corner Angle -- Set all vertex normals by corner angle.
   :type average_type: enum in [``'CUSTOM_NORMAL'``, ``'FACE_AREA'``, ``'CORNER_ANGLE'``], (optional)
   :arg weight: Weight, Weight applied per face
   :type weight: int in [1, 100], (optional)
   :arg threshold: Threshold, Threshold value for different weights to be considered equal
   :type threshold: float in [0, 10], (optional)

.. function:: beautify_fill(*, angle_limit=3.14159)

   Rearrange some faces to try to get less degenerated geometry

   :arg angle_limit: Max Angle, Angle limit
   :type angle_limit: float in [0, 3.14159], (optional)

.. function:: bevel(*, offset_type='OFFSET', offset=0.0, profile_type='SUPERELLIPSE', offset_pct=0.0, segments=1, profile=0.5, affect='EDGES', clamp_overlap=False, loop_slide=True, mark_seam=False, mark_sharp=False, material=-1, harden_normals=False, face_strength_mode='NONE', miter_outer='SHARP', miter_inner='SHARP', spread=0.1, vmesh_method='ADJ', release_confirm=False)

   Cut into selected items at an angle to create bevel or chamfer

   :arg offset_type: Width Type, The method for determining the size of the bevel

      * ``OFFSET``
        Offset -- Amount is offset of new edges from original.
      * ``WIDTH``
        Width -- Amount is width of new face.
      * ``DEPTH``
        Depth -- Amount is perpendicular distance from original edge to bevel face.
      * ``PERCENT``
        Percent -- Amount is percent of adjacent edge length.
      * ``ABSOLUTE``
        Absolute -- Amount is absolute distance along adjacent edge.
   :type offset_type: enum in [``'OFFSET'``, ``'WIDTH'``, ``'DEPTH'``, ``'PERCENT'``, ``'ABSOLUTE'``], (optional)
   :arg offset: Width, Bevel amount
   :type offset: float in [0, 1e+06], (optional)
   :arg profile_type: Profile Type, The type of shape used to rebuild a beveled section

      * ``SUPERELLIPSE``
        Superellipse -- The profile can be a concave or convex curve.
      * ``CUSTOM``
        Custom -- The profile can be any arbitrary path between its endpoints.
   :type profile_type: enum in [``'SUPERELLIPSE'``, ``'CUSTOM'``], (optional)
   :arg offset_pct: Width Percent, Bevel amount for percentage method
   :type offset_pct: float in [0, 100], (optional)
   :arg segments: Segments, Segments for curved edge
   :type segments: int in [1, 1000], (optional)
   :arg profile: Profile, Controls profile shape (0.5 = round)
   :type profile: float in [0, 1], (optional)
   :arg affect: Affect, Affect edges or vertices

      * ``VERTICES``
        Vertices -- Affect only vertices.
      * ``EDGES``
        Edges -- Affect only edges.
   :type affect: enum in [``'VERTICES'``, ``'EDGES'``], (optional)
   :arg clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other
   :type clamp_overlap: boolean, (optional)
   :arg loop_slide: Loop Slide, Prefer sliding along edges to even widths
   :type loop_slide: boolean, (optional)
   :arg mark_seam: Mark Seams, Mark Seams along beveled edges
   :type mark_seam: boolean, (optional)
   :arg mark_sharp: Mark Sharp, Mark beveled edges as sharp
   :type mark_sharp: boolean, (optional)
   :arg material: Material Index, Material for bevel faces (-1 means use adjacent faces)
   :type material: int in [-1, inf], (optional)
   :arg harden_normals: Harden Normals, Match normals of new faces to adjacent faces
   :type harden_normals: boolean, (optional)
   :arg face_strength_mode: Face Strength Mode, Whether to set face strength, and which faces to set face strength on

      * ``NONE``
        None -- Do not set face strength.
      * ``NEW``
        New -- Set face strength on new faces only.
      * ``AFFECTED``
        Affected -- Set face strength on new and modified faces only.
      * ``ALL``
        All -- Set face strength on all faces.
   :type face_strength_mode: enum in [``'NONE'``, ``'NEW'``, ``'AFFECTED'``, ``'ALL'``], (optional)
   :arg miter_outer: Outer Miter, Pattern to use for outside of miters

      * ``SHARP``
        Sharp -- Outside of miter is sharp.
      * ``PATCH``
        Patch -- Outside of miter is squared-off patch.
      * ``ARC``
        Arc -- Outside of miter is arc.
   :type miter_outer: enum in [``'SHARP'``, ``'PATCH'``, ``'ARC'``], (optional)
   :arg miter_inner: Inner Miter, Pattern to use for inside of miters

      * ``SHARP``
        Sharp -- Inside of miter is sharp.
      * ``ARC``
        Arc -- Inside of miter is arc.
   :type miter_inner: enum in [``'SHARP'``, ``'ARC'``], (optional)
   :arg spread: Spread, Amount to spread arcs for arc inner miters
   :type spread: float in [0, 1e+06], (optional)
   :arg vmesh_method: Vertex Mesh Method, The method to use to create meshes at intersections

      * ``ADJ``
        Grid Fill -- Default patterned fill.
      * ``CUTOFF``
        Cutoff -- A cutoff at each profile's end before the intersection.
   :type vmesh_method: enum in [``'ADJ'``, ``'CUTOFF'``], (optional)
   :arg release_confirm: Confirm on Release
   :type release_confirm: boolean, (optional)

.. function:: bisect(*, plane_co=(0.0, 0.0, 0.0), plane_no=(0.0, 0.0, 0.0), use_fill=False, clear_inner=False, clear_outer=False, threshold=0.0001, xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5)

   Cut geometry along a plane (click-drag to define plane)

   :arg plane_co: Plane Point, A point on the plane
   :type plane_co: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg plane_no: Plane Normal, The direction the plane points
   :type plane_no: :class:`mathutils.Vector` of 3 items in [-1, 1], (optional)
   :arg use_fill: Fill, Fill in the cut
   :type use_fill: boolean, (optional)
   :arg clear_inner: Clear Inner, Remove geometry behind the plane
   :type clear_inner: boolean, (optional)
   :arg clear_outer: Clear Outer, Remove geometry in front of the plane
   :type clear_outer: boolean, (optional)
   :arg threshold: Axis Threshold, Preserves the existing geometry along the cut plane
   :type threshold: float in [0, 10], (optional)
   :arg xstart: X Start
   :type xstart: int in [-inf, inf], (optional)
   :arg xend: X End
   :type xend: int in [-inf, inf], (optional)
   :arg ystart: Y Start
   :type ystart: int in [-inf, inf], (optional)
   :arg yend: Y End
   :type yend: int in [-inf, inf], (optional)
   :arg flip: Flip
   :type flip: boolean, (optional)
   :arg cursor: Cursor, Mouse cursor style to use during the modal operator
   :type cursor: int in [0, inf], (optional)

.. function:: blend_from_shape(*, shape='', blend=1.0, add=True)

   Blend in shape from a shape key

   :arg shape: Shape, Shape key to use for blending
   :type shape: enum in [], (optional)
   :arg blend: Blend, Blending factor
   :type blend: float in [-1000, 1000], (optional)
   :arg add: Add, Add rather than blend between shapes
   :type add: boolean, (optional)

.. function:: bridge_edge_loops(*, type='SINGLE', use_merge=False, merge_factor=0.5, twist_offset=0, number_cuts=0, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH')

   Create a bridge of faces between two or more selected edge loops

   :arg type: Connect Loops, Method of bridging multiple loops
   :type type: enum in [``'SINGLE'``, ``'CLOSED'``, ``'PAIRS'``], (optional)
   :arg use_merge: Merge, Merge rather than creating faces
   :type use_merge: boolean, (optional)
   :arg merge_factor: Merge Factor
   :type merge_factor: float in [0, 1], (optional)
   :arg twist_offset: Twist, Twist offset for closed loops
   :type twist_offset: int in [-1000, 1000], (optional)
   :arg number_cuts: Number of Cuts
   :type number_cuts: int in [0, 1000], (optional)
   :arg interpolation: Interpolation, Interpolation method
   :type interpolation: enum in [``'LINEAR'``, ``'PATH'``, ``'SURFACE'``], (optional)
   :arg smoothness: Smoothness, Smoothness factor
   :type smoothness: float in [0, 1000], (optional)
   :arg profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
   :type profile_shape_factor: float in [-1000, 1000], (optional)
   :arg profile_shape: Profile Shape, Shape of the profile
   :type profile_shape: enum in :ref:`rna_enum_proportional_falloff_curve_only_items`, (optional)

.. function:: colors_reverse()

   Flip direction of face corner color attribute inside faces

.. function:: colors_rotate(*, use_ccw=False)

   Rotate face corner color attribute inside faces

   :arg use_ccw: Counter Clockwise
   :type use_ccw: boolean, (optional)

.. function:: convex_hull(*, delete_unused=True, use_existing_faces=True, make_holes=False, join_triangles=True, face_threshold=0.698132, shape_threshold=0.698132, topology_influence=0.0, uvs=False, vcols=False, seam=False, sharp=False, materials=False, deselect_joined=False)

   Enclose selected vertices in a convex polyhedron

   :arg delete_unused: Delete Unused, Delete selected elements that are not used by the hull
   :type delete_unused: boolean, (optional)
   :arg use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face
   :type use_existing_faces: boolean, (optional)
   :arg make_holes: Make Holes, Delete selected faces that are used by the hull
   :type make_holes: boolean, (optional)
   :arg join_triangles: Join Triangles, Merge adjacent triangles into quads
   :type join_triangles: boolean, (optional)
   :arg face_threshold: Max Face Angle, Face angle limit
   :type face_threshold: float in [0, 3.14159], (optional)
   :arg shape_threshold: Max Shape Angle, Shape angle limit
   :type shape_threshold: float in [0, 3.14159], (optional)
   :arg topology_influence: Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads
   :type topology_influence: float in [0, 2], (optional)
   :arg uvs: Compare UVs
   :type uvs: boolean, (optional)
   :arg vcols: Compare Color Attributes
   :type vcols: boolean, (optional)
   :arg seam: Compare Seam
   :type seam: boolean, (optional)
   :arg sharp: Compare Sharp
   :type sharp: boolean, (optional)
   :arg materials: Compare Materials
   :type materials: boolean, (optional)
   :arg deselect_joined: Deselect Joined, Only select remaining triangles that were not merged
   :type deselect_joined: boolean, (optional)

.. function:: customdata_custom_splitnormals_add()

   Add a custom split normals layer, if none exists yet

.. function:: customdata_custom_splitnormals_clear()

   Remove the custom split normals layer, if it exists

.. function:: customdata_mask_clear()

   Clear vertex sculpt masking data from the mesh

.. function:: customdata_skin_add()

   Add a vertex skin layer

.. function:: customdata_skin_clear()

   Clear vertex skin layer

.. function:: decimate(*, ratio=1.0, use_vertex_group=False, vertex_group_factor=1.0, invert_vertex_group=False, use_symmetry=False, symmetry_axis='Y')

   Simplify geometry by collapsing edges

   :arg ratio: Ratio
   :type ratio: float in [0, 1], (optional)
   :arg use_vertex_group: Vertex Group, Use active vertex group as an influence
   :type use_vertex_group: boolean, (optional)
   :arg vertex_group_factor: Weight, Vertex group strength
   :type vertex_group_factor: float in [0, 1000], (optional)
   :arg invert_vertex_group: Invert, Invert vertex group influence
   :type invert_vertex_group: boolean, (optional)
   :arg use_symmetry: Symmetry, Maintain symmetry on an axis
   :type use_symmetry: boolean, (optional)
   :arg symmetry_axis: Axis, Axis of symmetry
   :type symmetry_axis: enum in :ref:`rna_enum_axis_xyz_items`, (optional)

.. function:: delete(*, type='VERT')

   Delete selected vertices, edges or faces

   :arg type: Type, Method used for deleting mesh data
   :type type: enum in [``'VERT'``, ``'EDGE'``, ``'FACE'``, ``'EDGE_FACE'``, ``'ONLY_FACE'``], (optional)

.. function:: delete_edgeloop(*, use_face_split=True)

   Delete an edge loop by merging the faces on each side

   :arg use_face_split: Face Split, Split off face corners to maintain surrounding geometry
   :type use_face_split: boolean, (optional)

.. function:: delete_loose(*, use_verts=True, use_edges=True, use_faces=False)

   Delete loose vertices, edges or faces

   :arg use_verts: Vertices, Remove loose vertices
   :type use_verts: boolean, (optional)
   :arg use_edges: Edges, Remove loose edges
   :type use_edges: boolean, (optional)
   :arg use_faces: Faces, Remove loose faces
   :type use_faces: boolean, (optional)

.. function:: dissolve_degenerate(*, threshold=0.0001)

   Dissolve zero area faces and zero length edges

   :arg threshold: Merge Distance, Maximum distance between elements to merge
   :type threshold: float in [1e-06, 50], (optional)

.. function:: dissolve_edges(*, use_verts=True, angle_threshold=3.14159, use_face_split=False)

   Dissolve edges, merging faces

   :arg use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges
   :type use_verts: boolean, (optional)
   :arg angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold.
   :type angle_threshold: float in [0, 3.14159], (optional)
   :arg use_face_split: Face Split, Split off face corners to maintain surrounding geometry
   :type use_face_split: boolean, (optional)

.. function:: dissolve_faces(*, use_verts=False)

   Dissolve faces

   :arg use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges
   :type use_verts: boolean, (optional)

.. function:: dissolve_limited(*, angle_limit=0.0872665, use_dissolve_boundaries=False, delimit={'NORMAL'})

   Dissolve selected edges and vertices, limited by the angle of surrounding geometry

   :arg angle_limit: Max Angle, Angle limit
   :type angle_limit: float in [0, 3.14159], (optional)
   :arg use_dissolve_boundaries: All Boundaries, Dissolve all vertices in between face boundaries
   :type use_dissolve_boundaries: boolean, (optional)
   :arg delimit: Delimit, Delimit dissolve operation
   :type delimit: enum set in :ref:`rna_enum_mesh_delimit_mode_items`, (optional)

.. function:: dissolve_mode(*, use_verts=False, angle_threshold=3.14159, use_face_split=False, use_boundary_tear=False)

   Dissolve geometry based on the selection mode

   :arg use_verts: Dissolve Vertices, Dissolve remaining vertices which connect to only two edges
   :type use_verts: boolean, (optional)
   :arg angle_threshold: Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold.
   :type angle_threshold: float in [0, 3.14159], (optional)
   :arg use_face_split: Face Split, Split off face corners to maintain surrounding geometry
   :type use_face_split: boolean, (optional)
   :arg use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
   :type use_boundary_tear: boolean, (optional)

.. function:: dissolve_verts(*, use_face_split=False, use_boundary_tear=False)

   Dissolve vertices, merge edges and faces

   :arg use_face_split: Face Split, Split off face corners to maintain surrounding geometry
   :type use_face_split: boolean, (optional)
   :arg use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
   :type use_boundary_tear: boolean, (optional)

.. function:: dupli_extrude_cursor(*, rotate_source=True)

   Duplicate and extrude selected vertices, edges or faces towards the mouse cursor

   :arg rotate_source: Rotate Source, Rotate initial selection giving better shape
   :type rotate_source: boolean, (optional)

.. function:: duplicate(*, mode=1)

   Duplicate selected vertices, edges or faces

   :arg mode: Mode
   :type mode: int in [0, inf], (optional)

.. function:: duplicate_move(*, MESH_OT_duplicate=None, TRANSFORM_OT_translate=None)

   Duplicate mesh and move

   :arg MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces
   :type MESH_OT_duplicate: :class:`MESH_OT_duplicate`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: edge_collapse()

   Collapse isolated edge and face regions, merging data such as UVs and color attributes. This can collapse edge-rings as well as regions of connected faces into vertices

.. function:: edge_face_add()

   Add an edge or face to selected

.. function:: edge_rotate(*, use_ccw=False)

   Rotate selected edge or adjoining faces

   :arg use_ccw: Counter Clockwise
   :type use_ccw: boolean, (optional)

.. function:: edge_split(*, type='EDGE')

   Split selected edges so that each neighbor face gets its own copy

   :arg type: Type, Method to use for splitting

      * ``EDGE``
        Faces by Edges -- Split faces along selected edges.
      * ``VERT``
        Faces & Edges by Vertices -- Split faces and edges connected to selected vertices.
   :type type: enum in [``'EDGE'``, ``'VERT'``], (optional)

.. function:: edgering_select(*, extend=False, deselect=False, toggle=False, ring=True)

   Select an edge ring

   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)
   :arg deselect: Deselect, Remove from the selection
   :type deselect: boolean, (optional)
   :arg toggle: Toggle Select, Toggle the selection
   :type toggle: boolean, (optional)
   :arg ring: Select Ring, Select ring
   :type ring: boolean, (optional)

.. function:: edges_select_sharp(*, sharpness=0.523599)

   Select all sharp enough edges

   :arg sharpness: Sharpness
   :type sharpness: float in [0.000174533, 3.14159], (optional)

.. function:: extrude_context(*, use_normal_flip=False, use_dissolve_ortho_edges=False, mirror=False)

   Extrude selection

   :arg use_normal_flip: Flip Normals
   :type use_normal_flip: boolean, (optional)
   :arg use_dissolve_ortho_edges: Dissolve Orthogonal Edges
   :type use_dissolve_ortho_edges: boolean, (optional)
   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)

.. function:: extrude_context_move(*, MESH_OT_extrude_context=None, TRANSFORM_OT_translate=None)

   Extrude region together along the average normal

   :arg MESH_OT_extrude_context: Extrude Context, Extrude selection
   :type MESH_OT_extrude_context: :class:`MESH_OT_extrude_context`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude_edges_indiv(*, use_normal_flip=False, mirror=False)

   Extrude individual edges only

   :arg use_normal_flip: Flip Normals
   :type use_normal_flip: boolean, (optional)
   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)

.. function:: extrude_edges_move(*, MESH_OT_extrude_edges_indiv=None, TRANSFORM_OT_translate=None)

   Extrude edges and move result

   :arg MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
   :type MESH_OT_extrude_edges_indiv: :class:`MESH_OT_extrude_edges_indiv`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude_faces_indiv(*, mirror=False)

   Extrude individual faces only

   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)

.. function:: extrude_faces_move(*, MESH_OT_extrude_faces_indiv=None, TRANSFORM_OT_shrink_fatten=None)

   Extrude each individual face separately along local normals

   :arg MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only
   :type MESH_OT_extrude_faces_indiv: :class:`MESH_OT_extrude_faces_indiv`, (optional)
   :arg TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
   :type TRANSFORM_OT_shrink_fatten: :class:`TRANSFORM_OT_shrink_fatten`, (optional)

.. function:: extrude_manifold(*, MESH_OT_extrude_region=None, TRANSFORM_OT_translate=None)

   Extrude, dissolves edges whose faces form a flat surface and intersect new edges

   :arg MESH_OT_extrude_region: Extrude Region, Extrude region of faces
   :type MESH_OT_extrude_region: :class:`MESH_OT_extrude_region`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude_region(*, use_normal_flip=False, use_dissolve_ortho_edges=False, mirror=False)

   Extrude region of faces

   :arg use_normal_flip: Flip Normals
   :type use_normal_flip: boolean, (optional)
   :arg use_dissolve_ortho_edges: Dissolve Orthogonal Edges
   :type use_dissolve_ortho_edges: boolean, (optional)
   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)

.. function:: extrude_region_move(*, MESH_OT_extrude_region=None, TRANSFORM_OT_translate=None)

   Extrude region and move result

   :arg MESH_OT_extrude_region: Extrude Region, Extrude region of faces
   :type MESH_OT_extrude_region: :class:`MESH_OT_extrude_region`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude_region_shrink_fatten(*, MESH_OT_extrude_region=None, TRANSFORM_OT_shrink_fatten=None)

   Extrude region together along local normals

   :arg MESH_OT_extrude_region: Extrude Region, Extrude region of faces
   :type MESH_OT_extrude_region: :class:`MESH_OT_extrude_region`, (optional)
   :arg TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
   :type TRANSFORM_OT_shrink_fatten: :class:`TRANSFORM_OT_shrink_fatten`, (optional)

.. function:: extrude_repeat(*, steps=10, offset=(0.0, 0.0, 0.0), scale_offset=1.0)

   Extrude selected vertices, edges or faces repeatedly

   :arg steps: Steps
   :type steps: int in [0, 1000000], (optional)
   :arg offset: Offset, Offset vector
   :type offset: :class:`mathutils.Vector` of 3 items in [-100000, 100000], (optional)
   :arg scale_offset: Scale Offset
   :type scale_offset: float in [0, inf], (optional)

.. function:: extrude_vertices_move(*, MESH_OT_extrude_verts_indiv=None, TRANSFORM_OT_translate=None)

   Extrude vertices and move result

   :arg MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only
   :type MESH_OT_extrude_verts_indiv: :class:`MESH_OT_extrude_verts_indiv`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: extrude_verts_indiv(*, mirror=False)

   Extrude individual vertices only

   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)

.. function:: face_make_planar(*, factor=1.0, repeat=1)

   Flatten selected faces

   :arg factor: Factor
   :type factor: float in [-10, 10], (optional)
   :arg repeat: Iterations
   :type repeat: int in [1, 10000], (optional)

.. function:: face_split_by_edges()

   Weld loose edges into faces (splitting them into new faces)

.. function:: faces_mirror_uv(*, direction='POSITIVE', precision=3)

   Copy mirror UV coordinates on the X axis based on a mirrored mesh

   :arg direction: Axis Direction
   :type direction: enum in [``'POSITIVE'``, ``'NEGATIVE'``], (optional)
   :arg precision: Precision, Tolerance for finding vertex duplicates
   :type precision: int in [1, 16], (optional)
   :File: `startup\bl_operators\mesh.py\:134 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\mesh.py#L134>`__


.. function:: faces_select_linked_flat(*, sharpness=0.0174533)

   Select linked faces by angle

   :arg sharpness: Sharpness
   :type sharpness: float in [0.000174533, 3.14159], (optional)

.. function:: faces_shade_flat()

   Display faces flat

.. function:: faces_shade_smooth()

   Display faces smooth (using vertex normals)

.. function:: fill(*, use_beauty=True)

   Fill a selected edge loop with faces

   :arg use_beauty: Beauty, Use best triangulation division
   :type use_beauty: boolean, (optional)

.. function:: fill_grid(*, span=1, offset=0, use_interp_simple=False)

   Fill grid from two loops

   :arg span: Span, Number of grid columns
   :type span: int in [1, 1000], (optional)
   :arg offset: Offset, Vertex that is the corner of the grid
   :type offset: int in [-1000, 1000], (optional)
   :arg use_interp_simple: Simple Blending, Use simple interpolation of grid vertices
   :type use_interp_simple: boolean, (optional)

.. function:: fill_holes(*, sides=4)

   Fill in holes (boundary edge loops)

   :arg sides: Sides, Number of sides in hole required to fill (zero fills all holes)
   :type sides: int in [0, 1000], (optional)

.. function:: flip_normals(*, only_clnors=False)

   Flip the direction of selected faces' normals (and of their vertices)

   :arg only_clnors: Custom Normals Only, Only flip the custom loop normals of the selected elements
   :type only_clnors: boolean, (optional)

.. function:: flip_quad_tessellation()

   Flips the tessellation of selected quads

.. function:: hide(*, unselected=False)

   Hide (un)selected vertices, edges or faces

   :arg unselected: Unselected, Hide unselected rather than selected
   :type unselected: boolean, (optional)

.. function:: inset(*, use_boundary=True, use_even_offset=True, use_relative_offset=False, use_edge_rail=False, thickness=0.0, depth=0.0, use_outset=False, use_select_inset=False, use_individual=False, use_interpolate=True, release_confirm=False)

   Inset new faces into selected faces

   :arg use_boundary: Boundary, Inset face boundaries
   :type use_boundary: boolean, (optional)
   :arg use_even_offset: Offset Even, Scale the offset to give more even thickness
   :type use_even_offset: boolean, (optional)
   :arg use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
   :type use_relative_offset: boolean, (optional)
   :arg use_edge_rail: Edge Rail, Inset the region along existing edges
   :type use_edge_rail: boolean, (optional)
   :arg thickness: Thickness
   :type thickness: float in [0, inf], (optional)
   :arg depth: Depth
   :type depth: float in [-inf, inf], (optional)
   :arg use_outset: Outset, Outset rather than inset
   :type use_outset: boolean, (optional)
   :arg use_select_inset: Select Outer, Select the new inset faces
   :type use_select_inset: boolean, (optional)
   :arg use_individual: Individual, Individual face inset
   :type use_individual: boolean, (optional)
   :arg use_interpolate: Interpolate, Blend face data across the inset
   :type use_interpolate: boolean, (optional)
   :arg release_confirm: Confirm on Release
   :type release_confirm: boolean, (optional)

.. function:: intersect(*, mode='SELECT_UNSELECT', separate_mode='CUT', threshold=1e-06, solver='EXACT')

   Cut an intersection into faces

   :arg mode: Source

      * ``SELECT``
        Self Intersect -- Self intersect selected faces.
      * ``SELECT_UNSELECT``
        Selected/Unselected -- Intersect selected with unselected faces.
   :type mode: enum in [``'SELECT'``, ``'SELECT_UNSELECT'``], (optional)
   :arg separate_mode: Separate Mode

      * ``ALL``
        All -- Separate all geometry from intersections.
      * ``CUT``
        Cut -- Cut into geometry keeping each side separate (Selected/Unselected only).
      * ``NONE``
        Merge -- Merge all geometry from the intersection.
   :type separate_mode: enum in [``'ALL'``, ``'CUT'``, ``'NONE'``], (optional)
   :arg threshold: Merge Threshold
   :type threshold: float in [0, 0.01], (optional)
   :arg solver: Solver, Which Intersect solver to use

      * ``FAST``
        Float -- Simple solver with good performance, without support for overlapping geometry.
      * ``EXACT``
        Exact -- Slower solver with the best results for coplanar faces.
   :type solver: enum in [``'FAST'``, ``'EXACT'``], (optional)

.. function:: intersect_boolean(*, operation='DIFFERENCE', use_swap=False, use_self=False, threshold=1e-06, solver='EXACT')

   Cut solid geometry from selected to unselected

   :arg operation: Boolean Operation, Which boolean operation to apply
   :type operation: enum in [``'INTERSECT'``, ``'UNION'``, ``'DIFFERENCE'``], (optional)
   :arg use_swap: Swap, Use with difference intersection to swap which side is kept
   :type use_swap: boolean, (optional)
   :arg use_self: Self Intersection, Do self-union or self-intersection
   :type use_self: boolean, (optional)
   :arg threshold: Merge Threshold
   :type threshold: float in [0, 0.01], (optional)
   :arg solver: Solver, Which Boolean solver to use

      * ``FAST``
        Fast -- Faster solver, some limitations.
      * ``EXACT``
        Exact -- Exact solver, slower, handles more cases.
   :type solver: enum in [``'FAST'``, ``'EXACT'``], (optional)

.. function:: knife_project(*, cut_through=False)

   Use other objects outlines and boundaries to project knife cuts

   :arg cut_through: Cut Through, Cut through all faces, not just visible ones
   :type cut_through: boolean, (optional)

.. function:: knife_tool(*, use_occlude_geometry=True, only_selected=False, xray=True, visible_measurements='NONE', angle_snapping='NONE', angle_snapping_increment=0.523599, wait_for_input=True)

   Cut new topology

   :arg use_occlude_geometry: Occlude Geometry, Only cut the front most geometry
   :type use_occlude_geometry: boolean, (optional)
   :arg only_selected: Only Selected, Only cut selected geometry
   :type only_selected: boolean, (optional)
   :arg xray: X-Ray, Show cuts hidden by geometry
   :type xray: boolean, (optional)
   :arg visible_measurements: Measurements, Visible distance and angle measurements

      * ``NONE``
        None -- Show no measurements.
      * ``BOTH``
        Both -- Show both distances and angles.
      * ``DISTANCE``
        Distance -- Show just distance measurements.
      * ``ANGLE``
        Angle -- Show just angle measurements.
   :type visible_measurements: enum in [``'NONE'``, ``'BOTH'``, ``'DISTANCE'``, ``'ANGLE'``], (optional)
   :arg angle_snapping: Angle Snapping, Angle snapping mode

      * ``NONE``
        None -- No angle snapping.
      * ``SCREEN``
        Screen -- Screen space angle snapping.
      * ``RELATIVE``
        Relative -- Angle snapping relative to the previous cut edge.
   :type angle_snapping: enum in [``'NONE'``, ``'SCREEN'``, ``'RELATIVE'``], (optional)
   :arg angle_snapping_increment: Angle Snap Increment, The angle snap increment used when in constrained angle mode
   :type angle_snapping_increment: float in [0, 3.14159], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)

.. function:: loop_multi_select(*, ring=False)

   Select a loop of connected edges by connection type

   :arg ring: Ring
   :type ring: boolean, (optional)

.. function:: loop_select(*, extend=False, deselect=False, toggle=False, ring=False)

   Select a loop of connected edges

   :arg extend: Extend Select, Extend the selection
   :type extend: boolean, (optional)
   :arg deselect: Deselect, Remove from the selection
   :type deselect: boolean, (optional)
   :arg toggle: Toggle Select, Toggle the selection
   :type toggle: boolean, (optional)
   :arg ring: Select Ring, Select ring
   :type ring: boolean, (optional)

.. function:: loop_to_region(*, select_bigger=False)

   Select region of faces inside of a selected loop of edges

   :arg select_bigger: Select Bigger, Select bigger regions instead of smaller ones
   :type select_bigger: boolean, (optional)

.. function:: loopcut(*, number_cuts=1, smoothness=0.0, falloff='INVERSE_SQUARE', object_index=-1, edge_index=-1, mesh_select_mode_init=(False, False, False))

   Add a new loop between existing loops

   :arg number_cuts: Number of Cuts
   :type number_cuts: int in [1, 1000000], (optional)
   :arg smoothness: Smoothness, Smoothness factor
   :type smoothness: float in [-1000, 1000], (optional)
   :arg falloff: Falloff, Falloff type of the feather
   :type falloff: enum in :ref:`rna_enum_proportional_falloff_curve_only_items`, (optional)
   :arg object_index: Object Index
   :type object_index: int in [-1, inf], (optional)
   :arg edge_index: Edge Index
   :type edge_index: int in [-1, inf], (optional)
   :type mesh_select_mode_init: boolean array of 3 items, (optional)

.. function:: loopcut_slide(*, MESH_OT_loopcut=None, TRANSFORM_OT_edge_slide=None)

   Cut mesh loop and slide it

   :arg MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops
   :type MESH_OT_loopcut: :class:`MESH_OT_loopcut`, (optional)
   :arg TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
   :type TRANSFORM_OT_edge_slide: :class:`TRANSFORM_OT_edge_slide`, (optional)

.. function:: mark_freestyle_edge(*, clear=False)

   (Un)mark selected edges as Freestyle feature edges

   :arg clear: Clear
   :type clear: boolean, (optional)

.. function:: mark_freestyle_face(*, clear=False)

   (Un)mark selected faces for exclusion from Freestyle feature edge detection

   :arg clear: Clear
   :type clear: boolean, (optional)

.. function:: mark_seam(*, clear=False)

   (Un)mark selected edges as a seam

   :arg clear: Clear
   :type clear: boolean, (optional)

.. function:: mark_sharp(*, clear=False, use_verts=False)

   (Un)mark selected edges as sharp

   :arg clear: Clear
   :type clear: boolean, (optional)
   :arg use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp
   :type use_verts: boolean, (optional)

.. function:: merge(*, type='CENTER', uvs=False)

   Merge selected vertices

   :arg type: Type, Merge method to use
   :type type: enum in [``'CENTER'``, ``'CURSOR'``, ``'COLLAPSE'``, ``'FIRST'``, ``'LAST'``], (optional)
   :arg uvs: UVs, Move UVs according to merge
   :type uvs: boolean, (optional)

.. function:: merge_normals()

   Merge custom normals of selected vertices

.. function:: mod_weighted_strength(*, set=False, face_strength='MEDIUM')

   Set/Get strength of face (used in Weighted Normal modifier)

   :arg set: Set Value, Set value of faces
   :type set: boolean, (optional)
   :arg face_strength: Face Strength, Strength to use for assigning or selecting face influence for weighted normal modifier
   :type face_strength: enum in [``'WEAK'``, ``'MEDIUM'``, ``'STRONG'``], (optional)

.. function:: normals_make_consistent(*, inside=False)

   Make face and vertex normals point either outside or inside the mesh

   :arg inside: Inside
   :type inside: boolean, (optional)

.. function:: normals_tools(*, mode='COPY', absolute=False)

   Custom normals tools using Normal Vector of UI

   :arg mode: Mode, Mode of tools taking input from interface

      * ``COPY``
        Copy Normal -- Copy normal to the internal clipboard.
      * ``PASTE``
        Paste Normal -- Paste normal from the internal clipboard.
      * ``ADD``
        Add Normal -- Add normal vector with selection.
      * ``MULTIPLY``
        Multiply Normal -- Multiply normal vector with selection.
      * ``RESET``
        Reset Normal -- Reset the internal clipboard and/or normal of selected element.
   :type mode: enum in [``'COPY'``, ``'PASTE'``, ``'ADD'``, ``'MULTIPLY'``, ``'RESET'``], (optional)
   :arg absolute: Absolute Coordinates, Copy Absolute coordinates of Normal vector
   :type absolute: boolean, (optional)

.. function:: offset_edge_loops(*, use_cap_endpoint=False)

   Create offset edge loop from the current selection

   :arg use_cap_endpoint: Cap Endpoint, Extend loop around end-points
   :type use_cap_endpoint: boolean, (optional)

.. function:: offset_edge_loops_slide(*, MESH_OT_offset_edge_loops=None, TRANSFORM_OT_edge_slide=None)

   Offset edge loop slide

   :arg MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection
   :type MESH_OT_offset_edge_loops: :class:`MESH_OT_offset_edge_loops`, (optional)
   :arg TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
   :type TRANSFORM_OT_edge_slide: :class:`TRANSFORM_OT_edge_slide`, (optional)

.. function:: point_normals(*, mode='COORDINATES', invert=False, align=False, target_location=(0.0, 0.0, 0.0), spherize=False, spherize_strength=0.1)

   Point selected custom normals to specified Target

   :arg mode: Mode, How to define coordinates to point custom normals to

      * ``COORDINATES``
        Coordinates -- Use static coordinates (defined by various means).
      * ``MOUSE``
        Mouse -- Follow mouse cursor.
   :type mode: enum in [``'COORDINATES'``, ``'MOUSE'``], (optional)
   :arg invert: Invert, Invert affected normals
   :type invert: boolean, (optional)
   :arg align: Align, Make all affected normals parallel
   :type align: boolean, (optional)
   :arg target_location: Target, Target location to which normals will point
   :type target_location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg spherize: Spherize, Interpolate between original and new normals
   :type spherize: boolean, (optional)
   :arg spherize_strength: Spherize Strength, Ratio of spherized normal to original normal
   :type spherize_strength: float in [0, 1], (optional)

.. function:: poke(*, offset=0.0, use_relative_offset=False, center_mode='MEDIAN_WEIGHTED')

   Split a face into a fan

   :arg offset: Poke Offset, Poke Offset
   :type offset: float in [-1000, 1000], (optional)
   :arg use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
   :type use_relative_offset: boolean, (optional)
   :arg center_mode: Poke Center, Poke face center calculation

      * ``MEDIAN_WEIGHTED``
        Weighted Median -- Weighted median face center.
      * ``MEDIAN``
        Median -- Median face center.
      * ``BOUNDS``
        Bounds -- Face bounds center.
   :type center_mode: enum in [``'MEDIAN_WEIGHTED'``, ``'MEDIAN'``, ``'BOUNDS'``], (optional)

.. function:: polybuild_delete_at_cursor(*, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg use_proportional_edit: Proportional Editing
   :type use_proportional_edit: boolean, (optional)
   :arg proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
   :type proportional_edit_falloff: enum in :ref:`rna_enum_proportional_falloff_items`, (optional)
   :arg proportional_size: Proportional Size
   :type proportional_size: float in [1e-06, inf], (optional)
   :arg use_proportional_connected: Connected
   :type use_proportional_connected: boolean, (optional)
   :arg use_proportional_projected: Projected (2D)
   :type use_proportional_projected: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: polybuild_dissolve_at_cursor()

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

.. function:: polybuild_extrude_at_cursor_move(*, MESH_OT_polybuild_transform_at_cursor=None, MESH_OT_extrude_edges_indiv=None, TRANSFORM_OT_translate=None)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
   :type MESH_OT_polybuild_transform_at_cursor: :class:`MESH_OT_polybuild_transform_at_cursor`, (optional)
   :arg MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
   :type MESH_OT_extrude_edges_indiv: :class:`MESH_OT_extrude_edges_indiv`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: polybuild_face_at_cursor(*, create_quads=True, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg create_quads: Create Quads, Automatically split edges in triangles to maintain quad topology
   :type create_quads: boolean, (optional)
   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg use_proportional_edit: Proportional Editing
   :type use_proportional_edit: boolean, (optional)
   :arg proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
   :type proportional_edit_falloff: enum in :ref:`rna_enum_proportional_falloff_items`, (optional)
   :arg proportional_size: Proportional Size
   :type proportional_size: float in [1e-06, inf], (optional)
   :arg use_proportional_connected: Connected
   :type use_proportional_connected: boolean, (optional)
   :arg use_proportional_projected: Projected (2D)
   :type use_proportional_projected: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: polybuild_face_at_cursor_move(*, MESH_OT_polybuild_face_at_cursor=None, TRANSFORM_OT_translate=None)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg MESH_OT_polybuild_face_at_cursor: Poly Build Face at Cursor
   :type MESH_OT_polybuild_face_at_cursor: :class:`MESH_OT_polybuild_face_at_cursor`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: polybuild_split_at_cursor(*, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg use_proportional_edit: Proportional Editing
   :type use_proportional_edit: boolean, (optional)
   :arg proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
   :type proportional_edit_falloff: enum in :ref:`rna_enum_proportional_falloff_items`, (optional)
   :arg proportional_size: Proportional Size
   :type proportional_size: float in [1e-06, inf], (optional)
   :arg use_proportional_connected: Connected
   :type use_proportional_connected: boolean, (optional)
   :arg use_proportional_projected: Projected (2D)
   :type use_proportional_projected: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: polybuild_split_at_cursor_move(*, MESH_OT_polybuild_split_at_cursor=None, TRANSFORM_OT_translate=None)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg MESH_OT_polybuild_split_at_cursor: Poly Build Split at Cursor
   :type MESH_OT_polybuild_split_at_cursor: :class:`MESH_OT_polybuild_split_at_cursor`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: polybuild_transform_at_cursor(*, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg use_proportional_edit: Proportional Editing
   :type use_proportional_edit: boolean, (optional)
   :arg proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
   :type proportional_edit_falloff: enum in :ref:`rna_enum_proportional_falloff_items`, (optional)
   :arg proportional_size: Proportional Size
   :type proportional_size: float in [1e-06, inf], (optional)
   :arg use_proportional_connected: Connected
   :type use_proportional_connected: boolean, (optional)
   :arg use_proportional_projected: Projected (2D)
   :type use_proportional_projected: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: polybuild_transform_at_cursor_move(*, MESH_OT_polybuild_transform_at_cursor=None, TRANSFORM_OT_translate=None)

   Undocumented, consider `contributing <https://developer.blender.org/>`__.

   :arg MESH_OT_polybuild_transform_at_cursor: Poly Build Transform at Cursor
   :type MESH_OT_polybuild_transform_at_cursor: :class:`MESH_OT_polybuild_transform_at_cursor`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: primitive_circle_add(*, vertices=32, radius=1.0, fill_type='NOTHING', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a circle mesh

   :arg vertices: Vertices
   :type vertices: int in [3, 10000000], (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg fill_type: Fill Type

      * ``NOTHING``
        Nothing -- Don't fill at all.
      * ``NGON``
        N-Gon -- Use n-gons.
      * ``TRIFAN``
        Triangle Fan -- Use triangle fans.
   :type fill_type: enum in [``'NOTHING'``, ``'NGON'``, ``'TRIFAN'``], (optional)
   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_cone_add(*, vertices=32, radius1=1.0, radius2=0.0, depth=2.0, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a conic mesh

   :arg vertices: Vertices
   :type vertices: int in [3, 10000000], (optional)
   :arg radius1: Radius 1
   :type radius1: float in [0, inf], (optional)
   :arg radius2: Radius 2
   :type radius2: float in [0, inf], (optional)
   :arg depth: Depth
   :type depth: float in [0, inf], (optional)
   :arg end_fill_type: Base Fill Type

      * ``NOTHING``
        Nothing -- Don't fill at all.
      * ``NGON``
        N-Gon -- Use n-gons.
      * ``TRIFAN``
        Triangle Fan -- Use triangle fans.
   :type end_fill_type: enum in [``'NOTHING'``, ``'NGON'``, ``'TRIFAN'``], (optional)
   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_cube_add(*, size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a cube mesh that consists of six square faces

   :arg size: Size
   :type size: float in [0, inf], (optional)
   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_cube_add_gizmo(*, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

   Construct a cube mesh

   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg matrix: Matrix
   :type matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], (optional)

.. function:: primitive_cylinder_add(*, vertices=32, radius=1.0, depth=2.0, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a cylinder mesh

   :arg vertices: Vertices
   :type vertices: int in [3, 10000000], (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg depth: Depth
   :type depth: float in [0, inf], (optional)
   :arg end_fill_type: Cap Fill Type

      * ``NOTHING``
        Nothing -- Don't fill at all.
      * ``NGON``
        N-Gon -- Use n-gons.
      * ``TRIFAN``
        Triangle Fan -- Use triangle fans.
   :type end_fill_type: enum in [``'NOTHING'``, ``'NGON'``, ``'TRIFAN'``], (optional)
   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_grid_add(*, x_subdivisions=10, y_subdivisions=10, size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a subdivided plane mesh

   :arg x_subdivisions: X Subdivisions
   :type x_subdivisions: int in [1, 10000000], (optional)
   :arg y_subdivisions: Y Subdivisions
   :type y_subdivisions: int in [1, 10000000], (optional)
   :arg size: Size
   :type size: float in [0, inf], (optional)
   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_ico_sphere_add(*, subdivisions=2, radius=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a spherical mesh that consists of equally sized triangles

   :arg subdivisions: Subdivisions
   :type subdivisions: int in [1, 10], (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_monkey_add(*, size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a Suzanne mesh

   :arg size: Size
   :type size: float in [0, inf], (optional)
   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_plane_add(*, size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a filled planar mesh with 4 vertices

   :arg size: Size
   :type size: float in [0, inf], (optional)
   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: primitive_torus_add(*, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), major_segments=48, minor_segments=12, mode='MAJOR_MINOR', major_radius=1.0, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75, generate_uvs=True)

   Construct a torus mesh

   :arg align: Align

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg major_segments: Major Segments, Number of segments for the main ring of the torus
   :type major_segments: int in [3, 256], (optional)
   :arg minor_segments: Minor Segments, Number of segments for the minor ring of the torus
   :type minor_segments: int in [3, 256], (optional)
   :arg mode: Dimensions Mode

      * ``MAJOR_MINOR``
        Major/Minor -- Use the major/minor radii for torus dimensions.
      * ``EXT_INT``
        Exterior/Interior -- Use the exterior/interior radii for torus dimensions.
   :type mode: enum in [``'MAJOR_MINOR'``, ``'EXT_INT'``], (optional)
   :arg major_radius: Major Radius, Radius from the origin to the center of the cross sections
   :type major_radius: float in [0, 10000], (optional)
   :arg minor_radius: Minor Radius, Radius of the torus' cross section
   :type minor_radius: float in [0, 10000], (optional)
   :arg abso_major_rad: Exterior Radius, Total Exterior Radius of the torus
   :type abso_major_rad: float in [0, 10000], (optional)
   :arg abso_minor_rad: Interior Radius, Total Interior Radius of the torus
   :type abso_minor_rad: float in [0, 10000], (optional)
   :arg generate_uvs: Generate UVs, Generate a default UV map
   :type generate_uvs: boolean, (optional)
   :File: `startup\bl_operators\add_mesh_torus.py\:222 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\add_mesh_torus.py#L222>`__


.. function:: primitive_uv_sphere_add(*, segments=32, ring_count=16, radius=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

   Construct a spherical mesh with quad faces, except for triangle faces at the top and bottom

   :arg segments: Segments
   :type segments: int in [3, 100000], (optional)
   :arg ring_count: Rings
   :type ring_count: int in [3, 100000], (optional)
   :arg radius: Radius
   :type radius: float in [0, inf], (optional)
   :arg calc_uvs: Generate UVs, Generate a default UV map
   :type calc_uvs: boolean, (optional)
   :arg enter_editmode: Enter Edit Mode, Enter edit mode when adding this object
   :type enter_editmode: boolean, (optional)
   :arg align: Align, The alignment of the new object

      * ``WORLD``
        World -- Align the new object to the world.
      * ``VIEW``
        View -- Align the new object to the view.
      * ``CURSOR``
        3D Cursor -- Use the 3D cursor orientation for the new object.
   :type align: enum in [``'WORLD'``, ``'VIEW'``, ``'CURSOR'``], (optional)
   :arg location: Location, Location for the newly added object
   :type location: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg rotation: Rotation, Rotation for the newly added object
   :type rotation: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], (optional)
   :arg scale: Scale, Scale for the newly added object
   :type scale: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

.. function:: quads_convert_to_tris(*, quad_method='BEAUTY', ngon_method='BEAUTY')

   Triangulate selected faces

   :arg quad_method: Quad Method, Method for splitting the quads into triangles
   :type quad_method: enum in :ref:`rna_enum_modifier_triangulate_quad_method_items`, (optional)
   :arg ngon_method: N-gon Method, Method for splitting the n-gons into triangles
   :type ngon_method: enum in :ref:`rna_enum_modifier_triangulate_ngon_method_items`, (optional)

.. function:: region_to_loop()

   Select boundary edges around the selected faces

.. function:: remove_doubles(*, threshold=0.0001, use_unselected=False, use_sharp_edge_from_normals=False)

   Merge vertices based on their proximity

   :arg threshold: Merge Distance, Maximum distance between elements to merge
   :type threshold: float in [1e-06, 50], (optional)
   :arg use_unselected: Unselected, Merge selected to other unselected vertices
   :type use_unselected: boolean, (optional)
   :arg use_sharp_edge_from_normals: Sharp Edges, Calculate sharp edges using custom normal data (when available)
   :type use_sharp_edge_from_normals: boolean, (optional)

.. function:: reveal(*, select=True)

   Reveal all hidden vertices, edges and faces

   :arg select: Select
   :type select: boolean, (optional)

.. function:: rip(*, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False, use_fill=False)

   Disconnect vertex or edges from connected geometry

   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg use_proportional_edit: Proportional Editing
   :type use_proportional_edit: boolean, (optional)
   :arg proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
   :type proportional_edit_falloff: enum in :ref:`rna_enum_proportional_falloff_items`, (optional)
   :arg proportional_size: Proportional Size
   :type proportional_size: float in [1e-06, inf], (optional)
   :arg use_proportional_connected: Connected
   :type use_proportional_connected: boolean, (optional)
   :arg use_proportional_projected: Projected (2D)
   :type use_proportional_projected: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)
   :arg use_fill: Fill, Fill the ripped region
   :type use_fill: boolean, (optional)

.. function:: rip_edge(*, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, release_confirm=False, use_accurate=False)

   Extend vertices along the edge closest to the cursor

   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg use_proportional_edit: Proportional Editing
   :type use_proportional_edit: boolean, (optional)
   :arg proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing mode
   :type proportional_edit_falloff: enum in :ref:`rna_enum_proportional_falloff_items`, (optional)
   :arg proportional_size: Proportional Size
   :type proportional_size: float in [1e-06, inf], (optional)
   :arg use_proportional_connected: Connected
   :type use_proportional_connected: boolean, (optional)
   :arg use_proportional_projected: Projected (2D)
   :type use_proportional_projected: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: rip_edge_move(*, MESH_OT_rip_edge=None, TRANSFORM_OT_translate=None)

   Extend vertices and move the result

   :arg MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor
   :type MESH_OT_rip_edge: :class:`MESH_OT_rip_edge`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: rip_move(*, MESH_OT_rip=None, TRANSFORM_OT_translate=None)

   Rip polygons and move the result

   :arg MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry
   :type MESH_OT_rip: :class:`MESH_OT_rip`, (optional)
   :arg TRANSFORM_OT_translate: Move, Move selected items
   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: screw(*, steps=9, turns=1, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0))

   Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

   :arg steps: Steps, Steps
   :type steps: int in [1, 100000], (optional)
   :arg turns: Turns, Turns
   :type turns: int in [1, 100000], (optional)
   :arg center: Center, Center in global view space
   :type center: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg axis: Axis, Axis in global view space
   :type axis: :class:`mathutils.Vector` of 3 items in [-1, 1], (optional)

.. function:: select_all(*, action='TOGGLE')

   (De)select all vertices, edges or faces

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: select_axis(*, orientation='LOCAL', sign='POS', axis='X', threshold=0.0001)

   Select all data in the mesh on a single axis

   :arg orientation: Axis Mode, Axis orientation
   :type orientation: enum in :ref:`rna_enum_transform_orientation_items`, (optional)
   :arg sign: Axis Sign, Side to select
   :type sign: enum in [``'POS'``, ``'NEG'``, ``'ALIGN'``], (optional)
   :arg axis: Axis, Select the axis to compare each vertex on
   :type axis: enum in :ref:`rna_enum_axis_xyz_items`, (optional)
   :arg threshold: Threshold
   :type threshold: float in [1e-06, 50], (optional)

.. function:: select_by_attribute()

   Select elements based on the active boolean attribute

.. function:: select_by_pole_count(*, pole_count=4, type='NOTEQUAL', extend=False, exclude_nonmanifold=True)

   Select vertices at poles by the number of connected edges. In edge and face mode the geometry connected to the vertices is selected

   :arg pole_count: Pole Count
   :type pole_count: int in [0, inf], (optional)
   :arg type: Type, Type of comparison to make
   :type type: enum in [``'LESS'``, ``'EQUAL'``, ``'GREATER'``, ``'NOTEQUAL'``], (optional)
   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)
   :arg exclude_nonmanifold: Exclude Non Manifold, Exclude non-manifold poles
   :type exclude_nonmanifold: boolean, (optional)

.. function:: select_face_by_sides(*, number=4, type='EQUAL', extend=True)

   Select vertices or faces by the number of face sides

   :arg number: Number of Vertices
   :type number: int in [3, inf], (optional)
   :arg type: Type, Type of comparison to make
   :type type: enum in [``'LESS'``, ``'EQUAL'``, ``'GREATER'``, ``'NOTEQUAL'``], (optional)
   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: select_interior_faces()

   Select faces where all edges have more than 2 face users

.. function:: select_less(*, use_face_step=True)

   Deselect vertices, edges or faces at the boundary of each selection region

   :arg use_face_step: Face Step, Connected faces (instead of edges)
   :type use_face_step: boolean, (optional)

.. function:: select_linked(*, delimit={'SEAM'})

   Select all vertices connected to the current selection

   :arg delimit: Delimit, Delimit selected region
   :type delimit: enum set in :ref:`rna_enum_mesh_delimit_mode_items`, (optional)

.. function:: select_linked_pick(*, deselect=False, delimit={'SEAM'}, object_index=-1, index=-1)

   (De)select all vertices linked to the edge under the mouse cursor

   :arg deselect: Deselect
   :type deselect: boolean, (optional)
   :arg delimit: Delimit, Delimit selected region
   :type delimit: enum set in :ref:`rna_enum_mesh_delimit_mode_items`, (optional)
   :type object_index: int in [-1, inf], (optional)
   :type index: int in [-1, inf], (optional)

.. function:: select_loose(*, extend=False)

   Select loose geometry based on the selection mode

   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: select_mirror(*, axis={'X'}, extend=False)

   Select mesh items at mirrored locations

   :arg axis: Axis
   :type axis: enum set in :ref:`rna_enum_axis_flag_xyz_items`, (optional)
   :arg extend: Extend, Extend the existing selection
   :type extend: boolean, (optional)

.. function:: select_mode(*, use_extend=False, use_expand=False, type='VERT', action='TOGGLE')

   Change selection mode

   :arg use_extend: Extend
   :type use_extend: boolean, (optional)
   :arg use_expand: Expand
   :type use_expand: boolean, (optional)
   :arg type: Type
   :type type: enum in :ref:`rna_enum_mesh_select_mode_items`, (optional)
   :arg action: Action, Selection action to execute

      * ``DISABLE``
        Disable -- Disable selected markers.
      * ``ENABLE``
        Enable -- Enable selected markers.
      * ``TOGGLE``
        Toggle -- Toggle disabled flag for selected markers.
   :type action: enum in [``'DISABLE'``, ``'ENABLE'``, ``'TOGGLE'``], (optional)

.. function:: select_more(*, use_face_step=True)

   Select more vertices, edges or faces connected to initial selection

   :arg use_face_step: Face Step, Connected faces (instead of edges)
   :type use_face_step: boolean, (optional)

.. function:: select_next_item()

   Select the next element (using selection order)

   :File: `startup\bl_operators\mesh.py\:206 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\mesh.py#L206>`__

.. function:: select_non_manifold(*, extend=True, use_wire=True, use_boundary=True, use_multi_face=True, use_non_contiguous=True, use_verts=True)

   Select all non-manifold vertices or edges

   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)
   :arg use_wire: Wire, Wire edges
   :type use_wire: boolean, (optional)
   :arg use_boundary: Boundaries, Boundary edges
   :type use_boundary: boolean, (optional)
   :arg use_multi_face: Multiple Faces, Edges shared by more than two faces
   :type use_multi_face: boolean, (optional)
   :arg use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions
   :type use_non_contiguous: boolean, (optional)
   :arg use_verts: Vertices, Vertices connecting multiple face regions
   :type use_verts: boolean, (optional)

.. function:: select_nth(*, skip=1, nth=1, offset=0)

   Deselect every Nth element starting from the active vertex, edge or face

   :arg skip: Deselected, Number of deselected elements in the repetitive sequence
   :type skip: int in [1, inf], (optional)
   :arg nth: Selected, Number of selected elements in the repetitive sequence
   :type nth: int in [1, inf], (optional)
   :arg offset: Offset, Offset from the starting point
   :type offset: int in [-inf, inf], (optional)

.. function:: select_prev_item()

   Select the previous element (using selection order)

   :File: `startup\bl_operators\mesh.py\:231 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\mesh.py#L231>`__

.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT')

   Randomly select vertices

   :arg ratio: Ratio, Portion of items to select randomly
   :type ratio: float in [0, 1], (optional)
   :arg seed: Random Seed, Seed for the random number generator
   :type seed: int in [0, inf], (optional)
   :arg action: Action, Selection action to execute

      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
   :type action: enum in [``'SELECT'``, ``'DESELECT'``], (optional)

.. function:: select_similar(*, type='VERT_NORMAL', compare='EQUAL', threshold=0.0)

   Select similar vertices, edges or faces by property types

   :arg type: Type
   :type type: enum in [``'VERT_NORMAL'``, ``'VERT_FACES'``, ``'VERT_GROUPS'``, ``'VERT_EDGES'``, ``'VERT_CREASE'``, ``'EDGE_LENGTH'``, ``'EDGE_DIR'``, ``'EDGE_FACES'``, ``'EDGE_FACE_ANGLE'``, ``'EDGE_CREASE'``, ``'EDGE_BEVEL'``, ``'EDGE_SEAM'``, ``'EDGE_SHARP'``, ``'EDGE_FREESTYLE'``, ``'FACE_MATERIAL'``, ``'FACE_AREA'``, ``'FACE_SIDES'``, ``'FACE_PERIMETER'``, ``'FACE_NORMAL'``, ``'FACE_COPLANAR'``, ``'FACE_SMOOTH'``, ``'FACE_FREESTYLE'``], (optional)
   :arg compare: Compare
   :type compare: enum in [``'EQUAL'``, ``'GREATER'``, ``'LESS'``], (optional)
   :arg threshold: Threshold
   :type threshold: float in [0, 100000], (optional)

.. function:: select_similar_region()

   Select similar face regions to the current selection

.. function:: select_ungrouped(*, extend=False)

   Select vertices without a group

   :arg extend: Extend, Extend the selection
   :type extend: boolean, (optional)

.. function:: separate(*, type='SELECTED')

   Separate selected geometry into a new mesh

   :arg type: Type
   :type type: enum in [``'SELECTED'``, ``'MATERIAL'``, ``'LOOSE'``], (optional)

.. function:: set_normals_from_faces(*, keep_sharp=False)

   Set the custom normals from the selected faces ones

   :arg keep_sharp: Keep Sharp Edges, Do not set sharp edges to face
   :type keep_sharp: boolean, (optional)

.. function:: set_sharpness_by_angle(*, angle=0.523599, extend=False)

   Set edge sharpness based on the angle between neighboring faces

   :arg angle: Angle
   :type angle: float in [0.000174533, 3.14159], (optional)
   :arg extend: Extend, Add new sharp edges without clearing existing sharp edges
   :type extend: boolean, (optional)

.. function:: shape_propagate_to_all()

   Apply selected vertex locations to all other shape keys

.. function:: shortest_path_pick(*, edge_mode='SELECT', use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0, index=-1)

   Select shortest path between two selections

   :arg edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
   :type edge_mode: enum in [``'SELECT'``, ``'SEAM'``, ``'SHARP'``, ``'CREASE'``, ``'BEVEL'``, ``'FREESTYLE'``], (optional)
   :arg use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
   :type use_face_step: boolean, (optional)
   :arg use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
   :type use_topology_distance: boolean, (optional)
   :arg use_fill: Fill Region, Select all paths between the source/destination elements
   :type use_fill: boolean, (optional)
   :arg skip: Deselected, Number of deselected elements in the repetitive sequence
   :type skip: int in [0, inf], (optional)
   :arg nth: Selected, Number of selected elements in the repetitive sequence
   :type nth: int in [1, inf], (optional)
   :arg offset: Offset, Offset from the starting point
   :type offset: int in [-inf, inf], (optional)
   :type index: int in [-1, inf], (optional)

.. function:: shortest_path_select(*, edge_mode='SELECT', use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0)

   Selected shortest path between two vertices/edges/faces

   :arg edge_mode: Edge Tag, The edge flag to tag when selecting the shortest path
   :type edge_mode: enum in [``'SELECT'``, ``'SEAM'``, ``'SHARP'``, ``'CREASE'``, ``'BEVEL'``, ``'FREESTYLE'``], (optional)
   :arg use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
   :type use_face_step: boolean, (optional)
   :arg use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
   :type use_topology_distance: boolean, (optional)
   :arg use_fill: Fill Region, Select all paths between the source/destination elements
   :type use_fill: boolean, (optional)
   :arg skip: Deselected, Number of deselected elements in the repetitive sequence
   :type skip: int in [0, inf], (optional)
   :arg nth: Selected, Number of selected elements in the repetitive sequence
   :type nth: int in [1, inf], (optional)
   :arg offset: Offset, Offset from the starting point
   :type offset: int in [-inf, inf], (optional)

.. function:: smooth_normals(*, factor=0.5)

   Smooth custom normals based on adjacent vertex normals

   :arg factor: Factor, Specifies weight of smooth vs original normal
   :type factor: float in [0, 1], (optional)

.. function:: solidify(*, thickness=0.01)

   Create a solid skin by extruding, compensating for sharp angles

   :arg thickness: Thickness
   :type thickness: float in [-10000, 10000], (optional)

.. function:: sort_elements(*, type='VIEW_ZAXIS', elements={'VERT'}, reverse=False, seed=0)

   The order of selected vertices/edges/faces is modified, based on a given method

   :arg type: Type, Type of reordering operation to apply

      * ``VIEW_ZAXIS``
        View Z Axis -- Sort selected elements from farthest to nearest one in current view.
      * ``VIEW_XAXIS``
        View X Axis -- Sort selected elements from left to right one in current view.
      * ``CURSOR_DISTANCE``
        Cursor Distance -- Sort selected elements from nearest to farthest from 3D cursor.
      * ``MATERIAL``
        Material -- Sort selected faces from smallest to greatest material index.
      * ``SELECTED``
        Selected -- Move all selected elements in first places, preserving their relative order.
        Warning: This will affect unselected elements' indices as well.
      * ``RANDOMIZE``
        Randomize -- Randomize order of selected elements.
      * ``REVERSE``
        Reverse -- Reverse current order of selected elements.
   :type type: enum in [``'VIEW_ZAXIS'``, ``'VIEW_XAXIS'``, ``'CURSOR_DISTANCE'``, ``'MATERIAL'``, ``'SELECTED'``, ``'RANDOMIZE'``, ``'REVERSE'``], (optional)
   :arg elements: Elements, Which elements to affect (vertices, edges and/or faces)
   :type elements: enum set in {``'VERT'``, ``'EDGE'``, ``'FACE'``}, (optional)
   :arg reverse: Reverse, Reverse the sorting effect
   :type reverse: boolean, (optional)
   :arg seed: Seed, Seed for random-based operations
   :type seed: int in [0, inf], (optional)

.. function:: spin(*, steps=12, dupli=False, angle=1.5708, use_auto_merge=True, use_normal_flip=False, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0))

   Extrude selected vertices in a circle around the cursor in indicated viewport

   :arg steps: Steps, Steps
   :type steps: int in [0, 1000000], (optional)
   :arg dupli: Use Duplicates
   :type dupli: boolean, (optional)
   :arg angle: Angle, Rotation for each step
   :type angle: float in [-inf, inf], (optional)
   :arg use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution
   :type use_auto_merge: boolean, (optional)
   :arg use_normal_flip: Flip Normals
   :type use_normal_flip: boolean, (optional)
   :arg center: Center, Center in global view space
   :type center: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg axis: Axis, Axis in global view space
   :type axis: :class:`mathutils.Vector` of 3 items in [-1, 1], (optional)

.. function:: split()

   Split off selected geometry from connected unselected geometry

.. function:: split_normals()

   Split custom normals of selected vertices

.. function:: subdivide(*, number_cuts=1, smoothness=0.0, ngon=True, quadcorner='STRAIGHT_CUT', fractal=0.0, fractal_along_normal=0.0, seed=0)

   Subdivide selected edges

   :arg number_cuts: Number of Cuts
   :type number_cuts: int in [1, 100], (optional)
   :arg smoothness: Smoothness, Smoothness factor
   :type smoothness: float in [0, 1000], (optional)
   :arg ngon: Create N-Gons, When disabled, newly created faces are limited to 3 and 4 sided faces
   :type ngon: boolean, (optional)
   :arg quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent n-gons)
   :type quadcorner: enum in [``'INNERVERT'``, ``'PATH'``, ``'STRAIGHT_CUT'``, ``'FAN'``], (optional)
   :arg fractal: Fractal, Fractal randomness factor
   :type fractal: float in [0, 1e+06], (optional)
   :arg fractal_along_normal: Along Normal, Apply fractal displacement along normal only
   :type fractal_along_normal: float in [0, 1], (optional)
   :arg seed: Random Seed, Seed for the random number generator
   :type seed: int in [0, inf], (optional)

.. function:: subdivide_edgering(*, number_cuts=10, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH')

   Subdivide perpendicular edges to the selected edge-ring

   :arg number_cuts: Number of Cuts
   :type number_cuts: int in [0, 1000], (optional)
   :arg interpolation: Interpolation, Interpolation method
   :type interpolation: enum in [``'LINEAR'``, ``'PATH'``, ``'SURFACE'``], (optional)
   :arg smoothness: Smoothness, Smoothness factor
   :type smoothness: float in [0, 1000], (optional)
   :arg profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
   :type profile_shape_factor: float in [-1000, 1000], (optional)
   :arg profile_shape: Profile Shape, Shape of the profile
   :type profile_shape: enum in :ref:`rna_enum_proportional_falloff_curve_only_items`, (optional)

.. function:: symmetrize(*, direction='NEGATIVE_X', threshold=0.0001)

   Enforce symmetry (both form and topological) across an axis

   :arg direction: Direction, Which sides to copy from and to
   :type direction: enum in :ref:`rna_enum_symmetrize_direction_items`, (optional)
   :arg threshold: Threshold, Limit for snap middle vertices to the axis center
   :type threshold: float in [0, 10], (optional)

.. function:: symmetry_snap(*, direction='NEGATIVE_X', threshold=0.05, factor=0.5, use_center=True)

   Snap vertex pairs to their mirrored locations

   :arg direction: Direction, Which sides to copy from and to
   :type direction: enum in :ref:`rna_enum_symmetrize_direction_items`, (optional)
   :arg threshold: Threshold, Distance within which matching vertices are searched
   :type threshold: float in [0, 10], (optional)
   :arg factor: Factor, Mix factor of the locations of the vertices
   :type factor: float in [0, 1], (optional)
   :arg use_center: Center, Snap middle vertices to the axis center
   :type use_center: boolean, (optional)

.. function:: tris_convert_to_quads(*, face_threshold=0.698132, shape_threshold=0.698132, topology_influence=0.0, uvs=False, vcols=False, seam=False, sharp=False, materials=False, deselect_joined=False)

   Merge triangles into four sided polygons where possible

   :arg face_threshold: Max Face Angle, Face angle limit
   :type face_threshold: float in [0, 3.14159], (optional)
   :arg shape_threshold: Max Shape Angle, Shape angle limit
   :type shape_threshold: float in [0, 3.14159], (optional)
   :arg topology_influence: Topology Influence, How much to prioritize regular grids of quads as well as quads that touch existing quads
   :type topology_influence: float in [0, 2], (optional)
   :arg uvs: Compare UVs
   :type uvs: boolean, (optional)
   :arg vcols: Compare Color Attributes
   :type vcols: boolean, (optional)
   :arg seam: Compare Seam
   :type seam: boolean, (optional)
   :arg sharp: Compare Sharp
   :type sharp: boolean, (optional)
   :arg materials: Compare Materials
   :type materials: boolean, (optional)
   :arg deselect_joined: Deselect Joined, Only select remaining triangles that were not merged
   :type deselect_joined: boolean, (optional)

.. function:: unsubdivide(*, iterations=2)

   Un-subdivide selected edges and faces

   :arg iterations: Iterations, Number of times to un-subdivide
   :type iterations: int in [1, 1000], (optional)

.. function:: uv_texture_add()

   Add UV map

.. function:: uv_texture_remove()

   Remove UV map

.. function:: uvs_reverse()

   Flip direction of UV coordinates inside faces

.. function:: uvs_rotate(*, use_ccw=False)

   Rotate UV coordinates inside faces

   :arg use_ccw: Counter Clockwise
   :type use_ccw: boolean, (optional)

.. function:: vert_connect()

   Connect selected vertices of faces, splitting the face

.. function:: vert_connect_concave()

   Make all faces convex

.. function:: vert_connect_nonplanar(*, angle_limit=0.0872665)

   Split non-planar faces that exceed the angle threshold

   :arg angle_limit: Max Angle, Angle limit
   :type angle_limit: float in [0, 3.14159], (optional)

.. function:: vert_connect_path()

   Connect vertices by their selection order, creating edges, splitting faces

.. function:: vertices_smooth(*, factor=0.0, repeat=1, xaxis=True, yaxis=True, zaxis=True, wait_for_input=True)

   Flatten angles of selected vertices

   :arg factor: Smoothing, Smoothing factor
   :type factor: float in [-10, 10], (optional)
   :arg repeat: Repeat, Number of times to smooth the mesh
   :type repeat: int in [1, 1000], (optional)
   :arg xaxis: X-Axis, Smooth along the X axis
   :type xaxis: boolean, (optional)
   :arg yaxis: Y-Axis, Smooth along the Y axis
   :type yaxis: boolean, (optional)
   :arg zaxis: Z-Axis, Smooth along the Z axis
   :type zaxis: boolean, (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)

.. function:: vertices_smooth_laplacian(*, repeat=1, lambda_factor=1.0, lambda_border=5e-05, use_x=True, use_y=True, use_z=True, preserve_volume=True)

   Laplacian smooth of selected vertices

   :arg repeat: Number of iterations to smooth the mesh
   :type repeat: int in [1, 1000], (optional)
   :arg lambda_factor: Lambda factor
   :type lambda_factor: float in [1e-07, 1000], (optional)
   :arg lambda_border: Lambda factor in border
   :type lambda_border: float in [1e-07, 1000], (optional)
   :arg use_x: Smooth X Axis, Smooth object along X axis
   :type use_x: boolean, (optional)
   :arg use_y: Smooth Y Axis, Smooth object along Y axis
   :type use_y: boolean, (optional)
   :arg use_z: Smooth Z Axis, Smooth object along Z axis
   :type use_z: boolean, (optional)
   :arg preserve_volume: Preserve Volume, Apply volume preservation after smooth
   :type preserve_volume: boolean, (optional)

.. function:: wireframe(*, use_boundary=True, use_even_offset=True, use_relative_offset=False, use_replace=True, thickness=0.01, offset=0.01, use_crease=False, crease_weight=0.01)

   Create a solid wireframe from faces

   :arg use_boundary: Boundary, Inset face boundaries
   :type use_boundary: boolean, (optional)
   :arg use_even_offset: Offset Even, Scale the offset to give more even thickness
   :type use_even_offset: boolean, (optional)
   :arg use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
   :type use_relative_offset: boolean, (optional)
   :arg use_replace: Replace, Remove original faces
   :type use_replace: boolean, (optional)
   :arg thickness: Thickness
   :type thickness: float in [0, 10000], (optional)
   :arg offset: Offset
   :type offset: float in [0, 10000], (optional)
   :arg use_crease: Crease, Crease hub edges for an improved subdivision surface
   :type use_crease: boolean, (optional)
   :arg crease_weight: Crease Weight
   :type crease_weight: float in [0, 1000], (optional)

