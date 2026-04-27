# Title
than_kosis Character Reference - Bust Portrait

# ID
than_kosis_bust_portrait_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Bust character reference portrait, bust portrait with head, shoulders, and facial structure readable, Humanoid ruler of Zodanga, human scale bipedal humanoid, angular face; dark eyes; practical short hair; humanoid morphology, worn cloth, leather, and practical field materials; Associated with Sab Than; Associated...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: than_kosis
- source_artifact_ids: CHAR_apache_warriors; than_kosis
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
- display_name: than_kosis
- identity_descriptor: Humanoid ruler of Zodanga
- body_descriptor: human scale bipedal humanoid
- face_descriptor: angular face; dark eyes; practical short hair; humanoid morphology
- costume_descriptor: worn cloth, leather, and practical field materials; Associated with Sab Than; Associated with Dejah Thoris; Associated with Notan
- posture_descriptor: upright and ready
- expression_descriptor: focused and self-controlled
- locked_fields: human scale bipedal humanoid Humanoid ruler of Zodanga
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: than kosis: Humanoid ruler of Zodanga. Use feral or primitive non-modern appearance, rough natural materials if clothed, no tailored business attire; do not modernize clothing or portrait styling
- fallback_fields_used: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Bust Portrait.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\than_kosis.json
