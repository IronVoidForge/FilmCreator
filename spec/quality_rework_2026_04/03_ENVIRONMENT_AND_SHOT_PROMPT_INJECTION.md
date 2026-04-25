# Environment and Shot Prompt Injection

## Target files

- `orchestrator/prompt_preparation.py`
- `tests/test_prompt_preparation_visual_fallbacks.py`

## Problems

1. Environment prompts receive negatives but not enough positive bucket geometry.
2. Shot prompts can mis-map image roles.
3. Shot prompts often use generic negatives only.

## Required implementation

## A. Environment bucket injection

Add helper:

```python
_environment_fallback_bucket(...)
_environment_fallback_text(...)
```

Buckets:

- `cave_or_cliffside`
- `desert_mountain`
- `interior`
- `wilderness`
- `general`

Use bucket text to fill missing:

- `architecture_descriptor`
- `scale_descriptor`
- `lighting_descriptor`
- `mood_descriptor`
- `locked_fields`

## B. Shot role repair

In `_package_for_shot(...)` ensure:

- image1 = visible primary subject identity reference
- image2 = environment reference

Never allow environment label to be written as image1 subject text.

## C. Shot positive fallback context

Add compact clause:

```text
Maintain the project visual language: <book_visual_context>
```

## D. Shot negative fallback merge

Use:

- generic negatives
- character negative terms when visible character exists
- environment negative terms when environment exists

## Unit tests

### Test 1: cave bucket selected

Input:

```text
arizona_mountain_cave
```

Expected bucket:

```text
cave_or_cliffside
```

### Test 2: shot role mapping

Visible subject = protagonist
Environment = arizona mountain cave

Expected prompt contains:

```text
Use image1 ... protagonist
Use image2 ... arizona mountain cave
```

Expected prompt does NOT contain:

```text
subject from image1 is arizona mountain cave
```

### Test 3: shot negatives merged

Expected negative prompt includes examples from fallback terms plus generic negatives.

### Test command

```bat
pytest tests/test_prompt_preparation_visual_fallbacks.py -q
```