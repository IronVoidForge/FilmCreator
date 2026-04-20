# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:13:42.260589+00:00
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

Chapter id: CH022

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

Stationed to guard Jeddak Than Kosis in a heavily tapestried apartment, John Carter observes from a hidden passage as Dejah Thoris enters the chamber. To his devastation, he overhears her formally retract her preference for Tal Hajus and pledge herself to Sab Than, the Prince of Zodanga, in a political effort to prevent the conquest of Helium.

Believing this to be a mistake, Carter abandons his post and pursues her through the palace corridors. He is intercepted by four of Dejah Thoris's guards and kills them all in a violent skirmish to reach the Princess. When he finally confronts her, she is initially unable to recognize him due to his unfamiliar armor. Once identified, she is overcome with grief, explaining that she only made the promise because she believed Carter was dead and felt compelled to sacrifice her heart to save her people.

Dejah Thoris informs Carter that she is bound by Barsoomian custom to Sab Than; she explains a cultural misunderstanding where Carter, despite fighting for her, failed to formally ask for her hand in marriage as required by protocol. Despite his pleas, she maintains she cannot wed him if it requires the death of her husband.

As Carter attempts to navigate the labyrinthine palace of Zodanga to escape, he overhears guards discussing the butchered men in the antechamber. While hiding in a great hall, he listens to Than Kosis and the royal psychologist, Notan, discuss the mystery of a single man with extraordinary strength and skill. Realizing that increased patrols are hunting him, Carter waits for darkness before using his superior physical capabilities to leap from a balcony and escape the palace grounds.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index: CH022

| Asset ID | Description |
| :--- | :--- |
| zodanga_palace_interior | The labyrinthine, tapestried halls and chambers of the Zodangan royal palace. |
| zodanga_palace_grounds | The exterior perimeter and balconies overlooking the city/palace complex. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_interior

[[SECTION markdown]]

# Zodanga Palace Interior

**Role:** Primary setting

**Architecture & Geography:** A labyrinthine complex consisting of heavily tapestried apartments, formal chambers, narrow corridors, and great halls. Includes antechambers used for guard posts and hidden passages for observation.

**Lighting & Atmosphere:** Formal, heavy, and oppressive. The atmosphere is thick with political tension and the scent of old textiles. Lighting shifts from the dimness of hidden passages to the grander, more open illumination of royal halls.

**Scale & Anchors:** Large-scale royal chambers contrasted by claustrophobic corridors; recurring anchors include heavy tapestries, ornate doorways, and formal seating areas for royalty.

**Prompt Phrases:** heavily tapestried apartments, labyrinthine palace corridors, grand royal hall, ornate antechamber, dim hidden passages, Barsoomian royal architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_grounds

[[SECTION markdown]]

# Zodanga Palace Grounds

**Role:** Transit / Escape setting

**Architecture & Geography:** The exterior perimeter of the palace, featuring high balconies and vertical drops suitable for leaping.

**Lighting & Atmosphere:** Transitioning from twilight to darkness; shadows are deep and provide cover for movement. High-stakes, kinetic atmosphere.

**Scale & Anchors:** Vertical scale defined by balcony heights and the drop to the ground below; recurring anchors include stone railings and palace exterior walls.

**Prompt Phrases:** high palace balconies, dark exterior grounds, vertical architectural drops, moonlit Barsoomian architecture, shadows of the Zodanga palace.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
