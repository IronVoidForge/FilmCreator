# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:57:03.006388+00:00
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

Chapter id: CH018

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

**Setting:**
The chapter moves from a small room within a Warhoon camp to the open Martian plains during a military march, and finally to a pitch-black, subterranean dungeon within the city of Warhoon.

**Characters:**
* **Protagonist:** A human captive who survives severe injuries through mysterious medical treatments but suffers extreme psychological trauma due to isolation and darkness.
* **Dak Kova:** A scarred, ferocious Warhoon warrior/jed; an insubordinate lieutenant who eventually murders his leader to become the new Jeddak.
* **Bar Comas:** The young, dignified Jeddak of the Warhoons who is killed in a primal duel with Dak Kova.
* **The Female Healer:** An ancient, ugly Warhoon woman who treats the protagonist's wounds.
* **Warhoon Warriors/Jailer:** A bloodthirsty horde characterized by their use of human skulls and hands as ornamentation; includes the silent jailer killed by the protagonist.

**Key Events:**
* **Recovery and Transport:** The protagonist regains consciousness, healed by a Warhoon female, and is strapped to a wild thoat to be transported to the main Warhoon column.
* **The Duel of the Jeddaks:** Dak Kova openly defies Bar Comas, leading to a savage, animalistic hand-to-hand combat between the two leaders. Dak Kova kills Bar Comas with a tusk thrust and seizes power.
* **The March to Warhoon:** The Warhoon horde, numbering ten thousand, retreats toward their city after the duel delays their raid on the Tharks.
* **Imprisonment:** The protagonist is cast into a dark dungeon in Warhoon, where he endures weeks or months of sensory deprivation and terror from unseen creatures.
* **The Escape Attempt:** Driven to near-madness, the protagonist ambushes his food deliverer with a heavy chain, killing him. He recovers his senses upon finding the jailer's keys but is immediately confronted by the glowing eyes of unseen entities in the darkness.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [warhoon_camp_interior](warhoon_camp_interior)
- [martian_plains_march_route](martian_plains_march_route)
- [warhoon_subterranean_dungeon](warhoon_subterranean_dungeon)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_camp_interior

[[SECTION markdown]]

# Warhoon Camp Interior

**Role:** Secondary setting (recovery site).

**Architecture/Geography:** Small, cramped interior room within a mobile or semi-permanent Warhoon camp structure.

**Lighting and Atmosphere:** Dim, claustrophobic, smelling of medicinal herbs and old blood; localized lighting from primitive sources.

**Scale Cues:** Human-scale, confined, intimate but threatening.

**Prompt Phrases:** Cramped warhoon tent interior, dim medicinal lighting, primitive camp dwelling, enclosed space, gritty survivalist atmosphere.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plains_march_route

[[SECTION markdown]]

# Martian Plains March Route

**Role:** Transit setting (military movement).

**Architecture/Geography:** Vast, open Martian plains; dusty terrain suitable for large-scale troop movements and thoat riding.

**Lighting and Atmosphere:** Harsh, wide-angle sunlight; sweeping vistas of red dust and rocky outcrops; high visibility with wind-swept grit.

**Scale Cues:** Massive scale; ten thousand warriors moving across a horizon; vast emptiness contrasted by the dense column of movement.

**Prompt Phrases:** Vast Martian plains, dusty red landscape, epic military march, wide horizon, sweeping desert vistas, sunlight hitting red dust.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: warhoon_subterranean_dungeon

[[SECTION markdown]]

# Warhoon Subterranean Dungeon

**Role:** Primary setting (imprisonment and psychological horror).

**Architecture/Geography:** Pitch-black subterranean chambers within the city of Warhoon; stone or earthen walls; narrow, oppressive corridors.

**Lighting and Atmosphere:** Absolute sensory deprivation; pitch darkness; heavy, stagnant air; terrifyingly silent except for unseen movements; occasional glint of glowing eyes in the dark.

**Scale Cues:** Enclosed, claustrophobic cells; deep underground voids; sense of infinite, unmapped darkness.

**Prompt Phrases:** Pitch-black subterranean dungeon, oppressive stone darkness, sensory deprivation chamber, abyssal shadows, glowing eyes in darkness, damp underground prison.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
