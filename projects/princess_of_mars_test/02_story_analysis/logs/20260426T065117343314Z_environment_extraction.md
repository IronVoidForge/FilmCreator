# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:51:17.343314+00:00
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

**Setting:** The Martian landscape during a march toward Thark; includes an incubator site for green Martian eggs and the open plains where a duel takes place.

**Characters:**
- **John Carter:** A human warrior struggling with his unrequited love for Dejah Thoris and his physical survival.
- **Dejah Thoris:** Princess of Helium, currently traveling under Thark custody; she is angry with Carter due to a perceived social insult.
- **Tars Tarkas:** A Thark chieftain who shows unexpected moments of restraint and empathy toward Carter and Dejah Thoris.
- **Sola:** A faithful companion to Dejah Thoris who risks her life to protect the princess.
- **Sarkoja:** A female Thark driven by intense hatred for John Carter; she orchestrates a distraction to ensure his death.
- **Zad:** A powerful green Martian warrior (*o mad*) who challenges Carter to a formal duel.

**Key Events:**
- **Emotional Conflict:** John Carter reflects on his love for Dejah Thoris, realizing the cultural and biological gulf between them, while Dejah Thoris remains cold toward him following an accidental social transgression.
- **The Journey Begins:** The group departs for Thark; Dejah Thoris is kept in chains by Sarkoja, though Tars Tarkas eventually intervenes to ensure her comfort and takes custody of the key.
- **Sabotage at the Incubator:** The party discovers and destroys a Warhoon incubator containing small green Martian eggs.
- **The Duel:** Zad challenges Carter to a formal duel with long-swords. During the fight, Sarkoja uses a mirror to flash sunlight into Carter's eyes, blinding him momentarily.
- **Chaos in the Chariot:** As the duel reaches its climax, Dejah Thoris confronts Sarkoja; Sola intercedes to protect the princess and is stabbed by Sarkoja.
- **The Climax:** Amidst the distraction, Zad delivers a fatal thrust to Carter's chest, leaving him on the brink of death.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [martian_plains_and_march_route](martian_plains_and_march_route)
- [warhoon_incubator_site](warhoon_incubator_site)
- [duel_arena_open_plains](duel_arena_open_plains)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plains_and_march_route

[[SECTION markdown]]

# Martian Plains and March Route

**Role:** Transit setting

**Geography:** Vast, undulating Martian plains characterized by rugged terrain and long-distance vistas. The route is a continuous stretch of alien landscape used for travel between major settlements.

**Lighting and Atmosphere:** Harsh, direct sunlight; thin atmosphere with high visibility; dusty and wind-swept.

**Scale Cues:** Expansive horizons; small silhouettes of travelers against massive geological features.

**Prompt Phrases:** vast martian plains, undulating red terrain, distant horizon, sweeping alien landscape, dust-swept vistas.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_incubator_site

[[SECTION markdown]]

# Warhoon Incubator Site

**Role:** Secondary setting

**Architecture/Geography:** A specialized facility or localized site designed for the incubation of green Martian eggs. Likely contains organic or mechanical structures suited for biological preservation.

**Lighting and Atmosphere:** Controlled, perhaps dim or humid; focused light on incubation vessels; sense of biological purpose and stillness.

**Scale Cues:** Clusters of small egg-vessels; intimate, enclosed feeling compared to the open plains.

**Prompt Phrases:** martian incubator facility, green egg clusters, biological preservation site, specialized incubation chambers, alien nursery.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: duel_arena_open_plains

[[SECTION markdown]]

# Duel Arena Open Plains

**Role:** Primary setting

**Geography:** A cleared or naturally flat area within the open plains, providing enough space for formal combat and chariot movement.

**Lighting and Atmosphere:** Intense, blinding sunlight; high-contrast shadows; sharp glare (noted by use of mirrors to flash light).

**Scale Cues:** Wide circular arena defined by the fighters' positions; large scale movement of chariots.

**Prompt Phrases:** sun-drenched duel ground, harsh martian sunlight, high-contrast desert lighting, wide combat clearing, blinding solar glare.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
