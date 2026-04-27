Status: 85%

# Quality Grading Calibration

## Target files

- `orchestrator/quality_grading.py`
- tests covering grading logic

## Problems

- Prompt packages over-score despite semantic issues.
- Empty dialogue timelines are treated as failures even when silence is intended.

## Required implementation

## A. Prompt package semantic checks

A prompt package should not receive A when any are true:

- review notes mention missing required subject anchor
n- reference conflict present
- image1 subject contradicts visible primary subject
- visible subject exists but positive prompt omits it
- shot negatives missing fallback terms
- prompt readiness score < 80
- environment prompt missing architecture/lighting/mood/scale descriptors

When triggered:

- lower grade cap to C or below
- set rerun recommended
- rerun stage = `run-prompt-preparation`

## B. Dialogue silent mode

If a dialogue timeline has no events but is explicitly silent:

```json
"no_dialogue_expected": true
```

Do not rerun for missing dialogue.

If dialogue is expected and no events exist, keep rerun behavior.

## Unit tests

### Test 1: prompt with missing subject anchor not A

### Test 2: prompt readiness 76 cannot be A

### Test 3: silent timeline passes
n### Test 4: expected-dialogue empty timeline reruns

### Test command

```bat
pytest tests/test_quality_grading.py -q
```
