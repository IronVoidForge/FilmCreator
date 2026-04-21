# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH026_SC001_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Tension $\rightarrow$ Chaotic Violence $\rightarrow$ Grim Triumph.. Active camera with tracking energy and clear spatial orientation.. balanced framing with clear spatial separation. Characters: described character with stable costume and silhouette. Environment: described environment with stable spatial continuity. Keep con...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH026_SC001; SHOT_INDEX; DIALOGUE; tars_tarkas; kantos_kan; None; None
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
- scene_id: CH026_SC001
- chapter_id: CH026
- shot_type: action
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: balanced framing with clear spatial separation
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH026_SC001 / To establish the military dominance of the Thark-Heliumite alliance a....
- Variant: Primary Keyframe.
- Ship positions relative to one another
- Direction of flight paths
- Timing of small-arms fire vs. naval maneuvers.
- A massive aerial battle ensues
- utilizing Heliumite naval tactics combined with Thark small-arms fire.
- Resolve John Carter (implied/observing) -> John Carter (implied/observing)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SH002\DIALOGUE.json
