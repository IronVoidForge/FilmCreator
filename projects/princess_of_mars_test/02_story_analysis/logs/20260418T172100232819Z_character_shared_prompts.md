# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:21:00.232819+00:00
- task: character_shared_prompts

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Work like a careful local planning assistant for chapter analysis and shot-prep authoring.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
Prefer short, concrete section bodies over long prose.
Follow the requested headings and record fields exactly.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
If information is missing, say so briefly instead of guessing.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Asset id: sola_ch001

Task: write one reusable shared character-reference prompt draft for stable local generation.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: <value>

[[SECTION purpose]]
...purpose content...
[[/SECTION]]

[[SECTION positive_prompt]]
...positive_prompt content...
[[/SECTION]]

[[SECTION negative_prompt]]
...negative_prompt content...
[[/SECTION]]

[[SECTION inputs_markdown]]
...inputs_markdown content...
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
...continuity_notes_markdown content...
[[/SECTION]]

[[SECTION repair_notes_markdown]]
...repair_notes_markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Rules:

- purpose and inputs may use stable asset ids

- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases

- keep prompts concrete and visible

- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/sola_ch001.md

# Sola (CH001)

## Display Name
Sola

## Chapter Role
Companion / Guide

## Physical Presence
Present at plaza upon arrival

## Physical Description
Not described in source material. No physical attributes provided for reliable image generation.

## Costume & Silhouette
Unknown. No costume details available in chapter text.

## Continuity-Critical Traits
- Rushes up to narrator upon arrival at plaza
- Appears to be familiar with narrator (implied relationship)

## Render-Facing Prompt Notes
- Requires manual description for image generation
- Consider approach from plaza toward narrator
- May need clarification on species, age, or distinguishing features

## Uncertainty Notes
**CRITICAL:** No physical description provided in source material. Cannot generate dependable images without additional details about appearance, age, gender, or distinguishing features.

# Aliases

-



# Canonical Character ID

sola



# Fully Identified

true

# Manual Description Input Required

Yes



# Manual Description Reason

No physical description provided in source material; only name and action (rushes to narrator) documented




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/sola_ch001_manual_description.md

<!-- FILMCREATOR_MANUAL_PLACEHOLDER -->

# Asset ID
sola_ch001

# Purpose
Paste a stable manual visual description for this character so later shared reference generation can use it.

# Why This Is Needed
No physical description provided in source material; only name and action (rushes to narrator) documented

# Guidance
- describe face, hair, body type, age impression, silhouette, skin tone, costume logic, and any continuity-critical marks
- prefer visible facts over backstory
- if multiple looks exist, describe the default look for this chapter

# Manual Description

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: sola_ch001

[[SECTION purpose]]
Manual visual description required for stable image generation. Source material provides only name and action (rushes to narrator at plaza). No physical attributes, costume details, or distinguishing features documented in chapter text. Requires additional clarification on species, age, gender, and appearance before reliable shared reference prompts can be created.

[[/SECTION]]

[[SECTION positive_prompt]]
young companion figure approaching from plaza direction, familiar with narrator, neutral expression, soft lighting, approachable silhouette, casual attire, warm skin tone, flowing hair, gentle posture, welcoming presence, detailed facial features, natural body proportions, contemporary clothing style, visible character design elements

[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific species names, exact age markers, gender indicators, costume brand names, scene-specific blocking, background details, narrator interaction specifics, plaza environment elements, action sequences, dialogue bubbles, text overlays, exaggerated features, unrealistic proportions, harsh lighting, dark shadows, cluttered composition, multiple character appearances, inconsistent design

[[/SECTION]]

[[SECTION inputs_markdown]]
# Manual Description Input Required

## Current Status
No physical description provided in source material for reliable image generation.

## Required Clarifications
- Species or humanoid classification
- Age impression (child, young adult, adult)
- Gender presentation
- Face structure and features
- Hair style and color
- Body type and proportions
- Skin tone
- Costume logic and materials
- Any continuity-critical marks or accessories

## Suggested Approach
Consider describing from plaza toward narrator perspective. May need additional source material or author clarification before creating dependable shared reference prompts.

[[/SECTION]]

[[SECTION continuity_notes_markdown]]
# Continuity Notes

## Chapter Context
Character appears at plaza upon arrival, rushes to narrator with implied familiarity.

## Render Constraints
- No physical description in source text
- Requires manual visual input for image generation
- Consider approach direction from plaza toward narrator
- May need clarification on distinguishing features before reliable prompts

## Shared Reference Status
Pending manual description input. Current shared prompts use general descriptive language to accommodate uncertainty while maintaining continuity with chapter action (approaching companion figure).

[[/SECTION]]

[[SECTION repair_notes_markdown]]
# Repair Notes

## Identified Issues
- Source material lacks physical description for character Sola
- Cannot generate dependable images without additional appearance details
- Shared prompts currently use general descriptive language to accommodate uncertainty

## Recommended Actions
1. Request manual visual description from author or source team
2. Clarify species, age, gender, and distinguishing features before creating specific shared references
3. Consider adding placeholder notes in shared prompts indicating need for clarification
4. Document any additional source material that provides physical details

## Current Workaround
Using general descriptive language in positive/negative prompts to maintain continuity while acknowledging uncertainty about specific physical attributes.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
