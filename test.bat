@echo off
taskkill /IM java.exe
shutdown -s -t 30
echo 'hello!'