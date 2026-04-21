# Title
young_martian Character Reference - Action Pose

# ID
young_martian_action_pose_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
Film character reference sheet, dynamic action pose that preserves anatomy, costume, and identity, [], No visual data provided in the evidence., unknown, clean neutral studio background, clear silhouette, consistent costume layers, consistent facial structure, no narrative action, no text, no watermark.

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: character
- subject_id: young_martian
- source_artifact_ids: CHAR_young_martian
- reference_mode: character_reference_sheet
- variant_name: action_pose
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: action_pose
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Action Pose.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_young_martian.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_young_martian.md
