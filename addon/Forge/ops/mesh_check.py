# Copyright (C) 2020-2026 Motphys Technology Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of Motrix Forge.
#
# Motrix Forge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Motrix Forge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Motrix Forge. If not, see <https://www.gnu.org/licenses/>.
# ==============================================================================

from collections.abc import Callable

import bmesh
import bpy
from bpy.types import Context, Depsgraph, Mesh, Object
from mathutils import Vector

from ..core.utils import (
    AABB,
    BVH_OVERLAP_EPSILON,
    MAX_LEAF_SIZE,
    BVHNode,
    Edge,
    FacePair,
    ObjectBVHData,
    Polygon,
    Triangle,
    Vec2,
    WmReportItems,
    set_collider_to_mesh,
)


def aabb_overlaps(a: AABB, b: AABB, eps: float = 1e-6) -> bool:
    """Check whether two axis-aligned bounding boxes (AABB) overlap.

    Separately checks each of the three axes for interval overlap. If no overlap is found on
    any axis, the AABBs are considered non-overlapping.

    Args:
        a: The first AABB.
        b: The second AABB.
        eps: Epsilon tolerance for the overlap test (default 1e-6).

    Returns:
        True if the two AABBs overlap, False otherwise.
    """

    if a.bmin is None or a.bmax is None or b.bmin is None or b.bmax is None:
        return False
    for axis in range(3):
        if a.bmax[axis] < b.bmin[axis] - eps:
            return False
        if b.bmax[axis] < a.bmin[axis] - eps:
            return False
    return True


def node_children(node: BVHNode) -> list[BVHNode]:
    """Return a list of non-None children for a given BVH node.

    Args:
        node: The BVH node whose children to retrieve.

    Returns:
        List of non-None child BVH nodes (left and/or right).
    """

    return [child for child in (node.left, node.right) if child is not None]


def collect_candidate_pairs(root: BVHNode) -> list[FacePair]:
    """Collect candidate triangle face pairs within a single BVH tree (for self-intersection detection).

    Uses a stack to traverse the BVH tree, performing AABB overlap tests on nodes. When both
    nodes are leaves, it enumerates face index pairs. When a and b refer to the same node,
    symmetric branching is used for efficiency.

    Args:
        root: The root BVH node of the tree.

    Returns:
        Sorted list of face pairs where each pair satisfies ai < bi.
    """

    pairs: set[FacePair] = set()
    stack: list[tuple[BVHNode, BVHNode]] = [(root, root)]

    while stack:
        a, b = stack.pop()
        if not aabb_overlaps(a.aabb, b.aabb):
            continue

        a_leaf: bool = a.face_indices is not None
        b_leaf: bool = b.face_indices is not None

        if a_leaf and b_leaf:
            for ai in a.face_indices:
                for bi in b.face_indices:
                    if ai < bi:
                        pairs.add((ai, bi))
            continue

        if a is b:
            children: list[BVHNode] = node_children(a)
            for i, child_a in enumerate(children):
                for child_b in children[i:]:
                    stack.append((child_a, child_b))
            continue

        if a_leaf:
            for child in node_children(b):
                stack.append((a, child))
        elif b_leaf:
            for child in node_children(a):
                stack.append((child, b))
        else:
            for child_a in node_children(a):
                for child_b in node_children(b):
                    stack.append((child_a, child_b))

    return sorted(pairs)


def collect_candidate_pairs_between(root_a: BVHNode, root_b: BVHNode) -> list[FacePair]:
    """Collect candidate face pairs between two different BVH trees (for inter-object intersection).

    Synchronously traverses both trees with a stack, preferentially splitting the node with
    larger surface area for more efficient pruning.

    Args:
        root_a: The root BVH node of the first tree.
        root_b: The root BVH node of the second tree.

    Returns:
        A list of ``(face_index_a, face_index_b)`` candidate pairs.
    """

    pairs: list[FacePair] = []
    stack: list[tuple[BVHNode, BVHNode]] = [(root_a, root_b)]

    while stack:
        a, b = stack.pop()
        if not aabb_overlaps(a.aabb, b.aabb):
            continue

        a_leaf: bool = a.face_indices is not None
        b_leaf: bool = b.face_indices is not None

        if a_leaf and b_leaf:
            for ai in a.face_indices:
                for bi in b.face_indices:
                    pairs.append((ai, bi))
            continue

        if a_leaf:
            for child in node_children(b):
                stack.append((a, child))
            continue

        if b_leaf:
            for child in node_children(a):
                stack.append((child, b))
            continue

        if a.aabb.surface_area() >= b.aabb.surface_area():
            for child in node_children(a):
                stack.append((child, b))
        else:
            for child in node_children(b):
                stack.append((a, child))

    return pairs


def triangle_points(vertices: list[Vector], tri: Triangle) -> tuple[Vector, Vector, Vector]:
    """Extract the three vertex coordinates of a triangle from a vertex list and triangle index tuple.

    Args:
        vertices: Full list of vertex positions.
        tri: A triangle index tuple ``(i0, i1, i2)``.

    Returns:
        Tuple of three Vectors representing the triangle vertices.
    """

    return vertices[tri[0]], vertices[tri[1]], vertices[tri[2]]


