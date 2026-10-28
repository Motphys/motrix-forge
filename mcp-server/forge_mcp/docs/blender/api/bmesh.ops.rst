
BMesh Operators (bmesh.ops)
===========================

.. module:: bmesh.ops

This module gives access to low level bmesh operations.

Most operators take input and return output, they can be chained together
to perform useful operations.


Operator Example
++++++++++++++++
This script shows how operators can be used to model a link of a chain.

.. literalinclude:: __/examples/bmesh.ops.1.py
.. function:: smooth_vert(bm, verts=[], factor=0, mirror_clip_x=False, mirror_clip_y=False, mirror_clip_z=False, clip_dist=0, use_axis_x=False, use_axis_y=False, use_axis_z=False)

   Vertex Smooth.

   Smooths vertices by using a basic vertex averaging scheme.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg factor:
      Smoothing factor.
   :type factor: float
   :arg mirror_clip_x:
      Set vertices close to the x axis before the operation to 0.
   :type mirror_clip_x: bool
   :arg mirror_clip_y:
      Set vertices close to the y axis before the operation to 0.
   :type mirror_clip_y: bool
   :arg mirror_clip_z:
      Set vertices close to the z axis before the operation to 0.
   :type mirror_clip_z: bool
   :arg clip_dist:
      Clipping threshold for the above three slots.
   :type clip_dist: float
   :arg use_axis_x:
      Smooth vertices along X axis.
   :type use_axis_x: bool
   :arg use_axis_y:
      Smooth vertices along Y axis.
   :type use_axis_y: bool
   :arg use_axis_z:
      Smooth vertices along Z axis.
   :type use_axis_z: bool


.. function:: smooth_laplacian_vert(bm, verts=[], lambda_factor=0, lambda_border=0, use_x=False, use_y=False, use_z=False, preserve_volume=False)

   Vertex Smooth Laplacian.

   Smooths vertices by using Laplacian smoothing propose by.
   Desbrun, et al. Implicit Fairing of Irregular Meshes using Diffusion and Curvature Flow.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg lambda_factor:
      Lambda parameter.
   :type lambda_factor: float
   :arg lambda_border:
      Lambda param in border.
   :type lambda_border: float
   :arg use_x:
      Smooth object along X axis.
   :type use_x: bool
   :arg use_y:
      Smooth object along Y axis.
   :type use_y: bool
   :arg use_z:
      Smooth object along Z axis.
   :type use_z: bool
   :arg preserve_volume:
      Apply volume preservation after smooth.
   :type preserve_volume: bool


.. function:: recalc_face_normals(bm, faces=[])

   Right-Hand Faces.

   Computes an "outside" normal for the specified input faces.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)


.. function:: planar_faces(bm, faces=[], iterations=0, factor=0)

   Planar Faces.

   Iteratively flatten faces.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input geometry.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg iterations:
      Number of times to flatten faces (for when connected faces are used)
   :type iterations: int
   :arg factor:
      Influence for making planar each iteration
   :type factor: float
   :return:

      - ``geom``:
        Output slot, computed boundary geometry.

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: region_extend(bm, geom=[], use_contract=False, use_faces=False, use_face_step=False)

   Region Extend.

   used to implement the select more/less tools.
   this puts some geometry surrounding regions of
   geometry in geom into geom.out.

   if use_faces is 0 then geom.out spits out verts and edges,
   otherwise it spits out faces.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input geometry.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg use_contract:
      Find boundary inside the regions, not outside.
   :type use_contract: bool
   :arg use_faces:
      Extend from faces instead of edges.
   :type use_faces: bool
   :arg use_face_step:
      Step over connected faces.
   :type use_face_step: bool
   :return:

      - ``geom``:
        Output slot, computed boundary geometry.

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: rotate_edges(bm, edges=[], use_ccw=False)

   Edge Rotate.

   Rotates edges topologically. Also known as "spin edge" to some people.
   Simple example: ``[/] becomes [|] then [\]``.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg use_ccw:
      Rotate edge counter-clockwise if true, otherwise clockwise.
   :type use_ccw: bool
   :return:

      - ``edges``:
        Newly spun edges.

        **type** list of (:class:`bmesh.types.BMEdge`)

   :rtype: dict[str, Any]


.. function:: reverse_faces(bm, faces=[], flip_multires=False)

   Reverse Faces.

   Reverses the winding (vertex order) of faces.
   This has the effect of flipping the normal.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg flip_multires:
      Maintain multi-res offset.
   :type flip_multires: bool


.. function:: flip_quad_tessellation(bm, faces=[])

   Flip Quad Tessellation

   Flip the tessellation direction of the selected quads.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)


