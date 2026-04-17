@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"
set "PROJECT_SLUG=pilot_scene"
set "SCENE_ID=SC001"
set "CLIP_ID=CL001"
set "COMFY_URL=http://127.0.0.1:8190/system_stats"
set "PROMPT_FILE=projects/pilot_scene/03_prompt_packages/fixes/SC001/CL001/SC001_CL001_fix_01_prompt.md"
set "SECONDARY_REF=projects/pilot_scene/05_scenes/SC001/clips/CL001/inputs/smoke_char.png"
set "STILL_FIX_DIR=projects/pilot_scene/05_scenes/SC001/clips/CL001/stills/fixes"
set "CLIP_STATE=projects/pilot_scene/05_scenes/SC001/clips/CL001/clip_state.json"
set "FILMCREATOR_COMFY_BASE_URL=http://127.0.0.1:8190"
set "FILMCREATOR_COMFY_INPUT_DIR=C:\FilmCreator\.comfy_clean\input"
set "FILMCREATOR_COMFY_OUTPUT_DIR=C:\FilmCreator\.comfy_clean\output"
set "FILMCREATOR_COMFY_TIMEOUT_SECONDS=7200"
set "PLAN_JSON=%TEMP%\filmcreator_still_fix_plan_%RANDOM%.json"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%PROMPT_FILE%" (
    echo Missing still-fix prompt file: %FILMCREATOR_ROOT%\%PROMPT_FILE%
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%SECONDARY_REF%" (
    echo Missing still-fix secondary reference: %FILMCREATOR_ROOT%\%SECONDARY_REF%
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%CLIP_STATE%" (
    echo Missing clip state: %FILMCREATOR_ROOT%\%CLIP_STATE%
    exit /b 1
)

call "%~dp0start_comfyui_clean_8190.bat"

echo Waiting for clean ComfyUI to answer on 8190...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ready=$false; for($i=0; $i -lt 30; $i++){ try { $null = Invoke-WebRequest -UseBasicParsing '%COMFY_URL%' -TimeoutSec 2; $ready=$true; break } catch { Start-Sleep -Seconds 1 } }; if($ready){ exit 0 } else { exit 1 }"
if not "%ERRORLEVEL%"=="0" (
    echo Clean ComfyUI did not become reachable on 127.0.0.1:8190 within the wait window.
    echo Check the clean ComfyUI terminal and retry this BAT.
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Planning the pilot still-fix batch...
python -m orchestrator plan-batch %PROJECT_SLUG% still_fix --scene %SCENE_ID% --clip %CLIP_ID% --seed 7000 > "%PLAN_JSON%"
if errorlevel 1 (
    echo.
    echo plan-batch failed.
    del "%PLAN_JSON%" >nul 2>nul
    pause
    exit /b 1
)

for /f "usebackq delims=" %%I in (`powershell -NoProfile -ExecutionPolicy Bypass -Command "$plan = Get-Content '%PLAN_JSON%' -Raw | ConvertFrom-Json; $plan.batch_manifest_path"`) do set "BATCH_MANIFEST=%%I"
if not defined BATCH_MANIFEST (
    echo Could not resolve batch_manifest_path from %PLAN_JSON%.
    del "%PLAN_JSON%" >nul 2>nul
    pause
    exit /b 1
)

echo Running the pilot still-fix batch...
python -m orchestrator run-batch "%BATCH_MANIFEST%" --ref "image_2=%SECONDARY_REF%" --seed-base 8000 --execute
if errorlevel 1 (
    echo.
    echo run-batch failed. Inspect the manifest for blockers.
    del "%PLAN_JSON%" >nul 2>nul
    pause
    exit /b 1
)

echo.
echo If this worked, you should see one or more PNG files under:
echo   %FILMCREATOR_ROOT%\%STILL_FIX_DIR%
echo.
echo What to look for:
echo   1. New PNG files named like SC001_CL001_FX##_v###.png
echo   2. The batch manifest status should be completed
echo   3. The stills should preserve the approved keyframe composition and lighting
echo   4. The human duelist likeness and local hand details should be tighter than the base keyframe

del "%PLAN_JSON%" >nul 2>nul
pause
endlocal
