# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:35:31.889914+00:00
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
- He explores a nearby glass-roofed enclosure and observes several hundred large white eggs; some have hatched into grotesque, six-limbed creatures with independent eyes and antennae.
- A party of twenty Martian warriors on eight-legged mounts approaches. The leader nearly kills the protagonist with a forty-foot spear, but the protagonist escapes by performing a massive thirty-foot leap over the incubator.
- Impressed by his agility rather than threatened by him, the Martians view him as a curiosity rather than an enemy.
- The leader of the party dismounts, approaches unarmed, and offers a metal armlet as a gesture of peace. 
- The protagonist accepts the armlet, signaling friendship. He is then hoisted onto a Martian mount and taken away by the cavalcade toward distant hills.

**Characters:**
- **The Protagonist:** An Earthman, currently naked and unarmed, possessing superhuman agility due to the Martian gravity.
- **Martian Warriors:** Fifteen-foot-tall humanoids with four arms (two right, two left), olive-green skin, and blood-red eyes. They are highly skilled with long spears and advanced radium-projectile rifles.
- **The Leader:** A prominent Martian warrior who initiates peaceful contact through gesture and a gift of an armlet.

**Key Elements/Technology:**
- **Martian Mounts:** Massive, eight-legged animals with slate-colored skin and no hair.
- **Martian Rifles:** Highly advanced weapons made of white metal and hard wood, capable of extreme long-range accuracy (up to 200+ miles).
- **The Incubator:** A glass-roofed structure used for hatching Martian lifeforms.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [arizona_quartz_vein_basin](arizona_quartz_vein_basin)
- [martian_incubator_enclosure](martian_incubator_enclosure)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_basin

[[SECTION markdown]]

# Arizona Quartz Vein Basin

**Role:** Primary setting / Transit setting.

**Geography:** A vast, circular basin on the Martian surface characterized by yellowish, moss-like vegetation and scattered quartz-bearing rock outcroppings. The terrain is rugged but open, facilitating large leaps and long-range visibility.

**Lighting and Atmosphere:** Bright, direct Martian sunlight; thin atmosphere with high clarity; grounded in a palette of yellow vegetation and pale quartz stone.

**Scale Cues:** Expansive basin floor; distant hills visible on the horizon; scale defined by the massive leaps of inhabitants and the movement of large eight-legged mounts.

**Prompt Phrases:** circular Martian basin, yellowish mossy vegetation, quartz rock outcroppings, vast red planet landscape, low gravity terrain, expansive desert basin.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_incubator_enclosure

[[SECTION markdown]]

# Martian Incubator Enclosure

**Role:** Secondary setting / Narrative anchor.

**Architecture:** A low, walled structure featuring a transparent glass roof designed for hatching and observing lifeforms.

**Lighting and Atmosphere:** Diffused light filtering through the glass roof; contained, sheltered atmosphere compared to the open basin; biological/organic undertones from hatching creatures.

**Scale Cues:** Low-profile walls; interior space large enough to house hundreds of large white eggs and multiple six-limbed hatchlings.

**Prompt Phrases:** low walled enclosure, glass-roofed incubator, translucent ceiling, biological nursery, Martian egg chamber, sheltered glass structure.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
