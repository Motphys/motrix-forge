Depsgraph(bpy_struct)
=====================

.. currentmodule:: bpy.types


Dependency graph: Evaluated ID example
++++++++++++++++++++++++++++++++++++++

This example demonstrates access to the evaluated ID (such as object, material, etc.) state from
an original ID.
This is needed every time one needs to access state with animation, constraints, and modifiers
taken into account.

.. literalinclude:: ..\examples\bpy.types.Depsgraph.1.py
   :lines: 10-


Dependency graph: Original object example
+++++++++++++++++++++++++++++++++++++++++

This example demonstrates access to the original ID.
Such access is needed to check whether object is selected, or to compare pointers.

.. literalinclude:: ..\examples\bpy.types.Depsgraph.2.py
   :lines: 8-


Dependency graph: Iterate over all object instances
+++++++++++++++++++++++++++++++++++++++++++++++++++

Sometimes it is needed to know all the instances with their matrices (for example, when writing an
exporter or a custom render engine).
This example shows how to access all objects and instances in the scene.

.. literalinclude:: ..\examples\bpy.types.Depsgraph.3.py
   :lines: 9-


Dependency graph: Object.to_mesh()
+++++++++++++++++++++++++++++++++++

Function to get a mesh from any object with geometry. It is typically used by exporters, render
engines and tools that need to access the evaluated mesh as displayed in the viewport.

Object.to_mesh() is closely interacting with dependency graph: its behavior depends on whether it
is used on original or evaluated object.

When is used on original object, the result mesh is calculated from the object without taking
animation or modifiers into account:

- For meshes this is similar to duplicating the source mesh.
- For curves this disables own modifiers, and modifiers of objects used as bevel and taper.
- For meta-balls this produces an empty mesh since polygonization is done as a modifier evaluation.

When is used on evaluated object all modifiers are taken into account.

.. note:: The result mesh is owned by the object. It can be freed by calling :meth:`~Object.to_mesh_clear`.
.. note::
   The result mesh must be treated as temporary, and cannot be referenced from objects in the main
   database. If the mesh intended to be used in a persistent manner use :meth:`~BlendDataMeshes.new_from_object`
   instead.
.. note:: If object does not have geometry (i.e. camera) the functions returns None.

.. literalinclude:: ..\examples\bpy.types.Depsgraph.4.py
   :lines: 27-


Dependency graph: bpy.data.meshes.new_from_object()
+++++++++++++++++++++++++++++++++++++++++++++++++++

Function to copy a new mesh from any object with geometry. The mesh is added to the main
database and can be referenced by objects. Typically used by tools that create new objects
or apply modifiers.

When is used on original object, the result mesh is calculated from the object without taking
animation or modifiers into account:

- For meshes this is similar to duplicating the source mesh.
- For curves this disables own modifiers, and modifiers of objects used as bevel and taper.
- For meta-balls this produces an empty mesh since polygonization is done as a modifier evaluation.

When is used on evaluated object all modifiers are taken into account.

All the references (such as materials) are re-mapped to original. This ensures validity and
consistency of the main database.

.. note:: If object does not have geometry (i.e. camera) the functions returns None.

.. literalinclude:: ..\examples\bpy.types.Depsgraph.5.py
   :lines: 23-


Dependency graph: Simple exporter
+++++++++++++++++++++++++++++++++

This example is a combination of all previous ones, and shows how to write a simple exporter
script.

.. literalinclude:: ..\examples\bpy.types.Depsgraph.6.py
   :lines: 8-


Dependency graph: Object.to_curve()
+++++++++++++++++++++++++++++++++++

Function to get a curve from text and curve objects. It is typically used by exporters, render
engines, and tools that need to access the curve representing the object.

The function takes the evaluated dependency graph as a required parameter and optionally a boolean
apply_modifiers which defaults to false. If apply_modifiers is true and the object is a curve object,
the spline deform modifiers are applied on the control points. Note that constructive modifiers and
modifiers that are not spline-enabled will not be applied. So modifiers like Array will not be applied
and deform modifiers that have Apply On Spline disabled will not be applied.

If the object is a text object. The text will be converted into a 3D curve and returned. Modifiers are
never applied on text objects and apply_modifiers will be ignored. If the object is neither a curve nor
a text object, an error will be reported.

