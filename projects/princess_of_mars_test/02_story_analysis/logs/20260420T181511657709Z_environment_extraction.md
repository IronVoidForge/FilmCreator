# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:15:11.657709+00:00
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

**Setting:**
The city of Zodanga (specifically the barracks, the streets, and the sky above) and the vast expanse of a dead sea bottom during flight.

**Characters:**
* **John Carter:** An air-scout/warrior attempting to reach Helium while evading Zodangan authorities.
* **Kantos Kan:** A Heliumite air-scout who pledges his sword to assist John Carter and Sab Than.
* **Sab Than:** The ruler of Zodanga (mentioned/target).
* **Dejah Thoris:** The Princess of Helium (mentioned as the motivation for the protagonists).
* **Zodangan Sentry:** A guard at the barracks intercepted by Carter.

**Events:**
* **The Secret Meeting:** John Carter infiltrates the quarters of Kantos Kan to inform him of Dejah Thoris's engagement to Sab Than. 
* **The Pact:** Distraught by the news, Kantos Kan vows to assassinate Sab Than via a secret palace entrance known only to the ruler. The two men devise a plan: Kantos Kan will strike the palace while Carter heads for Helium.
* **The Infiltration of the Barracks:** Carter performs a perilous climb up the side of the Zodangan barracks and uses a leather strap and hook to swing onto the roof. He subdues a sentry, binds him, and hangs him over the edge to delay discovery.
* **The Aerial Chase:** After retrieving two machines from the sheds, Carter and Kantos Kan depart. As they approach the palace, they are spotted by a patrol. Carter engages in a high-speed chase through the Martian sky, utilizing Heliumite gearing to increase his machine's speed.
* **The Crash and Disorientation:** A projectile from a Zodangan cruiser hits Carter's craft, causing him to plunge toward the ground. Though he regains control, the explosion destroys his compass and speedometer.
* **Lost in the Sky:** After six hours of flight, Carter realizes he is lost. He passes several large cities but fails to find Helium, noting that he cannot identify the city by its lack of the characteristic twin scarlet and yellow towers.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH023

| Asset ID | Description |
| :--- | :--- |
| zodanga_barracks_and_streets | Urban military architecture and narrow streets of Zodanga. |
| martian_sky_and_dead_sea_bottom | The vast aerial expanse and the desolate landscape below during flight. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_barracks_and_streets

[[SECTION markdown]]

# Zodanga Barracks and Streets

**Role:** Primary / Secondary setting

**Architecture or Geography:** High-walled military barracks with vertical climbing surfaces; rooftops accessible via exterior walls; narrow, urban street layouts characteristic of a Martian city.

**Lighting and Atmosphere Cues:** Harsh, direct sunlight typical of the Martian atmosphere; shadows cast by high architecture; sense of tension and surveillance within the urban corridors.

**Scale Cues and Recurring Environmental Anchors:** Large-scale military structures; verticality emphasized by climbing routes; rooftops serving as tactical vantage points.

**Descriptive Noun Phrases:** Zodangan stone barracks, vertical masonry walls, rooftop parapets, narrow urban canyons, high-altitude city architecture, military outpost exterior.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_sky_and_dead_sea_bottom

[[SECTION markdown]]

# Martian Sky and Dead Sea Bottom

**Role:** Transit setting

**Architecture or Geography:** A vast, open aerial expanse transitioning into the desolate, flat expanse of a dead sea bottom; distant silhouettes of large, unidentified Martian cities.

**Lighting and Atmosphere Cues:** High-altitude clarity; bright, sweeping light across the horizon; sense of immense distance and isolation; sudden flashes from projectile explosions.

**Scale Cues and Recurring Environmental Anchors:** Infinite horizon lines; massive scale of the dead sea floor; distant city skylines lacking specific landmarks (no twin scarlet/yellow towers).

**Descriptive Noun Phrases:** Desolate dead sea bed, vast Martian sky, aerial chase corridor, distant urban silhouettes, sun-bleached salt flats, high-altitude void.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
