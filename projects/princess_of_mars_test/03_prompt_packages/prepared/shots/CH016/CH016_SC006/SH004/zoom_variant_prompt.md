# Title
SH004 Shot Prompt - Tighter Zoom

# ID
CH016_SC006_SH004_zoom_variant_prompt

# Purpose
Prepare a compact shot prompt for enhancer-safe generation.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Film shot prompt. Tighter zoom with the same beat and preserved continuity.. Hopeful Action $\rightarrow$ Confusion $\rightarrow$ Terror/Realization of Trap.. Stable medium framing that keeps action and character readable.. Readable medium composition in featuring, .. Characters: [], unknown, . Environment: described environment with stable spatial continuity. Keep continuity exact across costume, silhouette, ligh...

# Negative Prompt
text, watermark, logo, subtitle, caption, signature, low quality, blurry, out of focus, distorted anatomy, extra limbs, duplicate faces, cropped head, bad hands, messy composition

# Inputs
- subject_kind: shot
- subject_id: SH004
- source_artifact_ids: CH016_SC006; SHOT_INDEX; DIALOGUE; john_carter
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
- scene_id: CH016_SC006
- chapter_id: CH016
- shot_type: medium
- previous_shot_id: SH003
- next_shot_id: SH005
- shot_lineage_ids: SH003; SH004; SH005
- camera_description: Stable medium framing that keeps action and character readable.
- composition: Readable medium composition in City outskirts featuring john_carter, Thark Chieftain (off-screen/overheard).
- prompt_family: shot_prompt
- reference_asset_ids: john_carter
- reference_asset_types: character; environment; scene_descriptor; shot_descriptor

# Continuity Notes
- Scene: CH016_SC006 / SC006.
- Variant: Tighter Zoom.
- Nighttime lighting and shadow consistency across locations
- Movement patterns/choreography of the Thark warriors
- Sound design synchronization for overheard dialogue
- John learns of the plan to take him to the vaults and Dejah Thoris being taken to Tal Hajus.
- Resolve Thark Chieftain (off-screen/overheard) -> Thark Chieftain (off-screen/overheard)
- Resolve Thark Warriors -> Thark Warriors
- Keep the prompt compact enough for ComfyUI text prompt enhancers to expand safely.

# Repair Notes

# Sources
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\scenes\CH016\CH016_SC006.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC006\SHOT_INDEX.json
- C:\FilmCreator_MC\projects\princess_of_mars_test\02_story_analysis\contracts\shots\CH016\CH016_SC006\SH004\DIALOGUE.json
