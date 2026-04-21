# Title
SH003 Shot Prompt - Tighter Zoom

# ID
CH012_SC003_SH003_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. From the tension of the meeting to a pragmatic, observant settling-in. **Likely Visual Coverage Families:** * Establishing shots of the m.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: [], unknown. Environment: described environment with stable spatial continui...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH012_SC003; SHOT_INDEX; DIALOGUE; john_carter; tars_tarkas
- reference_mode: shot_prompt_bundle
- variant_name: zoom_variant
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: zoom_variant
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH012_SC003
- chapter_id: CH012
- shot_type: medium
- previous_shot_id: SH002
- next_shot_id: SH004
- shot_lineage_ids: SH002; SH003; SH004
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in The Plaza/Thark City featuring john_carter, tars_tarkas.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; tars_tarkas
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH012_SC003 / SC003.
- Variant: Tighter Zoom.
- Precise arrangement of spoils (silks, weapons, furs) within the apartment.
- Precise arrangement of spoils (silks, weapons, furs) within the apartment
- Consistent number and placement of retinue members (women/youths)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH012\CH012_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC003\SH003\DIALOGUE.json
