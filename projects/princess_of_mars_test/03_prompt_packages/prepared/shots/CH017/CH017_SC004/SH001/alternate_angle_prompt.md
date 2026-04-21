# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH017_SC004_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Dread $\rightarrow$ Decisiveness $\rightarrow$ Heartbreak (during the farewell).. Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with, placed for immediate spatial orientation.. Characters: described character with stable costume and silhouette. Environment: described environment with stable...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH017_SC004; SHOT_INDEX; DIALOGUE; protagonist; dejah_thoris; sola; None
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
- scene_id: CH017_SC004
- chapter_id: CH017
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across The Mossy Waste near a mountain pass with protagonist, sola placed for immediate spatial orientation.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH017_SC004 / To introduce the primary antagonist force and trigger the climax..
- Variant: Alternate Angle.
- Direction of the Thark charge
- ammunition count (rifle shots)
- position of the fleeing thoat.
- A massive party of Thark warriors emerges from a mountain pass. The protagonist shoots the chieftain to create a distraction
- then commands Sola to flee with Dejah on the last thoat.
- Resolve Thark Warriors/Chieftain -> Thark Warriors/Chieftain
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH017\CH017_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH017\CH017_SC004\SH001\DIALOGUE.json
