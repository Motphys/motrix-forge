ThemeNodeEditor(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: ThemeNodeEditor(bpy_struct)

   Theme settings for the Node Editor

   .. attribute:: attribute_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: closure_zone

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: color_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: converter_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: dash_alpha

      Opacity for the dashed lines in wires

      :type: float in [0, 1], default 0.5

   .. attribute:: distor_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: filter_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: foreach_geometry_element_zone

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: frame_node

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: geometry_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: grid

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: grid_levels

      Number of subdivisions for the dot grid displayed in the background

      :type: int in [0, 3], default 3

   .. attribute:: group_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: group_socket_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: input_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: layout_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: matte_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: node_active

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: node_backdrop

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: node_selected

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: noodle_curving

      Curving of the noodle

      :type: int in [0, 10], default 5

   .. attribute:: output_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: pattern_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: repeat_zone

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: script_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: selected_text

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: shader_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: simulation_zone

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. data:: space

      Settings for space

      :type: :class:`ThemeSpaceGeneric`, (readonly, never None)

   .. data:: space_list

      Settings for space list

      :type: :class:`ThemeSpaceListGeneric`, (readonly, never None)

   .. attribute:: texture_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: vector_node

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: wire

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

   .. attribute:: wire_inner

      :type: :class:`mathutils.Color` of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: wire_select

      :type: float array of 4 items in [0, 1], default (0.0, 0.0, 0.0, 0.0)

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

   * :class:`Theme.node_editor`

