# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH020_SC003_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Curiosity $\rightarrow$ Intellectual Engagement $\rightarrow$ Growing Dread.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: described character with stable costume and silhouette. Environment: described environment with stable spati...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH020_SC003; SHOT_INDEX; DIALOGUE; protagonist; invisible_host; old_man
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH020_SC003
- chapter_id: CH020
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Interior of the Atmosphere Factory (industrial, ancient, high-tech) featuring protagonist, invisible_host.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH020_SC003 / Provide exposition regarding the planet's life support and introduce....
- Variant: Consistency Repair.
- The visual appearance/lighting of the "ninth ray" or machinery.
- Carry the emotional arc through: Curiosity $\rightarrow$ Intellectual Engagement $\rightarrow$ Growing Dread..
- Resolve Interior of the Atmosphere Factory (industrial, ancient, high-tech) -> Interior of the Atmosphere Factory (industrial, ancient, high-tech)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC003\SH002\DIALOGUE.json
