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

from __future__ import annotations

from collections.abc import Callable
from typing import TypeAlias, TypedDict

import bmesh
import numpy as np

try:
    import tetgen
except ImportError:
    tetgen = None
from bpy.types import Context, Object
from mathutils import Matrix, Quaternion, Vector

from ..core.function import get_size
from ..core.utils import WmReportItems, set_collider_to_mesh

FloatArray: TypeAlias = np.ndarray
IntArray: TypeAlias = np.ndarray
Edge: TypeAlias = tuple[int, int]


class MassProperties(TypedDict):
    volume: float
    mass: float
    com: Vector
    inertia_origin: Matrix
    inertia_com: Matrix
    principal_moments: Vector
    principal_axes: Matrix
    inertial_frame_diaginertia: Vector
    inertial_frame_axes: Matrix
    inertial_frame_quat_world: Quaternion
    principal_axes_degenerate: bool


class ObjectResult(TypedDict):
    obj: Object
    nodes: FloatArray
    tets: IntArray
    props: MassProperties


DENSITY = 1000.0  # kg / m^3 fallback

TETGEN_QUALITY = False
TETGEN_MIN_RATIO = 1.5
TETGEN_NO_BISECT = True
TETGEN_COARSEN = True

CREATE_COM_EMPTY = True
CREATE_TET_DEBUG_MESH = False
PRINCIPAL_AXIS_DEGENERACY_EPSILON: float = 1e-6
WORLD_UP: Vector = Vector((0.0, 0.0, 1.0))
WORLD_RIGHT: Vector = Vector((1.0, 0.0, 0.0))


def evaluated_triangle_mesh(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    obj: Object,
) -> tuple[FloatArray | None, IntArray | None]:
    """Evaluate the object's triangulated mesh and return world-space vertices and face indices.

    Evaluates the object's mesh with modifiers applied, triangulates all faces,
    and returns vertex positions in world space along with triangle face indices.

    Algorithm:
        1. Get the evaluated object from the dependency graph and extract the mesh.
        2. Use bmesh to triangulate all polygon faces.
        3. Transform each vertex coordinate to world space via object.matrix_world.
        4. Return two numpy arrays: vertex coordinates (Nx3) and face indices (Mx3).

    Args:
        context: Blender context for accessing the evaluated dependency graph.
        report: Callback for reporting errors to the Blender UI.
        obj: The Blender mesh object to evaluate.

    Returns:
        tuple[FloatArray, IntArray]: (vertices, faces)
            - vertices: (N, 3) float64 array of world-space vertex coordinates.
            - faces: (M, 3) int32 array of triangle vertex indices.
        If the mesh has no vertices or faces, returns (None, None).
    """
    depsgraph = context.evaluated_depsgraph_get()
    eval_obj = obj.evaluated_get(depsgraph)
    mesh = eval_obj.to_mesh()

    try:
        bm = bmesh.new()
        try:
            bm.from_mesh(mesh)
            bm.faces.ensure_lookup_table()
            bmesh.ops.triangulate(bm, faces=list(bm.faces))
            bm.to_mesh(mesh)
            mesh.update()
        finally:
            bm.free()

        matrix_world = eval_obj.matrix_world.copy()
        vertices: FloatArray = np.array(
            [tuple(matrix_world @ vertex.co) for vertex in mesh.vertices],
            dtype=np.float64,
        )
        faces: IntArray = np.array(
            [tuple(poly.vertices) for poly in mesh.polygons],
            dtype=np.int32,
        )
    finally:
        eval_obj.to_mesh_clear()

    if vertices.size == 0 or faces.size == 0:
        report({"ERROR"}, "Selected mesh has no vertices or faces")
        return None, None

    return vertices, faces


