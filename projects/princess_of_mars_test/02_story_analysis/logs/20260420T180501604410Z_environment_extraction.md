# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:05:01.605413+00:00
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

**Setting:**
The chapter moves from a small medical room to the open Martian plains during a military march, eventually concluding in the pitch-black, claustrophobic dungeons of the city of Warhoon.

**Characters:**
* **Protagonist:** A human survivor who has been wounded and is being held captive by the Warhoons.
* **Dak Kova:** A scarred, ferocious Warhoon warrior/jed; a former lieutenant who is ambitious, insubordinate, and murderous.
* **Bar Comas:** The young Jeddak of the Warhoon hordes, characterized by dignity and strength before his violent death.
* **The Female Healer:** An ancient, ugly Warhoon woman who treats the protagonist's wounds.
* **Warhoon Warriors/Jeddaks:** A bloodthirsty tribe known for wearing human skulls and dried hands as trophies; they are more ferocious than the Tharks.

**Key Events:**
* **Recovery and Transport:** The protagonist regains consciousness after being treated by a Warhoon female. He is strapped to a wild thoat and forced to ride with the main column of the Warhoon army.
* **The Duel for Power:** During a confrontation before the Jeddak Bar Comas, Dak Kova openly defies his leader. This escalates into a primal, animalistic duel between the two warriors. Bar Comas is killed in a brutal manner, allowing Dak Kova to seize the title of Jeddak.
* **The March to Warhoon:** The Warhoon army turns back toward their city after the delay caused by the duel. The protagonist observes the extreme violence and frequent duels inherent to Warhoon culture.
* **Imprisonment:** Upon reaching Warhoon, the protagonist is cast into a dark dungeon and chained to the floor for an indeterminate amount of time, suffering intense psychological terror in the darkness.
* **The Escape Attempt:** Driven to near-madness, the protagonist ambushes his food deliverer with his heavy chains, killing him. He recovers his senses upon finding the jailer's keys on the corpse.
* **The Eyes in the Dark:** As the protagonist prepares to use the keys, he is confronted by several pairs of gleaming eyes watching him from the darkness of the dungeon, which then retreat into the shadows.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH018

- [warhoon_medical_room](#warhoon_medical_room)
- [martian_plains_march_route](#martian_plains_march_route)
- [warhoon_city_dungeons](#warhoon_city_dungeons)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_medical_room

[[SECTION markdown]]

# Warhoon Medical Room

**Role:** Secondary setting (initial recovery)

**Architecture/Geography:** Small, cramped medical chamber within a Warhoon settlement.

**Lighting and Atmosphere:** Dimly lit, utilitarian, smelling of medicinal herbs and blood; oppressive and primitive.

**Scale Cues:** Small-scale, enclosed, intimate but threatening.

**Prompt Phrases:** small stone room, ancient healer's quarters, dim torchlight, primitive medical tools, cramped interior.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plains_march_route

[[SECTION markdown]]

# Martian Plains March Route

**Role:** Transit setting (military procession)

**Architecture/Geography:** Vast, open Martian plains; rugged terrain suitable for wild thoat travel.

**Lighting and Atmosphere:** Harsh sunlight or twilight, dusty atmosphere, wide-open vistas interrupted by the movement of a massive military column.

**Scale Cues:** Expansive, horizon-to-horizon scale; large-scale troop movements.

**Prompt Phrases:** vast Martian plains, rugged desert landscape, sweeping horizons, dust clouds from marching armies, wide open sky.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_city_dungeons

[[SECTION markdown]]

# Warhoon City Dungeons

**Role:** Primary setting (imprisonment and climax)

**Architecture/Geography:** Subterranean stone cells, pitch-black corridors, heavy iron chains anchored to floors.

**Lighting and Atmosphere:** Absolute darkness, claustrophobic, terrifying, psychological dread; occasional glints of light from eyes in the shadows.

**Scale Cues:** Enclosed, tight spaces; deep subterranean depths.

**Prompt Phrases:** pitch-black dungeon, stone prison cell, heavy iron chains, claustrophobic underground chamber, gleaming eyes in darkness, damp stone walls.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
