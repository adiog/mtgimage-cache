@echo off

IF NOT EXIST venv (virtualenv venv)
call venv/scripts/activate.bat
pip install -r virtualenv-python3.5.txt

