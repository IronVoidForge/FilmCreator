# Title
zodangan_palace_quarters Environment Reference - Detail Focus

# ID
zodangan_palace_quarters_detail_focus_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, detail-focused view on a recurring anchor or landmark, clear room or chamber layout, foreground midground background separation, pathways, anchor objects, visible scale, cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, generic meadow, open grassy field, rolling green hills, no cave, hidden landmark, modern road, cars, modern buildings

# Inputs
- subject_kind: environment
- subject_id: zodangan_palace_quarters
- source_artifact_ids: ENVIRONMENT_REGISTRY_GLOBAL
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
- display_name: zodangan_palace_quarters
- layout_descriptor: clear room or chamber layout, foreground midground background separation, pathways, anchor objects, visible scale
- scale_descriptor: clear room or chamber layout, foreground midground background separation, pathways, anchor objects, visible scale
- architecture_descriptor: clear room or chamber layout, foreground midground background separation, pathways, anchor objects, visible scale
- landmark_descriptor: 
- lighting_descriptor: clear room or chamber layout, foreground midground background separation, pathways, anchor objects, visible scale
- mood_descriptor: clear room or chamber layout, foreground midground background separation, pathways, anchor objects, visible scale
- locked_fields: clear room or chamber layout, foreground midground background separation, pathways, anchor objects, visible scale
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: zodangan palace quarters
- fallback_fields_used: 

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Detail Focus.
- If this prompt is later used with an image reference, treat image1 as the locked spatial reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- environment reference recommended input `landmark_descriptor` is missing

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\world\global\ENVIRONMENT_REGISTRY_GLOBAL.json
