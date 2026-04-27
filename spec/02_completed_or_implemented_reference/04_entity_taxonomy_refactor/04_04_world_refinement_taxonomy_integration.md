Status: 85%

# 04 - World Refinement Taxonomy Integration

## Goal
Use taxonomy in existing merge/alias refinement.

## Files
- `orchestrator/world_refinement.py`
- `tests/unit/test_world_refinement.py`

## Required changes
1. Replace book-specific weak-name lists with generic role-label heuristics.
2. Include taxonomy summaries in candidate evidence.
3. Use alias candidates from taxonomy.
4. Block auto-merge on type conflicts:
   - human vs animal
n- group vs individual
- object vs person
5. Low confidence => human review.

## Tests
- Role label becomes review candidate
- Proper alias can merge
- Human vs animal blocks merge

