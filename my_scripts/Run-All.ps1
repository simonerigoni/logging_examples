# Run all other .ps1 scripts in the correct order
# .\my_scripts\Run-All.ps1

$currentScriptFolder = $PSScriptRoot
$currentScriptFolderLeaf = Split-Path -Path $currentScriptFolder -Leaf
. ".\$currentScriptFolderLeaf\Config.ps1"

$setupScript = "Set-Up.ps1"
$formatScript = "FormatAndLint.ps1"
$testScript = "Test.ps1"
$cleanupScript = "Clean-Up.ps1"

Write-Host "Starting execution of all scripts in the correct order..." -ForegroundColor Green

& ".\$scriptsFolder\$setupScript"
& ".\$scriptsFolder\$formatScript"
& ".\$scriptsFolder\$testScript"

Write-Host "Run the cleanup script ($cleanupScript) manually when needed..." -ForegroundColor Yellow

Write-Host "All scripts completed successfully!" -ForegroundColor Green