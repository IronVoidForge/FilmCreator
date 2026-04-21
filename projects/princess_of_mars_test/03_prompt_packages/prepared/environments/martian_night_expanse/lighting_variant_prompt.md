# Title
martian_night_expanse Environment Reference - Lighting Variant

# ID
martian_night_expanse_lighting_variant_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
Film environment reference sheet, lighting variant preserving spatial layout while changing illumination, Vast desert plains with an infinite horizon, anchored spatially by two distinct moons overhead., Dual-moon illumination, Silver lunar glow, clear spatial layout, readable anchors and depth cues, no characters, n...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: environment
- subject_id: martian_night_expanse
- source_artifact_ids: ENV_martian_night_expanse
- reference_mode: environment_reference_sheet
- variant_name: lighting_variant
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve geography, lighting, and anchors
- reuse_policy: reuse canonical spatial canon
- variant_policy: lighting_variant
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: environment_reference
- target_models: qwen_image; flux; z_image

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Lighting Variant.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_martian_night_expanse.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_martian_night_expanse.md
