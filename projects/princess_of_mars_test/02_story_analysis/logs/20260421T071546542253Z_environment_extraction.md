# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:15:46.542253+00:00
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

Chapter id: CH012

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

**Events:**
John Carter is summoned to an audience with Lorquas Ptomel, a Thark leader. Ptomel confronts Carter regarding his status as a prisoner who nonetheless commands respect, and accuses him of plotting an escape with Dejah Thoris. Ptomel warns that while they are a just people, Carter will be executed if he attempts to flee or attacks a Thark in self-defense. Carter realizes that Sarkoja, a powerful female Thark, has been spying on him and reporting his intentions to undermine him.

Driven by the fear that Dejah Thoris will face cruelty at the hands of the brutal Tal Hajus, Carter becomes more determined to escape. Tars Tarkas approaches Carter and offers him quarters in a building near Sola and her charges. Following Thark custom, Carter is granted the spoils of the two chieftains he previously defeated, including weapons, silks, furs, and food. Carter selects a room on the third floor of a large building, positioned strategically to be near Dejah Thoris's quarters, hoping to establish a way to communicate with her. He also assumes responsibility for a retinue of women and youths who were part of the defeated chieftains' retinues, directing them to occupy the upper floors while he settles into his new quarters.

**Characters:**
* **John Carter:** The protagonist; a human prisoner navigating Thark politics and planning an escape to save Dejah Thoris.
* **Lorquas Ptomel:** A Thark leader who confronts Carter with warnings and accusations of plotting escape.
* **Tars Tarkas:** A respected Thark warrior who treats Carter with professional courtesy and assists him in finding quarters.
* **Sarkoja (Mentioned):** A powerful female Thark and trusted lieutenant of Tars Tarkas, identified by Carter as the one sabotaging him.
* **Tal Hajus (Mentioned):** A brutal and feared Thark leader described as a personification of cruelty.
* **Dejah Thoris (Mentioned):** The Red Martian princess held captive by the Tharks; the primary motivation for Carter's escape plans.

**Settings:**
* **The Audience Chamber:** Where Lorquas Ptomel delivers his warning to Carter.
* **The Plaza/Thark Settlement:** A large area containing various buildings, courtyards, and streets where the Thark warriors and their retinues reside.
* **Carter's New Quarters:** A room on the third floor of a multi-story building overlooking an overgrown central court filled with fountains and statuary.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [thark_audience_chamber](thark_audience_chamber)
- [thark_settlement_plaza](thark_settlement_plaza)
- [thark_residential_quarters](thark_residential_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_audience_chamber

[[SECTION markdown]]

# Thark Audience Chamber

**Role:** Primary (Political/Confrontational)

**Architecture/Geography:** A formal, imposing chamber designed for leadership gatherings and judicial warnings. Likely features high ceilings and heavy, martial aesthetics consistent with Thark culture.

**Lighting/Atmosphere:** Formal, tense, and authoritative. Shadows likely play heavily across the space to emphasize the gravity of the confrontation.

**Scale/Anchors:** Large-scale seating or platforms for leaders; central floor area for prisoners or petitioners.

**Prompt Phrases:** imposing thark hall, martial architecture, high ceilings, shadows of authority, formal stone chamber.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_settlement_plaza

[[SECTION markdown]]

# Thark Settlement Plaza

**Role:** Secondary (Transit/Social)

**Architecture/Geography:** A sprawling urban expanse containing various buildings, courtyards, and streets. It serves as the hub for warrior residences and retinue movements.

**Lighting/Atmosphere:** Open-air, dusty, and bustling with the movement of Thark warriors and their retinues. Exposed to Martian sky.

**Scale/Anchors:** Wide streets, interconnected courtyards, various multi-story structures.

**Prompt Phrases:** sprawling martian settlement, thark urban plaza, stone streets, courtyard networks, martial outpost.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_residential_quarters

[[SECTION markdown]]

# Thark Residential Quarters

**Role:** Primary (Character/Strategic)

**Architecture/Geography:** A multi-story stone building featuring upper-floor rooms overlooking a central courtyard. The courtyard is characterized by overgrown vegetation, fountains, and ancient statuary.

**Lighting/Atmosphere:** Dappled sunlight through overgrowth; a mix of domestic interior and lush, decaying exterior garden views.

**Scale/Anchors:** Third-floor balcony/windows, central fountain, weathered statues, overgrown greenery.

**Prompt Phrases:** multi-story thark building, overlooking overgrown courtyard, martian fountains, ancient statuary, third-floor stone room, lush decay.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
