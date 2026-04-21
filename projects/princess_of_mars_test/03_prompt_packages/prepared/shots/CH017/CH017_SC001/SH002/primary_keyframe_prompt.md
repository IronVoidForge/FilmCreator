# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH017_SC001_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Tension/Dread $\rightarrow$ Action/Adrenaline $\rightarrow$ Relief/Urgency.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with, crossing the frame and maintaining readable movement.. Characters: described character with stable costume and silhouette. Environment: described environ...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH017_SC001; SHOT_INDEX; DIALOGUE; protagonist; dejah_thoris; sola; None
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
- scene_id: CH017_SC001
- chapter_id: CH017
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The interior of the Jeddak's palace/chambers in Thark with protagonist, dejah_thoris crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH017_SC001 / To establish the high stakes of the rescue and execute the successful....
- Variant: Primary Keyframe.
- Lighting levels in the palace vs. the exterior
- wounds or dishevelment of characters after the scuffle.
- Carry the emotional arc through: Tension/Dread $\rightarrow$ Action/Adrenaline $\rightarrow$ Relief/Urgency..
- Resolve Tal Hajus (unconscious) -> Tal Hajus (unconscious)
- Resolve The interior of the Jeddak's palace/chambers in Thark -> The interior of the Jeddak's palace/chambers in Thark
- Resolve city rooftops/windows -> city rooftops/windows
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SH002\DIALOGUE.json
