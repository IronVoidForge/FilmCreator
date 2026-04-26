# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:42:31.669804+00:00
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

Chapter id: CH008

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

**Setting:** A deserted Martian city and the surrounding valleys/hills.

**Events:**
- As the protagonist and Sola attempt to return home after an incubator ceremony, a sudden retreat by the green Martians reveals the approach of twenty large, gray-painted aerial vessels.
- The green Martian warriors engage the fleet in a highly organized and deadly skirmish from the city's buildings, targeting specific components of the ships (gunners, steering gear, etc.).
- The Martian fleet is routed; most ships retreat, but one unmanned, damaged vessel drifts erratically toward the city.
- The green Martians capture the drifting craft, strip it of all valuables (arms, silks, food, water), and then set it ablaze, sending it drifting away as a funeral pyre.
- The protagonist experiences a profound sense of melancholy and empathy for the defeated crew, feeling a strange connection to these unknown foemen.
- Upon returning to the plaza, the protagonist spots the prisoner taken from the craft: a beautiful, slender, reddish-copper skinned woman who resembles an Earthly woman in form.
- The woman makes a silent gesture toward the protagonist, seeking help; however, due to his ignorance of Martian customs, he fails to respond, leaving her to be dragged away into captivity with a look of dejection and contempt.

**Characters:**
- **The Protagonist:** An Earthman observing the conflict with growing empathy for the non-green Martians.
- **Sola:** A companion to the protagonist.
- **Green Martian Warriors:** Highly disciplined, organized combatants capable of rapid tactical retreats and precise warfare.
- **The Captive Woman:** A beautiful, slender, reddish-copper skinned female from the aerial fleet; she appears physically distinct from the green Martians.
- **Woola:** The protagonist's hound.

**Key Elements for Extraction:**
- The aerial battle between the Martian warriors and the gray vessels.
- The systematic looting and destruction of the drifting ship.
- The visual encounter/eye contact between the Protagonist and the Captive Woman in the plaza.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [deserted_martian_city_plaza](deserted_martian_city_plaza)
- [aerial_battle_skies](aerial_battle_skies)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: deserted_martian_city_plaza

[[SECTION markdown]]

# Deserted Martian City Plaza

**Role:** Primary setting for character interaction and social observation.

**Architecture or Geography:** An open urban plaza within a deserted Martian city; features stone-like surfaces and structures capable of providing cover for combatants.

**Lighting and Atmosphere Cues:** Harsh, direct Martian light; atmosphere of tension and sudden melancholy following the battle; dust and smoke from drifting wreckage.

**Scale Cues and Recurring Environmental Anchors:** Large open spaces designed for gatherings; proximity to city buildings used as tactical vantage points by warriors.

**Descriptive Noun Phrases:** Deserted urban plaza, Martian stone architecture, wide ceremonial space, dusty city square, combat-scarred ruins.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: aerial_battle_skies

[[SECTION markdown]]

# Aerial Battle Skies

**Role:** Secondary setting for large-scale conflict and movement.

**Architecture or Geography:** The open Martian sky above the valleys and hills; high altitude airspace.

**Lighting and Atmosphere Cues:** High-contrast lighting; smoke trails from damaged vessels; flickering light from burning wreckage/funeral pyres; chaotic atmosphere of skirmish and retreat.

**Scale Cues and Recurring Environmental Anchors:** Vast, expansive sky; presence of large gray-painted aerial vessels; drifting unmanned craft.

**Descriptive Noun Phrases:** Expansive Martian sky, high-altitude combat zone, drifting aerial vessels, burning ship pyre, smoke-streaked atmosphere.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
