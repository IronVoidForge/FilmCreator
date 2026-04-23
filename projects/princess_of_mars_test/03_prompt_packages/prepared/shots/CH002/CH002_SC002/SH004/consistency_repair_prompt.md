# Title
SH004 Shot Prompt - Consistency Repair

# ID
CH002_SC002_SH004_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. From curiosity/investigation to primal terror and chaos. **Likely Visual Coverage Families:** - Wide shots of the gorge/entrance - Handhe.... shot size medium; camera angle eye_level; lens normal; camera motion locked_off; zoom none; focus deep_focus; lighting hard_directional; subject visibility on_screen;...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH002_SC002; SHOT_INDEX; DIALOGUE
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
- scene_id: CH002_SC002
- chapter_id: CH002
- shot_type: closing_reaction
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Cave Entrance / Rocky Gorge that emphasizes the consequence of participating characters: the protagonist (immobile observer), apache warriors.
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
- reference_asset_ids: DESC_CH002_SC002; DESC_CH002_SC002_SH004
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH002_SC002 / To introduce external conflict and demonstrate the supernatural power....
- Variant: Consistency Repair.
- Participating Characters: The Protagonist (Immobile observer), Apache Warriors.
- Participating Environments: Cave Entrance / Rocky Gorge.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH002\CH002_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH002\CH002_SC002\SH004\DIALOGUE.json
