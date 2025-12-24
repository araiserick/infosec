param (
    [string]$parameter
)
if (Test-Path -Path $parameter) {
    if (Get-Item -Path $parameter -ErrorAction SilentlyContinue | Where-Object { $_.PSIsContainer }) {
        Write-Output "$parameter - это каталог."
    } else {
        Write-Output "$parameter - это файл."
    }
} else {
    Write-Output "$parameter - не существует."
}