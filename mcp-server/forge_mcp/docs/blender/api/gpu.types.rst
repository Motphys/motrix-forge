GPU Types (gpu.types)
=====================

.. module:: gpu.types

.. class:: Buffer(format, dimensions, data)

   For Python access to GPU functions requiring a pointer.

   :arg format: Format type to interpret the buffer.
      Possible values are `FLOAT`, `INT`, `UINT`, `UBYTE`, `UINT_24_8` and `10_11_11_REV`.
   :type format: str
   :arg dimensions: Array describing the dimensions.
   :type dimensions: int
   :arg data: Optional data array.
   :type data: Buffer | Sequence[float] | Sequence[int]

   return the buffer as a list


   .. attribute:: dimensions

      Undocumented, consider `contributing <https://developer.blender.org/>`__.




.. class:: GPUBatch(type, buf, elem=None)

   Reusable container for drawable geometry.

   :arg type: The primitive type of geometry to be drawn.
      Possible values are `POINTS`, `LINES`, `TRIS`, `LINE_STRIP`, `LINE_LOOP`, `TRI_STRIP`, `TRI_FAN`, `LINES_ADJ`, `TRIS_ADJ` and `LINE_STRIP_ADJ`.
   :type type: str
   :arg buf: Vertex buffer containing all or some of the attributes required for drawing.
   :type buf: :class:`gpu.types.GPUVertBuf`
   :arg elem: An optional index buffer.
   :type elem: :class:`gpu.types.GPUIndexBuf`

   .. method:: draw(shader=None)
   
      Run the drawing shader with the parameters assigned to the batch.
   
      :arg shader: Shader that performs the drawing operations.
         If ``None`` is passed, the last shader set to this batch will run.
      :type program: :class:`gpu.types.GPUShader`


   .. method:: draw_instanced(program, *, instance_start=0, instance_count=0)
   
      Draw multiple instances of the drawing program with the parameters assigned
      to the batch. In the vertex shader, `gl_InstanceID` will contain the instance
      number being drawn.
   
      :arg program: Program that performs the drawing operations.
      :type program: :class:`gpu.types.GPUShader`
      :arg instance_start: Number of the first instance to draw.
      :type instance_start: int
      :arg instance_count: Number of instances to draw. When not provided or set to 0
         the number of instances will be determined by the number of rows in the first
         vertex buffer.
      :type instance_count: int


   .. method:: draw_range(program, *, elem_start=0, elem_count=0)
   
      Run the drawing program with the parameters assigned to the batch. Only draw the ``elem_count`` elements of the index buffer starting at ``elem_start``.
   
      :arg program: Program that performs the drawing operations.
      :type program: :class:`gpu.types.GPUShader`
      :arg elem_start: First index to draw. When not provided or set to 0 drawing
         will start from the first element of the index buffer.
      :type elem_start: int
      :arg elem_count: Number of elements of the index buffer to draw. When not
         provided or set to 0 all elements from ``elem_start`` to the end of the
         index buffer will be drawn.
      :type elem_count: int


   .. method:: program_set(program)
   
      Assign a shader to this batch that will be used for drawing when not overwritten later.
      Note: This method has to be called in the draw context that the batch will be drawn in.
      This function does not need to be called when you always
      set the shader when calling :meth:`gpu.types.GPUBatch.draw`.
   
      :arg program: The program/shader the batch will use in future draw calls.
      :type program: :class:`gpu.types.GPUShader`


   .. method:: vertbuf_add(buf)
   
      Add another vertex buffer to the Batch.
      It is not possible to add more vertices to the batch using this method.
      Instead it can be used to add more attributes to the existing vertices.
      A good use case would be when you have a separate
      vertex buffer for vertex positions and vertex normals.
      Current a batch can have at most GPU_BATCH_VBO_MAX_LEN vertex buffers.
   
      :arg buf: The vertex buffer that will be added to the batch.
      :type buf: :class:`gpu.types.GPUVertBuf`




