# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH022_SC001_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Observational tension $\rightarrow$ Devastation/Heartbreak.. Active camera with tracking energy and clear spatial orientation.. tighter framing on the same moment. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, sil...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH022_SC001; SHOT_INDEX; DIALOGUE; None; dejah_thoris; None
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
- scene_id: CH022_SC001
- chapter_id: CH022
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH022_SC001 / Establish the inciting incident and emotional devastation for the pro....
- Variant: Tighter Zoom.
- Lighting levels in the dark passage vs. the brightly lit apartment
- Carter's physical position relative to the viewing slit.
- Land the scene consequence or transition cleanly.
- Resolve John Carter (observer) -> John Carter (observer)
- Resolve Jeddak Than Kosis -> Jeddak Than Kosis
- Resolve Hidden passage/observation niche -> Hidden passage/observation niche
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC001\SH003\DIALOGUE.json
