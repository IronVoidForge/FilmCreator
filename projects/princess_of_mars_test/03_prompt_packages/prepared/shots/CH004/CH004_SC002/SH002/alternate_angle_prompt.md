# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH004_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Intimidation $\rightarrow$ Observational Curiosity. **Likely Visual Coverage Families:** * Medium shots of the Chieftain in regalia. * Cl.... Tight detail framing focused on a single visual object or gesture.. Detail composition centered on the key physical action or prop inside .. Characters: . Environment: Cavernous interior with hig...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH004_SC002; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain
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
- scene_id: CH004_SC002
- chapter_id: CH004
- shot_type: insert_detail
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Tight detail framing focused on a single visual object or gesture.
- composition: Detail composition centered on the key physical action or prop inside grand_audience_chamber.
- prompt_family: shot_prompt
- reference_asset_ids: grand_audience_chamber; DESC_CH004_SC002; DESC_CH004_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH004_SC002 / Introduce the political hierarchy and the physical absurdity of the M....
- Variant: Alternate Angle.
- The specific placement of the Narrator within the massive chamber
- the visual details of the Chieftain's regalia.
- Carry the emotional arc through: Intimidation -> Observational Curiosity.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SH002\DIALOGUE.json
