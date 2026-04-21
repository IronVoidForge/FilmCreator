# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:58:10.048507+00:00
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
* **The Protagonist:** An Earthman fighting for survival.
* **The Watch-thing:** A loyal, multi-legged, beast-like creature that serves as the protagonist's guardian.
* **The Ape-men:** Two massive, ten-to-fifteen-foot tall creatures with four limbs and gorilla-like features.
* **Tars Tarkas:** A Martian warrior who respects physical prowess.
* **Sola:** A Martian woman who shows compassion and solicitude toward the protagonist.
* **Martian Warriors:** A group of warriors following Tars Tarkas.

**Events:**
* **The Ambush:** The protagonist is pinned by one massive ape-man while its mate approaches with a stone cudgel to kill him.
* **The Battle of the Beasts:** The protagonist's watch-thing intervenes, engaging the second ape-man in a ferocious struggle. As the watch-thing begins to succumb to the ape-man's strength, the protagonist seizes the fallen cudgel and kills the first ape-man by crushing its skull.
* **The Second Duel:** The mate of the slain ape-man returns in a rage. Despite the overwhelming physical disadvantage, the protagonist decides to stay and fight to honor his dying guardian. Using earthly combat tactics—striking the creature's chin and stomach—the protagonist manages to incapacitate and kill the second monster.
* **The Arrival of the Martians:** Tars Tarkas, Sola, and a group of warriors arrive, having witnessed the fight. They applaud the protagonist's bravery, viewing his combat skills as a source of high regard.
* **Conflict over the Beast:** The Martian warriors attempt to execute the wounded watch-thing. The protagonist intervenes by striking a warrior's arm, preventing the shot. 
* **Resolution:** Tars Tarkas allows the protagonist to keep his beast. The protagonist realizes he has found two allies on Mars: Sola, who provides emotional care, and his loyal beast, who provides protection.
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

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_interior_chamber

[[SECTION markdown]]

# Martian Interior Chamber

**Role:** Primary combat setting / Secondary observation point.

**Architecture or Geography:** An interior chamber within a larger Martian structure, featuring an overlook that faces a wide plaza. The space is designed for large-scale occupants, accommodating massive creatures and warriors.

**Lighting and Atmosphere Cues:** Harsh, dramatic lighting typical of high-stakes combat; open vistas overlooking the exterior plaza suggest a transition between enclosed stone/metal structures and the vast Martian landscape.

**Scale Cues and Recurring Environmental Anchors:** High ceilings and wide floor spans capable of hosting ten-to-fifteen-foot tall ape-men; an overlook/balcony feature providing a vantage point over a public square or plaza.

**Descriptive Noun Phrases:** Martian architectural chamber, elevated plaza overlook, stone-hewn interior, vast combat arena, high-ceilinged Martian hall, overlooking courtyard.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
