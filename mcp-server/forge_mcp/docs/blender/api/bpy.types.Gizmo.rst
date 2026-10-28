Gizmo(bpy_struct)
=================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Gizmo(bpy_struct)

   Collection of gizmos

   .. attribute:: alpha

      :type: float in [0, 1], default 0.0

   .. attribute:: alpha_highlight

      :type: float in [0, 1], default 0.0

   .. attribute:: bl_idname

      :type: string, default "", (never None)

   .. attribute:: color

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: color_highlight

      :type: :class:`mathutils.Color` of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. data:: group

      Gizmo group this gizmo is a member of

      :type: :class:`GizmoGroup`, (readonly)

   .. attribute:: hide

      :type: boolean, default False

   .. attribute:: hide_keymap

      Ignore the key-map for this gizmo

      :type: boolean, default False

   .. attribute:: hide_select

      :type: boolean, default False

   .. data:: is_highlight

      :type: boolean, default False, (readonly)

   .. data:: is_modal

      :type: boolean, default False, (readonly)

   .. attribute:: line_width

      :type: float in [0, inf], default 0.0

   .. attribute:: matrix_basis

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: matrix_offset

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. attribute:: matrix_space

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))

   .. data:: matrix_world

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

   .. data:: properties

      :type: :class:`GizmoProperties`, (readonly, never None)

   .. attribute:: scale_basis

      :type: float in [0, inf], default 0.0

   .. attribute:: select

      :type: boolean, default False

   .. attribute:: select_bias

      Depth bias used for selection

      :type: float in [-inf, inf], default 0.0

   .. attribute:: use_draw_hover

      :type: boolean, default False

   .. attribute:: use_draw_modal

      Show while dragging

      :type: boolean, default False

   .. attribute:: use_draw_offset_scale

      Scale the offset matrix (use to apply screen-space offset)

      :type: boolean, default False

   .. attribute:: use_draw_scale

      Use scale when calculating the matrix

      :type: boolean, default True

   .. attribute:: use_draw_value

      Show an indicator for the current value while dragging

      :type: boolean, default False

   .. attribute:: use_event_handle_all

      When highlighted, do not pass events through to be handled by other keymaps

      :type: boolean, default False

   .. attribute:: use_grab_cursor

      :type: boolean, default False

   .. attribute:: use_operator_tool_properties

      Merge active tool properties on activation (does not overwrite existing)

      :type: boolean, default False

   .. attribute:: use_select_background

      Don't write into the depth buffer

      :type: boolean, default False

   .. attribute:: use_tooltip

      Use tooltips when hovering over this gizmo

      :type: boolean, default True

   .. method:: draw(context)

      

      :type context: :class:`Context`, (never None)

   .. method:: draw_select(context, *, select_id=0)

      

      :type context: :class:`Context`, (never None)
      :type select_id: int in [0, inf], (optional)

   .. method:: test_select(context, location)

      

      :type context: :class:`Context`, (never None)
      :arg location: Location, Region coordinates
      :type location: int array of 2 items in [-inf, inf], (never None)
      :return: Use -1 to skip this gizmo
      :rtype: int in [-1, inf]

   .. method:: modal(context, event, tweak)

      

      :type context: :class:`Context`, (never None)
      :type event: :class:`Event`, (never None)
      :arg tweak: Tweak
      :type tweak: enum set in {``'PRECISE'``, ``'SNAP'``}
      :return: result
      :rtype: enum set in :ref:`rna_enum_operator_return_items`

   .. method:: setup()

      


   .. method:: invoke(context, event)

      

      :type context: :class:`Context`, (never None)
      :type event: :class:`Event`, (never None)
      :return: result
      :rtype: enum set in :ref:`rna_enum_operator_return_items`

   .. method:: exit(context, cancel)

      

      :type context: :class:`Context`, (never None)
      :arg cancel: Cancel, otherwise confirm
      :type cancel: boolean

   .. method:: select_refresh()

      


   .. method:: draw_preset_box(matrix, *, select_id=-1)

      Draw a box

      :arg matrix: The matrix to transform
      :type matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]
      :arg select_id: ID to use when gizmo is selectable. Use -1 when not selecting.
      :type select_id: int in [-1, inf], (optional)

   .. method:: draw_preset_arrow(matrix, *, axis='POS_Z', select_id=-1)

      Draw a box

      :arg matrix: The matrix to transform
      :type matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]
      :arg axis: Arrow Orientation
      :type axis: enum in :ref:`rna_enum_object_axis_items`, (optional)
      :arg select_id: ID to use when gizmo is selectable. Use -1 when not selecting.
      :type select_id: int in [-1, inf], (optional)

   .. method:: draw_preset_circle(matrix, *, axis='POS_Z', select_id=-1)

      Draw a box

      :arg matrix: The matrix to transform
      :type matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]
      :arg axis: Arrow Orientation
      :type axis: enum in :ref:`rna_enum_object_axis_items`, (optional)
      :arg select_id: ID to use when gizmo is selectable. Use -1 when not selecting.
      :type select_id: int in [-1, inf], (optional)

   .. method:: target_set_prop(target, data, property, *, index=-1)

      

      :arg target: Target property
      :type target: string, (never None)
      :arg data: Data from which to take property
      :type data: :class:`AnyType`, (never None)
      :arg property: Identifier of property in data
      :type property: string, (never None)
      :type index: int in [-1, inf], (optional)

   .. method:: target_set_operator(operator, *, index=0)

      Operator to run when activating the gizmo (overrides property targets)

      :arg operator: Target operator
      :type operator: string, (never None)
      :arg index: Part index
      :type index: int in [0, 255], (optional)
      :return: Operator properties to fill in
      :rtype: :class:`OperatorProperties`

   .. method:: target_is_valid(property)

      

      :arg property: Property identifier
      :type property: string, (never None)
      :rtype: boolean

   .. method:: draw_custom_shape(shape, *, matrix=None, select_id=None)

      Draw a shape created form :class:`Gizmo.draw_custom_shape`.
      
      :arg shape: The cached shape to draw.
      :type shape: Any
      :arg matrix: 4x4 matrix, when not given :class:`Gizmo.matrix_world` is used.
      :type matrix: :class:`mathutils.Matrix`
      :arg select_id: The selection id.
         Only use when drawing within :class:`Gizmo.draw_select`.
      :type select_id: int

   .. staticmethod:: new_custom_shape(type, verts)

      Create a new shape that can be passed to :class:`Gizmo.draw_custom_shape`.
      
      :arg type: The type of shape to create in (POINTS, LINES, TRIS, LINE_STRIP).
      :type type: str
      :arg verts: Sequence of 2D or 3D coordinates.
      :type verts: Sequence[Sequence[float]]
      :return: The newly created shape (the return type make change).
      :rtype: Any

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


   .. method:: target_get_range(target):
   
      Get the range for this target property.
   
      :arg target: Target property name.
      :return: The range of this property (min, max).
      :rtype: tuple[float, float]


   .. method:: target_get_value(target):
   
      Get the value of this target property.
   
      :arg target: Target property name.
      :type target: str
      :return: The value of the target property as a value or array based on the target type.
      :rtype: float | tuple[float, ...]


   .. method:: target_set_handler(target, get, set, range=None):
   
      Assigns callbacks to a gizmos property.
   
      :arg target: Target property name.
      :type target: str
      :arg get: Function that returns the value for this property (single value or sequence).
      :type get: Callable[[], float | Sequence[float]]
      :arg set: Function that takes a single value argument and applies it.
      :type set: Callable[[tuple[float, ...]], Any]
      :arg range: Function that returns a (min, max) tuple for gizmos that use a range. The returned value is not used.
      :type range: callable


   .. method:: target_set_value(target):
   
      Set the value of this target property.
   
      :arg target: Target property name.
      :type target: str


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

   * :class:`GizmoGroup.gizmos`
   * :class:`GizmoGroup.invoke_prepare`
   * :class:`Gizmos.new`
   * :class:`Gizmos.remove`

