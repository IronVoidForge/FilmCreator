# Title
SC001 CL004 Keyframe Prompt

# ID
SC001_CL004_keyframe_prompt

# Purpose
Generate high-fidelity still reference image for scene build workflow, capturing upper floor window observation point and narrator presence at cut start to establish tension before fleet arrival

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Upper floor window frame, human male warrior standing, gray airships visible in distance, midday sunlight reflecting off ship devices, stone floor tiles, polished surface, plaza street level below, concern expression on face, hands near chest position, neutral observation posture, deserted city landscape, hills and rooftops in background

# Negative Prompt
Crowds, movement blur, exterior only views, other characters, dim lighting, chaotic scene, distorted anatomy, multiple figures, named locations, interior corridor space, dark shadows

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT004.md, Scene SC001 breakdown
- optional_refs: Portal visibility in background, lighting consistency
- visible_character_assets: human male warrior, distant airship fleet
- look_continuity_policy: Interior lighting consistency with previous beats
- intended_lighting_change: None, maintain ambient interior light
- composition_type: Medium shot capturing Sola's entrance → Close-up on narrator's reaction
- continuity_mode: cutaway
- starting_keyframe_strategy: Show interior space empty, then introduce Sola's presence
- dependency_policy: Dependent on CL003 for emotional progression
- auto_advance_policy: Static hold until entrance movement completes
- fallback_strategy: Use static medium if movement unavailable
- consistency_assist_policy: Maintain character proportions and lighting
- consistency_assist_method: Reference alignment with previous frames
- anatomy_repair_policy: Fix any distorted limbs or facial features
- consistency_targets: Narrator position, corridor depth, portal visibility
- style_profile: Klein distilled still scene build
- batch_role: Keyframe generation
- fix_of: Still scene build reference
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Window frame color consistency
- Midday lighting intensity
- Fleet positioning at mid-distance
- Character posture shift from sill to chest
- Plaza details clarity

# Repair Notes
- Fix anatomy distortions in hands or face
- Ensure background depth matches window view
- Correct lighting brightness to match midday conditions

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
