Status: 85%

# 07 - Quality Grading Rerun Routing

## Files
- `orchestrator/quality_grading.py`
- `tests/test_quality_grading.py`

## Add contradiction checks
- taxonomy human + fallback non-human
- taxonomy humanoid + fallback quadruped
- context_only + render prompt package
- alias candidate rendered as separate canonical character

## Rerun recommendations
- taxonomy missing/conflict -> synthesize-character-taxonomy
- bible missing taxonomy -> synthesize-character-bibles
- fallback contradiction -> repair bibles/fallback
- prompt contradiction -> run-prompt-preparation

