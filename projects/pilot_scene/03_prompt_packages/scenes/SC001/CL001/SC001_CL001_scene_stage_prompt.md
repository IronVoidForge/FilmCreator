# Title
SC001 CL001 Scene Stage Prompt

# ID
SC001_CL001_scene_stage_prompt

# Purpose
Define visual staging intent, subject placement, and environmental context alignment with approved keyframe assets

# Workflow Type
authoring.scene_stage

# Positive Prompt
centered subject placement within frame boundaries, balanced environmental context matching approved keyframe lighting conditions, clear visibility of character silhouette against background elements, consistent color grading with reference stills

# Negative Prompt
distorted facial features, mismatched lighting sources, incorrect framing composition, blurry details, extra limbs, inconsistent color grading, wrong subject count

# Inputs
- project_id: pilot_scene
- scene_id: SC001
- clip_id: CL001
- duration_seconds: variable
- required_refs: projects/pilot_scene/05_scenes/SC001/clips/CL001/stills/keyframes/SC001_CL001_KF01.png, projects/pilot_scene/05_scenes/SC001/clips/CL001/video/SC001_CL001_MV03_v003.mp4
- optional_refs: 
- style_profile: cinematic_compositional
- batch_role: scene_stage
- fix_of: 

# Continuity Notes
- Match approved keyframe composition exactly for subject positioning
- Maintain character appearance consistency with golden frame reference
- Align environmental texture and lighting with cut motion video style
- Ensure opening frame setup reflects intended staging intent from scene breakdown

# Repair Notes
- Adjust subject position if alignment deviates from keyframe reference
- Correct lighting mismatches to match approved stills
- Fix framing issues if subject placement is off-center relative to composition rules

# Sources
- projects/pilot_scene/02_story_analysis/clip_plans/SC001/CL001.md
