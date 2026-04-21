# Title
SH004 Shot Prompt - Consistency Repair

# ID
CH022_SC003_SH004_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Confrontation $\rightarrow$ Sorrowful Resignation. **Likely Visual Coverage Families:** - Two-shots to capture the intimacy and distance.... Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: [], u...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH022_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
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
- scene_id: CH022_SC003
- chapter_id: CH022
- shot_type: action
- previous_shot_id: SH003
- next_shot_id: SH005
- shot_lineage_ids: SH003; SH004; SH005
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in Palace interior (near the antechamber/corridors) with dejah_thoris crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH022_SC003 / SC003.
- Variant: Consistency Repair.
- Carter's physical state (sweat/blood from previous fight)
- Dejah Thoris's regal appearance/costume integrity
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC003\SH004\DIALOGUE.json
