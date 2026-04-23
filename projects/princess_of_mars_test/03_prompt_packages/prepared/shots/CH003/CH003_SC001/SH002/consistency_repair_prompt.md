# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH003_SC001_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Confusion $\rightarrow$ Physical Bewilderment/Surprise. **Likely Visual Coverage Families:** - Wide shots of the Martian landscape. - Med.... Stable medium framing that keeps action and character readable.. Readable medium composition in a circular basin on Mars featuring .. Characters: An Earthman undergoi...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH003_SC001; SHOT_INDEX; DIALOGUE; protagonist
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
- scene_id: CH003_SC001
- chapter_id: CH003
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in a circular basin on Mars featuring the protagonist.
- prompt_family: shot_prompt
- reference_asset_ids: protagonist; DESC_CH003_SC001; DESC_CH003_SC001_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH003_SC001 / Establish the protagonist's new physical reality and the alien enviro....
- Variant: Consistency Repair.
- The height and distance of the leaps
- The protagonist's nakedness/exposure
- Emotional shift from Confusion to Surprise
- the protagonist's physical state (nakedness/exposure).
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH003\CH003_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH003\CH003_SC001\SH002\DIALOGUE.json
