# Copyright (C) 2020-2026 Motphys Technology Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of Motrix Forge.
#
# Motrix Forge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Motrix Forge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Motrix Forge. If not, see <https://www.gnu.org/licenses/>.
# ==============================================================================

"""TCP client for the Blender-side Forge MCP bridge.

The Blender addon (``Forge/mcp``) listens on localhost:9876 and executes
null-byte-delimited JSON requests of the form::

    {"type": "execute", "code": <python>, "strict_json": true, "auth_token": <token>}

Each request must set the ``result`` dict; the response is
``{"status": "ok", "result": {...}}`` (or ``status: "error"``).
"""

from __future__ import annotations

import ast
import json
import os
import socket

from mcp.server.mcpserver.exceptions import ToolError

from .skills import claim_hints, hint_message, require_rule

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 9876
# Long import / export tasks can take a while. Matches the addon-side deferred
# timeout (Forge/mcp/constants.py DEFERRED_TIMEOUT, 30 min) so a deferred
# request is not abandoned client-side while Blender still holds it.
DEFAULT_TIMEOUT = 1800.0  # seconds

RECV_BUFFER_SIZE = 8192

_TrackedPath = tuple[str, ...]
_TrackedPaths = frozenset[_TrackedPath]
_AliasMap = dict[str, _TrackedPaths]

_BPY_PATH: _TrackedPath = ("bpy",)
_BPY_OBJECT_PATH: _TrackedPath = ("bpy", "<object>")
_BPY_OPS_PATH: _TrackedPath = ("bpy", "ops")
_FORGE_OPS_PATH: _TrackedPath = ("bpy", "ops", "forge")
_FORGE_PROPERTY_PATH: _TrackedPath = ("<forge>",)
_DYNAMIC_FORGE_PATH: _TrackedPath = ("<dynamic-forge>",)
_DYNAMIC_BPY_OPS_NAMESPACE_PATH: _TrackedPath = ("<dynamic-bpy-ops-namespace>",)
_DYNAMIC_BPY_OPS_OPERATOR_PATH: _TrackedPath = ("<dynamic-bpy-ops-operator>",)
_STRING_PATH_PREFIX = "<string>"
_MAX_TRACKED_STRING_VALUES = 32

# These names are only needed to disambiguate calls through an unknown
# ``bpy.ops`` namespace. Calls through the explicit ``forge`` namespace remain
# open-ended so newly added Forge operators are still guarded automatically.
_KNOWN_FORGE_OPERATORS = frozenset(
    {
        "add_tendon_target_item",
        "assign_material",
        "batch_rename",
        "coacds",
        "create_actuator",
        "create_attach",
        "create_camera",
        "create_checker_material",
        "create_collider",
        "create_contact",
        "create_equality",
        "create_frame",
        "create_geometry",
        "create_height_field",
        "create_include",
        "create_inertial",
        "create_joint",
        "create_light",
        "create_link",
        "create_material",
        "create_plane",
        "create_replicate",
        "create_sensor",
        "create_site",
        "create_tendon",
        "define_actuator_type",
        "define_collider_type",
        "define_geometry_type",
        "define_joint_type",
        "define_model_type",
        "define_parent",
        "define_site_type",
        "ensure_pip",
        "export_mjcf",
        "export_path",
        "file_path",
        "import_mjcf",
        "mark_instance_link",
        "mark_root_link",
        "mcp_server_start",
        "mcp_server_stop",
        "mesh_check",
        "pip_install",
        "properties_actuator",
        "properties_camera",
        "properties_contact",
        "properties_equality",
        "properties_global",
        "properties_hfield",
        "properties_joint",
        "properties_light",
        "properties_link",
        "properties_plane",
        "properties_replicate",
        "properties_sensor",
        "properties_shape",
        "properties_shape_site",
        "properties_tendon",
        "properties_visual",
        "remove_tendon_target_item",
        "scale_gizmo_size",
        "select_by_model_type",
        "select_by_tag",
        "select_hulls",
        "set_instance_idname",
        "temp_file",
        "temp_include",
        "temp_link",
    }
)


