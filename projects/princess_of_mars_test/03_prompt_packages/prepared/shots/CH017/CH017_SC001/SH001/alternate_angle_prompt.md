# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH017_SC001_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Tension/Dread $\rightarrow$ Action/Adrenaline $\rightarrow$ Relief/Urgency.. Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with, placed for immediate spatial orientation.. Characters: described character with stable costume and silhouette. Environment: described environment with stable spati...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH017_SC001; SHOT_INDEX; DIALOGUE; protagonist; dejah_thoris; sola; None
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
- scene_id: CH017_SC001
- chapter_id: CH017
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across The interior of the Jeddak's palace/chambers in Thark with protagonist, sola placed for immediate spatial orientation.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH017_SC001 / To establish the high stakes of the rescue and execute the successful....
- Variant: Alternate Angle.
- Lighting levels in the palace vs. the exterior
- wounds or dishevelment of characters after the scuffle.
- The protagonist infiltrates the city to find Dejah Thoris under threat by Tal Hajus. He knocks out the Jeddak
- rescues Dejah and Sola
- and escapes through a window into the night.
- Resolve Tal Hajus (unconscious) -> Tal Hajus (unconscious)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC001\SH001\DIALOGUE.json
