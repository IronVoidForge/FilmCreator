# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH016_SC001_SH003_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Stage with clear narrative intent, stable cast blocking, and continuity-aware coverage.. Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of land the scene consequence or transition cleanly... Characters: . Environment: described environment with stable spatial con...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH016_SC001; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH016_SC001
- chapter_id: CH016
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in CH016_SC001 that emphasizes the consequence of land the scene consequence or transition cleanly..
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH016_SC001 / CH016_SC001.
- Variant: Alternate Angle.
- Land the scene consequence or transition cleanly.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC001\SH003\DIALOGUE.json
