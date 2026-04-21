# Title
SH002 Shot Prompt - Tighter Zoom

# ID
CH013_SC003_SH002_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. From quiet companionship to deep romantic epiphany. **Likely Visual Coverage Families:** - Low-light/Moonlit wide shots of the couple wal.... Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: described character with stable costume and silhouette. Environment: describ...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH002
- source_artifact_ids: CH013_SC003; SHOT_INDEX; DIALOGUE; john_carter; dejah_thoris
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
- scene_id: CH013_SC003
- chapter_id: CH013
- shot_type: medium
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in An avenue or walkway in the Thark city under the night sky/two moons featuring john_carter, dejah_thoris.
- prompt_family: shot_prompt

# Continuity Notes
- Scene: CH013_SC003 / To advance the romantic relationship and highlight cultural misunders....
- Variant: Tighter Zoom.
- Lighting consistency (the two moons)
- the physical proximity/distance between the characters as they walk.
- Dejah refers to him as "my chieftain
- " a term with deep cultural weight that Carter doesn't fully understand.
- Resolve An avenue or walkway in the Thark city under the night sky/two moons -> An avenue or walkway in the Thark city under the night sky/two moons
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH013\CH013_SC003.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC003\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH013\CH013_SC003\SH002\DIALOGUE.json
