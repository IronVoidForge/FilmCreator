# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:26:54.278081+00:00
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

**Setting:** The palace of Zodanga, specifically the brilliantly illuminated audience chamber and the labyrinthine dungeons beneath.

**Characters:**
- **John Carter:** The protagonist, who infiltrates the palace to rescue Dejah Thoris.
- **Dejah Thoris:** Princess of Helium, who is being forced into a political marriage.
- **Than Kosis:** The Jeddak of Zodanga.
- **Sab Than:** Son of Than Kosis and the Prince of Zodanga.
- **Tars Tarkas:** Leader of the Tharks, providing military support to Carter.
- **Kantos Kan:** An ally of Carter, rescued from the Zodangan dungeons.

**Events:**
- **The Infiltration:** John Carter leads fifty Tharks into Zodanga. He infiltrates the palace alone by shattering a window and leaping into the audience chamber during a marriage ceremony.
- **The Ceremony Interrupted:** Carter interrupts the wedding of Sab Than and Dejah Thoris, destroying the golden ceremonial chain intended to bind her. 
- **The Battle in the Throne Room:** A chaotic skirmish ensues between Carter, the Zodangan nobility/guards, and the advancing Tharks led by Tars Tarkas. During the fight, Sab Than is killed, as is his father, Than Kosis. The Tharks eventually secure the hall, leaving only themselves, Carter, and Dejah Thoris alive.
- **The Rescue:** Carter descends into the dungeons to rescue Kantos Kan, finding him in a dark recess and freeing him using keys taken from a fallen jailer.
- **The Engagement:** Amidst the ongoing sounds of war and looting throughout Zodanga, John Carter and Dejah Thoris share a moment of intimacy in the throne room, where they officially pledge themselves to marriage.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index: CH025

- [zodanga_audience_chamber](zodanga_audience_chamber)
- [zodanga_dungeons](zodanga_dungeons)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_audience_chamber

[[SECTION markdown]]

# Zodanga Audience Chamber

**Role:** Primary setting (Ceremony and Battle).

**Architecture & Geography:** A grand, high-ceilinged throne room designed for political spectacle. Features a central area for ceremonial rites, including platforms or altars for binding ceremonies. The space is large enough to accommodate both nobility and an advancing military force of Tharks.

**Lighting & Atmosphere:** Brilliantly illuminated; high-key lighting intended to showcase wealth and power. Atmospheric shifts from ceremonial splendor to chaotic combat dust and smoke.

**Scale & Anchors:** Massive scale; high windows (one of which is shattered); central ceremonial dais; presence of a throne/seat of power for the Jeddak.

**Prompt Phrases:** Grand Zodangan palace hall, brilliantly lit audience chamber, shattered high windows, golden ceremonial chains, chaotic battleground, high-ceilinged marble architecture, opulent political ceremony setting.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_dungeons

[[SECTION markdown]]

# Zodanga Dungeons

**Role:** Secondary setting (Rescue mission).

**Architecture & Geography:** A labyrinthine subterranean complex located beneath the palace. Consists of narrow corridors, dark recesses, and individual cells.

**Lighting & Atmosphere:** Dark, oppressive, and shadowy; low-key lighting with minimal visibility in recessed areas. Heavy, claustrophobic atmosphere.

**Scale & Anchors:** Human-scale/tight scale; stone walls; iron bars or cell doors; heavy jailer keys; dark alcoves.

**Prompt Phrases:** Labyrinthine subterranean dungeons, dark stone recesses, oppressive prison cells, dim torchlight shadows, narrow stone corridors, Zodangan underworld architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
