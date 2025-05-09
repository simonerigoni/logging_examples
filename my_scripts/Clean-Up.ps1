# Clean up
# .\my_scripts\Clean-Up.ps1

$currentScriptFolder = $PSScriptRoot
$currentScriptFolderLeaf = Split-Path -Path $currentScriptFolder -Leaf
. ".\$currentScriptFolderLeaf\Config.ps1"

# Stop on any error for robust execution
$ErrorActionPreference = "Stop"

Write-Host "Starting cleanup process..." -ForegroundColor Green

# Check and delete virtual environment
Write-Host "Checking for virtual environment ($venvFolder)..." -ForegroundColor Yellow
if (Test-Path $venvFolder) {
    Write-Host "Deleting virtual environment..." -ForegroundColor Yellow
    try {
        Remove-Item -Path $venvFolder -Recurse -Force
        Write-Host "Virtual environment deleted!" -ForegroundColor Green
    } catch {
        Write-Host "Failed to delete virtual environment!" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "Virtual environment does not exist!" -ForegroundColor Green
}

# Delete specific files if needed


Write-Host "Cleanup complete!" -ForegroundColor Green