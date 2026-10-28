ParticleEdit(bpy_struct)
========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ParticleEdit(bpy_struct)

   Properties of particle editing mode

   .. data:: brush

      :type: :class:`ParticleBrush`, (readonly)

   .. attribute:: default_key_count

      How many keys to make new particles with

      :type: int in [2, 32767], default 5

   .. attribute:: display_step

      How many steps to display the path with

      :type: int in [1, 10], default 2

   .. attribute:: emitter_distance

      Distance to keep particles away from the emitter

      :type: float in [-inf, inf], default 0.25

   .. attribute:: fade_frames

      How many frames to fade

      :type: int in [1, 100], default 2

   .. data:: is_editable

      A valid edit mode exists

      :type: boolean, default False, (readonly)

   .. data:: is_hair

      Editing hair

      :type: boolean, default False, (readonly)

   .. data:: object

      The edited object

      :type: :class:`Object`, (readonly)

   .. attribute:: select_mode

      Particle select and display mode

      * ``PATH``
        Path -- Path edit mode.
      * ``POINT``
        Point -- Point select mode.
      * ``TIP``
        Tip -- Tip select mode.

      :type: enum in [``'PATH'``, ``'POINT'``, ``'TIP'``], default ``'PATH'``

   .. attribute:: shape_object

      Outer shape to use for tools

      :type: :class:`Object`

   .. attribute:: show_particles

      Display actual particles

      :type: boolean, default False

   .. attribute:: tool

      * ``COMB``
        Comb -- Comb hairs.
      * ``SMOOTH``
        Smooth -- Smooth hairs.
      * ``ADD``
        Add -- Add hairs.
      * ``LENGTH``
        Length -- Make hairs longer or shorter.
      * ``PUFF``
        Puff -- Make hairs stand up.
      * ``CUT``
        Cut -- Cut hairs.
      * ``WEIGHT``
        Weight -- Weight hair particles.

      :type: enum in [``'COMB'``, ``'SMOOTH'``, ``'ADD'``, ``'LENGTH'``, ``'PUFF'``, ``'CUT'``, ``'WEIGHT'``], default ``'COMB'``

   .. attribute:: type

      :type: enum in [``'PARTICLES'``, ``'SOFT_BODY'``, ``'CLOTH'``], default ``'PARTICLES'``

   .. attribute:: use_auto_velocity

      Calculate point velocities automatically

      :type: boolean, default True

   .. attribute:: use_default_interpolate

      Interpolate new particles from the existing ones

      :type: boolean, default False

   .. attribute:: use_emitter_deflect

      Keep paths from intersecting the emitter

      :type: boolean, default True

   .. attribute:: use_fade_time

      Fade paths and keys further away from current frame

      :type: boolean, default False

   .. attribute:: use_preserve_length

      Keep path lengths constant

      :type: boolean, default True

   .. attribute:: use_preserve_root

      Keep root keys unmodified

      :type: boolean, default True

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

   * :class:`ToolSettings.particle_edit`

