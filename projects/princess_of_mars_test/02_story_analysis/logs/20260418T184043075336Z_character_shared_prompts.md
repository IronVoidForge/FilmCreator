# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:40:43.075336+00:00
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

# Sola

**Display Name:** Sola  
**Chapter Role:** Human woman prisoner being dragged into building

**Physical Presence:** Referenced (seen by John Carter from window)

**Physical Description:** 
- Female human character
- Being dragged into building by warriors
- Shows emotional response: hope then dejection when failing to signal help
- Limited specific physical details in source material

**Costume/Silhouette/Continuity Traits:**
- Prisoner attire (specifics not detailed)
- Positioned at street/plaza level
- Cultural differences noted in interaction with John Carter

**Useful Descriptive Noun Phrases:**
- "Female prisoner figure"
- "Hopeful captive character"
- "Human woman in distress"
- "Victim of cultural misunderstanding"

**Uncertainty Notes:**
- Specific physical features not detailed in source material
- Exact costume details limited to general prisoner attire
- Facial expression details (hope, dejection) noted but not fully described

# Aliases

None



# Canonical Character ID

sola



# Fully Identified

false

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
Define a reusable prompt for generating Sola's character reference shots. Focus on stable traits like prisoner status, emotional expression (hope to dejection), and general attire without scene-specific blocking or proper nouns. Ensure continuity with cultural context notes.
[[/SECTION]]
[[SECTION positive_prompt]]
Female prisoner figure, hopeful captive character, human woman in distress, simple tattered attire, emotional expression of hope turning to dejection, street level positioning, cultural context differences, limited specific physical details beyond general human form
[[/SECTION]]
[[SECTION negative_prompt]]
proper nouns, specific names, detailed physical features not specified, scene blocking, action sequences, warrior figures, indoor settings unless specified, overly detailed facial features beyond general human
[[/SECTION]]
[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/sola.md
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Sola is a human woman prisoner being dragged into a building. Emotional state shifts from hope to dejection when signaling help fails. Positioned at street/plaza level. Cultural differences noted in interaction with John Carter. Specific physical features not detailed in source material. Costume limited to general prisoner attire. Victim of cultural misunderstanding.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
Manual description path missing (projects/princess_of_mars_test/01_source/character_descriptions/sola_manual_description.md). Specific physical features uncertain due to source limitations. Focus on emotional continuity and status rather than detailed anatomy.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
