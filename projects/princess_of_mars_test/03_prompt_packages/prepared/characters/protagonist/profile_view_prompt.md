# Title
protagonist Character Reference - Profile View

# ID
protagonist_profile_view_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Profile character reference portrait, profile view with a clean silhouette and side-plane facial structure, A transformed Earthman characterized by extreme physical agility and high-leaping capabilities suited for low gravity. The character exhibits a transition from a standard human state to a post-supernatural tr...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: protagonist
- source_artifact_ids: CHAR_apache_warriors; protagonist
- reference_mode: character_reference_sheet
- variant_name: profile_view
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: profile_view
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image
- display_name: protagonist
- identity_descriptor: A transformed Earthman characterized by extreme physical agility and high-leaping capabilities suited for low gravity. The character exhibits a transition from a standard human state to a post-supernatural transformation state, initially appearing naked and unarmed but demonstrating high-intensity combat prowess through earthly striking tactics
- body_descriptor: 
- face_descriptor: angular face; dark eyes; practical short hair; supernatural transformation (post-transformation state); capable of leaping over chariots; high physical prowess
- costume_descriptor: worn cloth, leather, and practical field materials
- posture_descriptor: upright and ready
- expression_descriptor: focused and self-controlled
- locked_fields: 
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: protagonist
- fallback_fields_used: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Profile View.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- character reference recommended input `body_descriptor` is missing
- character reference recommended input `locked_fields` is missing
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\protagonist.json
