# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH010_SC004_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Shock/Outrage to violent action to sudden social elevation.. Active camera with tracking energy and clear spatial orientation.. continuity-preserving framing with exact pose and costume locks. Characters: described character with stable costume and silhouette. Environment: described environment with stable...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH010_SC004; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; None; thark_warriors
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
- scene_id: CH010_SC004
- chapter_id: CH010
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: continuity-preserving framing with exact pose and costume locks
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH010_SC004 / Climax of the chapter; action beat and status shift..
- Variant: Consistency Repair.
- The movement of weapons/possessions from the dead warrior to Carter
- blood/injury on Dejah Thoris.
- A young Thark warrior strikes Dejah Thoris in a moment of cruel laughter.
- Resolve Young Thark Warrior -> Young Thark Warrior
- Resolve The Council Chamber/Plaza -> The Council Chamber/Plaza
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC004\SH001\DIALOGUE.json
