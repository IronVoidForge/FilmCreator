# Title
SH002 Shot Prompt - Primary Keyframe

# ID
CH005_SC002_SH002_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Determination $\rightarrow$ Alarm/Panic. **Likely Visual Coverage Families:** - Low-angle shots of to emphasize speed. - Handheld/shaky c.... Close framing that isolates reaction and emotional emphasis.. Intimate composition that isolates, against to capture the beat's emotional turn.. Characters: unknown, [], unknown. Envir...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH005_SC002; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
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
- scene_id: CH005_SC002
- chapter_id: CH005
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition that isolates the_watch_dog, protagonist against Captive's chamber to capture the beat's emotional turn.
- prompt_family: shot_prompt
- reference_asset_ids: the_watch_dog; protagonist
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH005_SC002 / SC002.
- Variant: Primary Keyframe.
- Precise physical distance between protagonist and the_watch_dog.
- Consistent direction of the chase sequence.
- the_watch_dog reveals its speed and intelligence
- intercepting the protagonist.
- Resolve Captive's chamber -> Captive's chamber
- Resolve immediate hallway/threshold -> immediate hallway/threshold
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SH002\DIALOGUE.json
