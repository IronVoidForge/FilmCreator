# Title
SH001 Shot Prompt - Consistency Repair

# ID
CH010_SC005_SH001_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Tenderness to intense confrontation and defiance.. Close framing that isolates reaction and emotional emphasis.. Intimate composition that isolates, against to capture the beat's emotional turn.. Characters: described character with stable costume and silhouette. Environment: described environment with stab...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH010_SC005; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas
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
- scene_id: CH010_SC005
- chapter_id: CH010
- shot_type: reaction_closeup
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates john_carter, dejah_thoris, tars_tarkas against The Council Chamber/Plaza to capture the beat's emotional turn.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH010_SC005 / Confrontation and character establishment..
- Variant: Consistency Repair.
- The state of Dejah's injury
- the items/weapons Carter now carries from the dead warrior.
- Carter tends to Dejah and reveals he is an Earthman.
- Resolve The Council Chamber/Plaza -> The Council Chamber/Plaza
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC005\SH001\DIALOGUE.json
