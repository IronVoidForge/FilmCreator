# Title
bull_ape Character Reference - Full Body Neutral

# ID
bull_ape_full_body_neutral_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Full-body character reference portrait, full-body neutral standing reference with balanced posture, Humanoid ape anatomy, Extreme height (10-15ft), Four-armed anatomy, Massive, four-armed primate silhouette., clean neutral studio background, clear silhouet...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: character
- subject_id: bull_ape
- source_artifact_ids: CHAR_apache_warriors
- reference_mode: character_reference_sheet
- variant_name: full_body_neutral
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: full_body_neutral
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image
- display_name: bull_ape
- identity_descriptor: Humanoid ape anatomy, Extreme height (10-15ft), Four-armed anatomy, Massive, four-armed primate silhouette.
- body_descriptor: Massive, immense strength; 10-15ft tall.
- face_descriptor: 
- costume_descriptor: Massive, four-armed primate silhouette.
- posture_descriptor: 
- expression_descriptor: 
- locked_fields: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Full Body Neutral.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- character reference recommended input `expression_descriptor` is missing
- character reference recommended input `face_descriptor` is missing
- character reference recommended input `locked_fields` is missing
- character reference recommended input `posture_descriptor` is missing

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