def triangle_normal(a: Vector, b: Vector, c: Vector) -> Vector:
    """Compute the normal vector of a triangle.

    Normal = (b - a) x (c - a), obtained by the cross product of two edge vectors.

    Args:
        a: First vertex of the triangle.
        b: Second vertex of the triangle.
        c: Third vertex of the triangle.

    Returns:
        The normal vector (not normalised).
    """

    return (b - a).cross(c - a)


def signed_plane_dist(point: Vector, plane_point: Vector, plane_normal: Vector) -> float:
    """Compute the signed distance from a point to a plane.

    Args:
        point: The query point.
        plane_point: A point on the plane.
        plane_normal: The normal vector of the plane.

    Returns:
        Signed distance value. Positive when the point is on the normal-facing side, negative otherwise.
    """

    return (point - plane_point).dot(plane_normal)


def point_in_triangle(
    point: Vector,
    a: Vector,
    b: Vector,
    c: Vector,
    eps: float = 1e-6,
) -> bool:
    """Test whether a point lies inside a triangle using barycentric coordinates.

    Treats the triangle as a plane spanned by v0 = c - a and v1 = b - a, solves for the
    barycentric coordinates (u, v) of point - a. The point is inside if u >= 0, v >= 0,
    and u + v <= 1.

    Args:
        point: The point to test.
        a: First vertex of the triangle.
        b: Second vertex of the triangle.
        c: Third vertex of the triangle.
        eps: Epsilon tolerance (default 1e-6).

    Returns:
        True if the point lies inside the triangle, False otherwise.
    """

    v0: Vector = c - a
    v1: Vector = b - a
    v2: Vector = point - a
    dot00: float = v0.dot(v0)
    dot01: float = v0.dot(v1)
    dot02: float = v0.dot(v2)
    dot11: float = v1.dot(v1)
    dot12: float = v1.dot(v2)
    denom: float = dot00 * dot11 - dot01 * dot01
    if abs(denom) <= eps:
        return False
    inv_denom: float = 1.0 / denom
    u: float = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v: float = (dot00 * dot12 - dot01 * dot02) * inv_denom
    return u >= -eps and v >= -eps and u + v <= 1.0 + eps


def segment_triangle_intersects(
    p0: Vector,
    p1: Vector,
    a: Vector,
    b: Vector,
    c: Vector,
    eps: float = BVH_OVERLAP_EPSILON,
) -> bool:
    """Test whether a line segment intersects a triangle.

    Algorithm:
    1. Compute the normalized triangle normal.
    2. Compute signed distances from both segment endpoints to the triangle plane.
       If both are on the same side, there is no intersection.
    3. Compute the intersection parameter t along the segment. If t is not in [0, 1],
       the segment does not reach the plane.
    4. Use barycentric coordinates to test whether the intersection point lies inside
       the triangle.

    Args:
        p0: First endpoint of the segment.
        p1: Second endpoint of the segment.
        a: First vertex of the triangle.
        b: Second vertex of the triangle.
        c: Third vertex of the triangle.
        eps: Epsilon tolerance for comparisons.

    Returns:
        True if the segment intersects the triangle, False otherwise.
    """

    normal: Vector = triangle_normal(a, b, c)
    normal_len: float = normal.length
    if normal_len <= eps:
        return False
    normal = normal / normal_len

    d0: float = signed_plane_dist(p0, a, normal)
    d1: float = signed_plane_dist(p1, a, normal)
    if d0 > eps and d1 > eps:
        return False
    if d0 < -eps and d1 < -eps:
        return False

    denom: float = d0 - d1
    if abs(denom) <= eps:
        return False

    t: float = d0 / denom
    if t < -eps or t > 1.0 + eps:
        return False

    point: Vector = p0 + (p1 - p0) * t
    return point_in_triangle(point, a, b, c, eps)


def project_axis_for_normal(normal: Vector) -> Edge:
    """Select the two optimal projection axes for a 3D-to-2D projection based on the normal.

    Selects the axis with the largest absolute component in the normal as the discarded axis;
    the remaining two axes form the projection plane. This projects the geometry onto the
    2D plane with the largest projected area, minimising numerical error.

    Args:
        normal: The 3D normal vector.

    Returns:
        A tuple (u_axis, v_axis) representing the two axis indices used for projection.
    """

    axis: int = max(range(3), key=lambda i: abs(normal[i]))
    if axis == 0:
        return 1, 2
    if axis == 1:
        return 0, 2
    return 0, 1


def project_point(point: Vector, axes: Edge) -> Vec2:
    """Project a 3D point onto a 2D plane defined by two specified axes.

    Extracts only the components corresponding to the two axes, discarding the third.

    Args:
        point: The 3D point to project.
        axes: A tuple ``(axis_u, axis_v)`` specifying which axes to keep.

    Returns:
        A 2D tuple ``(u, v)`` of the projected coordinates.
    """

    return (point[axes[0]], point[axes[1]])


