# Title
CH008_SC004 CL002 Keyframe Prompt

# ID
CH008_SC004_CL002_keyframe_prompt

# Purpose
Generate a stable wide shot establishing multiple green-skinned warriors positioned across three building roof levels, with missiles loaded in hands or on shoulders, overlooking a distant valley floor under daylight conditions.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide angle view of multiple green-skinned warriors standing on upper floors and roofs of city buildings. Warriors distributed across three vertical levels. Each level contains approximately four figures. Figures hold long missiles in hands or rest them on shoulders. Distant valley floor visible below rooftops. Smoke rising from ground level. Daylight illumination. Action-oriented atmosphere. Vertical composition showing height difference between roofs and valley.

# Negative Prompt
blurry, low resolution, indoor scene, night time, single warrior, crowded plaza, human faces, modern clothing, text, watermark, distorted anatomy, missing weapons, floating objects, excessive smoke obscuring figures, wrong color skin tone, close-up shot, interior walls.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_martian_warrior
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot (establishing multiple warriors)
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
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain consistent character count per roof level (approx 4). Ensure vertical axis from roofs to valley remains unobstructed. Match lighting conditions with previous battle sequence clips. Keep missile placement consistent with launch preparation phase.

# Repair Notes
- If anatomy is distorted, prioritize fixing weapon handling and limb connections. If character count varies, adjust generation parameters to match established wide shot composition. Ensure smoke density does not obscure facial features or skin tone.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
