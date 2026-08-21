# Install a logon scheduled task: WASAPI Spotify clips -> taste_data (this PC).
# Usage:
#   powershell -ExecutionPolicy Bypass -File .\tools\Install-SpotifyPcCapture.ps1
#   powershell -ExecutionPolicy Bypass -File .\tools\Install-SpotifyPcCapture.ps1 -Uninstall

param([switch]$Uninstall)

$ErrorActionPreference = "Stop"
$TaskName = "GitStatus-SpotifyPcCapture"
$Root = Split-Path -Parent $PSScriptRoot
$Pyw = (Get-Command pythonw.exe -ErrorAction SilentlyContinue).Source
if (-not $Pyw) {
    $Pyw = Join-Path $env:LOCALAPPDATA "Programs\Python\Python312\pythonw.exe"
}
if (-not (Test-Path $Pyw)) { throw "pythonw.exe not found" }

$Script = Join-Path $PSScriptRoot "spotify_pc_capture.py"
$Vbs = Join-Path $PSScriptRoot "Start-SpotifyPcCapture.vbs"
$LogDir = Join-Path $Root "taste_data"

if ($Uninstall) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
        Where-Object { $_.CommandLine -and $_.CommandLine -match "spotify_pc_capture.py" } |
        ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
    Write-Host "Removed $TaskName"
    exit 0
}

$rootEsc = $Root.Replace("\", "\\")
$pywEsc = $Pyw.Replace("\", "\\")
$scriptEsc = $Script.Replace("\", "\\")
$vbsLines = @(
    'Set sh = CreateObject("WScript.Shell")'
    ('sh.CurrentDirectory = "' + $rootEsc + '"')
    ('sh.Run """' + $pywEsc + '"" ""' + $scriptEsc + '"" loop", 0, False')
)
Set-Content -Path $Vbs -Value $vbsLines -Encoding ASCII

function Start-CaptureNow {
    Start-Process -FilePath $Pyw -ArgumentList @($Script, "loop") -WorkingDirectory $Root -WindowStyle Hidden
}

try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    $action = New-ScheduledTaskAction -Execute "wscript.exe" -Argument $Vbs -WorkingDirectory $Root
    $trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -MultipleInstances IgnoreNew -StartWhenAvailable
    $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
    Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force | Out-Null
    Start-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    Write-Host "Installed and started $TaskName"
} catch {
    Write-Host ("Scheduled task failed: " + $_.Exception.Message)
    Write-Host "Starting capture process now"
    Start-CaptureNow
}

$existing = Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -and $_.CommandLine -match "spotify_pc_capture.py" }
if (-not $existing) {
    Start-CaptureNow
}

Write-Host ("Log: " + (Join-Path $LogDir "pc_capture.log"))
Write-Host ("Status: python " + $Script + " status")
