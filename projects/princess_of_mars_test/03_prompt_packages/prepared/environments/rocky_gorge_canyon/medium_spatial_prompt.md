# Title
rocky_gorge_canyon Environment Reference - Medium Spatial View

# ID
rocky_gorge_canyon_medium_spatial_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, medium spatial view showing foreground, midground, and background relationships, cave mouth, rocky gorge canyon, cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-m...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: environment
- subject_id: rocky_gorge_canyon
- source_artifact_ids: ENV_ancient_cliffside_cave
- reference_mode: environment_reference_sheet
- variant_name: medium_spatial
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve geography, lighting, and anchors
- reuse_policy: reuse canonical spatial canon
- variant_policy: medium_spatial
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: environment_reference
- target_models: qwen_image; flux; z_image
- display_name: rocky_gorge_canyon
- layout_descriptor: cave mouth
- scale_descriptor: 
- architecture_descriptor: 
- landmark_descriptor: rocky gorge canyon
- lighting_descriptor: 
- mood_descriptor: 
- locked_fields: 
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: rocky gorge canyon
- fallback_fields_used: 

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Medium Spatial View.
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
