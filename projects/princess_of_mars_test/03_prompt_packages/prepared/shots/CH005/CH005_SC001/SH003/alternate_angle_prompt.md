# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH005_SC001_SH003_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Isolation/Curiosity $\rightarrow$ Comfort/Observation. **Likely Visual Coverage Families:** - Close-ups of 's eyes and facial expressions.... Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of learns about martian biology and environmental extremes (nocturnal cold...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH005_SC001; SHOT_INDEX; DIALOGUE; protagonist; sola
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
- scene_id: CH005_SC001
- chapter_id: CH005
- shot_type: closing_reaction
- previous_shot_id: SH002
- next_shot_id: (none)
- shot_lineage_ids: SH002; SH003
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in Captive's chamber (decorated with murals) that emphasizes the consequence of protagonist learns about martian biology and environmental extremes (nocturnal cold/moon cycles).
- prompt_family: shot_prompt
- reference_asset_ids: protagonist
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH005_SC001 / SC001.
- Variant: Alternate Angle.
- Lighting shifts must reflect moon cycles
- Food volume/type consistency for plant-milk/Martian biology
- The Watch Dog position relative to the door
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH005\CH005_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH005\CH005_SC001\SH003\DIALOGUE.json