def tetrahedralize(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    vertices: FloatArray,
    faces: IntArray,
) -> tuple[FloatArray | None, IntArray | None]:
    """Tetrahedralize a triangle mesh using the TetGen library.

    Produces a volume mesh of tetrahedra suitable for mass property computation.

    Algorithm:
        Uses tetgen.TetGen(vertices, faces).tetrahedralize() to generate the
        tetrahedral mesh. Parameters are controlled by module-level constants
        TETGEN_QUALITY, TETGEN_MIN_RATIO, TETGEN_NO_BISECT, and TETGEN_COARSEN.
        Returned node and tetrahedra arrays are cast to float64 and int32 for
        consistency.

    Args:
        context: Blender context passed to tetgen.
        report: Callback for reporting errors to the Blender UI.
        vertices: (N, 3) float64 array of triangle mesh vertex coordinates.
        faces: (M, 3) int32 array of triangle face vertex indices.

    Returns:
        tuple[FloatArray, IntArray]: (nodes, tets)
            - nodes: (K, 3) float64 array of tetrahedralized node coordinates.
            - tets: (L, 4) int32 array of tetrahedron node indices.
        If tetgen generates no tetrahedra, returns (None, None).
    """
    if tetgen is None:
        report({"ERROR"}, "TetGen is not installed")
        return None, None

    try:
        tet = tetgen.TetGen(vertices, faces)
        result = tet.tetrahedralize(
            quality=TETGEN_QUALITY,
            minratio=TETGEN_MIN_RATIO,
            nobisect=TETGEN_NO_BISECT,
            coarsen=TETGEN_COARSEN,
        )
    except Exception as ex:  # TetGen may reject otherwise valid surface meshes.
        report({"ERROR"}, f"TetGen failed: {ex}")
        return None, None

    nodes: FloatArray = result[0]
    tets: IntArray = result[1]

    if len(nodes) == 0 or len(tets) == 0:
        report({"ERROR"}, "TetGen generated no tetrahedra")
        return None, None

    return np.asarray(nodes, dtype=np.float64), np.asarray(tets, dtype=np.int32)


def zero_matrix() -> Matrix:
    """Return a 3x3 zero matrix with all elements set to 0.0.

    Use case:
        Used as a starting accumulator when summing second moments or inertia tensors.

    Returns:
        Matrix: A 3x3 Blender Matrix with all elements = 0.0.
    """
    return Matrix(((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)))


def matrix_from_columns(columns: list[Vector]) -> Matrix:
    """Construct a 3x3 matrix from a list of three column vectors.

    Formula:
        M = [c0  c1  c2]  where c0, c1, c2 are column vectors.

    Note:
        Unlike Blender's Matrix default row-major storage, this function
        assembles the matrix from column vectors. The returned Matrix stores
        elements in row-major representation as:
            (c0.x, c1.x, c2.x)
            (c0.y, c1.y, c2.y)
            (c0.z, c1.z, c2.z)

    Args:
        columns: List of three Vector objects representing the matrix columns.

    Returns:
        Matrix: A 3x3 Blender Matrix with the given column vectors.
    """
    return Matrix(
        (
            (columns[0].x, columns[1].x, columns[2].x),
            (columns[0].y, columns[1].y, columns[2].y),
            (columns[0].z, columns[1].z, columns[2].z),
        )
    )


def matrix_to_numpy(matrix: Matrix) -> FloatArray:
    """Convert a Blender Matrix to a numpy float64 array.

    Use case:
        Prepares data for numpy linear algebra operations such as
        np.linalg.eigh for computing principal axes and moments.

    Args:
        matrix: The 3x3 Blender Matrix to convert.

    Returns:
        FloatArray: (3, 3) float64 numpy array with the same element values.
    """
    return np.array(
        [[float(matrix[row][col]) for col in range(3)] for row in range(3)],
        dtype=np.float64,
    )


def matrix_from_numpy(matrix: FloatArray) -> Matrix:
    """
    Convert a 3x3 numpy array to a Blender Matrix.

    Args:
        matrix: A 3x3 numpy float64 array.

    Returns:
        A 3x3 Blender Matrix with the same element values.
    """
    return Matrix(
        (
            (float(matrix[0, 0]), float(matrix[0, 1]), float(matrix[0, 2])),
            (float(matrix[1, 0]), float(matrix[1, 1]), float(matrix[1, 2])),
            (float(matrix[2, 0]), float(matrix[2, 1]), float(matrix[2, 2])),
        )
    )


def vector_from_numpy(vector: FloatArray) -> Vector:
    """
    Convert a 3-element numpy array to a Blender Vector.

    Args:
        vector: A numpy array of length 3.

    Returns:
        A Blender Vector with the same element values.
    """
    return Vector((float(vector[0]), float(vector[1]), float(vector[2])))


