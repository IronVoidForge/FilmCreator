# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:36:55.659029+00:00
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

Asset id: airship_crews

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/airship_crews.md

# Airship Crews

**Display Name:** Airship Crews  
**Chapter Role:** Distant figures on gray airships (20+ ships)

**Physical Presence:** Uncertain (listed as distant figures in visual continuity)

**Physical Description:** 
- Group of crew characters on airships
- Return fire with ineffectual results due to suddenness and damage
- Retreat after sustaining heavy casualties
- Limited specific physical details in source material

**Costume/Silhouette/Continuity Traits:**
- Crew attire (specifics not detailed)
- Positioned on airships at distance from Carter's vantage point
- Cultural differences noted in interaction with John Carter

**Useful Descriptive Noun Phrases:**
- "Airship crew figures"
- "Distant vessel operators"
- "Retreating enemy personnel"
- "Heavy casualty survivors"

**Uncertainty Notes:**
- Specific physical features not detailed in source material
- Exact costume details limited to general crew attire
- Individual character distinctions not specified

# Aliases

None



# Canonical Character ID

airship_crews



# Fully Identified

false

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/airship_crews_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: airship_crews

[[SECTION purpose]]
Reusable visual reference for distant vessel operators maintaining consistent silhouette and costume logic across multiple airship scenes. Focuses on stable body type, attire materials, and recurring operational gear rather than scene-specific positioning or individual facial features.
[[/SECTION]]

[[SECTION positive_prompt]]
distant vessel operators in crew attire with muted industrial fabrics, positioned at medium distance showing uniform silhouette against gray ship hulls, wearing functional utility belts and standard issue work gloves, maintaining consistent body proportions across multiple figures, operational equipment visible on shoulders and backs, atmospheric lighting matching overcast conditions, group composition of 3-5 figures per shot
[[/SECTION]]

[[SECTION negative_prompt]]
close-up facial details, individual character names, specific scene blocking instructions, proper nouns or location identifiers, detailed weapon specifications, unique costume variations, bright or contrasting lighting conditions, foreground positioning that breaks distance continuity, individual facial expressions, named equipment brands or models
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/airship_crews.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Source material lists physical presence as uncertain with limited specific physical details. Crew figures appear at distance from Carter's vantage point across 20+ ships. Costume specifics not detailed beyond general crew attire. Individual character distinctions not specified in source material. Visual continuity treats them as distant operational personnel rather than named characters.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Physical details remain uncertain per source documentation. No manual description input available for this asset. Continuity notes indicate limited specific physical details in source material requiring general descriptive approach. Individual facial features and costume specifics not detailed enough for granular prompt engineering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
