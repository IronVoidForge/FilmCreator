# Title
circular_moss_basin Environment Reference - Interior Layout

# ID
circular_moss_basin_interior_layout_prompt

# Purpose
Prepare a compact environment reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked spatial reference. Environment reference sheet, clear interior layout with readable pathways, structure, and scale, described environment with stable spatial anchors, clear spatial layout, readable anchors and depth cues, no characters, no text, no watermark.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: environment
- subject_id: circular_moss_basin
- source_artifact_ids: ENV_ancient_cliffside_cave
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
- display_name: circular_moss_basin
- layout_descriptor: circular_moss_basin; incubator_enclosure; yellowish_moss_floor; incubator_interior; glass_roof_zone; vegetation_hiding_spot; transit_pathway; inner_moss_zone; enclosure_wall_boundary; far_side_landing_zone
- scale_descriptor: 
- architecture_descriptor: 
- landmark_descriptor: 
- lighting_descriptor: 
- mood_descriptor: 
- locked_fields: 

# Continuity Notes
- Preserve geographic layout, scale, lighting, and recurring anchors.
- Variant: Interior Layout.
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

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\environments\ENV_ancient_cliffside_cave.json
