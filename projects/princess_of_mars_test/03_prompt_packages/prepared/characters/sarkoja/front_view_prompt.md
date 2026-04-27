# Title
sarkoja Character Reference - Front View

# ID
sarkoja_front_view_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Front-view character reference portrait, front-facing full-body reference with the camera square to the subject, Green Martian (Thark) female humanoid, enormous frame built for combat and intimidation, severe planar Martian facial structure; hard-set eyes adapted to a harsh martial life; minimal or tightly kept sca...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: sarkoja
- source_artifact_ids: CHAR_apache_warriors; sarkoja
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
- display_name: sarkoja
- identity_descriptor: Green Martian (Thark) female humanoid
- body_descriptor: enormous frame built for combat and intimidation
- face_descriptor: severe planar Martian facial structure; hard-set eyes adapted to a harsh martial life; minimal or tightly kept scalp hair; Green skin pigmentation; Green skin
- costume_descriptor: hides, leather, metal fittings, and war gear; Associated with Sola; Associated with John Carter; Associated with Dejah Thoris; Associated with Lorquas Ptomel; Associated with Tal Hajus; Associated with Tars Tarkas
- posture_descriptor: upright, dominant, and imposing
- expression_descriptor: stern, martial self-command
- locked_fields: enormous frame built for combat and intimidation Green Martian (Thark) female humanoid
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: sarkoja: Green Martian (Thark) female humanoid. Use feral or primitive non-modern appearance, rough natural materials if clothed, no tailored business attire; do not modernize clothing or portrait styling
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
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\sarkoja.json
