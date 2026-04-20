# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:49:44.904661+00:00
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
- As the protagonist and Sola attempt to return home after an incubator ceremony, a sudden retreat is ordered by the green Martians as twenty large, gray aerial craft approach the city.
- A fierce battle ensues between the green Martian warriors (utilizing high-accuracy ground fire from buildings) and the approaching fleet. The Martian warriors target specific components of the ships: sighting apparatus, gunners, officers, and steering gear.
- The fleet is routed, leaving only one crippled, unmanned vessel drifting erratically toward the city.
- Green Martian warriors intercept the drifting craft, haul it to the ground using grappling hooks, and systematically loot it of weapons, silks, jewels, and food/water.
- After looting, the warriors set the vessel ablaze, sending it drifting away as a "floating funeral pyre."
- The protagonist experiences a profound sense of melancholy and empathy for the defeated crew, despite their status as enemies.
- Upon returning to the city plaza, the protagonist spots the prisoner taken from the craft: a beautiful, slender, copper-skinned woman with black hair who resembles Earthly women in form.
- The woman makes a silent gesture toward the protagonist, seeking help; however, due to his ignorance of Martian customs, he fails to respond, leading her to look upon him with dejection and contempt before she is taken away.

**Characters:**
- **The Protagonist:** Observes the battle from a window; feels an unexpected empathy for the defeated aerial crew.
- **Sola:** A green Martian accompanying the protagonist.
- **Green Martian Warriors:** Highly disciplined, tactical combatants with specialized roles in warfare.
- **The Prisoner:** A beautiful, slender, copper-skinned female captive from the aerial craft; she appears to be of a different, perhaps more "humanoid" race than the green Martians.
- **Woola:** The Martian hound following the protagonist.

**Key Elements for Extraction:**
- The tactical volley of the green Martian warriors against the airships.
- The looting and subsequent destruction (burning) of the derelict craft.
- The visual encounter/eye contact between the Protagonist and the female prisoner.
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
- [aerial_battle_skyline](#aerial_battle_skyline)
- [derelict_craft_crash_site](#derelict_craft_crash_site)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: deserted_martian_city

[[SECTION markdown]]

# Deserted Martian City

**Role:** Primary setting.

**Architecture or Geography:** A sprawling, desolate urban landscape characterized by buildings used as tactical vantage points; contains a central city plaza.

**Lighting and Atmosphere Cues:** Harsh Martian light; atmosphere of tension and sudden military mobilization; transition from quiet desertion to active combat zone.

**Scale Cues and Recurring Environmental Anchors:** High-accuracy ground fire originating from building heights; wide plazas for prisoner processing; windows overlooking the surrounding hills/valleys.

**Prompt Phrases:** Desolate Martian urban sprawl, tactical stone architecture, high-altitude vantage points, central city plaza, dusty Martian cityscape.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: aerial_battle_skyline

[[SECTION markdown]]

# Aerial Battle Skyline

**Role:** Secondary setting / Transit.

**Architecture or Geography:** The open Martian sky above the city and surrounding hills; populated by large, gray aerial craft.

**Lighting and Atmosphere Cues:** Chaotic combat lighting; streaks of high-accuracy ground fire; smoke from damaged vessels; sense of overwhelming scale as fleets approach.

**Scale Cues and Recurring Environmental Anchors:** Twenty large gray ships; drifting unmanned vessels; verticality between the ground warriors and the approaching fleet.

**Prompt Phrases:** Martian sky battle, massive gray aerial craft, streaks of projectile fire, high-altitude combat, drifting derelict ships.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: derelict_craft_crash_site

[[SECTION markdown]]

# Derelict Craft Crash Site

**Role:** Secondary setting.

**Architecture or Geography:** A localized ground site where a crippled vessel has been hauled down via grappling hooks; rugged Martian terrain near the city outskirts.

**Lighting and Atmosphere Cues:** Intense heat from burning wreckage; "floating funeral pyre" effect; smoke, embers, and looting activity under harsh sunlight.

**Scale Cues and Recurring Environmental Anchors:** A single large, crippled vessel; heavy grappling lines; scattered loot (silks, jewels, weapons).

**Prompt Phrases:** Burning spaceship wreckage, Martian ground site, smoldering metal hull, glowing funeral pyre, debris-strewn terrain.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
