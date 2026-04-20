# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:46:45.507992+00:00
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

**Setting:** An interior chamber within a Martian building, overlooking a plaza.

**Characters:**
- **The Protagonist:** An Earthman fighting for survival.
- **The Watch-thing:** The protagonist's loyal, multi-legged, beast-like guardian.
- **The Ape-creatures:** Two massive, ten-to-fifteen-foot tall, four-armed creatures resembling gorillas.
- **Tars Tarkas:** A Martian warrior who respects physical prowess.
- **Sola:** A Martian woman who shows compassion and solicitude toward the protagonist.
- **Martian Warriors:** A group of warriors observing the combat.

**Events:**
- The protagonist is pinned by one massive ape-creature while its mate approaches with a stone cudgel to kill him.
- The protagonist's "watch-thing" intervenes, engaging the second ape in a brutal, life-or-death struggle.
- As the watch-thing begins to lose the fight due to the ape's superior strength, the protagonist seizes the fallen cudgel and kills the first ape by crushing its skull.
- The second ape, enraged by its mate's death, charges the protagonist. Despite the overwhelming odds, the protagonist stays to defend his dying watch-thing.
- Using earthly combat tactics (striking the chin and stomach), the protagonist incapacitates the second ape and kills it with the cudgel.
- Tars Tarkas, Sola, and a group of warriors arrive, having witnessed the fight. They applaud the protagonist's bravery, viewing his combat as a display of high status.
- While Sola shows genuine concern for the protagonist's well-being, the other Martians laugh at the spectacle.
- A Martian warrior attempts to execute the wounded watch-thing; the protagonist intervenes by striking the warrior's arm, preventing the shot.
- Tars Tarkas allows the protagonist to keep his beast, and the protagonist departs into the plaza with Sola and his loyal creature.
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
- [martian_plaza](martian_plaza)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_interior_chamber

[[SECTION markdown]]

# Martian Interior Chamber

**Role:** Primary setting (combat arena).

**Architecture or Geography:** An interior chamber within a Martian building, featuring elevated vantage points overlooking a plaza. The space is designed for observation and public spectacle.

**Lighting and Atmosphere Cues:** High-contrast lighting; likely harsh sunlight filtering through openings or artificial Martian illumination; atmosphere of tension, dust, and sudden violence.

**Scale Cues and Recurring Environmental Anchors:** Large enough to accommodate ten-to-fifteen-foot ape-creatures and multi-legged beasts; presence of stone weaponry (cudgels); overlooking ledge/balcony structure.

**Descriptive Noun Phrases:** Martian architectural interior, stone combat chamber, elevated observation balcony, dust-mote filled air, brutalist Martian masonry.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plaza

[[SECTION markdown]]

# Martian Plaza

**Role:** Transit setting / Secondary background.

**Architecture or Geography:** An expansive open-air public space situated immediately outside the interior chambers.

**Lighting and Atmosphere Cues:** Bright, exposed Martian sky; wide-open vistas; sense of scale and communal gathering.

**Scale Cues and Recurring Environmental Anchors:** Vast horizontal expanse; transition point between indoor structures and the wider Martian landscape.

**Descriptive Noun Phrases:** Expansive Martian plaza, sun-drenched public square, open planetary courtyard, vast stone-paved expanse.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
