# Quicktest Phase Launchers

These BATs are small, phase-by-phase test launchers for the FilmCreator downstream pipeline.

They mirror the trusted command sequence in:

`launchers/RUN_PRINCESS_FULL_OVERNIGHT_TAXONOMY_RESUME.bat`

## Defaults

All BATs accept:

```text
%1 = PROJECT_SLUG
%2 = CHAPTERS
```

Defaults:

```text
PROJECT_SLUG = princess_of_mars_test
CHAPTERS = 2-3
```

Example:

```powershell
cmd /c launchers\quicktest_phase\11_SHOT_PACKAGES_CHAPTERS.bat
```

Example with overrides:

```powershell
cmd /c launchers\quicktest_phase\11_SHOT_PACKAGES_CHAPTERS.bat my_project 4-5
```

## Scope

The trusted overnight BAT only chapter-scopes phases 09-14.

Project-wide phases:

- 03 Character taxonomy
- 04 Identity refinement plan
- 05 Identity refinement apply
- 06 Character bibles
- 07 Environment bibles
- 08 Visual fallbacks
- 15 Quality grading

Chapter-scoped phases:

- 09 Scene contracts
- 10 Scene bindings
- 11 Shot packages
- 12 Dialogue timeline
- 13 Descriptor enrichment
- 14 Prompt preparation

Project-wide BATs accept CHAPTERS for interface consistency, but do not pass `--chapters`.

## Cleanup

These quicktest BATs do not delete artifacts.

Use cleanup separately when needed:

```powershell
cmd /c launchers\cleanup\CLEAR_PRINCESS_DOWNSTREAM_ARTIFACTS_FOR_REFINEMENT_TEST.bat princess_of_mars_test DRY_RUN
cmd /c launchers\cleanup\CLEAR_PRINCESS_DOWNSTREAM_ARTIFACTS_FOR_REFINEMENT_TEST.bat princess_of_mars_test
```

Then type:

```text
DELETE
```

## Recommended use

If you changed scene contract or scene binding logic:

```powershell
cmd /c launchers\quicktest_phase\RUN_09_TO_14_CHAPTER_SLICE.bat
```

If you changed shot planning, dialogue, descriptors, or prompt prep:

```powershell
cmd /c launchers\quicktest_phase\RUN_11_TO_14_CHAPTER_SLICE.bat
```

If you changed only descriptor enrichment or prompt preparation:

```powershell
cmd /c launchers\quicktest_phase\RUN_13_TO_14_CHAPTER_SLICE.bat
```

If you changed quality grading:

```powershell
cmd /c launchers\quicktest_phase\15_QUALITY_GRADING.bat
```

Remember: quality grading is currently project-wide.
