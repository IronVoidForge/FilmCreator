# Title
lorquas_ptomel_audience_chamber Environment Reference - Interior Layout

# ID
lorquas_ptomel_audience_chamber_interior_layout_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, clear interior layout with readable pathways, structure, and scale, Large scale; centered around a focal point for the presiding chieftain, monumental scale, stone, metal, and weathered architectural surfaces, clearly visible cave mouth in a rock face, strong entrance silhouette, rocky t...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: environment
- subject_id: lorquas_ptomel_audience_chamber
- source_artifact_ids: ENV_aerial_battle_skies; lorquas_ptomel_audience_chamber
- reference_mode: environment_reference_sheet
- variant_name: interior_layout
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve geography, lighting, and anchors
- reuse_policy: reuse canonical spatial canon
- variant_policy: interior_layout
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: environment_reference
- target_models: qwen_image; flux; z_image
- display_name: lorquas_ptomel_audience_chamber
- layout_descriptor: Large scale; centered around a focal point for the presiding chieftain
- scale_descriptor: monumental scale
- architecture_descriptor: stone, metal, and weathered architectural surfaces
- landmark_descriptor: clearly visible cave mouth in a rock face, strong entrance silhouette, rocky threshold
- lighting_descriptor: Dramatic and tension-filled; heavy atmosphere with shadows cast by large warriors
- mood_descriptor: Heavy, dramatic, and high-tension; suitable for trials and sudden outbursts of violence
- locked_fields: cave mouth, rock face, rocky threshold, shadowed interior
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: lorquas ptomel audience chamber: Large scale; centered around a focal point for the presiding chieftain. Preserve cave mouth, rock face, rocky threshold, shadowed interior
- fallback_fields_used: landmark_descriptor, locked_fields

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Interior Layout.
- If this prompt is later used with an image reference, treat image1 as the locked spatial reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair fallback fields used: landmark_descriptor, locked_fields
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_aerial_battle_skies.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\environments\lorquas_ptomel_audience_chamber.json
