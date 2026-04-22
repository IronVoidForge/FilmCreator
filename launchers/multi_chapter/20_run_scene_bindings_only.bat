@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    exit /b 1
)

pushd "%FILMCREATOR_ROOT%" >nul

set "DEFAULT_SLUG=princess_of_mars_test"
set /p PROJECT_SLUG=Project slug [%DEFAULT_SLUG%]:
if "%PROJECT_SLUG%"=="" set "PROJECT_SLUG=%DEFAULT_SLUG%"
set /p CHAPTERS=Chapters filter [all]:

echo.
echo ========================================
echo FilmCreator Scene Binding Synthesis
echo ========================================
echo.
echo Project slug: %PROJECT_SLUG%
echo Repo root: %FILMCREATOR_ROOT%
echo.

set "CHAPTER_ARGS="
if not "%CHAPTERS%"=="" set "CHAPTER_ARGS=--chapters %CHAPTERS%"

python -m orchestrator synthesize-scene-bindings %PROJECT_SLUG% --force %CHAPTER_ARGS%
if errorlevel 1 goto :fail

echo.
echo Scene binding synthesis complete.
goto :done

:fail
echo.
echo Scene binding synthesis failed.
pause
popd >nul
exit /b 1

:done
popd >nul
echo.
pause
exit /b 0
