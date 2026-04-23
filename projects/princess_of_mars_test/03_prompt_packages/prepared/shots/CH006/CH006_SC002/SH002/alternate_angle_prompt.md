# Title
SH002 Shot Prompt - Alternate Angle

# ID
CH006_SC002_SH002_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Panic $\rightarrow$ Resolve $\rightarrow$ Adrenaline-fueled triumph. **Likely Visual Coverage Families:** - Medium shots of the protagoni.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: . Environment: described environment with stable spatial continuity. Keep...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH006_SC002; SHOT_INDEX; DIALOGUE
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
- scene_id: CH006_SC002
- chapter_id: CH006
- shot_type: medium
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Interior chamber featuring scene_character.
- prompt_family: shot_prompt
- reference_asset_ids: DESC_CH006_SC002; DESC_CH006_SC002_SH002
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH006_SC002 / To showcase the protagonist's combat prowess using Earthly tactics an....
- Variant: Alternate Angle.
- The direction of the cudgel swings
- blood splatter patterns
- the physical exhaustion levels of the protagonist.
- The mate returns in a rage; rather than fleeing
- the protagonist uses precise strikes to the chin and stomach to incapacitate and ultimately kill the second ape.
- Resolve Interior chamber -> Interior chamber
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC002\SH002\DIALOGUE.json