.. class:: GPUFrameBuffer(depth_slot=None, color_slots=None)

   This object gives access to framebuffer functionalities.
   When a 'layer' is specified in a argument, a single layer of a 3D or array texture is attached to the frame-buffer.
   For cube map textures, layer is translated into a cube map face.

   :arg depth_slot: GPUTexture to attach or a `dict` containing keywords: 'texture', 'layer' and 'mip'.
   :type depth_slot: :class:`gpu.types.GPUTexture` | dict[] | None
   :arg color_slots: Tuple where each item can be a GPUTexture or a `dict` containing keywords: 'texture', 'layer' and 'mip'.
   :type color_slots: :class:`gpu.types.GPUTexture` | dict[str, int | :class:`gpu.types.GPUTexture`] | Sequence[:class:`gpu.types.GPUTexture` | dict[str, int | :class:`gpu.types.GPUTexture`]] | None

   .. function:: bind()
   
      Context manager to ensure balanced bind calls, even in the case of an error.


   .. method:: clear(color=None, depth=None, stencil=None)
   
      Fill color, depth and stencil textures with specific value.
      Common values: color=(0.0, 0.0, 0.0, 1.0), depth=1.0, stencil=0.
   
      :arg color: Sequence of 3 or 4 floats representing ``(r, g, b, a)``.
      :type color: Sequence[float]
      :arg depth: depth value.
      :type depth: float
      :arg stencil: stencil value.
      :type stencil: int


   .. function:: read_color(x, y, xsize, ysize, channels, slot, format, data=data)
   
      Read a block of pixels from the frame buffer.
   
      :arg x, y: Lower left corner of a rectangular block of pixels.
      :arg xsize, ysize: Dimensions of the pixel rectangle.
      :type x, y, xsize, ysize: int
      :arg channels: Number of components to read.
      :type channels: int
      :arg slot: The framebuffer slot to read data from.
      :type slot: int
      :arg format: The format that describes the content of a single channel.
         Possible values are `FLOAT`, `INT`, `UINT`, `UBYTE`, `UINT_24_8` and `10_11_11_REV`.
      :type format: str
      :arg data: Optional Buffer object to fill with the pixels values.
      :type data: :class:`gpu.types.Buffer`
      :return: The Buffer with the read pixels.
      :rtype: :class:`gpu.types.Buffer`


   .. function:: read_depth(x, y, xsize, ysize, data=data)
   
      Read a pixel depth block from the frame buffer.
   
      :arg x, y: Lower left corner of a rectangular block of pixels.
      :type x, y: int
      :arg xsize, ysize: Dimensions of the pixel rectangle.
      :type xsize, ysize: int
      :arg data: Optional Buffer object to fill with the pixels values.
      :type data: :class:`gpu.types.Buffer`
      :return: The Buffer with the read pixels.
      :rtype: :class:`gpu.types.Buffer`


   .. function:: viewport_get()
   
      Returns position and dimension to current viewport.


   .. function:: viewport_set(x, y, xsize, ysize)
   
      Set the viewport for this framebuffer object.
      Note: The viewport state is not saved upon framebuffer rebind.
   
      :arg x, y: lower left corner of the viewport_set rectangle, in pixels.
      :type x, y: int
      :arg xsize, ysize: width and height of the viewport_set.
      :type xsize, ysize: int


   .. attribute:: is_bound

      Checks if this is the active framebuffer in the context.




.. class:: GPUIndexBuf(type, seq)

   Contains an index buffer.

   :arg type: The primitive type this index buffer is composed of.
      Possible values are [``POINTS``, ``LINES``, ``TRIS``, ``LINES_ADJ``, ``TRIS_ADJ``].
   :type type: str
   :arg seq: Indices this index buffer will contain.
      Whether a 1D or 2D sequence is required depends on the type.
      Optionally the sequence can support the buffer protocol.
   :type seq: Buffer | Sequence[int] | Sequence[Sequence[int]]



