@echo off
if "%1"=="" (
	del *.pyc /s /q 2>NUL
	del *.pyo /s /q 2>NUL
	del __pycache__ /s /q 2>NUL
	rd __pycache__ /s /q 2>NUL
) else (
	del %1\*.pyc /s /q 2>NUL
	del %1\*.pyo /s /q 2>NUL
	del %1\__pycache__ /s /q 2>NUL
	rd %1\ __pycache__ /s /q 2>NUL
)

