bpy_prop_collection_idprop
==========================

.. currentmodule:: bpy.types

base classes --- :class:`bpy_prop_collection`

.. class:: bpy_prop_collection_idprop

   built-in class used for user defined collections.

   .. note::

      Note that :class:`bpy.types.bpy_prop_collection_idprop` is not actually available from within Blender,
      it only exists for the purpose of documentation.

   .. method:: add()
   
      This is a function to add a new item to a collection.
   
      :return: A newly created item.
      :rtype: Any


   .. method:: clear()
   
      This is a function to remove all items from a collection.


   .. method:: move(src_index, dst_index)
   
      This is a function to move an item in a collection.
   
      :arg src_index: Source item index.
      :type src_index: int
      :arg dst_index: Destination item index.
      :type dst_index: int


   .. method:: remove(index)
   
      This is a function to remove an item from a collection.
   
      :arg index: Index of the item to be removed.
      :type index: int