def cross2(a: Vec2, b: Vec2) -> float:
    """Compute the 2D cross product (scalar).

    The 2D cross product a x b = a.x * b.y - a.y * b.x. The sign indicates the
    orientation of b relative to a.

    Args:
        a: First 2D vector.
        b: Second 2D vector.

    Returns:
        The scalar cross product ``a.x * b.y - a.y * b.x``.
    """

    return a[0] * b[1] - a[1] * b[0]


def sub2(a: Vec2, b: Vec2) -> Vec2:
    """Compute 2D vector subtraction.

    Args:
        a: First 2D vector.
        b: Second 2D vector.

    Returns:
        The result of ``a - b`` as a 2D tuple.
    """

    return (a[0] - b[0], a[1] - b[1])


def polygon_area(poly: list[Vec2]) -> float:
    """Compute the signed area of a 2D polygon using the shoelace formula.

    Args:
        poly: List of 2D vertices in order.

    Returns:
        Signed area; positive value indicates counter-clockwise vertex order.
    """

    if len(poly) < 3:
        return 0.0
    area: float = 0.0
    for i, p in enumerate(poly):
        q = poly[(i + 1) % len(poly)]
        area += p[0] * q[1] - q[0] * p[1]
    return area * 0.5


def line_intersection_2d(
    p0: Vec2,
    p1: Vec2,
    q0: Vec2,
    q1: Vec2,
    eps: float = BVH_OVERLAP_EPSILON,
) -> Vec2:
    """Compute the intersection point of two 2D lines.

    Uses the parametric form: P = p0 + t * (p1 - p0), solving for parameter t.
    If the lines are parallel (cross product near zero), returns p1 as a fallback.

    Args:
        p0: First point on the first line.
        p1: Second point on the first line.
        q0: First point on the second line.
        q1: Second point on the second line.
        eps: Epsilon tolerance for parallel detection.

    Returns:
        The intersection point as a 2D tuple.
    """

    r: Vec2 = sub2(p1, p0)
    s: Vec2 = sub2(q1, q0)
    denom: float = cross2(r, s)
    if abs(denom) <= eps:
        return p1
    qp: Vec2 = sub2(q0, p0)
    t: float = cross2(qp, s) / denom
    return (p0[0] + t * r[0], p0[1] + t * r[1])


def clip_polygon_against_edge(poly: list[Vec2], edge_a: Vec2, edge_b: Vec2, clip_sign: float, eps: float) -> list[Vec2]:
    """Clip a polygon against one side of an edge using the Sutherland-Hodgman algorithm.

    Iterates over each edge of the polygon, determining whether vertices are inside or
    outside the clipping edge, and retains or inserts intersection points accordingly
    to produce the clipped sub-polygon.

    Args:
        poly: List of 2D polygon vertices.
        edge_a: Start point of the clipping edge.
        edge_b: End point of the clipping edge.
        clip_sign: Clipping direction sign (1.0 or -1.0), determines which side is kept.
        eps: Epsilon tolerance for inside/outside test.

    Returns:
        List of 2D vertices of the clipped polygon.
    """

    if not poly:
        return []

    edge: Vec2 = sub2(edge_b, edge_a)

    def inside(point: Vec2) -> bool:
        return clip_sign * cross2(edge, sub2(point, edge_a)) >= -eps

    result: list[Vec2] = []
    prev: Vec2 = poly[-1]
    prev_inside: bool = inside(prev)
    for curr in poly:
        curr_inside: bool = inside(curr)
        if curr_inside != prev_inside:
            result.append(line_intersection_2d(prev, curr, edge_a, edge_b, eps))
        if curr_inside:
            result.append(curr)
        prev = curr
        prev_inside = curr_inside
    return result


def triangle_plane_intersection_points(
    triangle: tuple[Vector, Vector, Vector],
    plane_distances: list[float],
    eps: float = BVH_OVERLAP_EPSILON,
) -> list[Vector]:
    """Clip a triangle against a plane and return its unique contact points."""

    points: list[Vector] = []

    def append_unique(point: Vector) -> None:
        if not any((point - existing).length <= eps for existing in points):
            points.append(point)

    for point, distance in zip(triangle, plane_distances):
        if abs(distance) <= eps:
            append_unique(point)

    for index in range(3):
        next_index = (index + 1) % 3
        distance = plane_distances[index]
        next_distance = plane_distances[next_index]
        if not ((distance > eps and next_distance < -eps) or (distance < -eps and next_distance > eps)):
            continue
        t = distance / (distance - next_distance)
        append_unique(triangle[index] + (triangle[next_index] - triangle[index]) * t)

    return points


