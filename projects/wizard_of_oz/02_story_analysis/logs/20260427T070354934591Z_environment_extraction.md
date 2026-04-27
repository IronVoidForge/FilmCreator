# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:03:54.934591+00:00
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

Chapter id: CH008

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

**Setting:** A sunny country featuring a wide river with a swift current, a grassy riverbank, and a vast meadow filled with scarlet poppies.

**Characters:** Dorothy, Toto, Scarecrow, Tin Woodman, Cowardly Lion, and a Stork.

**Events:**
- **The River Crossing:** The group attempts to cross a wide river on a makeshift raft. During the crossing, the current sweeps them downstream, causing the Scarecrow to become stuck on his pole in the middle of the river.
- **The Rescue of the Scarecrow:** After the raft reaches the shore, the group realizes they have lost the Scarecrow. A passing Stork agrees to help and flies out to retrieve the Scarecrow, carrying him back to the group.
- **The Poppy Field:** As the travelers walk along the riverbank toward the Yellow Brick Road, they enter a massive meadow of scarlet poppies. The scent of these flowers is deadly, causing anyone who breathes it to fall into an eternal sleep.
- **The Sleeping Danger:** Dorothy and Toto succumb to the scent and fall asleep in the field. The Cowardly Lion also falls asleep because he is too heavy for the others to carry. 
- **The Escape:** Because they are not made of flesh, the Scarecrow and Tin Woodman are immune to the scent. They form a "human chair" to carry the sleeping Dorothy and Toto out of the field. They manage to reach safety, but they are forced to leave the Cowardly Lion behind in the poppy field, fearing he will sleep forever.
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
| swift_river_crossing | A wide, fast-moving river with grassy banks and a dangerous current. |
| scarlet_poppy_meadow | A vast, immersive field of red flowers with a heavy, narcotic atmosphere. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: swift_river_crossing

[[SECTION markdown]]

# Swift River Crossing

**Role:** Transit setting / Obstacle

**Architecture or Geography:** A wide, expansive river characterized by a powerful and swift current. The banks are composed of lush, green grassy slopes that meet the water's edge.

**Lighting and Atmosphere Cues:** Bright, sunny daylight; high-contrast reflections on moving water; sense of kinetic energy and danger from the rushing current.

**Scale Cues and Recurring Environmental Anchors:** Wide horizontal expanse of water; makeshift wooden raft; riverbank vegetation; mid-river poles or obstructions.

**Descriptive Noun Phrases:** Rushing river current, grassy riverbank, sun-drenched waterway, wide aquatic expanse, swift-moving stream.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: scarlet_poppy_meadow

[[SECTION markdown]]

# Scarlet Poppy Meadow

**Role:** Primary setting / Hazard zone

**Architecture or Geography:** A massive, seemingly endless meadow dominated by dense clusters of scarlet poppies. The terrain is soft and undulating under the floral canopy.

**Lighting and Atmosphere Cues:** Dreamlike, hazy atmosphere; heavy, narcotic scent-laden air; dappled sunlight filtering through flower heads; a sense of beautiful but deadly lethargy.

**Scale Cues and Recurring Environmental Anchors:** Vast horizon of red; waist-high scarlet blooms; repetitive floral patterns; the distant Yellow Brick Road as a boundary.

**Descriptive Noun Phrases:** Endless field of scarlet poppies, narcotic floral meadow, dense red bloom canopy, heavy scented air, crimson flower sea.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
