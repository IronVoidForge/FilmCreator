# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:03:36.073429+00:00
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

Chapter id: CH006

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

**Setting:** An interior chamber within a building in a Martian city, leading out to a plaza.

**Characters:**
- **The Protagonist:** An Earthman fighting for survival.
- **The Watch-thing:** A multi-legged, loyal, and fierce creature that serves as the protagonist's guardian.
- **The Bull Ape & Mate:** Large (10-15ft), humanoid, ape-like creatures with four arms and immense strength.
- **Tars Tarkas:** A Martian warrior who observes and respects the protagonist's combat skills.
- **Sola:** A Martian woman who shows genuine concern and solicitude for the protagonist.
- **Martian Warriors:** A group of warriors who value physical prowess and witness the protagonist's fight.

**Events:**
- The protagonist is pinned by a large, ape-like creature while its mate approaches with a stone cudgel.
- The protagonist's "watch-thing" intervenes, engaging the mate in a brutal, life-or-death struggle.
- As the watch-thing begins to lose the fight against the mate, the protagonist uses the fallen cudgel to crush the skull of the first ape.
- The second ape (the mate) returns in a rage; the protagonist initially considers fleeing but decides to stay and defend his dying guardian.
- Using earthly combat tactics—striking the chin and stomach—the protagonist manages to incapacitate the enraged ape and kills it with the cudgel.
- Tars Tarkas, Sola, and other warriors arrive, having witnessed the fight; they applaud the protagonist's bravery, viewing him through the lens of Martian values (strength/skill).
- Sola shows empathy by checking the protagonist for injuries, contrasting with the laughter of the other warriors.
- A Martian warrior attempts to execute the wounded watch-thing, but the protagonist intervenes by striking the warrior's arm, preventing the shot.
- The protagonist leaves the building with Sola and his loyal beast, having secured two unlikely allies on Mars.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index

- [martian_interior_chamber](martian_interior_chamber)
- [martian_city_plaza](martian_city_plaza)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_interior_chamber

[[SECTION markdown]]

# Martian Interior Chamber

**Role:** Primary combat setting.

**Architecture/Geography:** An enclosed interior chamber within a Martian urban structure; contains hard surfaces suitable for heavy combat and the use of stone implements.

**Lighting/Atmosphere:** Enclosed, potentially dim or shadowed depending on structural openings; atmosphere is charged with high-tension violence and physical struggle.

**Scale/Anchors:** Large enough to accommodate multi-armed humanoid creatures (10-15ft) and a multi-legged guardian beast; anchored by the presence of heavy stone cudgels and debris from combat.

**Prompt Phrases:** enclosed martian chamber, brutal combat interior, stone floor, shadows and harsh light, large scale humanoid arena.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_city_plaza

[[SECTION markdown]]

# Martian City Plaza

**Role:** Secondary/Transit setting.

**Architecture/Geography:** An open urban space outside a building; part of a larger Martian city structure.

**Lighting/Atmosphere:** Open-air Martian atmosphere; transition from the enclosed chamber to the wider cityscape; populated by observing crowds and warriors.

**Scale/Anchors:** Expansive urban scale; anchored by surrounding buildings and the presence of groups of Martian warriors.

**Prompt Phrases:** martian city plaza, open urban expanse, alien architecture, gathering place, dusty martian atmosphere.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
