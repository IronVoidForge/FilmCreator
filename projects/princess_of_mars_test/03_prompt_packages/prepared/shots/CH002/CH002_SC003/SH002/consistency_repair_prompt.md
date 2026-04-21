# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH002_SC003_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Fear $\rightarrow$ Desperation/Exhaustion **Likely Visual Coverage Families:** - Tracking shots (Following the protagonist's flight) - Wi.... Stable medium framing that keeps action and character readable.. continuity-preserving framing with exact pose and costume locks. Characters: . Environment: described...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH002_SC003; SHOT_INDEX; DIALOGUE
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
- scene_id: CH002_SC003
- chapter_id: CH002
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: continuity-preserving framing with exact pose and costume locks
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH002_SC003 / Transition the protagonist from the claustrophobic cave to the vastne....
- Variant: Consistency Repair.
- Carry the emotional arc through: Fear $\rightarrow$ Desperation/Exhaustion
- **Likely Visual Coverage Families:**
- - Tracking shots (Following the protagonist's flight)
- - Wide landscape shots (Emphasizing his exposure and isolation)
- **Likely Continuity Sensitivities:**
- - The level of physical exertion/sweat on the protagonist.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC003\SH002\DIALOGUE.json
