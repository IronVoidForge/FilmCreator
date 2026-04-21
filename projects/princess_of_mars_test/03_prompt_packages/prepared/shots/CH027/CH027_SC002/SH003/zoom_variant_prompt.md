# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH027_SC002_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Peace $\rightarrow$ Panic/Urgency.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with, crossing the frame and maintaining readable movement.. Characters: [], unknown. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, lighting, a...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH027_SC002; SHOT_INDEX; DIALOGUE; john_carter; tardos_mors
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
- scene_id: CH027_SC002
- chapter_id: CH027
- shot_type: action
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The Palace of Helium with john_carter, tardos_mors crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tardos_mors
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH027_SC002 / SC002.
- Variant: Tighter Zoom.
- Atmospheric visual cues (haze, light refraction changes)
- The physical sensation of air thinning begins to affect the population in the streets and palace.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC002\SH003\DIALOGUE.json
