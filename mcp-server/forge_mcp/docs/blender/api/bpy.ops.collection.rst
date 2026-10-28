Collection Operators
====================

.. module:: bpy.ops.collection

.. function:: create(*, name="Collection")

   Create an object collection from selected objects

   :arg name: Name, Name of the new collection
   :type name: string, (optional, never None)

.. function:: export_all()

   Invoke all configured exporters on this collection

.. function:: exporter_add(*, name="")

   Add Exporter

   :arg name: Name, FileHandler idname
   :type name: string, (optional, never None)

.. function:: exporter_export(*, index=0)

   Invoke the export operation

   :arg index: Index, Exporter index
   :type index: int in [0, inf], (optional)

.. function:: exporter_remove(*, index=0)

   Remove Exporter

   :arg index: Index, Exporter index
   :type index: int in [0, inf], (optional)

.. function:: objects_add_active(*, collection='')

   Add selected objects to one of the collections the active-object is part of. Optionally add to "All Collections" to ensure selected objects are included in the same collections as the active object

   :arg collection: Collection, The collection to add other selected objects to
   :type collection: enum in [], (optional)

.. function:: objects_remove(*, collection='')

   Remove selected objects from a collection

   :arg collection: Collection, The collection to remove this object from
   :type collection: enum in [], (optional)

.. function:: objects_remove_active(*, collection='')

   Remove the object from an object collection that contains the active object

   :arg collection: Collection, The collection to remove other selected objects from
   :type collection: enum in [], (optional)

.. function:: objects_remove_all()

   Remove selected objects from all collections

