# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:21:29.664560+00:00
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

Chapter id: CH024

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

In Chapter XXIV, John Carter crashes his craft into a fierce battle between Tharks and Warhoons on ancient Mars. He saves Tars Tarkas from death by Warhoons, earning the green warrior's respect and friendship. Woola, the dog, also returns to Thark. Tars Tarkas brings John Carter before Jeddak Tal Hajus, who seeks revenge for a previous injury. During a council meeting, John Carter exposes Tal Hajus as a coward unfit to rule. The Thark council votes to challenge Tal Hajus to combat with Tars Tarkas. Tars Tarkas wins and becomes the new Jeddak of Thark. He is made a chieftain and proposes an alliance with Helium to rescue Dejah Thoris from Zodanga. The Tharks agree, gathering a massive force of 150,000 warriors. They march on Zodanga and enter the city through a gate constructed by John Carter using his men as steps.
````

## Raw Response
````text

````
