@echo off
cls
echo Protecting The Verdant Isle from Bot Crashes...
title Bot Restarter - The Verdant Isle

:values
set EXE=TheIsleClient-Win64-Shipping.exe

:BotStart
echo (%time%) Starting Bots...
echo (%time%) Empty Cooldown Bot started.
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\cooldowns\emptycooldown.py" 
echo (%time%) Food Cooldown Bot started.
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\cooldowns\foodcooldown.py" 
echo (%time%) Grow Cooldown Bot started.
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\cooldowns\growcooldown.py" 
echo (%time%) Slay Cooldown Bot started.
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\cooldowns\slaycooldown.py" 
echo (%time%) Economy/Legacy Bot started.
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\legacybiscuitbot.py" 

:check
tasklist /fi "ImageName eq %EXE%" /fo csv 2>NUL | find /I "%EXE%">NUL
if "%ERRORLEVEL%"=="0" goto FOUND
echo (%time%) Game Not Running!
echo (%time%) Starting Game Now...
start steam://rungameid/376210
timeout /t 50
goto check

:FOUND
echo (%time%) Game Running!
echo (%time%) Injecting Bot into Server Please Wait...
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\restarter.py"
echo (%time%) Biscuit Bot started.
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\biscuitbot.py" 
echo (%time%) Loading Bot Functions.... 
timeout /t 90
echo (%time%) Sea Biscuit Bot started.
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\seabiscuitbot .py" 
echo (%time%) Chat Commands Bot started.
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\chatcommandsbot.py"
echo (%time%) Restart Announcements started.
start /min "C:\Users\Olden\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Olden\Desktop\PythonBot\restartann.py"




echo (%time%) Restarting Automatically in:
echo (%time%) [CLICK HERE] AND HIT ENTER TO FORCE RESTART
timeout /t 21600



echo (%time%) WARNING: Restarting Everything in 30 seconds.
timeout /t 30

taskkill /F /IM python.exe /T
taskkill /F /IM TheIsleServer-Win64-Shipping.exe /T
taskkill /F /IM TheIsleClient-Win64-Shipping.exe /T

echo (%time%) WARNING: Waiting for Evrima Server Restart...
timeout /t 90
goto BotStart