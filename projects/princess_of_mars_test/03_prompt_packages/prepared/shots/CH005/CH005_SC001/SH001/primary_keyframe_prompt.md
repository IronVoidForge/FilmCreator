# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH005_SC001_SH001_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Ition/Curiosity $\rightarrow$ Comfort/Observation. **Likely Visual Coverage Families:** - Close-ups of 's eyes and facial expressions. -.... Stable medium framing that keeps action and character readable.. Readable medium composition in Captive's chamber featuring and against mural backgrounds.. Characters: An Earthman under...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH005_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola
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
- scene_id: CH005_SC001
- chapter_id: CH005
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Captive's chamber featuring protagonist and sola against mural backgrounds.
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; sola; DESC_CH005_SC001; DESC_CH005_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH005_SC001 / Establish the protagonist's status as a captive, introduce the Martia....
- Variant: Primary Keyframe.
- Lighting changes based on moon cycles
- amount/type of food provided by Sola
- position of the Watch Dog near the door
- position of the Watch Dog near the door.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC001\SH001\DIALOGUE.json
