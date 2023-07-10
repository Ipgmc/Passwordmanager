@echo off
setlocal enabledelayedexpansion
set "string=abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&/()=?*+'#-_.:,;><|~^°"
set "result="
for /L %%i in (1,1,30) do call :add
echo %result%


:add
set /a x=%random% %% 62
set result=%result%!string:~%x%,1!
