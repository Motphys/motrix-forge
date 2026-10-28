Scene Operators
===============

.. module:: bpy.ops.scene

.. function:: delete()

   Delete active scene

.. function:: freestyle_add_edge_marks_to_keying_set()

   Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set

   :File: `startup\bl_operators\freestyle.py\:136 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\freestyle.py#L136>`__

.. function:: freestyle_add_face_marks_to_keying_set()

   Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set

   :File: `startup\bl_operators\freestyle.py\:167 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\freestyle.py#L167>`__

.. function:: freestyle_alpha_modifier_add(*, type='ALONG_STROKE')

   Add an alpha transparency modifier to the line style associated with the active lineset

   :arg type: Type
   :type type: enum in :ref:`rna_enum_linestyle_alpha_modifier_type_items`, (optional)

.. function:: freestyle_color_modifier_add(*, type='ALONG_STROKE')

   Add a line color modifier to the line style associated with the active lineset

   :arg type: Type
   :type type: enum in :ref:`rna_enum_linestyle_color_modifier_type_items`, (optional)

.. function:: freestyle_fill_range_by_selection(*, type='COLOR', name="")

   Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object (either a user-specified object or the active camera)

   :arg type: Type, Type of the modifier to work on

      * ``COLOR``
        Color -- Color modifier type.
      * ``ALPHA``
        Alpha -- Alpha modifier type.
      * ``THICKNESS``
        Thickness -- Thickness modifier type.
   :type type: enum in [``'COLOR'``, ``'ALPHA'``, ``'THICKNESS'``], (optional)
   :arg name: Name, Name of the modifier to work on
   :type name: string, (optional, never None)
   :File: `startup\bl_operators\freestyle.py\:42 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\freestyle.py#L42>`__


.. function:: freestyle_geometry_modifier_add(*, type='2D_OFFSET')

   Add a stroke geometry modifier to the line style associated with the active lineset

   :arg type: Type
   :type type: enum in :ref:`rna_enum_linestyle_geometry_modifier_type_items`, (optional)

.. function:: freestyle_lineset_add()

   Add a line set into the list of line sets

.. function:: freestyle_lineset_copy()

   Copy the active line set to the internal clipboard

.. function:: freestyle_lineset_move(*, direction='UP')

   Change the position of the active line set within the list of line sets

   :arg direction: Direction, Direction to move the active line set towards
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: freestyle_lineset_paste()

   Paste the internal clipboard content to the active line set

.. function:: freestyle_lineset_remove()

   Remove the active line set from the list of line sets

.. function:: freestyle_linestyle_new()

   Create a new line style, reusable by multiple line sets

.. function:: freestyle_modifier_copy()

   Duplicate the modifier within the list of modifiers

.. function:: freestyle_modifier_move(*, direction='UP')

   Move the modifier within the list of modifiers

   :arg direction: Direction, Direction to move the chosen modifier towards
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: freestyle_modifier_remove()

   Remove the modifier from the list of modifiers

.. function:: freestyle_module_add()

   Add a style module into the list of modules

.. function:: freestyle_module_move(*, direction='UP')

   Change the position of the style module within in the list of style modules

   :arg direction: Direction, Direction to move the chosen style module towards
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)

.. function:: freestyle_module_open(*, filepath="", make_internal=True)

   Open a style module file

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg make_internal: Make internal, Make module file internal after loading
   :type make_internal: boolean, (optional)
   :File: `startup\bl_operators\freestyle.py\:212 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\freestyle.py#L212>`__


.. function:: freestyle_module_remove()

   Remove the style module from the stack

.. function:: freestyle_stroke_material_create()

   Create Freestyle stroke material for testing

.. function:: freestyle_thickness_modifier_add(*, type='ALONG_STROKE')

   Add a line thickness modifier to the line style associated with the active lineset

   :arg type: Type
   :type type: enum in :ref:`rna_enum_linestyle_thickness_modifier_type_items`, (optional)

.. function:: gltf2_action_filter_refresh()

   Refresh list of actions

   :File: `addons_core\io_scene_gltf2\blender\com\gltf2_blender_ui.py\:624 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\io_scene_gltf2\blender\com\gltf2_blender_ui.py#L624>`__

.. function:: gpencil_brush_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove grease pencil brush preset

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :File: `startup\bl_operators\presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L119>`__


.. function:: gpencil_material_preset_add(*, name="", remove_name=False, remove_active=False)

   Add or remove Grease Pencil material preset

   :arg name: Name, Name of the preset, used to make the path name
   :type name: string, (optional, never None)
   :arg remove_name: remove_name
   :type remove_name: boolean, (optional)
   :arg remove_active: remove_active
   :type remove_active: boolean, (optional)
   :File: `startup\bl_operators\presets.py\:119 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L119>`__


.. function:: new(*, type='NEW')

   Add new scene by type

   :arg type: Type

      * ``NEW``
        New -- Add a new, empty scene with default settings.
      * ``EMPTY``
        Copy Settings -- Add a new, empty scene, and copy settings from the current scene.
      * ``LINK_COPY``
        Linked Copy -- Link in the collections from the current scene (shallow copy).
      * ``FULL_COPY``
        Full Copy -- Make a full copy of the current scene.
   :type type: enum in [``'NEW'``, ``'EMPTY'``, ``'LINK_COPY'``, ``'FULL_COPY'``], (optional)

.. function:: new_sequencer(*, type='NEW')

   Add new scene by type in the sequence editor and assign to active strip

   :arg type: Type

      * ``NEW``
        New -- Add a new, empty scene with default settings.
      * ``EMPTY``
        Copy Settings -- Add a new, empty scene, and copy settings from the current scene.
      * ``LINK_COPY``
        Linked Copy -- Link in the collections from the current scene (shallow copy).
      * ``FULL_COPY``
        Full Copy -- Make a full copy of the current scene.
   :type type: enum in [``'NEW'``, ``'EMPTY'``, ``'LINK_COPY'``, ``'FULL_COPY'``], (optional)

.. function:: render_view_add()

   Add a render view

.. function:: render_view_remove()

   Remove the selected render view

.. function:: view_layer_add(*, type='NEW')

   Add a view layer

   :arg type: Type

      * ``NEW``
        New -- Add a new view layer.
      * ``COPY``
        Copy Settings -- Copy settings of current view layer.
      * ``EMPTY``
        Blank -- Add a new view layer with all collections disabled.
   :type type: enum in [``'NEW'``, ``'COPY'``, ``'EMPTY'``], (optional)

.. function:: view_layer_add_aov()

   Add a Shader AOV

.. function:: view_layer_add_lightgroup(*, name="")

   Add a Light Group

   :arg name: Name, Name of newly created lightgroup
   :type name: string, (optional, never None)

.. function:: view_layer_add_used_lightgroups()

   Add all used Light Groups

.. function:: view_layer_remove()

   Remove the selected view layer

.. function:: view_layer_remove_aov()

   Remove Active AOV

.. function:: view_layer_remove_lightgroup()

   Remove Active Lightgroup

.. function:: view_layer_remove_unused_lightgroups()

   Remove all unused Light Groups

