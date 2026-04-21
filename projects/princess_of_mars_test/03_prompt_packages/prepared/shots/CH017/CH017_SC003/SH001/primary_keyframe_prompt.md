# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH017_SC003_SH001_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Panic $\rightarrow$ Heroic Resolve $\rightarrow$ Intense Combat Tension. **Likely Visual Coverage Families:** - Long shots of the approac.... Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: . Environment: describ...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH017_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
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
- scene_id: CH017_SC003
- chapter_id: CH017
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The Mossy Waste / Low Mountains with Thark Chieftain crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: 
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH017_SC003 / SC003.
- Variant: Primary Keyframe.
- Precise tracking of rifle ammunition depletion
- Maintaining consistent spatial distance between Carter and the fleeing women (Dejah Thoris/Sola)
- Resolve Thark Chieftain -> Thark Chieftain
- Resolve Thark Warriors -> Thark Warriors
- Resolve The Mossy Waste / Low Mountains -> The Mossy Waste / Low Mountains
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SH001\DIALOGUE.json
