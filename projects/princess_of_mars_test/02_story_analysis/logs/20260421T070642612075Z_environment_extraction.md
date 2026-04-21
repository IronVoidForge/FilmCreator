# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:06:42.612075+00:00
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

Chapter id: CH007

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
The protagonist accompanies Sola and a massive military cavalcade—consisting of two hundred decorated chariots drawn by enormous animals—to a remote incubator located on a dead sea bottom. Upon arrival, the chieftain Lorquas Ptomel and Tars Tarkas oversee the hatching process. The protagonist performs a feat of physical prowess by leaping over parked chariots to impress the leaders. As the young Martians emerge from the incubator, they are captured in a ritualistic gauntlet formed by women and youths. The chapter details the brutal Martian child-rearing system: offspring are communal, raised by foster mothers without parental love, and trained solely for warfare and survival. Following the ceremony, the warriors transport eggs from subterranean vaults to the incubator, which will remain sealed for five years. Back at the dead city, the protagonist undergoes intensive training with Sola, learning the simple Martian language and developing telepathic abilities, while discovering that their own mind remains impenetrable to Martian telepathy.

**Characters:**
- **The Protagonist:** An Earthman learning Martian customs; possesses a unique mental immunity to telepathic reading.
- **Sola:** A female Martian who acts as the protagonist's guide and foster mother to a newly hatched Martian.
- **Tars Tarkas:** A Martian warrior/leader involved in the incubator ceremony.
- **Lorquas Ptomel, Jed:** The enormous chieftain overseeing the hatching.
- **The Young Martian:** A physically perfect, four-foot-tall male captured during the hatching, who becomes a rival to the protagonist during training.

**Settings:**
- **The Plaza/City:** The starting point of the journey, characterized by large chariots and communal activity.
- **The Dead Sea Bottom:** A level expanse where the incubator is located.
- **The Incubator:** A remote enclosure where Martian eggs are hatched via solar rays.
- **The Dead City:** The protagonist's base of operations during periods of idleness and training.
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
| dead_sea_bottom_incubator | A remote, level expanse containing the solar-ray hatching enclosure. |
| dead_city_plaza | A communal urban area characterized by large military chariots and ritual activity. |
| dead_city_interior | The protagonist's training grounds within the ruins of the dead city. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dead_sea_bottom_incubator

[[SECTION markdown]]

# Dead Sea Bottom Incubator

**Role:** Primary ritual setting.

**Architecture/Geography:** A vast, level expanse of a dried-up sea bed. The central feature is the incubator, a specialized enclosure designed to capture and focus solar rays for egg hatching. Nearby are subterranean vaults used for egg storage.

**Lighting/Atmosphere:** Harsh, direct solar illumination; high-contrast shadows across the flat basin; sense of desolate, ancient emptiness.

**Scale/Anchors:** Massive scale defined by the distance between the incubator and the surrounding wasteland; anchored by the presence of two hundred decorated military chariots and enormous beasts of burden.

**Prompt Phrases:** level desiccated sea bed, solar-ray hatching enclosure, vast barren basin, subterranean egg vaults, ritualistic expanse.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dead_city_plaza

[[SECTION markdown]]

# Dead City Plaza

**Role:** Secondary transit and assembly setting.

**Architecture/Geography:** A wide, open communal area within the ruins of a Martian city; paved or hard-packed ground capable of supporting heavy military movement.

**Lighting/Atmosphere:** Open sky lighting; bustling with communal activity and ritualistic movement; atmosphere of organized martial strength.

**Scale/Anchors:** Large scale; anchored by rows of decorated chariots and the presence of large-scale Martian military formations.

**Prompt Phrases:** ruined Martian plaza, wide ceremonial courtyard, heavy chariot parking, ancient stone architecture, communal assembly ground.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: dead_city_interior

[[SECTION markdown]]

# Dead City Interior

**Role:** Secondary training setting.

**Architecture/Geography:** The interior spaces of the dead city; likely composed of stone structures, corridors, or courtyards used for daily life and instruction.

**Lighting/Atmosphere:** Dimmer than the open plaza; focused on localized training areas; atmosphere of discipline and mental isolation.

**Scale/Anchors:** Human-to-Martian scale; anchored by training grounds and domestic/instructional quarters.

**Prompt Phrases:** ruined city interiors, stone training halls, Martian architectural ruins, shadowed corridors, martial instruction space.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
