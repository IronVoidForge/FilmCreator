# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH017_SC003_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Despair $\rightarrow$ Surprise/Warmth $\rightarrow$ Hardship.. Active camera with tracking energy and clear spatial orientation.. tighter framing on the same moment. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, s...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH017_SC003; SHOT_INDEX; DIALOGUE; protagonist; dejah_thoris; sola; None
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
- scene_id: CH017_SC003
- chapter_id: CH017
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH017_SC003 / To escalate the survival stakes and introduce a moment of unexpected....
- Variant: Tighter Zoom.
- The number of functioning thoats
- the presence/position of Woola.
- Amidst the struggle
- the protagonist discovers Woola has followed them.
- Resolve Woola (the hound) -> Woola (the hound)
- Resolve The Mossy Waste -> The Mossy Waste
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SH003\DIALOGUE.json
