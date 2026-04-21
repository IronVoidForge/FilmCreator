# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH008_SC003_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Observation $\rightarrow$ Melancholy/Empathy. **Likely Visual Coverage Families:** - Close-ups of the protagonist's face (Emotional react.... Active camera with tracking energy and clear spatial orientation.. continuity-preserving framing with exact pose and costume locks. Characters: . Environment: describ...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH008_SC003; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH008_SC003
- chapter_id: CH008
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: continuity-preserving framing with exact pose and costume locks
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH008_SC003 / Internalize the cost of war through the protagonist's perspective..
- Variant: Consistency Repair.
- Lighting/Atmosphere matching the smoke from the distant pyre.
- Carry the emotional arc through: Observation $\rightarrow$ Melancholy/Empathy.
- **Likely Visual Coverage Families:**
- - Close-ups of the protagonist's face (Emotional reaction).
- - Over-the-shoulder shots looking out at the burning ship..
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SH002\DIALOGUE.json
