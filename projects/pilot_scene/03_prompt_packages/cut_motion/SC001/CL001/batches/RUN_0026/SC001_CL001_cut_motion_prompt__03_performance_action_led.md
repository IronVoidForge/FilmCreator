# Title
SC001 CL001 Cut Motion Prompt [03 performance_action_led]

# ID
SC001_CL001_cut_motion_prompt_03_performance_action_led

# Purpose
Generate the first approved cut-motion pass from the approved opening keyframe while preserving identity, environment, and composition continuity.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Lead with subject behavior, interaction, body language, and visible action before secondary camera details.

Start from the provided opening duel frame and preserve the exact visible identities, costumes, proportions, lighting, architecture, and overall composition from that image. Two combatants hold crossed blades on a circular platform inside a monumental pale alien command chamber with ribbed nonhuman arches, cold sculptural overhead light, and faint haze. Motion should stay restrained and elegant. Use a slow cinematic push-in with a slight rightward drift. The lean dark-haired human duelist makes two tiny blade adjustments and a measured half-step inward, testing the bind without breaking the tableau. The taller pale alien prince answers with a controlled forward press, a subtle wrist turn, and a small shift of weight that keeps visible dominance. Let haze drift softly, let fabric and armor tails move slightly, and allow a faint seam-light pulse in the distant walls. No strike lands, no blood, no new characters, no costume changes, no room redesign, no abrupt camera move, and no chaotic action.

# Negative Prompt
identity drift, face drift, anatomy errors, extra limbs, extra weapons, duplicate characters, costume redesign, room redesign, hard cut, jumpy camera, fast action, impact hit, blood, gore, explosion, debris burst, comedy, text, watermark, logo

# Inputs
- project_id: pilot_scene
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: source_frame
- optional_refs: 
- style_profile: performance_action_led
- batch_role: candidate_03
- fix_of: 

# Continuity Notes
- Use the approved keyframe as the only starting image for the motion pass.
- Preserve the duel axis, chamber layout, costume silhouettes, and cold pale lighting.
- Keep motion small, readable, and unresolved so the cut can still feed later refinement.
- Generated batch candidate 03 for style profile 'performance_action_led'.

# Sources
- projects/pilot_scene/02_story_analysis/clip_plans/SC001/CL001.md
