# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH020_SC005_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Suspicion/Tiredness $\rightarrow$ Gratitude/Security.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep continuity exact acro...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH020_SC005; SHOT_INDEX; DIALOGUE; protagonist; red_martians
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
- scene_id: CH020_SC005
- chapter_id: CH020
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Red Martian Home (elevated structure on a metal shaft) featuring protagonist, red_martians.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH020_SC005 / Transition the protagonist toward his next objective (Zodanga) and pr....
- Variant: Primary Keyframe.
- The protagonist's physical appearance change (skin color, hair length).
- Carry the emotional arc through: Suspicion/Tiredness $\rightarrow$ Gratitude/Security..
- Resolve Red Martian Home (elevated structure on a metal shaft) -> Red Martian Home (elevated structure on a metal shaft)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC005\SH002\DIALOGUE.json
