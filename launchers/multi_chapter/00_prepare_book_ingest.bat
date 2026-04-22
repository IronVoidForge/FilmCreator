@echo off
setlocal

call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0" || goto :fail
set "PROJECT_SLUG=princess_of_mars_test"
set "BOOK_SOURCE=%FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%\01_source\book\book_input.txt"

if not exist "%FILMCREATOR_ROOT%" (
    echo Missing FilmCreator root: %FILMCREATOR_ROOT%
    pause
    exit /b 1
)

cd /d "%FILMCREATOR_ROOT%"

echo Multi-chapter ingest setup
echo.
echo Save or paste your full raw book text here before running:
echo   %BOOK_SOURCE%
echo.
echo This launcher will:
echo   - read book_input.txt
echo   - write raw_book.txt
echo   - split the book into chapter markdown files
echo   - write book_manifest.md
echo.

if not exist "%BOOK_SOURCE%" (
    echo Missing input file: %BOOK_SOURCE%
    echo Create that file and paste the full book text into it first.
    pause
    exit /b 1
)

echo Running ingest...
python -c "from pathlib import Path; from orchestrator.book_ingest import ingest_book_text; import json; root = Path(r'%FILMCREATOR_ROOT%'); project = '%PROJECT_SLUG%'; source = root / 'projects' / project / '01_source' / 'book' / 'book_input.txt'; raw = source.read_text(encoding='utf-8'); summary = ingest_book_text(project_slug=project, raw_text=raw, source_name='raw_book.txt'); print(json.dumps(summary.to_dict(), indent=2))"
if errorlevel 1 goto :fail

echo.
echo Ingest complete. Inspect:
echo   %FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%\01_source\book\raw_book.txt
echo   %FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%\01_source\book\book_manifest.md
echo   %FILMCREATOR_ROOT%\projects\%PROJECT_SLUG%\01_source\chapters\
pause
exit /b 0

:fail
echo.
echo Multi-chapter ingest setup failed.
pause
exit /b 1
