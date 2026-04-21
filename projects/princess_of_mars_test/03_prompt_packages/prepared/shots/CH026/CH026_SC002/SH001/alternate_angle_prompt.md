# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH026_SC002_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Relief $\rightarrow$ Public Reverence $\rightarrow$ Intense Familial Emotion.. Wide establishing frame with a steady or lightly drifting camera.. shifted perspective with preserved subject spacing. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH026_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; mors_kajak; tars_tarkas; None
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
- scene_id: CH026_SC002
- chapter_id: CH026
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: shifted perspective with preserved subject spacing
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH026_SC002 / To facilitate the emotional reunion and public recognition of the hero..
- Variant: Alternate Angle.
- The physical state/clothing of Dejah Thoris (post-rescue)
- Positioning of Carter relative to the Princess during the transfer.
- Upon reaching Helium
- John Carter assists in transferring Princess Dejah Thoris to the Heliumite flagship. In a moment of high ceremony
- Dejah Thoris publicly credits Carter for her rescue and the salvation of the city before being reunited with her father
- Mors Kajak.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC002\SH001\DIALOGUE.json
