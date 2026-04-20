# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:54:30.941506+00:00
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

Chapter id: CH011

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
A pretentious, ancient building near the audience chamber in the city of Korad, featuring elaborate architecture and frescoes depicting an extinct, fair-skinned race of Martians.

**Characters:**
* **John Carter:** An Earthman and rising Thark chieftain.
* **Dejah Thoris:** A princess of the red Martians; she is fascinated by ancient history and develops a deep trust in Carter.
* **Sola:** A female Thark who acts as a guardian for both Carter and Dejah Thoris.
* **Sarkoja:** A male Thark who harbors ill will toward Carter and Dejah Thoris.
* **Lorquas Ptomel:** The high-ranking chieftain of the Tharks.
* **Tars Tarkas:** A prominent Thark warrior.

**Events:**
* **Relocation:** After John Carter threatens Sarkoja to protect Dejah Thoris, he arranges for Sola to take Dejah Thoris to more secure, luxurious quarters in an ancient building.
* **Social Standing:** Sola informs Carter that his prowess has earned him the rank of eleventh among the Thark chieftains, noting that only Lorquas Ptomel ranks higher.
* **The Revelation:** In their new quarters, Dejah Thoris questions Carter's origins. Carter reveals he is from Earth (the planet Mars in his world). Despite the impossibility of his claim, Dejah Thoris chooses to believe him based on her intuition and his perceived honesty.
* **Martian Lore & Technology:** Dejah Thoris explains that Martians can observe other planets via advanced telescopic imaging technology. She also provides a history lesson on the ancient, fair-haired Martians who preceded the current red race, explaining how environmental changes forced different races to merge or compete.
* **Summons:** The peaceful conversation is interrupted by a messenger delivering a summons from Lorquas Ptomel, requiring Carter's immediate presence at the audience chamber.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [ancient_korad_quarters](ancient_korad_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_korad_quarters

[[SECTION markdown]]

# Ancient Korad Quarters

**Role:** Primary / Secondary Setting

**Architecture & Geography:**
An elaborate, pretentious structure located near the central audience chamber of the city of Korad. The architecture is characterized by ancient, high-status design featuring intricate frescoes on the walls. These murals depict an extinct race of fair-skinned Martians.

**Lighting & Atmosphere:**
Luxurious and secure; a sense of historical weight and quiet dignity compared to the rugged Thark encampments. The atmosphere is one of scholarly antiquity and sheltered prestige.

**Scale & Anchors:**
Large, high-ceilinged rooms designed for high-ranking inhabitants. Recurring anchors include the detailed wall frescoes and the proximity to the city's political center (the audience chamber).

**Prompt Phrases:**
Ancient Martian architecture, elaborate frescoes, extinct race murals, Korad city interior, luxurious ancient quarters, historical Martian ruins, high-status stone masonry.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
