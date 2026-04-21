# Title
SH001 Shot Prompt - Tighter Zoom

# ID
CH021_SC003_SH001_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Relief $\rightarrow$ Strategic Focus.. Shoulder-level conversational framing with visible foreground presence.. Over-the-shoulder composition in with sharing the frame for dialogue or tension.. Characters: [], unknown. Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, ligh...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH001
- source_artifact_ids: CH021_SC003; SHOT_INDEX; DIALOGUE; john_carter; kantos_kan
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
- scene_id: CH021_SC003
- chapter_id: CH021
- shot_type: over_the_shoulder
- previous_shot_id: (none)
- next_shot_id: SH002
- shot_lineage_ids: SH001; SH002
- camera_description: Shoulder-level conversational framing with visible foreground presence.
- composition: Over-the-shoulder composition in Zodanga Central Plaza (high-raised residences) with kantos_kan sharing the frame for dialogue or tension.
- prompt_family: shot_prompt
- reference_asset_ids: kantos_kan
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH021_SC003 / SC003.
- Variant: Tighter Zoom.
- Scale and height of surrounding Zodangan architecture (high-raised residences)
- Carter reunites with Kantos Kan in the central plaza.
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH021\CH021_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH021\CH021_SC003\SH001\DIALOGUE.json
