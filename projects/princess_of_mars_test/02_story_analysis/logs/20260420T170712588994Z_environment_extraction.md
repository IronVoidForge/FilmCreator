# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:07:12.589499+00:00
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

**Setting:** A chamber within a Martian building, near a window overlooking a plaza.

**Characters:**
* **The Narrator:** An Earthman who uses both primitive weapons and Earthly boxing tactics to survive.
* **The Watch-thing:** The narrator's loyal, multi-legged, monstrous pet/guardian.
* **The Ape-creatures:** Two massive (10-15ft tall), four-armed, gorilla-like beings with high physical strength.
* **Tars Tarkas:** A Martian warrior who observes the narrator's combat.
* **Sola:** A Martian woman who shows compassion and concern for the narrator.
* **Martian Warriors:** A group of onlookers who value physical prowess and witness the fight.

**Events:**
1. **The Initial Capture:** The narrator is pinned to the ground by one of the massive, ape-like creatures while its mate approaches with a stone cudgel to kill him.
2. **The First Battle:** The narrator's "watch-thing" attacks the second ape to save the narrator. A brutal struggle ensues between the two beasts; the watch-thing is severely wounded and nearly choked to death by the ape's immense strength.
3. **The Narrator's Intervention:** Driven by loyalty to his pet, the narrator uses a fallen cudgel to crush the skull of the first ape. 
4. **The Second Battle:** The mate of the deceased ape returns in a rage. The narrator initially considers fleeing but chooses to stay and defend his wounded beast. Using Earthly boxing techniques—specifically punches to the chin and stomach—the narrator manages to knock the creature off balance and finish it with the cudgel.
5. **The Arrival of Allies:** Tars Tarkas, Sola, and a group of warriors arrive, having witnessed the fight. They are impressed by the narrator's combat skill, though their reaction is rooted more in admiration of his strength than true friendship.
6. **An Act of Compassion:** A Martian warrior attempts to execute the wounded watch-thing with a pistol. The narrator intervenes, physically stopping the warrior's arm and preventing the shot. This act of mercy confuses the Martians but solidifies the narrator's bond with both Sola and his loyal beast.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

- martian_chamber
- martian_plaza

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_chamber

[[SECTION markdown]]

# Martian Chamber

**Role:** Primary setting for combat and confrontation.

**Architecture or Geography:** Interior chamber within a Martian building; features large viewing windows overlooking external vistas.

**Lighting and Atmosphere Cues:** High-tension, gritty atmosphere; lighting influenced by natural light from windows and heavy shadows cast by massive creatures during struggle.

**Scale Cues and Recurring Environmental Anchors:** Large interior volume capable of accommodating 15ft tall ape-creatures; anchored by a prominent window overlooking the plaza.

**Useful Descriptive Noun Phrases:** Stone chamber, viewing window, combat arena, Martian masonry, interior fighting floor.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_plaza

[[SECTION markdown]]

# Martian Plaza

**Role:** Secondary setting (visible through chamber windows).

**Architecture or Geography:** Open-air public square or plaza adjacent to the primary building.

**Lighting and Atmosphere Cues:** Bright, exposed, and communal; atmosphere of observation and gathering for Martian onlookers.

**Scale Cues and Recurring Environmental Anchors:** Expansive outdoor space; serves as a wide assembly ground for groups of Martian warriors.

**Useful Descriptive Noun Phrases:** Wide plaza, Martian courtyard, assembly square, exterior viewing area.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
