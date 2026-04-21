# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:24:13.466479+00:00
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

Chapter id: CH023

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

**Events:**
John Carter infiltrates the guarded quarters of Kantos Kan to inform him of Dejah Thoris's engagement to Sab Than. Upon hearing the news, a distraught Kantos Kan vows to assassinate Sab Than using a secret palace entrance. The two men devise a plan: Kantos Kan will infiltrate the palace to kill the usurper, while Carter will attempt to fly to Helium. 

Carter performs a perilous climb up the Zodanga barracks, using a grappling hook to reach the roof and neutralizing a sentry to secure two air machines. As Carter and Kantos Kan depart, they are intercepted by a Zodangan air patrol. After a high-speed chase through the Martian sky, Carter uses a Heliumite speed-gearing trick to outrun his pursuers, but his machine is struck by a projectile from a cruiser. The resulting crash leaves him flying blind without a compass or speedometer. After six hours of flight over a dead sea bottom, Carter realizes he is lost; despite seeing several large cities, none match the distinct twin-city architecture and scarlet/yellow towers of Helium.

**Characters:**
* **John Carter:** A resourceful adventurer and airman who executes a dangerous climb and high-speed aerial escape.
* **Kantos Kan:** A Heliumite air-scout who vows to kill Sab Than to avenge Dejah Thoris's honor.
* **Sab Than (Mentioned):** The ruler of Zodanga to whom Dejah Thoris is promised.
* **Dejah Thoris (Mentioned):** The Princess of Helium.
* **Zodangan Sentry:** A guard at the barracks neutralized by Carter.

**Settings:**
* **Zodanga:** A heavily guarded city characterized by high-rise buildings and active air patrols.
* **The Barracks:** An enormous, thousand-foot tall building in Zodanga.
* **The Martian Sky:** The setting for a high-speed pursuit involving air-scout craft and cruisers.
* **Dead Sea Bottom:** A vast, desolate expanse Carter flies over while lost.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [zodanga_urban_complex](zodanga_urban_complex)
- [martian_sky_aerial_corridors](martian_sky_aerial_corridors)
- [dead_sea_bottom_expanse](dead_sea_bottom_expanse)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_urban_complex

[[SECTION markdown]]

# Zodanga Urban Complex

**Role:** Primary / Transit Setting

**Architecture & Geography:** A heavily fortified, high-density metropolitan landscape. Features massive, thousand-foot tall barracks and high-rise structures designed for verticality. The architecture is dense and guarded, characterized by defensive perimeters and sentry posts.

**Lighting & Atmosphere:** Heavily patrolled and militarized atmosphere; constant presence of aerial movement and security lights.

**Scale & Anchors:** Enormous scale defined by the thousand-foot barracks; recurring anchors include high-altitude rooftops and fortified guard quarters.

**Prompt Phrases:** massive Zodangan barracks, thousand-foot vertical architecture, heavily guarded urban heights, high-rise military structures, dense Martian cityscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_sky_aerial_corridors

[[SECTION markdown]]

# Martian Sky Aerial Corridors

**Role:** Transit Setting

**Architecture & Geography:** Open, vast atmospheric space characterized by high-speed flight paths and aerial patrol routes.

**Lighting & Atmosphere:** High-altitude clarity; dynamic lighting shifts during high-speed chases; presence of projectile streaks and engine exhaust.

**Scale & Anchors:** Vast, boundless scale; recurring anchors include air-scout craft, cruisers, and distant city silhouettes.

**Prompt Phrases:** vast Martian atmosphere, aerial pursuit corridors, high-altitude skyways, drifting air machines, distant planetary horizons.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dead_sea_bottom_expanse

[[SECTION markdown]]

# Dead Sea Bottom Expanse

**Role:** Secondary / Transit Setting

**Architecture & Geography:** A vast, desolate, and dried-out seabed. A flat, featureless expanse stretching toward the horizon.

**Lighting & Atmosphere:** Desolate, lonely, and exposed; harsh lighting over a barren landscape.

**Scale & Anchors:** Immense, overwhelming scale; recurring anchors include distant, unidentified city clusters on the horizon.

**Prompt Phrases:** desolate dead sea bottom, vast dried Martian seabed, barren planetary expanse, lonely desert floor, distant horizon cities.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
