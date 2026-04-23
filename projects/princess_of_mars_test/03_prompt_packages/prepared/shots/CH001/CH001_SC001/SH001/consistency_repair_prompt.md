# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH001_SC001_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Introspection / Solemnity.. shot size medium; camera angle eye_level; lens normal; camera motion locked_off; zoom none; focus deep_focus; lighting hard_directional; subject visibility on_screen; narration none; primary subject angle front_three_quarter_left. Stable medium framing that keeps action and chara...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH001_SC001; SHOT_INDEX; DIALOGUE
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: normal
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
- scene_id: CH001_SC001
- chapter_id: CH001
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Unspecified (Narrative framing space) featuring John Carter (Elderly).
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- environment_subzone: primary scene playing area
- prompt_family: shot_prompt
- reference_asset_ids: DESC_CH001_SC001; DESC_CH001_SC001_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH001_SC001 / Establish the framing device and the protagonist's unique condition..
- Variant: Consistency Repair.
- Age of Carter (must remain consistent with "elderly" description)
- tone of voice/delivery.
- An elderly John Carter introduces himself to the reader/audience
- explaining his anomalous aging process and his decision to document his life story before he finally dies.
- Resolve John Carter (Elderly) -> John Carter (Elderly)
- Resolve Unspecified (Narrative framing space) -> Unspecified (Narrative framing space)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC001\SH001\DIALOGUE.json
