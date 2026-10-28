Modifier(bpy_struct)
====================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`ArmatureModifier`, :class:`ArrayModifier`, :class:`BevelModifier`, :class:`BooleanModifier`, :class:`BuildModifier`, :class:`CastModifier`, :class:`ClothModifier`, :class:`CollisionModifier`, :class:`CorrectiveSmoothModifier`, :class:`CurveModifier`, :class:`DataTransferModifier`, :class:`DecimateModifier`, :class:`DisplaceModifier`, :class:`DynamicPaintModifier`, :class:`EdgeSplitModifier`, :class:`ExplodeModifier`, :class:`FluidModifier`, :class:`GreasePencilArmatureModifier`, :class:`GreasePencilArrayModifier`, :class:`GreasePencilBuildModifier`, :class:`GreasePencilColorModifier`, :class:`GreasePencilDashModifierData`, :class:`GreasePencilEnvelopeModifier`, :class:`GreasePencilHookModifier`, :class:`GreasePencilLatticeModifier`, :class:`GreasePencilLengthModifier`, :class:`GreasePencilLineartModifier`, :class:`GreasePencilMirrorModifier`, :class:`GreasePencilMultiplyModifier`, :class:`GreasePencilNoiseModifier`, :class:`GreasePencilOffsetModifier`, :class:`GreasePencilOpacityModifier`, :class:`GreasePencilOutlineModifier`, :class:`GreasePencilShrinkwrapModifier`, :class:`GreasePencilSimplifyModifier`, :class:`GreasePencilSmoothModifier`, :class:`GreasePencilSubdivModifier`, :class:`GreasePencilTextureModifier`, :class:`GreasePencilThickModifierData`, :class:`GreasePencilTimeModifier`, :class:`GreasePencilTintModifier`, :class:`GreasePencilWeightAngleModifier`, :class:`GreasePencilWeightProximityModifier`, :class:`HookModifier`, :class:`LaplacianDeformModifier`, :class:`LaplacianSmoothModifier`, :class:`LatticeModifier`, :class:`MaskModifier`, :class:`MeshCacheModifier`, :class:`MeshDeformModifier`, :class:`MeshSequenceCacheModifier`, :class:`MeshToVolumeModifier`, :class:`MirrorModifier`, :class:`MultiresModifier`, :class:`NodesModifier`, :class:`NormalEditModifier`, :class:`OceanModifier`, :class:`ParticleInstanceModifier`, :class:`ParticleSystemModifier`, :class:`RemeshModifier`, :class:`ScrewModifier`, :class:`ShrinkwrapModifier`, :class:`SimpleDeformModifier`, :class:`SkinModifier`, :class:`SmoothModifier`, :class:`SoftBodyModifier`, :class:`SolidifyModifier`, :class:`SubsurfModifier`, :class:`SurfaceDeformModifier`, :class:`SurfaceModifier`, :class:`TriangulateModifier`, :class:`UVProjectModifier`, :class:`UVWarpModifier`, :class:`VertexWeightEditModifier`, :class:`VertexWeightMixModifier`, :class:`VertexWeightProximityModifier`, :class:`VolumeDisplaceModifier`, :class:`VolumeToMeshModifier`, :class:`WarpModifier`, :class:`WaveModifier`, :class:`WeightedNormalModifier`, :class:`WeldModifier`, :class:`WireframeModifier`

.. class:: Modifier(bpy_struct)

   Modifier affecting the geometry data of an object

   .. data:: execution_time

      Time in seconds that the modifier took to evaluate. This is only set on evaluated objects. If multiple modifiers run in parallel, execution time is not a reliable metric.

      :type: float in [-inf, inf], default 0.0, (readonly)

   .. attribute:: is_active

      The active modifier in the list

      :type: boolean, default False

   .. data:: is_override_data

      In a local override object, whether this modifier comes from the linked reference object, or is local to the override

      :type: boolean, default False, (readonly)

   .. attribute:: name

      Modifier name

      :type: string, default "", (never None)

   .. data:: persistent_uid

      Uniquely identifies the modifier within the modifier stack that it is part of

      :type: int in [-inf, inf], default 0, (readonly)

   .. attribute:: show_expanded

      Set modifier expanded in the user interface

      :type: boolean, default False

   .. attribute:: show_in_editmode

      Display modifier in Edit mode

      :type: boolean, default False

   .. attribute:: show_on_cage

      Adjust edit cage to modifier result

      :type: boolean, default False

   .. attribute:: show_render

      Use modifier during render

      :type: boolean, default False

   .. attribute:: show_viewport

      Display modifier in viewport

      :type: boolean, default False

   .. data:: type

      :type: enum in :ref:`rna_enum_object_modifier_type_items`, default ``'GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY'``, (readonly)

   .. attribute:: use_apply_on_spline

      Apply this and all preceding deformation modifiers on splines' points rather than on filled curve/surface

      :type: boolean, default False

   .. attribute:: use_pin_to_last

      Keep the modifier at the end of the list

      :type: boolean, default False

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

   * :class:`Object.modifiers`
   * :class:`ObjectModifiers.active`
   * :class:`ObjectModifiers.new`
   * :class:`ObjectModifiers.remove`

