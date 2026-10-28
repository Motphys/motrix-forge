Rigidbody Operators
===================

.. module:: bpy.ops.rigidbody

.. function:: bake_to_keyframes(*, frame_start=1, frame_end=250, step=1)

   Bake rigid body transformations of selected objects to keyframes

   :arg frame_start: Start Frame, Start frame for baking
   :type frame_start: int in [0, 300000], (optional)
   :arg frame_end: End Frame, End frame for baking
   :type frame_end: int in [1, 300000], (optional)
   :arg step: Frame Step, Frame Step
   :type step: int in [1, 120], (optional)
   :File: `startup\bl_operators\rigidbody.py\:108 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\rigidbody.py#L108>`__


.. function:: connect(*, con_type='FIXED', pivot_type='CENTER', connection_pattern='SELECTED_TO_ACTIVE')

   Create rigid body constraints between selected rigid bodies

   :arg con_type: Type, Type of generated constraint

      * ``FIXED``
        Fixed -- Glue rigid bodies together.
      * ``POINT``
        Point -- Constrain rigid bodies to move around common pivot point.
      * ``HINGE``
        Hinge -- Restrict rigid body rotation to one axis.
      * ``SLIDER``
        Slider -- Restrict rigid body translation to one axis.
      * ``PISTON``
        Piston -- Restrict rigid body translation and rotation to one axis.
      * ``GENERIC``
        Generic -- Restrict translation and rotation to specified axes.
      * ``GENERIC_SPRING``
        Generic Spring -- Restrict translation and rotation to specified axes with springs.
      * ``MOTOR``
        Motor -- Drive rigid body around or along an axis.
   :type con_type: enum in [``'FIXED'``, ``'POINT'``, ``'HINGE'``, ``'SLIDER'``, ``'PISTON'``, ``'GENERIC'``, ``'GENERIC_SPRING'``, ``'MOTOR'``], (optional)
   :arg pivot_type: Location, Constraint pivot location

      * ``CENTER``
        Center -- Pivot location is between the constrained rigid bodies.
      * ``ACTIVE``
        Active -- Pivot location is at the active object position.
      * ``SELECTED``
        Selected -- Pivot location is at the selected object position.
   :type pivot_type: enum in [``'CENTER'``, ``'ACTIVE'``, ``'SELECTED'``], (optional)
   :arg connection_pattern: Connection Pattern, Pattern used to connect objects

      * ``SELECTED_TO_ACTIVE``
        Selected to Active -- Connect selected objects to the active object.
      * ``CHAIN_DISTANCE``
        Chain by Distance -- Connect objects as a chain based on distance, starting at the active object.
   :type connection_pattern: enum in [``'SELECTED_TO_ACTIVE'``, ``'CHAIN_DISTANCE'``], (optional)
   :File: `startup\bl_operators\rigidbody.py\:270 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\rigidbody.py#L270>`__


.. function:: constraint_add(*, type='FIXED')

   Add Rigid Body Constraint to active object

   :arg type: Rigid Body Constraint Type
   :type type: enum in :ref:`rna_enum_rigidbody_constraint_type_items`, (optional)

.. function:: constraint_remove()

   Remove Rigid Body Constraint from Object

.. function:: mass_calculate(*, material='DEFAULT', density=1.0)

   Automatically calculate mass values for Rigid Body Objects based on volume

   :arg material: Material Preset, Type of material that objects are made of (determines material density)
   :type material: enum in [``'DEFAULT'``], (optional)
   :arg density: Density, Density value (kg/m^3), allows custom value if the 'Custom' preset is used
   :type density: float in [1.17549e-38, inf], (optional)

.. function:: object_add(*, type='ACTIVE')

   Add active object as Rigid Body

   :arg type: Rigid Body Type
   :type type: enum in :ref:`rna_enum_rigidbody_object_type_items`, (optional)

.. function:: object_remove()

   Remove Rigid Body settings from Object

.. function:: object_settings_copy()

   Copy Rigid Body settings from active object to selected

   :File: `startup\bl_operators\rigidbody.py\:45 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\rigidbody.py#L45>`__

.. function:: objects_add(*, type='ACTIVE')

   Add selected objects as Rigid Bodies

   :arg type: Rigid Body Type
   :type type: enum in :ref:`rna_enum_rigidbody_object_type_items`, (optional)

.. function:: objects_remove()

   Remove selected objects from Rigid Body simulation

.. function:: shape_change(*, type='MESH')

   Change collision shapes for selected Rigid Body Objects

   :arg type: Rigid Body Shape
   :type type: enum in :ref:`rna_enum_rigidbody_object_shape_items`, (optional)

.. function:: world_add()

   Add Rigid Body simulation world to the current scene

.. function:: world_remove()

   Remove Rigid Body simulation world from the current scene

