# Title
desolate_martian_wasteland Environment Reference - Time of Day Variant

# ID
desolate_martian_wasteland_time_of_day_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, same place rendered at a different time of day while preserving canon, Immense scale with vast arid plains and widely dispersed ruins, monumental scale, stone, metal, and weathered architectural surfaces, clear landmark or anchor feature defining the location, Harsh lighting contributing...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: environment
- subject_id: desolate_martian_wasteland
- source_artifact_ids: ENV_aerial_battle_skies; desolate_martian_wasteland
- reference_mode: environment_reference_sheet
- variant_name: time_of_day
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve geography, lighting, and anchors
- reuse_policy: reuse canonical spatial canon
- variant_policy: time_of_day
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: environment_reference
- target_models: qwen_image; flux; z_image
- display_name: desolate_martian_wasteland
- layout_descriptor: Immense scale with vast arid plains and widely dispersed ruins
- scale_descriptor: monumental scale
- architecture_descriptor: stone, metal, and weathered architectural surfaces
- landmark_descriptor: clear landmark or anchor feature defining the location
- lighting_descriptor: Harsh lighting contributing to a sense of isolation
- mood_descriptor: Lonely, isolating, and disorienting under a vast sky
- locked_fields: core landmark, scale, and material identity
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: desolate martian wasteland: Immense scale with vast arid plains and widely dispersed ruins. Preserve core landmark, scale, and material identity
- fallback_fields_used: landmark_descriptor, locked_fields

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Time of Day Variant.
- If this prompt is later used with an image reference, treat image1 as the locked spatial reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair fallback fields used: landmark_descriptor, locked_fields
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_aerial_battle_skies.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\environments\desolate_martian_wasteland.json
