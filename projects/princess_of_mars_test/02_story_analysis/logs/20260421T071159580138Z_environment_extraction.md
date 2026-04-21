# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:11:59.580138+00:00
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

Chapter id: CH009

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
- The protagonist receives a set of Martian warrior's arms and ornaments from a respectful yet menacing warrior.
- Sola and other women remodel the gear to fit the protagonist, who then begins training with the Martian youth in the plaza.
- The protagonist observes the social structure: women are the primary manufacturers and educators, while men handle strategy and law.
- Through persistent study, the protagonist masters the Martian language, allowing him to eavesdrop on the adults in his sleeping quarters.
- During a nighttime conversation, the protagonist learns through Sarkoja that the beautiful Red Martian prisoner is being taken to Thark to be executed at the great games rather than held for ransom.
- A heated argument breaksence between Sola and Sarkoja; Sola expresses sympathy for the prisoner and criticizes the constant, senseless bloodshed of Green Martian culture.
- The protagonist resolves to eventually confide in Sola to plan an escape.

**Characters:**
- **The Protagonist:** An Earthman learning Martian combat skills and language; observant and calculating.
- **Sola:** A female Green Martian who is kind to the protagonist and expresses unconventional empathy for the Red prisoner, much to the disapproval of her peers.
- **Sarkoja:** An older, more hardened female Green Martian who reprimands Sola for her "weak" sentiments.
- **The Prisoner:** A beautiful Red Martian woman being transported to Thark for execution.
- **The Women/Young Martians:** The community members providing training and social context.

**Settings:**
- **The Plaza:** Where the protagonist practices combat with the young Martians.
- **The Sleeping Quarters:** A communal living space shared by several females, young Martians, the protagonist, Sola, and Woola the hound.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

| Asset ID | Description |
| :--- | :--- |
| martian_plaza | Open training area for combat and social gathering. |
| communal_sleeping_quarters | Shared living space for the female community and protagonist. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plaza

[[SECTION markdown]]

# Martian Plaza

**Role:** Primary / Social Setting

**Architecture & Geography:** An open-air communal plaza serving as a central hub for physical training and social observation. Likely characterized by hard-packed Martian soil or stone paving suitable for combat drills.

**Lighting & Atmosphere:** Bright, exposed sunlight; high visibility; active and energetic atmosphere filled with the sounds of training and movement.

**Scale & Anchors:** Large open expanse; anchored by groups of young Martians engaged in combat practice and social clusters of women.

**Prompt Phrases:** wide open Martian plaza, sun-drenched training ground, dusty combat arena, communal gathering space, martial training grounds.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: communal_sleeping_quarters

[[SECTION markdown]]

# Communal Sleeping Quarters

**Role:** Secondary / Interior Setting

**Architecture & Geography:** A shared, multi-occupant living space. Functional and communal in design, housing several females, young Martians, the protagonist, and a large hound (Woola).

**Lighting & Atmosphere:** Dim, nighttime lighting; intimate but crowded; atmosphere of hushed conversations, eavesdropping, and domestic tension.

**Scale & Anchors:** Enclosed interior space; anchored by sleeping mats/areas and communal floor space occupied by inhabitants and animals.

**Prompt Phrases:** dim communal dormitory, Martian living quarters, shared sleeping chamber, low-light interior, crowded domestic space.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
