.. _bpy.ops.mesh.select_by_attribute:

************
By Attribute
************

.. reference::

   :Mode:      Edit Mode
   :Menu:      :menuselection:`Select --> By Attribute`

Selects vertices, edges, or faces based on the :term:`Active`
:doc:`Attribute </modeling/geometry_nodes/attributes_reference>`.


Usage
=====

.. note::

   - The active attribute must have a boolean :ref:`type <attribute-data-types>`.
   - The active attribute must be on the vertex, edge, or face :ref:`domain <attribute-domains>`.

#. Select the desired attribute from the :ref:`Attribute List <bpy.types.AttributeGroup>`.
#. Execute the *By Attribute* operator.
