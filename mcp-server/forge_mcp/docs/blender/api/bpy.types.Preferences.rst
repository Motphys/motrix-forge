Preferences(bpy_struct)
=======================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Preferences(bpy_struct)

   Global preferences

   .. attribute:: active_section

      Preferences

      :type: enum in :ref:`rna_enum_preference_section_items`, default ``'INTERFACE'``

   .. data:: addons

      :type: :class:`Addons` :class:`bpy_prop_collection` of :class:`Addon`, (readonly)

   .. attribute:: app_template

      :type: string, default "", (never None)

   .. data:: apps

      Preferences that work only for apps

      :type: :class:`PreferencesApps`, (readonly, never None)

   .. data:: autoexec_paths

      :type: :class:`PathCompareCollection` :class:`bpy_prop_collection` of :class:`PathCompare`, (readonly)

   .. data:: edit

      Settings for interacting with Blender data

      :type: :class:`PreferencesEdit`, (readonly, never None)

   .. data:: experimental

      Settings for features that are still early in their development stage

      :type: :class:`PreferencesExperimental`, (readonly, never None)

   .. data:: extensions

      Settings for extensions

      :type: :class:`PreferencesExtensions`, (readonly, never None)

   .. data:: filepaths

      Default paths for external files

      :type: :class:`PreferencesFilePaths`, (readonly, never None)

   .. data:: inputs

      Settings for input devices

      :type: :class:`PreferencesInput`, (readonly, never None)

   .. attribute:: is_dirty

      Preferences have changed

      :type: boolean, default False

   .. data:: keymap

      Shortcut setup for keyboards and other input devices

      :type: :class:`PreferencesKeymap`, (readonly, never None)

   .. data:: studio_lights

      :type: :class:`StudioLights` :class:`bpy_prop_collection` of :class:`StudioLight`, (readonly)

   .. data:: system

      Graphics driver and operating system settings

      :type: :class:`PreferencesSystem`, (readonly, never None)

   .. data:: themes

      :type: :class:`bpy_prop_collection` of :class:`Theme`, (readonly)

   .. data:: ui_styles

      :type: :class:`bpy_prop_collection` of :class:`ThemeStyle`, (readonly)

   .. attribute:: use_preferences_save

      Save preferences on exit when modified (unless factory settings have been loaded)

      :type: boolean, default True

   .. attribute:: use_recent_searches

      Sort the recently searched items at the top

      :type: boolean, default True

   .. data:: version

      Version of Blender the userpref.blend was saved with

      :type: int array of 3 items in [0, inf], default (0, 0, 0), (readonly)

   .. data:: view

      Preferences related to viewing data

      :type: :class:`PreferencesView`, (readonly, never None)

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

   * :class:`Context.preferences`

