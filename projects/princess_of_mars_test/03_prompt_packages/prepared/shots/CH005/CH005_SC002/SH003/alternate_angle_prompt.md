# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH005_SC002_SH003_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Determination $\rightarrow$ Alarm/Panic. **Likely Visual Coverage Families:** - Low-angle shots of to emphasize speed. - Handheld/shaky c.... Controlled closing frame that lands the consequence of the beat; handheld/shaky cam.. Closing composition in emphasizing the consequence of the chase.. Characters: An Earthman undergoing a supern...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH005_SC002; SHOT_INDEX; DIALOGUE; protagonist; the_watch_dog
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
- scene_id: CH005_SC002
- chapter_id: CH005
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat; handheld/shaky cam.
- composition: Closing composition in Captive's chamber emphasizing the consequence of the chase.
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; the_watch_dog; DESC_CH005_SC002; DESC_CH005_SC002_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH005_SC002 / To initiate the action and demonstrate the physical threat of the Mar....
- Variant: Alternate Angle.
- The physical distance between the protagonist and the dog
- the direction of the chase.
- Resolve Captive's chamber -> Captive's chamber
- Resolve immediate hallway/threshold -> immediate hallway/threshold
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC002\SH003\DIALOGUE.json
