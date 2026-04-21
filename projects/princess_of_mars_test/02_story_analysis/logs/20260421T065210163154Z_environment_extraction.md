# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:52:10.163154+00:00
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

**Events:**
The protagonist and his captor, Tars Tarkas, travel across a rising landscape toward a massive, deserted city situated on a table land. Upon entering the city, they find it inhabited by hundreds of Green Martians living in ruins that appear much older and more sophisticated than the current inhabitants. The party arrives at a magnificent marble edifice to meet with the local chieftain. After an introduction involving customary greetings, the protagonist is forced to perform for the assembled warriors. He initially struggles with movement, causing amusement among the Martians, but he earns their respect by striking a Martian who treated him roughly. The chapter concludes with a demonstration of "sak" (jumping), where the protagonist successfully performs a massive leap. Seeking food and water, he is led by a female Martian named Sola to a sleeping chamber, where he encounters a small, ten-legged creature resembling a frog-like pony.

**Characters:**
* **The Protagonist:** A human survivor, currently a prisoner, attempting to navigate Martian customs through observation and physical prowess.
* **Tars Tarkas:** A high-ranking Green Martian (vice-chieftain) who acts as the protagonist's escort and statesman.
* **The Chieftain:** The ruler of the local community, adorned in elaborate metal and feather ornaments.
* **Sola:** A young female Martian of Tars Tarkas's retinue; she is light olive-green and serves as the protagonist's guide to his quarters.
* **The Warriors/Martians:** A violent, highly physical race characterized by their tusks, varying heights (10-12 feet for females), and a culture that finds humor in death and struggle.

**Settings:**
* **The Deserted City:** An enormous, ancient city on a table land featuring ruins of a much older, more advanced civilization.
* **The Audience Chamber:** A massive marble building inlaid with gold and jewels, containing human-sized furniture that is incongruously small for the large Martians.
* **The Plaza:** A central open area used for public demonstrations and gatherings.
* **Sola's Quarters:** A spacious, well-lit room decorated with murals and mosaics, filled with silks and furs.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [ancient_tableland_city](ancient_tableland_city)
- [marble_audience_chamber](marble_audience_chamber)
- [martian_sleeping_quarters](martian_sleeping_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_tableland_city

[[SECTION markdown]]

# Ancient Tableland City

**Role:** Primary / Transit Setting

**Geography:** An enormous, sprawling city situated atop a massive table land. The landscape is characterized by rising terrain and vast, deserted expanses of ruins.

**Architecture:** Features remnants of an ancient, highly sophisticated civilization. The structures are much older and more advanced than the current Martian inhabitants, suggesting a lost era of grand design.

**Lighting & Atmosphere:** Open-air vistas; sense of immense scale and historical decay; dusty, sun-bleached ruins under a Martian sky.

**Scale Cues:** Massive city footprints; vast distances between structures; wide plazas for public gatherings.

**Prompt Phrases:** ancient ruined metropolis, table land plateau, sprawling desert ruins, advanced prehistoric architecture, massive stone vistas, desolate urban landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: marble_audience_chamber

[[SECTION markdown]]

# Marble Audience Chamber

**Role:** Primary Setting

**Architecture:** A magnificent, grand edifice constructed of polished marble. The interior is heavily inlaid with gold and precious jewels. 

**Lighting & Atmosphere:** Opulent and imposing; high-contrast lighting from jewel reflections; sense of ceremonial gravity and power.

**Scale Cues:** Massive scale designed for 10-12 foot inhabitants; human-sized furniture appears incongruously small within the vast hall.

**Prompt Phrases:** grand marble palace, gold inlaid walls, jeweled architecture, monumental hall, opulent chieftain throne room, oversized interior scale.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_sleeping_quarters

[[SECTION markdown]]

# Martian Sleeping Quarters

**Role:** Secondary Setting

**Architecture:** Spacious, well-lit residential chambers. The walls are decorated with intricate murals and mosaics.

**Lighting & Atmosphere:** Bright and airy; soft textures; sense of domestic comfort amidst a harsh world.

**Scale Cues:** Large rooms filled with luxurious textiles.

**Prompt Phrases:** mural-decorated chamber, mosaic walls, silk and fur furnishings, spacious Martian bedroom, bright interior, textured stone walls.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
