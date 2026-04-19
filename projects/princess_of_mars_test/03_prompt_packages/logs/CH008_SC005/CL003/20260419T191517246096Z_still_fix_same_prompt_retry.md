# FilmCreator Prompt Writing Exchange
- timestamp_utc: 2026-04-19T19:15:17.246096+00:00
- stage: still_fix
- clip_id: CL003
- retry_kind: same_prompt_retry

## System Prompt
````text
You are writing one FilmCreator prompt package for a local generation pipeline.
Your first output line must be exactly [[FILMCREATOR_PACKET]].
Your last output line must be exactly [[/FILMCREATOR_PACKET]].
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Do not omit the outer packet envelope.
Target stage: still_fix
Stage guidance: Write a corrective still-generation prompt that preserves composition and look while fixing local issues. Assume image_1 is the approved still base and image_2 is a secondary reference when needed.
Use descriptive noun phrases and avoid proper nouns in prompt text.
Keep duration and workflow metadata in inputs_markdown, not in the prompt body.
Follow the requested section names exactly.
````

## User Prompt
````text
Project: princess_of_mars_test

Scene: CH008_SC005

Clip: CL003

Prompt title: CH008_SC005 CL003 Fix 01 Prompt

Prompt id: CH008_SC005_CL003_fix_01_prompt

Workflow type: still.scene_insert.two_ref.klein.distilled

Write improved content for this canonical prompt package.

Output rules:

1. First line must be [[FILMCREATOR_PACKET]]

2. Last line must be [[/FILMCREATOR_PACKET]]

3. No text before the first line

4. No text after the last line

5. Every required section must appear exactly once



Use this exact packet envelope and section names:

[[FILMCREATOR_PACKET]]

task: clip_prompt

stage: still_fix

version: 1



[[SECTION purpose]]

...purpose text...

[[/SECTION]]



[[SECTION positive_prompt]]

...positive prompt text...

[[/SECTION]]



[[SECTION negative_prompt]]

...negative prompt text...

[[/SECTION]]



[[SECTION inputs_markdown]]

- key: value

[[/SECTION]]



[[SECTION continuity_notes_markdown]]

- note

[[/SECTION]]



[[SECTION repair_notes_markdown]]

- note

[[/SECTION]]

[[/FILMCREATOR_PACKET]]



Clip context:

## Project Summary

# Project Summary

**Title:** A Princess of Mars Test Project
**Slug:** princess_of_mars_test

**Setting:** Barsoom (Mars). Primary locations include a large Martian city with spacious doorways, upper floors, roofs, and the surrounding valley/hills. The environment features open plains and distant hills.

**Key Characters:**
- **John Carter:** Human protagonist, observer of events from windows/roofs.
- **Sola:** Companion, present in the plaza and procession.
- **Woola:** Hound companion, follows Carter closely.
- **Green Martians:** Warriors inhabiting the city buildings; use chariots, mastodons, mounted warriors.
- **Air Fleet Crews:** Operate large gray-painted air craft with wireless finding apparatus.

**Core Themes:** Aerial warfare, inter-species conflict (Green Martians vs. Air Fleet), rescue operations, discovery of new life forms.

**Tone:** Action-oriented, awe-inspiring, tense during combat sequences, melancholic regarding the destruction of the fleet.

## Chapter Summaries

## CH008_summary.md
# Chapter Summary: CH008 - A Fair Captive from the Sky

## Story Summary
The narrative begins on the third day after an incubator ceremony. The procession retreats to a city building due to an immediate order. From a window, John Carter observes the arrival of twenty large gray air craft. A battle ensues between Green Martians firing from buildings and the Air Fleet returning fire. The fleet retreats after damage; one ship is disabled and unmanned. Warriors loot the vessel (arms, jewels, water), burn it, and tow it away before it explodes. Carter witnesses a human female prisoner being dragged from the burning ship into a nearby building by Green Martian females. At the city plaza, the prisoner turns to Carter as she enters the building; he fails to respond to her signal of appeal. She is dragged away into the depths of the edifice.

