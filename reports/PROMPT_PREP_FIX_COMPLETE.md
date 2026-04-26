# Prompt Preparation Visual Fallbacks Fix - COMPLETE

## Issue Fixed
**NameError: name 'visual_fallbacks' is not defined**

The crash occurred in `_package_for_character()` and `_package_for_environment()` because they referenced `visual_fallbacks` as a free variable without receiving it as a parameter.

## Changes Made

### 1. Updated imports (line 16-21)
Added missing imports:
- `run_visual_fallback_synthesis`
- `visual_fallback_path`

### 2. Added helper function (line 551-555)
```python
def _ensure_visual_fallbacks(project_slug: str, project_dir: Path) -> dict[str, Any]:
    path = visual_fallback_path(project_dir)
    if not path.exists():
        run_visual_fallback_synthesis(project_slug, force=False)
    return load_visual_fallbacks(project_dir)
```

This ensures VISUAL_FALLBACKS.json exists before loading it.

### 3. Updated run_prompt_preparation (line 2065)
Added after `project_dir = create_project(project_slug)`:
```python
visual_fallbacks = _ensure_visual_fallbacks(project_slug, project_dir)
```

### 4. Updated _package_for_character signature (line 1258)
Added parameter:
```python
visual_fallbacks: dict[str, Any],
```

### 5. Updated _package_for_environment signature (line 1425)
Added parameter:
```python
visual_fallbacks: dict[str, Any],
```

### 6. Updated call sites (lines 2169, 2232)
Both calls now pass:
```python
visual_fallbacks=visual_fallbacks,
```

## Verification

✅ Compilation successful: `python -m compileall orchestrator\prompt_preparation.py`
✅ All visual_fallbacks references properly scoped (no free variables)
✅ Prompt prep now owns its visual fallback dependency
✅ Missing VISUAL_FALLBACKS.json will be auto-generated

## Expected Behavior

When resume BAT runs:
1. SKIP: 04.5 Visual fallback synthesis (sentinel exists)
2. SKIP: 05 Descriptor enrichment (sentinel exists)
3. START: 06 Prompt preparation
   - Auto-loads existing VISUAL_FALLBACKS.json
   - Or auto-generates if missing
   - Completes successfully
4. START: 07 Quality grading

## Files Modified
- `orchestrator/prompt_preparation.py` (6 surgical edits)

## Next Steps
Run the smart resume BAT:
```bat
C:\FilmCreator_MC\launchers\quick_pipeline_test\00_run_quick_pipeline_test_resume_from_045.bat
```
