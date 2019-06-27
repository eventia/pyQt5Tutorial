@echo off
echo ==========================================
echo [PROCESSING...] git add --all .
if [%1] EQU [] (
echo [PROCESSING...] git commit -m "pyQt5 Tutorial - %date%"
) else (
echo [PROCESSING...] git commit -m "%*"
)
echo [PROCESSING...] git push
echo ==========================================
echo.

echo [PROCESSING...] git pull
git pull
echo [PROCESSING...] git add --all .
git add --all .
if [%1] EQU [] (
echo.
echo [PROCESSING...] git commit -m "pyQt5 Tutorial - %date%"
echo.
git commit -m "pyQt5 Tutorial - %date%"
) else (
echo.
echo [PROCESSING...] git commit -m "%*"
echo.
git commit -m "%*"
)
echo.
echo [PROCESSING...] git push
echo.
git push
