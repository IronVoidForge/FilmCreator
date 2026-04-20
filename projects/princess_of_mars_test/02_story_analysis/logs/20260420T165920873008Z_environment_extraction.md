# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:59:20.873008+00:00
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

Chapter id: CH005

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

**Characters:**
* **The Protagonist:** A human captive with exceptional jumping abilities and an adventurous spirit.
* **Sola:** A Martian female who shows the protagonist kindness, sympathy, and care.
* **The Watchdog:** A ferocious, incredibly fast, and loyal Martian beast used for hunting and protection.
* **The Ape-like Creature:** A massive, white, hairless, and intimidating creature encountered at the end of the chapter.

**Settings:**
* **The Prisoner's Chamber:** A room decorated with beautiful murals depicting Martian landscapes (mountains, rivers, gardens) but devoid of living creatures.
* **Martian City Streets:** Deserted streets characterized by sudden temperature shifts and illuminated by moons or primitive oil lamps.
* **Building Ledge/Window:** A high vantage point thirty feet above the ground used during an escape attempt.

**Key Events:**
1. **The Guarded Captivity:** After Sola leaves him, the protagonist is left alone with a ferocious Martian watchdog that guards the threshold of his room.
2. **Observations of Mars:** While alone, the protagonist examines the room's murals and learns about Martian biology, specifically a large plant that produces milk-like liquid. He also notes the extreme cold of Martian nights and the influence of the two moons on nocturnal illumination.
3. **The Escape Attempt:** Seeking to test the watchdog's temperament, the protagonist attempts to leave the room. The dog follows him through the streets but suddenly turns to block his exit from the city limits with a ferocious charge.
4. **The High-Speed Chase:** A pursuit ensues where the protagonist uses his agility to evade the incredibly fast beast, eventually leaping into a high window of a nearby building.
5. **The Ambush:** Just as the protagonist believes he has reached safety on the windowsill, he is violently grabbed and dragged back into a room by a colossal, white, ape-like creature.
````

## Raw Response
````text
[[FILMCREAMENT_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- prisoners_chamber
- martian_city_streets
- building_ledge_window

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: prisoners_chamber

[[SECTION markdown]]

# Prisoners Chamber

**Role:** Primary setting (captivity).

**Architecture or Geography:** An interior chamber featuring expansive, detailed murals depicting Martian landscapes including mountains, rivers, and gardens. The room contains a threshold guarded by a predatory watchdog and features biological specimens such as milk-producing plants.

**Lighting and Atmosphere:** Quiet and observant; atmosphere of isolation punctuated by the presence of a large predator at the entrance.

**Scale Cues and Recurring Environmental Anchors:** Large-scale landscape murals; the heavy, watchful presence of the Martian watchdog at the doorway; milk-secreting flora.

**Descriptive Noun Phrases:** "landscape-painted walls", "milk-producing Martian flora", "guarded chamber threshold", "verdant mural landscapes".

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_city_streets

[[SECTION markdown]]

# Martian City Streets

**Role:** Transit setting (escape).

**Architecture or Geography:** Deserted urban streets and thoroughfares leading toward the city limits.

**Lighting and Atmosphere:** Extreme nocturnal temperature shifts; illumination provided by two moons and primitive, flickering oil lamps.

**Scale Cues and Recurring Environmental Anchors:** Wide, empty street corridors; sudden drops in temperature; the boundary of the city limits.

**Descriptive Noun Phrases:** "moonlit deserted streets", "flickering oil lamps", "nocturnal Martian chill", "desolate urban thoroughfares".

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: building_ledge_window

[[SECTION markdown]]

# Building Ledge Window

**Role:** Transit setting (escape/pursuit).

**Architecture or Geography:** A high-altitude window and ledge situated thirty feet above the ground level.

**Lighting and Atmosphere:** Exposed, high-vantage point; atmosphere of high-stakes pursuit and verticality.

**Scale Cues and Recurring Environmental Anchors:** A significant thirty-foot vertical drop; a high masonry ledge used as an escape anchor.

**Descriptive Noun Phrases:** "elevated window ledge", "thirty-foot vertical descent", "high-altitude building aperture".

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
