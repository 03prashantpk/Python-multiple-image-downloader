
@echo off
python main.py %*

Echo ===================================
echo    Show Downloaded Files
Echo ===================================

pause
set mypath=%cd%
%SystemRoot%\explorer.exe %mypath%\images

exit