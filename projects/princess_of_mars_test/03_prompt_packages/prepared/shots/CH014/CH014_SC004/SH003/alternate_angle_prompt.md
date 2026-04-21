# Title
SH003 Shot Prompt - Alternate Angle

# ID
CH014_SC004_SH003_alternate_angle_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Alternate angle with the same beat and preserved continuity.. Competitive/Formal $\rightarrow$ Disorientation/Panic.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: [], unknown, Big, hulking build, Powerful, brute-like stature, Seen in deep conversation with Sarkoja., is a large, imposing figure characterized by a hulking...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH003
- source_artifact_ids: CH014_SC004; SHOT_INDEX; DIALOGUE; john_carter; zad
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
- scene_id: CH014_SC004
- chapter_id: CH014
- shot_type: medium
- previous_shot_id: SH002
- next_shot_id: SH004
- shot_lineage_ids: SH002; SH003; SH004
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in Open terrain near the march path featuring john_carter, Zad.
- prompt_family: shot_prompt
- reference_asset_ids: john_carter; zad
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH014_SC004 / SC004.
- Variant: Alternate Angle.
- Sword positions during combat sequences
- Lighting angle for the mirror reflection to ensure blinding effect
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH014\CH014_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH014\CH014_SC004\SH003\DIALOGUE.json
