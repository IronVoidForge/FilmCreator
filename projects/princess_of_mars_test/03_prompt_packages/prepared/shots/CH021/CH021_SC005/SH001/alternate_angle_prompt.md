# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH021_SC005_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Peril $\rightarrow$ Action/Violence $\rightarrow$ Relief.. Wide establishing frame with a steady or lightly drifting camera.. shifted perspective with preserved subject spacing. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity exact ac...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH021_SC005; SHOT_INDEX; DIALOGUE; john_carter; red_martian_scout; None
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
- scene_id: CH021_SC005
- chapter_id: CH021
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: shifted perspective with preserved subject spacing
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH021_SC005 / Action climax and demonstration of Carter's combat prowess..
- Variant: Alternate Angle.
- Damage to Carter's aircraft
- weapon usage
- the identity reveal of the scout.
- During a solo flight
- Carter encounters a skirmish between a Red Martian scout and three Green warriors.
- Resolve Green Warriors -> Green Warriors
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC005\SH001\DIALOGUE.json
