# Title
grotesque_creatures Character Reference - Front View

# ID
grotesque_creatures_front_view_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Front-view character reference portrait, front-facing full-body reference with the camera square to the subject, grotesque creatures, cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern c...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: grotesque_creatures
- source_artifact_ids: CHARACTER_REGISTRY_GLOBAL
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
- display_name: grotesque_creatures
- identity_descriptor: grotesque creatures
- body_descriptor: 
- face_descriptor: 
- costume_descriptor: 
- posture_descriptor: 
- expression_descriptor: 
- locked_fields: 
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: grotesque creatures
- fallback_fields_used: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Front View.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- character reference recommended input `body_descriptor` is missing
- character reference recommended input `costume_descriptor` is missing
- character reference recommended input `expression_descriptor` is missing
- character reference recommended input `face_descriptor` is missing
- character reference recommended input `locked_fields` is missing
- character reference recommended input `posture_descriptor` is missing

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\world\global\CHARACTER_REGISTRY_GLOBAL.json
