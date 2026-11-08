[CmdletBinding()]
param(
    [string]$CodexHome,
    [string]$CodexExe
)
$ErrorActionPreference = 'Stop'
if (-not $CodexExe) { $CodexExe = (Get-Command codex -ErrorAction Stop).Source }
$market = Join-Path $PSScriptRoot '.agents/plugins/marketplace.json'
if (-not (Test-Path -LiteralPath $market -PathType Leaf)) {
    throw 'Marketplace missing. Extract the complete ZIP before running this installer.'
}
$previousCodexHome = $env:CODEX_HOME
try {
    if ($CodexHome) {
        $env:CODEX_HOME = [System.IO.Path]::GetFullPath($CodexHome)
        New-Item -ItemType Directory -Path $env:CODEX_HOME -Force | Out-Null
    }
    & $CodexExe plugin marketplace add $PSScriptRoot --json
    if ($LASTEXITCODE -ne 0) { throw 'Local marketplace registration failed.' }
    & $CodexExe plugin add 'youtube-bilibili-video-production@youtube-bilibili-local' --json
    if ($LASTEXITCODE -ne 0) { throw 'Plugin installation failed.' }
    & $CodexExe plugin list --marketplace youtube-bilibili-local --json
    if ($LASTEXITCODE -ne 0) { throw 'Plugin verification failed.' }
    Write-Output 'Installed. Start a new Codex chat to load YouTube+Bilibili Video Production.'
} finally {
    $env:CODEX_HOME = $previousCodexHome
}
