# Title
CH008_SC005 CL002 Scene Stage Prompt

# ID
CH008_SC005_CL002_scene_stage_prompt

# Purpose
Describe staging intent, subject placement, environmental context, and intended visible opening frame setup for CL002. Establish Carter's perspective as he observes the prisoner being dragged into the building entrance. Emphasize urgency and conflict introduction during the beat. Ensure the wide shot composition aligns with previous establishing shots while preparing for subsequent close-ups. Maintain depth layering between foreground observer and background action.

# Workflow Type
authoring.scene_stage

# Positive Prompt
human protagonist shoulder profile foreground left, slender female prisoner full body background right dragging motion through entrance threshold, exterior corridor building entrance threshold daylight smoke from fire distance, medium two shot over-the-shoulder perspective, stationary observer moving prisoner, urgency in movement, Martian city architecture visible, natural lighting with high contrast shadows, open ground plaza beyond

# Negative Prompt
close-up human protagonist face, wide shot, static background, blurry movement, modern clothing technology, green screen artifacts, low resolution, distorted anatomy, indoor artificial lighting, crowded scene, explosion effects in foreground, bright overexposed background, unnatural skin tones

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT002, CH008_SC005/BT002.md End State
- optional_refs: None
- visible_character_assets: Carter (shoulder/back profile), Prisoner (full body dragging)
- look_continuity_policy: Ensure background movement continuity; prisoner's clothing state must match BT002 start/end.
- intended_lighting_change: Maintain daylight with smoke effects from distant battle.
- composition_type: Medium two shot, over-the-shoulder from Carter's perspective
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: Prisoner visible in background plane, moving right-to-left across entrance
- dependency_policy: Depends on CL001 establishing spatial context; no reverse dependency
- auto_advance_policy: None
- fallback_strategy: If shoulder framing is unclear, shift to medium shot with both characters fully visible
- consistency_assist_policy: Ensure prisoner's movement vector is clear without obscuring foreground characters.
- consistency_assist_method: smooth_background_trajectory
- anatomy_repair_policy: Adjust anatomy if movement blur looks unnatural.
- consistency_targets: Maintain eye line consistency with CL001 wide establishing shot.
- style_profile: Action-oriented, awe-inspiring, tense during combat sequences.
- batch_role: Conflict Introduction
- fix_of: None

# Continuity Notes
- Maintain eye line consistency with CL001 wide establishing shot.
- Ensure prisoner's movement trajectory matches previous wide shot path.
- Keep Carter's shoulder framing consistent across interval beats.
- Match lighting conditions of the corridor and exterior threshold.
- Preserve background smoke and fire effects from distant battle.
- Verify character placement aligns with corridor axis.

# Repair Notes
- If human protagonist face is visible, hide it to maintain over-the-shoulder intent.
- If background is too bright, darken to match mood of urgency.
- Ensure prisoner's speed matches urgency of approach.
- Adjust anatomy if movement blur looks unnatural.
- Verify character placement aligns with corridor axis.
- If prisoner disappears too quickly, extend motion slightly for clarity.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
