BoneCollections(bpy_struct)
===========================

.. currentmodule:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BoneCollections(bpy_struct)

   The Bone Collections of this Armature

   .. attribute:: active

      Armature's active bone collection

      :type: :class:`BoneCollection`

   .. attribute:: active_index

      The index of the Armature's active bone collection; -1 when there is no active collection. Note that this is indexing the underlying array of bone collections, which may not be in the order you expect. Root collections are listed first, and siblings are always sequential. Apart from that, bone collections can be in any order, and thus incrementing or decrementing this index can make the active bone collection jump around in unexpected ways. For a more predictable interface, use ``active`` or ``active_name``.

      :type: int in [-inf, inf], default 0

   .. attribute:: active_name

      The name of the Armature's active bone collection; empty when there is no active collection

      :type: string, default "", (never None)

   .. data:: is_solo_active

      Read-only flag that indicates there is at least one bone collection marked as 'solo'

      :type: boolean, default False, (readonly)

   .. method:: new(name, *, parent=None)

      Add a new empty bone collection to the armature

      :arg name: Name, Name of the new collection. Blender will ensure it is unique within the collections of the Armature.
      :type name: string, (never None)
      :arg parent: Parent Collection, If not None, the new bone collection becomes a child of this collection
      :type parent: :class:`BoneCollection`, (optional)
      :return: Newly created bone collection
      :rtype: :class:`BoneCollection`

   .. method:: remove(bone_collection)

      Remove the bone collection from the armature. If this bone collection has any children, they will be reassigned to their grandparent; in other words, the children will take the place of the removed bone collection.

      :arg bone_collection: Bone Collection, The bone collection to remove
      :type bone_collection: :class:`BoneCollection`

   .. method:: move(from_index, to_index)

      Move a bone collection to a different position in the collection list. This can only be used to reorder siblings, and not to change parent-child relationships.

      :arg from_index: From Index, Index to move
      :type from_index: int in [-inf, inf]
      :arg to_index: To Index, Target index
      :type to_index: int in [-inf, inf]

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

   * :class:`Armature.collections`

