# Title
arizona_mountain_cave Environment Reference - Establishing Wide

# ID
arizona_mountain_cave_establishing_wide_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, wide establishing reference with clear horizon, depth, and geography, described environment with stable spatial anchors, clear spatial layout, readable anchors and depth cues, no characters, no text, no watermark., high quality, clean environment reference, balanced lighting, sharp environmental detail, clear spatial layout, readable foreground midground background, coherent scale, clear depth, visible landmarks, defined structures, recognizable environmental anchors, refined rendering, clean atmosphere, polished detail

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, underexposed, overexposed, text, watermark, confusing layout, muddy perspective, flat depth, hidden landmarks, cluttered composition, low detail, muddy image

# Inputs
- subject_kind: environment
- subject_id: arizona_mountain_cave
- source_artifact_ids: ENV_ancient_cliffside_cave
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
- display_name: arizona_mountain_cave
- layout_descriptor: cave floor contact zone; mid-air vapor layer; arizona_mountain_cave_floor; arizona_mountain_cave_shadows
- scale_descriptor: 
- architecture_descriptor: 
- landmark_descriptor: 
- lighting_descriptor: 
- mood_descriptor: 
- locked_fields: 

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Establishing Wide.
- If this prompt is later used with an image reference, treat image1 as the locked spatial reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- environment reference recommended input `architecture_descriptor` is missing
- environment reference recommended input `landmark_descriptor` is missing
- environment reference recommended input `lighting_descriptor` is missing
- environment reference recommended input `locked_fields` is missing
- environment reference recommended input `mood_descriptor` is missing
- environment reference recommended input `scale_descriptor` is missing
- Prompt boosters: variant=environment_polish bundles=environment_reference_clean_v1, environment_spatial_readability_v1, environment_landmark_readability_v1, environment_reference_polish_v1

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_ancient_cliffside_cave.json
