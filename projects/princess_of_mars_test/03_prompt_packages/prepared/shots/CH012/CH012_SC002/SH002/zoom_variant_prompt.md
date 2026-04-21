# Title
SH002 Shot Prompt - Tighter Zoom

# ID
CH012_SC002_SH002_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. From tension to focused, desperate determination. **Likely Visual Coverage Families:** * Tight close-ups on Carter's eyes/face to convey.... Close framing that isolates reaction and emotional emphasis.. Intimate composition isolating against to capture the emotional turn.. Characters: . Environment: described environment with stable spati...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH012_SC002; SHOT_INDEX; DIALOGUE
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
- scene_id: CH012_SC002
- chapter_id: CH012
- shot_type: reaction_closeup
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Close framing that isolates reaction and emotional emphasis.
- composition: Intimate composition isolating John Carter (Internal monologue/Realization) against Transitioning from the Audience Chamber to the city streets/plaza to capture the emotional turn.
- prompt_family: shot_prompt
- reference_asset_ids: 
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH012_SC002 / SC002.
- Variant: Tighter Zoom.
- Precise timing of the internal realization relative to physical movement through the city.
- Seamless transition from Audience Chamber to city streets/plaza.
- As Carter moves through the city streets/plaza, he realizes Sarkoja has been spying on him and reporting to Thark leadership.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH012\CH012_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC002\SH002\DIALOGUE.json
