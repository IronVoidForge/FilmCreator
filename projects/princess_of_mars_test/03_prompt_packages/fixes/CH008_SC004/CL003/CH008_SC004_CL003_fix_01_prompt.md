# Title
CH008_SC004 CL003 Fix 01 Prompt

# ID
CH008_SC004_CL003_fix_01_prompt

# Purpose
Preserve extreme wide shot composition of missiles in flight toward distant vessel while correcting local rendering issues and maintaining visual continuity with approved keyframe base. Fix smoke density, missile trajectory clarity, and vessel damage visibility without altering camera position or scene geography.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
extreme wide shot missiles mid-flight gray painted vessels with strange banners odd devices on prows visible in valley floor distance burning vessel with orange yellow flames dark gray smoke plume rising from previous impacts daylight conditions city buildings upper floors windows roofs background open ground plaza camera positioned at plaza level looking up and across vertical axis from roofs down to valley floor horizontal axis following missile trajectory

# Negative Prompt
close-up shot medium shot extreme close-up over-the-shoulder perspective character faces detailed facial features individual warrior expressions human female prisoner green skin ornaments naked except for highly wrought ornaments weapons spears chariots mastodons mounted warriors air craft crew wireless finding apparatus large gray painted air craft smoke too dense or too light flames not visible vessel hull intact no damage loot removal not visible valley floor debris hills beyond not visible

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Missiles in flight, vessel visible in valley floor distance, smoke rising from previous impacts
- look_continuity_policy: preserve approved keyframe base composition and lighting
- intended_lighting_change: none
- composition_type: extreme wide shot (action context)
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: reframe_same_moment
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: enabled
- consistency_assist_method: composition_lock
- anatomy_repair_policy: minimal
- consistency_targets: missile trajectory, vessel damage visibility, smoke density
- style_profile: action-oriented awe-inspiring tense combat sequences
- batch_role: still_fix
- fix_of: approved_keyframe_base

# Continuity Notes
- Capture the continuity rules for this stage.
- Maintain extreme wide shot composition without altering camera position or geography
- Preserve missile trajectory clarity and vessel damage visibility from previous impacts
- Keep smoke density consistent with rising from valley floor impacts
- Ensure daylight conditions match approved keyframe base
- No character movement during observation phase
- Camera positioned at plaza level looking up and across vertical axis
- Horizontal axis following missile trajectory toward target

# Repair Notes
- Capture any repair or corrective guidance for this stage.
- Fix smoke density if too light or too dark relative to approved base
- Correct missile trajectory visibility if obscured or unclear
- Enhance vessel damage and flame visibility without adding new elements
- Maintain composition lock while fixing local rendering issues
- Ensure no unintended character details appear in extreme wide shot
- Preserve vertical axis from roofs down to valley floor geography
- Keep horizontal axis following missile drift path consistent with approved keyframe

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