def matrix_outer(a: Vector, b: Vector) -> Matrix:
    """Compute the outer (tensor / dyadic) product of two 3D vectors.

    Formula:
        outer(a, b) = a * b^T =
            [a.x*b.x  a.x*b.y  a.x*b.z]
            [a.y*b.x  a.y*b.y  a.y*b.z]
            [a.z*b.x  a.z*b.y  a.z*b.z]

    Use case:
        Used when computing the second moment integral over a tetrahedron
        (r * r^T) and in the parallel axis theorem offset.

    Args:
        a: The left Vector.
        b: The right Vector.

    Returns:
        Matrix: 3x3 outer product Blender Matrix.
    """
    return Matrix(
        (
            (a.x * b.x, a.x * b.y, a.x * b.z),
            (a.y * b.x, a.y * b.y, a.y * b.z),
            (a.z * b.x, a.z * b.y, a.z * b.z),
        )
    )


def matrix_scale(matrix: Matrix, scale: float) -> Matrix:
    """Scale all elements of a 3x3 matrix by a scalar factor.

    Formula:
        result[i][j] = matrix[i][j] * scale

    Args:
        matrix: The 3x3 Blender Matrix to scale.
        scale: The scalar multiplier.

    Returns:
        Matrix: Scaled 3x3 Blender Matrix.
    """
    return Matrix(tuple(tuple(float(matrix[row][col]) * scale for col in range(3)) for row in range(3)))


def inertia_shift(mass: float, offset: Vector) -> Matrix:
    """Parallel axis theorem (Steiner's theorem): compute inertia tensor shift.

    Computes the change in the inertia tensor caused by displacing the reference
    point from the center of mass.

    Formula:
        I_shift = m * (|r|^2 * I_3 - r * r^T)

    where:
        m = mass, r = offset vector, I_3 = 3x3 identity matrix.

    Derivation:
        This is the additional term needed to translate the inertia tensor from
        the center-of-mass frame to a frame offset by r. If I_com is the inertia
        about the center of mass, the inertia about the displaced origin is:
            I_origin = I_com + I_shift

    Args:
        mass: Mass of the body.
        offset: Displacement vector from the center of mass to the new reference point.

    Returns:
        Matrix: 3x3 inertia shift tensor for the parallel axis theorem.
    """
    return matrix_scale(Matrix.Identity(3), mass * offset.dot(offset)) - matrix_scale(
        matrix_outer(offset, offset), mass
    )


def tetra_points(nodes: FloatArray, tet: IntArray) -> list[Vector]:
    """Extract tetrahedron vertices from a global node array as Blender Vectors.

    Args:
        nodes: (N, 3) float64 numpy array of all node coordinates.
        tet: (4,) int32 numpy array of the tetrahedron's four node indices.

    Returns:
        list[Vector]: Four Blender Vector objects representing the tetrahedron vertices.
    """
    return [vector_from_numpy(nodes[int(index)]) for index in tet]


def tetra_volume(a: Vector, b: Vector, c: Vector, d: Vector) -> float:
    """Compute the signed volume of a tetrahedron defined by four vertices.

    Formula:
        V = |(a - d) . ((b - d) x (c - d))| / 6

    Derivation:
        The volume of a tetrahedron is one-sixth of the absolute value of the
        scalar triple product of three edge vectors from vertex d:
        u = a - d, v = b - d, w = c - d
        The triple product (u x v) . w gives the signed volume of the
        parallelepiped spanned by the three edges; the tetrahedron volume is 1/6 of that.

    Args:
        a, b, c, d: Four vertex coordinates of the tetrahedron.

    Returns:
        float: The signed volume of the tetrahedron (always non-negative).
    """
    return abs((a - d).dot((b - d).cross(c - d))) / 6.0


def tetra_second_moment_about_origin(points: list[Vector], volume: float) -> Matrix:
    """Compute the second moment tensor about the origin for a tetrahedron.

    Computes the integral S = integral(r * r^T) dV over a tetrahedron volume,
    expressed with respect to the origin.

    Formula:
        Uses an analytic integration formula via barycentric coordinates:
            S = (V / 20) * [sum(r_i * r_i^T) + sum(r_i) * sum(r_j)^T]

        where r_i are the tetrahedron vertex position vectors relative to the
        origin and V is the tetrahedron volume.

    Derivation:
        For a linearly interpolated field f(r) = sum(w_i * r_i) where w_i are
        area coordinates, the integral int(r * r^T) dV can be computed
        analytically. This implementation runs in O(1) time, requiring no
        numerical quadrature.

    Args:
        points: List of four Blender Vectors (tetrahedron vertex coordinates relative to origin).
        volume: The tetrahedron volume.

    Returns:
        Matrix: 3x3 second moment tensor S = integral(r * r^T) dV.
    """
    # Integral of r*r^T over a tetrahedron using barycentric coordinates.
    vertex_outer_sum = zero_matrix()
    vertex_sum = Vector((0.0, 0.0, 0.0))

    for point in points:
        vertex_outer_sum += matrix_outer(point, point)
        vertex_sum += point

    return matrix_scale(matrix_outer(vertex_sum, vertex_sum) + vertex_outer_sum, volume / 20.0)


