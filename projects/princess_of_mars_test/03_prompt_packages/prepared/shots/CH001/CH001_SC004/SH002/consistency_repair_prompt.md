# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH001_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Horror / Grief $\rightarrow$ Desperation / Urgency.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with, crossing the frame and maintaining readable movement.. Characters: . Environment: described environment with stable spatial continuity. Keep continuity exact a...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH001_SC004; SHOT_INDEX; DIALOGUE; apache_warriors
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
- scene_id: CH001_SC004
- chapter_id: CH001
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The trail/valley near the ambush site with John Carter (Younger), Captain James K. Powell (Deceased) crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: DESC_CH001_SC004; DESC_CH001_SC004_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH001_SC004 / Raise the emotional stakes and transition to the escape..
- Variant: Consistency Repair.
- Condition of Powell's body (arrow placement)
- level of injury on Carter
- proximity of pursuers.
- Carry the emotional arc through: Horror / Grief -> Desperation / Urgency.
- Resolve John Carter (Younger) -> John Carter (Younger)
- Resolve Captain James K. Powell (Deceased) -> Captain James K. Powell (Deceased)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH001\CH001_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH001\CH001_SC004\SH002\DIALOGUE.json
