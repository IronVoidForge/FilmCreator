# Title
SC001 CL004 Keyframe Prompt

# ID
SC001_CL004_keyframe_prompt

# Purpose
Generate high-fidelity still reference image for scene build workflow, capturing interior corridor space and narrator presence at cut start to establish tension before entrance.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Interior corridor space, narrator standing alone, quiet atmosphere, abandoned building feel, light from window or portal visible in background, empty space, tension building, stone walls, dim lighting, single figure composition

# Negative Prompt
Crowds, movement blur, exterior views, other characters, bright sunlight, chaotic scene, distorted anatomy, multiple figures, proper nouns, named locations

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT004.md, Scene SC001 breakdown
- optional_refs: Portal visibility in background, lighting consistency
- visible_character_assets: Narrator (reacting), Woola (reacting to Sola), Sola (entrance)
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

# Continuity Notes
- Capture the continuity rules for this stage: interior corridor space, narrator standing alone, quiet atmosphere.
- Ensure lighting matches previous beats (dim interior light, window glow).
- Maintain portal visibility in background for depth consistency.
- Avoid introducing Sola fully until entrance movement completes.
- Keep hound positioning consistent with prior frames if visible.

# Repair Notes
- Fix any inconsistencies in character position or lighting if generated frames drift.
- Correct anatomy distortions in narrator figure or background elements.
- Ensure portal visibility remains consistent with previous interior shots.
- Adjust composition if movement blur appears unexpectedly in still generation.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