def inertia_from_second_moment(second_moment: Matrix, density: float) -> Matrix:
    """Compute the inertia tensor from the second moment tensor.

    Formula:
        The second moment tensor S is defined as integral(r * r^T) dV.
        The inertia tensor I is derived from S as:
            I = density * (tr(S) * I_3 - S)

        where density is the material density, tr(S) is the trace of S,
        and I_3 is the 3x3 identity matrix.

    Physics:
        The diagonal elements of the inertia tensor are the moments of inertia
        about each axis; the off-diagonal elements are the products of inertia.
        The tensor is symmetric and positive definite.

    Args:
        second_moment: The 3x3 second moment tensor S.
        density: Material density in kg/m^3.

    Returns:
        Matrix: 3x3 inertia tensor computed about the origin.
    """
    trace: float = sum(float(second_moment[index][index]) for index in range(3))
    return matrix_scale(Matrix.Identity(3), density * trace) - matrix_scale(second_moment, density)


def quaternion_from_axes(axes: Matrix) -> list[float]:
    """Convert a 3x3 rotation matrix to a quaternion.

    Use case:
        Used to generate a quaternion from the principal inertia axes, which
        can be used as the quat attribute of the inertial element in MuJoCo XML.

    Args:
        axes: A 3x3 Blender Matrix representing a rotation.

    Returns:
        list[float]: Quaternion components [w, x, y, z] compatible with MuJoCo format.
    """
    return axes.to_quaternion()


def normalized(vector: Vector) -> Vector:
    """
    Return a normalized copy of the vector, with a safe fallback for zero-length.

    If the vector length is near zero (<= 1e-12), returns the world up vector
    (0, 0, 1) as a safe default.
    """
    length: float = vector.length
    if length <= 1e-12:
        return Vector((0.0, 0.0, 1.0))
    return vector.normalized()


def stable_axes_from_z(z_axis: Vector, reference_axes: Matrix | None = None) -> Matrix:
    """
    Build a right-handed orthonormal frame from a given Z-axis.

    Project a reference X-axis onto the plane perpendicular to Z. This avoids
    amplifying numerical noise when Z is nearly parallel to world up.
    """
    z_axis = normalized(z_axis)
    reference_x = reference_axes.col[0] if reference_axes is not None else WORLD_RIGHT
    reference_y = reference_axes.col[1] if reference_axes is not None else Vector((0.0, 1.0, 0.0))
    x_axis = reference_x - z_axis * reference_x.dot(z_axis)
    if x_axis.length <= 1e-6:
        x_axis = reference_y - z_axis * reference_y.dot(z_axis)
    x_axis = normalized(x_axis)
    y_axis: Vector = normalized(z_axis.cross(x_axis))
    return matrix_from_columns([x_axis, y_axis, z_axis])


def object_world_axes(obj: Object) -> Matrix:
    """
    Extract the 3x3 rotation matrix from an object's world transform.

    Discards translation and scale, returning only the rotation component.
    """
    return obj.matrix_world.to_quaternion().to_matrix()


def has_three_equal_moments(moments: Vector) -> bool:
    """
    Check whether all three principal moments are equal within a tolerance.

    Uses PRINCIPAL_AXIS_DEGENERACY_EPSILON scaled by the largest absolute
    moment value as the relative equality threshold.
    """
    scale: float = max(max(abs(float(value)) for value in moments), 1e-30)
    return bool(
        abs(float(moments[0] - moments[1])) <= PRINCIPAL_AXIS_DEGENERACY_EPSILON * scale
        and abs(float(moments[1] - moments[2])) <= PRINCIPAL_AXIS_DEGENERACY_EPSILON * scale
    )


