# Title
CH008_SC003 CL003 Fix 01 Prompt

# ID
CH008_SC003_CL003_fix_01_prompt

# Purpose
Corrective still generation for close-up grappling hook deployment, ensuring continuity with CL002 and maintaining Martian warrior aesthetic within the disabled ship recovery sequence.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
close-up of green-skinned warrior hands releasing metal grappling hook from wrist mount, gray low-profile ship hull drifting southeast, urban Martian architecture background, dim atmospheric lighting, smoke particles visible, smooth motion blur on hook trajectory, detailed mechanical texture on hook, green skin tone consistency, disabled vessel hull shape.

# Negative Prompt
distorted fingers, wrong skin color, blue ship hull, modern technology, bright sunlight, extra characters, blurry background, floating debris, cartoonish style, human hands, red skin, clean ship, interior lighting only, static composition.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors hands, Martians observation
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: close-up
- continuity_mode: insert
- starting_keyframe_strategy: open on hook deployment action
- dependency_policy: depends on CL002
- auto_advance_policy: 
- fallback_strategy: cutaway if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Ship drift vector southeast must match previous frame trajectory.
- Warrior eyelines track ship movement across horizon.
- Hook release timing matches boarding initiation beat.
- Green skin tone consistency with approved character assets.
- Gray ship hull shape matches disabled vessel description.

# Repair Notes
- Ensure green skin tone consistency with previous frames in sequence.
- Verify gray ship hull shape matches disabled vessel description from scene summary.
- Fix any local distortion on hook deployment mechanism.
- Maintain dim atmospheric lighting consistent with battle aftermath context.
- Remove any modern technology artifacts or incorrect skin colors.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
