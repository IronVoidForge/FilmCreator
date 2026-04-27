# Title
dak_kova Character Reference - Expression Sheet

# ID
dak_kova_expression_sheet_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Character expression reference sheet, expression sheet showing several clear emotional beats without changing costume, A green-skinned Martian Warhoon chieftain and warlord, enormous frame built for combat and intimidation, severe planar Martian facial structure; hard-set eyes adapted to a harsh martial life; minim...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: dak_kova
- source_artifact_ids: CHAR_apache_warriors; dak_kova
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
- display_name: dak_kova
- identity_descriptor: A green-skinned Martian Warhoon chieftain and warlord
- body_descriptor: enormous frame built for combat and intimidation
- face_descriptor: severe planar Martian facial structure; hard-set eyes adapted to a harsh martial life; minimal or tightly kept scalp hair; Scarred skin; Green skin pigmentation; Green skin
- costume_descriptor: Warhoon warrior gear; likely utilizes tusks as weapons.; hides, leather, metal fittings, and war gear; Warhoon warrior gear; likely utilizes tusks as weapons.; Associated with Bar Comas; Leader of the Warhoon Warriors / Warhoon Horde
- posture_descriptor: upright, dominant, and imposing
- expression_descriptor: stern, martial self-command
- locked_fields: Warhoon warrior gear; likely utilizes tusks as weapons. enormous frame built for combat and intimidation A green-skinned Martian Warhoon chieftain and warlord
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: dak kova: A green-skinned Martian Warhoon chieftain and warlord. Use coherent group visual language using non-modern tribal, frontier, or alien-world materials as appropriate; do not modernize clothing or portrait styling
- fallback_fields_used: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Expression Sheet.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\dak_kova.json
