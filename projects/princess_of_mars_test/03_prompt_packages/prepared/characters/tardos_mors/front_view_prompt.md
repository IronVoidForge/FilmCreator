# Title
tardos_mors Character Reference - Front View

# ID
tardos_mors_front_view_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Front-view character reference portrait, front-facing full-body reference with the camera square to the subject, Human male of high status, lean but durable soldier's frame, weathered angular face; dark steady eyes; short practical frontier cut; human morphology, worn cloth, leather, cavalry gear, and salvaged mate...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: tardos_mors
- source_artifact_ids: CHAR_apache_warriors; tardos_mors
- reference_mode: character_reference_sheet
- variant_name: front_view
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: front_view
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image
- display_name: tardos_mors
- identity_descriptor: Human male of high status
- body_descriptor: lean but durable soldier's frame
- face_descriptor: weathered angular face; dark steady eyes; short practical frontier cut; human morphology
- costume_descriptor: worn cloth, leather, cavalry gear, and salvaged materials; Associated with Dejah Thoris; Associated with Mors Kajak; Associated with John Carter
- posture_descriptor: upright, self-possessed, and ready
- expression_descriptor: steady, capable, restrained intensity
- locked_fields: lean but durable soldier's frame Human male of high status
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: tardos mors: Human male of high status. Use feral or primitive non-modern appearance, rough natural materials if clothed, no tailored business attire; do not modernize clothing or portrait styling
- fallback_fields_used: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Front View.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\tardos_mors.json