.. function:: bisect_edges(bm, edges=[], cuts=0, edge_percents={})

   Edge Bisect.

   Splits input edges (but doesn't do anything else).
   This creates a 2-valence vert.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg cuts:
      Number of cuts.
   :type cuts: int
   :arg edge_percents:
      Undocumented.
   :type edge_percents: dict mapping vert/edge/face types to float
   :return:

      - ``geom_split``:
        Newly created vertices and edges.

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: mirror(bm, geom=[], matrix=mathutils.Matrix.Identity(4), merge_dist=0, axis='X', mirror_u=False, mirror_v=False, mirror_udim=False, use_shapekey=False)

   Mirror.

   Mirrors geometry along an axis. The resulting geometry is welded on using
   merge_dist. Pairs of original/mirrored vertices are welded using the merge_dist
   parameter (which defines the minimum distance for welding to happen).

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input geometry.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg matrix:
      Matrix defining the mirror transformation.
   :type matrix: :class:`mathutils.Matrix`
   :arg merge_dist:
      Maximum distance for merging. does no merging if 0.
   :type merge_dist: float
   :arg axis:
      The axis to use.
   :type axis: enum in ['X', 'Y', 'Z'], default 'X'
   :arg mirror_u:
      Mirror UVs across the u axis.
   :type mirror_u: bool
   :arg mirror_v:
      Mirror UVs across the v axis.
   :type mirror_v: bool
   :arg mirror_udim:
      Mirror UVs in each tile.
   :type mirror_udim: bool
   :arg use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool
   :return:

      - ``geom``:
        Output geometry, mirrored.

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: find_doubles(bm, verts=[], keep_verts=[], dist=0)

   Find Doubles.

   Takes input verts and find vertices they should weld to.
   Outputs a mapping slot suitable for use with the weld verts BMOP.

   If keep_verts is used, vertices outside that set can only be merged
   with vertices in that set.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg keep_verts:
      List of verts to keep.
   :type keep_verts: list of (:class:`bmesh.types.BMVert`)
   :arg dist:
      Maximum distance.
   :type dist: float
   :return:

      - ``targetmap``:


        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`

   :rtype: dict[str, Any]


.. function:: remove_doubles(bm, verts=[], dist=0)

   Remove Doubles.

   Finds groups of vertices closer than dist and merges them together,
   using the weld verts BMOP.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input verts.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg dist:
      Minimum distance.
   :type dist: float


.. function:: collapse(bm, edges=[], uvs=False)

   Collapse Connected.

   Collapses connected vertices

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg uvs:
      Also collapse UVs and such.
   :type uvs: bool


.. function:: pointmerge_facedata(bm, verts=[], vert_snap)

   Face-Data Point Merge.

   Merge uv/vcols at a specific vertex.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg vert_snap:
      Snap vertex.
   :type vert_snap: :class:`bmesh.types.BMVert`


.. function:: average_vert_facedata(bm, verts=[])

   Average Vertices Face-vert Data.

   Merge uv/vcols associated with the input vertices at
   the bounding box center. (I know, it's not averaging but
   the vert_snap_to_bb_center is just too long).

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)


.. function:: pointmerge(bm, verts=[], merge_co=mathutils.Vector())

   Point Merge.

   Merge verts together at a point.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices (all verts will be merged into the first).
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg merge_co:
      Position to merge at.
   :type merge_co: :class:`mathutils.Vector` or any sequence of 3 floats


.. function:: collapse_uvs(bm, edges=[])

   Collapse Connected UVs.

   Collapses connected UV vertices.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)


.. function:: weld_verts(bm, targetmap={})

   Weld Verts.

   Welds verts together (kind-of like remove doubles, merge, etc, all of which
   use or will use this BMOP). You pass in mappings from vertices to the vertices
   they weld with.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg targetmap:
      Maps welded vertices to verts they should weld to.
   :type targetmap: dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`


.. function:: create_vert(bm, co=mathutils.Vector())

   Make Vertex.

   Creates a single vertex; this BMOP was necessary
   for click-create-vertex.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg co:
      The coordinate of the new vert.
   :type co: :class:`mathutils.Vector` or any sequence of 3 floats
   :return:

      - ``vert``:
        The new vert.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: join_triangles(bm, faces=[], cmp_seam=False, cmp_sharp=False, cmp_uvs=False, cmp_vcols=False, cmp_materials=False, angle_face_threshold=0, angle_shape_threshold=0, topology_influence=0, deselect_joined=False, merge_limit=0, neighbor_debug=0)

   Join Triangles.

   Tries to intelligently join triangles according
   to angle threshold and delimiters.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input geometry.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg cmp_seam:
      Compare seam
   :type cmp_seam: bool
   :arg cmp_sharp:
      Compare sharp
   :type cmp_sharp: bool
   :arg cmp_uvs:
      Compare UVs
   :type cmp_uvs: bool
   :arg cmp_vcols:
      Compare VCols.
   :type cmp_vcols: bool
   :arg cmp_materials:
      Compare materials.
   :type cmp_materials: bool
   :arg angle_face_threshold:
      Undocumented.
   :type angle_face_threshold: float
   :arg angle_shape_threshold:
      Undocumented.
   :type angle_shape_threshold: float
   :arg topology_influence:
      Undocumented.
   :type topology_influence: float
   :arg deselect_joined:
      Undocumented.
   :type deselect_joined: bool
   :arg merge_limit:
      Undocumented.
   :type merge_limit: int
   :arg neighbor_debug:
      Undocumented.
   :type neighbor_debug: int
   :return:

      - ``faces``:
        Joined faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: contextual_create(bm, geom=[], mat_nr=0, use_smooth=False)

   Contextual Create.

   This is basically F-key, it creates
   new faces from vertices, makes stuff from edge nets,
   makes wire edges, etc. It also dissolves faces.

   Three verts become a triangle, four become a quad. Two
   become a wire edge.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input geometry.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg mat_nr:
      Material to use.
   :type mat_nr: int
   :arg use_smooth:
      Smooth to use.
   :type use_smooth: bool
   :return:

      - ``faces``:
        Newly-made face(s).

        **type** list of (:class:`bmesh.types.BMFace`)
      - ``edges``:
        Newly-made edge(s).

        **type** list of (:class:`bmesh.types.BMEdge`)

   :rtype: dict[str, Any]


.. function:: bridge_loops(bm, edges=[], use_pairs=False, use_cyclic=False, use_merge=False, merge_factor=0, twist_offset=0)

   Bridge edge loops with faces.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg use_pairs:
      Undocumented.
   :type use_pairs: bool
   :arg use_cyclic:
      Undocumented.
   :type use_cyclic: bool
   :arg use_merge:
      Merge rather than creating faces.
   :type use_merge: bool
   :arg merge_factor:
      merge factor
   :type merge_factor: float
   :arg twist_offset:
      Twist offset for closed loops.
   :type twist_offset: int
   :return:

      - ``faces``:
        New faces.

        **type** list of (:class:`bmesh.types.BMFace`)
      - ``edges``:
        New edges.

        **type** list of (:class:`bmesh.types.BMEdge`)

   :rtype: dict[str, Any]


.. function:: grid_fill(bm, edges=[], mat_nr=0, use_smooth=False, use_interp_simple=False)

   Grid Fill.

   Create faces defined by 2 disconnected edge loops (which share edges).

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg mat_nr:
      Material to use.
   :type mat_nr: int
   :arg use_smooth:
      Smooth state to use.
   :type use_smooth: bool
   :arg use_interp_simple:
      Use simple interpolation.
   :type use_interp_simple: bool
   :return:

      - ``faces``:
        New faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: holes_fill(bm, edges=[], sides=0)

   Fill Holes.

   Fill boundary edges with faces, copying surrounding custom-data.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg sides:
      Number of face sides to fill.
   :type sides: int
   :return:

      - ``faces``:
        New faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: face_attribute_fill(bm, faces=[], use_normals=False, use_data=False)

   Face Attribute Fill.

   Fill in faces with data from adjacent faces.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg use_normals:
      Copy face winding.
   :type use_normals: bool
   :arg use_data:
      Copy face data.
   :type use_data: bool
   :return:

      - ``faces_fail``:
        Faces that could not be handled.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: edgeloop_fill(bm, edges=[], mat_nr=0, use_smooth=False)

   Edge Loop Fill.

   Create faces defined by one or more non overlapping edge loops.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg mat_nr:
      Material to use.
   :type mat_nr: int
   :arg use_smooth:
      Smooth state to use.
   :type use_smooth: bool
   :return:

      - ``faces``:
        New faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: edgenet_fill(bm, edges=[], mat_nr=0, use_smooth=False, sides=0)

   Edge Net Fill.

   Create faces defined by enclosed edges.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg mat_nr:
      Material to use.
   :type mat_nr: int
   :arg use_smooth:
      Smooth state to use.
   :type use_smooth: bool
   :arg sides:
      Number of sides.
   :type sides: int
   :return:

      - ``faces``:
        New faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: edgenet_prepare(bm, edges=[])

   Edge-net Prepare.

   Identifies several useful edge loop cases and modifies them so
   they'll become a face when edgenet_fill is called. The cases covered are:

   - One single loop; an edge is added to connect the ends
   - Two loops; two edges are added to connect the endpoints (based on the
     shortest distance between each endpoint).

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :return:

      - ``edges``:
        New edges.

        **type** list of (:class:`bmesh.types.BMEdge`)

   :rtype: dict[str, Any]


.. function:: rotate(bm, cent=mathutils.Vector(), matrix=mathutils.Matrix.Identity(4), verts=[], space=mathutils.Matrix.Identity(4), use_shapekey=False)

   Rotate.

   Rotate vertices around a center, using a 3x3 rotation matrix.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg cent:
      Center of rotation.
   :type cent: :class:`mathutils.Vector` or any sequence of 3 floats
   :arg matrix:
      Matrix defining rotation.
   :type matrix: :class:`mathutils.Matrix`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :arg use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool


.. function:: translate(bm, vec=mathutils.Vector(), space=mathutils.Matrix.Identity(4), verts=[], use_shapekey=False)

   Translate.

   Translate vertices by an offset.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg vec:
      Translation offset.
   :type vec: :class:`mathutils.Vector` or any sequence of 3 floats
   :arg space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool


.. function:: scale(bm, vec=mathutils.Vector(), space=mathutils.Matrix.Identity(4), verts=[], use_shapekey=False)

   Scale.

   Scales vertices by an offset.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg vec:
      Scale factor.
   :type vec: :class:`mathutils.Vector` or any sequence of 3 floats
   :arg space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool


.. function:: transform(bm, matrix=mathutils.Matrix.Identity(4), space=mathutils.Matrix.Identity(4), verts=[], use_shapekey=False)

   Transform.

   Transforms a set of vertices by a matrix. Multiplies
   the vertex coordinates with the matrix.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg matrix:
      Transform matrix.
   :type matrix: :class:`mathutils.Matrix`
   :arg space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool


.. function:: object_load_bmesh(bm, scene, object)

   Object Load BMesh.

   Loads a bmesh into an object/mesh. This is a "private"
   BMOP.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg scene:
      Pointer to an scene structure.
   :type scene: :class:`bpy.types.Scene`
   :arg object:
      Pointer to an object structure.
   :type object: :class:`bpy.types.Object`


.. function:: bmesh_to_mesh(bm, mesh, object)

   BMesh to Mesh.

   Converts a bmesh to a Mesh. This is reserved for exiting edit-mode.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg mesh:
      Pointer to a mesh structure to fill in.
   :type mesh: :class:`bpy.types.Mesh`
   :arg object:
      Pointer to an object structure.
   :type object: :class:`bpy.types.Object`


.. function:: mesh_to_bmesh(bm, mesh, object, use_shapekey=False)

   Mesh to BMesh.

   Load the contents of a mesh into the bmesh. this BMOP is private, it's
   reserved exclusively for entering edit-mode.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg mesh:
      Pointer to a Mesh structure.
   :type mesh: :class:`bpy.types.Mesh`
   :arg object:
      Pointer to an Object structure.
   :type object: :class:`bpy.types.Object`
   :arg use_shapekey:
      Load active shapekey coordinates into verts.
   :type use_shapekey: bool


.. function:: extrude_discrete_faces(bm, faces=[], use_normal_flip=False, use_select_history=False)

   Individual Face Extrude.

   Extrudes faces individually.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg use_normal_flip:
      Create faces with reversed direction.
   :type use_normal_flip: bool
   :arg use_select_history:
      Pass to duplicate.
   :type use_select_history: bool
   :return:

      - ``faces``:
        Output faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: extrude_edge_only(bm, edges=[], use_normal_flip=False, use_select_history=False)

   Extrude Only Edges.

   Extrudes Edges into faces, note that this is very simple, there's no fancy
   winged extrusion.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input vertices.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg use_normal_flip:
      Create faces with reversed direction.
   :type use_normal_flip: bool
   :arg use_select_history:
      Pass to duplicate.
   :type use_select_history: bool
   :return:

      - ``geom``:
        Output geometry.

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: extrude_vert_indiv(bm, verts=[], use_select_history=False)

   Individual Vertex Extrude.

   Extrudes wire edges from vertices.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg use_select_history:
      Pass to duplicate.
   :type use_select_history: bool
   :return:

      - ``edges``:
        Output wire edges.

        **type** list of (:class:`bmesh.types.BMEdge`)
      - ``verts``:
        Output vertices.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: connect_verts(bm, verts=[], faces_exclude=[], check_degenerate=False)

   Connect Verts.

   Split faces by adding edges that connect **verts**.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg faces_exclude:
      Input faces to explicitly exclude from connecting.
   :type faces_exclude: list of (:class:`bmesh.types.BMFace`)
   :arg check_degenerate:
      Prevent splits with overlaps & intersections.
   :type check_degenerate: bool
   :return:

      - ``edges``:


        **type** list of (:class:`bmesh.types.BMEdge`)

   :rtype: dict[str, Any]


.. function:: connect_verts_concave(bm, faces=[])

   Connect Verts to form Convex Faces.

   Ensures all faces are convex **faces**.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :return:

      - ``edges``:


        **type** list of (:class:`bmesh.types.BMEdge`)
      - ``faces``:


        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: connect_verts_nonplanar(bm, angle_limit=0, faces=[])

   Connect Verts Across non Planer Faces.

   Split faces by connecting edges along non planer **faces**.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg angle_limit:
      Total rotation angle (radians).
   :type angle_limit: float
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :return:

      - ``edges``:


        **type** list of (:class:`bmesh.types.BMEdge`)
      - ``faces``:


        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: connect_vert_pair(bm, verts=[], verts_exclude=[], faces_exclude=[])

   Connect Verts.

   Split faces by adding edges that connect **verts**.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg verts_exclude:
      Input vertices to explicitly exclude from connecting.
   :type verts_exclude: list of (:class:`bmesh.types.BMVert`)
   :arg faces_exclude:
      Input faces to explicitly exclude from connecting.
   :type faces_exclude: list of (:class:`bmesh.types.BMFace`)
   :return:

      - ``edges``:


        **type** list of (:class:`bmesh.types.BMEdge`)

   :rtype: dict[str, Any]


.. function:: extrude_face_region(bm, geom=[], edges_exclude=set(), use_keep_orig=False, use_normal_flip=False, use_normal_from_adjacent=False, use_dissolve_ortho_edges=False, use_select_history=False)

   Extrude Faces.

   Extrude operator (does not transform)

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Edges and faces.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg edges_exclude:
      Input edges to explicitly exclude from extrusion.
   :type edges_exclude: set of vert/edge/face type
   :arg use_keep_orig:
      Keep original geometry (requires ``geom`` to include edges).
   :type use_keep_orig: bool
   :arg use_normal_flip:
      Create faces with reversed direction.
   :type use_normal_flip: bool
   :arg use_normal_from_adjacent:
      Use winding from surrounding faces instead of this region.
   :type use_normal_from_adjacent: bool
   :arg use_dissolve_ortho_edges:
      Dissolve edges whose faces form a flat surface.
   :type use_dissolve_ortho_edges: bool
   :arg use_select_history:
      Pass to duplicate.
   :type use_select_history: bool
   :return:

      - ``geom``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: dissolve_verts(bm, verts=[], use_face_split=False, use_boundary_tear=False)

   Dissolve Verts.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg use_face_split:
      Split off face corners to maintain surrounding geometry.
   :type use_face_split: bool
   :arg use_boundary_tear:
      Split off face corners instead of merging faces.
   :type use_boundary_tear: bool


.. function:: dissolve_edges(bm, edges=[], use_verts=False, use_face_split=False, angle_threshold=0)

   Dissolve Edges.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg use_verts:
      Dissolve verts left between only 2 edges.
   :type use_verts: bool
   :arg use_face_split:
      Split off face corners to maintain surrounding geometry.
   :type use_face_split: bool
   :arg angle_threshold:
      Do not dissolve verts between 2 edges when their angle exceeds this threshold.
      Disabled by default.
   :type angle_threshold: float
   :return:

      - ``region``:


        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: dissolve_faces(bm, faces=[], use_verts=False)

   Dissolve Faces.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg use_verts:
      Dissolve verts left between only 2 edges.
   :type use_verts: bool
   :return:

      - ``region``:


        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: dissolve_limit(bm, angle_limit=0, use_dissolve_boundaries=False, verts=[], edges=[], delimit=set())

   Limited Dissolve.

   Dissolve planar faces and co-linear edges.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg angle_limit:
      Total rotation angle (radians).
   :type angle_limit: float
   :arg use_dissolve_boundaries:
      Dissolve all vertices in between face boundaries.
   :type use_dissolve_boundaries: bool
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg delimit:
      Delimit dissolve operation.
   :type delimit: set of flags from ['NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'], default set()
   :return:

      - ``region``:


        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: dissolve_degenerate(bm, dist=0, edges=[])

   Degenerate Dissolve.

   Dissolve edges with no length, faces with no area.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg dist:
      Maximum distance to consider degenerate.
   :type dist: float
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)