.. note:: The resulting curve is owned by the object. It can be freed by calling :meth:`~Object.to_curve_clear`.
.. note::
   The resulting curve must be treated as temporary, and cannot be referenced from objects in the main
   database.

.. literalinclude:: ..\examples\bpy.types.Depsgraph.7.py
   :lines: 23-

base class --- :class:`bpy_struct`

.. class:: Depsgraph(bpy_struct)


   .. data:: ids

      All evaluated data-blocks

      :type: :class:`bpy_prop_collection` of :class:`ID`, (readonly)

   .. data:: mode

      Evaluation mode

      * ``VIEWPORT``
        Viewport -- Viewport non-rendered mode.
      * ``RENDER``
        Render -- Render.

      :type: enum in [``'VIEWPORT'``, ``'RENDER'``], default ``'VIEWPORT'``, (readonly)

   .. data:: object_instances

      All object instances to display or render (Warning: Only use this as an iterator, never as a sequence, and do not keep any references to its items)

      :type: :class:`bpy_prop_collection` of :class:`DepsgraphObjectInstance`, (readonly)

   .. data:: objects

      Evaluated objects in the dependency graph

      :type: :class:`bpy_prop_collection` of :class:`Object`, (readonly)

   .. data:: scene

      Original scene dependency graph is built for

      :type: :class:`Scene`, (readonly)

   .. data:: scene_eval

      Scene at its evaluated state

      :type: :class:`Scene`, (readonly)

   .. data:: updates

      Updates to data-blocks

      :type: :class:`bpy_prop_collection` of :class:`DepsgraphUpdate`, (readonly)

   .. data:: view_layer

      Original view layer dependency graph is built for

      :type: :class:`ViewLayer`, (readonly)

   .. data:: view_layer_eval

      View layer at its evaluated state

      :type: :class:`ViewLayer`, (readonly)

   .. method:: debug_relations_graphviz(*, filepath="")

      debug_relations_graphviz

      :arg filepath: File Name, Optional output path for the graphviz debug file
      :type filepath: string, (optional, never None)
      :return: Dot Graph, Graph in dot format
      :rtype: string

   .. method:: debug_stats_gnuplot(filepath, output_filepath)

      debug_stats_gnuplot

      :arg filepath: File Name, Output path for the gnuplot debug file
      :type filepath: string, (never None)
      :arg output_filepath: Output File Name, File name where gnuplot script will save the result
      :type output_filepath: string, (never None)

   .. method:: debug_tag_update()

      debug_tag_update


   .. method:: debug_stats()

      Report the number of elements in the Dependency Graph

      :return: result
      :rtype: string, (never None)

   .. method:: update()

      Re-evaluate any modified data-blocks, for example for animation or modifiers. This invalidates all references to evaluated data-blocks from this dependency graph.


   .. method:: id_eval_get(id)

      id_eval_get

      :arg id: Original ID to get evaluated complementary part for
      :type id: :class:`ID`
      :return: Evaluated ID for the given original one
      :rtype: :class:`ID`

   .. method:: id_type_updated(id_type)

      id_type_updated

      :arg id_type: ID Type
      :type id_type: enum in :ref:`rna_enum_id_type_items`
      :return: Updated, True if any datablock with this type was added, updated or removed
      :rtype: boolean

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

   * :class:`BlendDataMeshes.new_from_object`
   * :class:`Context.evaluated_depsgraph_get`
   * :class:`ID.evaluated_get`
   * :class:`Object.calc_matrix_camera`
   * :class:`Object.camera_fit_coords`
   * :class:`Object.closest_point_on_mesh`
   * :class:`Object.crazyspace_eval`
   * :class:`Object.ray_cast`
   * :class:`Object.to_curve`
   * :class:`Object.to_mesh`
   * :class:`RenderEngine.bake`
   * :class:`RenderEngine.draw`
   * :class:`RenderEngine.render`
   * :class:`RenderEngine.update`
   * :class:`RenderEngine.view_draw`
   * :class:`RenderEngine.view_update`
   * :class:`Scene.ray_cast`
   * :class:`ShaderNodeTexPointDensity.cache_point_density`
   * :class:`ShaderNodeTexPointDensity.calc_point_density`
   * :class:`ShaderNodeTexPointDensity.calc_point_density_minmax`
   * :class:`ViewLayer.depsgraph`

