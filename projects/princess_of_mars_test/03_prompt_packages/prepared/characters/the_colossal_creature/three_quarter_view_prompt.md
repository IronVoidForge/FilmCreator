# Title
the_colossal_creature Character Reference - 3/4 View

# ID
the_colossal_creature_three_quarter_view_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Three-quarter character reference portrait, three-quarter view with readable face, torso, and costume layers, A massive, white, hairless humanoid non-human with ape-like characteristics, Large-scale, bipedal, ape-like frame, angular face; dark eyes; practical short hair; White skin; Hairless body (except for specif...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: the_colossal_creature
- source_artifact_ids: CHAR_apache_warriors; the_colossal_creature
- reference_mode: character_reference_sheet
- variant_name: three_quarter_view
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: three_quarter_view
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image
- display_name: the_colossal_creature
- identity_descriptor: A massive, white, hairless humanoid non-human with ape-like characteristics
- body_descriptor: Large-scale, bipedal, ape-like frame
- face_descriptor: angular face; dark eyes; practical short hair; White skin; Hairless body (except for specific hair); A distinct shock of bristly hair; Bipedal; Ape-like
- costume_descriptor: worn cloth, leather, and practical field materials; Associated with the protagonist
- posture_descriptor: upright and ready
- expression_descriptor: focused and self-controlled
- locked_fields: Large-scale, bipedal, ape-like frame. A massive, white, hairless humanoid non-human with ape-like characteristics
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: the colossal creature: A massive, white, hairless humanoid non-human with ape-like characteristics. Use feral or primitive non-modern appearance, rough natural materials if clothed, no tailored business attire; do not modernize clothing or portrait styling
- fallback_fields_used: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: 3/4 View.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\the_colossal_creature.json