## Visual Continuity
- **Air Craft:** Long, low, gray-painted vessels with strange banners and odd devices on prows. Figures crowd forward decks.
- **Green Martians:** Green skin, wear ornaments, carry spears, fire from windows/roofs.
- **Prisoner:** Slender, girlish figure. Skin is light reddish copper. Features finely chiseled. Eyes large/lustrous. Hair coal black, waving, caught loosely into a strange coiffure. Naked except for highly wrought ornaments. Cheeks crimson, lips ruby.
- **Locations:** City buildings (upper floors, windows, roofs), open ground/plaza, valley, hills beyond.
- **Action Details:** Ships swing broadside, dip below hill crests, drift southeast/southwesterly. Fire causes spurt of flame from missile impact. Guy ropes release simultaneously.

## Character Index

# Character Index - Chapter CH008

| Asset ID | Canonical Character ID | Display Name | Role | Physical Presence |
|----------|------------------------|--------------|------|-------------------|
| john_carter | john_carter | John Carter | Observer, Witness | Present |
| human_female_prisoner | prisoner_human_female | Human Female Prisoner | Captive, Appeal Signal | Referenced |
| green_martian_warriors | green_martian_warrior | Green Martian Warriors | Combatants, Looters | Referenced |
| green_martian_females | green_martian_female | Green Martian Females | Draggers, Enforcers | Referenced |

**Notes:**
- John Carter: Physically present observing from window; witnesses prisoner's appeal
- Human Female Prisoner: Detailed visual description provided in chapter; signals to Carter
- Green Martians: Multiple individuals; described as group with consistent physical traits
- All characters have sufficient identification for continuity tracking

## Environment Index

# Environment Index - CH008

## Extracted Environments

| Asset ID | Role | Primary Geography | Atmosphere Cues |
|----------|------|-------------------|-----------------|
| city_buildings | primary | urban structures, upper floors, windows, roofs | daylight, smoke from fire, missile impact flames |
| open_ground_plaza | transit | open ground, plaza area | daylight, spurt of flame from impacts |
| valley | secondary | valley floor beyond city | daylight, distant horizon |
| hills_beyond | secondary | hill crests, slopes southeast/southwesterly | daylight, dip below crests |

## Environment Families Summary

- **city_buildings**: Primary observation and action setting with multiple levels
- **open_ground_plaza**: Transit zone for fleet movement and battle effects
- **valley**: Background geography establishing scale
- **hills_beyond**: Distant geography providing directional context

## Clip Plan

# CL003 - Eye Contact & Reaction (Emotional Anchor)

## Continuity Mode
- **Mode**: cutaway_to_action
- **Policy**: Ensure gaze exchange continuity; character positioning must match BT003 start/end.

## Composition Type
- **Type**: medium_close_up
- **Focus**: Carter's reaction and Sola's proximity; multi-directional gaze exchange.

## Starting Keyframe Strategy
- **Strategy**: insert_from_reaction
- **Intent**: Begin with Carter's reactive state after previous beats; emotional tension peaks.

## Dependency Policy
- **Policy**: reblock_same_scene
- **Fallback**: If medium close-up unavailable, use close-up (Carter reaction) or wide shot showing all three parties.

## Fallback Strategy
- **Fallback**: over_the_shoulder_from_sola_observing_carter_reaction if emotional state requires perspective shift.

## Visible Character Assets
- **Carter**: Upper body visible, central position, reactive to both Sola and prisoner.
- **Sola**: Positioned near Carter, may maintain or shift gaze based on emotional state.
- **Prisoner**: Background position, may make eye contact if visible in coverage.

## Required Refs
- `projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC005/BEAT_INDEX.md`
- `projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC005/BT003.md`

## Optional Refs
- `projects/princess_of_mars_test/02_story_analysis/shot_plans/CL003_shot_plan.md` (if exists)

## Opening Keyframe Intent
- **Intent**: Establish emotional reaction registered; scene tension peaks, connection established.

## Cut Motion Intent
- **Motion**: smooth_gaze_exchange
- **Note**: Ensure eyeline tracking is clear for coverage planning; multi-directional gaze exchange between all parties.

## Interval Beats
- **Beat 1 (0s-2s)**: All three characters positioned for potential gaze interaction after previous beats.
- **Beat 2 (2s-4s)**: Emotional reaction registered; scene tension peaks, connection established.
- **Beat 3 (4s-5s)**: Gaze exchange complete; emotional anchor set for subsequent scene coverage.