def principal_axis_properties(
    report: Callable[[set[WmReportItems] | None, str], None],
    inertia_com: Matrix,
) -> tuple[Vector, Matrix, Vector, Matrix, bool]:
    """
    Compute principal moments, principal axes, and inertial frame from the inertia tensor.

    Uses numpy.linalg.eigh for symmetric eigenvalue decomposition. Also detects
    degenerate (spherical or cylindrical) inertia distributions and falls back
    to stable_axes_from_z for the ambiguous axes. The inertial frame is ordered
    with the smallest moment on the Z-axis for MuJoCo compatibility.
    """
    moments_np, axes_np = np.linalg.eigh(matrix_to_numpy(inertia_com))
    moments: Vector = vector_from_numpy(moments_np)
    axes: Matrix = matrix_from_numpy(axes_np)
    scale: float = max(max(abs(float(value)) for value in moments), 1e-30)
    same_01: bool = abs(float(moments[0] - moments[1])) <= PRINCIPAL_AXIS_DEGENERACY_EPSILON * scale
    same_12: bool = abs(float(moments[1] - moments[2])) <= PRINCIPAL_AXIS_DEGENERACY_EPSILON * scale
    degenerate: bool = same_01 or same_12

    min_index: int = min(range(3), key=lambda index: moments[index])
    remaining: list[int] = [index for index in range(3) if index != min_index]
    remaining.sort(key=lambda index: moments[index], reverse=True)

    # MuJoCo's diaginertia is tied to inertial-frame XYZ, not sorted eigenvalue
    # order. For comparison, put the smallest moment on inertial Z.
    inertial_frame_order: list[int] = remaining + [min_index]
    inertial_frame_moments: Vector = Vector(tuple(float(moments[index]) for index in inertial_frame_order))
    inertial_frame_axes: Matrix = matrix_from_columns(
        [Vector((axes[0][index], axes[1][index], axes[2][index])) for index in inertial_frame_order]
    )

    if degenerate and not (same_01 and same_12):
        unique_index: int = 2 if same_01 else 0
        unique_axis: Vector = Vector((axes[0][unique_index], axes[1][unique_index], axes[2][unique_index]))
        inertial_frame_axes = stable_axes_from_z(unique_axis)
        inertial_frame_moments = Vector((float(moments[1]), float(moments[1]), float(moments[unique_index])))

    if inertial_frame_axes.determinant() < 0.0:
        inertial_frame_axes = matrix_from_columns(
            [
                -Vector((inertial_frame_axes[0][0], inertial_frame_axes[1][0], inertial_frame_axes[2][0])),
                Vector((inertial_frame_axes[0][1], inertial_frame_axes[1][1], inertial_frame_axes[2][1])),
                Vector((inertial_frame_axes[0][2], inertial_frame_axes[1][2], inertial_frame_axes[2][2])),
            ]
        )

    return moments, axes, inertial_frame_moments, inertial_frame_axes, degenerate


def prefer_object_rotation_for_spherical_inertia(props: MassProperties, obj: Object) -> None:
    """
    Resolve ambiguous principal-axis rotations using the object's world axes.

    For spherical inertia, use the object's rotation. With two equal moments,
    retain the unique principal axis and align the free axes with the object.
    """
    if not props["principal_axes_degenerate"]:
        return

    reference_axes = object_world_axes(obj)
    if has_three_equal_moments(props["principal_moments"]):
        inertial_frame_axes = reference_axes
    else:
        z_axis = props["inertial_frame_axes"].col[2].copy()
        # Eigenvector signs are arbitrary. Keep the unique axis pointing in
        # the same hemisphere as the closest object axis.
        reference_z = max(reference_axes.col, key=lambda axis: abs(axis.dot(z_axis)))
        if reference_z.dot(z_axis) < 0.0:
            z_axis = -z_axis
        inertial_frame_axes = stable_axes_from_z(z_axis, reference_axes)
    props["inertial_frame_axes"] = inertial_frame_axes
    props["inertial_frame_quat_world"] = quaternion_from_axes(inertial_frame_axes)