.. class:: GPUOffScreen(width, height, *, format='RGBA8')

   This object gives access to off screen buffers.

   :arg width: Horizontal dimension of the buffer.
   :type width: int
   :arg height: Vertical dimension of the buffer.
   :type height: int
   :arg format: Internal data format inside GPU memory for color attachment texture. Possible values are:
      `RGBA8`,
      `RGBA16`,
      `RGBA16F`,
      `RGBA32F`,
   :type format: str

   .. function:: bind()
   
      Context manager to ensure balanced bind calls, even in the case of an error.


   .. method:: draw_view3d(scene, view_layer, view3d, region, view_matrix, projection_matrix, do_color_management=False, draw_background=True)
   
      Draw the 3d viewport in the offscreen object.
   
      :arg scene: Scene to draw.
      :type scene: :class:`bpy.types.Scene`
      :arg view_layer: View layer to draw.
      :type view_layer: :class:`bpy.types.ViewLayer`
      :arg view3d: 3D View to get the drawing settings from.
      :type view3d: :class:`bpy.types.SpaceView3D`
      :arg region: Region of the 3D View (required as temporary draw target).
      :type region: :class:`bpy.types.Region`
      :arg view_matrix: View Matrix (e.g. ``camera.matrix_world.inverted()``).
      :type view_matrix: :class:`mathutils.Matrix`
      :arg projection_matrix: Projection Matrix (e.g. ``camera.calc_matrix_camera(...)``).
      :type projection_matrix: :class:`mathutils.Matrix`
      :arg do_color_management: Color manage the output.
      :type do_color_management: bool
      :arg draw_background: Draw background.
      :type draw_background: bool


   .. method:: free()
   
      Free the offscreen object.
      The framebuffer, texture and render objects will no longer be accessible.


   .. method:: unbind(restore=True)
   
      Unbind the offscreen object.
   
      :arg restore: Restore the OpenGL state, can only be used when the state has been saved before.
      :type restore: bool


   .. attribute:: color_texture

      OpenGL bindcode for the color texture.
      
      :type: int


   .. attribute:: height

      Height of the texture.
      
      :type: int


   .. attribute:: texture_color

      The color texture attached.
      
      :type: :class:`gpu.types.GPUTexture`


   .. attribute:: width

      Width of the texture.
      
      :type: int




