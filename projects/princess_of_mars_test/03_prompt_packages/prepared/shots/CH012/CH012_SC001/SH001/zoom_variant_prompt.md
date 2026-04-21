# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH012_SC001_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Stage with clear narrative intent, stable cast blocking, and continuity-aware coverage.. Wide establishing frame with a steady or lightly drifting camera.. tighter framing on the same moment. Characters: . Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, lighting, and spa...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH012_SC001; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: zoom_variant
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: zoom_variant
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH012_SC001
- chapter_id: CH012
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH012_SC001 / CH012_SC001.
- Variant: Tighter Zoom.
- Establish the production intent for CH012_SC001.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH012\CH012_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC001\SH001\DIALOGUE.json
