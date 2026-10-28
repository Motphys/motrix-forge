Path Utilities (bpy.path)
=========================

.. module:: bpy.path

This module has a similar scope to os.path, containing utility
functions for dealing with paths in Blender.

.. function:: abspath(path, *, start=None, library=None)

   Returns the absolute path relative to the current blend file
   using the "//" prefix.
   
   :arg start: Relative to this path,
      when not set the current filename is used.
   :type start: str | bytes
   :arg library: The library this path is from. This is only included for
      convenience, when the library is not None its path replaces *start*.
   :type library: :class:`bpy.types.Library`
   :return: The absolute path.
   :rtype: str

.. function:: basename(path)

   Equivalent to ``os.path.basename``, but skips a "//" prefix.
   
   Use for Windows compatibility.
   
   :return: The base name of the given path.
   :rtype: str

.. function:: clean_name(name, *, replace='_')

   Returns a name with characters replaced that
   may cause problems under various circumstances,
   such as writing to a file.
   
   All characters besides A-Z/a-z, 0-9 are replaced with "_"
   or the *replace* argument if defined.
   
   :arg name: The path name.
   :type name: str | bytes
   :arg replace: The replacement for non-valid characters.
   :type replace: str
   :return: The cleaned name.
   :rtype: str

.. function:: display_name(name, *, has_ext=True, title_case=True)

   Creates a display string from name to be used menus and the user interface.
   Intended for use with filenames and module names.
   
   :arg name: The name to be used for displaying the user interface.
   :type name: str
   :arg has_ext: Remove file extension from name.
   :type has_ext: bool
   :arg title_case: Convert lowercase names to title case.
   :type title_case: bool
   :return: The display string.
   :rtype: str

.. function:: display_name_to_filepath(name)

   Performs the reverse of display_name using literal versions of characters
   which aren't supported in a filepath.
   
   :arg name: The display name to convert.
   :type name: str
   :return: The file path.
   :rtype: str

.. function:: display_name_from_filepath(name)

   Returns the path stripped of directory and extension,
   ensured to be utf8 compatible.
   
   :arg name: The file path to convert.
   :type name: str
   :return: The display name.
   :rtype: str

.. function:: ensure_ext(filepath, ext, *, case_sensitive=False)

   Return the path with the extension added if it is not already set.
   
   :arg filepath: The file path.
   :type filepath: str
   :arg ext: The extension to check for, can be a compound extension. Should
             start with a dot, such as ``.blend`` or ``.tar.gz``.
   :type ext: str
   :arg case_sensitive: Check for matching case when comparing extensions.
   :type case_sensitive: bool
   :return: The file path with the given extension.
   :rtype: str

.. function:: is_subdir(path, directory)

   Returns true if *path* in a subdirectory of *directory*.
   Both paths must be absolute.
   
   :arg path: An absolute path.
   :type path: str | bytes
   :return: Whether or not the path is a subdirectory.
   :rtype: bool

.. function:: module_names(path, *, recursive=False, package='')

   Return a list of modules which can be imported from *path*.
   
   :arg path: a directory to scan.
   :type path: str
   :arg recursive: Also return submodule names for packages.
   :type recursive: bool
   :arg package: Optional string, used as the prefix for module names (without the trailing ".").
   :type package: str
   :return: a list of string pairs (module_name, module_file).
   :rtype: list[tuple[str, str]]

.. function:: native_pathsep(path)

   Replace the path separator with the systems native ``os.sep``.
   
   :arg path: The path to replace.
   :type path: str
   :return: The path with system native separators.
   :rtype: str

.. function:: reduce_dirs(dirs)

   Given a sequence of directories, remove duplicates and
   any directories nested in one of the other paths.
   (Useful for recursive path searching).
   
   :arg dirs: Sequence of directory paths.
   :type dirs: Sequence[str]
   :return: A unique list of paths.
   :rtype: list[str]

.. function:: relpath(path, *, start=None)

   Returns the path relative to the current blend file using the "//" prefix.
   
   :arg path: An absolute path.
   :type path: str | bytes
   :arg start: Relative to this path,
      when not set the current filename is used.
   :type start: str | bytes
   :return: The relative path.
   :rtype: str

.. function:: resolve_ncase(path)

   Resolve a case insensitive path on a case sensitive system,
   returning a string with the path if found else return the original path.
   
   :arg path: The path name to resolve.
   :type path: str
   :return: The resolved path.
   :rtype: str

