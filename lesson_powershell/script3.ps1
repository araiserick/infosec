param (
)
$currentDirectory = Get-Location
$files = Get-ChildItem -Path $currentDirectory
Write-Output "Текущий каталог: $currentDirectory"
Write-Output "Файлы в каталоге:"
$files | ForEach-Object { Write-Output $_.Name }
Write-Output "Количество файлов в каталоге: $($files.Count)"
