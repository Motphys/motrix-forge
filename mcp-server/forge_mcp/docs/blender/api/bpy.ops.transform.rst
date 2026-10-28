Transform Operators
===================

.. module:: bpy.ops.transform

.. function:: bbone_resize(*, value=(1.0, 1.0, 1.0), orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, release_confirm=False, use_accurate=False)

   Scale selected bendy bones display size

   :arg value: Display Size
   :type value: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg orient_type: Orientation, Transformation orientation
   :type orient_type: enum in [], (optional)
   :arg orient_matrix: Matrix
   :type orient_matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (optional)
   :arg orient_matrix_type: Matrix Orientation
   :type orient_matrix_type: enum in [], (optional)
   :arg constraint_axis: Constraint Axis
   :type constraint_axis: boolean array of 3 items, (optional)
   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: bend(*, value=(0.0), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Bend selected items between the 3D cursor and the mouse

   :arg value: Angle
   :type value: float array of 1 items in [-inf, inf], (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
   :type gpencil_strokes: boolean, (optional)
   :arg center_override: Center Override, Force using this center value (when set)
   :type center_override: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: create_orientation(*, name="", use_view=False, use=False, overwrite=False)

   Create transformation orientation from selection

   :arg name: Name, Name of the new custom orientation
   :type name: string, (optional, never None)
   :arg use_view: Use View, Use the current view instead of the active object to create the new orientation
   :type use_view: boolean, (optional)
   :arg use: Use After Creation, Select orientation after its creation
   :type use: boolean, (optional)
   :arg overwrite: Overwrite Previous, Overwrite previously created orientation with same name
   :type overwrite: boolean, (optional)

.. function:: delete_orientation()

   Delete transformation orientation

.. function:: edge_bevelweight(*, value=0.0, snap=False, release_confirm=False, use_accurate=False)

   Change the bevel weight of edges

   :arg value: Factor
   :type value: float in [-1, 1], (optional)
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: edge_crease(*, value=0.0, snap=False, release_confirm=False, use_accurate=False)

   Change the crease of edges

   :arg value: Factor
   :type value: float in [-1, 1], (optional)
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: edge_slide(*, value=0.0, single_side=False, use_even=False, flipped=False, use_clamp=True, mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, snap_point=(0.0, 0.0, 0.0), correct_uv=True, release_confirm=False, use_accurate=False)

   Slide an edge loop along a mesh

   :arg value: Factor
   :type value: float in [-10, 10], (optional)
   :arg single_side: Single Side
   :type single_side: boolean, (optional)
   :arg use_even: Even, Make the edge loop match the shape of the adjacent edge loop
   :type use_even: boolean, (optional)
   :arg flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
   :type flipped: boolean, (optional)
   :arg use_clamp: Clamp, Clamp within the edge extents
   :type use_clamp: boolean, (optional)
   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg snap_elements: Snap to Elements
   :type snap_elements: enum set in :ref:`rna_enum_snap_element_items`, (optional)
   :arg use_snap_project: Project Individual Elements
   :type use_snap_project: boolean, (optional)
   :arg snap_target: Snap Base, Point on source that will snap to target
   :type snap_target: enum in :ref:`rna_enum_snap_source_items`, (optional)
   :arg use_snap_self: Target: Include Active
   :type use_snap_self: boolean, (optional)
   :arg use_snap_edit: Target: Include Edit
   :type use_snap_edit: boolean, (optional)
   :arg use_snap_nonedit: Target: Include Non-Edited
   :type use_snap_nonedit: boolean, (optional)
   :arg use_snap_selectable: Target: Exclude Non-Selectable
   :type use_snap_selectable: boolean, (optional)
   :arg snap_point: Point
   :type snap_point: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg correct_uv: Correct UVs, Correct UV coordinates when transforming
   :type correct_uv: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: from_gizmo()

   Transform selected items by mode type

.. function:: mirror(*, orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Mirror selected items around one or more axes

   :arg orient_type: Orientation, Transformation orientation
   :type orient_type: enum in [], (optional)
   :arg orient_matrix: Matrix
   :type orient_matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (optional)
   :arg orient_matrix_type: Matrix Orientation
   :type orient_matrix_type: enum in [], (optional)
   :arg constraint_axis: Constraint Axis
   :type constraint_axis: boolean array of 3 items, (optional)
   :arg gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
   :type gpencil_strokes: boolean, (optional)
   :arg center_override: Center Override, Force using this center value (when set)
   :type center_override: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: push_pull(*, value=0.0, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Push/Pull selected items

   :arg value: Distance
   :type value: float in [-inf, inf], (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg center_override: Center Override, Force using this center value (when set)
   :type center_override: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: resize(*, value=(1.0, 1.0, 1.0), mouse_dir_constraint=(0.0, 0.0, 0.0), orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, snap_point=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, use_duplicated_keyframes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Scale (resize) selected items

   :arg value: Scale
   :type value: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg mouse_dir_constraint: Mouse Directional Constraint
   :type mouse_dir_constraint: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg orient_type: Orientation, Transformation orientation
   :type orient_type: enum in [], (optional)
   :arg orient_matrix: Matrix
   :type orient_matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (optional)
   :arg orient_matrix_type: Matrix Orientation
   :type orient_matrix_type: enum in [], (optional)
   :arg constraint_axis: Constraint Axis
   :type constraint_axis: boolean array of 3 items, (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg snap_elements: Snap to Elements
   :type snap_elements: enum set in :ref:`rna_enum_snap_element_items`, (optional)
   :arg use_snap_project: Project Individual Elements
   :type use_snap_project: boolean, (optional)
   :arg snap_target: Snap Base, Point on source that will snap to target
   :type snap_target: enum in :ref:`rna_enum_snap_source_items`, (optional)
   :arg use_snap_self: Target: Include Active
   :type use_snap_self: boolean, (optional)
   :arg use_snap_edit: Target: Include Edit
   :type use_snap_edit: boolean, (optional)
   :arg use_snap_nonedit: Target: Include Non-Edited
   :type use_snap_nonedit: boolean, (optional)
   :arg use_snap_selectable: Target: Exclude Non-Selectable
   :type use_snap_selectable: boolean, (optional)
   :arg snap_point: Point
   :type snap_point: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
   :type gpencil_strokes: boolean, (optional)
   :arg texture_space: Edit Texture Space, Edit object data texture space
   :type texture_space: boolean, (optional)
   :arg remove_on_cancel: Remove on Cancel, Remove elements on cancel
   :type remove_on_cancel: boolean, (optional)
   :arg use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
   :type use_duplicated_keyframes: boolean, (optional)
   :arg center_override: Center Override, Force using this center value (when set)
   :type center_override: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: rotate(*, value=0.0, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, snap_point=(0.0, 0.0, 0.0), gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Rotate selected items

   :arg value: Angle
   :type value: float in [-inf, inf], (optional)
   :arg orient_axis: Axis
   :type orient_axis: enum in :ref:`rna_enum_axis_xyz_items`, (optional)
   :arg orient_type: Orientation, Transformation orientation
   :type orient_type: enum in [], (optional)
   :arg orient_matrix: Matrix
   :type orient_matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (optional)
   :arg orient_matrix_type: Matrix Orientation
   :type orient_matrix_type: enum in [], (optional)
   :arg constraint_axis: Constraint Axis
   :type constraint_axis: boolean array of 3 items, (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg snap_elements: Snap to Elements
   :type snap_elements: enum set in :ref:`rna_enum_snap_element_items`, (optional)
   :arg use_snap_project: Project Individual Elements
   :type use_snap_project: boolean, (optional)
   :arg snap_target: Snap Base, Point on source that will snap to target
   :type snap_target: enum in :ref:`rna_enum_snap_source_items`, (optional)
   :arg use_snap_self: Target: Include Active
   :type use_snap_self: boolean, (optional)
   :arg use_snap_edit: Target: Include Edit
   :type use_snap_edit: boolean, (optional)
   :arg use_snap_nonedit: Target: Include Non-Edited
   :type use_snap_nonedit: boolean, (optional)
   :arg use_snap_selectable: Target: Exclude Non-Selectable
   :type use_snap_selectable: boolean, (optional)
   :arg snap_point: Point
   :type snap_point: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
   :type gpencil_strokes: boolean, (optional)
   :arg center_override: Center Override, Force using this center value (when set)
   :type center_override: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: rotate_normal(*, value=0.0, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, release_confirm=False, use_accurate=False)

   Rotate split normal of selected items

   :arg value: Angle
   :type value: float in [-inf, inf], (optional)
   :arg orient_axis: Axis
   :type orient_axis: enum in :ref:`rna_enum_axis_xyz_items`, (optional)
   :arg orient_type: Orientation, Transformation orientation
   :type orient_type: enum in [], (optional)
   :arg orient_matrix: Matrix
   :type orient_matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (optional)
   :arg orient_matrix_type: Matrix Orientation
   :type orient_matrix_type: enum in [], (optional)
   :arg constraint_axis: Constraint Axis
   :type constraint_axis: boolean array of 3 items, (optional)
   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: select_orientation(*, orientation='GLOBAL')

   Select transformation orientation

   :arg orientation: Orientation, Transformation orientation
   :type orientation: enum in [], (optional)

.. function:: seq_slide(*, value=(0.0, 0.0), use_restore_handle_selection=False, snap=False, view2d_edge_pan=False, release_confirm=False, use_accurate=False)

   Slide a sequence strip in time

   :arg value: Offset
   :type value: :class:`mathutils.Vector` of 2 items in [-inf, inf], (optional)
   :arg use_restore_handle_selection: Restore Handle Selection, Restore handle selection after tweaking
   :type use_restore_handle_selection: boolean, (optional)
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg view2d_edge_pan: Edge Pan, Enable edge panning in 2D view
   :type view2d_edge_pan: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: shear(*, value=0.0, orient_axis='Z', orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, gpencil_strokes=False, release_confirm=False, use_accurate=False)

   Shear selected items along the given axis

   :arg value: Offset
   :type value: float in [-inf, inf], (optional)
   :arg orient_axis: Axis
   :type orient_axis: enum in :ref:`rna_enum_axis_xyz_items`, (optional)
   :arg orient_axis_ortho: Axis Ortho
   :type orient_axis_ortho: enum in :ref:`rna_enum_axis_xyz_items`, (optional)
   :arg orient_type: Orientation, Transformation orientation
   :type orient_type: enum in [], (optional)
   :arg orient_matrix: Matrix
   :type orient_matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (optional)
   :arg orient_matrix_type: Matrix Orientation
   :type orient_matrix_type: enum in [], (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
   :type gpencil_strokes: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: shrink_fatten(*, value=0.0, use_even_offset=False, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, release_confirm=False, use_accurate=False)

   Shrink/fatten selected vertices along normals

   :arg value: Offset
   :type value: float in [-inf, inf], (optional)
   :arg use_even_offset: Offset Even, Scale the offset to give more even thickness
   :type use_even_offset: boolean, (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: skin_resize(*, value=(1.0, 1.0, 1.0), orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, snap_point=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Scale selected vertices' skin radii

   :arg value: Scale
   :type value: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg orient_type: Orientation, Transformation orientation
   :type orient_type: enum in [], (optional)
   :arg orient_matrix: Matrix
   :type orient_matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (optional)
   :arg orient_matrix_type: Matrix Orientation
   :type orient_matrix_type: enum in [], (optional)
   :arg constraint_axis: Constraint Axis
   :type constraint_axis: boolean array of 3 items, (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg snap_elements: Snap to Elements
   :type snap_elements: enum set in :ref:`rna_enum_snap_element_items`, (optional)
   :arg use_snap_project: Project Individual Elements
   :type use_snap_project: boolean, (optional)
   :arg snap_target: Snap Base, Point on source that will snap to target
   :type snap_target: enum in :ref:`rna_enum_snap_source_items`, (optional)
   :arg use_snap_self: Target: Include Active
   :type use_snap_self: boolean, (optional)
   :arg use_snap_edit: Target: Include Edit
   :type use_snap_edit: boolean, (optional)
   :arg use_snap_nonedit: Target: Include Non-Edited
   :type use_snap_nonedit: boolean, (optional)
   :arg use_snap_selectable: Target: Exclude Non-Selectable
   :type use_snap_selectable: boolean, (optional)
   :arg snap_point: Point
   :type snap_point: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: tilt(*, value=0.0, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, release_confirm=False, use_accurate=False)

   Tilt selected control vertices of 3D curve

   :arg value: Angle
   :type value: float in [-inf, inf], (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: tosphere(*, value=0.0, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Move selected items outward in a spherical shape around geometric center

   :arg value: Factor
   :type value: float in [0, 1], (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
   :type gpencil_strokes: boolean, (optional)
   :arg center_override: Center Override, Force using this center value (when set)
   :type center_override: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: trackball(*, value=(0.0, 0.0), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, gpencil_strokes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False)

   Trackball style rotation of selected items

   :arg value: Angle
   :type value: float array of 2 items in [-inf, inf], (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
   :type gpencil_strokes: boolean, (optional)
   :arg center_override: Center Override, Force using this center value (when set)
   :type center_override: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: transform(*, mode='TRANSLATION', value=(0.0, 0.0, 0.0, 0.0), orient_axis='Z', orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, use_duplicated_keyframes=False, center_override=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False, use_automerge_and_split=False)

   Transform selected items by mode type

   :arg mode: Mode
   :type mode: enum in :ref:`rna_enum_transform_mode_type_items`, (optional)
   :arg value: Values
   :type value: :class:`mathutils.Vector` of 4 items in [-inf, inf], (optional)
   :arg orient_axis: Axis
   :type orient_axis: enum in :ref:`rna_enum_axis_xyz_items`, (optional)
   :arg orient_type: Orientation, Transformation orientation
   :type orient_type: enum in :ref:`rna_enum_transform_orientation_items`, (optional)
   :arg orient_matrix: Matrix
   :type orient_matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (optional)
   :arg orient_matrix_type: Matrix Orientation
   :type orient_matrix_type: enum in :ref:`rna_enum_transform_orientation_items`, (optional)
   :arg constraint_axis: Constraint Axis
   :type constraint_axis: boolean array of 3 items, (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg snap_elements: Snap to Elements
   :type snap_elements: enum set in :ref:`rna_enum_snap_element_items`, (optional)
   :arg use_snap_project: Project Individual Elements
   :type use_snap_project: boolean, (optional)
   :arg snap_target: Snap Base, Point on source that will snap to target
   :type snap_target: enum in :ref:`rna_enum_snap_source_items`, (optional)
   :arg use_snap_self: Target: Include Active
   :type use_snap_self: boolean, (optional)
   :arg use_snap_edit: Target: Include Edit
   :type use_snap_edit: boolean, (optional)
   :arg use_snap_nonedit: Target: Include Non-Edited
   :type use_snap_nonedit: boolean, (optional)
   :arg use_snap_selectable: Target: Exclude Non-Selectable
   :type use_snap_selectable: boolean, (optional)
   :arg snap_point: Point
   :type snap_point: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg snap_align: Align with Point Normal
   :type snap_align: boolean, (optional)
   :arg snap_normal: Normal
   :type snap_normal: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
   :type gpencil_strokes: boolean, (optional)
   :arg texture_space: Edit Texture Space, Edit object data texture space
   :type texture_space: boolean, (optional)
   :arg remove_on_cancel: Remove on Cancel, Remove elements on cancel
   :type remove_on_cancel: boolean, (optional)
   :arg use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
   :type use_duplicated_keyframes: boolean, (optional)
   :arg center_override: Center Override, Force using this center value (when set)
   :type center_override: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)
   :arg use_automerge_and_split: Auto Merge & Split, Forces the use of Auto Merge and Split
   :type use_automerge_and_split: boolean, (optional)

.. function:: translate(*, value=(0.0, 0.0, 0.0), orient_type='GLOBAL', orient_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.0, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, cursor_transform=False, texture_space=False, remove_on_cancel=False, use_duplicated_keyframes=False, view2d_edge_pan=False, release_confirm=False, use_accurate=False, use_automerge_and_split=False, translate_origin=False)

   Move selected items

   :arg value: Move
   :type value: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg orient_type: Orientation, Transformation orientation
   :type orient_type: enum in :ref:`rna_enum_transform_orientation_items`, (optional)
   :arg orient_matrix: Matrix
   :type orient_matrix: :class:`mathutils.Matrix` of 3 * 3 items in [-inf, inf], (optional)
   :arg orient_matrix_type: Matrix Orientation
   :type orient_matrix_type: enum in :ref:`rna_enum_transform_orientation_items`, (optional)
   :arg constraint_axis: Constraint Axis
   :type constraint_axis: boolean array of 3 items, (optional)
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
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg snap_elements: Snap to Elements
   :type snap_elements: enum set in :ref:`rna_enum_snap_element_items`, (optional)
   :arg use_snap_project: Project Individual Elements
   :type use_snap_project: boolean, (optional)
   :arg snap_target: Snap Base, Point on source that will snap to target
   :type snap_target: enum in :ref:`rna_enum_snap_source_items`, (optional)
   :arg use_snap_self: Target: Include Active
   :type use_snap_self: boolean, (optional)
   :arg use_snap_edit: Target: Include Edit
   :type use_snap_edit: boolean, (optional)
   :arg use_snap_nonedit: Target: Include Non-Edited
   :type use_snap_nonedit: boolean, (optional)
   :arg use_snap_selectable: Target: Exclude Non-Selectable
   :type use_snap_selectable: boolean, (optional)
   :arg snap_point: Point
   :type snap_point: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg snap_align: Align with Point Normal
   :type snap_align: boolean, (optional)
   :arg snap_normal: Normal
   :type snap_normal: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
   :type gpencil_strokes: boolean, (optional)
   :arg cursor_transform: Transform Cursor
   :type cursor_transform: boolean, (optional)
   :arg texture_space: Edit Texture Space, Edit object data texture space
   :type texture_space: boolean, (optional)
   :arg remove_on_cancel: Remove on Cancel, Remove elements on cancel
   :type remove_on_cancel: boolean, (optional)
   :arg use_duplicated_keyframes: Duplicated Keyframes, Transform duplicated keyframes
   :type use_duplicated_keyframes: boolean, (optional)
   :arg view2d_edge_pan: Edge Pan, Enable edge panning in 2D view
   :type view2d_edge_pan: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)
   :arg use_automerge_and_split: Auto Merge & Split, Forces the use of Auto Merge and Split
   :type use_automerge_and_split: boolean, (optional)
   :arg translate_origin: Translate Origin, Translate origin instead of selection
   :type translate_origin: boolean, (optional)

.. function:: vert_crease(*, value=0.0, snap=False, release_confirm=False, use_accurate=False)

   Change the crease of vertices

   :arg value: Factor
   :type value: float in [-1, 1], (optional)
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: vert_slide(*, value=0.0, use_even=False, flipped=False, use_clamp=True, mirror=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, snap_point=(0.0, 0.0, 0.0), correct_uv=True, release_confirm=False, use_accurate=False)

   Slide a vertex along a mesh

   :arg value: Factor
   :type value: float in [-10, 10], (optional)
   :arg use_even: Even, Make the edge loop match the shape of the adjacent edge loop
   :type use_even: boolean, (optional)
   :arg flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
   :type flipped: boolean, (optional)
   :arg use_clamp: Clamp, Clamp within the edge extents
   :type use_clamp: boolean, (optional)
   :arg mirror: Mirror Editing
   :type mirror: boolean, (optional)
   :arg snap: Use Snapping Options
   :type snap: boolean, (optional)
   :arg snap_elements: Snap to Elements
   :type snap_elements: enum set in :ref:`rna_enum_snap_element_items`, (optional)
   :arg use_snap_project: Project Individual Elements
   :type use_snap_project: boolean, (optional)
   :arg snap_target: Snap Base, Point on source that will snap to target
   :type snap_target: enum in :ref:`rna_enum_snap_source_items`, (optional)
   :arg use_snap_self: Target: Include Active
   :type use_snap_self: boolean, (optional)
   :arg use_snap_edit: Target: Include Edit
   :type use_snap_edit: boolean, (optional)
   :arg use_snap_nonedit: Target: Include Non-Edited
   :type use_snap_nonedit: boolean, (optional)
   :arg use_snap_selectable: Target: Exclude Non-Selectable
   :type use_snap_selectable: boolean, (optional)
   :arg snap_point: Point
   :type snap_point: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)
   :arg correct_uv: Correct UVs, Correct UV coordinates when transforming
   :type correct_uv: boolean, (optional)
   :arg release_confirm: Confirm on Release, Always confirm operation when releasing button
   :type release_confirm: boolean, (optional)
   :arg use_accurate: Accurate, Use accurate transformation
   :type use_accurate: boolean, (optional)

.. function:: vertex_random(*, offset=0.0, uniform=0.0, normal=0.0, seed=0, wait_for_input=True)

   Randomize vertices

   :arg offset: Amount, Distance to offset
   :type offset: float in [-inf, inf], (optional)
   :arg uniform: Uniform, Increase for uniform offset distance
   :type uniform: float in [0, 1], (optional)
   :arg normal: Normal, Align offset direction to normals
   :type normal: float in [0, 1], (optional)
   :arg seed: Random Seed, Seed for the random number generator
   :type seed: int in [0, 10000], (optional)
   :arg wait_for_input: Wait for Input
   :type wait_for_input: boolean, (optional)

.. function:: vertex_warp(*, warp_angle=6.28319, offset_angle=0.0, min=-1.0, max=1.0, viewmat=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), center=(0.0, 0.0, 0.0))

   Warp vertices around the cursor

   :arg warp_angle: Warp Angle, Amount to warp about the cursor
   :type warp_angle: float in [-inf, inf], (optional)
   :arg offset_angle: Offset Angle, Angle to use as the basis for warping
   :type offset_angle: float in [-inf, inf], (optional)
   :arg min: Min
   :type min: float in [-inf, inf], (optional)
   :arg max: Max
   :type max: float in [-inf, inf], (optional)
   :arg viewmat: Matrix
   :type viewmat: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], (optional)
   :arg center: Center
   :type center: :class:`mathutils.Vector` of 3 items in [-inf, inf], (optional)

