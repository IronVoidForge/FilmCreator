# Title
CH008_SC004 CL008 Keyframe Prompt

# ID
CH008_SC004_CL008_keyframe_prompt

# Purpose
Establish texture detail of burning vessel and rising smoke during battle conclusion beat. Focus on flame coloration, smoke density, and loot visibility on warrior shoulders to maintain continuity with previous missile impacts.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
roaring orange and yellow flames consuming vessel hull, dark gray smoke plume rising vertically, small loot items resting on warrior shoulders, daylight illumination with smoke shadows, burning debris texture detail, spurt of flame from missile impact, drifting vessel silhouette, clean valley floor background.

# Negative Prompt
blue fire, excessive valley floor debris, human faces in close-up, green skin directly visible, static smoke motion, blurry focus, wrong color temperature, debris on roof surfaces, obscured vessel hull, bright sun glare without smoke contrast.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL008
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT002.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Flames, Smoke
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Close-up (texture detail)
- continuity_mode: cutaway
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
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Flame coloration must match orange/yellow spectrum from previous missile impacts.
- Smoke density should be dark gray plume rising above vessel without obscuring hull completely.
- Loot items visible on some warrior shoulders to indicate vessel lightened by removal.
- Valley floor must remain clean of debris from previous impacts.
- Vessel drifting unguided with no guy ropes attached.

# Repair Notes
- Repair flame texture if color shifts away from orange/yellow.
- Adjust smoke opacity to ensure vessel hull remains partially visible.
- Verify loot items are present on shoulders for continuity consistency.
- Check valley floor background for unexpected debris accumulation.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