def compute_mass_properties(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    nodes: FloatArray,
    tets: IntArray,
    density: float,
) -> None | MassProperties:
    """Compute mass properties from a tetrahedral volume mesh.

    Computes the full set of mass properties from a tetrahedral volume mesh,
    including volume, mass, center of mass, inertia tensors, and principal
    axis decomposition.

    Algorithm:
        1. Iterate over all tetrahedra, accumulating volume and weighted COM.
        2. Compute the overall COM: com = sum(V_i * com_i) / total_volume.
        3. Iterate over all tetrahedra to compute the second moment tensor
           relative to the COM using tetra_second_moment_about_origin and tetra_volume.
        4. Convert the second moment to an inertia tensor via inertia_from_second_moment.
        5. Compute the inertia about the origin via the parallel axis theorem (inertia_shift).
        6. Compute principal moments and axes via principal_axis_properties.
        7. Convert principal axes to a quaternion via quaternion_from_axes.

    Args:
        context: Blender context.
        report: Callback for reporting messages.
        nodes: (N, 3) float64 array of tetrahedralized node coordinates.
        tets: (M, 4) int32 array of tetrahedron node indices.
        density: Material density in kg/m^3.

    Returns:
        MassProperties | None: Dict containing all computed mass properties,
        or None if the total volume is zero.

    MassProperties dict contains:
        - volume: Total volume.
        - mass: Total mass.
        - com: Center of mass position (Vector).
        - inertia_origin: Inertia tensor about the origin (Matrix).
        - inertia_com: Inertia tensor about the COM (Matrix).
        - principal_moments: Principal moments of inertia (Vector).
        - principal_axes: Principal axes matrix (Matrix).
        - inertial_frame_diaginertia: Inertial frame diagonal inertia (Vector).
        - inertial_frame_axes: Inertial frame axes (Matrix).
        - inertial_frame_quat_world: Inertial frame world-space quaternion (Quaternion).
        - principal_axes_degenerate: Whether the principal axes are degenerate (bool).
    """
    total_volume = 0.0
    weighted_com: Vector = Vector((0.0, 0.0, 0.0))

    for tet in tets:
        points: list[Vector] = tetra_points(nodes, tet)
        volume: float = tetra_volume(points[0], points[1], points[2], points[3])
        if volume <= 0.0:
            continue

        total_volume += volume
        weighted_com += sum(points, Vector((0.0, 0.0, 0.0))) * (volume / 4.0)

    if total_volume <= 0.0:
        report({"ERROR"}, "Tetrahedral mesh has zero volume")
        return None

    mass: float = total_volume * density
    com: Vector = weighted_com / total_volume

    second_moment_com: Matrix = zero_matrix()
    for tet in tets:
        points = tetra_points(nodes, tet)
        volume = tetra_volume(points[0], points[1], points[2], points[3])
        if volume <= 0.0:
            continue

        second_moment_com += tetra_second_moment_about_origin([point - com for point in points], volume)

    inertia_com: Matrix = inertia_from_second_moment(second_moment_com, density)
    inertia_origin: Matrix = inertia_com + inertia_shift(mass, com)

    (
        principal_moments,
        principal_axes,
        inertial_frame_diaginertia,
        inertial_frame_axes,
        principal_axes_degenerate,
    ) = principal_axis_properties(report, inertia_com)

    return {
        "volume": total_volume,
        "mass": mass,
        "com": com,
        "inertia_origin": inertia_origin,
        "inertia_com": inertia_com,
        "principal_moments": principal_moments,
        "principal_axes": principal_axes,
        "inertial_frame_diaginertia": inertial_frame_diaginertia,
        "inertial_frame_axes": inertial_frame_axes,
        "inertial_frame_quat_world": quaternion_from_axes(inertial_frame_axes),
        "principal_axes_degenerate": principal_axes_degenerate,
    }