## Scene Breakdown

# CH008_SC005 - Carter & Prisoner Connection

## Scene Purpose
Establish connection between Carter and prisoner through Sola's intervention.

## Scene Summary
Sola rushes to Carter, glimpse of prisoner dragged into building, eye contact established between all parties.

## Staging Facts
- **Location**: Exterior corridor / Building entrance threshold
- **Axis**: Sola enters from left; Carter stands center-right facing camera; Prisoner moves background right-to-left
- **Time**: Immediate urgency (Sola's rush implies chase or rescue)
- **Key Props**: None specific, focus on physical movement and gaze

## Beat Breakdown
1. **BT001**: Sola Rushes In (Connection Initiation)
2. **BT002**: Prisoner Dragged Through View (Conflict Introduction)
3. **BT003**: Eye Contact & Reaction (Emotional Anchor)

## Beat Bundles

## BT001.md
# BT001 - Sola Rushes In (Connection Initiation)

## Beat Purpose
Initiate connection between Carter and Sola through urgent physical approach.

## Start State
Sola visible at distance, moving toward Carter who stands stationary center-right.

## End State
Sola reaches Carter's position, establishes physical contact or close proximity.

## Character Placement & Movement Logic
- **Sola**: Enters from left frame, diagonal movement toward center-right where Carter stands
- **Carter**: Stationary, facing camera, minimal movement during beat
- **Prisoner**: Background movement right-to-left, out of primary focus but present

## Geography, Axis, Eyeline Facts
- Primary axis: Left-to-center-right (Sola to Carter)
- Secondary axis: Background right-to-left (Prisoner movement)
- Eyeline: Sola's gaze directed at Carter; Carter's gaze initially neutral then reactive

## Prop, Vehicle, Crowd, Environmental State
- **Environment**: Exterior corridor with building entrance threshold visible
- **Crowd**: Minimal to none, focus on three main characters
- **Props**: None specific, emphasis on physical presence and movement
- **Continuity**: Sola's clothing state upon arrival affects subsequent scene coverage

## Likely Coverage Families
- Wide two-shot (Sola approaching Carter)
- Medium close-up (Carter reaction)
- Over-the-shoulder (Sola's perspective of Carter)
- Tracking shot following Sola's movement

## BT002.md
# BT002 - Prisoner Dragged Through View (Conflict Introduction)

## Beat Purpose
Introduce conflict element through prisoner's forced movement across frame.

## Start State
Prisoner visible in background, moving right-to-left across building entrance threshold.

## End State
Prisoner disappears into building interior, establishing threat/conflict presence.

## Character Placement & Movement Logic
- **Prisoner**: Background movement right-to-left, dragging motion through entrance
- **Carter**: Maintains position, observes prisoner movement
- **Sola**: May react to prisoner's appearance depending on beat timing

## Geography, Axis, Eyeline Facts
- Primary axis: Background right-to-left (prisoner trajectory)
- Secondary axis: Left-to-center-right (maintained from BT001)
- Eyeline: Carter and Sola may shift gaze toward prisoner movement
- Depth layering: Prisoner in background plane, Carter/Sola in foreground

## Prop, Vehicle, Crowd, Environmental State
- **Environment**: Building entrance threshold with interior visible behind
- **Crowd**: None specific, focus on prisoner's isolated movement
- **Props**: Dragging motion may involve unseen restraint or force
- **Continuity**: Prisoner's clothing state upon entry affects subsequent coverage

## Likely Coverage Families
- Wide shot showing full background movement
- Medium shot (Carter/Sola foreground with prisoner visible in background)
- Over-the-shoulder from Carter observing prisoner
- Rack focus between foreground characters and background prisoner

## BT003.md
# BT003 - Eye Contact & Reaction (Emotional Anchor)

## Beat Purpose
Establish emotional anchor through gaze exchange between all parties.

## Start State
All three characters positioned for potential gaze interaction after previous beats.

## End State
Emotional reaction registered, scene tension peaks, connection established.

## Character Placement & Movement Logic
- **Carter**: Central position, reactive to both Sola's arrival and prisoner's presence
- **Sola**: Positioned near Carter, may maintain or shift gaze based on emotional state
- **Prisoner**: Background position, may make eye contact if visible in coverage

## Geography, Axis, Eyeline Facts
- Primary axis: Left-to-center-right (Sola to Carter connection)
- Secondary axis: Background right-to-left (prisoner presence)
- Eyeline: Multi-directional gaze exchange between all parties
- Emotional beats require clear eyeline tracking for coverage planning

## Prop, Vehicle, Crowd, Environmental State
- **Environment**: Exterior corridor with building entrance threshold
- **Crowd**: Minimal, focus on character emotional states
- **Props**: None specific, emphasis on facial expressions and body language
- **Continuity**: Character positioning affects subsequent scene emotional beats

## Likely Coverage Families
- Close-up (Carter reaction)
- Medium close-up (Sola and Carter together)
- Wide shot showing all three parties in frame
- Over-the-shoulder from Sola observing Carter's reaction
- Rack focus between foreground characters and background prisoner

## Clip Roster

# CH008_SC005 - Clip Roster

| Clip ID | Beat Reference | Description | Duration (Target) |
|---------|----------------|--------------|-------------------|
| CL001 | BT001 | Sola Rushes In (Connection Initiation) | 5s |
| CL002 | BT002 | Prisoner Dragged Through View (Conflict Introduction) | 5s |
| CL003 | BT003 | Eye Contact & Reaction (Emotional Anchor) | 5s |

## Clip State

{
  "project_id": "princess_of_mars_test",
  "scene_id": "CH008_SC005",
  "clip_id": "CL003",
  "status": "planning",
  "inputs": {
    "shared_character_refs": [],
    "shared_environment_refs": [],
    "scene_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC005/CL003/CH008_SC005_CL003_scene_stage_prompt.md",
    "scene_stage_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC005/CL003/CH008_SC005_CL003_scene_stage_prompt.md",
    "keyframe_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/keyframes/CH008_SC005/CL003/CH008_SC005_CL003_keyframe_prompt.md",
    "fix_prompt_packages": [
      "projects/princess_of_mars_test/03_prompt_packages/fixes/CH008_SC005/CL003/CH008_SC005_CL003_fix_01_prompt.md"
    ],
    "anchor_prompt_packages": [],
    "video_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC005/CL003/CH008_SC005_CL003_cut_motion_prompt.md",
    "cut_motion_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC005/CL003/CH008_SC005_CL003_cut_motion_prompt.md",
    "legacy_anchor_prompt_packages": [],
    "legacy_video_prompt_package": null
  },
  "approved_assets": {
    "golden_frame": null,
    "approved_keyframe": null,
    "approved_video": null,
    "still_fixes": [],
    "anchor_frames": [],
    "interval_frames": [],
    "cut_motion_videos": []
  },
  "approved_video_last_frame": null,
  "current_continuity_source": null,
  "latest_runs": {},
  "review_batches": [],
  "latest_review_decision": null,
  "notes": [],
  "stage_style_preferences": {
    "cut_motion": {
      "literal_descriptive": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "cinematic_compositional": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "performance_action_led": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "sparse_conservative": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      }
    },
    "keyframe": {
      "literal_descriptive": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "cinematic_compositional": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "performance_action_led": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "sparse_conservative": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      }
    },
    "still_fix": {
      "literal_descriptive": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "cinematic_compositional": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "performance_action_led": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      },
      "sparse_conservative": {
        "appearances": 0,
        "top_two": 0,
        "wins": 0
      }
    }
  }
}



