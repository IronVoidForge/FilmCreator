@echo off
setlocal

call "%~dp0_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo FilmCreator Quick Pipeline Test
echo ========================================
echo.
echo This quick test mirrors the post-bible pipeline on a small slice:
echo   1. scene contract synthesis
echo   2. scene binding synthesis
echo   3. shot package synthesis
echo   4. dialogue timeline synthesis
echo   5. descriptor enrichment synthesis
echo   6. prompt preparation synthesis
echo   7. quality grading
echo.
pause

call "%~dp000_clear_downstream_artifacts.bat" %*
if errorlevel 1 goto :fail

call "%~dp001_run_scene_contracts.bat" %*
if errorlevel 1 goto :fail

call "%~dp002_run_scene_bindings.bat" %*
if errorlevel 1 goto :fail

call "%~dp003_run_shot_packages.bat" %*
if errorlevel 1 goto :fail

call "%~dp004_run_dialogue_timeline.bat" %*
if errorlevel 1 goto :fail

call "%~dp005_run_descriptor_enrichment.bat" %*
if errorlevel 1 goto :fail

call "%~dp006_run_prompt_preparation.bat" %*
if errorlevel 1 goto :fail

call "%~dp007_run_quality_grading.bat" %*
if errorlevel 1 goto :fail

echo.
echo Quick pipeline test complete.
goto :done

:fail
echo.
echo Quick pipeline test failed.
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
