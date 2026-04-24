@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat"
if errorlevel 1 goto :fail

pushd "%FILMCREATOR_ROOT%" >nul

echo.
echo ========================================
echo FilmCreator Quick Pipeline Test
echo ========================================
echo.
echo This quick test runs the post-bible pipeline in order:
echo   1. clear downstream artifacts
echo   2. descriptor enrichment refresh
echo   3. prompt preparation refresh
echo   4. downstream slice test (chapters 2-3)
echo   5. quality grading
echo.
pause

call "%FILMCREATOR_ROOT%\launchers\quick_pipeline_test\00_clear_downstream_artifacts.bat" %*
if errorlevel 1 goto :fail

call "%FILMCREATOR_ROOT%\launchers\quick_pipeline_test\01_refresh_descriptor_enrichment.bat" %*
if errorlevel 1 goto :fail

call "%FILMCREATOR_ROOT%\launchers\quick_pipeline_test\02_refresh_prompt_preparation.bat" %*
if errorlevel 1 goto :fail

call "%FILMCREATOR_ROOT%\launchers\quick_pipeline_test\03_run_downstream_slice_test.bat" %*
if errorlevel 1 goto :fail

call "%FILMCREATOR_ROOT%\launchers\quick_pipeline_test\04_run_quality_grading.bat" %*
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
