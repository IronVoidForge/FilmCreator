# Title
ape_man_2 Character Reference - Bust Portrait

# ID
ape_man_2_bust_portrait_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Bust character reference portrait, bust portrait with head, shoulders, and facial structure readable, unknown, clean neutral studio background, clear silhouette, consistent costume layers, consistent facial structure, no narrative action, no text, no water..., clean character reference image, neutral gray studio background, bright even soft lighting, soft frontal fill light, sharp subject detail, clear readable silhouette, natural contrast, no dramatic shadow, clear facial structure, visible eyes, readable facial planes, balanced facial lighting, natural skin texture, clean portrait detail, natural realistic body proportions, visible body proportions, clear posture, defined limbs, consistent anatomy, realistic physique, visible outfit details, clear clothing layers, realistic clothing fit, defined accessories, clean fabric detail, visible clothing edges, refined realistic detail, clean contrast, polished but natural reference image

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, underexposed, harsh shadow, silhouette, low key lighting, crushed blacks, cropped subject, text, watermark, obscured face, blurry face, deformed face, asymmetrical face, plastic skin, overly smooth skin, bad anatomy, extra limbs, cropped body, twisted proportions, cartoon proportions, bodybuilder exaggeration, muddy clothing, merged clothing shapes, hidden torso, generic athletic shirt, fashion catalog pose, flat image, low detail, overpolished render, toy-like character

# Inputs
- subject_kind: character
- subject_id: ape_man_2
- source_artifact_ids: CHAR_apache_warriors
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
- display_name: ape_man_2
- identity_descriptor: unknown
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
