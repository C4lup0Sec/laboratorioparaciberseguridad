Class DirToBackup
{
    [String]$path
    DirToBackup([String]$path) {
      $this.path = $path
    }
}
$defaultListOfExcluded = "C:\backup\listOfExcluded.txt"#aqui se incluyen los directorios a excluir

$pathFromPrefix = "C:\"
$pathToPrefix = "F:\Backup\"
Write-Output "Conecte un disco duro. puede mostrarse con la letra F"
pause
$dirsToBackup = @(
    New-Object DirToBackup "backup"
    New-Object DirToBackup "development"
    New-Object DirToBackup "Dropbox"
    New-Object DirToBackup "Google"
)
$dirsToBackup | ForEach-Object {
    mkdir -Path $($pathToPrefix + $_.path) -Force
    xcopy $($pathFromPrefix + $_.path) $($pathToPrefix + $_.path) /D /S /Y /H /EXCLUDE:$defaultListOfExcluded
    #https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy
}
pause
