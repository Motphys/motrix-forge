# MCP Skills

These English-only guides describe how agents use Forge MCP tools to create and modify MJCF scenes. They form a separate reference from the Blender UI user manual and MCP installation documentation.

## Guides

| Guide | Use it for |
| --- | --- |
| [Forge create](../reference/mcp-server/forge_mcp/skills/forge_create.md) | Creating model elements and building scene hierarchies |
| [Forge modify](../reference/mcp-server/forge_mcp/skills/forge_modify.md) | Editing existing elements, properties, and relationships |
| [Forge custom material](../reference/mcp-server/forge_mcp/skills/forge_custom_material.md) | Creating and checking custom textured materials |
| [Forge operators](../reference/mcp-server/forge_mcp/skills/forge_operators.md) | Looking up Operator signatures, selection requirements, and supported tool mappings |

## Before using a skill

Install and enable Forge in Blender, start its MCP Bridge, and configure the agent-side server using the [MCP installation guide](../reference/MCP_INSTALL.md). For server configuration and runtime details, read the [MCP Server README](../reference/mcp-server/README.md).

Read the create or modify guide for workflow rules, then use the operator inventory for individual operations. Use the custom material guide when working with texture-based materials.

## Language and source

MCP Skills are maintained in English only. Opening them preserves the current interface language: navigation, controls, and links remain Chinese or English while the article stays in English. The language selector changes the interface language, not the skill content. Both interface versions render the same Markdown sources, with no separate Chinese translation to maintain.

Individual guides use matching routes under `en/mcp_skills/` and `cn/mcp_skills/` for the two interface languages.

The site builds from portable snapshots in `docs/content/reference/mcp-server/forge_mcp/skills/`. To refresh them from the runtime sources in a full Forge checkout, run `python docs/scripts/sync_sources.py` and review the changes. Preview and builds do not depend on files outside `docs/`. Markdown guides added to the snapshot directory are included automatically.
