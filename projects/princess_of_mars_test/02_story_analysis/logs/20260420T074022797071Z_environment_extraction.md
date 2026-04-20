# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:40:22.797071+00:00
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

- keep the environment set small and useful

- use concise visible descriptions



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

## korad_city

Primary starting location where John Carter and Dejah Thoris prepare to travel. Features urban architecture with city defenses, atmospheric lighting suggesting anticipation of journey ahead. Scale includes city walls and gates as environmental anchors.

## march_route

Transit setting between Korad and Thark. Open terrain geography with natural landscape features, variable lighting conditions during the march, atmospheric cues indicating distance and journey progression. Scale includes horizon lines and path markers as recurring anchors.

## thark_city

Destination primary location in Barsoom. Urban architecture with distinctive city structures, atmospheric lighting reflecting cultural significance, scale includes major gates and central areas as environmental anchors.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: korad_city



[[SECTION markdown]]

# Korad City

Primary starting location where John Carter and Dejah Thoris prepare to travel from Korad to Thark. Urban architecture with city defenses and gates, atmospheric lighting suggesting anticipation of journey ahead. Scale includes city walls and gates as environmental anchors. Features urban structures with defensive elements, variable lighting conditions indicating time of day during preparations.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: march_route



[[SECTION markdown]]

# March Route

Transit setting between Korad and Thark during the journey. Open terrain geography with natural landscape features, variable lighting conditions during the march, atmospheric cues indicating distance and journey progression. Scale includes horizon lines and path markers as recurring anchors. Features open wilderness with directional elements, changing light patterns reflecting travel duration and environmental exposure.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city



[[SECTION markdown]]

# Thark City

Destination primary location in Barsoom where the journey concludes. Urban architecture with distinctive city structures and gates, atmospheric lighting reflecting cultural significance of arrival point. Scale includes major gates and central areas as environmental anchors. Features urban defensive structures with cultural elements, variable lighting indicating ceremonial or significant moments during arrival.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: battlefield_arena



[[SECTION markdown]]

# Battlefield Arena

Secondary combat setting where John Carter engages in sword fight with Zad and Sarkoja. Open arena geography with fighting space, dramatic lighting emphasizing combat intensity, atmospheric cues indicating tension and danger. Scale includes weapon range and movement zones as environmental anchors. Features open combat space with directional elements, variable lighting reflecting fight progression and character positioning during duel sequences.

[[/SECTION]]



[[FILMCREATOR_PACKET]]
````
