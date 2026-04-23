# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH004_SC003_SH003_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Humiliation $\rightarrow$ Defiance $\rightarrow$ Triumph/Respect. **Likely Visual Coverage Families:** * Tight Close-ups (CU) on the punc.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of he is then commanded to perform "sak" (jumping), which he does with imp...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH004_SC003; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain; martian_warrior
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
- scene_id: CH004_SC003
- chapter_id: CH004
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in grand_audience_chamber that emphasizes the consequence of he is then commanded to perform "sak" (jumping), which he does with impressive distance, further astounding the assembly..
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; chieftain; grand_audience_chamber; DESC_CH004_SC003; DESC_CH004_SC003_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH004_SC003 / Establish the Narrator's agency and his ability to command respect th....
- Variant: Alternate Angle.
- The physics/trajectory of the jump
- the physical contact during the fight sequence.
- He is then commanded to perform "sak" (jumping)
- which he does with impressive distance
- further astounding the assembly.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC003\SH003\DIALOGUE.json
