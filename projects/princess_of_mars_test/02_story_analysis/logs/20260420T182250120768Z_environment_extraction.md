# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:22:50.120768+00:00
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

Chapter id: CH025

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

**Setting:** The palace of Zodanga, specifically the brilliantly illuminated audience chamber and the labyrinthine dungeons beneath.

**Characters:**
* **John Carter:** The protagonist, who infiltrates the palace to prevent a forced marriage.
* **Dejah Thoris:** Princess of Helium, who is being held for a political marriage ceremony.
* **Than Kosis:** The Jeddak of Zodanga.
* **Sab Than:** The Prince of Zodanga, son of Than Kosis.
* **Tars Tarkas:** Leader of the Thark warriors, providing military support.
* **Kantos Kan:** An ally of Carter, rescued from the Zodangan dungeons.

**Events:**
* **The Infiltration:** John Carter and fifty Tharks led by Tars Tarkas breach the gates of Zodanga and enter the palace gardens.
* **The Ceremony Interrupted:** Inside the audience chamber, Than Kosis is conducting a ceremony to bind Dejah Thoris to Sab Than with golden chains. Carter shatters the chamber window and leaps into the hall, breaking the ceremonial chain.
* **The Battle in the Throne Room:** A chaotic skirmish ensues between Carter, the Zodangan nobility/guards, and the Tharks. During the fight, Sab Than is killed, as is his father, Than Kosis. Tars Tarkas eventually clears the room of opposition.
* **The Rescue:** Carter leads a search of the dungeons, successfully locating and freeing Kantos Kan using keys taken from a fallen jailer.
* **The Engagement:** Amidst the ongoing sounds of war in the streets of Zodanga, Carter and Dejah Thoris find a moment of peace. They profess their love for one another and formally promise themselves in marriage.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH025

- [zodanga_palace_audience_chamber](zodanga_palace_audience_chamber)
- [zodanga_palace_dungeons](zodanga_palace_dungeons)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_audience_chamber

[[SECTION markdown]]

# Zodanga Palace Audience Chamber

**Role:** Primary setting (climax/ceremony).

**Architecture & Geography:** A grand, high-ceilinged ceremonial hall designed for political spectacle. Features large windows capable of being breached from the exterior and a central area designated for ritualistic binding.

**Lighting & Atmosphere:** Brilliantly illuminated; high-contrast lighting suitable for dramatic ceremonies. The atmosphere shifts rapidly from ceremonial stillness to chaotic combat.

**Scale & Anchors:** Large-scale imperial architecture; recurring anchors include the ceremonial golden chains and the large glass windows/apertures.

**Prompt Phrases:** Grand Zodangan audience chamber, brilliant ceremonial illumination, high-ceilinged palace hall, shattered glass fragments, golden ritual chains, imperial scale, chaotic skirmish setting.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_dungeons

[[SECTION markdown]]

# Zodanga Palace Dungeons

**Role:** Secondary setting (rescue/infiltration).

**Architecture & Geography:** A labyrinthine subterranean complex located beneath the palace. Characterized by narrow corridors, cells, and heavy ironwork.

**Lighting & Atmosphere:** Dim, claustrophobic, and oppressive. Low-light environment with shadows cast by torchlight or minimal light shafts.

**Scale & Anchors:** Tight, enclosed spaces; recurring anchors include cell bars, heavy jailer keys, and stone masonry.

**Prompt Phrases:** Labyrinthine subterranean dungeons, dark stone corridors, cramped prison cells, dim torchlight, oppressive atmosphere, heavy iron gates, Zodangan dungeon architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
