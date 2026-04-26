# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:07:42.459823+00:00
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

**Setting:** The palace and throne room of Zodanga; the subterranean dungeons of the palace.

**Characters:**
- **John Carter:** The protagonist, who infiltrates the palace to prevent a forced marriage.
- **Dejah Thoris:** Princess of Helium, who is being forced into a marriage ceremony with Sab Than.
- **Than Kosis:** The Jeddak of Zodanga, who presides over the wedding ceremony.
- **Sab Than:** Prince of Zodanga, the intended groom and antagonist.
- **Tars Tarkas:** Leader of the Tharks, who leads a cavalry charge into the city.
- **Kantos Kan:** An ally of Carter, rescued from the palace dungeons.

**Events:**
- **The Infiltration:** John Carter leads fifty Tharks, commanded by Tars Tarkas, through the gates of Zodanga and into the palace gardens.
- **The Wedding Interruption:** Inside the audience chamber, a ceremony is underway to bind Dejah Thoris to Sab Than with golden chains. Carter smashes through a window and leaps into the hall, shattering the ceremonial chain.
- **The Battle in the Throne Room:** A chaotic skirmish ensues between Carter, the Zodangan nobility/guards, and the Tharks. During the fight, Sab Than attempts to strike Dejah Thoris, but Carter kills him. Tars Tarkas arrives on the platform to assist, eventually leaving only the Tharks and Carter's party alive in the hall.
- **The Rescue:** Carter and a small group of warriors descend into the dungeons, where they locate and free Kantos Kan using keys taken from a fallen jailer.
- **The Declaration:** Amidst the ongoing sounds of war in the streets of Zodanga, Carter and Dejah Thoris are left alone in the throne room. Carter confesses his love and asks for her hand in marriage; Dejah Thoris accepts, and they pledge themselves to one another.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - CH025

- [zodanga_palace_throne_room](zodanga_palace_throne_room)
- [zodanga_palace_dungeons](zodanga_palace_dungeons)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_throne_room

[[SECTION markdown]]

# Zodanga Palace Throne Room

**Role:** Primary setting for the climax and romantic resolution.

**Architecture & Geography:** A grand, high-ceilinged audience chamber designed for ceremonial display. Features large windows overlooking the city/gardens and a raised platform for the Jeddak's throne. The space is characterized by ceremonial elements like golden chains used for binding.

**Lighting & Atmosphere:** High-stakes, chaotic atmosphere transitioning from ceremonial stillness to violent skirmish. Lighting is influenced by large window openings and the shifting shadows of combat.

**Scale & Anchors:** Massive scale; high ceilings and wide floor space capable of hosting a cavalry charge/skirmish. Key anchors include the central throne platform and the shattered ceremonial chains.

**Prompt Phrases:** Grand Zodangan audience chamber, high-ceilinged palace hall, ceremonial golden chains, raised dais, large panoramic windows, chaotic battleground, regal architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_dungeons

[[SECTION markdown]]

# Zodanga Palace Dungeons

**Role:** Secondary setting for the rescue sequence.

**Architecture & Geography:** Subterranean, enclosed stone chambers located beneath the main palace structure. Features heavy doors and jailer stations.

**Lighting & Atmosphere:** Dim, claustrophobic, and oppressive. Low-light environment focused on shadows and narrow corridors.

**Scale & Anchors:** Small to medium scale; cramped cells and narrow passageways. Key anchors include iron cell doors, heavy keys, and stone masonry.

**Prompt Phrases:** Subterranean dungeon, dark stone prison cells, claustrophobic corridors, dim torchlight, heavy iron gates, underground palace vaults.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
