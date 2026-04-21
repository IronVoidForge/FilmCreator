# Title
SH005 Shot Prompt - Tighter Zoom

# ID
CH026_SC001_SH005_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Tension $\rightarrow$ Chaos/Action $\rightarrow$ Triumph.. Controlled closing frame that lands the consequence of the beat.. Closing composition in that emphasizes the consequence of the combined forces turn the tide against the zodangans.. Characters: [], unknown. Environment: described environment with stable spatial continuity. Keep co...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH005
- source_artifact_ids: CH026_SC001; SHOT_INDEX; DIALOGUE; tars_tarkas; kantos_kan
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
- scene_id: CH026_SC001
- chapter_id: CH026
- shot_type: closing_reaction
- previous_shot_id: SH004
- next_shot_id: (none)
- shot_lineage_ids: SH004; SH005
- camera_description: Controlled closing frame that lands the consequence of the beat.
- composition: Closing composition in The skies above the approach to Helium that emphasizes the consequence of the combined forces turn the tide against the zodangans.
- prompt_family: shot_prompt
- reference_asset_ids: tars_tarkas; kantos_kan
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH026_SC001 / SC001.
- Variant: Tighter Zoom.
- Vessel positions in the sky relative to fleets
- Running count of ships remaining during battle
- Weaponry and ammunition usage/depletion during dogfights
- The combined forces turn the tide against the Zodangans.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH026\CH026_SC001.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH026\CH026_SC001\SH005\DIALOGUE.json
