# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:35:14.560387+00:00
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

**Setting:** A room within Glinda's Castle and the Kansas prairie.

**Characters:** 
- Dorothy: Seeking to return to Kansas.
- Scarecrow: Desires to return to the Emerald City to rule.
- Tin Woodman: Desires to return to the West to rule the Winkies.
- Lion: Desires to return to his forest to be King of the beasts.
- Glinda the Good Witch: A beautiful, red-haired ruler on a ruby throne.
- Uncle Henry & Toto: Appearing in the final scene.

**Events:**
- The companions prepare themselves and meet Glinda in her ruby throne room.
- Dorothy explains her desire to return to Kansas to Aunt Em and Uncle Henry.
- Glinda agrees to help Dorothy on the condition that Dorothy surrenders the Golden Cap.
- Dorothy hands over the Golden Cap. Glinda uses its power to make three commands to the Winged Monkeys: 
    1. Carry the Scarecrow to the Emerald City.
    2. Carry the Tin Woodman to the land of the Winkies.
    3. Carry the Lion to his forest.
- After the commands, Glinda intends to give the Cap to the King of the Monkeys to grant them freedom.
- Glinda reveals that Dorothy's Silver Shoes have the power to transport her anywhere in three steps by clicking the heels together.
- The companions share a tearful farewell, acknowledging how their journey provided them with the qualities they originally sought.
- Dorothy clicks her heels three times and commands the shoes to take her home to Kansas.
- Dorothy arrives instantly on the Kansas prairie in front of her new farmhouse, but the Silver Shoes fall off during the flight and are lost forever in the desert.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [glinda_castle_throne_room](#glinda_castle_throne_room)
- [kansas_prairie_farmstead](#kansas_prairie_farmstead)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: glinda_castle_throne_room

[[SECTION markdown]]

# Glinda's Castle Throne Room

**Role:** Primary setting for the resolution of character arcs.

**Architecture & Geography:** An opulent, magical interior space centered around a prominent ruby throne. The architecture is designed to convey high magic and sovereign authority.

**Lighting & Atmosphere:** Radiant, shimmering, and ethereal. The atmosphere is heavy with enchantment and the presence of powerful sorcery.

**Scale & Anchors:** Grand scale; the ruby throne serves as the central environmental anchor for all character interactions.

**Descriptive Noun Phrases:** Ruby throne, enchanted castle interior, magical sovereign chamber, shimmering halls, high-magic architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: kansas_prairie_farmstead

[[SECTION markdown]]

# Kansas Prairie Farmstead

**Role:** Primary setting for the resolution and final scene.

**Architecture & Geography:** A flat, expansive prairie landscape featuring a farmhouse and immediate domestic surroundings. The terrain is grounded and rural.

**Lighting & Atmosphere:** Naturalistic, bright, and earthly. The atmosphere is one of homecoming and mundane reality compared to the magical realms.

**Scale & Anchors:** Wide-open horizon; the farmhouse serves as the primary structural anchor in an otherwise vast, flat landscape.

**Descriptive Noun Phrases:** Flat Kansas prairie, rural farmhouse, dusty plains, wide horizon, domestic homestead, sun-drenched farmland.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