.. class:: GPUShader(vertexcode, fragcode, geocode=None, libcode=None, defines=None, name='pyGPUShader')

   Constructor is deprecated and will be removed in Blender 5.0, use :func:`gpu.shader.create_from_info` instead.

   GPUShader combines multiple GLSL shaders into a program used for drawing.
   It must contain at least a vertex and fragment shaders.

   The GLSL ``#version`` directive is automatically included at the top of shaders,
   and set to 330. Some preprocessor directives are automatically added according to
   the Operating System or availability: ``GPU_ATI``, ``GPU_NVIDIA`` and ``GPU_INTEL``.

   The following extensions are enabled by default if supported by the GPU:
   ``GL_ARB_texture_gather``, ``GL_ARB_texture_cube_map_array``
   and ``GL_ARB_shader_draw_parameters``.

   For drawing user interface elements and gizmos, use
   ``fragOutput = blender_srgb_to_framebuffer_space(fragOutput)``
   to transform the output sRGB colors to the frame-buffer color-space.

   :arg vertexcode: Vertex shader code.
   :type vertexcode: str
   :arg fragcode: Fragment shader code.
   :type value: str
   :arg geocode: Geometry shader code.
   :type value: str
   :arg libcode: Code with functions and presets to be shared between shaders.
   :type value: str
   :arg defines: Preprocessor directives.
   :type value: str
   :arg name: Name of shader code, for debugging purposes.
   :type value: str

   .. method:: attr_from_name(name)
   
      Get attribute location by name.
   
      :arg name: The name of the attribute variable whose location is to be queried.
      :type name: str
      :return: The location of an attribute variable.
      :rtype: int


   .. method:: attrs_info_get()
   
      Information about the attributes used in the Shader.
   
      :return: tuples containing information about the attributes in order (name, type)
      :rtype: tuple[tuple[str, str | None], ...]


   .. method:: bind()
   
      Bind the shader object. Required to be able to change uniforms of this shader.


   .. method:: format_calc()
   
      Build a new format based on the attributes of the shader.
   
      :return: vertex attribute format for the shader
      :rtype: :class:`gpu.types.GPUVertFormat`


   .. method:: image(name, texture)
   
      Specify the value of an image variable for the current GPUShader.
   
      :arg name: Name of the image variable to which the texture is to be bound.
      :type name: str
      :arg texture: Texture to attach.
      :type texture: :class:`gpu.types.GPUTexture`


   .. method:: uniform_block(name, ubo)
   
      Specify the value of an uniform buffer object variable for the current GPUShader.
   
      :arg name: name of the uniform variable whose UBO is to be specified.
      :type name: str
      :arg ubo: Uniform Buffer to attach.
      :type texture: :class:`gpu.types.GPUUniformBuf`


   .. method:: uniform_block_from_name(name)
   
      Get uniform block location by name.
   
      :arg name: Name of the uniform block variable whose location is to be queried.
      :type name: str
      :return: The location of the uniform block variable.
      :rtype: int


   .. method:: uniform_bool(name, value)
   
      Specify the value of a uniform variable for the current program object.
   
      :arg name: Name of the uniform variable whose value is to be changed.
      :type name: str
      :arg value: Value that will be used to update the specified uniform variable.
      :type value: bool | Sequence[bool]


   .. method:: uniform_float(name, value)
   
      Specify the value of a uniform variable for the current program object.
   
      :arg name: Name of the uniform variable whose value is to be changed.
      :type name: str
      :arg value: Value that will be used to update the specified uniform variable.
      :type value: float | Sequence[float]


   .. method:: uniform_from_name(name)
   
      Get uniform location by name.
   
      :arg name: Name of the uniform variable whose location is to be queried.
      :type name: str
      :return: Location of the uniform variable.
      :rtype: int


   .. method:: uniform_int(name, seq)
   
      Specify the value of a uniform variable for the current program object.
   
      :arg name: name of the uniform variable whose value is to be changed.
      :type name: str
      :arg seq: Value that will be used to update the specified uniform variable.
      :type seq: Sequence[int]


   .. method:: uniform_sampler(name, texture)
   
      Specify the value of a texture uniform variable for the current GPUShader.
   
      :arg name: name of the uniform variable whose texture is to be specified.
      :type name: str
      :arg texture: Texture to attach.
      :type texture: :class:`gpu.types.GPUTexture`


   .. method:: uniform_vector_float(location, buffer, length, count)
   
      Set the buffer to fill the uniform.
   
      :arg location: Location of the uniform variable to be modified.
      :type location: int
      :arg buffer: The data that should be set. Can support the buffer protocol.
      :type buffer: Sequence[float]
      :arg length: Size of the uniform data type:
   
         - 1: float
         - 2: vec2 or float[2]
         - 3: vec3 or float[3]
         - 4: vec4 or float[4]
         - 9: mat3
         - 16: mat4
      :type length: int
      :arg count: Specifies the number of elements, vector or matrices that are to be modified.
      :type count: int


   .. method:: uniform_vector_int(location, buffer, length, count)
   
      See GPUShader.uniform_vector_float(...) description.


   .. attribute:: name

      The name of the shader object for debugging purposes (read-only).
      
      :type: str


   .. attribute:: program

      The name of the program object for use by the OpenGL API (read-only).
      This is deprecated and will always return -1.
      
      :type: int




