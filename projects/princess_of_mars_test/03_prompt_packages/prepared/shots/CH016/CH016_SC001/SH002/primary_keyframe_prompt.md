# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH016_SC001_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Stage with clear narrative intent, stable cast blocking, and continuity-aware coverage.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: . Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouett...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH016_SC001; SHOT_INDEX; DIALOGUE
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
- scene_id: CH016_SC001
- chapter_id: CH016
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in CH016_SC001 featuring scene_character.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH016_SC001 / CH016_SC001.
- Variant: Primary Keyframe.
- Escalate the scene tension and staging clearly.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC001\SH002\DIALOGUE.json
