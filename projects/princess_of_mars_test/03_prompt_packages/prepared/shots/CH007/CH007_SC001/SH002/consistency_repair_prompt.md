# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH007_SC001_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Awe to anticipation.. Stable medium framing that keeps action and character readable.. continuity-preserving framing with exact pose and costume locks. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity exact...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH007_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola
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
- scene_id: CH007_SC001
- chapter_id: CH007
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: continuity-preserving framing with exact pose and costume locks
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH007_SC001 / Establish the scale of Martian military culture and the protagonist's....
- Variant: Consistency Repair.
- Movement direction of the cavalcade
- lighting consistency across the vast landscape
- chariot/beast positioning.
- Carry the emotional arc through: Awe to anticipation..
- Resolve The Plaza (departure) -> The Plaza (departure)
- Resolve Martian Wilderness/Plains -> Martian Wilderness/Plains
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC001\SH002\DIALOGUE.json
