# Set up
# .\my_scripts\Set-Up.ps1

$currentScriptFolder = $PSScriptRoot
$currentScriptFolderLeaf = Split-Path -Path $currentScriptFolder -Leaf
. ".\$currentScriptFolderLeaf\Config.ps1"

# Stop on any error for robust execution
$ErrorActionPreference = "Stop"

Write-Host "Starting setup process..." -ForegroundColor Green

# Check for Python
Write-Host "Checking for Python..." -ForegroundColor Yellow
$pythonVersion = (python --version 2>$null)
if (-not $pythonVersion) {
    Write-Host "Python not found! Please install Python and rerun this script" -ForegroundColor Red
    exit 1
} else {
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
}

# Create virtual environment if it doesn't exist
Write-Host "Checking for virtual environment ($venvFolder)..." -ForegroundColor Yellow
if (-not (Test-Path $venvFolder)) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv $venvFolder
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to create virtual environment!" -ForegroundColor Red
        exit 1
    }
    Write-Host "Virtual environment created!" -ForegroundColor Green
} else {
    Write-Host "Virtual environment already exists!" -ForegroundColor Green
}

# Activate virtual environment and install dependencies
Write-Host "Activating virtual environment and installing dependencies..." -ForegroundColor Yellow
. ".\$venvFolder\Scripts\Activate.ps1"
if (-not (Test-Path $requirementsFile)) {
    Write-Host "$requirementsFile not found! Please create it with required dependencies" -ForegroundColor Red
    exit 1
}

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Cyan
python -m pip install --upgrade pip

# Install requirements
Write-Host "Installing project dependencies..." -ForegroundColor Cyan
pip install -r $requirementsFile
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to install dependencies from $requirementsFile!" -ForegroundColor Red
    exit 1
}
Write-Host "Dependencies installed successfully!" -ForegroundColor Green

# Deactivate virtual environment if it was activated
Write-Host "Deactivating virtual environment..." -ForegroundColor Cyan
Write-Host "Note: To activate the virtual environment run: .\$venvFolder\Scripts\Activate.ps1"
deactivate

Write-Host "Setup complete! Your Python project environment is ready" -ForegroundColor Green
