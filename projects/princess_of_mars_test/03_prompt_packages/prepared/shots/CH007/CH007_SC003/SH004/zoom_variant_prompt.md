# Title
SH004 Shot Prompt - Tighter Zoom

# ID
CH007_SC003_SH004_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Coldness and detachment; a sense of systemic brutality. **Likely Visual Coverage Families:** - Montage or observational shots of the egg.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of the incubator is sealed for a five-year duration... Characters: . Environme...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH007_SC003; SHOT_INDEX; DIALOGUE
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
- scene_id: CH007_SC003
- chapter_id: CH007
- shot_type: closing_reaction
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in SC003 that emphasizes the consequence of the incubator is sealed for a five-year duration..
- prompt_family: shot_prompt
- reference_asset_ids: 
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH007_SC003 / SC003.
- Variant: Tighter Zoom.
- Physical handling/manipulation of the eggs
- Lighting transition from subterranean vaults to sunlit incubator
- The incubator is sealed for a five-year duration.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH007\CH007_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH007\CH007_SC003\SH004\DIALOGUE.json
