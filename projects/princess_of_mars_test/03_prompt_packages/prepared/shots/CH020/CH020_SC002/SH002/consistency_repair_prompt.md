# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH020_SC002_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Curiosity $\rightarrow$ Terror/Realization.. Shoulder-level conversational framing with visible foreground presence.. Over-the-shoulder composition in with sharing the frame for dialogue or tension.. Characters: unknown. Environment: described environment with stable spatial continuity. Keep continuity exac...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH020_SC002; SHOT_INDEX; DIALOGUE; protagonist; caretaker
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
- scene_id: CH020_SC002
- chapter_id: CH020
- shot_type: over_the_shoulder
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Shoulder-level conversational framing with visible foreground presence.
- composition: Over-the-shoulder composition in Interior Atmosphere Factory with caretaker sharing the frame for dialogue or tension.
- prompt_family: shot_prompt
- reference_asset_ids: caretaker
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH020_SC002 / SC002.
- Variant: Consistency Repair.
- Caretaker physical appearance (must maintain "dried-up" look)
- Industrial lighting consistency within the factory setting
- caretaker explains the mechanics of "the ninth ray" and radium pumps.
- Resolve Interior Atmosphere Factory -> Interior Atmosphere Factory
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH020\CH020_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH020\CH020_SC002\SH002\DIALOGUE.json
