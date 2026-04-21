# Title
SH003 Shot Prompt - Primary Keyframe

# ID
CH020_SC004_SH003_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Dread $\rightarrow$ Panic $\rightarrow$ Intense Focus/Action $\rightarrow$ Relief.. Active camera with tracking energy and clear spatial orientation.. balanced framing with clear spatial separation. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial cont...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH020_SC004; SHOT_INDEX; DIALOGUE; protagonist; old_man; woola
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
- scene_id: CH020_SC004
- chapter_id: CH020
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: balanced framing with clear spatial separation
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH020_SC004 / Provide a high-stakes climax and demonstrate the protagonist's unique....
- Variant: Primary Keyframe.
- The timing of the door/lock mechanisms responding to thought-waves.
- Land the scene consequence or transition cleanly.
- Resolve Interior of the Atmosphere Factory (escape corridors/locks) -> Interior of the Atmosphere Factory (escape corridors/locks)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC004\SH003\DIALOGUE.json
