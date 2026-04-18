# Title
SC001 CL004 Keyframe Prompt

# ID
SC001_CL004_keyframe_prompt

# Purpose
Generate high-fidelity still reference image for scene build workflow, capturing upper floor window observation point and banner design detail focus at cut start to establish visual continuity of fleet movement and narrator curiosity regarding strange devices on ship prows.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Upper floor stone window frame edge visible, human observer figure standing in neutral observation posture, close-up detail of strange banners on low painted vessel prows visible in distance, bright natural daylight reflecting off ship devices, polished stone floor tiles surface, open ground street level below, concern expression on face, hands near chest position, deserted city landscape background, hills and rooftops visible, focus axis locked on vertical vessel prow details.

# Negative Prompt
Crowds, movement blur, exterior only views, other characters, dim lighting, chaotic scene, distorted anatomy, multiple figures, named locations, interior corridor space, dark shadows, companion presence, earthly woman appearance, bright artificial light, night sky, interior wall textures.

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT003.md, Scene SC001 breakdown
- optional_refs: Portal visibility in background, lighting consistency
- visible_character_assets: human observer figure, distant vessel fleet
- look_continuity_policy: Interior lighting consistency with previous beats
- intended_lighting_change: None, maintain ambient interior light
- composition_type: Close-up shot capturing banner detail focus
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert_banner_detail_focus
- dependency_policy: Dependent on CL003 for emotional progression
- auto_advance_policy: Static hold until entrance movement completes
- fallback_strategy: Use static medium if movement unavailable
- consistency_assist_policy: Maintain character proportions and lighting
- consistency_assist_method: Reference alignment with previous frames
- anatomy_repair_policy: Fix any distorted limbs or facial features
- consistency_targets: Observer position, corridor depth, banner visibility
- style_profile: Klein distilled still scene build
- batch_role: Keyframe generation
- fix_of: Still scene build reference
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Window frame color consistency
- Midday lighting intensity
- Fleet positioning at mid-distance
- Character posture shift from sill to chest
- Open ground details clarity
- Banner design visibility across shots
- Device shape continuity markers

# Repair Notes
- Fix anatomy distortions in hands or face
- Ensure background depth matches window view
- Correct lighting brightness to match midday conditions
- Verify banner detail focus is sharp
- Check vessel prow device alignment

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
