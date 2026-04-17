@echo off
setlocal

set "FILMCREATOR_ROOT=C:\FilmCreator"
set "PROJECT_SLUG=pilot_scene"
set "SCENE_ID=SC001"
set "CLIP_ID=CL001"
set "COMFY_URL=http://127.0.0.1:8191/system_stats"
set "PROMPT_FILE=projects/pilot_scene/03_prompt_packages/cut_motion/SC001/CL001/SC001_CL001_cut_motion_prompt.md"
set "VIDEO_DIR=projects/pilot_scene/05_scenes/SC001/clips/CL001/video"
set "CLIP_STATE=projects/pilot_scene/05_scenes/SC001/clips/CL001/clip_state.json"
set "FILMCREATOR_COMFY_BASE_URL=http://127.0.0.1:8191"
set "FILMCREATOR_COMFY_INPUT_DIR=C:\FilmCreator\.comfy_video\input"
set "FILMCREATOR_COMFY_OUTPUT_DIR=C:\FilmCreator\.comfy_video\output"
set "FILMCREATOR_COMFY_TIMEOUT_SECONDS=7200"
set "PLAN_JSON=%TEMP%\filmcreator_cut_motion_plan_%RANDOM%.json"
set "RUN_JSON=%TEMP%\filmcreator_cut_motion_run_%RANDOM%.json"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%PROMPT_FILE%" (
    echo Missing cut-motion prompt file: %FILMCREATOR_ROOT%\%PROMPT_FILE%
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%CLIP_STATE%" (
    echo Missing clip state: %FILMCREATOR_ROOT%\%CLIP_STATE%
    exit /b 1
)

for /f "usebackq delims=" %%I in (`powershell -NoProfile -ExecutionPolicy Bypass -Command "$clipState = Get-Content '%FILMCREATOR_ROOT%\%CLIP_STATE%' -Raw | ConvertFrom-Json; if($clipState.current_continuity_source){ $clipState.current_continuity_source } elseif($clipState.approved_assets.approved_keyframe){ $clipState.approved_assets.approved_keyframe }"`) do set "CONTINUITY_SOURCE=%%I"

if not defined CONTINUITY_SOURCE (
    echo No approved continuity source was found in clip state.
    echo Run the keyframe review-and-approval BAT first, then retry this smoke test.
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%CONTINUITY_SOURCE%" (
    echo The continuity source recorded in clip state does not exist:
    echo   %FILMCREATOR_ROOT%\%CONTINUITY_SOURCE%
    exit /b 1
)

call "%~dp0start_comfyui_video_8191.bat"

echo Waiting for video ComfyUI to answer on 8191...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ready=$false; for($i=0; $i -lt 90; $i++){ try { $null = Invoke-WebRequest -UseBasicParsing '%COMFY_URL%' -TimeoutSec 2; $ready=$true; break } catch { Start-Sleep -Seconds 1 } }; if($ready){ exit 0 } else { exit 1 }"
if not "%ERRORLEVEL%"=="0" (
    echo Video ComfyUI did not become reachable on 127.0.0.1:8191 within the wait window.
    echo Check the video ComfyUI terminal and retry this BAT.
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Planning the pilot short-cut motion batch...
python -m orchestrator plan-batch %PROJECT_SLUG% cut_motion --scene %SCENE_ID% --clip %CLIP_ID% --seed 5000 > "%PLAN_JSON%"
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

echo Running the pilot short-cut motion batch...
python -m orchestrator run-batch "%BATCH_MANIFEST%" --seed-base 6000 --execute > "%RUN_JSON%"
if errorlevel 1 (
    echo.
    echo run-batch failed. Inspect the manifest for blockers.
    del "%PLAN_JSON%" >nul 2>nul
    del "%RUN_JSON%" >nul 2>nul
    pause
    exit /b 1
)

for /f "usebackq delims=" %%I in (`powershell -NoProfile -ExecutionPolicy Bypass -Command "$manifest = Get-Content '%FILMCREATOR_ROOT%\%BATCH_MANIFEST%' -Raw | ConvertFrom-Json; $manifest.status"`) do set "BATCH_STATUS=%%I"
if /I not "%BATCH_STATUS%"=="completed" (
    echo.
    echo The cut-motion batch finished with status: %BATCH_STATUS%
    echo Review blockers in:
    echo   %FILMCREATOR_ROOT%\%BATCH_MANIFEST%
    echo.
    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
      "$manifest = Get-Content '%FILMCREATOR_ROOT%\%BATCH_MANIFEST%' -Raw | ConvertFrom-Json; " ^
      "Write-Host 'blockers:'; " ^
      "$manifest.blockers | ForEach-Object { Write-Host ('  ' + $_) }"
    del "%PLAN_JSON%" >nul 2>nul
    del "%RUN_JSON%" >nul 2>nul
    pause
    exit /b 1
)

echo.
echo Short-cut motion summary:
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$manifest = Get-Content '%FILMCREATOR_ROOT%\%BATCH_MANIFEST%' -Raw | ConvertFrom-Json; " ^
  "Write-Host ('manifest: ' + '%BATCH_MANIFEST%'); " ^
  "Write-Host ('status: ' + $manifest.status); " ^
  "Write-Host ('approved continuity source: ' + $manifest.batch.candidates[0].continuity_source); " ^
  "Write-Host 'output_files:'; " ^
  "$manifest.output_files | ForEach-Object { Write-Host ('  ' + $_) }"

echo.
echo If this worked, you should see one or more MP4 files under:
echo   %FILMCREATOR_ROOT%\%VIDEO_DIR%
echo.
echo What to look for:
echo   1. New MP4 files named like SC001_CL001_MV##_v###.mp4
echo   2. The batch manifest status should be completed
echo   3. Each candidate in the manifest should have output_files populated
echo   4. The motion should start from the approved keyframe composition rather than a random new frame
echo   5. Each candidate should be one short cut, not a stitched long-form continuation
echo   6. The short motion should preserve the approved keyframe lighting rather than shifting to an unexplained blue cast

del "%PLAN_JSON%" >nul 2>nul
del "%RUN_JSON%" >nul 2>nul
pause
endlocal
