# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:13:34.041580+00:00
- task: environment_extraction

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

Chapter id: CH005

Task: extract environment families into an environment index plus one Markdown file per environment family.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
...environment_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment
asset_id: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

**Visual Context:** The room is furnished with silks and furs for warmth. Murals depict mountains, rivers, lakes, and gardens with rare beauty but no animal forms. Food consists of a tasteless cheese-like substance; drink is milk from a large plant (8-10 quarts/day). Martian nights are cold with sudden temperature changes due to two moons (one ~5,000 miles away, one ~14,000 miles away) and thin atmosphere.
**Story Events:** Sola leaves the chamber while the Watch Dog guards alone. The narrator examines the room's murals. Upon Sola's return, she provides food and drink. After sleeping through the cold night, the narrator decides to test the Watch Dog's loyalty by attempting an escape. The narrator successfully jumps over the dog and reaches a window sill thirty feet up. However, upon being dragged back into the room by a hand, the narrator finds themselves facing a colossal, white, ape-like creature standing over them.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH005

## Primary Environments

| Asset ID | Name | Role | Description |
|----------|------|------|-------------|
| chamber_001 | The Chamber | Primary Setting | Main room with silks, furs, murals, food/drink area |
| window_area_001 | Window Area | Transit Setting | Elevated window sill 30 feet up where narrator jumps |
| watch_dog_position_001 | Watch Dog Position | Secondary Setting | Location within chamber where dog stands |

## Environmental Families

- **The Chamber** - Primary setting with furniture, murals, and sustenance area
- **Window Area** - Transit location at elevated window sill
- **Watch Dog Position** - Secondary location within the main chamber

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chamber_001

[[SECTION markdown]]
# The Chamber

## Environment Role
Primary Setting

## Architecture and Geography
Interior room space furnished with silks and furs for warmth. Features murals depicting mountains, rivers, lakes, and gardens with rare beauty but no animal forms. Contains food/drink area with tasteless cheese-like substance and milk from large plant (8-10 quarts/day).

## Lighting and Atmosphere Cues
Cold Martian nights with sudden temperature changes due to two moons (one ~5,000 miles away, one ~14,000 miles away) and thin atmosphere. Murals provide visual warmth despite cold ambient conditions.

## Scale Cues and Recurring Environmental Anchors
Room accommodates Watch Dog standing over narrator. Window sill positioned 30 feet above ground level. Furniture scale suggests human-sized space with elevated viewing points.

## Descriptive Noun Phrases for Render-Facing Prompts
- "Silks and furs arranged for warmth"
- "Murals depicting mountains rivers lakes gardens rare beauty no animal forms"
- "Tasteless cheese-like substance food area"
- "Milk from large plant 8-10 quarts daily"
- "Cold Martian nights sudden temperature changes two moons thin atmosphere"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: window_area_001

[[SECTION markdown]]
# Window Area

## Environment Role
Transit Setting

## Architecture and Geography
Elevated window sill positioned 30 feet above ground level. Accessible via jump from chamber floor. Features hand-drag mechanism for returning intruder to room interior.

## Lighting and Atmosphere Cues
Cold Martian night conditions extend to window area. Two moons create atmospheric temperature fluctuations visible from elevated position. Thin atmosphere affects visibility and thermal comfort at height.

## Scale Cues and Recurring Environmental Anchors
30 feet vertical elevation from chamber floor. Window sill serves as landing point for escape attempt. Hand mechanism positioned near window frame for dragging action.

## Descriptive Noun Phrases for Render-Facing Prompts
- "Elevated window sill 30 feet above ground"
- "Escape jump landing point"
- "Hand-drag mechanism near window frame"
- "Cold Martian night conditions at height"
- "Two moons atmospheric temperature fluctuations visible from elevated position"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: watch_dog_position_001

[[SECTION markdown]]
# Watch Dog Position

## Environment Role
Secondary Setting

## Architecture and Geography
Location within chamber where Watch Dog stands. Positioned to guard narrator alone when Sola leaves room. Features space for colossal white ape-like creature standing over intruder.

## Lighting and Atmosphere Cues
Cold Martian night conditions extend to dog's position. Murals provide visual backdrop despite cold ambient temperature. Thin atmosphere creates thermal challenges at this location within chamber.

## Scale Cues and Recurring Environmental Anchors
Colossal white ape-like creature stands over narrator in this position. Space accommodates both human-sized intruder and larger guardian figure. Chamber floor provides stable ground for dog's stance.

## Descriptive Noun Phrases for Render-Facing Prompts
- "Location within chamber where Watch Dog stands"
- "Space for colossal white ape-like creature standing over intruder"
- "Guard position when Sola leaves room"
- "Chamber floor stable ground for dog's stance"
- "Cold Martian night conditions at guardian position"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
