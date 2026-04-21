# Title
SH004 Shot Prompt - Alternate Angle

# ID
CH008_SC002_SH004_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Tension $\rightarrow$ High-Stakes Action $\rightarrow$ Victory/Chaos.. Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of the airship fleet is routed amidst victory and chaos... Characters: [], Insufficient evidence to establish a stable visual identity. The entit...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH008_SC002; SHOT_INDEX; DIALOGUE; green_martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH008_SC002
- chapter_id: CH008
- shot_type: closing_reaction
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in City buildings that emphasizes the consequence of the airship fleet is routed amidst victory and chaos..
- prompt_family: shot_prompt
- reference_asset_ids: green_martian_warriors
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH008_SC002 / SC002.
- Variant: Alternate Angle.
- Trajectory of projectiles must remain consistent across shots
- Damage states of various ships must be tracked incrementally during the engagement
- The airship fleet is routed amidst victory and chaos.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SH004\DIALOGUE.json
