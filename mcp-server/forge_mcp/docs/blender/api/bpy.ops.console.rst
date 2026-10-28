Console Operators
=================

.. module:: bpy.ops.console

.. function:: autocomplete()

   Evaluate the namespace up until the cursor and give a list of options or complete the name if there is only one

   :File: `startup\bl_operators\console.py\:61 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\console.py#L61>`__

.. function:: banner()

   Print a message when the terminal initializes

   :File: `startup\bl_operators\console.py\:104 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\console.py#L104>`__

.. function:: clear(*, scrollback=True, history=False)

   Clear text by type

   :arg scrollback: Scrollback, Clear the scrollback history
   :type scrollback: boolean, (optional)
   :arg history: History, Clear the command history
   :type history: boolean, (optional)

.. function:: clear_line()

   Clear the line and store in history

.. function:: copy(*, delete=False)

   Copy selected text to clipboard

   :arg delete: Delete Selection, Whether to delete the selection after copying
   :type delete: boolean, (optional)

.. function:: copy_as_script()

   Copy the console contents for use in a script

   :File: `startup\bl_operators\console.py\:82 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\console.py#L82>`__

.. function:: delete(*, type='NEXT_CHARACTER')

   Delete text by cursor position

   :arg type: Type, Which part of the text to delete
   :type type: enum in [``'NEXT_CHARACTER'``, ``'PREVIOUS_CHARACTER'``, ``'NEXT_WORD'``, ``'PREVIOUS_WORD'``], (optional)

.. function:: execute(*, interactive=False)

   Execute the current console line as a Python expression

   :arg interactive: interactive
   :type interactive: boolean, (optional)
   :File: `startup\bl_operators\console.py\:38 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\console.py#L38>`__


.. function:: history_append(*, text="", current_character=0, remove_duplicates=False)

   Append history at cursor position

   :arg text: Text, Text to insert at the cursor position
   :type text: string, (optional, never None)
   :arg current_character: Cursor, The index of the cursor
   :type current_character: int in [0, inf], (optional)
   :arg remove_duplicates: Remove Duplicates, Remove duplicate items in the history
   :type remove_duplicates: boolean, (optional)

.. function:: history_cycle(*, reverse=False)

   Cycle through history

   :arg reverse: Reverse, Reverse cycle history
   :type reverse: boolean, (optional)

.. function:: indent()

   Add 4 spaces at line beginning

.. function:: indent_or_autocomplete()

   Indent selected text or autocomplete

.. function:: insert(*, text="")

   Insert text at cursor position

   :arg text: Text, Text to insert at the cursor position
   :type text: string, (optional, never None)

.. function:: language(*, language="")

   Set the current language for this console

   :arg language: Language
   :type language: string, (optional, never None)
   :File: `startup\bl_operators\console.py\:136 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\console.py#L136>`__


.. function:: move(*, type='LINE_BEGIN', select=False)

   Move cursor position

   :arg type: Type, Where to move cursor to
   :type type: enum in [``'LINE_BEGIN'``, ``'LINE_END'``, ``'PREVIOUS_CHARACTER'``, ``'NEXT_CHARACTER'``, ``'PREVIOUS_WORD'``, ``'NEXT_WORD'``], (optional)
   :arg select: Select, Whether to select while moving
   :type select: boolean, (optional)

.. function:: paste(*, selection=False)

   Paste text from clipboard

   :arg selection: Selection, Paste text selected elsewhere rather than copied (X11/Wayland only)
   :type selection: boolean, (optional)

.. function:: scrollback_append(*, text="", type='OUTPUT')

   Append scrollback text by type

   :arg text: Text, Text to insert at the cursor position
   :type text: string, (optional, never None)
   :arg type: Type, Console output type
   :type type: enum in [``'OUTPUT'``, ``'INPUT'``, ``'INFO'``, ``'ERROR'``], (optional)

.. function:: select_all()

   Select all the text

.. function:: select_set()

   Set the console selection

.. function:: select_word()

   Select word at cursor position

.. function:: unindent()

   Delete 4 spaces from line beginning

