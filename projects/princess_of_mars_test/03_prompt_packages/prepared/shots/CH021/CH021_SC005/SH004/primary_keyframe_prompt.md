# Title
SH004 Shot Prompt - Primary Keyframe

# ID
CH021_SC005_SH004_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Tension $\rightarrow$ High Action $\rightarrow$ Relief.. Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: . Environment: described environment with stable spatial continuity. Keep continuity exact across costume,...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH021_SC005; SHOT_INDEX; DIALOGUE; john_carter; zodangan_scout
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
- scene_id: CH021_SC005
- chapter_id: CH021
- shot_type: action
- previous_shot_id: SH003
- next_shot_id: SH005
- shot_lineage_ids: SH003; SH004; SH005
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in The Martian sky/aerial combat zone with Three Green Martian Warriors crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: 
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH021_SC005 / SC005.
- Variant: Primary Keyframe.
- Precise flight trajectories for all airborne entities
- Physical state/damage to airships post-combat
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC005\SH004\DIALOGUE.json
