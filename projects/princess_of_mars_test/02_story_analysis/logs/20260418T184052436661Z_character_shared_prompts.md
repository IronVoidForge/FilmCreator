# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:40:52.436661+00:00
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

Asset id: woola

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/woola.md

# Woola

**Display Name:** Woola  
**Chapter Role:** Companion character (listed in visual continuity)

**Physical Presence:** Referenced (listed as visible character in visual continuity)

**Physical Description:** 
- Character companion to John Carter
- Listed in visual continuity but no specific physical details provided
- Limited description in source material

**Costume/Silhouette/Continuity Traits:**
- Companion role suggests close association with protagonist
- Specific costume and silhouette not detailed in source

**Useful Descriptive Noun Phrases:**
- "Companion character figure"
- "Loyal associate"
- "Character with unknown physical features"

**Uncertainty Notes:**
- Physical species/build not specified in source material
- No distinctive markings or features described
- Costume details limited to general companion attire

# Aliases

None



# Canonical Character ID

woola



# Fully Identified

false

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/woola_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: woola

[[SECTION purpose]]
Reusable shared character-reference prompt draft for stable local generation of Woola companion figure. Focuses on silhouette, costume logic, and recurring materials while preserving uncertainty about physical species and distinctive features due to limited source material. Designed for consistency across shots where this companion appears in visual continuity with protagonist John Carter.

[[/SECTION]]

[[SECTION positive_prompt]]
Companion character figure standing beside protagonist, loyal associate posture, simple companion attire, neutral facial expression, generic humanoid silhouette, soft fabric materials, muted color palette, clean lines, approachable build type, understated costume design, minimal distinctive markings, functional clothing layers, practical footwear, unadorned accessories

[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific species identifiers, detailed facial features, ornate costume elements, bright saturated colors, complex patterns, distinctive markings, fantasy creature traits, elaborate jewelry, intricate armor pieces, scene-specific blocking details, location markers, character name references, John Carter visual overlap, protagonist face duplication, excessive detail beyond silhouette

[[/SECTION]]

[[SECTION inputs_markdown]]
Asset ID: woola
Project: princess_of_mars_test
Chapter Role: Companion character (listed in visual continuity)
Physical Presence: Referenced as visible character in visual continuity
Canonical Character ID: woola
Fully Identified: false
Manual Description Input Required: No

[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Uncertainty preserved per source material limitations. Physical species/build not specified in source material. No distinctive markings or features described. Costume details limited to general companion attire. Companion role suggests close association with protagonist but specific costume and silhouette not detailed in source. Character listed in visual continuity but no specific physical details provided. Limited description in source material.

[[/SECTION]]

[[SECTION repair_notes_markdown]]
No manual character description file available at projects/princess_of_mars_test/01_source/character_descriptions/woola_manual_description.md. Physical features remain undefined per source constraints. Prompts intentionally avoid proper nouns and use descriptive noun phrases only. Continuity notes explicitly flag missing information rather than inventing details.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
