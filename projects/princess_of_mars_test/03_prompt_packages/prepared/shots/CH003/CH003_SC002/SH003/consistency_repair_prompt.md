# Title
SH003 Shot Prompt - Consistency Repair

# ID
CH003_SC002_SH003_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Curiosity $\rightarrow$ Horror/Awe. **Likely Visual Coverage Families:** - Macro shots of the eggs and the multi-limbed hatchlings. - POV.... shot size medium; camera angle eye_level; lens normal; camera motion locked_off; zoom none; focus deep_focus; lighting hard_directional; subject visibility on_screen;...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH003_SC002; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH003_SC002
- chapter_id: CH003
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in The glass-roofed incubator enclosure that emphasizes the consequence of land the scene consequence or transition cleanly..
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
- reference_asset_ids: protagonist; DESC_CH003_SC002; DESC_CH003_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH003_SC002 / Introduce the biological horror/wonder of Martian life..
- Variant: Consistency Repair.
- The movement patterns of the hatchlings
- lighting through the glass roof.
- Land the scene consequence or transition cleanly.
- Resolve The glass-roofed incubator enclosure -> The glass-roofed incubator enclosure
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC002\SH003\DIALOGUE.json
