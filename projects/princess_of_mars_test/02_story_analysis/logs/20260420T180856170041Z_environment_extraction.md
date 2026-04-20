# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:08:56.170041+00:00
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

Chapter id: CH020

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
After a failed attempt to meet Kantos Kan, the protagonist embarks on a two-week trek northwest through the Martian wilderness. During this journey, he survives on vegetable milk and narrowly avoids several beast attacks, one of which is only thwarted by the intervention of his emaciated calot, Woola. On the fifteenth day, the protagonist discovers a massive, four-square-mile atmosphere factory. After gaining entry through automated doors, he is hosted by an invisible entity and meets a withered old man who has guarded the facility for eight hundred years. Through telepathy, the protagonist learns that the plant uses a "ninth ray" to generate life-sustaining air, which is then distributed via radium pumps to five principal centers across Mars.

The situation turns dangerous when the protagonist senses the old man's murderous intent; the guardian plans to kill him to protect the factory's secrets. Using his telepathic abilities to manipulate the facility's thought-wave locks, the protagonist manages to escape with Woola. While traveling toward the central turnpike, he is intercepted by hospitable Red Martians who take him into their elevated home. To assist his journey to Zodanga, the Red Martians provide him with a disguise—anointing his skin with reddish oil and cutting his hair in the local fashion—and supply him with Zodangan money and a bullthoat. He departs for Zodanga following their advice that military service is the most effective way to gain status and trust.

**Characters:**
* **The Protagonist:** An Earthman with telepathic powers who is recognized as biologically distinct from Barsoomians; he is currently exhausted and starving.
* **Woola:** A faithful, though seemingly emaciated, calot who protects the protagonist from wild beasts.
* **The Invisible Host:** An entity within the factory that can see through the protagonist's body but cannot read his thoughts.
* **The Old Man:** A mummy-like guardian of the atmosphere pumps for eight centuries; he wears a nine-rayed diadem and attempts to kill the protagonist to protect the plant's secrets.
* **Red Martians:** A hospitable group of inhabitants who provide the protagonist with local disguises, currency, and transport.

**Settings:**
* **The Martian Wilderness:** A dangerous landscape filled with strange beasts and vegetation that yields vegetable milk.
* **The Atmosphere Factory:** A massive, highly secure concrete facility containing automated doors and machinery used to generate the Martian atmosphere via the ninth ray.
* **Red Martian Home:** A structure raised on a metal shaft for safety, reflecting local social structures and customs.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [martian_wilderness](martian_wilderness)
- [atmosphere_factory](atmosphere_factory)
- [red_martian_elevated_home](red_martian_elevated_home)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_wilderness

[[SECTION markdown]]

# Martian Wilderness

**Role:** Primary / Transit Setting

**Geography:** Vast, rugged northwest Martian terrain; desolate landscapes punctuated by strange vegetation capable of yielding vegetable milk.

**Lighting and Atmosphere:** Harsh, exposed sunlight; sense of isolation and constant predatory threat; dry and dusty atmosphere.

**Scale and Anchors:** Expansive horizons; scattered patches of alien flora; tracks of wild beasts.

**Prompt Phrases:** vast martian desert, rugged wilderness, alien vegetation, desolate wasteland, harsh sun, predator-filled landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: atmosphere_factory

[[SECTION markdown]]

# Atmosphere Factory

**Role:** Primary Setting

**Architecture:** Massive four-square-mile concrete facility; automated heavy doors; complex internal machinery; high-security industrial design.

**Lighting and Atmosphere:** Artificial lighting; humming energy from the "ninth ray"; sterile yet ancient; sense of immense, hidden power.

**Scale and Anchors:** Colossal scale; radium pumps; central ninth-ray generator; thought-wave locks.

**Prompt Phrases:** massive concrete factory, industrial atmosphere plant, ninth ray machinery, radium pumps, high-tech ancient facility, automated heavy doors.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: red_martian_elevated_home

[[SECTION markdown]]

# Red Martian Elevated Home

**Role:** Secondary Setting

**Architecture:** Raised structures built upon tall metal shafts for protection against ground-based threats.

**Lighting and Atmosphere:** Sheltered, communal atmosphere; sense of safety from the wilderness below; local cultural aesthetic.

**Scale and Anchors:** Verticality; elevated platforms; metal support shafts; domestic Martian interior.

**Prompt Phrases:** elevated martian dwelling, structure on metal shaft, high-altitude home, red martian architecture, protected settlement.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
