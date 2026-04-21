# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH008_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Chaos $\rightarrow$ Methodical Efficiency $\rightarrow$ Somber Spectacle. **Likely Visual Coverage Families:** - Low angle shots of grapp.... Stable medium framing that keeps action and character readable.. shifted perspective with preserved subject spacing. Characters: . Environment: described environment with stable spatial continuit...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH008_SC002; SHOT_INDEX; DIALOGUE
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
- scene_id: CH008_SC002
- chapter_id: CH008
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: shifted perspective with preserved subject spacing
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH008_SC002 / Show the aftermath of the battle and the ritualistic destruction of t....
- Variant: Alternate Angle.
- The movement/drift of the burning ship
- the amount of loot being carried away.
- Martian warriors use grappling hooks to pull the ship down
- systematically looting it of weapons
- silks
- jewels
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC002\SH002\DIALOGUE.json
