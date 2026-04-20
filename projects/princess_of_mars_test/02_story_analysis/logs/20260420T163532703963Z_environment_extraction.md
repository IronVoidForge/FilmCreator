# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:35:32.703963+00:00
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

**Setting:** A cave in the Arizona mountains; transitions from dawn to a moonlit night.

**Characters:**
* **The Narrator:** A man rendered paralyzed by an unknown vapor, who undergoes a supernatural metamorphosis.
* **Apache Warriors:** A group of scouts who approach the cave but flee in terror from an unseen horror within.

**Key Events:**
* **Paralysis:** The narrator finds himself unable to move due to a mysterious gas in a cave, watching helplessly as Apache warriors approach the ledge.
* **The Terror in the Cave:** A low, terrifying moan emanates from the depths of the cave, causing the Apache warriors to flee in a panic, leaving the narrator alone with his fear.
* **Metamorphosis:** After hours of paralysis, the narrator breaks free through intense mental willpower, only to discover a supernatural reality: he sees his own lifeless, naked body lying on the cave floor while he stands as a separate entity.
* **Escape and Cosmic Pull:** Lacking weapons and fearing the unseen presence in the cave, the narrator escapes into the Arizona night. While gazing at the red star of Mars, he feels an overwhelming, magnetic pull from the planet that suddenly transports him through the cold darkness of space.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

- [arizona_mountain_cave](#arizona_mountain_cave)
- [cosmic_void_mars_transit](#cosmic_void_mars_transit)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_mountain_cave

[[SECTION markdown]]

# Arizona Mountain Cave

**Role:** Primary setting.

**Architecture or Geography:** A rocky cave interior located within the Arizona mountains, featuring a prominent ledge and deep, unseen recesses that descend into darkness.

**Lighting and Atmosphere Cues:** Transitions from the soft light of dawn to a stark, moonlit night; characterized by a heavy, terrifying atmosphere and the presence of a mysterious, paralyzing vapor/gas.

**Scale Cues and Recurring Environmental Anchors:** A high mountain ledge overlooking the landscape; deep, cavernous shadows; jagged stone formations.

**Useful Descriptive Noun Phrases:** mist-shrouded cave interior, jagged rocky ledge, shadowy mountain depths, ethereal paralyzing vapor, dark cavernous recesses.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: cosmic_void_mars_transit

[[SECTION markdown]]

# Cosmic Void (Mars Transit)

**Role:** Transit setting.

**Architecture or Geography:** The infinite, cold vacuum of space; a transitionary void between Earth and Mars.

**Lighting and Atmosphere Cues:** Stark, freezing darkness; dominated by the luminous, magnetic glow of the red star (Mars); sense of overwhelming cosmic pull.

**Scale Cues and Recurring Environmental Anchors:** Vast interstellar scale; the distant, glowing orb of Mars acting as a gravitational/magnetic anchor.

**Useful Descriptive Noun Phrases:** infinite cosmic void, luminous red planet, stark interstellar darkness, magnetic celestial pull, freezing vacuum.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
