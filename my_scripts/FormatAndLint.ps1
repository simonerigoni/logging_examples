# Formats and lint code
# .\my_scripts\FormatAndLint.ps1

$currentScriptFolder = $PSScriptRoot
$currentScriptFolderLeaf = Split-Path -Path $currentScriptFolder -Leaf
. ".\$currentScriptFolderLeaf\Config.ps1"

# Stop on any error for robust execution
$ErrorActionPreference = "Stop"

Write-Host "Starting format and lint process..." -ForegroundColor Green

# Activate virtual environment
Write-Host "Activating virtual environment ($venvFolder)..." -ForegroundColor Yellow
if (-not (Test-Path $venvFolder)) {
    Write-Host "Virtual environment ($venvFolder) not found! Please run setup.ps1 first" -ForegroundColor Red
    exit 1
}
. ".\$venvFolder\Scripts\Activate.ps1"

# Format Python files with autopep8
Write-Host "Formatting Python files with autopep8..." -ForegroundColor Yellow
$pythonFiles = Get-ChildItem -Path . -Filter *.py -Recurse | Where-Object { $_.FullName -notmatch $venvFolder }
if ($pythonFiles.Count -eq 0) {
    Write-Host "No Python files found to format!" -ForegroundColor Yellow
} else {
    foreach ($file in $pythonFiles) {
        autopep8 --in-place $file.FullName
        if ($LASTEXITCODE -ne 0) {
            Write-Host "autopep8 failed for $($file.FullName)! Check the file for errors" -ForegroundColor Red
            exit 1
        }
        Write-Host "Formatted: $($file.FullName)" -ForegroundColor Green
    }
}

# Lint Python files with pycodestyle and save reports
Write-Host "Linting Python files with pycodestyle..." -ForegroundColor Yellow
if (-not (Test-Path $codeStyleFolder)) {
    New-Item -ItemType Directory -Path $codeStyleFolder | Out-Null
    Write-Host "Created folder: $codeStyleFolder" -ForegroundColor Green
}

foreach ($file in $pythonFiles) {
    $reportFile = Join-Path $codeStyleFolder "pycodestyle_$($file.BaseName)_report.txt"
    pycodestyle $file.FullName | Out-File $reportFile
    if ($LASTEXITCODE -ne 0) {
        Write-Host "pycodestyle found issues in $($file.FullName). Report saved to $reportFile" -ForegroundColor Yellow
    } else {
        Write-Host "No issues found in $($file.FullName). Report saved to $reportFile" -ForegroundColor Green
    }
}

# Deactivate virtual environment if it was activated
Write-Host "Deactivating virtual environment..." -ForegroundColor Cyan
deactivate

Write-Host "Format and lint process complete! Check reports in $codeStyleFolder if needed" -ForegroundColor Green