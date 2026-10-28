Workspace Operators
===================

.. module:: bpy.ops.workspace

.. function:: add()

   Add a new workspace by duplicating the current one or appending one from the user configuration

.. function:: append_activate(*, idname="", filepath="")

   Append a workspace and make it the active one in the current window

   :arg idname: Identifier, Name of the workspace to append and activate
   :type idname: string, (optional, never None)
   :arg filepath: Filepath, Path to the library
   :type filepath: string, (optional, never None, blend relative ``//`` prefix supported)

.. function:: delete()

   Delete the active workspace

.. function:: duplicate()

   Add a new workspace

.. function:: reorder_to_back()

   Reorder workspace to be last in the list

.. function:: reorder_to_front()

   Reorder workspace to be first in the list

.. function:: scene_pin_toggle()

   Remember the last used scene for the current workspace and switch to it whenever this workspace is activated again

