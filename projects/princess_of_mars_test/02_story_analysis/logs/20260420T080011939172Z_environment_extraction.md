# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:00:11.940173+00:00
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

Chapter id: CH019

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

John Carter attempts to retrieve keys from his dead jailer but discovers they are gone, realizing Dejah Thoris and Sola have been taken by the Tharks to be devoured. He meets Kantos Kan, a fellow prisoner and Helium Navy Lieutenant, who shares details about the failed expedition and the ongoing search for the princess. Both are dragged to the Thark amphitheater for the arena games. Carter fights through various beasts and warriors, eventually facing Kantos Kan in the final match. They collude to escape; Carter pretends to die so Kan can claim freedom. Carter escapes into the hills east of the city while Kan leaves him there.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

## prison_jail_location
- Role: primary setting
- Architecture: stone jail/prison structure
- Lighting: dim, confined interior lighting
- Atmosphere: oppressive, deathly silence after Carter's discovery

## thark_amphitheater_arena
- Role: primary/transit setting
- Architecture: massive amphitheater with tiered seating
- Lighting: natural daylight during arena games
- Atmosphere: tense, violent, crowd-filled energy

## hills_east_city_escape
- Role: transit/escape setting
- Architecture: rugged hillside terrain
- Lighting: open sky, natural sunlight
- Atmosphere: freedom, isolation, post-confrontation relief

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: prison_jail_location



[[SECTION markdown]]

# Prison Jail Location

Short, grounded environment markdown.

## Environment Role
Primary setting where John Carter is held captive before the arena games.

## Architecture
Stone jail/prison structure with confined interior spaces and barred areas.

## Lighting
Dim, confined interior lighting creating shadows and oppressive atmosphere.

## Atmosphere
Deathly silence after Carter discovers his keys are gone; realization of Dejah Thoris and Sola's capture.

## Scale Cues
Small, enclosed spaces emphasizing vulnerability and confinement.

## Recurring Anchors
Jailer's cell, prison bars, confined corridors.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_amphitheater_arena



[[SECTION markdown]]

# Thark Amphitheater Arena

Short, grounded environment markdown.

## Environment Role
Primary/transit setting for the arena games and final confrontation.

## Architecture
Massive amphitheater with tiered seating surrounding a central fighting area.

## Lighting
Natural daylight during arena games; open-air structure allowing full visibility.

## Atmosphere
Tense, violent energy with crowd-filled atmosphere; anticipation of combat and escape.

## Scale Cues
Large-scale venue accommodating warriors, beasts, and spectators; epic confrontation space.

## Recurring Anchors
Central fighting pit, tiered spectator seating, arena entrance/exit points.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: hills_east_city_escape



[[SECTION markdown]]

# Hills East City Escape

Short, grounded environment markdown.

## Environment Role
Transit/escape setting where Carter leaves the city after colluding with Kantos Kan.

## Architecture
Rugged hillside terrain with natural pathways and open vistas away from urban structures.

## Lighting
Open sky with natural sunlight; unconfined lighting creating sense of freedom.

## Atmosphere
Freedom, isolation, post-confrontation relief; escape from the Thark city's violence.

## Scale Cues
Expansive landscape contrasting with confined prison and arena spaces; journey terrain.

## Recurring Anchors
Hillside paths, distant city skyline, natural elevation points.

[[/SECTION]]

[[FILMCREATOR_PACKET]]
````
