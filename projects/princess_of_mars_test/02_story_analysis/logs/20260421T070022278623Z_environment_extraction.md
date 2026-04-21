# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:00:22.278623+00:00
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

Chapter id: CH005

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

**Setting:** A captive's chamber decorated with masterfully painted murals of Martian landscapes; a deserted street in a Martian city; the exterior of a building overlooking a valley.

**Characters:**
- **The Protagonist:** An adventurous human captive attempting to test his physical limits and escape his guards.
- **Sola:** A female Martian who shows uncharacteristic sympathy, kindness, and care for the protagonist, providing him with food and warmth.
- **The Watch Dog:** A ferocious, short-legged but incredibly fast Martian beast used for protection and hunting; it serves as the protagonist's constant guardian.
- **The Colossal Creature:** A large, white, hairless, ape-like being that captures the protagonist during his escape attempt.

**Key Events:**
- **Observation of Captivity:** The protagonist observes his guard dog and examines the room's murals, noting the absence of living creatures in the art.
- **Martian Biology & Environment:** Through Sola’s care, the protagonist learns about Martian food (milk from a large plant), the extreme cold of the nights, and the mechanics of the two Martian moons which provide nocturnal light.
- **The Escape Attempt:** Seeking to test the watch dog's limits, the protagonist leaves his room. He discovers that despite its short legs, the beast is incredibly fast and intelligent.
- **The Chase:** The protagonist engages in a high-stakes chase through the city, using his jumping ability to evade the beast.
- **Capture:** After leaping into a window thirty feet above the ground to escape the dog, the protagonist is grabbed from behind by a massive, ape-like creature and dragged into a room.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH005

| Asset ID | Description | Role |
| :--- | :--- | :--- |
| captive_chamber_murals | A room decorated with landscape murals lacking living creatures. | Primary |
| martian_city_streets | Deserted urban streets used for high-stakes chases. | Secondary |
| valley_overlook_exterior | High-altitude building exterior overlooking a vast valley. | Transit |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: captive_chamber_murals

[[SECTION markdown]]

# Captive Chamber Murals

**Role:** Primary setting for character observation and exposition.

**Architecture & Geography:** An enclosed interior chamber featuring walls adorned with masterfully painted murals depicting Martian landscapes. The art is notable for its lack of living fauna, focusing purely on terrain.

**Lighting & Atmosphere:** Controlled indoor lighting; atmosphere is one of isolation and quiet observation.

**Scale & Anchors:** Enclosed room scale; the muraled walls serve as the primary visual anchor.

**Prompt Phrases:** masterfully painted Martian murals, landscape paintings, desolate scenery, interior captive cell, absence of life in art.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_city_streets

[[SECTION markdown]]

# Martian City Streets

**Role:** Secondary setting for action and chase sequences.

**Architecture & Geography:** Deserted urban streets within a Martian settlement; characterized by verticality and jumping-friendly architecture.

**Lighting & Atmosphere:** Nocturnal lighting provided by the dual Martian moons; extreme cold atmosphere; sense of emptiness and desolation.

**Scale & Anchors:** Urban scale; narrow street corridors, building facades, and windows positioned at significant heights (30ft+).

**Prompt Phrases:** deserted Martian city streets, nocturnal moonlight, dual moonlit sky, urban chase setting, high-altitude windows, cold Martian night.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: valley_overlook_exterior

[[SECTION markdown]]

# Valley Overlook Exterior

**Role:** Transit setting for escape and capture.

**Architecture & Geography:** The exterior of a high-rise building overlooking a vast, sweeping Martian valley.

**Lighting & Atmosphere:** Open sky; moonlight exposure; sense of immense scale and exposure to the elements.

**Scale & Anchors:** Massive scale; high-altitude ledge/window, expansive valley view below.

**Prompt Phrases:** high-altitude building exterior, overlooking vast Martian valley, moonlit precipice, extreme height, sweeping landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
