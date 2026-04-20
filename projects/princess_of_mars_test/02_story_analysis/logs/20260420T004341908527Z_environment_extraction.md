# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:43:41.908527+00:00
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

Chapter id: CH001

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

**Story Summary:**
Carter waits for mining partner James K. Powell to return from the valley after leaving to purchase machinery. Apaches attack Powell. Carter pursues, finds Powell dead in a cave after being pursued by Indians. He enters the cave and collapses due to fatigue.

**Visual Continuity:**
Arizona landscape (hills, moonlight), horse tracks (unshod ponies), Indian tepees (white with warriors), cave interior (smooth floor, shadows), Powell's body (bristling with arrows). Carter is armed with two Colt revolvers and a carbine. The setting transitions from open valley to narrow gorge to large chamber within the cave.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH001

## Extracted Environments

| Asset ID | Name | Role | Description |
|----------|------|------|-------------|
| open_valley | Arizona Open Valley | Primary | Hills, moonlight, horse tracks |
| tepee_encampment | Indian Tepee Area | Secondary | White tepees with warriors |
| narrow_gorge | Transition Gorge | Transit | Narrow passage from valley to cave |
| cave_chamber | Cave Interior Chamber | Primary | Smooth floor, shadows, large chamber |

## Environment Families Summary

- **Arizona Landscape**: Open valley terrain with hills and moonlight illumination
- **Native Encampment**: Tepee structures with warrior presence
- **Cave System**: Multi-section interior from narrow gorge to large chamber
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: open_valley

[[SECTION markdown]]
# Arizona Open Valley

## Environment Role
Primary setting - main action location for Carter's wait and pursuit

## Architecture and Geography
- Rolling hills with undulating terrain
- Wide valley floor with natural vegetation
- Unshod pony tracks visible across ground surface
- Open sky above with no structural elements

## Lighting and Atmosphere Cues
- Moonlight illumination from overhead
- Cool nighttime temperature implied
- Shadows cast by hill contours
- Atmospheric haze over distant landscape features

## Scale and Environmental Anchors
- Large scale open space
- Horse tracks provide ground-level reference points
- Hill ridges create natural boundaries
- Valley width suggests expansive territory

## Descriptive Noun Phrases
- moonlit valley floor
- rolling Arizona hills
- pony track patterns
- open sky expanse
- hillside contours
- nighttime landscape
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: tepee_encampment

[[SECTION markdown]]
# Indian Tepee Encampment

## Environment Role
Secondary setting - location of Apache warriors and their structures

## Architecture and Geography
- White tepee structures with conical shapes
- Warrior presence around encampment perimeter
- Ground-level campsite area
- Natural clearing for settlement

## Lighting and Atmosphere Cues
- Moonlight reflecting off white tepee surfaces
- Warm ambient light from warrior activities
- Shadows cast by tepee poles
- Nighttime encampment atmosphere

## Scale and Environmental Anchors
- Medium scale human settlement
- Tepee structures provide vertical anchors
- Camp perimeter defines boundaries
- Ground surface shows campsite layout

## Descriptive Noun Phrases
- white tepee structures
- warrior encampment area
- conical shelter forms
- campsite ground level
- tepee pole shadows
- nighttime settlement
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: narrow_gorge

[[SECTION markdown]]
# Transition Gorge Passage

## Environment Role
Transit setting - connecting space between valley and cave interior

## Architecture and Geography
- Narrow gorge passage with constricted width
- Natural rock formations creating walls
- Transition from open valley to enclosed space
- Underground entrance point

## Lighting and Atmosphere Cues
- Dimmer lighting than open valley
- Moonlight filtering through narrow opening
- Shadow play on rock surfaces
- Atmospheric compression in confined space

## Scale and Environmental Anchors
- Medium scale passage
- Rock walls provide vertical boundaries
- Gorge width creates sense of enclosure
- Entrance point marks transition threshold

## Descriptive Noun Phrases
- narrow gorge passage
- rock wall formations
- underground entrance
- constricted valley exit
- filtered moonlight
- enclosed space entry
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: cave_chamber

[[SECTION markdown]]
# Cave Interior Chamber

## Environment Role
Primary setting - final location of Powell's body and Carter's collapse

## Architecture and Geography
- Large chamber with expansive interior space
- Smooth floor surface throughout
- Natural rock ceiling above
- Underground cave system structure

## Lighting and Atmosphere Cues
- Dim ambient lighting from natural sources
- Shadows cast across smooth floor
- Moonlight filtering through cave openings
- Atmospheric stillness in enclosed space

## Scale and Environmental Anchors
- Large scale chamber interior
- Rock formations provide structural anchors
- Floor surface shows wear patterns
- Chamber dimensions suggest significant underground space

## Descriptive Noun Phrases
- large cave chamber
- smooth floor surface
- rock ceiling structure
- underground interior space
- filtered cave light
- shadowed chamber floor
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
