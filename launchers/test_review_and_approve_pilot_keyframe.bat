@echo off
setlocal EnableDelayedExpansion

set "FILMCREATOR_ROOT=C:\FilmCreator"
set "PROJECT_SLUG=pilot_scene"
set "SCENE_ID=SC001"
set "CLIP_ID=CL001"
set "STAGE=keyframe"
set "MANIFEST_REL=projects\pilot_scene\05_scenes\SC001\clips\CL001\logs\RUN_0001.json"
set "KEYFRAME_DIR_REL=projects\pilot_scene\05_scenes\SC001\clips\CL001\stills\keyframes"
set "CLIP_STATE_REL=projects\pilot_scene\05_scenes\SC001\clips\CL001\clip_state.json"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%MANIFEST_REL%" (
    echo Missing batch manifest: %FILMCREATOR_ROOT%\%MANIFEST_REL%
    exit /b 1
)

if not exist "%FILMCREATOR_ROOT%\%KEYFRAME_DIR_REL%" (
    echo Missing keyframe directory: %FILMCREATOR_ROOT%\%KEYFRAME_DIR_REL%
    exit /b 1
)

for /f %%I in ('powershell -NoProfile -ExecutionPolicy Bypass -Command "(Get-ChildItem \"%FILMCREATOR_ROOT%\%KEYFRAME_DIR_REL%\" -Filter '*.png' | Measure-Object).Count"') do set "KEYFRAME_COUNT=%%I"
if not "%KEYFRAME_COUNT%"=="4" (
    echo Expected exactly 4 keyframe candidates, but found %KEYFRAME_COUNT%.
    echo Check the keyframe folder before running this approval test.
    exit /b 1
)

echo Opening the keyframe folder for review...
start "" "%FILMCREATOR_ROOT%\%KEYFRAME_DIR_REL%"
echo.
echo Review the 4 keyframe images, then choose your top 2 finalists and 1 primary winner.
echo.
call :print_candidates
echo.

:pick_top1
choice /C 1234 /N /M "Choose the first finalist [1-4]: "
set "TOP1=%ERRORLEVEL%"

:pick_top2
choice /C 1234 /N /M "Choose the second finalist [1-4]: "
set "TOP2=%ERRORLEVEL%"
if "%TOP2%"=="%TOP1%" (
    echo The second finalist must be different from the first. Please choose again.
    echo.
    goto :pick_top2
)

:pick_primary
choice /C 1234 /N /M "Choose the primary winner [1-4]: "
set "PRIMARY=%ERRORLEVEL%"
if not "%PRIMARY%"=="%TOP1%" if not "%PRIMARY%"=="%TOP2%" (
    echo The primary winner must also be one of the top 2 finalists.
    echo.
    goto :pick_primary
)

call :resolve_candidate_path %TOP1% TOP1_PATH TOP1_NAME
call :resolve_candidate_path %TOP2% TOP2_PATH TOP2_NAME
call :resolve_candidate_path %PRIMARY% PRIMARY_PATH PRIMARY_NAME

echo.
echo Review choices:
echo Top 2 finalists:
echo   %TOP1%. %TOP1_NAME%
echo   %TOP2%. %TOP2_NAME%
echo Primary winner:
echo   %PRIMARY%. %PRIMARY_NAME%
echo.

cd /d "%FILMCREATOR_ROOT%"

python -m orchestrator review-batch %PROJECT_SLUG% %SCENE_ID% %CLIP_ID% %STAGE% "%MANIFEST_REL%" --decision approve --top-two "%TOP1_PATH%" --top-two "%TOP2_PATH%" --primary "%PRIMARY_PATH%"
if errorlevel 1 (
    echo.
    echo review-batch failed. No promotion was performed.
    pause
    exit /b 1
)

python -m orchestrator promote-asset %PROJECT_SLUG% "%PRIMARY_PATH%" approved_keyframe --scene %SCENE_ID% --clip %CLIP_ID% --index 1
if errorlevel 1 (
    echo.
    echo promote-asset failed after review was recorded.
    pause
    exit /b 1
)

echo.
echo Approval summary:
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$clipState = Get-Content '%FILMCREATOR_ROOT%\%CLIP_STATE_REL%' -Raw | ConvertFrom-Json; " ^
  "Write-Host ('approved_keyframe: ' + $clipState.approved_assets.approved_keyframe); " ^
  "Write-Host ('golden_frame: ' + $clipState.approved_assets.golden_frame); " ^
  "Write-Host ('current_continuity_source: ' + $clipState.current_continuity_source); " ^
  "Write-Host ('latest_review_decision: ' + $clipState.latest_review_decision.decision); " ^
  "Write-Host ('chosen_primary: ' + $clipState.latest_review_decision.chosen_primary); " ^
  "Write-Host 'top_two:'; " ^
  "$clipState.latest_review_decision.top_two | ForEach-Object { Write-Host ('  ' + $_) }"

echo.
echo Manifest review summary:
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$manifest = Get-Content '%FILMCREATOR_ROOT%\%MANIFEST_REL%' -Raw | ConvertFrom-Json; " ^
  "Write-Host ('batch.review_status: ' + $manifest.batch.review_status); " ^
  "Write-Host ('batch.chosen_primary: ' + $manifest.batch.chosen_primary); " ^
  "Write-Host 'batch.top_two:'; " ^
  "$manifest.batch.top_two | ForEach-Object { Write-Host ('  ' + $_) }"

echo.
echo Selected review copy should now exist under:
echo   %FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%\06_reviews\selected\
echo.
echo If the values above are populated, the review-and-approval handoff worked.
pause
exit /b 0

:print_candidates
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$files = Get-ChildItem '%FILMCREATOR_ROOT%\%KEYFRAME_DIR_REL%' -Filter '*.png' | Sort-Object Name; " ^
  "for($i = 0; $i -lt $files.Count; $i++) { Write-Host (($i + 1).ToString() + '. ' + $files[$i].Name) }"
exit /b 0

:resolve_candidate_path
set "CANDIDATE_INDEX=%~1"
set "TARGET_PATH_VAR=%~2"
set "TARGET_NAME_VAR=%~3"
for /f "usebackq delims=" %%I in (`powershell -NoProfile -ExecutionPolicy Bypass -Command "$files = Get-ChildItem '%FILMCREATOR_ROOT%\%KEYFRAME_DIR_REL%' -Filter '*.png' | Sort-Object Name; $index = %CANDIDATE_INDEX%; if($index -lt 1 -or $index -gt $files.Count){ throw 'Candidate index out of range.' }; $files[$index - 1].FullName"`) do set "%TARGET_PATH_VAR%=%%I"
for /f "usebackq delims=" %%I in (`powershell -NoProfile -ExecutionPolicy Bypass -Command "$files = Get-ChildItem '%FILMCREATOR_ROOT%\%KEYFRAME_DIR_REL%' -Filter '*.png' | Sort-Object Name; $index = %CANDIDATE_INDEX%; if($index -lt 1 -or $index -gt $files.Count){ throw 'Candidate index out of range.' }; $files[$index - 1].Name"`) do set "%TARGET_NAME_VAR%=%%I"
exit /b 0
