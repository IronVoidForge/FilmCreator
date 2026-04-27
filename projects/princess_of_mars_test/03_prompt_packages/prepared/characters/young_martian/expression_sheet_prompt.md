# Title
young_martian Character Reference - Expression Sheet

# ID
young_martian_expression_sheet_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Character expression reference sheet, expression sheet showing several clear emotional beats without changing costume, Small, humanoid non-human male, Three-to-four-foot-tall; described as "physically perfect.", weathered angular face; dark steady eyes; short practical frontier cut; Physically perfect anatomy; Bipe...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: young_martian
- source_artifact_ids: CHAR_apache_warriors; young_martian
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
- display_name: young_martian
- identity_descriptor: Small, humanoid non-human male
- body_descriptor: Three-to-four-foot-tall; described as "physically perfect."
- face_descriptor: weathered angular face; dark steady eyes; short practical frontier cut; Physically perfect anatomy; Bipedal morphology; Small scale
- costume_descriptor: A small, humanoid non-human male standing approximately three to four feet tall. He is characterized by a "physically perfect" anatomy and appears in a newly hatched state, devoid of clothing or costume
- posture_descriptor: upright, self-possessed, and ready
- expression_descriptor: steady, capable, restrained intensity
- locked_fields: 
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: young martian: Small, humanoid non-human male. Use feral or primitive non-modern appearance, rough natural materials if clothed, no tailored business attire; do not modernize clothing or portrait styling
- fallback_fields_used: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Expression Sheet.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- character reference recommended input `locked_fields` is missing
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\young_martian.json
