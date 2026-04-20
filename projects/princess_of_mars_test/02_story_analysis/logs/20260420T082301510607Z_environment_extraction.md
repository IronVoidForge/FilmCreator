# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:23:01.511607+00:00
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

Chapter id: CH025

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

Chapter XXV: The Looting of Zodanga. John Carter leads fifty Tharks into the impregnable palace of Zodanga to interrupt a state ceremony where Prince Sab Than is to marry Princess Dejah Thoris. Inside the throne room, Carter shatters the window and attacks the assembly, killing Than Kosis and then Sab Than while defending Dejah Thoris from the guards. With Tars Tarkas's help, they clear the hall. Carter secures Kantos Kan from the dungeons and finds him in a dark recess. After searching for keys to release Kantos Kan, they regroup with Dejah Thoris. In the throne room, amidst the chaos of war outside, Dejah Thoris promises herself to John Carter in marriage.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Zodanga Palace Environment Index

- **zodanga_palace_throne_room** - Primary setting, grand architecture, ceremonial lighting, palace atmosphere
- **dungeons** - Secondary setting, dark confined spaces, subterranean lighting, prison atmosphere
- **dark_recess** - Transit/finding location, mysterious shadows, minimal lighting, hidden space

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_throne_room



[[SECTION markdown]]

# Zodanga Palace Throne Room

Primary setting for the state ceremony and battle. Grand palace architecture with towering columns and ornate decorations. Ceremonial lighting from chandeliers and torches creates dramatic shadows across marble floors. Opulent atmosphere with royal banners, throne seating, and assembled guards. Large scale space accommodating fifty Tharks and palace assembly. Throne room windows overlooking the palace exterior provide natural light sources during daylight hours.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: dungeons



[[SECTION markdown]]

# Dungeons

Secondary setting where Kantos Kan is held prisoner. Dark confined subterranean spaces with stone walls and minimal openings. Subdued lighting from torches or natural seepage creates oppressive shadows. Prison atmosphere with chains, bars, and restricted movement. Small scale cells within larger underground complex. Underground architecture beneath the palace throne room provides depth to the setting.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: dark_recess



[[SECTION markdown]]

# Dark Recess

Transit/finding location where keys are discovered. Mysterious shadowed space with minimal natural light sources. Atmospheric darkness punctuated by occasional torch or candlelight. Hidden architectural feature within the palace complex. Small scale confined area that serves as a transitional space between main locations. Subterranean or basement-level positioning beneath throne room provides depth to palace architecture.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_exterior



[[SECTION markdown]]

# Zodanga Palace Exterior

Transit setting for approach and departure from palace grounds. Grand palace silhouette against sky with multiple towers and spires. Natural daylight lighting creates clear visibility of architectural features. Open atmosphere with palace grounds, pathways, and surrounding landscape. Large scale structure dominating the Zodanga cityscape. Palace exterior provides geographical anchor for the battle sequence outside throne room windows.

[[/SECTION]]



[[FILMCREATOR_PACKET]]
````
