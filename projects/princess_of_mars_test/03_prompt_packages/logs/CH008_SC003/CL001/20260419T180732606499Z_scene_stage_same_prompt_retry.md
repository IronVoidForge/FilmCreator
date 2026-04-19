# FilmCreator Prompt Writing Exchange
- timestamp_utc: 2026-04-19T18:07:32.606499+00:00
- stage: scene_stage
- clip_id: CL001
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
Target stage: scene_stage
Stage guidance: Describe staging intent, subject placement, environmental context, and the intended visible opening frame setup. This is authoring-only and should not read like a render prompt for a model.
Use descriptive noun phrases and avoid proper nouns in prompt text.
Keep duration and workflow metadata in inputs_markdown, not in the prompt body.
Follow the requested section names exactly.
````

## User Prompt
````text
Project: princess_of_mars_test

Scene: CH008_SC003

Clip: CL001

Prompt title: CH008_SC003 CL001 Scene Stage Prompt

Prompt id: CH008_SC003_CL001_scene_stage_prompt

Workflow type: authoring.scene_stage

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

stage: scene_stage

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

# CH008_SC003_CL001 - Wide Tracking Shot of Drifting Craft from Building Roofs

## Continuity Mode
tracking_shot_of_drifting_craft

## Composition Type
wide_angle

## Starting Keyframe Strategy
establishing_wide_frame_from_building_roof_position

## Dependency Policy
independent_opening_keyframe_with_contextual_reference_to_bodies_strewn_about

## Fallback Strategy
reframe_same_moment_if_tracking_fails_to_show_vertical_axis

## Visible Character Assets
green_warriors_on_building_roofs, drifting_craft_in_plain_below

## Required Refs
CH008_SC003_BT001.md (boarding action beat documentation)

## Optional Refs
CH008_SC003_scene_breakdown.md (overall scene context)

## Opening Keyframe Intent
show_drifting_craft_positioned_centrally_in_frame_with_building_roofs_as_elevated_approach_point

## Cut Motion Intent
smooth_tracking_motion_following_warriors_movement_from_roof_to_plain

## Interval Beats
- 0s: Warriors visible on building roofs, drifting craft in plain below
- 2.5s: Tracking motion emphasizes vertical axis between roof and plain
- 5s: Movement from roof to craft complete, focus shifts to craft interior

## Scene Breakdown

# CH008_SC003 - Aftermath and Discovery

## Scene Purpose
Shift focus to aftermath and discovery of prisoner.

## Scene Summary
Warriors board drifting craft, haul to ground, discover prisoner.

## Participating Characters
Green Warriors, Prisoner (Human Woman)

## Participating Environments
Building roofs, plain, building south of position

## Dominant Emotional Shift
Curiosity to Discovery/Concern

## Likely Visual Coverage Families
Tracking shots of drifting craft, close-ups on boarding action, medium shot of prisoner being dragged

## Likely Continuity Sensitivities
Bodies strewn about, no sign of life, creature less than half as tall, walks erect.

## Beat Bundles

## BT001.md
# CH008_SC003_BT001 - Boarding Action Beat

## Beat Purpose
Warriors approach and board drifting craft. Establishes aftermath of battle and transition to prisoner recovery.

## Start State
- Warriors positioned on building roofs
- Drifting craft visible in plain below
- Bodies strewn about, no sign of life
- Creature less than half as tall, walks erect

## End State
- Warriors successfully board drifting craft
- Movement from roof to craft complete
- Focus shifts to prisoner inside craft

## Character Placement and Movement Logic
- Green Warriors move from building roofs down to plain
- Approach craft with tactical formation
- Boarding action shows coordination between warriors
- Prisoner remains stationary inside craft during boarding

## Geography, Axis, or Eyeline Facts
- Building roofs serve as elevated approach point
- Plain below provides vertical axis for tracking shots
- Drifting craft positioned centrally in frame
- Eyelines directed toward craft interior

## Prop, Vehicle, Crowd, and Environmental State
- Bodies strewn about (continuity element)
- No sign of life (establishes aftermath)
- Creature less than half as tall (size reference)
- Walks erect (behavioral note)
- Drifting craft shows damage from battle

## Likely Coverage Families
- Tracking shots of drifting craft
- Close-ups on boarding action
- Wide shots showing building roofs to plain transition
- Medium shots of warrior movement

## BT002.md
# CH008_SC003_BT002 - Haul to Ground Beat

## Beat Purpose
Drag prisoner from craft to ground. Establishes physical recovery and warrior concern for prisoner.

