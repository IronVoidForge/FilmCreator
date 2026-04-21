# Title
SH004 Shot Prompt - Primary Keyframe

# ID
CH008_SC003_SH004_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Chaos $\rightarrow$ Methodical/Ruthless Efficiency.. Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of the warriors set the ship on fire, creating a drifting funeral pyre... Characters: [], Insufficient evidence to establish a stable visual identity. T...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH008_SC003; SHOT_INDEX; DIALOGUE; green_martian_warriors
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
- scene_id: CH008_SC003
- chapter_id: CH008
- shot_type: closing_reaction
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in City outskirts / Ground level near the impact site that emphasizes the consequence of the warriors set the ship on fire, creating a drifting funeral pyre..
- prompt_family: shot_prompt
- reference_asset_ids: green_martian_warriors
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH008_SC003 / SC003.
- Variant: Primary Keyframe.
- Direction and speed of the drifting, burning vessel must remain consistent across shots.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC003\SH004\DIALOGUE.json
