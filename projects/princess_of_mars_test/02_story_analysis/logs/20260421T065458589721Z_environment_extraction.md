# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:54:58.589721+00:00
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

**Setting:** A captive's chamber decorated with beautiful murals of Martian landscapes; later, the deserted streets and outskirts of a Martian city.

**Characters:**
- **The Protagonist:** A human male, an adventurer and skilled jumper, currently held captive.
- **Sola:** A female Martian who shows kindness and sympathy toward the protagonist, providing him with food (cheese-like substance) and milk from a large plant, and tending to him during the cold Martian nights.
- **The Watch Dog:** A ferocious, short-legged but incredibly fast Martian beast used for protection and hunting; it guards the protagonist's door.
- **The Colossal Ape-like Creature:** A large, white, hairless creature with a shock of bristly hair that captures the protagonist after his attempted escape.

**Events:**
- Sola leaves the protagonist under the guard of a ferocious Martian watchdog.
- The protagonist observes the room's murals and learns about the Martian environment, including the extreme cold at night and the influence of Mars' two moons.
- Sola returns to feed the protagonist and provides furs to protect him from the sudden temperature drops during the night.
- Seeking to test the limits of his guard, the protagonist attempts to escape the room. The watchdog follows him cautiously until they reach the edge of the city.
- The watchdog suddenly turns aggressive, charging at the protagonist with incredible speed.
- The protagonist uses his jumping ability to evade the beast, eventually leaping toward a window thirty feet above the ground.
- After successfully pulling himself onto a windowsill, the protagonist is grabbed from behind by a massive, white, ape-like creature and dragged into a building.
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
| captive_chamber_murals | A decorated room featuring Martian landscape art. | Primary |
| martian_city_outskirts | Deserted streets and urban edges of a Martian settlement. | Secondary/Transit |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: captive_chamber_murals

[[SECTION markdown]]

# Captive Chamber Murals

**Role:** Primary setting for character interaction and exposition.

**Architecture & Geography:** An enclosed, interior chamber featuring walls adorned with detailed, beautiful murals depicting various Martian landscapes. The room contains basic amenities provided by a caretaker (food, milk-producing plants, furs).

**Lighting & Atmosphere:** Transitions from stable indoor lighting to extreme temperature shifts; atmosphere is characterized by sudden, biting cold during the Martian night.

**Scale & Anchors:** Enclosed space; large-scale mural depictions of distant geography serve as visual anchors.

**Prompt Phrases:** decorated captive chamber, Martian landscape murals, interior cell, extreme nocturnal cold, heavy furs, bioluminescent plant milk, detailed wall paintings.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_city_outskirts

[[SECTION markdown]]

# Martian City Outskirts

**Role:** Secondary setting for action and transit.

**Architecture & Geography:** Deserted urban streets transitioning into the outskirts of a Martian city; includes high-altitude windows (approx. 30 feet up) and building facades.

**Lighting & Atmosphere:** Open sky exposure; influenced by the presence of two moons; sense of desolation and emptiness.

**Scale & Anchors:** Wide, deserted streetscapes; verticality provided by tall buildings and high windows; vast Martian horizon.

**Prompt Phrases:** deserted Martian streets, urban outskirts, moonlit Martian cityscape, high windows, desolate architecture, wide dusty thoroughfares, two moons overhead.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