## Start State
- Warriors inside drifting craft
- Prisoner visible inside craft
- Craft positioned in plain below building roofs

## End State
- Prisoner successfully hauled to ground
- Warrior team surrounds prisoner on plain
- Focus shifts to prisoner's condition

## Character Placement and Movement Logic
- Warriors coordinate drag operation from craft interior
- Green Warriors maintain formation during haul
- Prisoner dragged across plain surface
- Movement shows tactical care for prisoner

## Geography, Axis, or Eyeline Facts
- Plain provides horizontal movement axis
- Building south of position serves as reference point
- Vertical drop from craft to ground emphasized
- Eyelines directed toward prisoner's face and body

## Prop, Vehicle, Crowd, and Environmental State
- Bodies strewn about (continuity element)
- No sign of life (establishes aftermath)
- Creature less than half as tall (size reference)
- Walks erect (behavioral note)
- Plain surface shows drag marks

## Likely Coverage Families
- Medium shot of prisoner being dragged
- Tracking shots following haul operation
- Close-ups on warrior hands during drag
- Wide shots showing plain and building context

## BT003.md
# CH008_SC003_BT003 - Discovery Beat

## Beat Purpose
Warriors discover the prisoner. Establishes emotional shift from curiosity to concern and discovery.

## Start State
- Warriors on plain after hauling prisoner
- Prisoner positioned on ground
- Building south of position visible in background

## End State
- Warriors fully aware of prisoner's presence
- Emotional shift to Discovery/Concern established
- Scene transitions to aftermath processing

## Character Placement and Movement Logic
- Warriors gather around prisoner on plain
- Green Warriors show concern through positioning
- Prisoner remains stationary, discovered state
- Movement shows tactical assessment of situation

## Geography, Axis, or Eyeline Facts
- Building south of position provides background reference
- Plain serves as discovery location
- Vertical axis from craft to ground complete
- Eyelines directed toward prisoner's face and condition

## Prop, Vehicle, Crowd, and Environmental State
- Bodies strewn about (continuity element)
- No sign of life (establishes aftermath)
- Creature less than half as tall (size reference)
- Walks erect (behavioral note)
- Plain environment shows drag operation completion

## Likely Coverage Families
- Close-ups on boarding action (contextual)
- Medium shots showing prisoner discovery
- Wide shots establishing building and plain context
- Tracking shots following warrior assessment

## Clip Roster

# CH008_SC003 Clip Roster

## CL001 - Wide Tracking Shot of Drifting Craft from Building Roofs (BT001)
**Purpose:** Establish aftermath and vertical axis for boarding action  
**Duration:** ~5 seconds  
**Continuity Mode:** tracking_shot_of_drifting_craft  
**Composition Type:** wide_angle  

## CL002 - Close-up Boarding Action Showing Warriors Approaching Craft (BT001)
**Purpose:** Show coordination between warriors during approach  
**Duration:** ~5 seconds  
**Continuity Mode:** close_ups_on_boarding_action  
**Composition Type:** medium_shot  

## CL003 - Medium Shot Warriors Successfully Board Craft (BT001)
**Purpose:** Complete movement from roof to craft  
**Duration:** ~5 seconds  
**Continuity Mode:** tracking_shows_building_roofs_to_plain_transition  
**Composition Type:** wide_shot  

## CL004 - Medium Shot Prisoner Being Dragged Across Plain (BT002)
**Purpose:** Establish physical recovery and warrior concern  
**Duration:** ~5 seconds  
**Continuity Mode:** medium_shot_of_prisoner_being_dragged  
**Composition Type:** medium_shot  

## CL005 - Tracking Shot Following Haul Operation (BT002)
**Purpose:** Show tactical care for prisoner during drag  
**Duration:** ~5 seconds  
**Continuity Mode:** tracking_shots_following_haul_operation  
**Composition Type:** wide_shot  

## CL006 - Medium Shots Showing Prisoner Discovery (BT003)
**Purpose:** Establish emotional shift from curiosity to concern  
**Duration:** ~5 seconds  
**Continuity Mode:** medium_shows_prisoner_discovery  
**Composition Type:** medium_shot

## Clip State

