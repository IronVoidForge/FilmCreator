# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH008_SC004_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Curiosity $\rightarrow$ Tension/Connection $\rightarrow$ Regret/Dejection. **Likely Visual Coverage Families:** - Eye-contact close-ups (.... Close framing that isolates reaction and emotional emphasis.. Intimate composition that isolates against to capture the beat's emotional turn.. Characters: . Environment: described env...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH008_SC004; SHOT_INDEX; DIALOGUE
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
- scene_id: CH008_SC004
- chapter_id: CH008
- shot_type: reaction_closeup
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates scene_character against Introduce a new character and create a moment of missed connection/dr... to capture the beat's emotional turn.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH008_SC004 / Introduce a new character and create a moment of missed connection/dr....
- Variant: Primary Keyframe.
- The specific hand gesture used by the prisoner
- the direction of movement as she is taken away.
- She makes a silent gesture for help
- but the protagonist—unaware of Martian customs—fails to respond.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH008\CH008_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH008\CH008_SC004\SH002\DIALOGUE.json
