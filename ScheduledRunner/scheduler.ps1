#Variables
$TaskName = "Scrape Web CSV Sports Data"

#create a scheduled task with powershell
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "C:\Users\varkr\PycharmProjects\pythonProject1\Selenium\intro.intro.py"
$Trigger = New-ScheduledTaskTrigger -Daily -At 1am
$ScheduledTask = New-ScheduledTask -Action $action -Trigger $trigger

Register-ScheduledTask  -TaskName $TaskName -InputObject $ScheduledTask

