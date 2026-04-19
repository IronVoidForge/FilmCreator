# Title
CH008_SC003 CL002 Keyframe Prompt

# ID
CH008_SC003_CL002_keyframe_prompt

# Purpose
Fill in the stage intent for medium shot warrior approach during ship interception beat, capturing eyeline tracking and movement toward vessel perimeter while maintaining scene continuity.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Green-skinned warrior medium shot eyeline tracking distant gray drifting vessel, elevated observers visible in background windows, natural daylight continuity, smooth movement toward ship perimeter, urban Martian architecture context, faint smoke rising from hull.

# Negative Prompt
distorted anatomy, extra fingers, bad hands, text, watermark, logo, modern clothing, bright sunlight, dark shadows, blurry foreground, low resolution, morphing objects, wrong skin tone, floating elements, incorrect perspective, close-up faces, modern technology, human observer visible.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors (approaching), Martians (elevated)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium shot
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: open on warrior eyeline tracking ship
- dependency_policy: depends on CL001
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain ship drift vector southeast from previous wide shot
- Ensure warrior positioning aligns with building window fire positions
- Match lighting conditions established in opening keyframe of scene

# Repair Notes
- Correct any anatomical distortions on green-skinned figures
- Verify eyeline direction matches distant ship position
- Adjust color grading to match Martian environment consistency

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
