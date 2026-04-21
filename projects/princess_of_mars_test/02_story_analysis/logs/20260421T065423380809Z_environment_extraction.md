# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:54:23.380809+00:00
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

Chapter id: CH003

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

**Setting:** A circular basin on Mars covered in yellowish, moss-like vegetation, featuring a low walled enclosure with a glass roof (an incubator).

**Events:**
- The protagonist wakes up on Mars and discovers the effects of low gravity, finding that simple movements cause him to leap great distances.
- He explores a nearby enclosure and discovers it is an incubator containing large white eggs; several grotesque, multi-limbed young Martians have already hatched.
- A party of twenty mounted Martian warriors approaches. The protagonist narrowly avoids being killed by the leader's spear after hearing the rattle of equipment.
- To escape, the protagonist performs a massive leap (thirty feet into the air), landing on the far side of the enclosure. This display of agility shifts the Martians' perception of him from prey to a "wonderful discovery."
- The protagonist observes the Martians' advanced weaponry, specifically long-range rifles made of white metal and wood.
- The leader of the party dismounts, approaches unarmed, and offers the protagonist a metal armlet as a gesture of peace.
- The protagonist accepts the armlet, signaling his peaceful intent. He is then lifted onto a Martian mount and taken away with the cavalcade toward distant hills.

**Characters:**
- **The Protagonist:** An Earthman, currently naked and unarmed, possessing superior agility due to the low gravity.
- **Martian Warriors:** Large (15ft), four-armed humanoids with olive-green skin, red eyes, and tusks. They ride eight-legged, slate-colored animals.
- **The Leader:** A Martian warrior who initiates peaceful contact through gesture and a gift of an armlet.

**Key Details for Scene Extraction:**
- The physical sensation of low gravity (the "ludicrous" attempts at walking).
- The visual description of the hatching Martians inside the glass incubator.
- The tension of the near-death encounter with the spear.
- The non-verbal communication exchange between the protagonist and the Martian leader.
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
| circular_moss_basin | A yellowish, moss-covered basin containing an incubator structure. |
| martian_distant_hills | The rolling landscape toward which the Martian cavalcade travels. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: circular_moss_basin

[[SECTION markdown]]

# Circular Moss Basin

**Role:** Primary setting

**Architecture & Geography:** A wide, circular basin on the Martian surface. The ground is covered in a thick layer of yellowish, moss-like vegetation. Centrally located is a low-walled enclosure topped with a transparent glass roof, functioning as an incubator.

**Lighting & Atmosphere:** Bright, direct Martian light filtered through the glass roof; atmosphere feels alien and biological due to the presence of hatching organisms.

**Scale & Anchors:** The glass incubator serves as the central anchor; scale is defined by the contrast between the low walls and the massive 15ft Martian warriors.

**Prompt Phrases:** yellowish mossy basin, circular vegetation field, glass-roofed incubator enclosure, low walled biological station, alien hatching site.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_distant_hills

[[SECTION markdown]]

# Martian Distant Hills

**Role:** Transit setting / Background

**Architecture & Geography:** Rolling, distant hills visible on the horizon of the Martian landscape.

**Lighting & Atmosphere:** Vast, open sky; sense of immense scale and distance as the cavalcade moves away from the basin.

**Scale & Anchors:** The horizon line and the movement of the mounted warriors toward the distance.

**Prompt Phrases:** rolling martian hills, distant desert topography, vast alien horizon, sweeping landscape vistas.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
