# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH001_SC003_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Suspicion $\rightarrow$ Alertness $\rightarrow$ Chaos/Adrenaline.. Tight detail framing focused on a single visual object or gesture.. Detail composition centered on the key physical action or prop inside .. Characters: A large group of hostile indigenous fighters., readable production detail, group silhouette emphasizes num...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH001_SC003; SHOT_INDEX; DIALOGUE; apache_warriors
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
- scene_id: CH001_SC003
- chapter_id: CH001
- shot_type: insert_detail
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside Arizona hills/plateau.
- prompt_family: shot_prompt
- reference_asset_ids: apache_warriors; DESC_CH001_SC003; DESC_CH001_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH001_SC003 / Introduce the primary conflict and physical threat..
- Variant: Primary Keyframe.
- Number of warriors
- direction of pursuit
- weapon handling (rifles/sidearms)
- weapon handling (rifles/sidearms).
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC003\SH003\DIALOGUE.json
