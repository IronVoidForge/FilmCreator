# Title
arizona_quartz_vein_basin Environment Reference - Medium Spatial View

# ID
arizona_quartz_vein_basin_medium_spatial_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, medium spatial view showing foreground, midground, and background relationships, Circular basin geometry; rugged terrain with high visibility and open spaces suitable for large leaps, monumental scale, stone, metal, and weathered architectural surfaces, recognizable ridge lines, rock for...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: environment
- subject_id: arizona_quartz_vein_basin
- source_artifact_ids: ENV_aerial_battle_skies; arizona_quartz_vein_basin
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
- display_name: arizona_quartz_vein_basin
- layout_descriptor: Circular basin geometry; rugged terrain with high visibility and open spaces suitable for large leaps
- scale_descriptor: monumental scale
- architecture_descriptor: stone, metal, and weathered architectural surfaces
- landmark_descriptor: recognizable ridge lines, rock formations, and terrain silhouette
- lighting_descriptor: clear readable cinematic lighting with visible forms and depth
- mood_descriptor: grounded atmospheric adventure tone
- locked_fields: rugged terrain, rock materials, readable horizon
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: arizona quartz vein basin: Circular basin geometry; rugged terrain with high visibility and open spaces suitable for large leaps. Preserve rugged terrain, rock materials, readable horizon
- fallback_fields_used: landmark_descriptor, lighting_descriptor, mood_descriptor, locked_fields

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Medium Spatial View.
- If this prompt is later used with an image reference, treat image1 as the locked spatial reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair fallback fields used: landmark_descriptor, lighting_descriptor, mood_descriptor, locked_fields
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_aerial_battle_skies.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\environments\arizona_quartz_vein_basin.json
