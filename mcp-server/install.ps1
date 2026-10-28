[CmdletBinding()]
param(
    [ValidateSet("none", "claude", "codex")]
    [string] $Launch = "none"
)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$server = Join-Path $root "mcp-server"

if (-not (Test-Path (Join-Path $server "pyproject.toml"))) {
    throw "mcp-server/pyproject.toml was not found. Run this script from a complete MCP workspace."
}

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    throw "uv is required. Install it from https://docs.astral.sh/uv/ and reopen PowerShell."
}

Write-Host "Installing forge-mcp dependencies..."

# A copied MCP workspace does not include the Blender test project's root
# pyproject.toml. Install against the server's own environment so only MCP
# dependencies are resolved and the command also works outside this repository.
$venv = Join-Path $server ".venv"
$venvPython = Join-Path $venv "Scripts\python.exe"
& uv venv $venv --python 3.11
if ($LASTEXITCODE -ne 0) { throw "uv venv failed (exit code $LASTEXITCODE)." }
& uv pip install --python $venvPython --editable $server
if ($LASTEXITCODE -ne 0) { throw "MCP dependency installation failed (exit code $LASTEXITCODE)." }

Write-Host "MCP dependencies are ready in $venv"
Write-Host "Open a new console in $root before launching Claude Code or Codex."

if ($Launch -eq "claude") {
    if (-not (Get-Command claude -ErrorAction SilentlyContinue)) { throw "claude was not found on PATH." }
    Push-Location $root
    try { & claude } finally { Pop-Location }
} elseif ($Launch -eq "codex") {
    # Prefer the .cmd shim on Windows; PowerShell execution policy can block
    # the equally-installed codex.ps1 shim even though Codex itself is usable.
    $codexCommand = Get-Command codex.cmd -ErrorAction SilentlyContinue
    if (-not $codexCommand) { $codexCommand = Get-Command codex -ErrorAction SilentlyContinue }
    if (-not $codexCommand) { throw "codex was not found on PATH." }
    # CODEX_HOME makes this copied .codex/config.toml the active Codex config.
    $env:CODEX_HOME = Join-Path $root ".codex"
    Push-Location $root
    try { & $codexCommand.Source } finally { Pop-Location }
}
