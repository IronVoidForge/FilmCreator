# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T06:32:52.286318+00:00
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

Asset id: martian_females

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/martian_females.md

# Martian Females

## Display Name
Martian Females / Female Warrior Group

## Chapter Role
Draggers of captives into buildings; involved in ship salvage and burning operations; participants in procession returning to city.

## Physical Presence
**Present:** Yes - Physically present in Story Beat 3 dragging Earthling woman into building; also present during ship salvage operations.

## Physical Description (Supported by Source)
- **Group Identity:** Martian females referenced collectively
- **Individual Details:** Not provided in source material
- **Visual Continuity:** Dragging captives, boarding drifting ship, burning it as funeral pyre

## Costume & Silhouette
- **Silhouette:** Female warrior group form (individual silhouettes not detailed)
- **Color Association:** Green (implied by "Martian" designation)
- **Equipment:** Associated with chariots, mastodons, mounted warriors

## Continuity-Critical Traits
- Group entity without individualized physical descriptions
- Involved in captive handling operations
- Participate in ship salvage and burning procedures
- Green color designation distinguishes from other entities

## Render-Facing Prompt Elements
"Martian female group; collective form without individualized physical details; green color designation; involved in captive handling and ship salvage operations"

## Uncertainty Notes
- **CRITICAL:** Individual physical descriptions not provided in source material
- No specific facial features, body types, or individual costume details available
- Manual description required for specific individuals to support dependable image generation
- Group references only; no individual female warrior profiles established

# Aliases

None



# Canonical Character ID

martian_females



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/martian_females_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: martian_females

[[SECTION purpose]]
Reusable shared character-reference prompt for stable local generation of Martian female group entities; focuses on continuity-critical visual traits including green color designation and warrior silhouette form without inventing individual physical details not present in source material; supports consistent rendering across multiple scenes involving captive handling, ship salvage, and burning operations.
[[/SECTION]]

[[SECTION positive_prompt]]
green colored female warrior group; collective form without individualized physical features; flowing robes with green accents; mounted on chariot-like vehicles; involved in dragging captives; participating in ship salvage operations; burning funeral pyre activities; procession returning to city; multiple figures in unified visual style.
[[/SECTION]]

[[SECTION negative_prompt]]
individual facial features, specific body types, detailed costume elements, scene-specific blocking, Earthling characteristics, proper nouns, brand names, logos, text overlays, single figure composition, isolated character portraits, modern clothing, technology, weapons not associated with chariots or mastodons.
[[/SECTION]]

[[SECTION inputs_markdown]]
Source material path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/martian_females.md; Display Name: Martian Females / Female Warrior Group; Chapter Role: Draggers of captives into buildings; involved in ship salvage and burning operations; participants in procession returning to city; Physical Presence: Yes - Physically present in Story Beat 3 dragging Earthling woman into building; also present during ship salvage operations; Color Association: Green (implied by Martian designation); Equipment: Associated with chariots, mastodons, mounted warriors; Continuity-Critical Traits: Group entity without individualized physical descriptions; Involved in captive handling operations; Participate in ship salvage and burning procedures; Green color designation distinguishes from other entities.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Green color designation is primary visual identifier for this group entity; collective form means prompts should reference multiple figures rather than single character compositions; warrior silhouette form without detailed individual physical descriptions requires focus on unified visual style across all figures; scenes involving captive handling, ship salvage, and burning operations are key contexts where these characters appear; avoid proper nouns and use descriptive noun phrases to maintain prompt stability; manual description input not available in source material so prompts must work with group-level visual traits only.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
If generated images show individualized facial features or body types, remove those elements and return to collective form representation; if proper nouns appear in output, replace with descriptive noun phrases focusing on green color and warrior silhouette; ensure multiple figures are shown rather than single character portraits; verify chariot-like vehicles and mastodon associations are present when relevant to scene context; maintain consistent visual style across all figures in the group.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
