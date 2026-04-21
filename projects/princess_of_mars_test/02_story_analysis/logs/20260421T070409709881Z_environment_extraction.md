# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:04:09.709881+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH008

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location



[[SECTION markdown]]

# Arizona Quartz Vein Location

Short, grounded environment markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- emit one explicit environment record per meaningful location or setting family

- every environment record must have a FILMCREATOR_RECORD wrapper with type environment

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

**Setting:** A deserted Martian city and its surrounding valleys/hills.

**Events:**
- As the green Martian procession prepares to return home, they are suddenly forced into hiding by the arrival of twenty large, gray-painted aerial vessels.
- A fierce battle erupts between the green Martians (utilizing high-precision ground fire from buildings) and the approaching fleet. The green warriors demonstrate highly disciplined targeting of specific ship components (guns, officers, steering gear).
- The Martian fleet is routed, with most ships retreating. One unmanned, damaged vessel drifts erratically toward the city.
- Green Martian warriors intercept the drifting craft, haul it to the ground using grappling hooks, and systematically loot it for weapons, jewels, and food/water.
- After looting, the warriors set the ship on fire, turning it into a floating funeral pyre that drifts away into the distance.
- The protagonist feels an unexpected sense of melancholy and kinship toward the defeated crew, hoping for their return to seek vengeance.
- While waiting in the city for the danger to pass, the protagonist spots the prisoner taken from the downed craft: a beautiful, slender, copper-skinned female with black hair, resembling an Earth woman in form.
- The female prisoner makes a silent sign toward the protagonist, seeking help; however, due to his ignorance of Martian customs, he fails to respond, leaving her to be dragged away in dejection.

**Characters:**
- **The Protagonist (Earthman):** Observes the battle from a window; experiences complex emotions regarding the destruction of the aerial crew.
- **Sola:** Accompanies the protagonist during the conflict.
- **Green Martian Warriors:** Highly disciplined, tactical, and ruthless combatants.
- **The Prisoner:** A beautiful, slender female with copper skin and black hair, captured from the aerial vessel; she appears more human-like than the green Martians.
- **Woola:** The protagonist's loyal hound.

**Key Themes/Motifs:** Technological warfare, biological disparity between Martian species, misunderstood communication, and the "funeral pyre" of a lost civilization.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH008

| Asset ID | Description | Type |
| :--- | :--- | :--- |
| deserted_martian_city | A fortified urban setting used for ground-based combat and observation. | Primary |
| martian_valley_skyline | The open airspace and surrounding hills where the aerial battle occurs. | Secondary |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: deserted_martian_city

[[SECTION markdown]]

# Deserted Martian City

**Role:** Primary setting; tactical combat hub and observation point.

**Architecture & Geography:** 
A collection of stone or metallic buildings overlooking the valleys. Features high-precision firing positions, windows for long-range observation, and ground-level landing zones where captured vessels are hauled via grappling hooks.

**Lighting & Atmosphere:** 
Harsh, direct Martian light punctuated by the sudden, violent flashes of high-precision ground fire and explosions. The atmosphere is thick with the smoke of burning wreckage and the orange glow of a drifting funeral pyre.

**Scale & Anchors:** 
Large-scale urban structures providing verticality; heavy grappling lines anchored to buildings; wide streets or plazas used for looting captured craft.

**Prompt Phrases:** 
Deserted Martian architecture, fortified stone windows, tactical combat vantage points, smoke-filled city streets, glowing funeral pyre in distance, high-precision artillery positions.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_valley_skyline

[[SECTION markdown]]

# Martian Valley Skyline

**Role:** Secondary setting; transit and aerial combat zone.

**Architecture & Geography:** 
Expansive valleys and rolling hills surrounding the city. The sky is dominated by large, gray-painted aerial vessels and drifting, damaged crafts.

**Lighting & Atmosphere:** 
Open, vast skyways; atmospheric haze from battle debris; the visual of a single, unmanned vessel drifting erratically through the air.

**Scale & Anchors:** 
Massive scale defined by twenty large aerial ships; the contrast between the grounded city and the high-altitude fleet; the movement of drifting, burning wreckage across the horizon.

**Prompt Phrases:** 
Vast Martian valleys, gray-painted aerial vessels, drifting damaged spacecraft, skyward combat zone, sweeping hillsides, atmospheric battle haze, floating funeral pyre.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
