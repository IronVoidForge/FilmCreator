# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:49:19.754116+00:00
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

**Setting:** A circular basin on Mars covered in yellowish, moss-like vegetation, featuring quartz-bearing rock outcroppings and a low, walled glass enclosure (an incubator).

**Events:**
- The protagonist wakes up on Mars and discovers the effects of low gravity, finding that even simple movements result in massive leaps.
- He explores a nearby glass-roofed enclosure and observes several hundred large white eggs; some have hatched into grotesque, six-limbed young creatures.
- A party of twenty Martian warriors on eight-legged mounts approaches. The leader nearly kills the protagonist with a forty-foot spear, but the protagonist narrowly escapes by performing a massive thirty-foot leap over the incubator.
- The Martians, astonished by his agility rather than angered by his presence near their young, decide to capture him as a curiosity.
- The leader of the party dismounts, approaches unarmed, and offers a metal armlet as a gesture of peace. 
- The protagonist accepts the armlet, signaling friendship. He is then hoisted onto a Martian mount and taken away by the cavalcade toward distant hills.

**Characters:**
- **The Protagonist:** An Earthman, currently naked and unarmed, possessing superhuman agility due to the Martian gravity.
- **Martian Warriors:** Fifteen-foot-tall humanoids with four arms (two right, two left), red eyes, and white tusks. They are highly skilled with long-range radium rifles.
- **The Leader:** A prominent warrior who initiates peaceful contact through gesture and a gift of an armlet.
- **Martian Mounts:** Ten-foot-tall, eight-legged, slate-colored animals with glossy skin and no hair.

**Key Technology/Biology:**
- **Incubator:** A glass-roofed structure used for hatching Martian eggs.
- **Martian Rifles:** Highly advanced weapons made of white metal and wood, capable of firing radium projectiles at extreme ranges (up to 200+ miles).
- **Martian Anatomy:** Multi-limbed, large-boned, and possessing antenna-like ears and independent eyes.
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
| circular_moss_basin | A yellowish, moss-covered basin containing quartz outcroppings and a glass incubator. |
| martian_distant_hills | The distant landscape traversed by the Martian cavalry. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: circular_moss_basin

[[SECTION markdown]]

# Circular Moss Basin

**Role:** Primary setting

**Architecture & Geography:** A wide, circular basin on the Martian surface. The ground is covered in a thick layer of yellowish, moss-like vegetation. Scattered throughout the basin are jagged rock outcroppings containing visible quartz veins. Centrally located is a low, walled glass enclosure serving as an incubator.

**Lighting & Atmosphere:** Diffuse Martian light filtered through a thin atmosphere; high-contrast shadows cast by quartz outcroppings. The atmosphere feels alien and biological due to the pervasive moss.

**Scale & Anchors:** Large-scale basin floor; the glass incubator acts as a central focal point; quartz veins provide micro-scale texture against the macro-scale basin.

**Prompt Phrases:** yellowish mossy terrain, quartz-bearing rock outcroppings, low walled glass incubator, circular Martian basin, alien vegetation textures.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_distant_hills

[[SECTION markdown]]

# Martian Distant Hills

**Role:** Transit setting / Background

**Architecture & Geography:** Rolling, distant hills forming the horizon of the Martian landscape.

**Lighting & Atmosphere:** Hazy, atmospheric perspective; distant silhouettes against a Martian sky.

**Scale & Anchors:** Massive scale; provides a sense of vastness and distance for the traveling cavalcade.

**Prompt Phrases:** distant martian hills, hazy horizon, sweeping alien landscape, far-off geological formations.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