def noncoplanar_triangles_penetrate(
    tri_a: tuple[Vector, Vector, Vector],
    dist_a: list[float],
    tri_b: tuple[Vector, Vector, Vector],
    dist_b: list[float],
    intersection_axis: Vector,
    eps: float = BVH_OVERLAP_EPSILON,
) -> bool:
    """Return whether two non-coplanar faces cross along a positive-length segment.

    Point-point, point-line, and line-line boundary contact are intentionally not
    penetration. Both triangles must cross the other plane, and their clipped
    intervals on the planes' intersection line must overlap with positive length.
    """

    a_straddles = any(distance > eps for distance in dist_a) and any(distance < -eps for distance in dist_a)
    b_straddles = any(distance > eps for distance in dist_b) and any(distance < -eps for distance in dist_b)
    if not a_straddles or not b_straddles:
        return False

    axis_length = intersection_axis.length
    if axis_length <= eps:
        return False
    axis = intersection_axis / axis_length

    points_a = triangle_plane_intersection_points(tri_a, dist_a, eps)
    points_b = triangle_plane_intersection_points(tri_b, dist_b, eps)
    if len(points_a) < 2 or len(points_b) < 2:
        return False

    interval_a = [point.dot(axis) for point in points_a]
    interval_b = [point.dot(axis) for point in points_b]
    overlap_start = max(min(interval_a), min(interval_b))
    overlap_end = min(max(interval_a), max(interval_b))
    return overlap_end - overlap_start > eps


def coplanar_triangles_overlap_area(
    tri_a: tuple[Vector, Vector, Vector],
    tri_b: tuple[Vector, Vector, Vector],
    normal: Vector,
    eps: float = BVH_OVERLAP_EPSILON,
) -> bool:
    """Test whether two coplanar triangles overlap in the 2D projection plane.

    Algorithm:
    1. Choose optimal projection axes based on the normal, project both triangles to 2D.
    2. Clip triangle A against each edge of triangle B using Sutherland-Hodgman.
    3. If the remaining clipped polygon has positive area, the triangles overlap.

    Args:
        tri_a: Tuple of three Vectors for the first triangle.
        tri_b: Tuple of three Vectors for the second triangle.
        normal: The common plane normal.
        eps: Epsilon tolerance.

    Returns:
        True if the two triangles have overlapping area when coplanar, False otherwise.
    """

    axes: Edge = project_axis_for_normal(normal)
    subject: list[Vec2] = [project_point(p, axes) for p in tri_a]
    clip: list[Vec2] = [project_point(p, axes) for p in tri_b]

    clip_area: float = polygon_area(clip)
    if abs(clip_area) <= eps * eps:
        return False

    clip_sign: float = 1.0 if clip_area > 0.0 else -1.0
    poly: list[Vec2] = subject
    for i, edge_a in enumerate(clip):
        edge_b = clip[(i + 1) % len(clip)]
        poly = clip_polygon_against_edge(poly, edge_a, edge_b, clip_sign, eps)
        if len(poly) < 3:
            return False

    return abs(polygon_area(poly)) > eps * eps


def triangles_intersect_between(
    vertices_a: list[Vector],
    tri_a_indices: Triangle,
    vertices_b: list[Vector],
    tri_b_indices: Triangle,
    skip_shared_indices: bool = False,
) -> bool:
    """Test whether two triangles (potentially from different vertex lists) intersect.

    Algorithm:
    1. Extract vertex coordinates and normals of both triangles.
    2. Perform separating-plane test: check whether all vertices of one triangle lie on
       the same side of the other triangle's plane.
    3. If coplanar, use 2D overlap detection on the projection plane. Coincident
       faces with opposite winding (opposite normals) are treated as a valid
       back-to-back shell and are not reported as intersections.
    4. For non-coplanar faces, intersect each triangle with the other plane and
       compare the resulting intervals. Boundary-only point/line contact is ignored.

    Args:
        vertices_a: Vertex list for the first object.
        tri_a_indices: Triangle index tuple for the first triangle.
        vertices_b: Vertex list for the second object.
        tri_b_indices: Triangle index tuple for the second triangle.
        skip_shared_indices: Whether to skip pairs sharing vertex indices (avoids false
            positives for same-object intersection).

    Returns:
        True if the two triangles intersect, False otherwise.
    """

    tri_a: tuple[Vector, Vector, Vector] = triangle_points(vertices_a, tri_a_indices)
    tri_b: tuple[Vector, Vector, Vector] = triangle_points(vertices_b, tri_b_indices)
    normal_a: Vector = triangle_normal(*tri_a)
    normal_b: Vector = triangle_normal(*tri_b)

    normal_a_len: float = normal_a.length
    normal_b_len: float = normal_b.length
    if normal_a_len <= BVH_OVERLAP_EPSILON:
        return False
    if normal_b_len <= BVH_OVERLAP_EPSILON:
        return False
    normal_a = normal_a / normal_a_len
    normal_b = normal_b / normal_b_len

    dist_b: list[float] = [signed_plane_dist(p, tri_a[0], normal_a) for p in tri_b]
    dist_a: list[float] = [signed_plane_dist(p, tri_b[0], normal_b) for p in tri_a]

    if all(d > BVH_OVERLAP_EPSILON for d in dist_b) or all(d < -BVH_OVERLAP_EPSILON for d in dist_b):
        return False
    if all(d > BVH_OVERLAP_EPSILON for d in dist_a) or all(d < -BVH_OVERLAP_EPSILON for d in dist_a):
        return False

    coplanar: bool = normal_a.cross(normal_b).length <= BVH_OVERLAP_EPSILON and all(
        abs(d) <= BVH_OVERLAP_EPSILON for d in dist_b
    )
    if coplanar:
        # Two coincident surfaces with opposite normals describe the two sides
        # of a zero-thickness shell. Their overlapping area is intentional and
        # must not be reported as mesh penetration. Same-facing coplanar faces
        # remain intersections.
        if normal_a.dot(normal_b) < 0.0:
            return False
        return coplanar_triangles_overlap_area(tri_a, tri_b, normal_a)

    if skip_shared_indices and set(tri_a_indices) & set(tri_b_indices):
        return False

    return noncoplanar_triangles_penetrate(tri_a, dist_a, tri_b, dist_b, normal_a.cross(normal_b))


