# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH007_SC003_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Curiosity to horror/disillusionment.. Stable medium framing that keeps action and character readable.. balanced framing with clear spatial separation. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, si...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH007_SC003; SHOT_INDEX; DIALOGUE; protagonist; sola; None; None
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
- scene_id: CH007_SC003
- chapter_id: CH007
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: balanced framing with clear spatial separation
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH007_SC003 / Reveal the cold, utilitarian, and Darwinian nature of Martian society..
- Variant: Primary Keyframe.
- The movement pattern of the gauntlet
- the physical appearance of the newly hatched Martians.
- Carry the emotional arc through: Curiosity to horror/disillusionment..
- Resolve Newly Hatched Martians -> Newly Hatched Martians
- Resolve Martian Women/Youths -> Martian Women/Youths
- Resolve The Dead Sea Bottom (near the incubator) -> The Dead Sea Bottom (near the incubator)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC003\SH002\DIALOGUE.json
