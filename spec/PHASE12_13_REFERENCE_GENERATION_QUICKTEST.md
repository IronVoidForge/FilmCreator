Status: 90%

# Phase 12/13 Reference Generation Quicktest Spec

## Goal

Add the Phase 12 and Phase 13 reference generation launchers to the new quicktest folder:

```text
launchers/quicktest_phase/
```

These launchers should modernize the old quick pipeline reference-generation BATs and make them work with the current CLI shape.

The new files should be one per phase:

```text
launchers/quicktest_phase/PHASE12_CHARACTER_REFERENCE_GENERATION_CHAPTERS.bat
launchers/quicktest_phase/PHASE13_ENVIRONMENT_REFERENCE_GENERATION_CHAPTERS.bat
```

Do not replace the existing downstream quicktest files for dialogue/descriptor phases. Use the `PHASE12_` and `PHASE13_` prefixes to avoid confusion with existing numbered files such as `12_DIALOGUE_TIMELINE_CHAPTERS.bat` and `13_DESCRIPTOR_ENRICHMENT_CHAPTERS.bat`.

## Existing old implementation to salvage

The old quick pipeline files are:

```text
launchers/quick_pipeline_test/10_run_character_reference_generation.bat
launchers/quick_pipeline_test/11_run_environment_reference_generation.bat
```

They already run the practical Phase 12/13 generation flow:

- start clean ComfyUI on port `8190`
- set FilmCreator Comfy env vars
- run a small validation slice
- default project to `princess_of_mars_test`
- default chapters to `2-3`
- default limit to `2`
- run four prompt variants for comparison

## Current Phase 12/13 Python support

At the working ref used during planning, the repo already has:

```text
orchestrator/character_references.py
orchestrator/environment_references.py
orchestrator/reference_assets.py
```

The CLI also exposes planning, generation, registration, approval, rejection, and locking commands:

```text
plan-character-references
generate-character-references
register-character-reference-candidate
approve-character-reference
reject-character-reference
lock-character-reference

plan-environment-references
generate-environment-references
register-environment-reference-candidate
approve-environment-reference
reject-environment-reference
lock-environment-reference
```

The generation functions in the modules already accept `chapters: str | None = None` and use chapter selectors to filter prompt-prep entries by `chapter_mentions`.

The likely gap is in `orchestrator/cli.py`: the argparse definitions for `generate-character-references` and `generate-environment-references` may not expose `--chapters`, even though the underlying functions support it.

## Required CLI patch

Patch `orchestrator/cli.py` if needed.

### Character generation parser

Find the parser for:

```python
generate-character-references
```

Ensure it includes:

```python
crg.add_argument("--chapters", type=str, default=None)
```

The dispatch into `run_character_reference_generation(...)` must pass:

```python
chapters=args.chapters,
```

The final command must support:

```powershell
python -m orchestrator generate-character-references princess_of_mars_test --chapters 2-3 --variant bust_portrait --limit 1 --test-slice --execute --prompt-variant raw
```

### Environment generation parser

Find the parser for:

```python
generate-environment-references
```

Ensure it includes:

```python
erg.add_argument("--chapters", type=str, default=None)
```

The dispatch into `run_environment_reference_generation(...)` must pass:

```python
chapters=args.chapters,
```

The final command must support:

```powershell
python -m orchestrator generate-environment-references princess_of_mars_test --chapters 2-3 --variant establishing_wide --limit 1 --test-slice --execute --prompt-variant raw
```

## New quicktest BAT conventions

Both new BATs should follow the new quicktest folder conventions.

Arguments:

```text
%1 = PROJECT_SLUG, default princess_of_mars_test
%2 = CHAPTERS, default 2-3
%3 = LIMIT, default 2
```

Do not use interactive `set /p` prompts.

Use the existing shared resolver:

```bat
call "%~dp0..\_shared\resolve_filmcreator_root.bat" "%~dp0"
```

Then:

```bat
cd /d "%FILMCREATOR_ROOT%"
```

