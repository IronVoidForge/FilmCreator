# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:45:02.494798+00:00
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

Chapter id: CH027

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

This chapter depicts the transition from celebration to catastrophe in Helium. Following a peace treaty with Thark led by Tars Tarkas and Sola, preparations are underway for the wedding of Dejah Thoris and John Carter, symbolized by an incubated egg. However, news arrives that the atmosphere plant's keeper has been assassinated and the engine has stopped, causing air pressure to drop rapidly across Barsoom. The people of Helium face imminent asphyxiation and death within three days. Despite their bravery, Dejah Thoris and John Carter succumb to the thinning air in the palace garden. As they die, John Carter remembers a series of nine thought waves from his past life on Earth, which unlock the secret to the atmosphere plant's doors. He launches an air-scout machine to the plant, opens the three great doors, and collapses, leaving hope for Barsoom's survival.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - Helium Chapter

## Primary Settings

- **helium_palace_garden**: Main wedding preparation and death scene location within the palace grounds
- **atmosphere_plant**: Critical Barsoom facility housing the atmospheric engine with three great doors

## Secondary/Transit Settings

- **helium_city_streets**: General Helium urban environment for movement between locations

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: helium_palace_garden



[[SECTION markdown]]

# Helium Palace Garden

Primary setting for wedding preparations and death scene.

## Architecture & Geography

Palace grounds with elevated garden terraces overlooking the city of Helium. Ornate Barsoomian architecture with stone pathways, decorative fountains, and palace walls enclosing the space.

## Lighting & Atmosphere

Golden hour lighting during wedding preparations, transitioning to dimming light as air pressure drops. Thin, ethereal atmosphere with visible dust particles in the thinning air.

## Scale & Anchors

Large open garden space with palace structures as visual anchors. Wedding decorations including banners and ceremonial seating define the scale. The incubated egg serves as a central symbolic anchor.

## Descriptive Noun Phrases

Palace garden terrace, Barsoomian stone pathways, wedding ceremony decorations, thinning air visibility, ornate palace walls, elevated garden grounds, ceremonial seating area, decorative fountains, golden hour lighting.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: atmosphere_plant



[[SECTION markdown]]

# Atmosphere Plant

Critical Barsoom facility housing the atmospheric engine with three great doors.

## Architecture & Geography

Industrial-scale facility with massive reinforced doors and atmospheric containment structures. Three great doors leading to the core atmospheric engine room. Heavy metal construction with Barsoomian engineering aesthetics.

## Lighting & Atmosphere

Dim industrial lighting with emergency system indicators. Atmospheric pressure gauges visible on walls. Emergency air-scout machine launch area with bright activation lights.

## Scale & Anchors

Massive three-door entrance structure as primary visual anchor. Atmospheric engine core visible through central doorway. Air-scout machine serves as secondary anchor during launch sequence.

## Descriptive Noun Phrases

Three great doors, atmospheric engine core, industrial containment structures, emergency system indicators, air-scout machine launch area, reinforced metal construction, Barsoomian engineering aesthetics, pressure gauge displays, massive door entrance.

[[/SECTION]]



Asset id rules:

- lowercase snake_case
- stable across later reruns
- emit one explicit environment record per meaningful location or setting family
- every environment record must have a FILMCREATOR_RECORD wrapper with type environment
- keep the environment set small and useful
- use concise visible descriptions
````
