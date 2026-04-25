# Title
watch_thing Character Reference - Profile View

# ID
watch_thing_profile_view_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Profile character reference portrait, profile view with a clean silhouette and side-plane facial structure, Fierce appearance, Non-humanoid silhouette defined by multiple limbs., A fierce, multi-legged non-humanoid creature., unknown, clean neutral studio...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: character
- subject_id: watch_thing
- source_artifact_ids: CHAR_apache_warriors
- reference_mode: character_reference_sheet
- variant_name: profile_view
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: profile_view
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image
- display_name: watch_thing
- identity_descriptor: Fierce appearance, Non-humanoid silhouette defined by multiple limbs., A fierce, multi-legged non-humanoid creature., unknown
- body_descriptor: Multi-legged anatomy; non-humanoid frame.
- face_descriptor: 
- costume_descriptor: Non-humanoid silhouette defined by multiple limbs.
- posture_descriptor: 
- expression_descriptor: 
- locked_fields: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Profile View.
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
