# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH014_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Protest/Conflict $\rightarrow$ Quiet Compassion $\rightarrow$ Growing Dread.. Wide establishing frame with a steady or lightly drifting camera.. shifted perspective with preserved subject spacing. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH014_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas; sarkoja; zad
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
- scene_id: CH014_SC002
- chapter_id: CH014
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: shifted perspective with preserved subject spacing
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH014_SC002 / Establish the logistical tension and the power dynamics within the gr....
- Variant: Alternate Angle.
- The state of Dejah's fetters/chains
- the positioning of the chariot.
- The party prepares to depart for Thark.
- Resolve Camp/Chariot staging area -> Camp/Chariot staging area
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC002\SH001\DIALOGUE.json
