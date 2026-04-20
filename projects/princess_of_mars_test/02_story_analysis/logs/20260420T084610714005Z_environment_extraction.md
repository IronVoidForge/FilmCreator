# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:46:10.714005+00:00
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

Chapter id: CH028

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

The narrator awakens in an Arizona cave after ten years on Mars, finding strange garments that disintegrate upon rising and artifacts including matches and green powder. Inside, he discovers a mummified woman and hanging skeletons before exiting to realize he is back on Earth. He reflects on his wealth from an old mine but expresses deep longing for Dejah Thoris and the fate of Helium. The chapter concludes with a vision of her waiting in the garden on Mars, suggesting a reunion.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

## Arizona Cave Location
Primary setting where narrator awakens after ten years on Mars. Features cave architecture, dim lighting, and atmospheric tension with mummified remains and hanging skeletons.

## Mars Garden Setting
Secondary/transit location referenced in vision sequence. Features garden geography, warm lighting, and reunion atmosphere associated with Dejah Thoris.

## Earth Surface Location
Transit setting where narrator realizes his return from Mars. Features open geography, natural lighting, and reflective atmosphere about wealth and longing.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_cave_location



[[SECTION markdown]]

# Arizona Cave Location

Primary setting for chapter action.

## Environment Role
Primary setting where narrator awakens after ten years on Mars.

## Architecture and Geography
Cave interior with natural rock formations, underground chamber space, and exit passage to surface.

## Lighting and Atmosphere
Dim, shadowed lighting with mysterious green powder glow. Atmospheric tension from disintegrating garments and mummified remains.

## Scale Cues
Underground cave scale with hanging skeletons as environmental anchors. Mummified woman provides human-scale reference point.

## Descriptive Noun Phrases
Arizona cave interior, underground chamber, rock formations, dim lighting, mysterious green powder, disintegrating garments, mummified remains, hanging skeletons, cave exit passage.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: mars_garden_setting



[[SECTION markdown]]

# Mars Garden Setting

Secondary/transit location referenced in vision sequence.

## Environment Role
Secondary setting referenced in narrator's vision of reunion with Dejah Thoris.

## Architecture and Geography
Garden geography on Mars surface, outdoor space with plant life and waiting position.

## Lighting and Atmosphere
Warm, hopeful lighting suggesting reunion atmosphere. Atmospheric connection to Helium fate and longing for Dejah Thoris.

## Scale Cues
Garden scale with waiting figure as environmental anchor. Outdoor space provides open-air reference point.

## Descriptive Noun Phrases
Mars garden, outdoor waiting position, plant life, warm lighting, hopeful atmosphere, reunion vision, Helium connection, Dejah Thoris waiting figure.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: earth_surface_location



[[SECTION markdown]]

# Earth Surface Location

Transit setting where narrator realizes his return from Mars.

## Environment Role
Transit location for narrator's realization of return to Earth after ten years on Mars.

## Architecture and Geography
Open surface geography, natural landscape with mine wealth context. Outdoor space providing transition between Mars memory and Earth reality.

## Lighting and Atmosphere
Natural daylight with reflective atmosphere about wealth from old mine. Atmospheric tension from longing for Dejah Thoris and fate of Helium.

## Scale Cues
Surface scale with open landscape as environmental anchor. Natural geography provides spatial reference point.

## Descriptive Noun Phrases
Earth surface, open landscape, natural daylight, mine wealth context, reflective atmosphere, old mine location, return realization, natural geography.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_PACKET]]
````
