@echo off

REM generated in GPT-4-turbo

REM Create virtual environment named venv
python -m venv .venv

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Install requests, beautifulsoup4 and customtkinter packages
pip install requests beautifulsoup4 customtkinter

REM Deactivate the virtual environment
deactivate

echo Virtual environment setup complete.
pause