.. class:: GPUShaderCreateInfo()

   Stores and describes types and variables that are used in shader sources.

   .. method:: compute_source(source)
   
      compute shader source code written in GLSL.
   
      Example:
   
      .. code-block:: python
   
         """void main() {
            int2 index = int2(gl_GlobalInvocationID.xy);
            vec4 color = vec4(0.0, 0.0, 0.0, 1.0);
            imageStore(img_output, index, color);
         }"""
   
      :arg source: The compute shader source code.
      :type source: str
   
      .. seealso:: `GLSL Cross Compilation <https://developer.blender.org/docs/features/gpu/glsl_cross_compilation/>`__


   .. method:: define(name, value)
   
      Add a preprocessing define directive. In GLSL it would be something like:
   
      .. code-block:: glsl
   
         #define name value
   
      :arg name: Token name.
      :type name: str
      :arg value: Text that replaces token occurrences.
      :type value: str


   .. method:: depth_write(value)
   
      Specify a depth write behavior when modifying gl_FragDepth.
   
      There is a common optimization for GPUs that relies on an early depth
      test to be run before the fragment shader so that the shader evaluation
      can be skipped if the fragment ends up being discarded because it is occluded.
   
      This optimization does not affect the final rendering, and is typically
      possible when the fragment does not change the depth programmatically.
      There are, however a class of operations on the depth in the shader which
      could still be performed while allowing the early depth test to operate.
   
      This function alters the behavior of the optimization to allow those operations
      to be performed.
   
      :arg value: Depth write value. It can be 'UNCHANGED' (default), 'ANY', 'GREATER' or 'LESS'.
         :UNCHANGED: disables depth write in a fragment shader and execution of thefragments can be optimized away.
         :ANY: enables depth write in a fragment shader for any fragments
         :GREATER: enables depth write in a fragment shader for depth values thatare greater than the depth value in the output buffer.
         :LESS: enables depth write in a fragment shader for depth values thatare less than the depth value in the output buffer.
      :type blend: str


   .. method:: fragment_out(slot, type, name, blend='NONE')
   
      Specify a fragment output corresponding to a framebuffer target slot.
   
      :arg slot: The attribute index.
      :type slot: int
      :arg type: One of these types:
   
         - ``FLOAT``
         - ``VEC2``
         - ``VEC3``
         - ``VEC4``
         - ``MAT3``
         - ``MAT4``
         - ``UINT``
         - ``UVEC2``
         - ``UVEC3``
         - ``UVEC4``
         - ``INT``
         - ``IVEC2``
         - ``IVEC3``
         - ``IVEC4``
         - ``BOOL``
   
      :type type: str
      :arg name: Name of the attribute.
      :type name: str
      :arg blend: Dual Source Blending Index. It can be 'NONE', 'SRC_0' or 'SRC_1'.
      :type blend: str


   .. method:: fragment_source(source)
   
      Fragment shader source code written in GLSL.
   
      Example:
   
      .. code-block:: python
   
         "void main {fragColor = vec4(0.0, 0.0, 0.0, 1.0);}"
   
      :arg source: The fragment shader source code.
      :type source: str
   
      .. seealso:: `GLSL Cross Compilation <https://developer.blender.org/docs/features/gpu/glsl_cross_compilation/>`__


   .. method:: image(slot, format, type, name, qualifiers={'NO_RESTRICT'})
   
      Specify an image resource used for arbitrary load and store operations.
   
      :arg slot: The image resource index.
      :type slot: int
      :arg format: The GPUTexture format that is passed to the shader. Possible values are:
   
         - ``RGBA8UI``
         - ``RGBA8I``
         - ``RGBA8``
         - ``RGBA32UI``
         - ``RGBA32I``
         - ``RGBA32F``
         - ``RGBA16UI``
         - ``RGBA16I``
         - ``RGBA16F``
         - ``RGBA16``
         - ``RG8UI``
         - ``RG8I``
         - ``RG8``
         - ``RG32UI``
         - ``RG32I``
         - ``RG32F``
         - ``RG16UI``
         - ``RG16I``
         - ``RG16F``
         - ``RG16``
         - ``R8UI``
         - ``R8I``
         - ``R8``
         - ``R32UI``
         - ``R32I``
         - ``R32F``
         - ``R16UI``
         - ``R16I``
         - ``R16F``
         - ``R16``
         - ``R11F_G11F_B10F``
         - ``DEPTH32F_STENCIL8``
         - ``DEPTH24_STENCIL8``
         - ``SRGB8_A8``
         - ``RGB16F``
         - ``SRGB8_A8_DXT1``
         - ``SRGB8_A8_DXT3``
         - ``SRGB8_A8_DXT5``
         - ``RGBA8_DXT1``
         - ``RGBA8_DXT3``
         - ``RGBA8_DXT5``
         - ``DEPTH_COMPONENT32F``
         - ``DEPTH_COMPONENT24``
         - ``DEPTH_COMPONENT16``
      :type format: str
      :arg type: The data type describing how the image is to be read in the shader. Possible values are:
   
         - ``FLOAT_BUFFER``
         - ``FLOAT_1D``
         - ``FLOAT_1D_ARRAY``
         - ``FLOAT_2D``
         - ``FLOAT_2D_ARRAY``
         - ``FLOAT_3D``
         - ``FLOAT_CUBE``
         - ``FLOAT_CUBE_ARRAY``
         - ``INT_BUFFER``
         - ``INT_1D``
         - ``INT_1D_ARRAY``
         - ``INT_2D``
         - ``INT_2D_ARRAY``
         - ``INT_3D``
         - ``INT_CUBE``
         - ``INT_CUBE_ARRAY``
         - ``UINT_BUFFER``
         - ``UINT_1D``
         - ``UINT_1D_ARRAY``
         - ``UINT_2D``
         - ``UINT_2D_ARRAY``
         - ``UINT_3D``
         - ``UINT_CUBE``
         - ``UINT_CUBE_ARRAY``
         - ``SHADOW_2D``
         - ``SHADOW_2D_ARRAY``
         - ``SHADOW_CUBE``
         - ``SHADOW_CUBE_ARRAY``
         - ``DEPTH_2D``
         - ``DEPTH_2D_ARRAY``
         - ``DEPTH_CUBE``
         - ``DEPTH_CUBE_ARRAY``
   
      :type type: str
      :arg name: The image resource name.
      :type name: str
      :arg qualifiers: Set containing values that describe how the image resource is to be read or written. Possible values are:
         - ``NO_RESTRICT``
         - ``READ``
         - ``WRITE``
      :type qualifiers: set[str]


   .. method:: local_group_size(x, y=1, z=1)
   
      Specify the local group size for compute shaders.
   
      :arg x: The local group size in the x dimension.
      :type x: int
      :arg y: The local group size in the y dimension. Optional. Defaults to 1.
      :type y: int
      :arg z: The local group size in the z dimension. Optional. Defaults to 1.
      :type z: int


   .. method:: push_constant(type, name, size=0)
   
      Specify a global access constant.
   
      :arg type: One of these types:
   
         - ``FLOAT``
         - ``VEC2``
         - ``VEC3``
         - ``VEC4``
         - ``MAT3``
         - ``MAT4``
         - ``UINT``
         - ``UVEC2``
         - ``UVEC3``
         - ``UVEC4``
         - ``INT``
         - ``IVEC2``
         - ``IVEC3``
         - ``IVEC4``
         - ``BOOL``
   
      :type type: str
      :arg name: Name of the constant.
      :type name: str
      :arg size: If not zero, indicates that the constant is an array with the specified size.
      :type size: int


   .. method:: sampler(slot, type, name)
   
      Specify an image texture sampler.
   
      :arg slot: The image texture sampler index.
      :type slot: int
      :arg type: The data type describing the format of each sampler unit. Possible values are:
   
         - ``FLOAT_BUFFER``
         - ``FLOAT_1D``
         - ``FLOAT_1D_ARRAY``
         - ``FLOAT_2D``
         - ``FLOAT_2D_ARRAY``
         - ``FLOAT_3D``
         - ``FLOAT_CUBE``
         - ``FLOAT_CUBE_ARRAY``
         - ``INT_BUFFER``
         - ``INT_1D``
         - ``INT_1D_ARRAY``
         - ``INT_2D``
         - ``INT_2D_ARRAY``
         - ``INT_3D``
         - ``INT_CUBE``
         - ``INT_CUBE_ARRAY``
         - ``UINT_BUFFER``
         - ``UINT_1D``
         - ``UINT_1D_ARRAY``
         - ``UINT_2D``
         - ``UINT_2D_ARRAY``
         - ``UINT_3D``
         - ``UINT_CUBE``
         - ``UINT_CUBE_ARRAY``
         - ``SHADOW_2D``
         - ``SHADOW_2D_ARRAY``
         - ``SHADOW_CUBE``
         - ``SHADOW_CUBE_ARRAY``
         - ``DEPTH_2D``
         - ``DEPTH_2D_ARRAY``
         - ``DEPTH_CUBE``
         - ``DEPTH_CUBE_ARRAY``
   
      :type type: str
      :arg name: The image texture sampler name.
      :type name: str


   .. method:: typedef_source(source)
   
      Source code included before resource declaration. Useful for defining structs used by Uniform Buffers.
   
      Example:
   
      .. code-block:: python
   
         "struct MyType {int foo; float bar;};"
   
      :arg source: The source code defining types.
      :type source: str


   .. method:: uniform_buf(slot, type_name, name)
   
      Specify a uniform variable whose type can be one of those declared in :meth:`gpu.types.GPUShaderCreateInfo.typedef_source`.
   
      :arg slot: The uniform variable index.
      :type slot: int
      :arg type_name: Name of the data type. It can be a struct type defined in the source passed through the :meth:`gpu.types.GPUShaderCreateInfo.typedef_source`.
      :type type_name: str
      :arg name: The uniform variable name.
      :type name: str


   .. method:: vertex_in(slot, type, name)
   
      Add a vertex shader input attribute.
   
      :arg slot: The attribute index.
      :type slot: int
      :arg type: One of these types:
   
         - ``FLOAT``
         - ``VEC2``
         - ``VEC3``
         - ``VEC4``
         - ``MAT3``
         - ``MAT4``
         - ``UINT``
         - ``UVEC2``
         - ``UVEC3``
         - ``UVEC4``
         - ``INT``
         - ``IVEC2``
         - ``IVEC3``
         - ``IVEC4``
         - ``BOOL``
   
      :type type: str
      :arg name: name of the attribute.
      :type name: str


   .. method:: vertex_out(interface)
   
      Add a vertex shader output interface block.
   
      :arg interface: Object describing the block.
      :type interface: :class:`gpu.types.GPUStageInterfaceInfo`


   .. method:: vertex_source(source)
   
      Vertex shader source code written in GLSL.
   
      Example:
   
      .. code-block:: python
   
         "void main {gl_Position = vec4(pos, 1.0);}"
   
      :arg source: The vertex shader source code.
      :type source: str
   
      .. seealso:: `GLSL Cross Compilation <https://developer.blender.org/docs/features/gpu/glsl_cross_compilation/>`__




