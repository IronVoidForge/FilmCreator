# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH020_SC005_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Gratitude $\rightarrow$ Purpose/Determination.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: [], unknown. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, lighting, and spatial relationships.. Avo...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH020_SC005; SHOT_INDEX; DIALOGUE; protagonist; ptor_family
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
- scene_id: CH020_SC005
- chapter_id: CH020
- shot_type: medium
- previous_shot_id: SH002
- next_shot_id: SH004
- shot_lineage_ids: SH002; SH003; SH004
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in The Ptor Farm featuring protagonist.
- prompt_family: shot_prompt
- reference_asset_ids: protagonist
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH020_SC005 / SC005.
- Variant: Tighter Zoom.
- Protagonist's new appearance (reddish skin/haircut)
- Specific visual design of Zodangan currency
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC005\SH003\DIALOGUE.json
