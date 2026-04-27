# Title
barsoomian_wilderness Environment Reference - Lighting Variant

# ID
barsoomian_wilderness_lighting_variant_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, lighting variant preserving spatial layout while changing illumination, No specific visual details are provided in the current evidence. The environment is identified as a Barsoomian wilderness, but physical characteristics remain undefined, monumental scale, stone, metal, and weathered...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: environment
- subject_id: barsoomian_wilderness
- source_artifact_ids: ENV_aerial_battle_skies; barsoomian_wilderness
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
- display_name: barsoomian_wilderness
- layout_descriptor: No specific visual details are provided in the current evidence. The environment is identified as a Barsoomian wilderness, but physical characteristics remain undefined
- scale_descriptor: monumental scale
- architecture_descriptor: stone, metal, and weathered architectural surfaces
- landmark_descriptor: recognizable ridge lines, rock formations, and terrain silhouette
- lighting_descriptor: rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale
- mood_descriptor: rugged desert mountain terrain, dry scrub, weathered rock, clear horizon, readable distance and scale
- locked_fields: rugged terrain, rock materials, readable horizon
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: barsoomian wilderness
- fallback_fields_used: landmark_descriptor, locked_fields

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Lighting Variant.
- If this prompt is later used with an image reference, treat image1 as the locked spatial reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair fallback fields used: landmark_descriptor, locked_fields
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_aerial_battle_skies.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\environments\barsoomian_wilderness.json
