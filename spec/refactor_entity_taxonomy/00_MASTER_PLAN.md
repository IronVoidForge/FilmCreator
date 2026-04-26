# Entity Taxonomy Refactor Master Plan

Base branch point: `c70a6828feb749613133f641ab6e3a623047d934`.

## Critical rule

Runtime logic must be book-agnostic. Do not hardcode project/book/entity names such as `john_carter`, `protagonist`, `Barsoom`, `Green Martian`, `martian_leader`, or `chieftain` as universal rules.

Use structured evidence instead:

- direct identity evidence
- direct body/morphology evidence
- costume/equipment evidence
- associated entity evidence
- alias/role evidence
- confidence
- source refs

## Problem

The current `visual_production_fallback` classifier is trying to infer entity taxonomy too late from mixed prose. It can confuse associated entities with the entity itself, such as treating a humanoid who rides a mount as a quadruped.

Fallback should not be the primary source of identity/type truth.

## Source of truth hierarchy

1. Source text excerpts / paragraph windows
2. Chapter-level structured extraction
3. Chapter summary
4. Character registry aggregation
5. Character taxonomy artifact
6. Character bible
7. Visual production fallback
8. Descriptor enrichment
9. Prompt package
10. Image job

## Specs in this folder

1. `01_FALLBACK_SAFETY_PATCH.md`
   - Remove hardcoded/book-specific fallback rules.
   - Make fallback conservative until taxonomy exists.

2. `02_CHAPTER_ENTITY_EXTRACTION.md`
   - Upgrade chapter summary/extraction outputs with entity type hints, morphology, confidence, and associated entity separation.

3. `03_CHARACTER_TAXONOMY_STAGE.md`
   - Add first-class character taxonomy artifacts and CLI command.

4. `04_WORLD_REFINEMENT_TAXONOMY_INTEGRATION.md`
   - Extend existing merge/refinement stage with taxonomy and alias candidate evidence.

5. `05_CHARACTER_BIBLE_TAXONOMY_INTEGRATION.md`
   - Feed taxonomy and associated entity evidence into character bibles.

6. `06_FALLBACK_FROM_TAXONOMY.md`
   - Make fallback derive buckets from taxonomy instead of messy prose.

7. `07_QUALITY_GRADING_RERUN_ROUTING.md`
   - Add contradiction checks and stage-specific rerun recommendations.

8. `08_IMPLEMENTATION_ORDER_AND_VALIDATION.md`
   - Safe order of implementation, tests, and validation commands.
