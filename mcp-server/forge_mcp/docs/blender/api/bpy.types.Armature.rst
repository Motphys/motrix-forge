Armature(ID)
============

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Armature(ID)

   Armature data-block containing a hierarchy of bones, usually used for rigging characters

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: axes_position

      The position for the axes on the bone. Increasing the value moves it closer to the tip; decreasing moves it closer to the root.

      :type: float in [0, 1], default 0.0

   .. data:: bones

      :type: :class:`ArmatureBones` :class:`bpy_prop_collection` of :class:`Bone`, (readonly)

   .. attribute:: collections

      :type: :class:`BoneCollections` :class:`bpy_prop_collection` of :class:`BoneCollection`

   .. data:: collections_all

      List of all bone collections of the armature

      :type: :class:`bpy_prop_collection` of :class:`BoneCollection`, (readonly)

   .. attribute:: display_type

      * ``OCTAHEDRAL``
        Octahedral -- Display bones as octahedral shape (default).
      * ``STICK``
        Stick -- Display bones as simple 2D lines with dots.
      * ``BBONE``
        B-Bone -- Display bones as boxes, showing subdivision and B-Splines.
      * ``ENVELOPE``
        Envelope -- Display bones as extruded spheres, showing deformation influence volume.
      * ``WIRE``
        Wire -- Display bones as thin wires, showing subdivision and B-Splines.

      :type: enum in [``'OCTAHEDRAL'``, ``'STICK'``, ``'BBONE'``, ``'ENVELOPE'``, ``'WIRE'``], default ``'OCTAHEDRAL'``

   .. data:: edit_bones

      :type: :class:`ArmatureEditBones` :class:`bpy_prop_collection` of :class:`EditBone`, (readonly)

   .. data:: is_editmode

      True when used in editmode

      :type: boolean, default False, (readonly)

   .. attribute:: pose_position

      Show armature in binding pose or final posed state

      * ``POSE``
        Pose Position -- Show armature in posed state.
      * ``REST``
        Rest Position -- Show Armature in binding pose state (no posing possible).

      :type: enum in [``'POSE'``, ``'REST'``], default ``'POSE'``

   .. attribute:: relation_line_position

      The start position of the relation lines from parent to child bones

      * ``TAIL``
        Tail -- Draw the relationship line from the parent tail to the child head.
      * ``HEAD``
        Head -- Draw the relationship line from the parent head to the child head.

      :type: enum in [``'TAIL'``, ``'HEAD'``], default ``'TAIL'``

   .. attribute:: show_axes

      Display bone axes

      :type: boolean, default False

   .. attribute:: show_bone_colors

      Display bone colors

      :type: boolean, default True

   .. attribute:: show_bone_custom_shapes

      Display bones with their custom shapes

      :type: boolean, default True

   .. attribute:: show_names

      Display bone names

      :type: boolean, default False

   .. attribute:: use_mirror_x

      Apply changes to matching bone on opposite side of X-Axis

      :type: boolean, default False

   .. method:: transform(matrix)

      Transform armature bones by a matrix

      :arg matrix: Matrix
      :type matrix: :class:`mathutils.Matrix` of 4 * 4 items in [-inf, inf]

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
   * :class:`ID.name`
   * :class:`ID.name_full`
   * :class:`ID.id_type`
   * :class:`ID.session_uid`
   * :class:`ID.is_evaluated`
   * :class:`ID.original`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.use_extra_user`
   * :class:`ID.is_embedded_data`
   * :class:`ID.is_missing`
   * :class:`ID.is_runtime_data`
   * :class:`ID.is_editable`
   * :class:`ID.tag`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.library_weak_reference`
   * :class:`ID.asset_data`
   * :class:`ID.override_library`
   * :class:`ID.preview`

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
   * :class:`ID.rename`
   * :class:`ID.evaluated_get`
   * :class:`ID.copy`
   * :class:`ID.asset_mark`
   * :class:`ID.asset_clear`
   * :class:`ID.asset_generate_preview`
   * :class:`ID.override_create`
   * :class:`ID.override_hierarchy_create`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`
   * :class:`ID.preview_ensure`
   * :class:`ID.bl_rna_get_subclass`
   * :class:`ID.bl_rna_get_subclass_py`

References
----------

.. hlist::
   :columns: 2

   * :mod:`bpy.context.armature`
   * :class:`BlendData.armatures`
   * :class:`BlendDataArmatures.new`
   * :class:`BlendDataArmatures.remove`

