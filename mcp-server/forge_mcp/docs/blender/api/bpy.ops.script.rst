Script Operators
================

.. module:: bpy.ops.script

.. function:: execute_preset(*, filepath="", menu_idname="")

   Load a preset

   :arg filepath: filepath
   :type filepath: string, (optional, never None)
   :arg menu_idname: Menu ID Name, ID name of the menu this was called from
   :type menu_idname: string, (optional, never None)
   :File: `startup\bl_operators\presets.py\:285 <https://projects.blender.org/blender/blender/src/branch/main/scripts/startup\bl_operators\presets.py#L285>`__


.. function:: python_file_run(*, filepath="")

   Run Python file

   :arg filepath: Path
   :type filepath: string, (optional, never None)

.. function:: reload()

   Reload scripts