.. class:: GPUStageInterfaceInfo(name)

   List of varyings between shader stages.

   :arg name: Name of the interface block.
   :type value: str

   .. method:: flat(type, name)
   
      Add an attribute with qualifier of type ``flat`` to the interface block.
   
      :arg type: One of these types:
   
         - ``FLOAT``
         - ``VEC2``
         - ``VEC3``
         - ``VEC4``
         - ``MAT3``
         - ``MAT4``
         - ``UINT``
         - ``UVEC2``
         - ``UVEC3``
         - ``UVEC4``
         - ``INT``
         - ``IVEC2``
         - ``IVEC3``
         - ``IVEC4``
         - ``BOOL``
   
      :type type: str
      :arg name: name of the attribute.
      :type name: str


   .. method:: no_perspective(type, name)
   
      Add an attribute with qualifier of type ``no_perspective`` to the interface block.
   
      :arg type: One of these types:
   
         - ``FLOAT``
         - ``VEC2``
         - ``VEC3``
         - ``VEC4``
         - ``MAT3``
         - ``MAT4``
         - ``UINT``
         - ``UVEC2``
         - ``UVEC3``
         - ``UVEC4``
         - ``INT``
         - ``IVEC2``
         - ``IVEC3``
         - ``IVEC4``
         - ``BOOL``
   
      :type type: str
      :arg name: name of the attribute.
      :type name: str


   .. method:: smooth(type, name)
   
      Add an attribute with qualifier of type *smooth* to the interface block.
   
      :arg type: One of these types:
   
         - ``FLOAT``
         - ``VEC2``
         - ``VEC3``
         - ``VEC4``
         - ``MAT3``
         - ``MAT4``
         - ``UINT``
         - ``UVEC2``
         - ``UVEC3``
         - ``UVEC4``
         - ``INT``
         - ``IVEC2``
         - ``IVEC3``
         - ``IVEC4``
         - ``BOOL``
   
      :type type: str
      :arg name: name of the attribute.
      :type name: str


   .. attribute:: name

      Name of the interface block.
      
      :type: str