Existing prompt draft:

# Title
CH008_SC005 CL003 Fix 01 Prompt

# ID
CH008_SC005_CL003_fix_01_prompt

# Purpose
Corrective still generation for CL003 close-up on human female companion. Preserves emotional urgency and visual continuity while addressing local artifacts or anatomical inconsistencies in the approved base image. Ensures facial expression clarity and lighting consistency with previous shots (daylight, corridor shadows).

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Close up portrait of human female companion, coal black hair loosely caught into strange coiffure, crimson cheeks, ruby lips, expression of urgency and determination, daylight lighting with corridor shadows, focus on eyes locked forward, high fidelity facial details, green skin context implied by environment, minimal background clutter, sharp focus on face.

# Negative Prompt
distorted face, extra fingers, wrong hair color, text, watermark, blurry, low resolution, mismatched lighting, green skin on human unless context requires, extra limbs, facial asymmetry, poor anatomy, low contrast, noisy background.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md End State
- optional_refs: None
- visible_character_assets: Sola (face, eyes, upper body)
- look_continuity_policy: Maintain emotional intensity and lighting consistency with CL002
- intended_lighting_change: None
- composition_type: Close Up
- continuity_mode: insert
- starting_keyframe_strategy: Static close frame on face showing urgency
- dependency_policy: Depends on CL002 establishing spatial context
- auto_advance_policy: Standard
- fallback_strategy: Tighten to extreme close-up on eyes if expression unclear
- consistency_assist_policy: Enable
- consistency_assist_method: Face focus
- anatomy_repair_policy: Strict
- consistency_targets: Facial features, hair coiffure, lighting direction
- style_profile: Action-oriented, awe-inspiring
- batch_role: Fix 01
- fix_of: CL003 Base Image

