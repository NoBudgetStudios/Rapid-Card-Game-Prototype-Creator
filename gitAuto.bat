@echo on
cd %~dp0
git add .
FOR /F "tokens=*" %%i IN ('date /t') DO set DATEVAR=%%i
FOR /F "tokens=*" %%i IN ('time /t') DO set TIMEVAR=%%i
git commit -m "%DATEVAR% %TIMEVAR%"
git push origin main
pause