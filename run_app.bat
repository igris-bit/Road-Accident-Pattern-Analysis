@echo off
title IIoT Road Accident Pattern Analysis - Dashboard
echo ===============================================================
echo Starting Road Accident Pattern Analysis & IIoT Dashboard...
echo ===============================================================

REM Try direct python command first
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python -m streamlit run streamlit_app.py
    goto end
)

REM Fallback to the installed Python 3.12 location
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -m streamlit run streamlit_app.py
    goto end
)

echo [ERROR] Python installation not detected.
echo Please run: winget install Python.Python.3.12
pause

:end
pause

