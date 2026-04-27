Status: 70%

# Smart Resume Validation

## Current behavior

- Smart resume skip is sentinel-file based only
- Sentinel-only skip is too shallow

## Problem

Current resume logic checks for sentinel files but does not validate artifact completeness before skipping stages.

## Solution

Future resume should validate artifact completeness before skipping.

## Implementation approach

- Validation should be done in Python, not complex BAT JSON parsing
- Each stage should have focused validation logic

## Visual fallback skip validation

Should validate:
- source_title
- book_visual_context
- character_fallbacks
- environment_fallbacks
- negative_terms
- context_digest/source_context_files

## Descriptor skip validation

Should validate:
- descriptor index count
- expected CH002/CH003 descriptors

## Prompt prep skip validation

Should validate:
- prompt index count
- subject_kind mix
- variants
- non-empty prompt files

## Quality grading skip validation

Should validate:
- total_records
- family_summaries
- rerun queue

## Testing strategy

Tests should be unit/focused tests, not full pipeline reruns.

