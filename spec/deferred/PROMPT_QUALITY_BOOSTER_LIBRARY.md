# Deferred: Prompt Quality Booster Library

## Purpose

Create reusable bundles of prompt modifiers that can be selectively appended to Phase 12 / 13 / 14 prompt packages as controlled variations.

The goal is not random keyword stuffing. The goal is structured A/B testing of prompt additives commonly reported as useful in diffusion workflows.

## Principles

- Bundles should be optional and trackable.
- Use small coherent bundles, not giant noisy lists.
- Preserve subject identity and scene intent first.
- Prefer clean readability for references.
- Separate aesthetic boosters from technical boosters.
- Every bundle used in generation should be recorded in candidate metadata.

## Bundle Format

```json
{
  "bundle_id": "clean_reference_v1",
  "category": "reference",
  "positive": ["high quality", "clean studio lighting"],
  "negative": ["underexposed", "text"],
  "notes": "Use for character and environment references."
}
```

## Recommended Initial Bundles

These are conservative bundles based on common diffusion prompting practice.

---

## 1. clean_reference_v1

Best for Phase 12 / 13 references.

### Positive

- high quality
- clean studio lighting
- even soft lighting
- sharp focus
- visible details
- neutral background
- production reference sheet

### Negative

- underexposed
- harsh shadow
- silhouette
- text
- watermark
- cropped subject
- blurry

---

## 2. portrait_face_clarity_v1

Best for bust portraits and face approval rounds.

### Positive

- detailed face
n- clear eyes
- symmetrical features
- realistic skin detail
- crisp facial structure
- centered portrait

### Negative

- deformed face
- extra eyes
- asymmetrical face
- blurry face
- obscured face

---

## 3. costume_readability_v1

Best when clothing detail matters.

### Positive

- visible costume layers
- clear fabric detail
- readable accessories
- defined seams and straps
- clean silhouette

### Negative

- muddy clothing
- merged clothing shapes
- hidden torso
- crushed blacks

---

## 4. environment_spatial_clarity_v1

Best for environment references.

### Positive

- readable layout
- clear depth
- defined foreground midground background
- coherent architecture
- visible landmarks
- balanced lighting

### Negative

- cluttered composition
- confusing layout
- muddy perspective
- overdark shadows
- blown highlights

---

## 5. cinematic_polish_v1

Optional aesthetic pass after references are solved.

### Positive

- cinematic composition
- volumetric atmosphere
- rich detail
- polished rendering
- dramatic depth

### Negative

- flat image
- low detail

Use sparingly. Can hurt clean reference readability.

---

## Terms To Treat As Experimental

These should be tested, not assumed universally helpful:

- masterpiece
n- best quality
- immaculate
- award winning
- trending on artstation
- ultra detailed

They may help some checkpoints and hurt others.
Always track when used.

## Integration Plan

Prompt preparation should support:

```json
{
  "booster_bundles": [
    "clean_reference_v1",
    "portrait_face_clarity_v1"
  ]
}
```

Generation should then append bundle positives to positive prompts and bundle negatives to negative prompts.

## Tracking Requirements

Every candidate should record:

- booster bundle IDs used
n- workflow ID
- seed
- model
- manual rank
- final approval decision

## Suggested First Tests

### Character Bust A/B

A: base prompt only  
B: base + clean_reference_v1 + portrait_face_clarity_v1

### Full Body A/B

A: base only  
B: base + clean_reference_v1 + costume_readability_v1

### Environment A/B

A: base only  
B: base + clean_reference_v1 + environment_spatial_clarity_v1

## Non-Goals

- Massive keyword spam.
- Different bundles per sentence.
- Auto-optimizing without human review.

## Acceptance Criteria

- Bundles are reusable and versioned.
- Each generation records bundles used.
- Rankings can later reveal which bundles actually help.
