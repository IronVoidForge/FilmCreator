# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH005_SC003_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Adrenaline/Exertion $\rightarrow$ Desperation. **Likely Visual Coverage Families:** - Wide sweeping shots of the Martian architecture. -.... Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with crossing the frame and maintaining readable movement.. Characters: An Ea...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH005_SC003; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
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
- scene_id: CH005_SC003
- chapter_id: CH005
- shot_type: action
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in Deserted Martian city streets with protagonist crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; DESC_CH005_SC003; DESC_CH005_SC003_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH005_SC003 / To escalate the tension through a high-stakes pursuit and showcase th....
- Variant: Consistency Repair.
- The height and distance of jumps
- the timing of the dog's arrival at various street corners.
- Carry the emotional arc through: Adrenaline/Exertion -> Desperation.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC003\SH002\DIALOGUE.json