def combine_mass_properties(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    parts: list[MassProperties],
) -> None | MassProperties:
    """Combine mass properties of multiple rigid bodies into an aggregate result.

    Uses the parallel axis theorem to merge the inertial properties of several
    bodies as if they were a single rigid body.

    Algorithm:
        1. Sum the volume and mass of all parts to obtain totals.
        2. Compute the combined COM via mass-weighted average:
            com_total = sum(m_i * com_i) / sum(m_i)
        3. For each part, use the parallel axis theorem to shift its inertia
           tensor to the combined COM:
            I_total += I_i_com + m_i * (|r_i|^2 * I_3 - r_i * r_i^T)
           where r_i = com_i - com_total.
        4. Optionally compute the inertia about the origin.
        5. Perform principal axis decomposition for the combined result.

    Use case:
        When multiple separate objects need to be represented as a single
        inertial body in MuJoCo.

    Args:
        context: Blender context.
        report: Callback for reporting messages.
        parts: List of MassProperties dicts, each representing one body's properties.

    Returns:
        MassProperties | None: Combined mass properties dict, or None if total mass is zero.
    """
    total_volume: float = sum(part["volume"] for part in parts)
    total_mass: float = sum(part["mass"] for part in parts)

    if total_mass <= 0.0:
        report({"ERROR"}, "Combined selection has zero mass")
        return None

    com: Vector = (
        sum(
            (part["com"] * part["mass"] for part in parts),
            Vector((0.0, 0.0, 0.0)),
        )
        / total_mass
    )
    inertia_com: Matrix = zero_matrix()

    for part in parts:
        offset: Vector = part["com"] - com
        inertia_com += part["inertia_com"] + inertia_shift(part["mass"], offset)

    inertia_origin: Matrix = inertia_com + inertia_shift(total_mass, com)

    (
        principal_moments,
        principal_axes,
        inertial_frame_diaginertia,
        inertial_frame_axes,
        principal_axes_degenerate,
    ) = principal_axis_properties(report, inertia_com)

    return {
        "volume": total_volume,
        "mass": total_mass,
        "com": com,
        "inertia_origin": inertia_origin,
        "inertia_com": inertia_com,
        "principal_moments": principal_moments,
        "principal_axes": principal_axes,
        "inertial_frame_diaginertia": inertial_frame_diaginertia,
        "inertial_frame_axes": inertial_frame_axes,
        "inertial_frame_quat_world": quaternion_from_axes(inertial_frame_axes),
        "principal_axes_degenerate": principal_axes_degenerate,
    }


def compute_shape_mass_properties(
    report: Callable[[set[WmReportItems] | None, str], None],
    obj: Object,
    density: float,
) -> MassProperties | None:
    """Integrate a solid primitive from its parameters, without generating a mesh."""
    shape = obj.Forge_Geometry.type
    size = get_size(obj)
    if size is None:
        report({"ERROR"}, f"{obj.name}: missing shape size modifier")
        return None

    dimensions = np.atleast_1d(np.asarray(size, dtype=np.float64))
    if not np.all(np.isfinite(dimensions)) or np.any(dimensions < 0.0):
        report({"ERROR"}, f"{obj.name}: invalid shape size")
        return None

    # Diagonal entries of integral(r*r^T) dV in the primitive's local frame.
    match shape:
        case "BOX":
            volume = 8.0 * float(np.prod(dimensions))
            second_moments = volume * dimensions**2 / 3.0
        case "SPHERE":
            radius = float(size)
            volume = 4.0 * np.pi * radius**3 / 3.0
            second_moments = np.full(3, volume * radius**2 / 5.0)
        case "CYLINDER" | "CAPSULE":
            radius, half_height = dimensions
            cylinder_volume = np.pi * radius**2 * (2.0 * half_height)
            radial = cylinder_volume * radius**2 / 4.0
            axial = cylinder_volume * half_height**2 / 3.0
            volume = cylinder_volume
            if shape == "CAPSULE":
                sphere_volume = 4.0 * np.pi * radius**3 / 3.0
                volume += sphere_volume
                radial += sphere_volume * radius**2 / 5.0
                # Two hemispheres centered at +/-half_height. Their centroid
                # offsets from the cutting planes are +/-3*radius/8.
                axial += sphere_volume * (radius**2 / 5.0 + half_height**2 + 0.75 * half_height * radius)
            second_moments = np.array((radial, radial, axial))
        case _:
            report({"ERROR"}, f"{obj.name}: unsupported shape type {shape}")
            return None

    transform = matrix_to_numpy(obj.matrix_world.to_3x3())
    volume_scale = abs(float(np.linalg.det(transform)))
    volume *= volume_scale
    if not np.isfinite(volume) or volume <= 0.0:
        report({"ERROR"}, f"{obj.name}: shape has zero or invalid volume")
        return None

    # Transform the second moment tensor before converting to inertia so that
    # nonuniform scale, reflections and parent-induced shear are included.
    second_moment = volume_scale * transform @ np.diag(second_moments) @ transform.T
    inertia_com = inertia_from_second_moment(matrix_from_numpy(second_moment), density)
    mass = volume * density
    com = obj.matrix_world.to_translation()
    moments, axes, frame_moments, frame_axes, degenerate = principal_axis_properties(report, inertia_com)
    return {
        "volume": volume,
        "mass": mass,
        "com": com,
        "inertia_origin": inertia_com + inertia_shift(mass, com),
        "inertia_com": inertia_com,
        "principal_moments": moments,
        "principal_axes": axes,
        "inertial_frame_diaginertia": frame_moments,
        "inertial_frame_axes": frame_axes,
        "inertial_frame_quat_world": quaternion_from_axes(frame_axes),
        "principal_axes_degenerate": degenerate,
    }


