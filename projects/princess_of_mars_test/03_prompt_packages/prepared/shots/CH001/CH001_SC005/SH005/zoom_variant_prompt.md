# Title
SH005 Shot Prompt - Tighter Zoom

# ID
CH001_SC005_SH005_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Exhaustion $\rightarrow$ Confusion $\rightarrow$ Lethargy/Loss of consciousness.. Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of carter collapses into unconsciousness... Characters: . Environment: described environment with stable spatial continuity. Keep continu...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH005
- source_artifact_ids: CH001_SC005; SHOT_INDEX; DIALOGUE
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
- scene_id: CH001_SC005
- chapter_id: CH001
- shot_type: closing_reaction
- previous_shot_id: SH004
- next_shot_id: (none)
- shot_lineage_ids: SH004; SH005
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in High cliffside trail that emphasizes the consequence of carter collapses into unconsciousness..
- prompt_family: shot_prompt
- reference_asset_ids: 
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH001_SC005 / SC005.
- Variant: Tighter Zoom.
- Lighting transition (from bright exterior to dark/dim cave)
- Visual cues for unnatural drowsiness (heavy eyelids, blurred vision)
- Carter collapses into unconsciousness.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC005\SH005\DIALOGUE.json
