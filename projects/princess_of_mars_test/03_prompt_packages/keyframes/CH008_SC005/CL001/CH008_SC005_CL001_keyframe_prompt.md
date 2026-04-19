# Title
CH008_SC005 CL001 Keyframe Prompt

# ID
CH008_SC005_CL001_keyframe_prompt

# Purpose
Establishes spatial relationship between approaching green-skinned companion and stationary human observer within exterior corridor threshold. Static wide frame captures urgent diagonal movement vector from left edge toward center-right position, setting up connection initiation beat BT001 start state with daylight smoke haze atmosphere.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide exterior corridor threshold, green-skinned humanoid companion entering from left edge moving rightward across frame, human male observer standing center-right partial profile facing camera, daylight atmosphere with smoke haze, burning vessel visible in background distance, open plaza ground texture, gray painted air craft debris scattered near horizon, minimal crowd presence, building entrance threshold visible behind characters.

# Negative Prompt
blur, motion artifacts on static subjects, wrong character count, text overlay, distorted anatomy, dark shadows obscuring faces, extra limbs, missing eyes, low resolution, color shift, green skin on observer, fire on companion face, inconsistent proportions, facial feature distortion, background element misplacement, overexposed highlights, underexposed shadows, wrong skin tone for characters.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL001
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001
- optional_refs: 
- visible_character_assets: observer, companion_human
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight with smoke haze
- composition_type: Wide shot, exterior corridor threshold
- continuity_mode: static wide frame
- starting_keyframe_strategy: Companion at left edge moving right
- dependency_policy: No dependencies; standalone establishing shot
- auto_advance_policy: Hold on wide frame for 3-4 seconds
- fallback_strategy: Tighten to medium wide if entry unclear
- consistency_assist_policy: Apply four_ref consistency targets
- consistency_assist_method: 
- anatomy_repair_policy: Active for humanoid figures
- consistency_targets: 
- style_profile: Martian environment, daylight, smoke haze
- batch_role: establishing_shot
- fix_of: 

# Continuity Notes
- Keyframe must match start state of beat BT001.
- Companion at left edge moving right towards observer.
- Observer static center-right maintaining eye line on companion.
- No motion blur on observer during initial frame lock.
- Background smoke and fire effects consistent with chapter summary.
- Spatial axis: Left-to-center-right (companion to observer).
- Background movement: Right-to-left for prisoner silhouette if visible.
- Environment continuity: Exterior corridor threshold with building entrance.

# Repair Notes
- Apply four_ref consistency targets for humanoid figures.
- Ensure anatomy repair policy active for green-skinned entities.
- Maintain style profile for Martian environment lighting conditions.
- Verify character count matches visible assets list strictly.
- Check skin tone consistency between companion and observer.
- Confirm background elements match chapter visual continuity requirements.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