Start clean ComfyUI exactly like the old quick pipeline:

```bat
call "%~dp0..\quick_pipeline_test\_shared\start_clean_comfyui_8190.bat"
```

Then set:

```bat
set "FILMCREATOR_COMFY_BASE_URL=http://127.0.0.1:8190"
set "FILMCREATOR_COMFY_INPUT_DIR=%FILMCREATOR_ROOT%\.comfy_clean\input"
set "FILMCREATOR_COMFY_OUTPUT_DIR=%FILMCREATOR_ROOT%\.comfy_clean\output"
```

If the relative path to `start_clean_comfyui_8190.bat` is wrong in the local tree, fix it during implementation, but do not duplicate the helper.

## Phase 12 BAT

Create:

```text
launchers/quicktest_phase/PHASE12_CHARACTER_REFERENCE_GENERATION_CHAPTERS.bat
```

It should run the character reference generation validation slice for `bust_portrait`.

Prompt variants:

```text
raw
character_clean
character_readability
character_polish
```

Commands:

```bat
python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant raw
python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant character_clean
python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant character_readability
python -m orchestrator generate-character-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant bust_portrait --limit "%LIMIT%" --test-slice --execute --prompt-variant character_polish
```

Stop immediately on any nonzero exit code.

## Phase 13 BAT

Create:

```text
launchers/quicktest_phase/PHASE13_ENVIRONMENT_REFERENCE_GENERATION_CHAPTERS.bat
```

It should run the environment reference generation validation slice for `establishing_wide`.

Prompt variants:

```text
raw
environment_clean
environment_readability
environment_polish
```

Commands:

```bat
python -m orchestrator generate-environment-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant establishing_wide --limit "%LIMIT%" --test-slice --execute --prompt-variant raw
python -m orchestrator generate-environment-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant establishing_wide --limit "%LIMIT%" --test-slice --execute --prompt-variant environment_clean
python -m orchestrator generate-environment-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant establishing_wide --limit "%LIMIT%" --test-slice --execute --prompt-variant environment_readability
python -m orchestrator generate-environment-references "%PROJECT_SLUG%" --chapters "%CHAPTERS%" --variant establishing_wide --limit "%LIMIT%" --test-slice --execute --prompt-variant environment_polish
```

Stop immediately on any nonzero exit code.

## Dependency expectations

These Phase 12/13 generation launchers require prepared prompt packages from Phase 11.5.

Before running them, the user should have already run either the full overnight pipeline or at least:

```powershell
cmd /c launchers\quicktest_phase\RUN_13_TO_14_CHAPTER_SLICE.bat
```

That ensures descriptor enrichment and prompt preparation artifacts exist for the selected chapter slice.

## Static validation before running generation

Do not run generation while another full pipeline is running.

Safe static checks:

```powershell
python -m orchestrator generate-character-references --help
python -m orchestrator generate-environment-references --help
```

Verify both help outputs include:

```text
--chapters
```

Then inspect BAT contents without executing:

```powershell
findstr /S /I /N "generate-character-references generate-environment-references --chapters start_clean_comfyui_8190" .\launchers\quicktest_phase\*.bat
```

## First real run after the full pipeline is done

Use limit `1` first because each BAT runs four prompt variants.

```powershell
cmd /c launchers\quicktest_phase\PHASE12_CHARACTER_REFERENCE_GENERATION_CHAPTERS.bat princess_of_mars_test 2-3 1
```

Then:

```powershell
cmd /c launchers\quicktest_phase\PHASE13_ENVIRONMENT_REFERENCE_GENERATION_CHAPTERS.bat princess_of_mars_test 2-3 1
```

## Later overnight integration

Do not wire these into the overnight resume BAT until the tiny slice succeeds.

Once validated, the overnight runner can add reference generation after quality grading, but should probably run full-project mode without `--chapters` when no chapter slice is provided and chapter-slice mode when `CHAPTERS` is passed.

Do not add overnight integration in the first implementation pass.

