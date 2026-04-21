# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH026_SC002_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Relief $\rightarrow$ Public Reverence $\rightarrow$ Intense Familial Emotion.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with, crossing the frame and maintaining readable movement.. Characters: described character with stable costume and silhouette. Environment: described envir...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH026_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; mors_kajak; tars_tarkas; None
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH026_SC002
- chapter_id: CH026
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The Heliumite Flagship / Helium Harbor/Docking area with john_carter, dejah_thoris crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH026_SC002 / To facilitate the emotional reunion and public recognition of the hero..
- Variant: Primary Keyframe.
- The physical state/clothing of Dejah Thoris (post-rescue)
- Positioning of Carter relative to the Princess during the transfer.
- Land the scene consequence or transition cleanly.
- Resolve Heliumite Officers -> Heliumite Officers
- Resolve The Heliumite Flagship / Helium Harbor/Docking area -> The Heliumite Flagship / Helium Harbor/Docking area
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC002\SH003\DIALOGUE.json
