# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:01:48.092983+00:00
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

Chapter id: CH016

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

After a twenty-day journey across Martian sea bottoms and cultivated lands, John Carter and Dejah Thoris arrive at the ancient city of Thark, the stronghold of the green Tharks ruled by Tal Hajus. Upon settling into their quarters, John Carter confesses his absolute devotion to Dejah Thoris and enlists her help in planning an escape. They attempt to persuade Sola to join them, promising her sanctuary among the red men of Helium, but she expresses deep skepticism regarding the safety of their route. Using a diamond to map out waterways on a marble floor, the group decides on a northern route to bypass Thark territory.

The escape is set for that night, but as John Carter prepares his thoats and moves toward the rendezvous point, he realizes the plan has been compromised after overhearing mounted warriors discussing their intentions. While maneuvering through the city to find the women, Carter climbs into Dejah Thoris's quarters and overhears a Thark chieftain instructing warriors to ambush him and imprison him in the vaults for Tal Hajus. He also learns that Sola has already been taken into custody.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [city_of_thark](city_of_thark)
- [thark_quarters_and_vaults](thark_quarters_and_vaults)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: city_of_thark

[[SECTION markdown]]

# City of Thark

**Role:** Primary setting / Stronghold

**Architecture & Geography:** An ancient, sprawling Martian stronghold characterized by massive stone structures and fortified urban layouts. The city is built to accommodate the green Tharks, featuring wide thoroughfares suitable for mounted warriors and large-scale military movements.

**Lighting & Atmosphere:** Harsh, imposing, and militaristic. The atmosphere is heavy with the presence of constant surveillance and the tension of a high-security stronghold.

**Scale & Anchors:** Massive scale; characterized by wide streets, fortified walls, and central hubs for Thark leadership. Recurring anchors include large stone plazas and military encampments within the city limits.

**Prompt Phrases:** ancient Martian stone city, massive green Thark stronghold, sprawling megalithic architecture, militaristic urban landscape, heavy stone fortifications.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: thark_quarters_and_vaults

[[SECTION markdown]]

# Thark Quarters and Vaults

**Role:** Secondary setting / Interior tension zones

**Architecture & Geography:** Interior living quarters for the Thark elite/warriors, transitioning into subterranean or heavily fortified stone vaults used for imprisonment. Features marble floors suitable for mapping and heavy, enclosed chambers.

**Lighting & Atmosphere:** Dimly lit, claustrophobic, and secretive. The atmosphere shifts from the domestic tension of the quarters to the cold, oppressive darkness of the prison vaults.

**Scale & Anchors:** Human-scale (or Thark-scale) rooms; recurring anchors include marble floors used for tactical planning and heavy stone doors/vault entrances.

**Prompt Phrases:** dim stone interior, marble floor chambers, subterranean stone vaults, claustrophobic prison cells, ancient Martian masonry.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
