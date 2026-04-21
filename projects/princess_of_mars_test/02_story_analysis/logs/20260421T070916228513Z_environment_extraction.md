# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:09:16.228513+00:00
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

**Setting:** A deserted Martian city and its surrounding hills/valleys.

**Events:**
- As the protagonist and Sola prepare to depart from the city, a sudden retreat by the green Martians occurs as twenty large, gray-painted airships approach the valley.
- A fierce battle ensues between the Martian warriors in the city buildings and the approaching fleet. The green Martians utilize highly disciplined, specialized marksmanship to target specific components of the ships (guns, officers, steering gear).
- The Martian fleet is routed, with most ships retreating. One unmanned, damaged vessel drifts erratically toward the city.
- The green warriors intercept the drifting craft, haul it to the ground using grappling hooks, and systematically loot it for arms, jewels, food, and water.
- After stripping the ship, the warriors set it ablaze, creating a massive floating funeral pyre that drifts into the distance.
- The protagonist feels an unexpected sense of melancholy and empathy for the defeated crew of the airships.
- Upon returning to the city plaza, the protagonist spots the prisoner taken from the airship: a beautiful, slender, copper-skinned woman with black hair who resembles Earthly women in form. 
- The woman makes a silent gesture toward the protagonist, seeking help; however, due to his ignorance of Martian customs, he fails to respond, leading her to look at him with dejection and contempt before she is taken away.

**Characters:**
- **The Protagonist:** Observes the battle from a window; feels a strange kinship with the defeated airship crew.
- **Sola:** Accompanies the protagonist.
- **Green Martian Warriors:** Highly organized, disciplined military force.
- **The Prisoner:** A beautiful, slender, copper-skinned female captive from the airship; she appears to be of a different, more refined species than the green Martians.
- **Woola:** The Martian hound accompanying the protagonist.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [deserted_martian_city](#deserted_martian_city)
- [martian_valley_battlefield](#martian_valley_battlefield)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: deserted_martian_city

[[SECTION markdown]]

# Deserted Martian City

**Role:** Primary setting.

**Architecture/Geography:** A collection of stone or metallic buildings, featuring plazas and elevated windows overlooking the surrounding terrain. The structures appear ancient or abandoned prior to the conflict.

**Lighting/Atmosphere:** Harsh Martian light; shadows cast by high-altitude airships; smoke from burning wreckage; a sense of sudden, violent transition from stillness to combat.

**Scale/Anchors:** City plaza; elevated vantage points (windows); narrow streets suitable for ground-based interception.

**Prompt Phrases:** abandoned martian architecture, stone city ruins, urban combat zone, high-altitude airship shadows, dusty plaza, scorched masonry.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_valley_battlefield

[[SECTION markdown]]

# Martian Valley Battlefield

**Role:** Secondary / Transit setting.

**Architecture/Geography:** Wide, open valleys and rolling hills surrounding the city; expansive airspace capable of hosting large-scale fleet maneuvers.

**Lighting/Atmosphere:** Open sky; drifting smoke from a massive floating funeral pyre; erratic movement of damaged vessels; dust kicked up by retreating fleets.

**Scale/Anchors:** Vast valley floor; wide horizon; high-altitude flight paths for gray-painted airships.

**Prompt Phrases:** vast martian valley, sweeping hills, aerial combat landscape, drifting smoke plumes, burning wreckage in sky, expansive desert basin.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
