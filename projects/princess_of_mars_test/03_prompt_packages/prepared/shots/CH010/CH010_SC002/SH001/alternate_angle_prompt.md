# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH010_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. From observation/curiosity to growing indignation and tension. **Likely Visual Coverage Families:** - Medium shots of the council members.... Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: [], unknown. Environment: describ...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH010_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sarkoja; lorquas_ptomel
- reference_mode: shot_prompt_bundle
- variant_name: alternate_angle
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: alternate_angle
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH010_SC002
- chapter_id: CH010
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The interior audience chamber of Lorquas Ptomel with dejah_thoris crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: dejah_thoris
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH010_SC002 / SC002.
- Variant: Alternate Angle.
- Spatial relationship between prisoners and guards
- Scale and proportions of the audience chamber
- Carter observes Dejah Thoris being brought before the Thark council from a distance/periphery.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC002\SH001\DIALOGUE.json
