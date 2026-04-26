# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:48:23.316774+00:00
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
John Carter is summoned to an audience with Lorquas Ptomel, the Tharkian leader. Ptomel confronts Carter regarding his ambiguous status as a prisoner who commands respect, and accuses him of plotting an escape with a red Martian prisoner. Ptomel warns that while they are a just people, Carter may be killed in self-defense or if caught attempting to escape. He emphasizes the importance of delivering the red girl (Dejah Thoris) to Tal Hajus. 

Carter realizes that Sarkoja, a powerful female figure within the Thark community, has been spying on him and reporting his words to Ptomel. Fearing for Dejah Thoris's safety at the hands of the brutal Tal Hajus, Carter becomes more determined to escape. Tars Tarkas later approaches Carter and assists him in selecting quarters in a large building near Sola and the other prisoners. Carter chooses a room on the third floor to be closer to Dejah Thoris. He receives his spoils of war—weapons, silks, furs, and food—delivered by the retinues of the chieftains he defeated. Carter organizes these people into a functional unit to manage his new living quarters.

**Characters:**
* **John Carter:** The protagonist; a human/Earthman acting as a Tharkian chieftain.
* **Lorquas Ptomel:** A Tharkian leader who confronts Carter with warnings and accusations.
* **Tars Tarkas:** A respected Thark warrior who treats Carter with professional courtesy and assists him with housing.
* **Sarkoja:** An influential female figure (implied to be the source of the reports against Carter).
* **Dejah Thoris:** The red Martian princess; mentioned as the primary motivation for Carter's escape plans.
* **Tal Hajus:** A brutal and feared leader of the red Martians, described by Sola as a monster.

**Settings:**
* **The Audience Chamber:** Where Carter meets with Lorquas Ptomel.
* **The Plaza/Thark City:** A large area featuring buildings, courtyards, and streets where various warriors and animals are quartered.
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
- [thark_city_plaza](thark_city_plaza)
- [carters_quarters_building](carters_quarters_building)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_audience_chamber

[[SECTION markdown]]

# Thark Audience Chamber

**Role:** Primary (Political/Narrative)

**Architecture/Geography:** A formal, imposing chamber designed for leadership confrontation and judgment. Likely features large-scale stone or metal structures suitable for Tharkian chieftains.

**Lighting/Atmosphere:** Formal, tense, and authoritative. High-contrast lighting emphasizing the power dynamics between leaders.

**Scale/Anchors:** Large scale; designed to accommodate high-ranking warriors and leaders like Lorquas Ptomel.

**Prompt Phrases:** imposing chieftain's hall, formal Martian audience chamber, Tharkian leadership seat, stone authority chamber.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_plaza

[[SECTION markdown]]

# Thark City Plaza

**Role:** Secondary (Transit/Social)

**Architecture/Geography:** A vast urban expanse consisting of courtyards, streets, and various buildings. Serves as a hub for warriors, animals, and retinues.

**Lighting/Atmosphere:** Open-air, bustling, and utilitarian. Exposed to the Martian sky; atmosphere of organized military or tribal activity.

**Scale/Anchors:** Large scale urban center; wide streets and communal gathering areas.

**Prompt Phrases:** sprawling Tharkian city plaza, Martian warrior encampment, ancient red planet courtyard, busy Tharkian streetscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: carters_quarters_building

[[SECTION markdown]]

# Carter's Quarters Building

**Role:** Primary (Living/Domestic)

**Architecture/Geography:** A multi-story stone building. The specific setting is a third-floor room overlooking an overgrown central court featuring fountains and statuary.

**Lighting/Atmosphere:** Overgrown, ancient, and somewhat neglected; sunlight filtering through courtyard greenery and fountain spray.

**Scale/Anchors:** Multi-story verticality; recurring anchor of the central courtyard with fountains and statues.

**Prompt Phrases:** third-floor Martian apartment, overgrown courtyard with fountains, ancient stone residential building, view of Martian statuary and gardens.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
