# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:51:37.215085+00:00
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

Chapter id: CH002

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

**Setting:** A cave in the Arizona mountains; a rocky gorge and canyon under moonlight; the vastness of space.

**Characters:**
- **The Protagonist:** A man who experiences physical paralysis due to a mysterious gas, undergoes a supernatural metamorphosis, and is eventually pulled toward Mars.
- **Apache Warriors:** A group of braves who approach the cave but flee in terror from an unseen moaning sound emanating from the cave's depths.
- **The Dead Friend:** The protagonist's companion, whose body lies near the cave entrance.

**Events:**
- **Paralysis:** The protagonist is rendered immobile by a pungent, tenuous vapor within the cave, leaving him conscious but unable to move.
- **The Apache Encounter:** A group of Apache warriors discovers the protagonist; however, they are terrified by a low moaning sound from the back of the cave and flee in a panic, causing one warrior to fall to his death.
- **Metamorphosis:** After hours of isolation, the protagonist exerts a massive mental effort to break his paralysis. Upon succeeding, he discovers he has undergone a strange transformation: he is standing naked, while his physical body remains lying on the cave floor, clothed and seemingly lifeless.
- **The Escape:** Fearing an unseen presence in the dark cave, the protagonist flees into the Arizona night.
- **The Call of Mars:** While observing the landscape, the protagonist becomes mesmerized by a large red star (Mars). He feels an irresistible pull toward the planet, closes his eyes, and is suddenly transported through space into darkness and cold.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

| Asset ID | Description |
| :--- | :--- |
| arizona_mountain_cave | A dark, gas-filled cave in the Arizona mountains. |
| rocky_gorge_canyon | A moonlit canyon landscape under the night sky. |
| deep_space_void | The vast, cold expanse of space during transit. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_mountain_cave

[[SECTION markdown]]

# Arizona Mountain Cave

**Role:** Primary setting (metamorphosis site)

**Architecture/Geography:** A subterranean cave system located within the Arizona mountains; features a cave entrance and deep, dark recesses.

**Lighting/Atmosphere:** Dimly lit, heavy with a pungent, tenuous vapor; oppressive darkness in the depths; presence of an unseen, moaning sound.

**Scale/Anchors:** Narrow passages transitioning to larger chambers; floor space occupied by a lifeless physical body.

**Prompt Phrases:** dark mountain cave, pungent gas vapor, subterranean chamber, shadowy recesses, claustrophobic stone walls.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: rocky_gorge_canyon

[[SECTION markdown]]

# Rocky Gorge Canyon

**Role:** Secondary setting (escape and observation)

**Architecture/Geography:** A rugged canyon and rocky gorge landscape under the night sky.

**Lighting/Atmosphere:** Moonlit, vast open air, nocturnal Arizona desert atmosphere.

**Scale/Anchors:** Expansive vistas; high cliffs overlooking the gorge; visible red star (Mars) in the zenith.

**Prompt Phrases:** moonlit canyon, rocky gorge, Arizona night landscape, vast desert vista, starry night sky, glowing red planet Mars.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: deep_space_void

[[SECTION markdown]]

# Deep Space Void

**Role:** Transit setting (metaphysical transport)

**Architecture/Geography:** The infinite expanse of the cosmos.

**Lighting/Atmosphere:** Absolute darkness, extreme cold, vacuum, sense of weightlessness and isolation.

**Scale/Anchors:** Infinite scale; absence of terrestrial landmarks.

**Prompt Phrases:** deep space void, cosmic darkness, interstellar vacuum, freezing celestial expanse, starless abyss.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
