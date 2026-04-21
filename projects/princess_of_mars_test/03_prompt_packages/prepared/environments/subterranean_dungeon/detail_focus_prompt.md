# Title
subterranean_dungeon Environment Reference - Detail Focus

# ID
subterranean_dungeon_detail_focus_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
Film environment reference sheet, detail-focused view on a recurring anchor or landmark, Psychological., Unknown., None documented, clear spatial layout, readable anchors and depth cues, no characters, no text, no watermark.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: environment
- subject_id: subterranean_dungeon
- source_artifact_ids: ENV_subterranean_dungeon
- reference_mode: environment_reference_sheet
- variant_name: detail_focus
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve geography, lighting, and anchors
- reuse_policy: reuse canonical spatial canon
- variant_policy: detail_focus
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: environment_reference
- target_models: qwen_image; flux; z_image

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Detail Focus.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_subterranean_dungeon.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_subterranean_dungeon.md
