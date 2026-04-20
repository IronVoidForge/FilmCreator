# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:42:24.573697+00:00
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

**Setting:** A circular basin on Mars covered in yellowish, moss-like vegetation, featuring a low walled enclosure with a thick glass roof (an incubator).

**Events:**
- The protagonist wakes up on Mars and discovers the effects of low gravity, finding that even small movements result in massive leaps.
- He explores a nearby enclosure and discovers it is an incubator containing large white eggs; several grotesque, six-limbed young Martians have already hatched.
- A party of twenty Martian warriors on multi-legged mounts approaches. The leader nearly kills the protagonist with a forty-foot spear, but the protagonist escapes by performing a massive thirty-foot leap over the incubator.
- Impressed by his agility rather than angered by his presence, the Martians view him as a curiosity rather than a threat.
- The leader dismounts, approaches unarmed, and offers a metal armlet as a gesture of peace. 
- The protagonist accepts the armlet, signaling friendship. He is then hoisted onto a Martian mount and taken away with the cavalcade toward distant hills.

**Characters:**
- **The Protagonist:** An Earthman, currently naked and unarmed, possessing superior agility due to Mars' low gravity.
- **Martian Warriors:** Large (15ft tall), multi-limbed humanoids with olive/green skin and red eyes. They are highly skilled with advanced long-range rifles.
- **The Leader:** A Martian warrior who initiates peaceful contact through gestures and the offering of an armlet.
- **Martian Mounts:** Massive, eight-legged animals with slate-colored skin and no hair.

**Key Elements for Scene Extraction:**
- The physical sensation of low-gravity movement (the "ludicrous" hopping).
- The visual reveal of the hatching Martian eggs inside the glass enclosure.
- The high-tension standoff between the protagonist and the charging cavalry.
- The non-verbal peace negotiation involving the metal armlet.
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
| circular_moss_basin | A yellowish, moss-covered basin containing a glass incubator. |
| martian_distant_hills | The vast, rolling landscape toward which the Martian cavalry travels. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: circular_moss_basin

[[SECTION markdown]]

# Circular Moss Basin

**Role:** Primary setting

**Architecture & Geography:** A large, circular basin on the Martian surface. The ground is covered in a thick layer of yellowish, moss-like vegetation. Centrally located is a low-walled enclosure topped with a heavy, thick glass roof, functioning as an incubator.

**Lighting & Atmosphere:** Bright, direct Martian sunlight filtered through a dusty atmosphere; high-contrast shadows within the basin; the interior of the incubator features soft, diffused light through the glass.

**Scale & Anchors:** The low-walled incubator serves as a central anchor; scale is defined by the massive size of the hatched Martian young and the height of the glass enclosure.

**Prompt Phrases:** yellowish mossy terrain, circular basin, thick glass roof incubator, low walled enclosure, Martian vegetation, high-contrast desert light.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_distant_hills

[[SECTION markdown]]

# Martian Distant Hills

**Role:** Secondary / Transit setting

**Architecture & Geography:** Vast, rolling hills in the distance, characteristic of the Martian landscape.

**Lighting & Atmosphere:** Hazy, distant horizon; atmospheric perspective creating a sense of immense scale and depth.

**Scale & Anchors:** The hills serve as a massive backdrop for the traveling Martian cavalcade, emphasizing the vastness of the planet.

**Prompt Phrases:** rolling martian hills, hazy distant horizon, vast desert landscape, sweeping vistas, alien topography.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
