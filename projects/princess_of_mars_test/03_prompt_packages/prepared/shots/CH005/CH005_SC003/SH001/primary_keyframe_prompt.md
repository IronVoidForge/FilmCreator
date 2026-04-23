# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH005_SC003_SH001_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Adrenaline/Exertion $\rightarrow$ Desperation. **Likely Visual Coverage Families:** - Wide sweeping shots of the Martian architecture. -.... shot size medium; camera angle eye_level; lens normal; camera motion locked_off; zoom none; focus deep_focus; lighting hard_directional; subject visibility on_screen; narration none; pr...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH005_SC003; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: normal
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
- scene_id: CH005_SC003
- chapter_id: CH005
- shot_type: action
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in Deserted Martian city streets with protagonist crossing the frame and maintaining readable movement.
- shot_size: medium
- camera_angle: eye_level
- camera_motion: locked_off
- zoom_behavior: none
- focus_strategy: deep_focus
- lighting_style: hard_directional
- subject_visibility: on_screen
- narration_mode: none
- primary_subject_angle: front_three_quarter_left
- environment_subzone: primary scene playing area
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; DESC_CH005_SC003; DESC_CH005_SC003_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH005_SC003 / To escalate the tension through a high-stakes pursuit and showcase th....
- Variant: Primary Keyframe.
- The height and distance of jumps
- the timing of the dog's arrival at various street corners.
- A frantic chase ensues through the deserted streets of the Martian city. The protagonist uses his superior jumping ability to navigate the urban landscape
- attempting to stay ahead of the relentless Watch Dog.
- Resolve Deserted Martian city streets -> Deserted Martian city streets
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SH001\DIALOGUE.json
