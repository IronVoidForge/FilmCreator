# Title
SH001 Shot Prompt - Primary Keyframe

# ID
CH004_SC002_SH001_primary_keyframe_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Primary keyframe with balanced composition and clear subject placement.. Intimidation $\rightarrow$ Observational Curiosity. **Likely Visual Coverage Families:** * Medium shots of the Chieftain in regalia. * Cl.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring .. Characters: . Environment: Cavernous interior with high vaulted ceilings, i...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH004_SC002; SHOT_INDEX; DIALOGUE; tars_tarkas; chieftain
- reference_mode: shot_prompt_bundle
- variant_name: primary_keyframe
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: primary_keyframe
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH004_SC002
- chapter_id: CH004
- shot_type: medium
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in grand_audience_chamber featuring The Narrator.
- prompt_family: shot_prompt
- reference_asset_ids: grand_audience_chamber; DESC_CH004_SC002; DESC_CH004_SC002_SH001
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH004_SC002 / Introduce the political hierarchy and the physical absurdity of the M....
- Variant: Primary Keyframe.
- The specific placement of the Narrator within the massive chamber
- the visual details of the Chieftain's regalia.
- The Narrator is presented to the Chieftain in a grand audience chamber. He observes the mismatch between the massive, ancient furniture and the Martians' biology, emphasizing the antiquity of the ruins.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH004\CH004_SC002.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH004\CH004_SC002\SH001\DIALOGUE.json
