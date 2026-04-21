# Title
SH004 Shot Prompt - Consistency Repair

# ID
CH022_SC002_SH004_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Desperation $\rightarrow$ Rage/Combat Intensity. **Likely Visual Coverage Families:** - Wide shots to establish the geography of the figh.... Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: . En...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH022_SC002; SHOT_INDEX; DIALOGUE; john_carter
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH022_SC002
- chapter_id: CH022
- shot_type: action
- previous_shot_id: SH003
- next_shot_id: (none)
- shot_lineage_ids: SH003; SH004
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in Palace corridors/Antechambers with Four Guardsmen crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: 
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH022_SC002 / SC002.
- Variant: Consistency Repair.
- Blood splatter patterns.
- Weapon positions throughout the sequence.
- Incremental count of fallen guards in frame.
- The combat concludes with the death of all four guardsmen.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC002\SH004\DIALOGUE.json
