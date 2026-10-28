ActionSlot(bpy_struct)
======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ActionSlot(bpy_struct)

   Identifier for a set of channels in this Action, that can be used by a data-block to specify what it gets animated by

   .. data:: active

      Whether this is the active slot, can be set by assigning to action.slots.active

      :type: boolean, default False, (readonly)

   .. data:: handle

      Number specific to this Slot, unique within the Action.
      This is used, for example, on a ActionKeyframeStrip to look up the ActionChannelbag for this Slot

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: identifier

      Used when connecting an Action to a data-block, to find the correct slot handle. This is the display name, prefixed by two characters determined by the slot's ID type

      :type: string, default "", (never None)

   .. attribute:: name_display

      Name of the slot, for display in the user interface. This name combined with the slot's data-block type is unique within its Action

      :type: string, default "", (never None)

   .. attribute:: select

      Selection state of the slot

      :type: boolean, default False

   .. attribute:: show_expanded

      Expanded state of the slot

      :type: boolean, default False

   .. attribute:: target_id_type

      Type of data-block that this slot is intended to animate; can be set when 'UNSPECIFIED' but is otherwise read-only

      * ``ACTION``
        Action.
      * ``ARMATURE``
        Armature.
      * ``BRUSH``
        Brush.
      * ``CACHEFILE``
        Cache File.
      * ``CAMERA``
        Camera.
      * ``COLLECTION``
        Collection.
      * ``CURVE``
        Curve.
      * ``CURVES``
        Curves.
      * ``FONT``
        Font.
      * ``GREASEPENCIL``
        Grease Pencil.
      * ``GREASEPENCIL_V3``
        Grease Pencil v3.
      * ``IMAGE``
        Image.
      * ``KEY``
        Key.
      * ``LATTICE``
        Lattice.
      * ``LIBRARY``
        Library.
      * ``LIGHT``
        Light.
      * ``LIGHT_PROBE``
        Light Probe.
      * ``LINESTYLE``
        Line Style.
      * ``MASK``
        Mask.
      * ``MATERIAL``
        Material.
      * ``MESH``
        Mesh.
      * ``META``
        Metaball.
      * ``MOVIECLIP``
        Movie Clip.
      * ``NODETREE``
        Node Tree.
      * ``OBJECT``
        Object.
      * ``PAINTCURVE``
        Paint Curve.
      * ``PALETTE``
        Palette.
      * ``PARTICLE``
        Particle.
      * ``POINTCLOUD``
        Point Cloud.
      * ``SCENE``
        Scene.
      * ``SCREEN``
        Screen.
      * ``SOUND``
        Sound.
      * ``SPEAKER``
        Speaker.
      * ``TEXT``
        Text.
      * ``TEXTURE``
        Texture.
      * ``VOLUME``
        Volume.
      * ``WINDOWMANAGER``
        Window Manager.
      * ``WORKSPACE``
        Workspace.
      * ``WORLD``
        World.
      * ``UNSPECIFIED``
        Unspecified -- Not yet specified. When this slot is first assigned to a data-block, this will be set to the type of that data-block.

      :type: enum in [``'ACTION'``, ``'ARMATURE'``, ``'BRUSH'``, ``'CACHEFILE'``, ``'CAMERA'``, ``'COLLECTION'``, ``'CURVE'``, ``'CURVES'``, ``'FONT'``, ``'GREASEPENCIL'``, ``'GREASEPENCIL_V3'``, ``'IMAGE'``, ``'KEY'``, ``'LATTICE'``, ``'LIBRARY'``, ``'LIGHT'``, ``'LIGHT_PROBE'``, ``'LINESTYLE'``, ``'MASK'``, ``'MATERIAL'``, ``'MESH'``, ``'META'``, ``'MOVIECLIP'``, ``'NODETREE'``, ``'OBJECT'``, ``'PAINTCURVE'``, ``'PALETTE'``, ``'PARTICLE'``, ``'POINTCLOUD'``, ``'SCENE'``, ``'SCREEN'``, ``'SOUND'``, ``'SPEAKER'``, ``'TEXT'``, ``'TEXTURE'``, ``'VOLUME'``, ``'WINDOWMANAGER'``, ``'WORKSPACE'``, ``'WORLD'``, ``'UNSPECIFIED'``], default ``'UNSPECIFIED'``

   .. data:: target_id_type_icon

      :type: int in [-inf, inf], default 0, (readonly)

   .. method:: users()

      Return the data-blocks that are animated by this slot of this action

      :return: users
      :rtype: :class:`bpy_prop_collection` of :class:`ID`

   .. method:: duplicate()

      Duplicate this slot, including all the animation data associated with it

      :return: Duplicated Slot, The slot created by duplicating this one
      :rtype: :class:`ActionSlot`

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

   * :class:`Action.slots`
   * :class:`ActionChannelbag.slot`
   * :class:`ActionChannelbags.new`
   * :class:`ActionConstraint.action_slot`
   * :class:`ActionConstraint.action_suitable_slots`
   * :class:`ActionKeyframeStrip.channelbag`
   * :class:`ActionKeyframeStrip.key_insert`
   * :class:`ActionSlot.duplicate`
   * :class:`ActionSlots.active`
   * :class:`ActionSlots.new`
   * :class:`ActionSlots.remove`
   * :class:`AnimData.action_slot`
   * :class:`AnimData.action_suitable_slots`
   * :class:`NlaStrip.action_slot`
   * :class:`NlaStrip.action_suitable_slots`

