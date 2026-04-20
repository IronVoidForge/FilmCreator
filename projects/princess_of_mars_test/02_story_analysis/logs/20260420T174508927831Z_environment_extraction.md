# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:45:08.927831+00:00
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

**Setting:** A captive's chamber decorated with beautiful murals of Martian landscapes; a deserted Martian city street; and an overlooking building.

**Characters:**
- **The Protagonist:** A human male, adventurous and physically agile (a "jumper"), currently held captive.
- **Sola:** A kind and sympathetic female Martian who provides the protagonist with food, drink, and warmth.
- **The Watch Dog:** A ferocious, short-legged but incredibly fast Martian beast used for guarding and hunting.
- **The Colossal Creature:** A large, white, hairless, ape-like being encountered at the end of the chapter.

**Events:**
- Sola leaves the protagonist under the guard of a ferocious Martian watchdog that blocks the room's exit.
- The protagonist observes the room's murals and learns about Martian biology, specifically a milk-producing plant and the extreme temperature fluctuations caused by the thin atmosphere and dual moons.
- Sola returns to feed him (cheese-like substance and plant-milk) and provides furs for warmth during the cold Martian night.
- The protagonist decides to test the watchdog's temperament by attempting to leave the room.
- The watchdog follows him at a distance until they reach the edge of the city, where it suddenly turns aggressive and charges.
- The protagonist uses his jumping ability to evade the beast, eventually leaping into a window thirty feet above the ground to escape.
- Upon entering the building through the window, the protagonist is violently grabbed by the neck and thrown to the floor by a massive, white, ape-like creature.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

| Asset ID | Description | Role |
| :--- | :--- | :--- |
| captive_chamber_murals | A decorated room featuring Martian landscape murals. | Primary |
| deserted_martian_cityscape | An empty, urban street at the edge of a city. | Transit |
| overlooking_building_interior | A high-altitude building interior with large windows. | Secondary |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: captive_chamber_murals

[[SECTION markdown]]

# Captive Chamber Murals

**Role:** Primary setting for character interaction and exposition.

**Architecture/Geography:** An enclosed chamber decorated with detailed, large-scale murals depicting Martian landscapes, flora (milk-producing plants), and celestial bodies (dual moons).

**Lighting/Atmosphere:** Dimly lit interior; atmosphere shifts from warmth provided by furs to the implied extreme cold of the Martian night.

**Scale/Anchors:** Murals serve as the primary visual anchor; scale is intimate and enclosed.

**Prompt Phrases:** decorated captive chamber, large-scale Martian landscape murals, milk-producing plant illustrations, dual moon celestial art, dim interior lighting, cozy furs against cold stone.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: deserted_martian_cityscape

[[SECTION markdown]]

# Deserted Martian Cityscape

**Role:** Transit setting for action and evasion.

**Architecture/Geography:** An empty, urban street transitioning into the outskirts of a city; wide streets leading toward open Martian terrain.

**Lighting/Atmosphere:** Harsh lighting dictated by thin atmosphere; extreme temperature fluctuations; desolate and quiet.

**Scale/Anchors:** Wide urban corridors; transition from built structures to the edge of the city.

**Prompt Phrases:** deserted Martian street, empty urban canyon, thin atmosphere lighting, desolate cityscape, outskirts of a Martian colony, high-contrast shadows.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: overlooking_building_interior

[[SECTION markdown]]

# Overlooking Building Interior

**Role:** Secondary setting for climax and confrontation.

**Architecture/Geography:** A high-altitude building featuring large windows positioned thirty feet above the ground level.

**Lighting/Atmosphere:** High-altitude light; interior space vulnerable to external elements through large openings.

**Scale/Anchors:** Large window frames; verticality emphasized by the height from the street below.

**Prompt Phrases:** high-altitude building interior, large elevated windows, urban overlook, interior room with high ceilings, sudden confrontation space.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
