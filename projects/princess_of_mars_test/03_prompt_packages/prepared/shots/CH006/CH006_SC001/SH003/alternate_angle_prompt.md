# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH006_SC001_SH003_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Terror $\rightarrow$ Desperation $\rightarrow$ Fierce Loyalty. **Likely Visual Coverage Families:** - Tight close-ups on the protagonist'.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of **participating characters:**\n- the protagonist\n- the watch-thing\n-...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH006_SC001; SHOT_INDEX; DIALOGUE
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
- scene_id: CH006_SC001
- chapter_id: CH006
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Interior chamber that emphasizes the consequence of **participating characters:**\n- the protagonist\n- the watch-thing\n- the bull ape\n- the mate (bull ape).
- prompt_family: shot_prompt
- reference_asset_ids: DESC_CH006_SC001; DESC_CH006_SC001_SH003
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH006_SC001 / To establish immediate life-or-death stakes and demonstrate the loyal....
- Variant: Alternate Angle.
- The positioning of the Bull Ape's limbs
- the location of the fallen cudgel
- the physical state (injuries) of the Watch-thing during the fight.
- **Participating Characters:**
- The Protagonist
- The Watch-thing
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH006\CH006_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH006\CH006_SC001\SH003\DIALOGUE.json