.. function:: triangulate(bm, faces=[], quad_method='BEAUTY', ngon_method='BEAUTY')

   Triangulate.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg quad_method:
      Method for splitting the quads into triangles.
   :type quad_method: enum in ['BEAUTY', 'FIXED', 'ALTERNATE', 'SHORT_EDGE', 'LONG_EDGE'], default 'BEAUTY'
   :arg ngon_method:
      Method for splitting the polygons into triangles.
   :type ngon_method: enum in ['BEAUTY', 'EAR_CLIP'], default 'BEAUTY'
   :return:

      - ``edges``:


        **type** list of (:class:`bmesh.types.BMEdge`)
      - ``faces``:


        **type** list of (:class:`bmesh.types.BMFace`)
      - ``face_map``:


        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`
      - ``face_map_double``:
        Duplicate faces.

        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`

   :rtype: dict[str, Any]


.. function:: unsubdivide(bm, verts=[], iterations=0)

   Un-Subdivide.

   Reduce detail in geometry containing grids.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg verts:
      Input vertices.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg iterations:
      Number of times to unsubdivide.
   :type iterations: int


.. function:: subdivide_edges(bm, edges=[], smooth=0, smooth_falloff='SMOOTH', fractal=0, along_normal=0, cuts=0, seed=0, custom_patterns={}, edge_percents={}, quad_corner_type='STRAIGHT_CUT', use_grid_fill=False, use_single_edge=False, use_only_quads=False, use_sphere=False, use_smooth_even=False)

   Subdivide Edges.

   Advanced operator for subdividing edges
   with options for face patterns, smoothing and randomization.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg smooth:
      Smoothness factor.
   :type smooth: float
   :arg smooth_falloff:
      Smooth falloff type.
   :type smooth_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'SHARP', 'LINEAR', 'INVERSE_SQUARE'], default 'SMOOTH'
   :arg fractal:
      Fractal randomness factor.
   :type fractal: float
   :arg along_normal:
      Apply fractal displacement along normal only.
   :type along_normal: float
   :arg cuts:
      Number of cuts.
   :type cuts: int
   :arg seed:
      Seed for the random number generator.
   :type seed: int
   :arg custom_patterns:
      Uses custom pointers.
   :type custom_patterns: dict mapping vert/edge/face types to unknown internal data, not compatible with Python
   :arg edge_percents:
      Undocumented.
   :type edge_percents: dict mapping vert/edge/face types to float
   :arg quad_corner_type:
      Quad corner type.
   :type quad_corner_type: enum in ['STRAIGHT_CUT', 'INNER_VERT', 'PATH', 'FAN'], default 'STRAIGHT_CUT'
   :arg use_grid_fill:
      Fill in fully-selected faces with a grid.
   :type use_grid_fill: bool
   :arg use_single_edge:
      Tessellate the case of one edge selected in a quad or triangle.
   :type use_single_edge: bool
   :arg use_only_quads:
      Only subdivide quads (for loop-cut).
   :type use_only_quads: bool
   :arg use_sphere:
      For making new primitives only.
   :type use_sphere: bool
   :arg use_smooth_even:
      Maintain even offset when smoothing.
   :type use_smooth_even: bool
   :return:

      - ``geom_inner``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
      - ``geom_split``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
      - ``geom``:
        Contains all output geometry.

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: subdivide_edgering(bm, edges=[], interp_mode='LINEAR', smooth=0, cuts=0, profile_shape='SMOOTH', profile_shape_factor=0)

   Subdivide Edge-Ring.

   Take an edge-ring, and subdivide with interpolation options.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input vertices.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg interp_mode:
      Interpolation method.
   :type interp_mode: enum in ['LINEAR', 'PATH', 'SURFACE'], default 'LINEAR'
   :arg smooth:
      Smoothness factor.
   :type smooth: float
   :arg cuts:
      Number of cuts.
   :type cuts: int
   :arg profile_shape:
      Profile shape type.
   :type profile_shape: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'SHARP', 'LINEAR', 'INVERSE_SQUARE'], default 'SMOOTH'
   :arg profile_shape_factor:
      How much intermediary new edges are shrunk/expanded.
   :type profile_shape_factor: float
   :return:

      - ``faces``:
        Output faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: bisect_plane(bm, geom=[], dist=0, plane_co=mathutils.Vector(), plane_no=mathutils.Vector(), use_snap_center=False, clear_outer=False, clear_inner=False)

   Bisect Plane.

   Bisects the mesh by a plane (cut the mesh in half).

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input geometry.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg dist:
      Minimum distance when testing if a vert is exactly on the plane.
   :type dist: float
   :arg plane_co:
      Point on the plane.
   :type plane_co: :class:`mathutils.Vector` or any sequence of 3 floats
   :arg plane_no:
      Direction of the plane.
   :type plane_no: :class:`mathutils.Vector` or any sequence of 3 floats
   :arg use_snap_center:
      Snap axis aligned verts to the center.
   :type use_snap_center: bool
   :arg clear_outer:
      When enabled. remove all geometry on the positive side of the plane.
   :type clear_outer: bool
   :arg clear_inner:
      When enabled. remove all geometry on the negative side of the plane.
   :type clear_inner: bool
   :return:

      - ``geom_cut``:
        Output geometry aligned with the plane (new and existing).

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`)
      - ``geom``:
        Input and output geometry (result of cut).

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: delete(bm, geom=[], context='VERTS')

   Delete Geometry.

   Utility operator to delete geometry.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input geometry.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg context:
      Geometry types to delete.
   :type context: enum in ['VERTS', 'EDGES', 'FACES_ONLY', 'EDGES_FACES', 'FACES', 'FACES_KEEP_BOUNDARY', 'TAGGED_ONLY'], default 'VERTS'


.. function:: duplicate(bm, geom=[], dest=None, use_select_history=False, use_edge_flip_from_face=False)

   Duplicate Geometry.

   Utility operator to duplicate geometry,
   optionally into a destination mesh.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input geometry.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg dest:
      Destination bmesh, if None will use current on.
   :type dest: :class:`bmesh.types.BMesh`
   :arg use_select_history:
      Undocumented.
   :type use_select_history: bool
   :arg use_edge_flip_from_face:
      Undocumented.
   :type use_edge_flip_from_face: bool
   :return:

      - ``geom_orig``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
      - ``geom``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
      - ``vert_map``:


        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`
      - ``edge_map``:


        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`
      - ``face_map``:


        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`
      - ``boundary_map``:
        Boundary edges from the split geometry that maps edges from the original geometry
        to the destination edges.

        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`
      - ``isovert_map``:


        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`

   :rtype: dict[str, Any]


