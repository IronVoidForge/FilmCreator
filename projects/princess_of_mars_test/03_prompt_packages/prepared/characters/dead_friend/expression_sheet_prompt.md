# Title
dead_friend Character Reference - Expression Sheet

# ID
dead_friend_expression_sheet_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
Film character reference sheet, expression sheet showing several clear emotional beats without changing costume, deceased individual, readable production detail, lean athletic build, decisive, efficient movement, clean neutral studio background, clear silhouette, consistent costume layers, consistent facial structur...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: character
- subject_id: dead_friend
- source_artifact_ids: CHAR_dead_friend
- reference_mode: character_reference_sheet
- variant_name: expression_sheet
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: expression_sheet
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Expression Sheet.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_dead_friend.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_dead_friend.md
