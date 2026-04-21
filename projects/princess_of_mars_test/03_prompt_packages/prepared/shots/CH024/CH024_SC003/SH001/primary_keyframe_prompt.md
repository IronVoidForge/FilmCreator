# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH024_SC003_SH001_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Oppression to Defiance to Violent Resolution.. Wide establishing frame with a steady or lightly drifting camera.. balanced framing with clear spatial separation. Characters: described character with stable costume and silhouette. Environment: Formal assembly hall within the Thark stronghold, structured for council proceeding...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH024_SC003; SHOT_INDEX; DIALOGUE; john_carter; tal_hajus; tars_tarkas; None
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
- scene_id: CH024_SC003
- chapter_id: CH024
- shot_type: establishing_wide
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: balanced framing with clear spatial separation
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH024_SC003 / Resolve the political tension through a climax of leadership and combat..
- Variant: Primary Keyframe.
- Positioning of characters in the council circle
- weapon types used in the duel.
- In the palace
- Tal Hajus orders Carter's torture.
- Resolve Thark Council members -> Thark Council members
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH024\CH024_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH024\CH024_SC003\SH001\DIALOGUE.json
