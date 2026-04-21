# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH008_SC002_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Tension $\rightarrow$ High-Stakes Action $\rightarrow$ Victory/Chaos.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: [], Insufficient evidence to establish a stable visual identity. The entity is identified as a group of warriors., unknown. Environment: described e...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH008_SC002; SHOT_INDEX; DIALOGUE; green_martian_warriors
- reference_mode: shot_prompt_bundle
- variant_name: zoom_variant
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: zoom_variant
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH008_SC002
- chapter_id: CH008
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in City buildings featuring green_martian_warriors.
- prompt_family: shot_prompt
- reference_asset_ids: green_martian_warriors
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH008_SC002 / SC002.
- Variant: Tighter Zoom.
- Trajectory of projectiles must remain consistent across shots
- Damage states of various ships must be tracked incrementally during the engagement
- Tension builds as the green Martian warriors prepare for engagement.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SH001\DIALOGUE.json
