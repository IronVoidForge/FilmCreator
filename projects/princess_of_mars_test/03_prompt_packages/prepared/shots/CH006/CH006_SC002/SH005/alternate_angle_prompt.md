# Title
SH005 Shot Prompt - Alternate Angle

# ID
CH006_SC002_SH005_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Panic $\rightarrow$ Resolve $\rightarrow$ Adrenaline-fueled triumph. **Likely Visual Coverage Families:** - Medium shots of the protagoni.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of the protagonist incapacitates and kills the second ape... Characters: ....

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH005
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
- shot_type: closing_reaction
- previous_shot_id: SH004
- next_shot_id: (none)
- shot_lineage_ids: SH004; SH005
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Interior chamber that emphasizes the consequence of the protagonist incapacitates and kills the second ape..
- prompt_family: shot_prompt
- reference_asset_ids: DESC_CH006_SC002; DESC_CH006_SC002_SH005
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH006_SC002 / SC002.
- Variant: Alternate Angle.
- Directionality of cudgel swings
- Blood splatter patterns
- Protagonist's physical exhaustion levels
- The Protagonist incapacitates and kills the second ape.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC002\SH005\DIALOGUE.json