def triangles_intersect(vertices: list[Vector], tri_a_indices: Triangle, tri_b_indices: Triangle) -> bool:
    """Test whether two triangles within the same object intersect (underlying check for self-intersection).

    Wraps triangles_intersect_between with the same vertex list and enables the
    skip-shared-indices optimisation.

    Args:
        vertices: Full vertex list for the object.
        tri_a_indices: Triangle index tuple for the first triangle.
        tri_b_indices: Triangle index tuple for the second triangle.

    Returns:
        True if the triangles intersect, False otherwise.
    """

    return triangles_intersect_between(vertices, tri_a_indices, vertices, tri_b_indices, skip_shared_indices=True)


def polygons_intersect(
    vertices: list[Vector],
    face_triangles: list[list[Triangle]],
    face_a: int,
    face_b: int,
) -> bool:
    """Test whether two polygon faces within the same object intersect.

    Triangulates both polygons and calls triangles_intersect on every triangle pair.

    Args:
        vertices: Full vertex list for the object.
        face_triangles: Per-face list of triangle index tuples.
        face_a: Index of the first face.
        face_b: Index of the second face.

    Returns:
        True if the two faces intersect, False otherwise.
    """

    for tri_a in face_triangles[face_a]:
        for tri_b in face_triangles[face_b]:
            if triangles_intersect(vertices, tri_a, tri_b):
                return True
    return False


def polygon_edges(polygon: Polygon) -> list[Edge]:
    """Extract all edges of a polygon face, each edge sorted by vertex index.

    Args:
        polygon: A polygon represented as a tuple of vertex indices.

    Returns:
        List of edges, each edge is a sorted pair of vertex indices.
    """

    edges: list[Edge] = []
    for i, vertex_index in enumerate(polygon):
        next_index: int = polygon[(i + 1) % len(polygon)]
        edges.append(tuple(sorted((vertex_index, next_index))))
    return edges


def polygons_intersect_between(
    vertices_a: list[Vector],
    face_triangles_a: list[list[Triangle]],
    face_a: int,
    vertices_b: list[Vector],
    face_triangles_b: list[list[Triangle]],
    face_b: int,
) -> bool:
    """Test whether two polygon faces from different objects intersect.

    Triangulates both polygons and calls triangles_intersect_between on every triangle pair.

    Args:
        vertices_a: Vertex list for the first object.
        face_triangles_a: Per-face triangle list for the first object.
        face_a: Index of the first face.
        vertices_b: Vertex list for the second object.
        face_triangles_b: Per-face triangle list for the second object.
        face_b: Index of the second face.

    Returns:
        True if the two faces intersect, False otherwise.
    """

    for tri_a in face_triangles_a[face_a]:
        for tri_b in face_triangles_b[face_b]:
            if triangles_intersect_between(vertices_a, tri_a, vertices_b, tri_b):
                return True
    return False


def plane_separates_vertex_sets(
    origin: Vector,
    normal: Vector,
    vertices_a: list[Vector],
    vertices_b: list[Vector],
    eps: float = BVH_OVERLAP_EPSILON,
) -> bool:
    """Return whether a plane keeps two complete vertex sets on opposite sides.

    Vertices within ``eps`` may lie on the plane, so aligned face/edge/point
    contact is accepted. The result is independent of face winding.
    """

    normal_length = normal.length
    if normal_length <= eps:
        return False
    normal = normal / normal_length
    distances_a = [signed_plane_dist(vertex, origin, normal) for vertex in vertices_a]
    distances_b = [signed_plane_dist(vertex, origin, normal) for vertex in vertices_b]
    return (max(distances_a) <= eps and min(distances_b) >= -eps) or (
        max(distances_b) <= eps and min(distances_a) >= -eps
    )


