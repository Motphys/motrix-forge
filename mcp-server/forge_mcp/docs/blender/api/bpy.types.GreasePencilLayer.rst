GreasePencilLayer(GreasePencilTreeNode)
=======================================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`GreasePencilTreeNode`

.. class:: GreasePencilLayer(GreasePencilTreeNode)

   Collection of related drawings

   .. attribute:: blend_mode

      Blend mode

      :type: enum in [``'REGULAR'``, ``'HARDLIGHT'``, ``'ADD'``, ``'SUBTRACT'``, ``'MULTIPLY'``, ``'DIVIDE'``], default ``'REGULAR'``

   .. data:: frames

      Grease Pencil frames

      :type: :class:`GreasePencilFrames` :class:`bpy_prop_collection` of :class:`GreasePencilFrame`, (readonly)

   .. attribute:: ignore_locked_materials

      Allow editing strokes even if they use locked materials

      :type: boolean, default False

   .. attribute:: lock_frame

      Lock current frame displayed by layer

      :type: boolean, default False

   .. data:: mask_layers

      List of Masking Layers

      :type: :class:`GreasePencilLayerMasks` :class:`bpy_prop_collection` of :class:`GreasePencilLayerMask`, (readonly)

   .. data:: matrix_local

      Local transformation matrix of the layer

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

   .. data:: matrix_parent_inverse

      Inverse of layer's parent transformation matrix

      :type: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), (readonly)

   .. attribute:: opacity

      Layer Opacity

      :type: float in [0, 1], default 0.0

   .. attribute:: parent

      Parent object

      :type: :class:`Object`

   .. attribute:: parent_bone

      Name of parent bone. Only used when the parent object is an armature.

      :type: string, default "", (never None)

   .. attribute:: pass_index

      Index number for the "Layer Index" pass

      :type: int in [0, inf], default 0

   .. attribute:: radius_offset

      Radius change to apply to current strokes

      :type: float in [-inf, inf], default 0.0

   .. attribute:: rotation

      Euler rotation of the layer

      :type: :class:`mathutils.Euler` rotation of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: scale

      Scale of the layer

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (1.0, 1.0, 1.0)

   .. attribute:: tint_color

      Color for tinting stroke colors

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: tint_factor

      Factor of tinting color

      :type: float in [0, 1], default 0.0

   .. attribute:: translation

      Translation of the layer

      :type: :class:`mathutils.Vector` of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)

   .. attribute:: use_lights

      Enable the use of lights on stroke and fill materials

      :type: boolean, default False

   .. attribute:: use_viewlayer_masks

      Include the mask layers when rendering the view-layer

      :type: boolean, default False

   .. attribute:: viewlayer_render

      Only include Layer in this View Layer render output (leave blank to include always)

      :type: string, default "", (never None)

   .. method:: get_frame_at(frame_number)

      Get the frame at given frame number

      :arg frame_number: Frame Number
      :type frame_number: int in [-1048574, 1048574]
      :return: Frame
      :rtype: :class:`GreasePencilFrame`

   .. method:: current_frame()

      The Grease Pencil frame at the current scene time on this layer

      :rtype: :class:`GreasePencilFrame`

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
   * :class:`GreasePencilTreeNode.name`
   * :class:`GreasePencilTreeNode.hide`
   * :class:`GreasePencilTreeNode.lock`
   * :class:`GreasePencilTreeNode.select`
   * :class:`GreasePencilTreeNode.use_onion_skinning`
   * :class:`GreasePencilTreeNode.use_masks`
   * :class:`GreasePencilTreeNode.channel_color`
   * :class:`GreasePencilTreeNode.next_node`
   * :class:`GreasePencilTreeNode.prev_node`
   * :class:`GreasePencilTreeNode.parent_group`

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
   * :class:`GreasePencilTreeNode.bl_rna_get_subclass`
   * :class:`GreasePencilTreeNode.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :class:`GreasePencilv3.layers`
   * :class:`GreasePencilv3Layers.active`
   * :class:`GreasePencilv3Layers.move`
   * :class:`GreasePencilv3Layers.move_bottom`
   * :class:`GreasePencilv3Layers.move_to_layer_group`
   * :class:`GreasePencilv3Layers.move_top`
   * :class:`GreasePencilv3Layers.new`
   * :class:`GreasePencilv3Layers.remove`

