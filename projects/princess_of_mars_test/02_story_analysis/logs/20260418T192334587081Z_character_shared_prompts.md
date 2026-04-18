# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:23:34.587081+00:00
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

Asset id: carter

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/carter.md

# Carter (Chapter VIII)

## Display Name
Carter

## Chapter Role
Leader/Warrior

## Presence Status
Referenced (Eyes meet him, emerges onto street)

## Physical Description
*None provided in chapter summary.*

## Costume & Silhouette
*None provided in chapter summary.*

## Continuity-Critical Traits
*None provided in chapter summary.*

## Descriptive Noun Phrases
*Leader of warriors, city dweller.*

## Uncertainty Notes
No physical description available in chapter summary. Manual description required for image generation.

# Aliases

None



# Canonical Character ID

carter



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/carter_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: carter

[[SECTION purpose]]
Create reusable character reference prompts for stable local generation. Asset ID carter requires manual physical description input due to missing chapter summary details. Prompts should establish consistent face, hair, body type, costume logic, silhouette, and recurring materials without scene-specific blocking. Purpose is to document uncertainty and guide future image generation with descriptive noun phrases avoiding proper nouns.
[[/SECTION]]

[[SECTION positive_prompt]]
leader of warriors, city dweller, confident posture, urban environment, detailed facial features, styled hair, fitted costume, strong silhouette, visible clothing textures, mature build, expressive eyes, practical footwear, structured shoulders, clean lines, neutral background, consistent character design
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, scene-specific blocking, temporary materials, inconsistent proportions, distorted face, messy hair, ill-fitting costume, weak silhouette, blurry details, inappropriate age markers, casual stance, cluttered environment, variable lighting, mismatched textures, undefined features, unstable character identity
[[/SECTION]]

[[SECTION inputs_markdown]]
Asset ID: carter
Display Name: Carter
Chapter Role: Leader/Warrior
Presence Status: Referenced (Eyes meet him, emerges onto street)
Physical Description: None provided in chapter summary
Costume & Silhouette: None provided in chapter summary
Continuity-Critical Traits: None provided in chapter summary
Descriptive Noun Phrases: Leader of warriors, city dweller
Uncertainty Notes: No physical description available in chapter summary. Manual description required for image generation.
Manual Description Path: projects/princess_of_mars_test/01_source/character_descriptions/carter_manual_description.md (missing)
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Character carter appears referenced in chapter VIII with eye contact and street emergence. No physical description exists in current chapter summary, requiring manual input for image generation. Costume and silhouette details are absent from source material. Continuity-critical traits not documented in chapter breakdown. Descriptive noun phrases available: leader of warriors, city dweller. Manual character description path is missing and needs creation before prompt finalization.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Manual character description file at projects/princess_of_mars_test/01_source/character_descriptions/carter_manual_description.md is missing and must be created with physical details for carter. Current prompts use placeholder descriptive phrases due to lack of source material. Future iterations should incorporate actual costume, silhouette, and facial feature specifications once manual description is completed. Prompts currently avoid proper nouns as required but need concrete visual descriptors from manual input.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