def candidate_face_plane_separates_objects(
    data_a: ObjectBVHData,
    data_b: ObjectBVHData,
    candidate_pairs: list[FacePair],
) -> bool:
    """Find a candidate face plane that proves two objects only touch or are separate."""

    checked_planes: set[tuple[int, Triangle]] = set()
    for face_a, face_b in candidate_pairs:
        for triangle_indices_a in data_a.face_triangles[face_a]:
            triangle_a = triangle_points(data_a.verts, triangle_indices_a)
            normal_a = triangle_normal(*triangle_a)
            normal_a_length = normal_a.length
            if normal_a_length <= BVH_OVERLAP_EPSILON:
                continue
            normal_a = normal_a / normal_a_length

            for triangle_indices_b in data_b.face_triangles[face_b]:
                triangle_b = triangle_points(data_b.verts, triangle_indices_b)
                normal_b = triangle_normal(*triangle_b)
                normal_b_length = normal_b.length
                if normal_b_length <= BVH_OVERLAP_EPSILON:
                    continue
                normal_b = normal_b / normal_b_length

                coplanar = normal_a.cross(normal_b).length <= BVH_OVERLAP_EPSILON and all(
                    abs(signed_plane_dist(point, triangle_a[0], normal_a)) <= BVH_OVERLAP_EPSILON
                    for point in triangle_b
                )
                plane_key = (face_a, triangle_indices_a)
                if not coplanar or plane_key in checked_planes:
                    continue
                checked_planes.add(plane_key)
                if plane_separates_vertex_sets(triangle_a[0], normal_a, data_a.verts, data_b.verts):
                    return True

    return False


def find_self_intersections(
    vertices: list[Vector],
    polygons: list[Polygon],
    face_triangles: list[list[Triangle]],
    root: BVHNode,
) -> tuple[list[FacePair], set[int], set[Edge], set[int]]:
    """Find all self-intersecting faces within a single object.

    Uses the BVH to collect candidate face pairs, performs exact triangle-level
    intersection tests on each pair, and collects face/edge/vertex indices for highlighting.

    Args:
        vertices: Full vertex list for the object.
        polygons: List of polygon vertex-index tuples.
        face_triangles: Per-face list of triangle index tuples.
        root: Root node of the constructed BVH tree.

    Returns:
        A tuple of four elements:
        - List of intersecting face pairs
        - Set of intersecting face indices
        - Set of intersecting edge indices
        - Set of intersecting vertex indices
    """

    candidate_pairs: list[FacePair] = collect_candidate_pairs(root)

    face_pairs: list[FacePair] = []
    face_indices: set[int] = set()
    edge_indices: set[Edge] = set()
    vertex_indices: set[int] = set()

    for a, b in candidate_pairs:
        if not polygons_intersect(vertices, face_triangles, a, b):
            continue

        face_pairs.append((a, b))
        face_indices.update((a, b))
        vertex_indices.update(polygons[a])
        vertex_indices.update(polygons[b])
        edge_indices.update(polygon_edges(polygons[a]))
        edge_indices.update(polygon_edges(polygons[b]))

    return face_pairs, face_indices, edge_indices, vertex_indices


def find_object_intersections(
    data_a: ObjectBVHData,
    data_b: ObjectBVHData,
) -> tuple[list[FacePair], set[int], set[Edge], set[int], set[int], set[Edge], set[int]]:
    """Find all intersecting faces between two objects.

    Uses the BVH to collect candidate face pairs between the two objects, performs exact
    triangle-level intersection tests on each pair, and collects face/edge/vertex indices
    for each object separately.

    Args:
        data_a: BVH acceleration data for the first object.
        data_b: BVH acceleration data for the second object.

    Returns:
        A tuple of seven elements: face pairs between A and B, object A's face/edge/vertex
        sets, and object B's face/edge/vertex sets.
    """

    candidate_pairs: list[FacePair] = collect_candidate_pairs_between(data_a.root, data_b.root)

    face_pairs: list[FacePair] = []
    face_indices_a: set[int] = set()
    edge_indices_a: set[Edge] = set()
    vertex_indices_a: set[int] = set()
    face_indices_b: set[int] = set()
    edge_indices_b: set[Edge] = set()
    vertex_indices_b: set[int] = set()

    # A shared face/edge/point can be proved non-penetrating when one of the
    # candidate face planes keeps the complete objects in opposite half-spaces.
    # This handles aligned boxes even when imported winding/normals disagree.
    if candidate_face_plane_separates_objects(data_a, data_b, candidate_pairs):
        return (
            face_pairs,
            face_indices_a,
            edge_indices_a,
            vertex_indices_a,
            face_indices_b,
            edge_indices_b,
            vertex_indices_b,
        )

    for a, b in candidate_pairs:
        if not polygons_intersect_between(
            data_a.verts,
            data_a.face_triangles,
            a,
            data_b.verts,
            data_b.face_triangles,
            b,
        ):
            continue

        face_pairs.append((a, b))
        face_indices_a.add(a)
        vertex_indices_a.update(data_a.polygons[a])
        edge_indices_a.update(polygon_edges(data_a.polygons[a]))
        face_indices_b.add(b)
        vertex_indices_b.update(data_b.polygons[b])
        edge_indices_b.update(polygon_edges(data_b.polygons[b]))

    return (
        face_pairs,
        face_indices_a,
        edge_indices_a,
        vertex_indices_a,
        face_indices_b,
        edge_indices_b,
        vertex_indices_b,
    )


