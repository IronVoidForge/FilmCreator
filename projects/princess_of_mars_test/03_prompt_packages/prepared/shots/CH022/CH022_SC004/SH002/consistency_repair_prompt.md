# Title
SH002 Shot Prompt - Consistency Repair

# ID
CH022_SC004_SH002_consistency_repair_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Continuity repair pass that preserves pose, costume, lighting, and spatial relationships.. Tension $\rightarrow$ Dread. **Likely Visual Coverage Families:** - Macro shots of Carter's eyes/face within the ornament. - Low-angle or.... Shoulder-level conversational framing with visible foreground presence.. Over-the-shoulder composition in with, sharing the frame for dialogue or tension.. Characters...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH022_SC004; SHOT_INDEX; DIALOGUE; notan; than_kosis
- reference_mode: shot_prompt_bundle
- variant_name: consistency_repair
- lens_family: neutral_reference
- composition_lock: preserve canonical identity and framing rules
- trait_lock: preserve stable visual canon
- image_to_image_source: 
- change_budget: preserve scene continuity and shot intent
- reuse_policy: reuse canonical shot contract canon
- variant_policy: consistency_repair
- review_notes: 
- prompt_enhancer_mode: comfyui_text_prompt_enhancer
- prompt_enhancer_profile: shot_reference
- target_models: qwen_image; flux; z_image
- scene_id: CH022_SC004
- chapter_id: CH022
- shot_type: over_the_shoulder
- previous_shot_id: SH001
- next_shot_id: SH003
- shot_lineage_ids: SH001; SH002; SH003
- camera_description: Shoulder-level conversational framing with visible foreground presence.
- composition: Over-the-shoulder composition in The Great Hall with notan, than_kosis sharing the frame for dialogue or tension.
- prompt_family: shot_prompt
- reference_asset_ids: notan; than_kosis
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH022_SC004 / SC004.
- Variant: Consistency Repair.
- Sound design: Muffled voices from inside the ornament vs. clear palace noise/chaos.
- Carter takes cover inside a large hanging ornament within the Great Hall.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH022\CH022_SC004.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC004\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH022\CH022_SC004\SH002\DIALOGUE.json
