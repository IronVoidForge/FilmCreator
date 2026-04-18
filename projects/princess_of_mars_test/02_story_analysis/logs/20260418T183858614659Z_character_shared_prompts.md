# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:38:58.614659+00:00
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

Asset id: green_martian_warriors

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martian_warriors.md

# Green Martian Warriors

**Display Name:** Green Martian Warriors  
**Chapter Role:** Enemy combatants firing volley from buildings

**Physical Presence:** Referenced (listed as visible characters in visual continuity)

**Physical Description:** 
- Group of warrior characters
- Fire volley from buildings during battle
- Board drifting airship and loot arms, jewels, water
- Limited specific physical details in source material

**Costume/Silhouette/Continuity Traits:**
- Warrior attire (specifics not detailed)
- Positioned at rooftops and building interiors
- Cultural differences noted in interaction with John Carter

**Useful Descriptive Noun Phrases:**
- "Martian warrior group"
- "Enemy combatant figures"
- "Building-based attackers"
- "Looters of drifting vessel"

**Uncertainty Notes:**
- Specific physical features not detailed in source material
- Exact costume details limited to general warrior attire
- Individual character distinctions not specified

# Aliases

None



# Canonical Character ID

green_martian_warriors



# Fully Identified

false

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/green_martian_warriors_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: green_martian_warriors
[[SECTION purpose]]
Define visual consistency for enemy combatants referenced in the story analysis breakdown. Focus on group composition, positioning on high ground (rooftops/buildings), and interaction with drifting vessels. Maintain stable attire logic and silhouette across shots to ensure continuity without relying on specific physical features that are limited in source material. Use stable asset ids for reference files.
[[/SECTION]]
[[SECTION positive_prompt]]
Group of armored figures, enemy combatants, positioned on high ground, building interiors, looting vessels, metallic and fabric textures, warrior attire, dark tones, volley firing stance, atmospheric lighting, dynamic battle composition, structural backgrounds, alien silhouette, tactical gear, debris and dust particles.
[[/SECTION]]
[[SECTION negative_prompt]]
Human faces, civilian clothing, peaceful scenes, bright daylight only, specific named characters, clean backgrounds, static poses, modern technology, civilian architecture, detailed facial features, bright colors, soft focus, indoor domestic settings, non-combatant expressions.
[[/SECTION]]
[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martian_warriors.md
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Source material indicates limited specific physical details for individual characters within the group. Visual continuity should prioritize role (enemy, building-based) and general attire over distinct facial features or specific coloration not explicitly detailed in the breakdown. Interaction with other factions (e.g., John Carter) notes cultural differences but does not specify exact costume variations.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
If physical details remain ambiguous during generation, rely on visual continuity files to maintain consistent silhouette and attire style. Avoid inventing specific facial features or color palettes that contradict the general "warrior" archetype established in the breakdown. Use atmospheric elements (dust, debris) to bridge gaps between shots where character specifics are limited.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
