# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:24:10.493653+00:00
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

**Summary:**
John Carter is summoned to an audience with Lorquas Ptomel, a Thark leader. Ptomel issues a stern warning: while Carter has earned respect through combat, he remains an alien prisoner. He is accused of plotting escape with Dejah Thoris (the "red girl") and warns that if Carter attempts to flee with her, he will be killed. Ptomel emphasizes the importance of delivering Dejah Thoris safely to Tal Hajus, a brutal and powerful leader. 

Carter realizes that Sarkoja, a high-ranking female Thark, has been spying on him and reporting his intentions to undermine him. This encounter intensifies Carter's resolve to escape, driven by fear of what the predatory Tal Hajus might do to Dejah Thoris.

Following the meeting, Tars Tarkas assists Carter in establishing quarters. Following Thark custom, Carter is granted the spoils of the two chieftains he defeated, including weapons, silks, and furs. He moves into a third-floor apartment in a large building, strategically choosing a room close to Dejah Thoris's quarters to facilitate potential communication. Carter also takes responsibility for the retinues (women and youths) belonging to the fallen chieftains, organizing them within his new living quarters while reflecting on the cold, communal, and loveless social structures of the green Martians.

**Characters:**
* **John Carter:** The protagonist; a Thark chieftain by prowess but a prisoner by status; determined to rescue Dejah Thoris.
* **Lorquas Ptomel:** A Thark leader; stern, just by Martian standards, and wary of Carter's influence.
* **Tars Tarkas:** A respected Thark warrior who treats Carter with professional courtesy and assists him with logistics.
* **Sarkoja (Mentioned):** A powerful female Thark and informant who is actively working against Carter.
* **Tal Hajus (Mentioned):** A feared, brutal leader to whom Dejah Thoris is being delivered.
* **Dejah Thoris (Mentioned):** The captive red Jeddak princess; the primary motivation for Carter's escape plans.

**Settings:**
* **The Audience Chamber:** Where Carter meets Lorquas Ptomel.
* **The Plaza/Thark City:** A complex of buildings and streets featuring overgrown courts, fountains, and statuary from a lost era of Martian civilization.
* **Carter’s New Quarters:** A third-floor apartment in a large building overlooking an enormous central court filled with animals and vegetation.
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
- [carters_apartment_quarters](carters_apartment_quarters)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_audience_chamber

[[SECTION markdown]]

# Thark Audience Chamber

**Role:** Primary (Narrative Pivot)

**Architecture/Geography:** A formal, imposing chamber designed for leadership and judgment. Likely features heavy, stone-like structures suited to the Thark aesthetic.

**Lighting/Atmosphere:** Stern, authoritative, and high-tension. The atmosphere is one of political scrutiny and cold Martian justice.

**Scale/Anchors:** Large enough to accommodate a leader and his retinue; designed to dwarf those being summoned for judgment.

**Prompt Phrases:** imposing martial chamber, Thark leadership hall, stern stone architecture, formal audience setting, high-tension meeting space.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_city_plaza

[[SECTION markdown]]

# Thark City Plaza

**Role:** Secondary (World Building)

**Architecture/Geography:** A complex network of streets and buildings. Features overgrown courts, ancient fountains, and weathered statuary from a lost era of Martian civilization.

**Lighting/Atmosphere:** Ancient, decaying grandeur; a mix of martial utility and the remnants of a sophisticated, vanished culture.

**Scale/Anchors:** Expansive urban layout; recurring anchors include crumbling fountains and monumental statues.

**Prompt Phrases:** overgrown Martian plaza, ancient ruins, weathered stone statuary, decaying civilization, Thark city streets, abandoned fountains.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: carters_apartment_quarters

[[SECTION markdown]]

# Carter's Apartment Quarters

**Role:** Secondary (Character Base)

**Architecture/Geography:** A third-floor apartment within a large, multi-story building. The room overlooks an enormous central court filled with vegetation and animals.

**Lighting/Atmosphere:** Communal yet cold; functional living space decorated with spoils of war (silks, furs, weapons). High vantage point overlooking a bustling courtyard.

**Scale/Anchors:** Elevated urban dwelling; large central courtyard anchor; interior cluttered with trophies and communal retinues.

**Prompt Phrases:** third-floor Martian apartment, elevated urban quarters, view of overgrown central court, trophy-laden room, martial spoils, silks and furs decor.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