{
  "project_id": "princess_of_mars_test",
  "scene_id": "CH008_SC003",
  "clip_id": "CL001",
  "status": "planning",
  "inputs": {
    "shared_character_refs": [],
    "shared_environment_refs": [],
    "scene_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC003/CL001/CH008_SC003_CL001_scene_stage_prompt.md",
    "scene_stage_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/scenes/CH008_SC003/CL001/CH008_SC003_CL001_scene_stage_prompt.md",
    "keyframe_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/keyframes/CH008_SC003/CL001/CH008_SC003_CL001_keyframe_prompt.md",
    "fix_prompt_packages": [
      "projects/princess_of_mars_test/03_prompt_packages/fixes/CH008_SC003/CL001/CH008_SC003_CL001_fix_01_prompt.md"
    ],
    "anchor_prompt_packages": [],
    "video_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC003/CL001/CH008_SC003_CL001_cut_motion_prompt.md",
    "cut_motion_prompt_package": "projects/princess_of_mars_test/03_prompt_packages/cut_motion/CH008_SC003/CL001/CH008_SC003_CL001_cut_motion_prompt.md",
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
    }
  }
}



Existing prompt draft:

# Title
CH008_SC003 CL001 Scene Stage Prompt

# ID
CH008_SC003_CL001_scene_stage_prompt

# Purpose
Introduce Earthling captive and establish cultural misunderstanding regarding her treatment. Group returns to plaza center from left side at 45-degree camera angle. Medium shot composition capturing Green Martian females dragging copper-skinned woman with black hair into building entrance. Narrator positioned edge of frame maintaining fixed gaze. Plaza environment features copper flooring reflecting ambient light, building entrance is 3-meter wide archway with shadowed interior. Staging intent focuses on establishing group approach movement, captive's physical characteristics (oval face, finely chiseled features, large lustrous eyes, coal black waving hair caught loosely), and narrator's observational position without participation in action.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martian females 2-3 dragging Earthling woman with copper skin and black hair into building entrance archway, plaza center with copper flooring reflecting daylight, narrator edge of frame right side maintaining fixed gaze, medium shot composition, open plaza space 15 meters depth, building entrance shadowed interior creating depth contrast, V-shape formation visible during group approach, oval face finely chiseled features large lustrous eyes coal black waving hair caught loosely, light reddish copper color with crimson glow of cheeks and ruby lips, daylight ambient lighting, no modern clothing, no weapons visible, static camera position

# Negative Prompt
modern clothing, human faces on Martians, weapons or ammunition visible, indoor shadows too dark, camera movement toward action, close-up only shots, wide establishing shots from different angle, night lighting effects, fire illumination during this sequence, narrator participating in dragging action, building interior fully lit, copper flooring not reflecting light, contemporary technology elements, mechanical devices, urban transit vehicles

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL001
- duration_seconds: 15
- required_refs: BT001.md, CH008_SC003/BEAT_INDEX.md
- optional_refs: plaza_environment_assets.md
- visible_character_assets: 2-3 Green Martian females, Narrator edge of frame, copper-skinned Earthling woman
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_opening
- dependency_policy: independent
- auto_advance_policy: manual_review
- fallback_strategy: insert_alternate_angle
- consistency_assist_policy: enabled
- consistency_assist_method: anatomical_verification
- anatomy_repair_policy: strict
- consistency_targets: copper_skin_texture, black_hair_contrast, green_martian_skin_tone, narrator_eyeline_direction
- style_profile: classic_narrative_film
- batch_role: scene_stage_authoring
- fix_of: 

# Continuity Notes
- Captive's copper skin texture must remain consistent across all frames with light reddish copper color and crimson glow of cheeks
- Black hair caught loosely must show coal black waving texture without modern styling elements
- Green Martian females maintain uniform green skin tone throughout sequence
- Narrator positioned at right edge of frame maintaining fixed gaze on captive throughout beats
- Plaza depth spans 15 meters with copper flooring reflecting ambient daylight lighting
- Building entrance is 3-meter wide archway with shadowed interior creating depth contrast
- Group enters from left side forming V-shape formation visible during approach
- No character movement toward camera except for lateral movement into building
- Daylight ambient lighting maintained without fire illumination effects in this sequence

# Repair Notes
- Ensure captive's naked state is handled with appropriate cultural context accuracy
- Maintain continuity of narrator's silence and lack of participation in dragging action
- Avoid modern lighting effects that would contradict valley city environment
- Verify copper flooring reflection matches ambient daylight intensity across all frames
- Confirm building entrance shadow depth creates proper visual closure when captive enters
- Check that no weapons or ammunition are visible on any character during this sequence
- Ensure Martians' green skin tone remains consistent without contamination from lighting effects

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md

````

## Raw Response
````text

````
