#!/usr/bin/env bash
set -eu

launch="${1:-none}"
case "$launch" in
  none|claude|codex) ;;
  *) echo "Usage: $0 [none|claude|codex]" >&2; exit 2 ;;
esac

root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
server="$root/mcp-server"

if [ ! -f "$server/pyproject.toml" ]; then
  echo "mcp-server/pyproject.toml was not found. Run this script from a complete MCP workspace." >&2
  exit 1
fi
if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required. Install it from https://docs.astral.sh/uv/ and reopen the shell." >&2
  exit 1
fi

echo "Installing forge-mcp dependencies..."
# A copied MCP workspace does not include the Blender test project's root
# pyproject.toml. Install against the server's own environment so only MCP
# dependencies are resolved and the command also works outside this repository.
venv="$server/.venv"
uv venv "$venv" --python 3.11
uv pip install --python "$venv/bin/python" --editable "$server"
echo "MCP dependencies are ready in $venv"
echo "Open a new console in $root before launching Claude Code or Codex."

case "$launch" in
  claude)
    command -v claude >/dev/null 2>&1 || { echo "claude was not found on PATH." >&2; exit 1; }
    cd "$root"
    exec claude
    ;;
  codex)
    command -v codex >/dev/null 2>&1 || { echo "codex was not found on PATH." >&2; exit 1; }
    export CODEX_HOME="$root/.codex"
    cd "$root"
    exec codex
    ;;
esac
