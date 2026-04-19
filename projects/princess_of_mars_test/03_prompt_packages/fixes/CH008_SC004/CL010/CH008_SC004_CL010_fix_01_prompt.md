# Title
CH008_SC004 CL010 Fix 01 Prompt

# ID
CH008_SC004_CL010_fix_01_prompt

# Purpose
Corrective still generation for CL010 Wide Shot of Group Gathering at Plaza Entrance. Preserves composition and look while fixing local issues such as debris on plaza surface, smoke density consistency with BT002, and warrior positioning convergence toward plaza center per BT003 beat logic. Ensures continuity with scene insert workflow using two reference inputs.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide shot of green warriors gathered at plaza entrance, moving from multiple points toward plaza center, consolidating loot on shoulders and hands. City buildings with upper floors, windows, roofs visible in background. Open ground plaza surface clean without debris. Valley floor beyond city with distant hills. Smoke clearing significantly from immediate area, diminished flames in distance. Daylight lighting conditions. Vertical axis from roofs down to plaza level. Green skin tone on warriors, wearing ornaments and carrying spears.

# Negative Prompt
Debris on plaza surface, excessive smoke obscuring subjects, wrong character count, anatomy errors, modern clothing, incorrect skin tone, blurry focus, distorted limbs, missing loot items, wrong lighting direction, fire damage to buildings, human observer visible in frame, vertical axis misalignment.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL010
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_martian_warrior
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot (establishing)
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- note Maintain vertical axis from roofs down to plaza level as per BT003.
- note Ensure smoke density matches clearing state from previous beat (BT002).
- note Keep warriors converging toward plaza center without stopping mid-path.
- note Preserve clean plaza surface condition established in scene summary.

# Repair Notes
- note Fix any debris artifacts on the clean plaza surface.
- note Adjust smoke opacity to ensure visibility of background hills.
- note Correct warrior positioning to match converging paths from roofs and valley floor.
- note Verify loot items are visible but not obscuring main character forms.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL010.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
