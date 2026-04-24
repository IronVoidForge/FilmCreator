# Title
former_self Character Reference - Bust Portrait

# ID
former_self_bust_portrait_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Bust character reference portrait, bust portrait with head, shoulders, and facial structure readable, readable production detail, lean athletic build, decisive, efficient movement, male, clean neutral studio background, clear silhouette, consistent costume..., high quality, clean character reference image, neutral background, even soft lighting, sharp subject detail, clear readable silhouette, clear facial structure, visible eyes, balanced facial lighting, clean portrait detail, visible body proportions, clear posture, defined limbs, consistent anatomy, visible outfit details, clear clothing layers, defined accessories, clean fabric detail, refined rendering, clean contrast, polished detail

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, underexposed, harsh shadow, silhouette, cropped subject, text, watermark, obscured face, blurry face, deformed face, asymmetrical face, bad anatomy, extra limbs, cropped body, twisted proportions, muddy clothing, merged clothing shapes, hidden torso, crushed blacks, flat image, low detail

# Inputs
- subject_kind: character
- subject_id: former_self
- source_artifact_ids: CHAR_apache_warriors; former_self
- reference_mode: character_reference_sheet
- variant_name: bust_portrait
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: bust_portrait
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image
- display_name: former_self
- identity_descriptor: readable production detail, lean athletic build, decisive, efficient movement, male
- body_descriptor: unknown
- face_descriptor: 
- costume_descriptor: unknown
- posture_descriptor: 
- expression_descriptor: 
- locked_fields: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Bust Portrait.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- character reference recommended input `expression_descriptor` is missing
- character reference recommended input `face_descriptor` is missing
- character reference recommended input `locked_fields` is missing
- character reference recommended input `posture_descriptor` is missing
- Prompt boosters: variant=character_polish bundles=character_reference_clean_v1, character_face_readability_v1, character_body_readability_v1, character_costume_readability_v1, character_reference_polish_v1

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\former_self.json
