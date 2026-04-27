Status: 95%

# Descriptor Prompt Normalization

## Target files

- `orchestrator/descriptor_enrichment.py`
- `orchestrator/prompt_preparation.py`
- `tests/test_descriptor_prompt_normalization.py`

## Problem

Descriptor enrichment already stores:

- `supported_field_values`
- `generated_field_values`
- `reference_repair`

But prompt prep currently allows generic generated fields to outrank stronger repaired prompt-facing values.

## Goal

Make repaired fields and production fallback values the normalized prompt-facing source.

## Required implementation

### 1. Prompt field precedence

In `orchestrator/prompt_preparation.py`, update `_prompt_field_text(...)` precedence to:

1. supported field values
2. `reference_repair`
3. generated field values
4. raw field values
5. fallback arguments

### 2. Add alias mapping

Support prompt-facing aliases such as:

- `identity_descriptor`
- `body_descriptor`
- `face_descriptor`
- `costume_descriptor`
- `posture_descriptor`
- `locked_fields`

Map them to canonical/generated/fallback names.

### 3. Descriptor ingestion of bible fallback
nIn `orchestrator/descriptor_enrichment.py`, if a bible has `visual_production_fallback`, use it to fill missing generated fields only.

Mark origin as:

```text
visual_production_fallback
```

## Do not do

- Do not move fallback data into supported fields.
- Do not erase evidence-supported values.

## Unit tests

### Test 1: repair outranks generic generated

Generated:

```text
generic body
```

Repair:

```text
specific repaired body
```

Expected prompt field:

```text
specific repaired body
```

### Test 2: supported outranks repair

Supported field present and repair also present.

Expected:

Supported value wins.

### Test 3: bible fallback fills missing generated field only

Expected:

- missing generated costume gets fallback costume
- existing supported costume unchanged

### Test command

```bat
pytest tests/test_descriptor_prompt_normalization.py -q
```
