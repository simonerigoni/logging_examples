# Testing
# .\my_scripts\Test.ps1

$currentScriptFolder = $PSScriptRoot
$currentScriptFolderLeaf = Split-Path -Path $currentScriptFolder -Leaf
. ".\$currentScriptFolderLeaf\Config.ps1"

# Stop on any error for robust execution
$ErrorActionPreference = "Stop"

Write-Host "Starting test process..." -ForegroundColor Green

# Activate virtual environment
Write-Host "Activating virtual environment ($venvFolder)..." -ForegroundColor Yellow
if (-not (Test-Path $venvFolder)) {
    Write-Host "Virtual environment ($venvFolder) not found! Please run setup.ps1 first" -ForegroundColor Red
    exit 1
}
. ".\$venvFolder\Scripts\Activate.ps1"

# Run pytest to test the function locally
Write-Host "Running tests with pytest..." -ForegroundColor Yellow
pytest
if ($LASTEXITCODE -ne 0) {
    Write-Host "Tests failed!" -ForegroundColor Red
    exit 1
}

# Deactivate virtual environment if it was activated
Write-Host "Deactivating virtual environment..." -ForegroundColor Cyan
deactivate

Write-Host "Tests passed successfully!" -ForegroundColor Green