Particle Operators
==================

.. module:: bpy.ops.particle

.. function:: brush_edit(*, stroke=None, pen_flip=False)

   Apply a stroke of brush to the particles

   :arg stroke: Stroke
   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg pen_flip: Pen Flip, Whether a tablet's eraser mode is being used
   :type pen_flip: boolean, (optional)

.. function:: connect_hair(*, all=False)

   Connect hair to the emitter mesh

   :arg all: All Hair, Connect all hair systems to the emitter mesh
   :type all: boolean, (optional)

.. function:: copy_particle_systems(*, space='OBJECT', remove_target_particles=True, use_active=False)

   Copy particle systems from the active object to selected objects

   :arg space: Space, Space transform for copying from one object to another

      * ``OBJECT``
        Object -- Copy inside each object's local space.
      * ``WORLD``
        World -- Copy in world space.
   :type space: enum in [``'OBJECT'``, ``'WORLD'``], (optional)
   :arg remove_target_particles: Remove Target Particles, Remove particle systems on the target objects
   :type remove_target_particles: boolean, (optional)
   :arg use_active: Use Active, Use the active particle system from the context
   :type use_active: boolean, (optional)

.. function:: delete(*, type='PARTICLE')

   Delete selected particles or keys

   :arg type: Type, Delete a full particle or only keys
   :type type: enum in [``'PARTICLE'``, ``'KEY'``], (optional)

.. function:: disconnect_hair(*, all=False)

   Disconnect hair from the emitter mesh

   :arg all: All Hair, Disconnect all hair systems from the emitter mesh
   :type all: boolean, (optional)

.. function:: duplicate_particle_system(*, use_duplicate_settings=False)

   Duplicate particle system within the active object

   :arg use_duplicate_settings: Duplicate Settings, Duplicate settings as well, so the new particle system uses its own settings
   :type use_duplicate_settings: boolean, (optional)

.. function:: dupliob_copy()

   Duplicate the current instance object

.. function:: dupliob_move_down()

   Move instance object down in the list

.. function:: dupliob_move_up()

   Move instance object up in the list

.. function:: dupliob_refresh()

   Refresh list of instance objects and their weights

.. function:: dupliob_remove()

   Remove the selected instance object

.. function:: edited_clear()

   Undo all edition performed on the particle system

.. function:: hair_dynamics_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove a Hair Dynamics Preset

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :File: `startup\bl_operators\presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L119>`__


.. function:: hide(*, unselected=False)

   Hide selected particles

   :arg unselected: Unselected, Hide unselected rather than selected
   :type unselected: boolean, (optional)

.. function:: mirror()

   Duplicate and mirror the selected particles along the local X axis

.. function:: new()

   Add new particle settings

.. function:: new_target()

   Add a new particle target

.. function:: particle_edit_toggle()

   Toggle particle edit mode

.. function:: rekey(*, keys_number=2)

   Change the number of keys of selected particles (root and tip keys included)

   :arg keys_number: Number of Keys
   :type keys_number: int in [2, inf], (optional)

.. function:: remove_doubles(*, threshold=0.0002)

   Remove selected particles close enough of others

   :arg threshold: Merge Distance, Threshold distance within which particles are removed
   :type threshold: float in [0, inf], (optional)

.. function:: reveal(*, select=True)

   Show hidden particles

   :arg select: Select
   :type select: boolean, (optional)

.. function:: select_all(*, action='TOGGLE')

   (De)select all particles' keys

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: select_less()

   Deselect boundary selected keys of each particle

.. function:: select_linked()

   Select all keys linked to already selected ones

.. function:: select_linked_pick(*, deselect=False, location=(0, 0))

   Select nearest particle from mouse pointer

   :arg deselect: Deselect, Deselect linked keys rather than selecting them
   :type deselect: boolean, (optional)
   :arg location: Location
   :type location: int array of 2 items in [0, inf], (optional)

.. function:: select_more()

   Select keys linked to boundary selected keys of each particle

.. function:: select_random(*, ratio=0.5, seed=0, action='SELECT', type='HAIR')

   Select a randomly distributed set of hair or points

   :arg ratio: Ratio, Portion of items to select randomly
   :type ratio: float in [0, 1], (optional)
   :arg seed: Random Seed, Seed for the random number generator
   :type seed: int in [0, inf], (optional)
   :arg action: Action, Selection action to execute

      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
   :type action: enum in [``'SELECT'``, ``'DESELECT'``], (optional)
   :arg type: Type, Select either hair or points
   :type type: enum in [``'HAIR'``, ``'POINTS'``], (optional)

.. function:: select_roots(*, action='SELECT')

   Select roots of all visible particles

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: select_tips(*, action='SELECT')

   Select tips of all visible particles

   :arg action: Action, Selection action to execute

      * ``TOGGLE``
        Toggle -- Toggle selection for all elements.
      * ``SELECT``
        Select -- Select all elements.
      * ``DESELECT``
        Deselect -- Deselect all elements.
      * ``INVERT``
        Invert -- Invert selection of all elements.
   :type action: enum in [``'TOGGLE'``, ``'SELECT'``, ``'DESELECT'``, ``'INVERT'``], (optional)

.. function:: shape_cut()

   Cut hair to conform to the set shape object

.. function:: subdivide()

   Subdivide selected particles segments (adds keys)

.. function:: target_move_down()

   Move particle target down in the list

.. function:: target_move_up()

   Move particle target up in the list

.. function:: target_remove()

   Remove the selected particle target

.. function:: unify_length()

   Make selected hair the same length

.. function:: weight_set(*, factor=1.0)

   Set the weight of selected keys

   :arg factor: Factor, Interpolation factor between current brush weight, and keys' weights
   :type factor: float in [0, 1], (optional)

