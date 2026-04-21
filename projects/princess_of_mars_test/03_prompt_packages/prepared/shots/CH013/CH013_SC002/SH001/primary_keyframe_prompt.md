# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH013_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. From intellectual curiosity to indignation and empathy. **Likely Visual Coverage Families:** - Two-shots of Carter and Dejah discussing t.... Close framing that isolates reaction and emotional emphasis.. Intimate composition that isolates against to capture the beat's emotional turn.. Characters: described character with sta...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH013_SC002; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris; sola
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
- scene_id: CH013_SC002
- chapter_id: CH013
- shot_type: reaction_closeup
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates dejah_thoris against A working area/plaza within the Thark city to capture the beat's emotional turn.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH013_SC002 / To provide exposition on Martian technology and introduce the social....
- Variant: Primary Keyframe.
- The presence of radium powder
- the physical labor/exhaustion visible on Dejah's person.
- Dejah Thoris explains the volatile nature of radium projectiles to Carter
- noting their danger in sunlight. She then reveals the hostility she faces from the older Thark women
- who are forcing her into menial labor (mixing radium powder) due to jealousy of her status.
- Resolve A working area/plaza within the Thark city -> A working area/plaza within the Thark city
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC002\SH001\DIALOGUE.json
