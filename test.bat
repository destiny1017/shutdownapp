@echo off
#timeout /t 1 /nobreak >nul
taskkill /IM java.exe
shutdown -s -t 30
echo 'hello!'