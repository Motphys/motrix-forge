GPencilLayer(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: GPencilLayer(bpy_struct)

   Collection of related sketches

   .. data:: active_frame

      Frame currently being displayed for this layer

      :type: :class:`GPencilFrame`, (readonly)

   .. attribute:: annotation_hide

      Set annotation Visibility

      :type: boolean, default False

   .. attribute:: annotation_onion_after_color

      Base color for ghosts after the active frame

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.25, 0.1, 1.0)

   .. attribute:: annotation_onion_after_range

      Maximum number of frames to show after current frame

      :type: int in [-1, 120], default 0

   .. attribute:: annotation_onion_before_color

      Base color for ghosts before the active frame

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.302, 0.851, 0.302)

   .. attribute:: annotation_onion_before_range

      Maximum number of frames to show before current frame

      :type: int in [-1, 120], default 0

   .. attribute:: annotation_onion_use_custom_color

      Use custom colors for onion skinning instead of the theme

      :type: boolean, default False

   .. attribute:: annotation_opacity

      Annotation Layer Opacity

      :type: float in [0, 1], default 0.0

   .. attribute:: color

      Color for all strokes in this layer

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. data:: frames

      Sketches for this layer on different frames

      :type: :class:`GPencilFrames` :class:`bpy_prop_collection` of :class:`GPencilFrame`, (readonly)

   .. attribute:: info

      Layer name

      :type: string, default "", (never None)

   .. data:: is_ruler

      This is a special ruler layer

      :type: boolean, default False, (readonly)

   .. attribute:: lock

      Protect layer from further editing and/or frame changes

      :type: boolean, default False

   .. attribute:: lock_frame

      Lock current frame displayed by layer

      :type: boolean, default False

   .. attribute:: select

      Layer is selected for editing in the Dope Sheet

      :type: boolean, default False

   .. attribute:: show_in_front

      Make the layer display in front of objects

      :type: boolean, default False

   .. attribute:: thickness

      Thickness of annotation strokes

      :type: int in [1, 10], default 0

   .. attribute:: use_annotation_onion_skinning

      Display annotation onion skins before and after the current frame

      :type: boolean, default False

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

   * :mod:`bpy.context.active_annotation_layer`
   * :class:`GreasePencil.layers`
   * :class:`GreasePencilLayers.new`
   * :class:`GreasePencilLayers.remove`

