# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH012_SC003_SH001_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. From the tension of the meeting to a pragmatic, observant settling-in. **Likely Visual Coverage Families:** * Establishing shots of the m.... Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with, placed for immediate spatial orientation.. Characters: [], unknown. Environment: descri...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH012_SC003; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
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
- scene_id: CH012_SC003
- chapter_id: CH012
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across The Plaza/Thark City with john_carter, tars_tarkas placed for immediate spatial orientation.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH012_SC003 / SC003.
- Variant: Primary Keyframe.
- Establishing shots of Thark architecture and the central court.
- Precise arrangement of spoils (silks, weapons, furs) within the apartment
- Consistent number and placement of retinue members (women/youths)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH012\CH012_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC003\SH001\DIALOGUE.json
