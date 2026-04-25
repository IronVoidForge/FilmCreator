# Title
deep_space_void Environment Reference - Detail Focus

# ID
deep_space_void_detail_focus_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, detail-focused view on a recurring anchor or landmark, rocky gorge canyon, deep space void, cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weath...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: environment
- subject_id: deep_space_void
- source_artifact_ids: ENV_ancient_cliffside_cave
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
- display_name: deep_space_void
- layout_descriptor: rocky gorge canyon
- scale_descriptor: 
- architecture_descriptor: 
- landmark_descriptor: deep space void
- lighting_descriptor: 
- mood_descriptor: 
- locked_fields: 
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: deep space void
- fallback_fields_used: 

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Detail Focus.
- If this prompt is later used with an image reference, treat image1 as the locked spatial reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- environment reference recommended input `architecture_descriptor` is missing
- environment reference recommended input `lighting_descriptor` is missing
- environment reference recommended input `locked_fields` is missing
- environment reference recommended input `mood_descriptor` is missing
- environment reference recommended input `scale_descriptor` is missing

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_ancient_cliffside_cave.json
