# Title
woola Character Reference - Front View

# ID
woola_front_view_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Front-view character reference portrait, front-facing full-body reference with the camera square to the subject, A large, quadrupedal Martian creature identified as a calot, Giant, large-scale quadrupedal frame; hound-like morphology, animal skull structure with species-specific proportions; animal eyes with a pred...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: woola
- source_artifact_ids: CHAR_apache_warriors; woola
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
- display_name: woola
- identity_descriptor: A large, quadrupedal Martian creature identified as a calot
- body_descriptor: Giant, large-scale quadrupedal frame; hound-like morphology
- face_descriptor: animal skull structure with species-specific proportions; animal eyes with a predatory alertness; natural animal coat or mane; Calot species; Hound-like appearance
- costume_descriptor: Large quadrupedal silhouette.; natural hide, harness, or no costume materials; Loyal protector of the protagonist; Associated with John Carter and Sola
- posture_descriptor: animal stance ready to spring or charge
- expression_descriptor: feral or alert animal focus
- locked_fields: Large quadrupedal silhouette. Giant, large-scale quadrupedal frame; hound-like morphology. A large, quadrupedal Martian creature identified as a calot
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: woola: A large, quadrupedal Martian creature identified as a calot. Use feral or primitive non-modern appearance, rough natural materials if clothed, no tailored business attire; do not modernize clothing or portrait styling
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
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\woola.json
