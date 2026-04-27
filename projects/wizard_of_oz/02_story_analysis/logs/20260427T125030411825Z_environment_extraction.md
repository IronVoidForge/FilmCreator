# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T12:50:30.411825+00:00
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
Project slug: wizard_of_oz

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

[[SECTION
Dorothy returns to her farm in Kansas, running toward Aunt Em. Upon seeing her, Aunt Em is shocked and embraces her. Dorothy informs her aunt that she has returned from the Land of Oz, accompanied by Toto, expressing her profound relief at being home.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [kansas_farmstead](kansas_farmstead)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: kansas_farmstead

[[SECTION markdown]]

# Kansas Farmstead

**Role:** Primary setting

**Architecture & Geography:** A rural, grounded farmstead featuring a modest farmhouse and surrounding agricultural land. The landscape is characterized by the flat, expansive plains of Kansas.

**Lighting & Atmosphere:** Naturalistic, bright daylight; sense of relief and domestic warmth.

**Scale & Anchors:** Human-scale architecture; anchored by the farmhouse entrance and the immediate proximity to Aunt Em.

**Descriptive Noun Phrases:** dusty farmyard, rustic farmhouse, wide Kansas plains, sun-drenched homestead, rural prairie landscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
