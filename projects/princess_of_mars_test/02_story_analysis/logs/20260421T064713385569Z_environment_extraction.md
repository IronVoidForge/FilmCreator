# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:47:13.385569+00:00
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

**Setting:** A cave on a narrow cliff ledge in the Arizona mountains; later, the vast expanse of space.

**Characters:**
- **The Protagonist:** An experienced fighter who becomes paralyzed by a mysterious gas in a cave, only to undergo a supernatural transformation.
- **Apache Warriors:** A group of braves who approach the cave but flee in terror from an unseen moaning sound emanating from the cave's depths.
- **The Protagonist's Former Self:** A lifeless, clothed body left behind in the cave after the protagonist's consciousness/spirit separates and manifests as a naked entity.

**Events:**
- The protagonist is paralyzed by a pungent, tenuous vapor within a cave, rendering him unable to move despite remaining mentally alert.
- A group of Apache warriors approaches the cave; they are struck with awe and terror upon seeing the protagonist, but flee in panic when they hear a low moaning sound from the back of the cave.
- The protagonist's horse wanders off down the trail, leaving him isolated.
- At midnight, after hearing more mysterious sounds and rustling from the darkness, the protagonist exerts immense mental will to break his paralysis.
- Upon breaking free, the protagonist discovers he has undergone a metamorphosis: he is standing naked while his original, clothed body lies lifeless on the cave floor.
- Fearing the unseen entity in the shadows, the protagonist escapes the cave into the Arizona night.
- While gazing at the landscape and the red star of Mars, the protagonist feels an irresistible, magnetic pull toward the planet.
- The chapter concludes with the protagonist being violently drawn through the void of space.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [arizona_mountain_cave_ledge](arizona_mountain_cave_ledge)
- [vast_cosmic_void](vast_cosmic_void)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_mountain_cave_ledge

[[SECTION markdown]]

# Arizona Mountain Cave Ledge

**Role:** Primary setting (transformation site).

**Architecture/Geography:** A narrow, precarious cliff ledge situated within the rugged Arizona mountains. Features a cave mouth leading into dark, deep recesses containing pungent, tenuous vapors and unseen shadows.

**Lighting/Atmosphere:** Dimly lit by moonlight; heavy with thick, mysterious gas/vapor; oppressive darkness in the cave interior; transition from night-time mountain air to an eerie, supernatural stillness.

**Scale/Anchors:** Narrow trail, steep drop-offs, rocky cave floor, deep cavernous depths.

**Prompt Phrases:** narrow cliff ledge, rugged Arizona mountains, dark cave mouth, pungent vapor, moonlight on rock, deep shadows, precarious mountain path.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: vast_cosmic_void

[[SECTION markdown]]

# Vast Cosmic Void

**Role:** Transit setting (interstellar travel).

**Architecture/Geography:** The infinite expanse of space; a vacuum between Earth and Mars.

**Lighting/Atmosphere:** Absolute darkness punctuated by distant stars; the glowing red presence of Mars; high-contrast celestial lighting; sense of violent, magnetic motion through a vacuum.

**Scale/Anchors:** Infinite scale; the singular red point of Mars; the void of the cosmos.

**Prompt Phrases:** vast cosmic expanse, deep space void, glowing red planet Mars, starlight in darkness, interstellar vacuum, celestial transit.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
