# Title
SH001 Shot Prompt - Alternate Angle

# ID
CH027_SC005_SH001_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. High Tension $\rightarrow$ Exhausted Relief.. Wide establishing frame with a steady or lightly drifting camera.. Wide composition across with placed for immediate spatial orientation.. Characters: [], unknown. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, lighting,...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH027_SC005; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH027_SC005
- chapter_id: CH027
- shot_type: establishing_wide
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Wide establishing frame with a steady or lightly drifting camera.
- composition: Wide composition across The Atmosphere Plant (interior/exterior) with john_carter placed for immediate spatial orientation.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH027_SC005 / SC005.
- Variant: Alternate Angle.
- Mechanical state progression (doors unlocking/opening -> pumps restarting)
- John Carter's physiological degradation (asphyxiation/exhaustion levels)
- Mechanical state progression (doors unlocking/opening $\rightarrow$ pumps restarting)
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH027\CH027_SC005.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC005\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH027\CH027_SC005\SH001\DIALOGUE.json
