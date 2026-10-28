Text(ID)
========

.. currentmodule:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Text(ID)

   Text data-block referencing an external or packed text file

   .. attribute:: current_character

      Index of current character in current line, and also start index of character in selection if one exists

      :type: int in [0, inf], default 0

   .. data:: current_line

      Current line, and start line of selection if one exists

      :type: :class:`TextLine`, (readonly, never None)

   .. attribute:: current_line_index

      Index of current TextLine in TextLine collection

      :type: int in [-inf, inf], default 0

   .. attribute:: filepath

      Filename of the text file

      :type: string, default "", (never None)

   .. attribute:: indentation

      Use tabs or spaces for indentation

      * ``TABS``
        Tabs -- Indent using tabs.
      * ``SPACES``
        Spaces -- Indent using spaces.

      :type: enum in [``'TABS'``, ``'SPACES'``], default ``'TABS'``

   .. data:: is_dirty

      Text file has been edited since last save

      :type: boolean, default False, (readonly)

   .. data:: is_in_memory

      Text file is in memory, without a corresponding file on disk

      :type: boolean, default False, (readonly)

   .. data:: is_modified

      Text file on disk is different than the one in memory

      :type: boolean, default False, (readonly)

   .. data:: lines

      Lines of text

      :type: :class:`bpy_prop_collection` of :class:`TextLine`, (readonly)

   .. attribute:: select_end_character

      Index of character after end of selection in the selection end line

      :type: int in [0, inf], default 0

   .. data:: select_end_line

      End line of selection

      :type: :class:`TextLine`, (readonly, never None)

   .. attribute:: select_end_line_index

      Index of last TextLine in selection

      :type: int in [-inf, inf], default 0

   .. attribute:: use_module

      Run this text as a Python script on loading

      :type: boolean, default False

   .. method:: clear()

      clear the text block


   .. method:: write(text)

      write text at the cursor location and advance to the end of the text block

      :arg text: New text for this data-block
      :type text: string, (never None)

   .. method:: from_string(text)

      Replace text with this string.

      :type text: string, (never None)

   .. method:: as_string()

      Return the text as a string

      :rtype: string, (never None)

   .. method:: is_syntax_highlight_supported()

      Returns True if the editor supports syntax highlighting for the current text datablock

      :rtype: boolean

   .. method:: select_set(line_start, char_start, line_end, char_end)

      Set selection range by line and character index

      :arg line_start: Start Line
      :type line_start: int in [-inf, inf]
      :arg char_start: Start Character
      :type char_start: int in [-inf, inf]
      :arg line_end: End Line
      :type line_end: int in [-inf, inf]
      :arg char_end: End Character
      :type char_end: int in [-inf, inf]

   .. method:: cursor_set(line, *, character=0, select=False)

      Set cursor by line and (optionally) character index

      :arg line: Line
      :type line: int in [0, inf]
      :arg character: Character
      :type character: int in [0, inf], (optional)
      :arg select: Select when moving the cursor
      :type select: boolean, (optional)

   .. method:: as_module()

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


   .. method:: region_as_string(range=None)
   
      :arg range: The region of text to be returned, defaulting to the selection when no range is passed.
         Each int pair represents a line and column: ((start_line, start_column), (end_line, end_column))
         The values match Python's slicing logic (negative values count backwards from the end, the end value is not inclusive).
      :type range: tuple[tuple[int, int], tuple[int, int]]
      :return: The specified region as a string.
      :rtype: str.


   .. method:: region_from_string(body, range=None)
   
      :arg body: The text to be inserted.
      :type body: str
      :arg range: The region of text to be returned, defaulting to the selection when no range is passed.
         Each int pair represents a line and column: ((start_line, start_column), (end_line, end_column))
         The values match Python's slicing logic (negative values count backwards from the end, the end value is not inclusive).
      :type range: tuple[tuple[int, int], tuple[int, int]]


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

   * :mod:`bpy.context.edit_text`
   * :class:`BlendData.texts`
   * :class:`BlendDataTexts.load`
   * :class:`BlendDataTexts.new`
   * :class:`BlendDataTexts.remove`
   * :class:`Camera.custom_shader`
   * :class:`FreestyleModuleSettings.script`
   * :class:`NodeFrame.text`
   * :class:`ShaderNodeScript.script`
   * :class:`ShaderNodeTexIES.ies`
   * :class:`SpaceTextEditor.text`