def process_object(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    obj: Object,
) -> ObjectResult | None:
    """Process a single object through the mass property computation pipeline.

    Primitive shapes are integrated directly from their size parameters.
    Mesh pipeline steps:
        1. evaluated_triangle_mesh: Evaluate the mesh, apply modifiers, triangulate.
        2. tetrahedralize: Use TetGen to tetrahedralize the triangle mesh.
        3. compute_mass_properties: Compute all mass properties from the tetrahedral mesh.
        4. prefer_object_rotation_for_spherical_inertia: If the principal moments
           indicate spherical inertia, replace the inertial frame axes with the
           object's world rotation.

    Args:
        context: Blender context.
        report: Callback for reporting messages.
        obj: The Blender mesh object to process.

    Returns:
        ObjectResult: Result dict containing:
            - obj: The original Blender object.
            - nodes: Tetrahedralized node coordinate array.
            - tets: Tetrahedral index array.
            - props: Computed mass properties (MassProperties).
    """

    density = obj.Forge_Geometry.density
    if obj.type == "MESH" and obj.data.materials:
        material = obj.data.materials[0]
        if material is not None and "density" in material:
            density = float(material["density"])
    if obj.Forge_Geometry.type not in {"MESH", "SDF"}:
        props = compute_shape_mass_properties(report, obj, density)
        nodes = np.empty((0, 3), dtype=np.float64)
        tets = np.empty((0, 4), dtype=np.int32)
    else:
        set_collider_to_mesh(obj, True)
        try:
            vertices, faces = evaluated_triangle_mesh(context, report, obj)
            if vertices is None or faces is None:
                report({"ERROR"}, "Vertices or faces size is 0")
                return None
            nodes, tets = tetrahedralize(context, report, vertices, faces)
        finally:
            set_collider_to_mesh(obj, False)
        if nodes is None or tets is None:
            return None
        props = compute_mass_properties(context, report, nodes, tets, density)
    if props is None:
        return None
    prefer_object_rotation_for_spherical_inertia(props, obj)

    return {
        "obj": obj,
        "nodes": nodes,
        "tets": tets,
        "props": props,
    }


def compute_inertia(
    context: Context,
    report: Callable[[set[WmReportItems] | None, str], None],
    objs: list[Object],
) -> tuple[Vector, Quaternion, float, Vector, Matrix] | None:
    """Compute inertia data for one or more selected objects (top-level entry).

    This is the main entry point called by the operator.

    Algorithm:
        - If a single object is selected, process it directly and return its
          inertial properties.
        - If multiple objects are selected, process each individually and then
          combine their results via combine_mass_properties using the parallel
          axis theorem.

    Return format:
        Returns (com, quat, mass, diaginertia, inertia_com_world).

    Args:
        context: Blender context.
        report: Callback for reporting messages.
        objs: List of Blender objects to process.

    Returns:
        tuple[Vector, Quaternion, float, Vector, Matrix]:
            - com: Center of mass position (Vector).
            - quat: Inertial frame world-space quaternion (Quaternion) [w, x, y, z].
            - mass: Total mass (float).
            - diaginertia: Diagonal inertia in the inertial frame (Vector) [ixx, iyy, izz].
            - inertia_com_world: Full tensor about the COM in world axes.
    """
    if not objs:
        report({"ERROR"}, "No visual meshes selected for inertia computation")
        return None

    results = []
    for mesh_obj in objs:
        result = process_object(context, report, mesh_obj)
        if result is None:
            return None
        results.append(result)
    if len(results) == 1:
        result: ObjectResult = results[0]
        props: MassProperties = result["props"]
        return (
            props["com"],
            props["inertial_frame_quat_world"],
            props["mass"],
            props["inertial_frame_diaginertia"],
            props["inertia_com"],
        )

    else:
        aggregate_props = combine_mass_properties(context, report, [result["props"] for result in results])
        if aggregate_props is None:
            return None

        return (
            aggregate_props["com"],
            aggregate_props["inertial_frame_quat_world"],
            aggregate_props["mass"],
            aggregate_props["inertial_frame_diaginertia"],
            aggregate_props["inertia_com"],
        )
