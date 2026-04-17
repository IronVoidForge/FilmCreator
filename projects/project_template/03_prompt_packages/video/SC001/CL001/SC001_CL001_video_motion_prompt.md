# Title
SC001 CL001 Video Motion Prompt

# ID
SC001_CL001_video_motion_prompt

# Purpose
Capture motion-only intent after still continuity is stable.

# Workflow Type
deferred.video.motion

# Positive Prompt
Describe motion, timing, and continuity-preserving movement only.

# Negative Prompt
List motion failures to avoid.

# Inputs
- project_id: project_template
- scene_id: SC001
- clip_id: CL001
- required_refs:
  - approved golden frame
  - approved anchor frame

# Continuity Notes
- Do not redefine identity or environment here.

# Sources
- projects/project_template/02_story_analysis/clip_plans/SC001/CL001.md
