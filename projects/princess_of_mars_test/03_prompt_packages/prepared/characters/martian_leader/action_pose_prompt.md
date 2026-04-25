# Title
martian_leader Character Reference - Action Pose

# ID
martian_leader_action_pose_prompt

# Purpose
Prepare a compact character reference prompt for enhancer-safe generation.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
If this prompt is later used with an image reference, treat image1 as the locked identity reference. Action character reference portrait, dynamic action pose that preserves anatomy, costume, and identity, A massive, four-armed Martian warrior leader, 15ft tall; heavy humanoid frame with four arms, severe planar Martian facial structure; hard-set eyes adapted to a harsh martial life; minimal or tightly kept scalp h...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition, modern suit, necktie, business attire, office clothing, corporate headshot, passport photo, turtleneck, modern athletic shirt

# Inputs
- subject_kind: character
- subject_id: martian_leader
- source_artifact_ids: CHAR_apache_warriors; martian_leader
- reference_mode: character_reference_sheet
- variant_name: action_pose
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve identity, costume, and silhouette
- reuse_policy: reuse canonical visual canon
- variant_policy: action_pose
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: character_reference
- target_models: qwen_image; flux; z_image
- display_name: martian_leader
- identity_descriptor: A massive, four-armed Martian warrior leader
- body_descriptor: 15ft tall; heavy humanoid frame with four arms
- face_descriptor: severe planar Martian facial structure; hard-set eyes adapted to a harsh martial life; minimal or tightly kept scalp hair; Olive-green skin; Four arms; Red eyes; Tusks
- costume_descriptor: Unarmed; carrying a metal armlet as a peace offering.; hides, leather, metal fittings, and war gear; Unarmed, carrying a metal armlet as a peace offering.; Approaches others with a metal armlet as a peace offering
- posture_descriptor: upright, dominant, and imposing
- expression_descriptor: stern, martial self-command
- locked_fields: Unarmed, carrying a metal armlet as a peace offering. 15ft tall; heavy humanoid frame with four arms. A massive, four-armed Martian warrior leader
- source_visual_context: cinematic readable reference lighting, pulp planetary-romance adventure, ancient alien-world culture, frontier desert realism, weathered rock and dry wilderness terrain, non-modern clothing, weathered natural materials, tribal or gladiatorial costume logic
- subject_visual_context: martian leader: A massive, four-armed Martian warrior leader. Use feral or primitive non-modern appearance, rough natural materials if clothed, no tailored business attire; do not modernize clothing or portrait styling
- fallback_fields_used: 

# Continuity Notes
- Preserve canonical identity, costume silhouette, and body proportions.
- Variant: Action Pose.
- If this prompt is later used with an image reference, treat image1 as the locked identity reference.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.
- Avoid proper nouns in the prompt body unless text is meant to appear on screen.

# Repair Notes
- reference repair sources: VISUAL_FALLBACKS.json, descriptor_enrichment

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_apache_warriors.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\descriptors\characters\martian_leader.json
