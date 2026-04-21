# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH017_SC003_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Panic $\rightarrow$ Heroic Resolve $\rightarrow$ Intense Combat Tension. **Likely Visual Coverage Families:** - Long shots of the approac.... Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with, crossing the frame and maintaining readable movement.. Characters: [], unknown. Environment: described...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH017_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
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
- previous_shot_id: SH002
- next_shot_id: SH004
- shot_lineage_ids: SH002; SH003; SH004
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The Mossy Waste / Low Mountains with john_carter, dejah_thoris crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; dejah_thoris
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH017_SC003 / SC003.
- Variant: Tighter Zoom.
- Precise tracking of rifle ammunition depletion
- Maintaining consistent spatial distance between Carter and the fleeing women (Dejah Thoris/Sola)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC003\SH003\DIALOGUE.json
