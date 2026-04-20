# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:39:54.671641+00:00
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

John Carter reflects on his love for Dejah Thoris as they prepare to travel from Korad to Thark. Dejah is chained by Sarkoja's order to ensure security during the journey. Tars Tarkas intervenes, taking custody of the key and promising to protect her from Sarkoja's harassment. During the march, John Carter engages in a duel with Zad, a warrior who struck his animal. The fight is interrupted when Dejah Thoris throws a mirror that blinds Zad, allowing him to strike John in the shoulder. Sarkoja attempts to stab Dejah Thoris, but Sola intercepts. The chapter culminates in a fierce sword fight where John Carter is stabbed in the chest and collapses, ending on a cliffhanger of his potential death or unconsciousness.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

## Korad City

Primary departure setting for John Carter and Dejah Thoris. Urban architecture with established city infrastructure. Lighting suggests daytime travel preparations. Scale indicates a significant settlement with populated streets and buildings.

## Thark City

Destination location for the journey. Barren, desert-based geography characteristic of Thark's environment. Atmospheric conditions reflect harsh desert climate. Scale suggests a major settlement with cultural significance to the inhabitants.

## March Route

Transit setting between Korad and Thark. Open terrain with minimal cover. Lighting varies across the journey path. Atmosphere includes dust and heat cues typical of desert travel. Scale indicates extended distance requiring significant travel time.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: korad_city_location



[[SECTION markdown]]

# Korad City Location

Primary departure setting for John Carter and Dejah Thoris. Urban architecture with established city infrastructure. Lighting suggests daytime travel preparations. Scale indicates a significant settlement with populated streets and buildings. Environment role: primary setting. Architecture: urban city structures. Lighting: daylight conditions. Atmosphere: settled, prepared for journey.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_location



[[SECTION markdown]]

# Thark City Location

Destination location for the journey. Barren, desert-based geography characteristic of Thark's environment. Atmospheric conditions reflect harsh desert climate. Scale suggests a major settlement with cultural significance to the inhabitants. Environment role: destination setting. Architecture: desert city structures. Lighting: bright daylight. Atmosphere: arid, culturally significant.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: march_route_location



[[SECTION markdown]]

# March Route Location

Transit setting between Korad and Thark. Open terrain with minimal cover. Lighting varies across the journey path. Atmosphere includes dust and heat cues typical of desert travel. Scale indicates extended distance requiring significant travel time. Environment role: transit setting. Architecture: open natural terrain. Lighting: variable daylight conditions. Atmosphere: dusty, hot, extended journey.

[[/SECTION]]



Asset id rules:

- lowercase snake_case
- stable across later reruns
- emit one explicit environment record per meaningful location or setting family
- every environment record must have a FILMCREATOR_RECORD wrapper with type environment
- include stable environment families rather than every one-off mention
- prefer visible geography and atmosphere over literary abstraction
````