.. class:: GPUTexture(size, layers=0, is_cubemap=False, format='RGBA8', data=None)

   This object gives access to off GPU textures.

   :arg size: Dimensions of the texture 1D, 2D, 3D or cubemap.
   :type size: int | Sequence[int]
   :arg layers: Number of layers in texture array or number of cubemaps in cubemap array
   :type layers: int
   :arg is_cubemap: Indicates the creation of a cubemap texture.
   :type is_cubemap: int
   :arg format: Internal data format inside GPU memory. Possible values are:
      `RGBA8UI`,
      `RGBA8I`,
      `RGBA8`,
      `RGBA32UI`,
      `RGBA32I`,
      `RGBA32F`,
      `RGBA16UI`,
      `RGBA16I`,
      `RGBA16F`,
      `RGBA16`,
      `RG8UI`,
      `RG8I`,
      `RG8`,
      `RG32UI`,
      `RG32I`,
      `RG32F`,
      `RG16UI`,
      `RG16I`,
      `RG16F`,
      `RG16`,
      `R8UI`,
      `R8I`,
      `R8`,
      `R32UI`,
      `R32I`,
      `R32F`,
      `R16UI`,
      `R16I`,
      `R16F`,
      `R16`,
      `R11F_G11F_B10F`,
      `DEPTH32F_STENCIL8`,
      `DEPTH24_STENCIL8`,
      `SRGB8_A8`,
      `RGB16F`,
      `SRGB8_A8_DXT1`,
      `SRGB8_A8_DXT3`,
      `SRGB8_A8_DXT5`,
      `RGBA8_DXT1`,
      `RGBA8_DXT3`,
      `RGBA8_DXT5`,
      `DEPTH_COMPONENT32F`,
      `DEPTH_COMPONENT24`,
      `DEPTH_COMPONENT16`,
   :type format: str
   :arg data: Buffer object to fill the texture.
   :type data: :class:`gpu.types.Buffer`

   .. method:: clear(format='FLOAT', value=(0.0, 0.0, 0.0, 1.0))
   
      Fill texture with specific value.
   
      :arg format: The format that describes the content of a single item.
         Possible values are `FLOAT`, `INT`, `UINT`, `UBYTE`, `UINT_24_8` and `10_11_11_REV`.
      :type format: str
      :arg value: Sequence each representing the value to fill. Sizes 1..4 are supported.
      :type value: Sequence[float]


   .. method:: read()
   
      Creates a buffer with the value of all pixels.


   .. attribute:: format

      Format of the texture.
      
      :type: str


   .. attribute:: height

      Height of the texture.
      
      :type: int


   .. attribute:: width

      Width of the texture.
      
      :type: int




