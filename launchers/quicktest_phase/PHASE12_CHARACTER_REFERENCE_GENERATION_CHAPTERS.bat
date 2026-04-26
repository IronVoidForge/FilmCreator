@echo off
setlocal EnableExtensions
set "PROJECT_SLUG=%~1"
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=princess_of_mars_test"
set "CHAPTERS=%~2"
if "%CHAPTERS%"=="" set "CHAPTERS=2-3"
set "LIMIT=%~3"
if "%LIMIT%"=="" set "LIMIT=2"
call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0"
if errorlevel 1 exit /b 1
cd /d "%FILMCREATOR_ROOT%"
call "%~dp0..\quick_pipeline_test\_shared\start_clean_comfyui_8190.bat"
if errorlevel 1 exit /b 1
set "FILMCREATOR_COMFY_BASE_URL=http://127.0.0.1:8190"
set "FILMCREATOR_COMFY_INPUT_DIR=%FILMCREATOR_ROOT%\.comfy_clean\input"
set "FILMCREATOR_COMFY_OUTPUT_DIR=%FILMCREATOR_ROOT%\.comfy_clean\output"
echo COMMAND: python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant raw
python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant raw
if errorlevel 1 exit /b 1
echo COMMAND: python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant character_clean
python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant character_clean
if errorlevel 1 exit /b 1
echo COMMAND: python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant character_readability
python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant character_readability
if errorlevel 1 exit /b 1
echo COMMAND: python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant character_polish
python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant character_polish
if errorlevel 1 exit /b 1
pause
