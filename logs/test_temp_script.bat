@echo off
setlocal EnableDelayedExpansion

set "TEMP_SCRIPT=logs\test_script.tmp"

(
echo print("Hello from temp script"^)
echo print("Line 2"^)
) > "%TEMP_SCRIPT%"

python "%TEMP_SCRIPT%"
set "EXIT_CODE=%ERRORLEVEL%"

del "%TEMP_SCRIPT%" >nul 2>nul

echo Exit code: %EXIT_CODE%
