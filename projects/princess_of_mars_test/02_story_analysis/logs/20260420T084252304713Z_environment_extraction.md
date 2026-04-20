# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:42:52.304713+00:00
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

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



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

````
