# Title
CH008_SC005 CL003 Scene Stage Prompt

# ID
CH008_SC005_CL003_scene_stage_prompt

# Purpose
Establish close-up framing on companion character face and upper body showing urgency in expression. Static frame locked on eyes focused forward with micro-expression shift indicating determination. Cut from preceding two-shot as character arrives at proximity. Visual opening frame setup emphasizes emotional intensity and connection initiation within exterior corridor environment context.

# Workflow Type
authoring.scene_stage

# Positive Prompt
companion character face upper body urgent expression determination eyes focused forward exterior corridor daylight smoke shadows high contrast lighting approaching movement implied proximity static close frame composition human skin tone reddish copper features finely chiseled hair coal black waving loosely caught coiffure ornaments highly wrought cheeks crimson lips ruby action-oriented awe-inspiring tense atmosphere.

# Negative Prompt
green skin static background explosion fire on face wrong character focus blurry anatomy inconsistent expression neutral emotion wide shot medium shot close-up of observer character green_martian_warrior chaotic movement overexposed underexposed distorted features missing ornaments incorrect coiffure.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md End State
- optional_refs: None
- visible_character_assets: companion character face eyes upper body
- look_continuity_policy: match preceding two-shot lighting and expression intensity
- intended_lighting_change: maintain daylight with smoke shadows from battle context
- composition_type: close up
- continuity_mode: insert
- starting_keyframe_strategy: static close frame on face showing urgency in expression
- dependency_policy: depends on CL002 establishing spatial context; no reverse dependency
- auto_advance_policy: prepare cut to CL004 at 3s mark
- fallback_strategy: tighten to extreme close-up on eyes if facial expression unclear
- consistency_assist_policy: ensure eye line matches observer character for reaction shot preparation
- consistency_assist_method: 
- anatomy_repair_policy: correct any distortion in facial features or ornaments
- consistency_targets: 
- style_profile: action-oriented awe-inspiring tense melancholic regarding destruction
- batch_role: strong initial test clip
- fix_of: 

# Continuity Notes
- Maintain companion character expression urgency throughout duration.
- Ensure eye line locks with observer character at 3s mark to prepare cut to CL004.
- Lighting must reflect exterior corridor context with smoke shadows from battle.
- Avoid showing green_martian_warriors or other characters in frame unless minimal background presence.
- Keep focus on emotional intensity and connection initiation between characters.

# Repair Notes
- If facial expression unclear, tighten to extreme close-up on eyes immediately.
- If background too busy, simplify to focus solely on companion character face.
- If lighting inconsistent with battle context, adjust shadows to match smoke effects.
- If ornaments missing or incorrect, ensure highly wrought ornaments are visible and consistent.
- If coiffure does not match coal black waving loosely caught style, correct hair texture and arrangement.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
