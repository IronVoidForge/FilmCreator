# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:41:04.252361+00:00
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

Chapter id: CH002

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

**Setting:** A cave in the Arizona mountains; a rocky gorge under a clear starlight night.

**Characters:** 
- The Protagonist (experiencing paralysis, metamorphosis, and astral projection).
- Apache Warriors (who flee the cave in terror).
- The Protagonist's deceased friend (lying on the cave ledge).

**Events:**
- **Paralysis:** The protagonist wakes in a cave to find himself physically paralyzed by a mysterious, pungent vapor. 
- **The Apache Encounter:** A group of Apache warriors approaches the cave but are terrified by a low moaning sound coming from the darkness behind the protagonist; they flee in panic, causing one warrior to fall to his death.
- **Metamorphosis:** After hours of isolation, the protagonist exerts immense mental will to break the paralysis. Upon succeeding, he discovers he has undergone a metamorphosis: he is standing naked and alive, while his physical body remains lying on the cave floor, clothed and seemingly dead.
- **The Escape:** Fearing the unseen presence in the cave, the protagonist flees into the Arizona night. 
- **The Call of Mars:** While admiring the moonlit landscape, the protagonist becomes mesmerized by a large red star—Mars. He feels an irresistible pull toward the planet and, through a sudden surge of will, is transported through space via an instant of cold and darkness.
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
| arizona_mountain_cave | A dark, vapor-filled cave in the Arizona mountains. | Primary |
| rocky_gorge_nightscape | A moonlit gorge under clear starlight. | Secondary/Transit |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_mountain_cave

[[SECTION markdown]]

# Arizona Mountain Cave

**Role:** Primary setting

**Architecture & Geography:** A dark, enclosed mountain cave featuring rocky ledges and uneven floor surfaces. The space is characterized by deep shadows and narrow passages that amplify sound.

**Lighting & Atmosphere:** Thick, pungent, mysterious vapors clinging to the ground; heavy darkness; oppressive atmosphere; low-frequency moaning sounds echoing from the depths.

**Scale & Anchors:** Enclosed cave walls; a specific ledge where a body lies; a sense of claustrophobia contrasted by the vastness of the unseen darkness behind the protagonist.

**Prompt Phrases:** dark mountain cavern, pungent swirling vapors, rocky cave ledge, oppressive shadows, subterranean gloom, echoing stone chamber.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: rocky_gorge_nightscape

[[SECTION markdown]]

# Rocky Gorge Nightscape

**Role:** Secondary / Transit setting

**Architecture & Geography:** An open, rugged gorge within the Arizona mountain range; steep rocky terrain under an expansive sky.

**Lighting & Atmosphere:** Clear starlight night; bright moonlight illuminating the landscape; vast, cold, and silent atmosphere; presence of a large, mesmerizing red star (Mars) dominating the celestial view.

**Scale & Anchors:** Wide-angle vistas; immense scale of the desert night; the visual anchor of the glowing red planet Mars.

**Prompt Phrases:** moonlit rocky gorge, clear starlight sky, vast Arizona nightscape, glowing red planet Mars, cinematic desert night, wide mountain vista.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