def set_source_mesh_selection(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    obj: Object,
    face_indices: set[int],
    edge_indices: set[Edge],
    vertex_indices: set[int],
    expected_face_count: int,
    expected_vertex_count: int,
) -> None:
    """Highlight intersecting faces, edges, and vertices in the Blender viewport.

    Switches object mode, modifies selection state, and then restores the original mode and
    active object. If the evaluated mesh topology does not match the original (e.g., modifiers
    are enabled), the selection is skipped with a warning.

    Args:
        context: The active Blender context.
        report: Callback function for reporting messages to the Blender UI.
        obj: The source mesh object.
        face_indices: Set of face indices to select.
        edge_indices: Set of edge keys to select.
        vertex_indices: Set of vertex indices to select.
        expected_face_count: The original face count, used to verify topology consistency.
        expected_vertex_count: The original vertex count, used to verify topology consistency.
    """

    mesh: Mesh = obj.data
    if len(mesh.polygons) != expected_face_count or len(mesh.vertices) != expected_vertex_count:
        report(
            {"WARNING"},
            """Source mesh selection skipped because evaluated mesh indices do not match the original mesh.
            Disable modifiers or run on original topology.""",
        )
        return

    previous_active: Object | None = context.view_layer.objects.active
    previous_mode: str = obj.mode
    previous_select_mode = tuple(context.tool_settings.mesh_select_mode)

    if previous_active != obj:
        context.view_layer.objects.active = obj

    if previous_mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")

    for vertex in mesh.vertices:
        vertex.select = vertex.index in vertex_indices

    for edge in mesh.edges:
        edge_key: Edge = tuple(sorted(edge.vertices))
        edge.select = edge_key in edge_indices

    for polygon in mesh.polygons:
        polygon.select = polygon.index in face_indices

    mesh.update()
    context.tool_settings.mesh_select_mode = (False, False, True)

    if previous_mode != "OBJECT":
        bpy.ops.object.mode_set(mode=previous_mode)

    if previous_active is not None and previous_active != obj:
        context.view_layer.objects.active = previous_active
    context.tool_settings.mesh_select_mode = previous_select_mode


def extract_object_polygons(
    context: Context,
    obj: Object,
    triangulate: bool = False,
) -> tuple[list[Vector], list[Polygon], list[list[Triangle]], bool]:
    """Extract polygon data from a Blender object, including vertex coordinates, face
    definitions, and triangle decompositions.

    Retrieves the evaluated mesh via Depsgraph (including modifiers), uses BMesh for
    non-manifold edge detection and optional triangulation, and transforms coordinates
    to world space.

    Args:
        context: The active Blender context.
        obj: The source mesh object.
        triangulate: When True, all faces are triangulated in the result.

    Returns:
        A tuple of four elements: (world-space vertex list, polygon list,
        per-face triangle list, whether the mesh is non-manifold).
    """

    set_collider_to_mesh(obj, True)

    depsgraph: Depsgraph = context.evaluated_depsgraph_get()
    obj_eval: Object = obj.evaluated_get(depsgraph)

    non_manifold_count = 0

    mesh = obj_eval.to_mesh()
    bm = bmesh.new()
    try:
        bm.from_mesh(mesh)
        bm.edges.ensure_lookup_table()
        bm.edges.index_update()
        for vert in mesh.vertices:
            vert.select = False

        for edge in bm.edges:
            if not edge.is_manifold:
                non_manifold_count += 1

        if triangulate:
            bmesh.ops.triangulate(bm, faces=list(bm.faces))
        bm.faces.ensure_lookup_table()
        bm.verts.ensure_lookup_table()
        bm.faces.index_update()
        bm.verts.index_update()

        matrix_world = obj_eval.matrix_world.copy()
        verts: list[Vector] = [(matrix_world @ v.co).copy() for v in bm.verts]

        polygons: list[Polygon] = []
        face_index_map: dict[int, int] = {}
        for face in bm.faces:
            if len(face.verts) >= 3:
                face_index_map[face.index] = len(polygons)
                polygons.append(tuple(v.index for v in face.verts))

        face_triangles: list[list[Triangle]] = [[] for _ in polygons]
        for loops in bm.calc_loop_triangles():
            polygon_index: int | None = face_index_map.get(loops[0].face.index)
            if polygon_index is None:
                continue
            face_triangles[polygon_index].append(tuple(loop.vert.index for loop in loops))
    finally:
        bm.free()
        obj_eval.to_mesh_clear()

    set_collider_to_mesh(obj, False)

    return verts, polygons, face_triangles, True if non_manifold_count > 0 else False


def build_object_bvh(
    context: Context,
    obj: Object,
    triangulate: bool = False,
    max_depth: int | None = None,
) -> ObjectBVHData | None:
    """Build a BVH (Bounding Volume Hierarchy) acceleration structure for the specified object.

    Extracts polygon data from the object, then recursively builds the BVH tree based
    on each polygon's AABB.

    Args:
        context: The active Blender context.
        obj: The mesh object to build BVH data for.
        triangulate: When True, triangulate the mesh before building the BVH.
        max_depth: Maximum depth of the BVH tree. If None, it is calculated automatically
            from the number of faces.

    Returns:
        An ObjectBVHData object (containing BVH data) along with a non-manifold flag;
        returns None if the object has no faces.
    """

    verts, polygons, face_triangles, non_manifold = extract_object_polygons(context, obj, triangulate)
    if not polygons:
        # check_mesh unpacks (data, non_manifold); return a tuple so its
        # "has no faces" error branch can report instead of crashing.
        return None, False

    aabbs: list[AABB] = [AABB.polygon_aabb(verts, polygon) for polygon in polygons]
    indices: list[int] = list(range(len(polygons)))
    build_depth: int = BVHNode.get_max_depth(len(polygons), max_depth, MAX_LEAF_SIZE)
    root: BVHNode = BVHNode.build(polygons, aabbs, indices, build_depth, MAX_LEAF_SIZE)
    return ObjectBVHData(obj, verts, polygons, face_triangles, root, build_depth), non_manifold


