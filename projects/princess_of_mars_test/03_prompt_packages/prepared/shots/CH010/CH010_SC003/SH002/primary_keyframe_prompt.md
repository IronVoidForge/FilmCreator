# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH010_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Defiance to profound emotional resonance (and underlying tension).. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with, crossing the frame and maintaining readable movement.. Characters: described character with stable costume and silhouette. Environment: described environment with...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH010_SC003; SHOT_INDEX; DIALOGUE; dejah_thoris; tars_tarkas; lorquas_ptomel; None
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH010_SC003
- chapter_id: CH010
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The Council Chamber/Plaza with dejah_thoris, tars_tarkas crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH010_SC003 / Character exposition and ideological conflict..
- Variant: Primary Keyframe.
- Dejah's physical stance and gestures during the speech.
- Carry the emotional arc through: Defiance to profound emotional resonance (and underlying tension)..
- Resolve Thark Council members -> Thark Council members
- Resolve The Council Chamber/Plaza -> The Council Chamber/Plaza
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC003\SH002\DIALOGUE.json
