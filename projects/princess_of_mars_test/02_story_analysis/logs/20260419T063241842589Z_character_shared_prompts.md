# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T06:32:41.843586+00:00
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

## Display Name
Green Martian Warriors / Warrior Group

## Chapter Role
Procession participants returning to city after incubator ceremony; defenders firing volley from building windows against approaching airships; involved in ship salvage and burning operations.

## Physical Presence
**Present:** Yes - Physically present throughout chapter as group entity; no individual warriors specifically detailed beyond collective description.

## Physical Description (Supported by Source)
- **Group Identity:** Green Martian warriors referenced collectively
- **Individual Details:** Not provided in source material
- **Visual Continuity:** Procession returning to city, firing from windows, boarding drifting ship

## Costume & Silhouette
- **Silhouette:** Warrior group form (individual silhouettes not detailed)
- **Color Association:** Green (implied by "Green Martian" designation)
- **Equipment:** Chariots and mastodons mentioned as associated transport

## Continuity-Critical Traits
- Group entity without individualized physical descriptions
- Associated with chariots, mastodons, mounted warriors
- Involved in combat against airships and ship salvage operations
- Green color designation distinguishes from other entities

## Render-Facing Prompt Elements
"Green Martian warrior group; collective form without individualized physical details; associated with chariots and mastodons; green color designation"

## Uncertainty Notes
- **CRITICAL:** Individual physical descriptions not provided in source material
- No specific facial features, body types, or individual costume details available
- Manual description required for specific individuals to support dependable image generation
- Group references only; no individual warrior profiles established

# Aliases

None



# Canonical Character ID

green_martian_warriors



# Fully Identified

true

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
Reusable shared prompt for generating Green Martian warrior group visualizations; maintains collective form without individualized physical details; supports continuity across procession, combat, and salvage scenes; avoids proper nouns and uses descriptive noun phrases for stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking.
[[/SECTION]]

[[SECTION positive_prompt]]
Green Martian warrior group collective form without individualized physical details; green color designation on armor and clothing; mounted warriors on chariots and mastodons; combat-ready stance with weapons drawn; procession returning to city or firing from windows against airships; ship salvage operations with burning materials; armored silhouette with flowing green fabric; bronze metal accents on helmets and shields; group formation maintaining visual continuity across scenes.
[[/SECTION]]

[[SECTION negative_prompt]]
blurry individual facial features, specific body types not in source material, detailed costume elements beyond green designation, scene-specific blocking details, airship designs not associated with warrior group, mastodon or chariot variations beyond established transport, burning effects not part of salvage operations, floating or detached armor pieces, overly bright or dark color saturation outside green palette.
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martian_warriors.md; projects/princess_of_mars_test/01_source/character_descriptions/green_martian_warriors_manual_description.md (missing); green_martian_warriors canonical character ID.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Green color designation must remain consistent across all warrior group visualizations; collective form without individualized physical details per source material; associated with chariots and mastodons as established transport; combat against airships and ship salvage operations are key scene contexts; manual description input required for specific individuals to support dependable image generation since no individual profiles established in source.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Manual character description path missing at projects/princess_of_mars_test/01_source/character_descriptions/green_martian_warriors_manual_description.md; uncertainty noted that individual physical descriptions not provided in source material requiring manual intervention for specific individuals; group references only without individual warrior profiles established; render-facing prompt elements must avoid proper nouns and use descriptive noun phrases per task requirements.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
