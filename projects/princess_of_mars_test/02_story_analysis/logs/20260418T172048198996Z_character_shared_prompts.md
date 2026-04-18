# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:20:48.198996+00:00
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

Asset id: narrator_ch001

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/narrator_ch001.md

# Narrator (CH001)

## Display Name
Narrator

## Chapter Role
Observer / Witness

## Physical Presence
Uncertain (observes from distance, descends to street)

## Physical Description
Not described in source material. No physical attributes provided for reliable image generation.

## Costume & Silhouette
Unknown. No costume details available in chapter text.

## Continuity-Critical Traits
- Observes events from elevated position initially
- Descends to street level by end of chapter
- Witness to naval engagement and captive discovery

## Render-Facing Prompt Notes
- Requires manual description for image generation
- Focus on observational perspective rather than physical presence
- Consider positioning relative to airships, plaza, and building interiors

## Uncertainty Notes
**CRITICAL:** No physical description provided in source material. Cannot generate dependable images without additional details about appearance, age, gender, or distinguishing features.

# Aliases

-



# Canonical Character ID

narrator



# Fully Identified

true

# Manual Description Input Required

Yes



# Manual Description Reason

No physical description provided in source material; cannot support dependable image generation without additional details




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/narrator_ch001_manual_description.md

<!-- FILMCREATOR_MANUAL_PLACEHOLDER -->

# Asset ID
narrator_ch001

# Purpose
Paste a stable manual visual description for this character so later shared reference generation can use it.

# Why This Is Needed
No physical description provided in source material; cannot support dependable image generation without additional details

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
asset_id: narrator_ch001

[[SECTION purpose]]
Manual visual description placeholder for shared reference generation. Requires stable descriptive input for face, hair, body type, age impression, silhouette, skin tone, costume logic, and continuity-critical marks to support dependable image generation.

[[/SECTION]]

[[SECTION positive_prompt]]
human figure with neutral expression, medium length hair, average build, youthful appearance, light skin tone, simple clothing, standing posture, clear outline, visible facial features, natural lighting, detailed texture on fabric, calm demeanor, observational stance

[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, brand names, specific character identifiers, exaggerated features, distorted anatomy, blurry details, dark shadows, complex background elements, multiple figures, dynamic action poses, heavy makeup, ornate costumes, unrealistic proportions, cartoon style, low resolution, missing facial features, obscured identity markers

[[/SECTION]]

[[SECTION inputs_markdown]]
Asset ID: narrator_ch001
Display Name: Narrator
Chapter Role: Observer / Witness
Physical Presence: Uncertain (observes from distance, descends to street)
Continuity-Critical Traits: Observes events from elevated position initially, Descends to street level by end of chapter, Witness to naval engagement and captive discovery
Render-Facing Notes: Requires manual description for image generation, Focus on observational perspective rather than physical presence, Consider positioning relative to airships, plaza, and building interiors

[[/SECTION]]

[[SECTION continuity_notes_markdown]]
CRITICAL: No physical description provided in source material. Cannot generate dependable images without additional details about appearance, age, gender, or distinguishing features. Manual character description input required before shared reference generation can proceed reliably. Current prompts use generic descriptive terms that may need refinement once specific visual attributes are established.

[[/SECTION]]

[[SECTION repair_notes_markdown]]
Pending manual description input at: projects/princess_of_mars_test/01_source/character_descriptions/narrator_ch001_manual_description.md. Once physical attributes are documented, shared reference prompts should be updated with specific face, hair, body type, age impression, silhouette, skin tone, costume logic, and continuity-critical marks for more accurate image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
