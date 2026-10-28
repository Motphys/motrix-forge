Uilist Operators
================

.. module:: bpy.ops.uilist

.. function:: entry_add(*, list_path="", active_index_path="")

   Add an entry to the list after the current active item

   :arg list_path: list_path
   :type list_path: string, (optional, never None)
   :arg active_index_path: active_index_path
   :type active_index_path: string, (optional, never None)
   :File: `startup\bl_ui\generic_ui_list.py\:210 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_ui\generic_ui_list.py#L210>`__


.. function:: entry_move(*, list_path="", active_index_path="", direction='UP')

   Move an entry in the list up or down

   :arg list_path: list_path
   :type list_path: string, (optional, never None)
   :arg active_index_path: active_index_path
   :type active_index_path: string, (optional, never None)
   :arg direction: Direction

      * ``UP``
        UP -- UP.
      * ``DOWN``
        DOWN -- DOWN.
   :type direction: enum in [``'UP'``, ``'DOWN'``], (optional)
   :File: `startup\bl_ui\generic_ui_list.py\:238 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_ui\generic_ui_list.py#L238>`__


.. function:: entry_remove(*, list_path="", active_index_path="")

   Remove the selected entry from the list

   :arg list_path: list_path
   :type list_path: string, (optional, never None)
   :arg active_index_path: active_index_path
   :type active_index_path: string, (optional, never None)
   :File: `startup\bl_ui\generic_ui_list.py\:193 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_ui\generic_ui_list.py#L193>`__


