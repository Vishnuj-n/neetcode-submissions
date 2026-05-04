$taskName = "NeetCode Anki Sync"
$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "run.py" -WorkingDirectory (Get-Location)
$trigger = New-ScheduledTaskTrigger -Daily -At "09:00"
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Force
Write-Host "Task '$taskName' created. Runs daily at 9:00 AM."
