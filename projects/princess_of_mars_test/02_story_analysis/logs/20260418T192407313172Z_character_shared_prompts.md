# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:24:07.313172+00:00
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

Asset id: sola

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/sola.md

# Sola (Chapter VIII)

## Display Name
Sola

## Chapter Role
Companion/Leader

## Presence Status
Referenced (Rushes up to Carter)

## Physical Description
*None provided in chapter summary.*

## Costume & Silhouette
*None provided in chapter summary.*

## Continuity-Critical Traits
*None provided in chapter summary.*

## Descriptive Noun Phrases
*Companion of Carter, city dweller.*

## Uncertainty Notes
No physical description available in chapter summary. Manual description required for image generation.

# Aliases

None



# Canonical Character ID

sola



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/sola_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: sola

[[SECTION purpose]]
Physical description missing from chapter summary (Chapter VIII). Manual character description input required for image generation. Companion role and city dweller status confirmed from continuity notes. Needs stable face, hair, body type, costume logic, silhouette, and recurring materials defined before scene-specific blocking.
[[/SECTION]]

[[SECTION positive_prompt]]
young adult female companion, urban city dweller attire, practical everyday clothing, neutral facial expression, approachable demeanor, modern casual style, grounded posture, accessible appearance, friendly presence, contemporary fashion, functional wardrobe, natural stance, open body language, relatable character design, everyday materials, simple silhouette, approachable face structure
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific names, scene blocking, dramatic lighting, fantasy elements, historical costume, elaborate accessories, theatrical makeup, stylized features, exaggerated proportions, cinematic composition, narrative-specific details, character-specific identifiers, branded items, celebrity likeness, unrealistic anatomy, overly detailed background, complex pose, dynamic action, emotional intensity, period-specific clothing
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/sola.md
projects/princess_of_mars_test/01_source/character_descriptions/sola_manual_description.md (missing)
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Chapter Role: Companion/Leader
Presence Status: Referenced (Rushes up to Carter)
Descriptive Noun Phrases: Companion of Carter, city dweller
Canonical Character ID: sola
Fully Identified: true
Manual Description Input Required: No (but physical details missing from chapter summary)
Continuity-Critical Traits: None provided in chapter summary
Physical Description: None provided in chapter summary
Costume & Silhouette: None provided in chapter summary
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Add manual character description to projects/princess_of_mars_test/01_source/character_descriptions/sola_manual_description.md with stable face, hair, body type, costume logic, silhouette, and recurring materials. Define companion role visual indicators (practical clothing, approachable posture). Specify city dweller aesthetic (modern casual style, urban materials). Avoid proper nouns in prompt bodies. Keep prompts concrete and visible.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
