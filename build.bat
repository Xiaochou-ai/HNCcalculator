@echo off
chcp 65001

:: Delete temporary files and build directory
rmdir /s /q build 2>nul
del *.spec 2>nul

:: Get formatted date time
for /f "delims=" %%a in ('powershell -Command "Get-Date -Format 'yyyyMMdd_HHmm'"') do set "DATETIME=%%a"

:: Set output file name
set "EXE_NAME=HuaZhong_Calculator_%DATETIME%"

:: Create dist directory if it doesn't exist
if not exist dist mkdir dist

:: Check if both required image files exist
if not exist xiaoai.jpg (
    echo Error: xiaoai.jpg not found
    pause
    exit /b 1
)

if not exist hnc-logo.png (
    echo Error: hnc-logo.png not found
    pause
    exit /b 1
)

:: Convert xiaoai.jpg to icon for application icon
python convert_icon.py

:: Package the application with the icon
pyinstaller -F --noconsole --icon=logo.ico --add-data "hnc-logo.png;." --name "%EXE_NAME%" --distpath "dist" acceleration_calculator.py

:: Clean up
if exist logo.ico del logo.ico

echo Build completed: %EXE_NAME%.exe
pause