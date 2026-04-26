# Title
grotesque_creatures Character Reference - Back View

# ID
grotesque_creatures_back_view_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Back-view character reference portrait, rear view with costume back detail and full silhouette clarity, Small, six-limbed alien lifeforms characterized by a grotesque morphology, Small-scale, multi-legged frame with six limbs, angular face; dark eyes; practical short hair; Six limbs; Independent eyes; Antennae; Mul...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: grotesque_creatures
- source_artifact_ids: CHAR_apache_warriors; grotesque_creatures
- reference_mode: character_reference_sheet
- variant_name: back_view
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: back_view
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image
- display_name: grotesque_creatures
- identity_descriptor: Small, six-limbed alien lifeforms characterized by a grotesque morphology
- body_descriptor: Small-scale, multi-legged frame with six limbs
- face_descriptor: angular face; dark eyes; practical short hair; Six limbs; Independent eyes; Antennae; Multi-legged; Grotesque appearance
- costume_descriptor: worn cloth, leather, and practical field materials; Associated with The Incubator
- posture_descriptor: upright and ready
- expression_descriptor: focused and self-controlled
- locked_fields: Small-scale, multi-legged frame with six limbs. Small, six-limbed alien lifeforms characterized by a grotesque morphology
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: grotesque creatures: Small, six-limbed alien lifeforms characterized by a grotesque morphology. Use feral or primitive non-modern appearance, rough natural materials if clothed, no tailored business attire; do not modernize clothing or portrait styling
- fallback_fields_used: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Back View.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\grotesque_creatures.json
