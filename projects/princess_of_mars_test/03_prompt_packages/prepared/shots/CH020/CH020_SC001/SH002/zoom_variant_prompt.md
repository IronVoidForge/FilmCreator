# Title
SH002 Shot Prompt - Tighter Zoom

# ID
CH020_SC001_SH002_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Desperation/Exhaustion $\rightarrow$ Terror (during beast attacks) $\rightarrow$ Relief/Survival.. Active camera with tracking energy and clear spatial orientation.. tighter framing on the same moment. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Kee...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH020_SC001; SHOT_INDEX; DIALOGUE; protagonist; woola
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
- scene_id: CH020_SC001
- chapter_id: CH020
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: tighter framing on the same moment
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH020_SC001 / Establish the protagonist's physical struggle, isolation, and the dan....
- Variant: Tighter Zoom.
- Protagonist's level of physical deterioration (dirt, weight loss)
- Woola's condition.
- Carry the emotional arc through: Desperation/Exhaustion $\rightarrow$ Terror (during beast attacks) $\rightarrow$ Relief/Survival..
- Resolve The Martian Wilderness (desolate, dangerous terrain) -> The Martian Wilderness (desolate, dangerous terrain)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC001\SH002\DIALOGUE.json
