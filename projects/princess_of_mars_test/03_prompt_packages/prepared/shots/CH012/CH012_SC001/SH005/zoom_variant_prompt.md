# Title
SH005 Shot Prompt - Tighter Zoom

# ID
CH012_SC001_SH005_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. From wary respect to intense political pressure and threat. **Likely Visual Coverage Families:** * Medium shots of the two leaders facing.... Active camera with tracking energy and clear spatial orientation.. Dynamic composition in with, crossing the frame and maintaining readable movement.. Characters: [], unknown, unknown. Environment:...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH005
- source_artifact_ids: CH012_SC001; SHOT_INDEX; DIALOGUE; john_carter; lorquas_ptomel
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
- scene_id: CH012_SC001
- chapter_id: CH012
- shot_type: action
- previous_shot_id: SH004
- next_shot_id: (none)
- shot_lineage_ids: SH004; SH005
- camera_description: Active camera with tracking energy and clear spatial orientation.
- composition: Dynamic composition in audience_chamber with john_carter, lorquas_ptomel crossing the frame and maintaining readable movement.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; lorquas_ptomel; audience_chamber
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH012_SC001 / SC001.
- Variant: Tighter Zoom.
- Carter's physical posture/expression during verbal threats
- Character placement within the audience chamber
- Ptomel reinforces the mandate to deliver Dejah Thoris safely to Tal Hajus.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH012\CH012_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH012\CH012_SC001\SH005\DIALOGUE.json
