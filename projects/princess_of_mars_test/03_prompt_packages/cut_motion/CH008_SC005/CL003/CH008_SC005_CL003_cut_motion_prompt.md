# Title
CH008_SC005 CL003 Cut Motion Prompt

# ID
CH008_SC005_CL003_cut_motion_prompt

# Purpose
Establish three-character dynamic and spatial depth within medium two-shot composition. Focus on visible motion of prisoner dragging right-to-left while maintaining connection between foreground observer protagonist and mid-ground female companion. Maintain daylight lighting and smoke haze context from building entrance threshold. Emphasize emotional intensity and urgency in facial expression without proper nouns. Match cut to previous clip on gaze shift or emotional impact reaction.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
observer protagonist upper body medium shot, female companion mid-ground static presence, prisoner background movement right to left, building entrance threshold environment, daylight lighting smoke haze, fire smoke particles drifting, high contrast shadows from urgency, cinematic grade action oriented, green skin tone ornaments visible, slight camera static frame on face, micro-expression shift showing determination.

# Negative Prompt
blur, morphing, extra fingers, wrong skin tone, static image, cartoonish, low resolution, flickering, inconsistent lighting, distorted face, missing eyes, green screen, watermark, text overlay, low fidelity, deformed anatomy, inconsistent character features, wrong background environment, proper nouns, names, labels.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL003
- duration_seconds: 5
- required_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC005/BT002.md, projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL003.md
- optional_refs: None
- visible_character_assets: observer protagonist (face, eyes, upper body), female companion (face, eyes, ornaments), prisoner (background movement)
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None
- composition_type: Medium two-shot
- continuity_mode: insert
- starting_keyframe_strategy: Static close frame on observer protagonist face showing urgency in expression
- dependency_policy: Depends on CL002 establishing spatial context; no reverse dependency
- auto_advance_policy: Prepare transition to BT003 emotional anchor
- fallback_strategy: If facial expression unclear, tighten to extreme close-up on eyes or widen slightly to include more context
- consistency_assist_policy: Match previous clip lighting and color grade
- consistency_assist_method: Reference CL002 golden frame
- anatomy_repair_policy: Ensure eye contact direction matches observer protagonist position
- consistency_targets: female companion face, eyes, upper body ornaments
- style_profile: Action-oriented, awe-inspiring, tense during combat sequences
- batch_role: Strong Initial Test Clip
- fix_of: None
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Capture the continuity rules for this stage. Match lighting and grade from CL002 exactly. Maintain female companion urgency expression throughout duration. Ensure eye contact direction aligns with observer protagonist position in background or side frame. Preserve smoke haze density consistent with building entrance threshold environment. Avoid static image look; ensure subtle motion of head tilt or breathing.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If face morphs, increase detail weight on eyes and mouth corners. If motion is too static, add subtle head tilt or slight camera push. If lighting shifts, reference CL002 golden frame for correction. If character identity drifts, tighten focus to ornaments and skin tone consistency.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