def check_mesh(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    objs: list[Object],
    triangulate: bool = False,
    max_depth: int | None = None,
):
    """Main mesh validation function that detects self-intersections and inter-object intersections.

    For each object, builds a BVH and finds self-intersecting face pairs. Then searches for
    intersecting face pairs between object pairs. All detected intersecting faces, edges,
    and vertices are highlighted in the Blender viewport.
    Returns False with error reports if any intersections or mesh issues are found.

    Args:
        context: The active Blender context.
        report: Callback function for reporting to the Blender UI.
        objs: List of mesh objects to validate.
        triangulate: When True, triangulate meshes before BVH construction.
        max_depth: Maximum BVH tree depth (None for auto).

    Returns:
        True if all objects are valid (no intersections), False if issues were found.
    """

    selection_by_object: dict[Object, tuple[set[int], set[Edge], set[int], ObjectBVHData]] = {}

    object_data: dict[Object, ObjectBVHData] = {}
    self_intersect_count = 0
    unvalidate_obj_count = 0
    non_manifold_count = 0

    for obj in objs:
        data, non_manifold = build_object_bvh(context, obj, triangulate, max_depth)
        if data is None:
            unvalidate_obj_count += 1
            report({"ERROR"}, f"Object {obj.name!r} has no faces.")
            return False
        if non_manifold:
            non_manifold_count += 1
            report({"ERROR"}, f"Object {obj.name!r} is not manifold.")
            return False

        object_data[obj] = data
        selection_by_object[obj] = (set(), set(), set(), data)

        face_pairs, face_indices, edge_indices, vertex_indices = find_self_intersections(
            data.verts,
            data.polygons,
            data.face_triangles,
            data.root,
        )

        if not face_pairs:
            continue

        sel_faces, sel_edges, sel_vertices, _ = selection_by_object[obj]
        sel_faces.update(face_indices)
        sel_edges.update(edge_indices)
        sel_vertices.update(vertex_indices)

        if face_pairs:
            self_intersect_count += 1
            report(
                {"ERROR"},
                f"Self intersection: {len(face_pairs)} face pairs, {len(face_indices)} faces on {obj.name!r}.",
            )

    intersect_count = 0
    if len(objs) > 1:
        object_pair_count: int = 0
        object_face_pair_count: int = 0
        checked_objects: list[Object] = list(object_data.keys())
        for i, obj_a in enumerate(checked_objects):
            data_a: ObjectBVHData = object_data[obj_a]
            for obj_b in checked_objects[i + 1 :]:
                data_b: ObjectBVHData = object_data[obj_b]
                (
                    object_face_pairs,
                    faces_a,
                    edges_a,
                    vertices_a,
                    faces_b,
                    edges_b,
                    vertices_b,
                ) = find_object_intersections(data_a, data_b)
                if not object_face_pairs:
                    continue

                object_pair_count += 1
                object_face_pair_count += len(object_face_pairs)

                sel_faces_a, sel_edges_a, sel_vertices_a, _ = selection_by_object[obj_a]
                sel_faces_b, sel_edges_b, sel_vertices_b, _ = selection_by_object[obj_b]
                sel_faces_a.update(faces_a)
                sel_edges_a.update(edges_a)
                sel_vertices_a.update(vertices_a)
                sel_faces_b.update(faces_b)
                sel_edges_b.update(edges_b)
                sel_vertices_b.update(vertices_b)

                report(
                    {"ERROR"},
                    f"""Object intersection: {obj_a.name!r} vs {obj_b.name!r}: {len(object_face_pairs)} face pairs,
{len(faces_a)} faces on {obj_a.name!r}, {len(faces_b)} faces on {obj_b.name!r}.""",
                )

    for source_obj, (
        selected_faces,
        selected_edges,
        selected_vertices,
        source_data,
    ) in selection_by_object.items():
        if not selected_faces:
            continue
        intersect_count += 1

        set_source_mesh_selection(
            context,
            report,
            source_obj,
            selected_faces,
            selected_edges,
            selected_vertices,
            expected_face_count=len(source_data.polygons),
            expected_vertex_count=len(source_data.verts),
        )

    if intersect_count > 0 or self_intersect_count > 0 or unvalidate_obj_count > 0 or non_manifold_count > 0:
        report(
            {"ERROR"},
            "Find object intersections or self intersections or mesh is not manifold, see previous error.",
        )
        return False

    report(
        {"INFO"},
        "All object are validate.",
    )
    return True
