# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:52:49.121375+00:00
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

Chapter id: CH004

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

The narrator and Tars Tarkas arrive at a massive, ancient city situated on a table land near a dried sea. The city is populated by hundreds of Green Martians, a violent race characterized by their large size, tusks, and lack of clothing. Upon entering the central plaza, the group meets with the local Chieftain in a magnificent marble hall that appears to have been built by a much older, more advanced race. During an audience, the narrator demonstrates his physical strength through "sak" (jumping) and earns the respect of the warriors by punching a Martian who treated him roughly. Seeking food and water, the narrator is led away by Sola, a female Martian in Tars Tarkas's retinue, to a decorated sleeping chamber where he encounters a strange, ten-legged creature.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [ancient_city_plateau](#ancient_city_plateau)
- [marble_audience_hall](#marble_audience_hall)
- [martian_sleeping_chambers](#martian_sleeping_chambers)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_city_plateau

[[SECTION markdown]]

# Ancient City Plateau

**Role:** Primary setting / Transit setting

**Geography:** A massive, elevated table land situated near the expanse of a dried sea bed. The terrain is characterized by high-altitude plateaus and vast, arid basins.

**Lighting and Atmosphere:** Harsh, bright light typical of an open plateau; ancient and imposing atmosphere.

**Scale Cues:** Massive urban sprawl; large-scale geological features including the nearby dried sea.

**Prompt Phrases:** massive ancient city, elevated table land, dried sea basin, high plateau landscape, ancient Martian architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: marble_audience_hall

[[SECTION markdown]]

# Marble Audience Hall

**Role:** Secondary setting / Primary interaction site

**Architecture:** A magnificent hall constructed from polished marble. The architecture is distinct from the current inhabitants, appearing to be built by a much older, more technologically or aesthetically advanced race.

**Lighting and Atmosphere:** Grand, regal, and imposing; sense of historical weight and architectural sophistication.

**Scale Cues:** Large-scale ceremonial chamber; high ceilings and wide floor space for gatherings.

**Prompt Phrases:** magnificent marble hall, ancient advanced architecture, grand audience chamber, polished marble interior, prehistoric monumental hall.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_sleeping_chambers

[[SECTION markdown]]

# Martian Sleeping Chambers

**Role:** Secondary setting / Interior habitat

**Architecture:** Decorated residential chambers within the city; interior spaces designed for rest and habitation.

**Lighting and Atmosphere:** Intimate, decorated, and slightly alien/strange due to the presence of unusual fauna (ten-legged creatures).

**Scale Cues:** Humanoid/Martian scale; enclosed, private room dimensions.

**Prompt Phrases:** decorated sleeping chamber, Martian residential interior, ornate living quarters, strange creature habitat.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
