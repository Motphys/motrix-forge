Gizmogroup Operators
====================

.. module:: bpy.ops.gizmogroup

.. function:: gizmo_select(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False)

   Select the currently highlighted gizmo

   :arg extend: Extend, Extend selection instead of deselecting everything first
   :type extend: boolean, (optional)
   :arg deselect: Deselect, Remove from selection
   :type deselect: boolean, (optional)
   :arg toggle: Toggle Selection, Toggle the selection
   :type toggle: boolean, (optional)
   :arg deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
   :type deselect_all: boolean, (optional)
   :arg select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
   :type select_passthrough: boolean, (optional)

.. function:: gizmo_tweak()

   Tweak the active gizmo