.. class:: GPUUniformBuf(data)

   This object gives access to off uniform buffers.

   :arg data: Data to fill the buffer.
   :type data: object exposing buffer interface

   .. method:: update(data)
   
      Update the data of the uniform buffer object.




.. class:: GPUVertBuf(format, len)

   Contains a VBO.

   :arg format: Vertex format.
   :type format: :class:`gpu.types.GPUVertFormat`
   :arg len: Amount of vertices that will fit into this buffer.
   :type len: int

   .. method:: attr_fill(id, data)
   
      Insert data into the buffer for a single attribute.
   
      :arg id: Either the name or the id of the attribute.
      :type id: int | str
      :arg data: Buffer or sequence of data that should be stored in the buffer
      :type data: Buffer | Sequence[float] | Sequence[int] | Sequence[Sequence[float]] | Sequence[Sequence[int]]




.. class:: GPUVertFormat()

   This object contains information about the structure of a vertex buffer.

   .. method:: attr_add(id, comp_type, len, fetch_mode)
   
      Add a new attribute to the format.
   
      :arg id: Name the attribute. Often `position`, `normal`, ...
      :type id: str
      :arg comp_type: The data type that will be used store the value in memory.
         Possible values are `I8`, `U8`, `I16`, `U16`, `I32`, `U32`, `F32` and `I10`.
      :type comp_type: str
      :arg len: How many individual values the attribute consists of
         (e.g. 2 for uv coordinates).
      :type len: int
      :arg fetch_mode: How values from memory will be converted when used in the shader.
         This is mainly useful for memory optimizations when you want to store values with
         reduced precision. E.g. you can store a float in only 1 byte but it will be
         converted to a normal 4 byte float when used.
         Possible values are `FLOAT`, `INT`, `INT_TO_FLOAT_UNIT` and `INT_TO_FLOAT`.
      :type fetch_mode: str




