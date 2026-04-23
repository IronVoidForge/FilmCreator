# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH004_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Intimidation $\rightarrow$ Observational Curiosity. **Likely Visual Coverage Families:** * Medium shots of the Chieftain in regalia. * Cl.... shot size medium; camera angle eye_level; lens normal; camera motion locked_off; zoom none; focus deep_focus; lighting hard_directional; subject visibility off_screen_voice; narration...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC002; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH004_SC002
- chapter_id: CH004
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside grand_audience_chamber.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: off_screen_voice
- narration_mode: voiceover_off_screen
- primary_subject_angle: front_three_quarter_left
- environment_subzone: primary scene playing area
- prompt_family: shot_prompt
- reference_asset_ids: grand_audience_chamber; DESC_CH004_SC002; DESC_CH004_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH004_SC002 / Introduce the political hierarchy and the physical absurdity of the M....
- Variant: Primary Keyframe.
- The specific placement of the Narrator within the massive chamber
- the visual details of the Chieftain's regalia.
- Carry the emotional arc through: Intimidation $\\rightarrow$ Observational Curiosity.
- **Likely Visual Coverage Families:**
- * Medium shots of the Chieftain in regalia.
- * Close-ups on the Narrator's face reacting to the environment.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SH002\DIALOGUE.json