.. function:: split(bm, geom=[], dest=None, use_only_faces=False)

   Split Off Geometry.

   Disconnect geometry from adjacent edges and faces,
   optionally into a destination mesh.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input geometry.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg dest:
      Destination bmesh, if None will use current one.
   :type dest: :class:`bmesh.types.BMesh`
   :arg use_only_faces:
      When enabled. don't duplicate loose verts/edges.
   :type use_only_faces: bool
   :return:

      - ``geom``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
      - ``boundary_map``:
        Boundary edges from the split geometry that maps edges from the original geometry
        to the destination edges.

        When the source edges have been deleted, the destination edge will be used
        for both the key and the value.

        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`
      - ``isovert_map``:


        **type** dict mapping vert/edge/face types to :class:`bmesh.types.BMVert`/:class:`bmesh.types.BMEdge`/:class:`bmesh.types.BMFace`

   :rtype: dict[str, Any]


.. function:: spin(bm, geom=[], cent=mathutils.Vector(), axis=mathutils.Vector(), dvec=mathutils.Vector(), angle=0, space=mathutils.Matrix.Identity(4), steps=0, use_merge=False, use_normal_flip=False, use_duplicate=False)

   Spin.

   Extrude or duplicate geometry a number of times,
   rotating and possibly translating after each step

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input geometry.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg cent:
      Rotation center.
   :type cent: :class:`mathutils.Vector` or any sequence of 3 floats
   :arg axis:
      Rotation axis.
   :type axis: :class:`mathutils.Vector` or any sequence of 3 floats
   :arg dvec:
      Translation delta per step.
   :type dvec: :class:`mathutils.Vector` or any sequence of 3 floats
   :arg angle:
      Total rotation angle (radians).
   :type angle: float
   :arg space:
      Matrix to define the space (typically object matrix).
   :type space: :class:`mathutils.Matrix`
   :arg steps:
      Number of steps.
   :type steps: int
   :arg use_merge:
      Merge first/last when the angle is a full revolution.
   :type use_merge: bool
   :arg use_normal_flip:
      Create faces with reversed direction.
   :type use_normal_flip: bool
   :arg use_duplicate:
      Duplicate or extrude?.
   :type use_duplicate: bool
   :return:

      - ``geom_last``:
        Result of last step.

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: rotate_uvs(bm, faces=[], use_ccw=False)

   UV Rotation.

   Cycle the loop UVs

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg use_ccw:
      Rotate counter-clockwise if true, otherwise clockwise.
   :type use_ccw: bool


.. function:: reverse_uvs(bm, faces=[])

   UV Reverse.

   Reverse the UVs

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)


.. function:: rotate_colors(bm, faces=[], use_ccw=False, color_index=0)

   Color Rotation.

   Cycle the loop colors

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg use_ccw:
      Rotate counter-clockwise if true, otherwise clockwise.
   :type use_ccw: bool
   :arg color_index:
      Index into color attribute list.
   :type color_index: int


.. function:: reverse_colors(bm, faces=[], color_index=0)

   Color Reverse

   Reverse the loop colors.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg color_index:
      Index into color attribute list.
   :type color_index: int


.. function:: split_edges(bm, edges=[], verts=[], use_verts=False)

   Edge Split.

   Disconnects faces along input edges.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg verts:
      Optional tag verts, use to have greater control of splits.
   :type verts: list of (:class:`bmesh.types.BMVert`)
   :arg use_verts:
      Use 'verts' for splitting, else just find verts to split from edges.
   :type use_verts: bool
   :return:

      - ``edges``:
        Old output disconnected edges.

        **type** list of (:class:`bmesh.types.BMEdge`)

   :rtype: dict[str, Any]


.. function:: create_grid(bm, x_segments=0, y_segments=0, size=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Grid.

   Creates a grid with a variable number of subdivisions

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg x_segments:
      Number of x segments.
   :type x_segments: int
   :arg y_segments:
      Number of y segments.
   :type y_segments: int
   :arg size:
      Size of the grid.
   :type size: float
   :arg matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :arg calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: create_uvsphere(bm, u_segments=0, v_segments=0, radius=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create UV Sphere.

   Creates a grid with a variable number of subdivisions

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg u_segments:
      Number of u segments.
   :type u_segments: int
   :arg v_segments:
      Number of v segment.
   :type v_segments: int
   :arg radius:
      Radius.
   :type radius: float
   :arg matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :arg calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: create_icosphere(bm, subdivisions=0, radius=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Ico-Sphere.

   Creates a grid with a variable number of subdivisions

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg subdivisions:
      How many times to recursively subdivide the sphere.
   :type subdivisions: int
   :arg radius:
      Radius.
   :type radius: float
   :arg matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :arg calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: create_monkey(bm, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Suzanne.

   Creates a monkey (standard blender primitive).

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :arg calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: create_cone(bm, cap_ends=False, cap_tris=False, segments=0, radius1=0, radius2=0, depth=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Cone.

   Creates a cone with variable depth at both ends

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg cap_ends:
      Whether or not to fill in the ends with faces.
   :type cap_ends: bool
   :arg cap_tris:
      Fill ends with triangles instead of ngons.
   :type cap_tris: bool
   :arg segments:
      Number of vertices in the base circle.
   :type segments: int
   :arg radius1:
      Radius of one end.
   :type radius1: float
   :arg radius2:
      Radius of the opposite.
   :type radius2: float
   :arg depth:
      Distance between ends.
   :type depth: float
   :arg matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :arg calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: create_circle(bm, cap_ends=False, cap_tris=False, segments=0, radius=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Creates a Circle.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg cap_ends:
      Whether or not to fill in the ends with faces.
   :type cap_ends: bool
   :arg cap_tris:
      Fill ends with triangles instead of ngons.
   :type cap_tris: bool
   :arg segments:
      Number of vertices in the circle.
   :type segments: int
   :arg radius:
      Radius of the circle.
   :type radius: float
   :arg matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :arg calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: create_cube(bm, size=0, matrix=mathutils.Matrix.Identity(4), calc_uvs=False)

   Create Cube

   Creates a cube.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg size:
      Size of the cube.
   :type size: float
   :arg matrix:
      Matrix to multiply the new geometry with.
   :type matrix: :class:`mathutils.Matrix`
   :arg calc_uvs:
      Calculate default UVs.
   :type calc_uvs: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: bevel(bm, geom=[], offset=0, offset_type='OFFSET', profile_type='SUPERELLIPSE', segments=0, profile=0, affect='VERTICES', clamp_overlap=False, material=0, loop_slide=False, mark_seam=False, mark_sharp=False, harden_normals=False, face_strength_mode='NONE', miter_outer='SHARP', miter_inner='SHARP', spread=0, custom_profile=None, vmesh_method='ADJ')

   Bevel.

   Bevels edges and vertices

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input edges and vertices.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg offset:
      Amount to offset beveled edge.
   :type offset: float
   :arg offset_type:
      How to measure the offset.
   :type offset_type: enum in ['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE'], default 'OFFSET'
   :arg profile_type:
      The profile type to use for bevel.
   :type profile_type: enum in ['SUPERELLIPSE', 'CUSTOM'], default 'SUPERELLIPSE'
   :arg segments:
      Number of segments in bevel.
   :type segments: int
   :arg profile:
      Profile shape, 0->1 (.5=>round).
   :type profile: float
   :arg affect:
      Whether to bevel vertices or edges.
   :type affect: enum in ['VERTICES', 'EDGES'], default 'VERTICES'
   :arg clamp_overlap:
      Do not allow beveled edges/vertices to overlap each other.
   :type clamp_overlap: bool
   :arg material:
      Material for bevel faces, -1 means get from adjacent faces.
   :type material: int
   :arg loop_slide:
      Prefer to slide along edges to having even widths.
   :type loop_slide: bool
   :arg mark_seam:
      Extend edge data to allow seams to run across bevels.
   :type mark_seam: bool
   :arg mark_sharp:
      Extend edge data to allow sharp edges to run across bevels.
   :type mark_sharp: bool
   :arg harden_normals:
      Harden normals.
   :type harden_normals: bool
   :arg face_strength_mode:
      Whether to set face strength, and which faces to set if so.
   :type face_strength_mode: enum in ['NONE', 'NEW', 'AFFECTED', 'ALL'], default 'NONE'
   :arg miter_outer:
      Outer miter kind.
   :type miter_outer: enum in ['SHARP', 'PATCH', 'ARC'], default 'SHARP'
   :arg miter_inner:
      Outer miter kind.
   :type miter_inner: enum in ['SHARP', 'PATCH', 'ARC'], default 'SHARP'
   :arg spread:
      Amount to offset beveled edge.
   :type spread: float
   :arg custom_profile:
      CurveProfile, if None ignored
   :type custom_profile: :class:`bpy.types.bpy_struct`
   :arg vmesh_method:
      The method to use to create meshes at intersections.
   :type vmesh_method: enum in ['ADJ', 'CUTOFF'], default 'ADJ'
   :return:

      - ``faces``:
        Output faces.

        **type** list of (:class:`bmesh.types.BMFace`)
      - ``edges``:
        Output edges.

        **type** list of (:class:`bmesh.types.BMEdge`)
      - ``verts``:
        Output verts.

        **type** list of (:class:`bmesh.types.BMVert`)

   :rtype: dict[str, Any]


.. function:: beautify_fill(bm, faces=[], edges=[], use_restrict_tag=False, method='AREA')

   Beautify Fill.

   Rotate edges to create more evenly spaced triangles.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg edges:
      Edges that can be flipped.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg use_restrict_tag:
      Restrict edge rotation to mixed tagged vertices.
   :type use_restrict_tag: bool
   :arg method:
      Method to define what is beautiful.
   :type method: enum in ['AREA', 'ANGLE'], default 'AREA'
   :return:

      - ``geom``:
        New flipped faces and edges.

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: triangle_fill(bm, use_beauty=False, use_dissolve=False, edges=[], normal=mathutils.Vector())

   Triangle Fill.

   Fill edges with triangles

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg use_beauty:
      Use best triangulation division.
   :type use_beauty: bool
   :arg use_dissolve:
      Dissolve resulting faces.
   :type use_dissolve: bool
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg normal:
      Optionally pass the fill normal to use.
   :type normal: :class:`mathutils.Vector` or any sequence of 3 floats
   :return:

      - ``geom``:
        New faces and edges.

        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: solidify(bm, geom=[], thickness=0)

   Solidify.

   Turns a mesh into a shell with thickness

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg geom:
      Input geometry.
   :type geom: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg thickness:
      Thickness.
   :type thickness: float
   :return:

      - ``geom``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: inset_individual(bm, faces=[], thickness=0, depth=0, use_even_offset=False, use_interpolate=False, use_relative_offset=False)

   Face Inset (Individual).

   Insets individual faces.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg thickness:
      Thickness.
   :type thickness: float
   :arg depth:
      Depth.
   :type depth: float
   :arg use_even_offset:
      Scale the offset to give more even thickness.
   :type use_even_offset: bool
   :arg use_interpolate:
      Blend face data across the inset.
   :type use_interpolate: bool
   :arg use_relative_offset:
      Scale the offset by surrounding geometry.
   :type use_relative_offset: bool
   :return:

      - ``faces``:
        Output faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: inset_region(bm, faces=[], faces_exclude=[], use_boundary=False, use_even_offset=False, use_interpolate=False, use_relative_offset=False, use_edge_rail=False, thickness=0, depth=0, use_outset=False)

   Face Inset (Regions).

   Inset or outset face regions.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg faces_exclude:
      Input faces to explicitly exclude from inset.
   :type faces_exclude: list of (:class:`bmesh.types.BMFace`)
   :arg use_boundary:
      Inset face boundaries.
   :type use_boundary: bool
   :arg use_even_offset:
      Scale the offset to give more even thickness.
   :type use_even_offset: bool
   :arg use_interpolate:
      Blend face data across the inset.
   :type use_interpolate: bool
   :arg use_relative_offset:
      Scale the offset by surrounding geometry.
   :type use_relative_offset: bool
   :arg use_edge_rail:
      Inset the region along existing edges.
   :type use_edge_rail: bool
   :arg thickness:
      Thickness.
   :type thickness: float
   :arg depth:
      Depth.
   :type depth: float
   :arg use_outset:
      Outset rather than inset.
   :type use_outset: bool
   :return:

      - ``faces``:
        Output faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: offset_edgeloops(bm, edges=[], use_cap_endpoint=False)

   Edge-loop Offset.

   Creates edge loops based on simple edge-outset method.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg edges:
      Input edges.
   :type edges: list of (:class:`bmesh.types.BMEdge`)
   :arg use_cap_endpoint:
      Extend loop around end-points.
   :type use_cap_endpoint: bool
   :return:

      - ``edges``:
        Output edges.

        **type** list of (:class:`bmesh.types.BMEdge`)

   :rtype: dict[str, Any]


.. function:: wireframe(bm, faces=[], thickness=0, offset=0, use_replace=False, use_boundary=False, use_even_offset=False, use_crease=False, crease_weight=0, use_relative_offset=False, material_offset=0)

   Wire Frame.

   Makes a wire-frame copy of faces.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg thickness:
      Thickness.
   :type thickness: float
   :arg offset:
      Offset the thickness from the center.
   :type offset: float
   :arg use_replace:
      Remove original geometry.
   :type use_replace: bool
   :arg use_boundary:
      Inset face boundaries.
   :type use_boundary: bool
   :arg use_even_offset:
      Scale the offset to give more even thickness.
   :type use_even_offset: bool
   :arg use_crease:
      Crease hub edges for improved subdivision surface.
   :type use_crease: bool
   :arg crease_weight:
      The mean crease weight for resulting edges.
   :type crease_weight: float
   :arg use_relative_offset:
      Scale the offset by surrounding geometry.
   :type use_relative_offset: bool
   :arg material_offset:
      Offset material index of generated faces.
   :type material_offset: int
   :return:

      - ``faces``:
        Output faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: poke(bm, faces=[], offset=0, center_mode='MEAN_WEIGHTED', use_relative_offset=False)

   Pokes a face.

   Splits a face into a triangle fan.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg faces:
      Input faces.
   :type faces: list of (:class:`bmesh.types.BMFace`)
   :arg offset:
      Center vertex offset along normal.
   :type offset: float
   :arg center_mode:
      Calculation mode for center vertex.
   :type center_mode: enum in ['MEAN_WEIGHTED', 'MEAN', 'BOUNDS'], default 'MEAN_WEIGHTED'
   :arg use_relative_offset:
      Apply offset.
   :type use_relative_offset: bool
   :return:

      - ``verts``:
        Output verts.

        **type** list of (:class:`bmesh.types.BMVert`)
      - ``faces``:
        Output faces.

        **type** list of (:class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: convex_hull(bm, input=[], use_existing_faces=False)

   Convex Hull

   Builds a convex hull from the vertices in 'input'.

   If 'use_existing_faces' is true, the hull will not output triangles
   that are covered by a pre-existing face.

   All hull vertices, faces, and edges are added to 'geom.out'. Any
   input elements that end up inside the hull (i.e. are not used by an
   output face) are added to the 'interior_geom' slot. The
   'unused_geom' slot will contain all interior geometry that is
   completely unused. Lastly, 'holes_geom' contains edges and faces
   that were in the input and are part of the hull.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg input:
      Input geometry.
   :type input: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg use_existing_faces:
      Skip hull triangles that are covered by a pre-existing face.
   :type use_existing_faces: bool
   :return:

      - ``geom``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
      - ``geom_interior``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
      - ``geom_unused``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
      - ``geom_holes``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


.. function:: symmetrize(bm, input=[], direction='-X', dist=0, use_shapekey=False)

   Symmetrize.

   Makes the mesh elements in the "input" slot symmetrical. Unlike
   normal mirroring, it only copies in one direction, as specified by
   the "direction" slot. The edges and faces that cross the plane of
   symmetry are split as needed to enforce symmetry.

   All new vertices, edges, and faces are added to the "geom.out" slot.

   :arg bm: The bmesh to operate on.
   :type bm: :class:`bmesh.types.BMesh`
   :arg input:
      Input geometry.
   :type input: list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)
   :arg direction:
      Axis to use.
   :type direction: enum in ['-X', '-Y', '-Z', 'X', 'Y', 'Z'], default '-X'
   :arg dist:
      Minimum distance.
   :type dist: float
   :arg use_shapekey:
      Transform shape keys too.
   :type use_shapekey: bool
   :return:

      - ``geom``:


        **type** list of (:class:`bmesh.types.BMVert`, :class:`bmesh.types.BMEdge`, :class:`bmesh.types.BMFace`)

   :rtype: dict[str, Any]


