# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH016_SC003_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Stage with clear narrative intent, stable cast blocking, and continuity-aware coverage.. Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with placed for immediate spatial orientation.. Characters: . Environment: described environment with stable spatial continuity....

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH016_SC003; SHOT_INDEX; DIALOGUE
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
- scene_id: CH016_SC003
- chapter_id: CH016
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across CH016_SC003 with scene_character placed for immediate spatial orientation.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH016_SC003 / CH016_SC003.
- Variant: Consistency Repair.
- Establish the production intent for CH016_SC003.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC003\SH001\DIALOGUE.json
