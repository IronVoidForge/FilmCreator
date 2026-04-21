# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH021_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Caution/Stealth.. Stable medium framing that keeps action and character readable.. shifted perspective with preserved subject spacing. Characters: described character with stable costume and silhouette, . Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, lighting, and s...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH021_SC002; SHOT_INDEX; DIALOGUE; john_carter; None
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
- scene_id: CH021_SC002
- chapter_id: CH021
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: shifted perspective with preserved subject spacing
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH021_SC002 / Transition Carter from the wilderness into the urban setting of Zodanga..
- Variant: Alternate Angle.
- Separation from Woola
- Carter's level of disguise or inconspicuousness.
- Carry the emotional arc through: Caution/Stealth..
- Resolve Woola (briefly) -> Woola (briefly)
- Resolve The walls/gates of Zodanga -> The walls/gates of Zodanga
- Resolve urban streets -> urban streets
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC002\SH002\DIALOGUE.json
