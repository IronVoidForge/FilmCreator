# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH020_SC002_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Fatigue $\rightarrow$ Awe/Wonder.. Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of land the scene consequence or transition cleanly... Characters: described character with stable costume and silhouette. Environment: described environment with stable...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH020_SC002; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH020_SC002
- chapter_id: CH020
- shot_type: closing_reaction
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Exterior of the Atmosphere Factory that emphasizes the consequence of land the scene consequence or transition cleanly..
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH020_SC002 / Introduce the scale of Martian technology and transition from surviva....
- Variant: Primary Keyframe.
- Scale of the machinery relative to the character.
- Land the scene consequence or transition cleanly.
- Resolve Exterior of the Atmosphere Factory -> Exterior of the Atmosphere Factory
- Resolve Automated Entryway -> Automated Entryway
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC002\SH003\DIALOGUE.json
