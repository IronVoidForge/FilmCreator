# Title
SH004 Shot Prompt - Tighter Zoom

# ID
CH019_SC001_SH004_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Confusion $\rightarrow$ Realization of entrapment/Danger. **Likely Visual Coverage Families:** - Close-ups on Carter's face and hands. -.... Tight detail framing focused on a single visual object or gesture.. Detail composition centered on the key physical action or prop inside .. Characters: . Environment: described environment with stab...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH019_SC001; SHOT_INDEX; DIALOGUE
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
- scene_id: CH019_SC001
- chapter_id: CH019
- shot_type: insert_detail
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside SC001.
- prompt_family: shot_prompt
- reference_asset_ids: 
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH019_SC001 / SC001.
- Variant: Tighter Zoom.
- Lighting levels within the cell must remain consistent to maintain tension
- Precise tracking of the stolen keys' position/absence
- Final realization of entrapment and imminent danger.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH019\CH019_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH019\CH019_SC001\SH004\DIALOGUE.json
