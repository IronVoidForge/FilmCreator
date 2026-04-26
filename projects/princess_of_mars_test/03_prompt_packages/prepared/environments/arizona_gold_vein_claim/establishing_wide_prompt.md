# Title
arizona_gold_vein_claim Environment Reference - Establishing Wide

# ID
arizona_gold_vein_claim_establishing_wide_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, wide establishing reference with clear horizon, depth, and geography, rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale, cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier dese...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: environment
- subject_id: arizona_gold_vein_claim
- source_artifact_ids: ENVIRONMENT_REGISTRY_GLOBAL
- reference_mode: environment_reference_sheet
- variant_name: establishing_wide
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve geography, lighting, and anchors
- reuse_policy: reuse canonical spatial canon
- variant_policy: establishing_wide
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: environment_reference
- target_models: qwen_image; flux; z_image
- display_name: arizona_gold_vein_claim
- layout_descriptor: rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale
- scale_descriptor: rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale
- architecture_descriptor: rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale
- landmark_descriptor: 
- lighting_descriptor: rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale
- mood_descriptor: rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale
- locked_fields: rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: arizona gold vein claim
- fallback_fields_used: 

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Establishing Wide.
- If this prompt is later used with an image reference, treat image1 as the locked spatial reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- environment reference recommended input `landmark_descriptor` is missing

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\world\global\ENVIRONMENT_REGISTRY_GLOBAL.json
