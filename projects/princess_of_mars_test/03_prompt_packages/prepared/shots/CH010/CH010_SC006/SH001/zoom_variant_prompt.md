# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH010_SC006_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Resignation to a tentative, uneasy freedom.. Wide establishing frame with a steady or lightly drifting camera.. tighter framing on the same moment. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, lightin...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH010_SC006; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; tars_tarkas; woola
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
- scene_id: CH010_SC006
- chapter_id: CH010
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH010_SC006 / Resolution and transition to next chapter..
- Variant: Tighter Zoom.
- Group formation/walking order.
- Impressed by Carter's resolve
- the Tharks allow Carter
- Dejah Thoris
- and Woola to depart the chamber
- though they remain under supervision/custody.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH010\CH010_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH010\CH010_SC006\SH001\DIALOGUE.json