class _ForgeOperatorCallVisitor(ast.NodeVisitor):
    """Find Forge operations while following straightforward bpy aliases."""

    def __init__(self) -> None:
        self.operators: set[str] = set()
        self.modifies_forge_properties = False
        self.requires_all_skills = False
        self._aliases: list[_AliasMap] = [{"bpy": frozenset({_BPY_PATH})}]
        self._scope_kinds: list[str] = ["module"]

    @property
    def aliases(self) -> _AliasMap:
        return self._aliases[-1]

    def _push_scope(self, aliases: _AliasMap, kind: str) -> None:
        self._aliases.append(aliases)
        self._scope_kinds.append(kind)

    def _pop_scope(self) -> None:
        self._aliases.pop()
        self._scope_kinds.pop()

    def _function_parent_aliases(self) -> _AliasMap:
        """Return the nearest enclosing non-class scope for a function body."""
        for aliases, kind in zip(reversed(self._aliases), reversed(self._scope_kinds), strict=True):
            if kind != "class":
                return aliases.copy()
        return {}

    @staticmethod
    def _extend_path(path: _TrackedPath, attribute: str) -> _TrackedPath:
        """Extend a tracked path while keeping the abstract domain finite."""
        if path in {
            _FORGE_PROPERTY_PATH,
            _DYNAMIC_FORGE_PATH,
            _DYNAMIC_BPY_OPS_OPERATOR_PATH,
        }:
            return path
        if attribute.startswith("Forge_"):
            return _FORGE_PROPERTY_PATH
        if path == _DYNAMIC_BPY_OPS_NAMESPACE_PATH:
            return (*_DYNAMIC_BPY_OPS_NAMESPACE_PATH, attribute)
        if len(path) == 2 and path[:1] == _DYNAMIC_BPY_OPS_NAMESPACE_PATH:
            return path
        if path == _BPY_PATH:
            return _BPY_OPS_PATH if attribute == "ops" else _BPY_OBJECT_PATH
        if path == _BPY_OPS_PATH:
            return _FORGE_OPS_PATH if attribute == "forge" else _BPY_OBJECT_PATH
        if path == _FORGE_OPS_PATH:
            return (*_FORGE_OPS_PATH, attribute)
        if len(path) == 4 and path[:3] == _FORGE_OPS_PATH:
            return _DYNAMIC_FORGE_PATH
        if path and path[0] == "bpy":
            return _BPY_OBJECT_PATH
        return path

    def _paths(self, node: ast.AST) -> _TrackedPaths:
        if isinstance(node, ast.Name):
            return self.aliases.get(node.id, frozenset())
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return frozenset({(_STRING_PATH_PREFIX, node.value)})
        if isinstance(node, ast.Attribute):
            parents = frozenset(path for path in self._paths(node.value) if path[:1] != (_STRING_PATH_PREFIX,))
            if parents:
                return frozenset(self._extend_path(parent, node.attr) for parent in parents)
            if node.attr.startswith("Forge_"):
                return frozenset({_FORGE_PROPERTY_PATH})
            return frozenset()
        if isinstance(node, ast.Subscript):
            return frozenset(path for path in self._paths(node.value) if path[:1] != (_STRING_PATH_PREFIX,))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            left = self._string_values(self._paths(node.left))
            right = self._string_values(self._paths(node.right))
            values = {left_value + right_value for left_value in left for right_value in right}
            if len(values) <= _MAX_TRACKED_STRING_VALUES:
                return frozenset((_STRING_PATH_PREFIX, value) for value in values)
            return frozenset()
        if isinstance(node, ast.IfExp):
            return self._paths(node.body) | self._paths(node.orelse)
        if isinstance(node, ast.BoolOp):
            return frozenset(path for value in node.values for path in self._paths(value))
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
            return frozenset(path for element in node.elts for path in self._paths(element))
        if isinstance(node, ast.Dict):
            return frozenset(path for value in node.values for path in self._paths(value))
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "getattr"
            and len(node.args) >= 2
        ):
            parents = self._paths(node.args[0])
            attribute_names = self._string_values(self._paths(node.args[1]))
            if attribute_names:
                resolved_paths: set[_TrackedPath] = set()
                for attribute_name in attribute_names:
                    if attribute_name.startswith("Forge_"):
                        resolved_paths.add(_FORGE_PROPERTY_PATH)
                    else:
                        resolved_paths.update(self._extend_path(parent, attribute_name) for parent in parents)
                return frozenset(resolved_paths)
            dynamic_paths: set[_TrackedPath] = set()
            for parent in parents:
                if parent == _BPY_OPS_PATH:
                    dynamic_paths.add(_DYNAMIC_BPY_OPS_NAMESPACE_PATH)
                elif parent == _DYNAMIC_BPY_OPS_NAMESPACE_PATH:
                    dynamic_paths.add(_DYNAMIC_BPY_OPS_OPERATOR_PATH)
                elif parent in {_FORGE_OPS_PATH, _FORGE_PROPERTY_PATH, _DYNAMIC_FORGE_PATH} or (
                    len(parent) == 4 and parent[:3] == _FORGE_OPS_PATH
                ):
                    dynamic_paths.add(_DYNAMIC_FORGE_PATH)
            return frozenset(dynamic_paths)
        return frozenset()

    @staticmethod
    def _string_values(paths: _TrackedPaths) -> frozenset[str]:
        """Extract the finite string constants represented by tracked paths."""
        return frozenset(path[1] for path in paths if len(path) == 2 and path[0] == _STRING_PATH_PREFIX)

    def _bind(self, name: str, paths: _TrackedPaths) -> None:
        tracked = frozenset(
            path
            for path in paths
            if path
            and path[0]
            in {
                "bpy",
                "<forge>",
                "<dynamic-forge>",
                "<dynamic-bpy-ops-namespace>",
                "<dynamic-bpy-ops-operator>",
                _STRING_PATH_PREFIX,
            }
        )
        if tracked:
            self.aliases[name] = tracked
        else:
            self.aliases.pop(name, None)

    def _bind_target(self, target: ast.AST, paths: _TrackedPaths) -> None:
        if isinstance(target, ast.Name):
            self._bind(target.id, paths)
        elif isinstance(target, ast.Starred):
            self._bind_target(target.value, paths)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for element in target.elts:
                self._bind_target(element, paths)

    def _bind_assignment_target(self, target: ast.AST, value: ast.AST) -> None:
        if (
            isinstance(target, (ast.Tuple, ast.List))
            and isinstance(value, (ast.Tuple, ast.List))
            and len(target.elts) == len(value.elts)
        ):
            for target_element, value_element in zip(target.elts, value.elts, strict=True):
                self._bind_assignment_target(target_element, value_element)
            return
        self._bind_target(target, self._paths(value))

    def _bind_iteration_target(self, target: ast.AST, iterable: ast.AST) -> None:
        if isinstance(iterable, (ast.List, ast.Tuple, ast.Set)):
            values = list(iterable.elts)
        elif isinstance(iterable, ast.Dict):
            values = [key for key in iterable.keys if key is not None]
        else:
            values = [iterable]
        self._bind_target_from_values(target, values)

    def _bind_target_from_values(self, target: ast.AST, values: list[ast.AST]) -> None:
        if isinstance(target, ast.Starred):
            self._bind_target_from_values(target.value, values)
            return
        if isinstance(target, (ast.Tuple, ast.List)):
            for index, target_element in enumerate(target.elts):
                element_values = [
                    value.elts[index]
                    for value in values
                    if isinstance(value, (ast.Tuple, ast.List)) and index < len(value.elts)
                ]
                if element_values:
                    self._bind_target_from_values(target_element, element_values)
                else:
                    paths = frozenset(path for value in values for path in self._paths(value))
                    self._bind_target(target_element, paths)
            return
        paths = frozenset(path for value in values for path in self._paths(value))
        self._bind_target(target, paths)

    @staticmethod
    def _target_names(target: ast.AST) -> set[str]:
        if isinstance(target, ast.Name):
            return {target.id}
        if isinstance(target, ast.Starred):
            return _ForgeOperatorCallVisitor._target_names(target.value)
        if isinstance(target, (ast.Tuple, ast.List)):
            return {name for element in target.elts for name in _ForgeOperatorCallVisitor._target_names(element)}
        return set()

    @staticmethod
    def _merge_aliases(states: list[_AliasMap]) -> _AliasMap:
        """Conservatively retain every tracked binding possible after a branch."""
        merged: dict[str, set[_TrackedPath]] = {}
        for state in states:
            for name, paths in state.items():
                merged.setdefault(name, set()).update(paths)
        return {name: frozenset(paths) for name, paths in merged.items()}

    def _visit_branch(self, statements: list[ast.stmt], initial: _AliasMap) -> _AliasMap:
        self._aliases[-1] = initial.copy()
        for statement in statements:
            self.visit(statement)
        return self.aliases.copy()

    @staticmethod
    def _pattern_names(pattern: ast.pattern) -> set[str]:
        names: set[str] = set()
        for child in ast.walk(pattern):
            if isinstance(child, (ast.MatchAs, ast.MatchStar)) and child.name:
                names.add(child.name)
        return names

    def _is_forge_property_target(self, target: ast.AST) -> bool:
        """Return whether an expression traverses a Forge property group."""
        return any(path in {_FORGE_PROPERTY_PATH, _DYNAMIC_FORGE_PATH} for path in self._paths(target))

    def _record_forge_property_write(self, target: ast.AST) -> None:
        if self._is_forge_property_target(target):
            self.modifies_forge_properties = True

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            path = tuple(alias.name.split("."))
            bound_name = alias.asname or path[0]
            if path[0] != "bpy":
                self._bind(bound_name, frozenset())
                continue
            if alias.asname:
                tracked_path = (
                    path
                    if path in {_BPY_PATH, _BPY_OPS_PATH, _FORGE_OPS_PATH}
                    or (len(path) == 4 and path[:3] == _FORGE_OPS_PATH)
                    else _BPY_OBJECT_PATH
                )
                self._bind(alias.asname, frozenset({tracked_path}))
            else:
                # ``import bpy.ops`` binds the top-level ``bpy`` name.
                self._bind("bpy", frozenset({_BPY_PATH}))

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        module_path = tuple((node.module or "").split("."))
        for alias in node.names:
            if alias.name == "*":
                if not node.level and module_path and module_path[0] == "bpy":
                    self.requires_all_skills = True
                continue
            if not node.level and module_path and module_path[0] == "bpy":
                path = (*module_path, alias.name)
                tracked_path = (
                    path
                    if path in {_BPY_PATH, _BPY_OPS_PATH, _FORGE_OPS_PATH}
                    or (len(path) == 4 and path[:3] == _FORGE_OPS_PATH)
                    else _BPY_OBJECT_PATH
                )
                self._bind(alias.asname or alias.name, frozenset({tracked_path}))
            else:
                self._bind(alias.asname or alias.name, frozenset())

    def visit_Assign(self, node: ast.Assign) -> None:
        self.visit(node.value)
        for target in node.targets:
            self._record_forge_property_write(target)
            self._bind_assignment_target(target, node.value)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        self.visit(node.annotation)
        if node.value is not None:
            self.visit(node.value)
        self._record_forge_property_write(node.target)
        self._bind_target(node.target, self._paths(node.value) if node.value else frozenset())

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        self.visit(node.value)
        self._record_forge_property_write(node.target)
        self._bind_target(node.target, frozenset())

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.visit(node.value)
        self._record_forge_property_write(node.target)
        self._bind_target(node.target, self._paths(node.value))

    def visit_Delete(self, node: ast.Delete) -> None:
        for target in node.targets:
            self._record_forge_property_write(target)
            self.visit(target)

    def visit_Call(self, node: ast.Call) -> None:
        paths = self._paths(node.func)
        for path in paths:
            if len(path) == 4 and path[:3] == ("bpy", "ops", "forge"):
                self.operators.add(path[3])
            elif len(path) == 2 and path[:1] == _DYNAMIC_BPY_OPS_NAMESPACE_PATH:
                operator = path[1]
                if operator in _KNOWN_FORGE_OPERATORS:
                    self.operators.add(operator)
            elif path == _DYNAMIC_FORGE_PATH:
                self.requires_all_skills = True
            elif path == _DYNAMIC_BPY_OPS_OPERATOR_PATH:
                self.requires_all_skills = True
        if isinstance(node.func, ast.Name) and node.func.id in {"exec", "eval"}:
            self.requires_all_skills = True
        if self._is_forge_property_target(node.func):
            # Calls such as ``Forge_GlobalConfig.reset()`` and collection
            # ``clear()``/``add()`` operations may mutate Forge state.
            self.modifies_forge_properties = True
        if isinstance(node.func, ast.Name) and node.func.id in {"setattr", "delattr"} and len(node.args) >= 2:
            attribute_names = self._string_values(self._paths(node.args[1]))
            target_paths = self._paths(node.args[0])
            writes_forge_attribute = any(name.startswith("Forge_") for name in attribute_names)
            dynamically_writes_bpy = not attribute_names and any(
                path == _BPY_OBJECT_PATH or (path and path[0] == "bpy") for path in target_paths
            )
            if self._is_forge_property_target(node.args[0]) or writes_forge_attribute or dynamically_writes_bpy:
                self.modifies_forge_properties = True
        self.generic_visit(node)

    def visit_If(self, node: ast.If) -> None:
        self.visit(node.test)
        initial = self.aliases.copy()
        body = self._visit_branch(node.body, initial)
        orelse = self._visit_branch(node.orelse, initial) if node.orelse else initial
        self._aliases[-1] = self._merge_aliases([body, orelse])

    def _visit_try(self, node: ast.Try | ast.TryStar) -> None:
        initial = self.aliases.copy()
        body = self._visit_branch(node.body, initial)
        success = self._visit_branch(node.orelse, body) if node.orelse else body
        states = [success]
        handler_initial = self._merge_aliases([initial, body])
        for handler in node.handlers:
            self._aliases[-1] = handler_initial.copy()
            if handler.type is not None:
                self.visit(handler.type)
            if handler.name:
                self._bind(handler.name, frozenset())
            states.append(self._visit_branch(handler.body, self.aliases))
        self._aliases[-1] = self._merge_aliases(states)
        for statement in node.finalbody:
            self.visit(statement)

    def visit_Try(self, node: ast.Try) -> None:
        self._visit_try(node)

    def visit_TryStar(self, node: ast.TryStar) -> None:
        self._visit_try(node)

    def visit_Match(self, node: ast.Match) -> None:
        self.visit(node.subject)
        initial = self.aliases.copy()
        states = [initial]
        for case in node.cases:
            self._aliases[-1] = initial.copy()
            for name in self._pattern_names(case.pattern):
                self._bind(name, frozenset())
            if case.guard is not None:
                self.visit(case.guard)
            states.append(self._visit_branch(case.body, self.aliases))
        self._aliases[-1] = self._merge_aliases(states)

    def _visit_loop(self, node: ast.For | ast.AsyncFor) -> None:
        self.visit(node.iter)
        initial = self.aliases.copy()
        after_loop = initial
        while True:
            self._aliases[-1] = after_loop.copy()
            self._bind_iteration_target(node.target, node.iter)
            body = self._visit_branch(node.body, self.aliases)
            merged = self._merge_aliases([initial, after_loop, body])
            if merged == after_loop:
                break
            after_loop = merged
        orelse = self._visit_branch(node.orelse, after_loop) if node.orelse else after_loop
        self._aliases[-1] = self._merge_aliases([after_loop, orelse])

    def visit_For(self, node: ast.For) -> None:
        self._visit_loop(node)

    def visit_AsyncFor(self, node: ast.AsyncFor) -> None:
        self._visit_loop(node)

    def visit_While(self, node: ast.While) -> None:
        initial = self.aliases.copy()
        after_loop = initial
        while True:
            self._aliases[-1] = after_loop.copy()
            self.visit(node.test)
            tested = self.aliases.copy()
            body = self._visit_branch(node.body, tested)
            merged = self._merge_aliases([initial, after_loop, tested, body])
            if merged == after_loop:
                break
            after_loop = merged
        orelse = self._visit_branch(node.orelse, after_loop) if node.orelse else after_loop
        self._aliases[-1] = self._merge_aliases([after_loop, orelse])

    def _default_argument_paths(self, arguments: ast.arguments) -> dict[str, _TrackedPaths]:
        defaults: dict[str, _TrackedPaths] = {}
        positional = [*arguments.posonlyargs, *arguments.args]
        positional_with_defaults = positional[-len(arguments.defaults) :] if arguments.defaults else []
        for argument, expression in zip(positional_with_defaults, arguments.defaults, strict=True):
            self.visit(expression)
            defaults[argument.arg] = self._paths(expression)
        for argument, expression in zip(arguments.kwonlyargs, arguments.kw_defaults, strict=True):
            if expression is not None:
                self.visit(expression)
                defaults[argument.arg] = self._paths(expression)
        return defaults

    def _local_aliases(
        self,
        arguments: ast.arguments,
        defaults: dict[str, _TrackedPaths],
        parent_aliases: _AliasMap,
    ) -> _AliasMap:
        local_aliases = parent_aliases.copy()
        all_arguments = [*arguments.posonlyargs, *arguments.args, *arguments.kwonlyargs]
        if arguments.vararg:
            all_arguments.append(arguments.vararg)
        if arguments.kwarg:
            all_arguments.append(arguments.kwarg)
        for argument in all_arguments:
            local_aliases.pop(argument.arg, None)
        for name, paths in defaults.items():
            tracked = frozenset(
                path
                for path in paths
                if path
                and path[0]
                in {
                    "bpy",
                    "<forge>",
                    "<dynamic-forge>",
                    "<dynamic-bpy-ops-namespace>",
                    "<dynamic-bpy-ops-operator>",
                    _STRING_PATH_PREFIX,
                }
            )
            if tracked:
                local_aliases[name] = tracked
        return local_aliases

    def _visit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        for expression in node.decorator_list:
            self.visit(expression)
        function_arguments = [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]
        if node.args.vararg:
            function_arguments.append(node.args.vararg)
        if node.args.kwarg:
            function_arguments.append(node.args.kwarg)
        for argument in function_arguments:
            if argument.annotation is not None:
                self.visit(argument.annotation)
        if node.returns is not None:
            self.visit(node.returns)
        defaults = self._default_argument_paths(node.args)
        # Defaults and decorators are evaluated before the function name is
        # rebound in the enclosing scope.
        self._bind(node.name, frozenset())
        local_aliases = self._local_aliases(node.args, defaults, self._function_parent_aliases())
        self._push_scope(local_aliases, "function")
        for statement in node.body:
            self.visit(statement)
        self._pop_scope()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._visit_function(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._visit_function(node)

    def visit_Lambda(self, node: ast.Lambda) -> None:
        defaults = self._default_argument_paths(node.args)
        local_aliases = self._local_aliases(node.args, defaults, self._function_parent_aliases())
        self._push_scope(local_aliases, "lambda")
        self.visit(node.body)
        self._pop_scope()

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        for expression in [*node.decorator_list, *node.bases]:
            self.visit(expression)
        for keyword in node.keywords:
            self.visit(keyword.value)
        self._push_scope(self.aliases.copy(), "class")
        for statement in node.body:
            self.visit(statement)
        self._pop_scope()
        self._bind(node.name, frozenset())

    def _visit_comprehension(self, generators: list[ast.comprehension], expressions: list[ast.AST]) -> None:
        first, *remaining = generators
        self.visit(first.iter)

        # The outermost iterable is evaluated in the containing scope, while
        # targets, filters, nested generators, and results use the implicit
        # comprehension scope. Class locals are not closure variables.
        outer_aliases = self.aliases.copy()
        self._push_scope(outer_aliases.copy(), "temporary")
        self._bind_iteration_target(first.target, first.iter)
        first_bindings = {name: self.aliases.get(name, frozenset()) for name in self._target_names(first.target)}
        self._pop_scope()

        self._push_scope(self._function_parent_aliases(), "comprehension")
        for name, paths in first_bindings.items():
            self._bind(name, paths)
        for condition in first.ifs:
            self.visit(condition)
        for generator in remaining:
            self.visit(generator.iter)
            self._bind_iteration_target(generator.target, generator.iter)
            for condition in generator.ifs:
                self.visit(condition)
        for expression in expressions:
            self.visit(expression)
        self._pop_scope()

    def visit_ListComp(self, node: ast.ListComp) -> None:
        self._visit_comprehension(node.generators, [node.elt])

    def visit_SetComp(self, node: ast.SetComp) -> None:
        self._visit_comprehension(node.generators, [node.elt])

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:
        self._visit_comprehension(node.generators, [node.elt])

    def visit_DictComp(self, node: ast.DictComp) -> None:
        self._visit_comprehension(node.generators, [node.key, node.value])

    def _visit_with(self, node: ast.With | ast.AsyncWith) -> None:
        for item in node.items:
            self.visit(item.context_expr)
            if item.optional_vars is not None:
                self._bind_target(item.optional_vars, self._paths(item.context_expr))
        for statement in node.body:
            self.visit(statement)

    def visit_With(self, node: ast.With) -> None:
        self._visit_with(node)

    def visit_AsyncWith(self, node: ast.AsyncWith) -> None:
        self._visit_with(node)


def required_skills_for_code(code: str) -> tuple[str, ...]:
    """Return skills needed by Forge operator calls and property writes.

    Creation operators use the creation guide; every other Forge operator is
    covered by the modification guide. Direct writes through ``Forge_*``
    property groups also require the modification guide. A script may contain
    both kinds of operation, so both requirements are returned in stable order.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        # Blender will return the syntax error without executing any operator.
        return ()
    visitor = _ForgeOperatorCallVisitor()
    visitor.visit(tree)
    operators = visitor.operators
    required: list[str] = []
    if visitor.requires_all_skills or any(operator.startswith("create_") for operator in operators):
        required.append("create")
    if (
        visitor.requires_all_skills
        or visitor.modifies_forge_properties
        or any(not operator.startswith("create_") for operator in operators)
    ):
        required.append("modify")
    return tuple(required)


def call_blender(
    code: str,
    strict_json: bool = True,
    timeout: float | None = None,
    *,
    enforce_skill: bool = True,
) -> dict:
    """Send *code* to the Blender Forge bridge and return the execution result.

    *timeout* defaults to the ``FORGE_MCP_TIMEOUT`` env var, then to
    ``DEFAULT_TIMEOUT``.

    ``enforce_skill`` applies the authoring-guide gate (see
    :func:`forge_mcp.skills.require_rule`) — leave it enabled so that code
    driving a Forge operator or writing Forge properties is gated; only tests
    that deliberately bypass the gate pass ``False``.

    Raises:
        ToolError: when the bridge cannot be reached or Blender reports a
            status ``error``. ``ToolError`` messages reach the MCP client
            verbatim; a generic exception's text would be treated as a crash
            detail and never leave the server.
    """
    # One check for every entry point, dedicated tools and ``forge_execute``
    # alike: it follows bpy aliases, so ordinary Blender modelling passes
    # through and only code that actually drives a Forge operator or writes
    # Forge properties asks for the authoring guide. Scanning the generated
    # code for marker substrings used to sit here, but it could not tell a
    # Forge edit from the ``obj.select_set(True)`` that ``op_call`` emits for
    # every selection-based call — so it demanded the guide for nearly
    # everything.
    required: tuple[str, ...] = ()
    if enforce_skill:
        required = required_skills_for_code(code)
        for name in required:
            require_rule(name)
    host = os.environ.get("FORGE_MCP_HOST", DEFAULT_HOST)
    port = int(os.environ.get("FORGE_MCP_PORT", str(DEFAULT_PORT)))
    if timeout is None:
        timeout = float(os.environ.get("FORGE_MCP_TIMEOUT", str(DEFAULT_TIMEOUT)))
    request = (
        json.dumps(
            {
                "type": "execute",
                "code": code,
                "strict_json": strict_json,
                "auth_token": os.environ.get("FORGE_MCP_TOKEN", ""),
            }
        )
        + "\0"
    ).encode("utf-8")

    try:
        with socket.create_connection((host, port), timeout=timeout) as conn:
            conn.sendall(request)
            buf = bytearray()
            while b"\0" not in buf:
                chunk = conn.recv(RECV_BUFFER_SIZE)
                if not chunk:
                    raise ToolError("Blender bridge closed the connection before completing its response")
                buf.extend(chunk)
    except OSError as exc:
        raise ToolError(
            f"Cannot reach the Blender Forge bridge at {host}:{port}: {exc}. "
            "Is Blender running with the Forge MCP bridge started? Note that a Blender "
            "session without online access (no --online-mode) never starts the bridge — "
            "check the addon preferences and the autostart_error field."
        ) from exc

    try:
        response = json.loads(buf.split(b"\0", 1)[0])
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ToolError("Blender bridge returned an invalid JSON response") from exc
    if not isinstance(response, dict):
        raise ToolError("Blender bridge response must be a JSON object")
    status = response.get("status")
    if status == "error":
        raise ToolError(response.get("message", "Blender execution error"))
    if status != "ok":
        raise ToolError(f"Blender bridge returned unknown response status: {status!r}")
    result = response.get("result")
    if not isinstance(result, dict):
        raise ToolError("Blender bridge response field 'result' must be a JSON object")
    if response.get("stdout"):
        result = {**result, "stdout": response["stdout"]}
    if response.get("stderr"):
        result = {**result, "stderr": response["stderr"]}
    # Soft mode: the operation went through, so hand back a one-time pointer to
    # the guide it would otherwise have been blocked on. Claiming happens here,
    # after success, so a failed call leaves nothing queued behind it.
    if hints := claim_hints(required):
        result = {**result, "skill_hint": hint_message(hints)}
    return result


def op_call(
    op_name: str,
    select: list[str] | None = None,
    setup: str = "",
    post_select_setup: str = "",
    **params,
) -> str:
    """Build Python code that calls ``bpy.ops.forge.<op_name>`` and reports the result.

    *select* is a list of object names: the generated code deselects everything,
    then selects them in order (first becomes active) before calling the operator
    — most Forge operators act on the current selection. When *select* is None
    the current selection is left untouched.

    The generated code sets Blender's ``result`` dict (required by the bridge)
    with the operator return value, the selected object names after the call,
    and the objects created by the call (scene membership diff before/after) —
    letting the agent chain operators without guessing generated names.
    *setup* is extra code executed before selection; *post_select_setup* runs
    after generated selection setup and before the operator call.
    """
    args = ", ".join(f"{key}={value!r}" for key, value in params.items())
    lines = ["import bpy"]
    if setup:
        lines.append(setup)
    lines.append("before = set(bpy.context.scene.objects)")
    if select is not None:
        names = ", ".join(repr(n) for n in select)
        lines.append("bpy.ops.object.select_all(action='DESELECT')")
        lines.append("for obj in bpy.data.objects:")
        lines.append("    if 'selected_order' in obj:")
        lines.append("        del obj['selected_order']")
        lines.append(f"for order, n in enumerate([{names}]):")
        lines.append("    obj = bpy.data.objects[n]")
        lines.append("    obj['selected_order'] = order")
        lines.append("    obj.select_set(True)")
        if select:
            lines.append(f"bpy.context.view_layer.objects.active = bpy.data.objects[{select[0]!r}]")
        else:
            lines.append("bpy.context.view_layer.objects.active = None")
    if post_select_setup:
        lines.append(post_select_setup)
    lines.append(f"ret = bpy.ops.forge.{op_name}({args})")
    lines.append(
        "result = {\n"
        '    "return_value": list(ret),\n'
        '    "objects": [o.name for o in bpy.context.selected_objects],\n'
        '    "created": [o.name for o in bpy.context.scene.objects if o not in before],\n'
        "}"
    )
    return "\n".join(lines)