# Continuity Notes
- Sola's expression must convey both desperation and purpose.
- Lighting should match daylight with smoke effects from nearby battle.
- Hair coiffure must remain consistent with canonical style (loose, strange).
- Composition remains close-up on face and upper body only.
- Eye contact prepares for cut to CL004 reaction shot.

# Repair Notes
- Fix any distorted facial features or asymmetry in the base image.
- Ensure eyes are sharp and focused forward, not looking away.
- Correct lighting shadows to match corridor environment consistency.
- Verify hair strands do not blend into background incorrectly.
- Maintain skin tone consistency with human female companion profile.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: clip_prompt
stage: still_fix
version: 1

[[SECTION purpose]]
Corrective still generation for CL003 close-up on human female companion. Preserves emotional urgency and visual continuity while addressing local artifacts or anatomical inconsistencies in the approved base image. Ensures facial expression clarity and lighting consistency with previous shots (daylight, corridor shadows).
[[/SECTION]]

[[SECTION positive_prompt]]
Close up portrait of human female companion, coal black hair loosely caught into strange coiffure, crimson cheeks, ruby lips, expression of urgency and determination, daylight lighting with corridor shadows, focus on eyes locked forward, high fidelity facial details, green skin context implied by environment, minimal background clutter, sharp focus on face.
[[/SECTION]]

[[SECTION negative_prompt]]
distorted face, extra fingers, wrong hair color, text, watermark, blurry, low resolution, mismatched lighting, green skin on human unless context requires, extra limbs, facial asymmetry, poor anatomy, low contrast, noisy background.
[[/SECTION]]

[[SECTION inputs_markdown]]
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md End State
- optional_refs: None
- visible_character_assets: Sola (face, eyes, upper body)
- look_continuity_policy: Maintain emotional intensity and lighting consistency with CL002
- intended_lighting_change: None
- composition_type: Close Up
- continuity_mode: insert
- starting_keyframe_strategy: Static close frame on face showing urgency
- dependency_policy: Depends on CL002 establishing spatial context
- auto_advance_policy: Standard
- fallback_strategy: Tighten to extreme close-up on eyes if expression unclear
- consistency_assist_policy: Enable
- consistency_assist_method: Face focus
- anatomy_repair_policy: Strict
- consistency_targets: Facial features, hair coiffure, lighting direction
- style_profile: Action-oriented, awe-inspiring
- batch_role: Fix 01
- fix_of: CL003 Base Image
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
- Sola's expression must convey both desperation and purpose.
- Lighting should match daylight with smoke effects from nearby battle.
- Hair coiffure must remain consistent with canonical style (loose, strange).
- Composition remains close-up on face and upper body only.
- Eye contact prepares for cut to CL004 reaction shot.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
- Fix any distorted facial features or asymmetry in the base image.
- Ensure eyes are sharp and focused forward, not looking away.
- Correct lighting shadows to match corridor environment consistency.
- Verify hair strands do not blend into background incorrectly.
- Maintain skin tone consistency with human female companion profile.
[[/SECTION]]
[[/FILMCREATOR_PACKET]]
````
