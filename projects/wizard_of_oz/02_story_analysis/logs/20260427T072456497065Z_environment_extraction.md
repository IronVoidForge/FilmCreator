# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:24:56.497065+00:00
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
Project slug: wizard_of_oz

Chapter id: CH018

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

**Setting:** The Throne Room in the Emerald City.

**Characters:** Dorothy, Scarecrow (now ruler of the Emerald City), Tin Woodman, Cowardly Lion, the Monkey King and his band of Winged Monkeys, and a Soldier with green whiskers.

**Events:**
- Following Oz's departure via balloon, the group mourns his loss; the Tin Woodman is comforted by Dorothy to prevent rusting.
- The Scarecrow, now the official ruler of the Emerald City, convenes a meeting with the travelers in the Throne Room.
- Dorothy expresses her desire to return to Kansas, prompting the Scarecrow to suggest using the Golden Cap to summon the Winged Monkeys for transport.
- The Monkey King appears but refuses to fly Dorothy across the desert, stating that Winged Monkeys are bound to their own country and cannot leave it.
- Seeking an alternative, the group summons a soldier who suggests seeking help from Glinda, the Good Witch of the South, who lives on the edge of the desert.
- The soldier warns that the road south is dangerous, filled with wild beasts and hostile people.
- Despite the risks, Dorothy, the Lion, the Tin Woodman, and the Scarecrow decide to depart for the South the following morning to seek Glinda's aid.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [emerald_city_throne_room](#emerald_city_throne_room)
- [the_great_desert_border](#the_great_desert_border)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: emerald_city_throne_room

[[SECTION markdown]]

# Emerald City Throne Room

**Role:** Primary setting.

**Architecture & Geography:** A grand, ceremonial chamber designed for a ruler. The space is dominated by the throne of the Scarecrow and reflects the opulence of the Emerald City.

**Lighting & Atmosphere:** Brilliant, green-tinted light; high-status, formal, yet currently heavy with mourning and political transition.

**Scale & Anchors:** Large-scale ceremonial hall; central throne as the primary anchor; vast floor space for gatherings of travelers and officials.

**Descriptive Noun Phrases:** Emerald-hued grandeur, ceremonial throne room, glittering green architecture, royal assembly chamber, polished emerald surfaces.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: the_great_desert_border

[[SECTION markdown]]

# The Great Desert Border

**Role:** Transit setting / Obstacle.

**Architecture & Geography:** A vast, inhospitable expanse of sand and dunes marking the boundary of the known territories; transition zone between the Emerald City and the South.

**Lighting & Atmosphere:** Harsh, unrelenting sunlight; heat haze; sense of isolation and extreme danger; wild and untamed.

**Scale & Anchors:** Infinite horizon; shifting sand dunes; presence of wild beasts and hostile elements.

**Descriptive Noun Phrases:** Scorching desert expanse, treacherous dune landscapes, sun-bleached wasteland, dangerous southern frontier, vast arid emptiness.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
