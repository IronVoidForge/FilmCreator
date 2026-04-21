# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH027_SC005_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. High Tension $\rightarrow$ Exhausted Relief.. Tight detail framing focused on a single visual object or gesture.. Detail composition centered on the key physical action or prop inside .. Characters: . Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, lighting...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH027_SC005; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH027_SC005
- chapter_id: CH027
- shot_type: insert_detail
- previous_shot_id: SH002
- next_shot_id: SH004
- shot_lineage_ids: SH002; SH003; SH004
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside The Atmosphere Plant (interior/exterior).
- prompt_family: shot_prompt
- reference_asset_ids: 
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH027_SC005 / SC005.
- Variant: Primary Keyframe.
- Mechanical state progression (doors unlocking/opening -> pumps restarting)
- John Carter's physiological degradation (asphyxiation/exhaustion levels)
- Mechanical state progression (doors unlocking/opening $\rightarrow$ pumps restarting)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC005\SH003\DIALOGUE.json
