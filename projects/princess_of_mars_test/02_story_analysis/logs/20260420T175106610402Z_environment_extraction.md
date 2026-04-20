# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:51:06.610402+00:00
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
The protagonist undergoes a period of rapid adaptation, receiving Martian warrior attire and training in various weapons under the instruction of Sola and other females. He learns that Green Martian society is divided by gendered roles: women are the artisans, manufacturers, and defenders, while men focus on high-level strategy and law. Driven by curiosity regarding a beautiful Red female prisoner he witnessed being treated brutally, the protagonist pushes himself to master the Martian language. Through eavesdropping on a late-night conversation among the women in his sleeping quarters, he learns that the prisoner is destined to be taken to Thark to die in public games. A heated argument breaks out between Sola and Sarkoja; Sola expresses sympathy for the captive, which the others view as a sign of weakness and "atavism." This interaction confirms Sola's compassionate nature and motivates the protagonist to plan an eventual escape with her help.

**Characters:**
- **The Protagonist:** An Earthman learning Martian combat and language; determined to find his own kind.
- **Sola:** A Green Martian female who acts as a mentor/guardian to the protagonist; shows unexpected empathy for the Red prisoner, defying social norms.
- **Sarkoja:** An older, more hardened Green Martian woman; critical of Sola's perceived weakness.
- **The Prisoner:** A beautiful "Red" Martian woman being held for public execution.
- **The Women (Group):** Artisans and warriors who manage the domestic and manufacturing aspects of their society.

**Settings:**
- **The Plaza/Training Grounds:** Where the protagonist practices combat with the Martian youth.
- **The Sleeping Quarters:** A communal living space shared by several females, young Martians, the protagonist, Sola, and Woola the hound; the site of the pivotal overheard conversation.
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
| martian_training_plaza | Open-air combat and training grounds for Martian youth and warriors. |
| communal_sleeping_quarters | Shared living space for Green Martian females, youths, and the protagonist. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_training_plaza

[[SECTION markdown]]

# Martian Training Plaza

**Role:** Primary / Secondary (Training)

**Architecture & Geography:** An open-air expanse designed for physical conditioning and combat drills. Likely integrated into the larger Green Martian settlement architecture, featuring durable surfaces suitable for weapon practice.

**Lighting & Atmosphere:** Bright, exposed Martian sunlight; dusty atmosphere typical of outdoor training areas; high visibility.

**Scale & Anchors:** Large scale to accommodate groups of youths and warriors; anchored by training equipment and martial instructors.

**Prompt Phrases:** open-air combat arena, martian dust, sun-drenched training grounds, martial drill expanse, stone-paved plaza.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: communal_sleeping_quarters

[[SECTION markdown]]

# Communal Sleeping Quarters

**Role:** Primary (Social/Narrative)

**Architecture & Geography:** A shared, multi-occupant living space. Contains sleeping areas for various demographics including females, young Martians, and the protagonist. Includes space for a Martian hound (Woola).

**Lighting & Atmosphere:** Dimly lit at night; intimate but communal; heavy with the sounds of conversation and breathing; enclosed atmosphere.

**Scale & Anchors:** Medium scale; crowded/dense occupancy; anchored by sleeping mats, personal belongings, and shared domestic spaces.

**Prompt Phrases:** communal dormitory, dim nocturnal lighting, shared living quarters, martian interior, crowded sleeping chamber.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
