Cycles Operators
================

.. module:: bpy.ops.cycles

.. function:: denoise_animation(*, input_filepath="", output_filepath="")

   Denoise rendered animation sequence using current scene and view layer settings. Requires denoising data passes and output to OpenEXR multilayer files

   :arg input_filepath: Input Filepath, File path for image to denoise. If not specified, uses the render file path and frame range from the scene
   :type input_filepath: string, (optional, never None)
   :arg output_filepath: Output Filepath, If not specified, renders will be denoised in-place
   :type output_filepath: string, (optional, never None)
   :File: `addons_core\cycles\operators.py\:54 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\cycles\operators.py#L54>`__


.. function:: merge_images(*, input_filepath1="", input_filepath2="", output_filepath="")

   Combine OpenEXR multi-layer images rendered with different sample ranges into one image with reduced noise

   :arg input_filepath1: Input Filepath, File path for image to merge
   :type input_filepath1: string, (optional, never None)
   :arg input_filepath2: Input Filepath, File path for image to merge
   :type input_filepath2: string, (optional, never None)
   :arg output_filepath: Output Filepath, File path for merged image
   :type output_filepath: string, (optional, never None)
   :File: `addons_core\cycles\operators.py\:142 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\cycles\operators.py#L142>`__


.. function:: use_shading_nodes()

   Enable nodes on a material, world or light

   :File: `addons_core\cycles\operators.py\:24 <https://projects.blender.org/blender/blender/src/branch/main/scripts/addons_core\cycles\operators.py#L24>`__

