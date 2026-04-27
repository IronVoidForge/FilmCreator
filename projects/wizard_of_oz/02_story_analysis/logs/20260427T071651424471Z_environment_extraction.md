# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:16:51.424471+00:00
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

Chapter id: CH014

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

**Setting:** The vast, scarlet fields of buttercups and yellow daisies between the Wicked Witch's castle and the Emerald City; later, the air above the landscape during flight.

**Characters:** 
- **Dorothy:** Uses the Golden Cap to summon help.
- **Scarecrow, Tin Woodman, Cowardly Lion, Toto:** Dorothy's companions, who become lost and discouraged in the fields.
- **Queen of the Mice:** Provides directions and explains the power of the Golden Cap.
- **The Winged Monkeys (including the Monkey King):** Magical creatures bound to obey the wearer of the Golden Cap.

**Events:**
- **Lost in the Fields:** After being carried away from the Wicked Witch's castle by Winged Monkeys, the travelers become lost in a massive field of flowers because they cannot maintain their direction without a road.
- **The Mice's Advice:** Desperate and exhausted, Dorothy uses her whistle to summon the Queen of the Mice. The Queen informs them that they have been walking in the wrong direction and suggests using the Golden Cap to command the Winged Monkeys for transport.
- **Summoning the Monkeys:** Dorothy reads the magic words inside the Golden Cap and performs a ritual involving standing on different feet. This summons the band of Winged Monkeys, who arrive to obey her command to fly them to the Emerald City.
- **The Legend of the Golden Cap:** During the flight, the Monkey King tells Dorothy the history of his people. He explains how they were once free until a prank played by his grandfather on the groom-to-be, Quelala, angered the sorceress Gayelette. As punishment, the monkeys were bound to obey the wearer of the Golden Cap three times.
- **Arrival:** The Winged Monkeys fly the group rapidly across the land, arriving at the gates of the Emerald City, successfully ending their period of being lost.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [scarlet_flower_fields](scarlet_flower_fields)
- [aerial_landscape_transit](aerial_landscape_transit)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: scarlet_flower_fields

[[SECTION markdown]]

# Scarlet Flower Fields

**Role:** Primary setting (lost/navigation phase).

**Architecture or Geography:** A vast, sprawling expanse of dense vegetation; characterized by massive fields of scarlet buttercups and yellow daisies. The terrain is repetitive and lacks distinct landmarks, contributing to the sense of being lost.

**Lighting and Atmosphere Cues:** Bright, saturated daylight; overwhelming floral colors; a sense of disorientation due to the sheer scale of the blooms.

**Scale Cues and Recurring Environmental Anchors:** Immense horizontal scale; endless rows of flowers; lack of visible roads or paths.

**Descriptive Noun Phrases:** Scarlet buttercup expanse, yellow daisy meadows, endless floral sea, saturated petal landscape, directionless flower fields.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: aerial_landscape_transit

[[SECTION markdown]]

# Aerial Landscape Transit

**Role:** Transit setting (flight phase).

**Architecture or Geography:** High-altitude perspective looking down upon the Oz landscape; a moving tapestry of diverse terrains passing beneath.

**Lighting and Atmosphere Cues:** Dynamic lighting shifts based on altitude; wind-swept atmosphere; sense of rapid movement and height.

**Scale Cues and Recurring Environmental Anchors:** Macro-scale geography; distant horizons; shrinking landmarks below.

**Descriptive Noun Phrases:** Aerial vista, sweeping landscape view, high-altitude flight path, panoramic Oz terrain, bird's-eye floral fields.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
