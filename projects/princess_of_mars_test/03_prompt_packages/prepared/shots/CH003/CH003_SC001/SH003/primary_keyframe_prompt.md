# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH003_SC001_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Confusion $\rightarrow$ Physical Bewilderment/Surprise. **Likely Visual Coverage Families:** - Wide shots of the Martian landscape. - Med.... Controlled closing frame that lands the consequence of the beat.. Closing composition in a circular basin on Mars emphasizing the consequence of the movement/environment.. Characters:...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH003_SC001; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH003_SC001
- chapter_id: CH003
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in a circular basin on Mars emphasizing the consequence of the movement/environment.
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; DESC_CH003_SC001; DESC_CH003_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH003_SC001 / Establish the protagonist's new physical reality and the alien enviro....
- Variant: Primary Keyframe.
- The height and distance of the leaps
- The protagonist's physical state (nakedness/exposure)
- the protagonist's physical state (nakedness/exposure).
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SH003\DIALOGUE.json
